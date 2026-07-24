from __future__ import annotations

import json
from pathlib import Path

from pulse.rag.chunking import choose_policy, chunk_document
from pulse.rag.pipeline import build_index, query_index


def _knowledge(tmp_path: Path, text: str) -> Path:
    root = tmp_path / "knowledge" / "projects" / "demo"
    (root / "pages").mkdir(parents=True)
    (root / "pages" / "doc.md").write_text("---\nid: doc\n---\n\n" + text, encoding="utf-8")
    (root / "pages" / "README.md").write_text("# README without frontmatter", encoding="utf-8")
    (root / "manifest.json").write_text(json.dumps({
        "schema_version": 2,
        "project": "demo",
        "documents": [{
            "id": "doc", "title": "Doc", "project": "demo", "source": "doc.txt",
            "page": "pages/doc.md", "checksum": "source-checksum", "source_type": "txt",
            "status": "imported", "created_at": "2026-01-01", "updated_at": "2026-01-01",
            "index_fingerprint": "",
        }],
    }), encoding="utf-8")
    return root


def test_adaptive_policy_ranges() -> None:
    assert choose_policy(2_500).strategy == "whole"
    assert choose_policy(10_000).strategy == "recursive"
    assert choose_policy(50_000).strategy == "hierarchical"
    assert choose_policy(150_000).strategy == "streaming_hierarchical"


def test_hierarchical_chunking_creates_parent_and_leaf_chunks() -> None:
    text = "# One\n\n" + ("alpha beta gamma. " * 1800) + "\n\n# Two\n\n" + ("delta epsilon. " * 1800)
    chunks = chunk_document("doc", text, choose_policy(len(text)))
    assert any(chunk.level == "section" for chunk in chunks)
    assert any(chunk.level == "leaf" for chunk in chunks)


def test_build_is_manifest_driven_and_incremental(tmp_path: Path) -> None:
    root = _knowledge(tmp_path, "Playback event ad_start contains session_id and timestamp. " * 100)
    first = build_index(root, "demo", provider="hash")
    second = build_index(root, "demo", provider="hash")
    assert first.indexed == 1
    assert second.indexed == 0
    assert second.skipped == 1
    assert first.chunks > 0
    chunks = (root / ".rag" / "chunks.jsonl").read_text(encoding="utf-8")
    assert "README without frontmatter" not in chunks


def test_hybrid_query_and_context_budget(tmp_path: Path) -> None:
    root = _knowledge(tmp_path, "The exact tracking event is ad_start. It includes ad_id and playback_session_id. " * 100)
    build_index(root, "demo", provider="hash")
    results = query_index(root, "ad_start playback_session_id", top_k=5, context_chars=3000)
    assert results
    assert "ad_start" in results[0].text
    assert sum(len(item.text) for item in results) <= 3000


def test_legacy_import_manifest_is_migrated(tmp_path: Path) -> None:
    root = tmp_path / "legacy"
    (root / "pages").mkdir(parents=True)
    (root / "pages" / "legacy.md").write_text("Legacy tracking specification", encoding="utf-8")
    (root / "imports.json").write_text(json.dumps([{
        "document_id": "legacy", "source": "legacy.txt", "page": "any/pages/legacy.md",
        "status": "imported", "updated": "2026-01-01",
    }]), encoding="utf-8")
    report = build_index(root, "demo", provider="hash")
    assert report.indexed == 1
    assert (root / "manifest.json").exists()
