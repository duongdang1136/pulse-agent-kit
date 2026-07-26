from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

from pulse.project import slugify

DOC_TYPES = {
    "research-report",
    "knowledge-ingest-note",
    "ba-document",
    "audit-report",
    "api-doc",
    "business-rules",
    "acceptance-criteria",
    "metrics",
    "content-brief",
    "benchmark-report",
}

DOC_STATUSES = {"draft", "reviewed", "approved", "archived"}


@dataclass(frozen=True)
class DocsWorkspace:
    root: Path
    project: str
    project_root: Path
    manifest_path: Path


@dataclass(frozen=True)
class DocRecord:
    id: str
    project: str
    doc_type: str
    status: str
    epic: str
    feature: str
    sub_feature: str
    path: Path
    checksum: str


def init_docs_workspace(workspace: Path, project: str) -> DocsWorkspace:
    project_slug = slugify(project)
    workspace = workspace.expanduser().resolve()
    project_root = workspace / project_slug
    for path in (
        project_root / "epics",
        project_root / ".rag",
    ):
        path.mkdir(parents=True, exist_ok=True)
    manifest_path = project_root / "manifest.json"
    if not manifest_path.exists():
        _save_manifest(manifest_path, _empty_manifest(project_slug))
    return DocsWorkspace(workspace, project_slug, project_root, manifest_path)


def add_doc(
    workspace: Path,
    project: str,
    source: Path,
    *,
    doc_type: str,
    epic: str,
    feature: str,
    sub_feature: str = "",
    status: str = "draft",
    title: str = "",
    overwrite: bool = False,
) -> DocRecord:
    _validate_doc_type(doc_type)
    _validate_status(status)
    docs = init_docs_workspace(workspace, project)
    source = source.expanduser().resolve()
    if not source.exists():
        raise FileNotFoundError(f"Source report was not found: {source}")

    epic_slug = slugify(epic)
    feature_slug = slugify(feature)
    sub_feature_slug = slugify(sub_feature) if sub_feature else ""
    target = doc_path(docs.root, docs.project, doc_type, epic_slug, feature_slug, sub_feature_slug)
    if target.exists() and not overwrite:
        raise FileExistsError(f"Report already exists: {target}")

    raw_content = source.read_text(encoding="utf-8-sig", errors="replace")
    body = _strip_frontmatter(raw_content)
    checksum = hashlib.sha256(raw_content.encode("utf-8")).hexdigest()
    record_id = _doc_id(doc_type, docs.project, epic_slug, feature_slug, sub_feature_slug)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        _render_doc(
            record_id,
            docs.project,
            doc_type,
            status,
            epic_slug,
            feature_slug,
            sub_feature_slug,
            title or _title_from_source(source, doc_type),
            source,
            checksum,
            body,
        ),
        encoding="utf-8",
    )

    manifest = _load_manifest(docs.manifest_path, docs.project)
    existing = {item["id"]: item for item in manifest["documents"] if item.get("id")}
    current = existing.get(record_id, {})
    today = date.today().isoformat()
    current.update({
        "id": record_id,
        "project": docs.project,
        "type": doc_type,
        "status": status,
        "title": title or _title_from_source(source, doc_type),
        "epic": epic_slug,
        "feature": feature_slug,
        "sub_feature": sub_feature_slug,
        "path": target.relative_to(docs.project_root).as_posix(),
        "source": str(source),
        "checksum": checksum,
        "created_at": current.get("created_at", today),
        "updated_at": today,
        "rag_enabled": status in {"reviewed", "approved"},
    })
    existing[record_id] = current
    manifest["documents"] = sorted(existing.values(), key=lambda item: item["id"])
    _save_manifest(docs.manifest_path, manifest)
    return DocRecord(record_id, docs.project, doc_type, status, epic_slug, feature_slug, sub_feature_slug, target, checksum)


