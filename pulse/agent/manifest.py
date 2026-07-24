from __future__ import annotations

from pathlib import Path
from typing import Any
import yaml

from .models import AgentManifest


class AgentManifestError(ValueError):
    pass


def load_agent_manifest(path: str | Path) -> AgentManifest:
    candidate = Path(path)
    manifest_path = candidate / "manifest.yaml" if candidate.is_dir() else candidate
    manifest_path = manifest_path.resolve()

    if not manifest_path.is_file():
        raise AgentManifestError(f"Agent manifest not found: {manifest_path}")

    try:
        raw: Any = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise AgentManifestError(f"Could not read {manifest_path}: {exc}") from exc

    if not isinstance(raw, dict):
        raise AgentManifestError("Agent manifest must contain a YAML mapping.")

    try:
        return AgentManifest.from_mapping(raw, manifest_path=manifest_path)
    except (TypeError, ValueError) as exc:
        raise AgentManifestError(f"Invalid agent manifest: {exc}") from exc
