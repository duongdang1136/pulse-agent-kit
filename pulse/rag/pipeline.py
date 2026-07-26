from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

from .chunking import choose_policy, chunk_document
from .embedding import create_embedder
from .manifest import load_manifest, save_manifest
from .store import cosine, keyword_score, read_jsonl, write_jsonl


@dataclass(frozen=True)
class BuildReport:
    indexed: int
    skipped: int
    removed: int
    chunks: int
    provider: str
    model: str


@dataclass(frozen=True)
class SearchResult:
    chunk_id: str
    document_id: str
    score: float
    text: str
    source: str
    heading: str
    level: str


def build_index(knowledge_root: Path, project: str, *, provider: str = "hash", model: str | None = None, batch_size: int = 64, force: bool = False) -> BuildReport:
    manifest_path = knowledge_root / "manifest.json"
    if not manifest_path.exists() and (knowledge_root / "imports.json").exists():
        # Automatic Milestone 2 migration; README and unregistered Markdown are never scanned.
        legacy = json.loads((knowledge_root / "imports.json").read_text(encoding="utf-8"))
        migrated = {"schema_version": 2, "project": project, "documents": []}
        for item in legacy if isinstance(legacy, list) else []:
            doc_id = item.get("document_id")
            if not doc_id:
                continue
            page = Path(item.get("page", ""))
            migrated["documents"].append({
                "id": doc_id, "title": doc_id.replace("-", " ").title(), "project": project,
                "source": item.get("source", ""), "page": f"pages/{page.name}",
                "checksum": "", "source_type": Path(item.get("source", "")).suffix.lstrip("."),
                "status": "imported", "created_at": item.get("updated", ""),
                "updated_at": item.get("updated", ""), "index_fingerprint": "",
            })
        save_manifest(manifest_path, migrated)
    manifest = load_manifest(manifest_path, project)
    embedder = create_embedder(provider, model)
    fingerprint = f"autorig-v2:{embedder.name}:{embedder.model}:adaptive-v1"
    chunks_path = knowledge_root / ".rag" / "chunks.jsonl"
    vectors_path = knowledge_root / ".rag" / "vectors.jsonl"
    old_chunks = read_jsonl(chunks_path)
    old_vectors = read_jsonl(vectors_path)
    chunks_by_doc: dict[str, list[dict[str, Any]]] = {}
    vectors_by_doc: dict[str, list[dict[str, Any]]] = {}
    for row in old_chunks:
        chunks_by_doc.setdefault(row["document_id"], []).append(row)
    for row in old_vectors:
        vectors_by_doc.setdefault(row["document_id"], []).append(row)

    indexed = skipped = removed = 0
    active_ids: set[str] = set()
    for document in manifest["documents"]:
        doc_id = document.get("id") or document.get("document_id")
        if not doc_id or document.get("status") == "deleted":
            continue
        if document.get("rag_enabled") is False:
            continue
        active_ids.add(doc_id)
        page = _resolve_path(knowledge_root, document.get("page") or document.get("path", ""))
        if not page.exists():
            document["status"] = "missing"
            continue
        body = _read_normalized_body(page)
        checksum = document.get("checksum") or hashlib.sha256(body.encode("utf-8")).hexdigest()
        unchanged = (
            not force
            and document.get("checksum") == checksum
            and document.get("index_fingerprint") == fingerprint
            and doc_id in chunks_by_doc
            and doc_id in vectors_by_doc
        )
        if unchanged:
            skipped += 1
            continue
        policy = choose_policy(len(body))
        chunks = chunk_document(doc_id, body, policy)
        chunk_rows = [chunk.to_dict() for chunk in chunks]
        vector_rows: list[dict[str, Any]] = []
        for start in range(0, len(chunks), batch_size):
            batch = chunks[start:start + batch_size]
            vectors = embedder.embed_batch([chunk.text for chunk in batch])
            for chunk, vector in zip(batch, vectors):
                vector_rows.append({"chunk_id": chunk.id, "document_id": doc_id, "vector": vector})
        chunks_by_doc[doc_id] = chunk_rows
        vectors_by_doc[doc_id] = vector_rows
        document.update({
            "checksum": checksum,
            "status": "indexed",
            "updated_at": date.today().isoformat(),
            "char_count": len(body),
            "chunk_strategy": policy.strategy,
            "chunk_count": len(chunks),
            "index_fingerprint": fingerprint,
            "embedding_provider": embedder.name,
            "embedding_model": embedder.model,
        })
        indexed += 1

    for stale in set(chunks_by_doc) - active_ids:
        chunks_by_doc.pop(stale, None)
        vectors_by_doc.pop(stale, None)
        removed += 1

    all_chunks = [row for doc_id in sorted(chunks_by_doc) for row in chunks_by_doc[doc_id]]
    all_vectors = [row for doc_id in sorted(vectors_by_doc) for row in vectors_by_doc[doc_id]]
    write_jsonl(chunks_path, all_chunks)
    write_jsonl(vectors_path, all_vectors)
    (knowledge_root / ".rag" / "index.json").write_text(json.dumps({
        "schema_version": 2,
        "project": project,
        "provider": embedder.name,
        "model": embedder.model,
        "dimensions": embedder.dimensions,
        "chunk_count": len(all_chunks),
        "fingerprint": fingerprint,
    }, indent=2) + "\n", encoding="utf-8")
    save_manifest(manifest_path, manifest)
    return BuildReport(indexed, skipped, removed, len(all_chunks), embedder.name, embedder.model)