def list_docs(
    workspace: Path,
    project: str,
    *,
    doc_type: str | None = None,
    epic: str | None = None,
    feature: str | None = None,
) -> list[dict[str, Any]]:
    docs = init_docs_workspace(workspace, project)
    manifest = _load_manifest(docs.manifest_path, docs.project)
    rows = manifest["documents"]
    if doc_type:
        _validate_doc_type(doc_type)
        rows = [item for item in rows if item.get("type") == doc_type]
    if epic:
        epic_slug = slugify(epic)
        rows = [item for item in rows if item.get("epic") == epic_slug]
    if feature:
        feature_slug = slugify(feature)
        rows = [item for item in rows if item.get("feature") == feature_slug]
    return sorted(rows, key=lambda item: (item.get("epic", ""), item.get("feature", ""), item.get("type", "")))


def doc_path(
    workspace: Path,
    project: str,
    doc_type: str,
    epic: str,
    feature: str,
    sub_feature: str = "",
) -> Path:
    _validate_doc_type(doc_type)
    root = workspace.expanduser().resolve() / slugify(project)
    base = root / "epics" / slugify(epic) / "features" / slugify(feature)
    if sub_feature:
        base = base / "sub-features" / slugify(sub_feature)
    return base / f"{doc_type}.md"


def _validate_doc_type(doc_type: str) -> None:
    if doc_type not in DOC_TYPES:
        raise ValueError("Unsupported doc type. Choose one of: " + ", ".join(sorted(DOC_TYPES)))


def _validate_status(status: str) -> None:
    if status not in DOC_STATUSES:
        raise ValueError("Unsupported doc status. Choose one of: " + ", ".join(sorted(DOC_STATUSES)))


def _empty_manifest(project: str) -> dict[str, Any]:
    return {"schema_version": 1, "project": project, "documents": []}


def _load_manifest(path: Path, project: str) -> dict[str, Any]:
    if not path.exists():
        return _empty_manifest(project)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid docs manifest JSON: {path}") from exc
    payload.setdefault("schema_version", 1)
    payload.setdefault("project", project)
    payload.setdefault("documents", [])
    return payload


def _save_manifest(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)


def _strip_frontmatter(content: str) -> str:
    normalized = content.replace("\r\n", "\n").replace("\r", "\n")
    if normalized.startswith("---\n"):
        end = normalized.find("\n---\n", 4)
        if end != -1:
            return normalized[end + 5:].strip()
    return normalized.strip()


def _render_doc(
    record_id: str,
    project: str,
    doc_type: str,
    status: str,
    epic: str,
    feature: str,
    sub_feature: str,
    title: str,
    source: Path,
    checksum: str,
    body: str,
) -> str:
    today = date.today().isoformat()
    sub_feature_line = f'sub_feature: "{_yaml_escape(sub_feature)}"\n' if sub_feature else 'sub_feature: ""\n'
    return (
        "---\n"
        f'id: "{_yaml_escape(record_id)}"\n'
        f'title: "{_yaml_escape(title)}"\n'
        f'type: "{_yaml_escape(doc_type)}"\n'
        f'project: "{_yaml_escape(project)}"\n'
        f'status: "{_yaml_escape(status)}"\n'
        f'epic: "{_yaml_escape(epic)}"\n'
        f'feature: "{_yaml_escape(feature)}"\n'
        f"{sub_feature_line}"
        f'created_at: "{today}"\n'
        f'updated_at: "{today}"\n'
        f'source_file: "{_yaml_escape(str(source))}"\n'
        f'checksum_sha256: "{checksum}"\n'
        f"rag_enabled: {str(status in {'reviewed', 'approved'}).lower()}\n"
        "---\n\n"
        f"{body}\n"
    )


def _title_from_source(source: Path, doc_type: str) -> str:
    value = source.stem or doc_type
    return value.replace("-", " ").replace("_", " ").strip().title()


def _doc_id(doc_type: str, project: str, epic: str, feature: str, sub_feature: str) -> str:
    parts = [doc_type, project, epic, feature]
    if sub_feature:
        parts.append(sub_feature)
    return "-".join(parts)


def _yaml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')
