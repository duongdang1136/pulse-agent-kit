"""Workflow manifest loading."""
from __future__ import annotations
from pathlib import Path
from typing import Any, Mapping
import yaml
from .models import WorkflowManifest

class WorkflowManifestError(ValueError):
    pass

def load_workflow_manifest(path: str | Path) -> WorkflowManifest:
    manifest_path = Path(path)
    if manifest_path.is_dir():
        manifest_path = manifest_path / "manifest.yaml"
    if not manifest_path.is_file():
        raise WorkflowManifestError(f"Workflow manifest does not exist: {manifest_path}")
    try:
        value: Any = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    except (yaml.YAMLError, OSError) as exc:
        raise WorkflowManifestError(f"Could not load workflow manifest {manifest_path}: {exc}") from exc
    if not isinstance(value, Mapping):
        raise WorkflowManifestError(f"Workflow manifest root must be a mapping: {manifest_path}")
    return WorkflowManifest.from_mapping(value, manifest_path=manifest_path)