def query_index(knowledge_root: Path, query: str, *, top_k: int = 5, candidate_k: int = 40, context_chars: int = 12_000) -> list[SearchResult]:
    index_path = knowledge_root / ".rag" / "index.json"
    if not index_path.exists():
        raise FileNotFoundError("RAG index not found. Run: pulse rag build <project>")
    config = json.loads(index_path.read_text(encoding="utf-8"))
    embedder = create_embedder(config["provider"], config.get("model"))
    query_vector = embedder.embed_batch([query])[0]
    chunks = {row["id"]: row for row in read_jsonl(knowledge_root / ".rag" / "chunks.jsonl")}
    vectors = read_jsonl(knowledge_root / ".rag" / "vectors.jsonl")
    manifest = load_manifest(knowledge_root / "manifest.json", config.get("project", ""))
    docs = {(item.get("id") or item.get("document_id")): item for item in manifest["documents"]}
    scored = []
    for row in vectors:
        chunk = chunks.get(row["chunk_id"])
        if not chunk:
            continue
        semantic = max(0.0, cosine(query_vector, row["vector"]))
        keyword = keyword_score(query, chunk["text"])
        score = 0.65 * semantic + 0.35 * keyword
        scored.append((score, chunk))
    scored.sort(key=lambda item: item[0], reverse=True)

    results: list[SearchResult] = []
    used_chars = 0
    seen_text: set[str] = set()
    for score, chunk in scored[:candidate_k]:
        signature = hashlib.sha1(chunk["text"][:500].encode("utf-8")).hexdigest()
        if signature in seen_text:
            continue
        if results and used_chars + len(chunk["text"]) > context_chars:
            continue
        seen_text.add(signature)
        used_chars += len(chunk["text"])
        doc = docs.get(chunk["document_id"], {})
        results.append(SearchResult(
            chunk_id=chunk["id"],
            document_id=chunk["document_id"],
            score=score,
            text=chunk["text"],
            source=doc.get("source", doc.get("page", "")),
            heading=chunk.get("heading", ""),
            level=chunk.get("level", "leaf"),
        ))
        if len(results) >= top_k:
            break
    return results


def _resolve_path(knowledge_root: Path, value: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    # Manifest stores repo-relative paths; recover page by basename if needed.
    direct = knowledge_root / path
    if direct.exists():
        return direct
    return knowledge_root / "pages" / path.name


def _read_normalized_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8-sig", errors="replace").replace("\r\n", "\n").replace("\r", "\n")
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5:].strip()
    return text.strip()
