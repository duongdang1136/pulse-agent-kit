from __future__ import annotations

import json
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 2


def empty_manifest(project: str) -> dict[str, Any]:
    return {"schema_version": SCHEMA_VERSION, "project": project, "documents": []}


def load_manifest(path: Path, project: str) -> dict[str, Any]:
    if not path.exists():
        return empty_manifest(project)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid manifest JSON: {path}") from exc
    if isinstance(payload, list):
        # Milestone 2 migration.
        documents = []
        for item in payload:
            documents.append({
                "id": item.get("document_id", ""),
                "title": item.get("document_id", ""),
                "project": project,
                "source": item.get("source", ""),
                "page": item.get("page", ""),
                "checksum": item.get("checksum", ""),
                "source_type": Path(item.get("source", "")).suffix.lstrip("."),
                "status": item.get("status", "imported"),
                "created_at": item.get("updated", ""),
                "updated_at": item.get("updated", ""),
            })
        payload = empty_manifest(project)
        payload["documents"] = documents
    payload.setdefault("schema_version", SCHEMA_VERSION)
    payload.setdefault("project", project)
    payload.setdefault("documents", [])
    return payload


def save_manifest(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)
