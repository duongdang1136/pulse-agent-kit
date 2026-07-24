"""Data models for provider-independent Pulse workflow packages."""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping

def _strings(value: Any) -> tuple[str, ...]:
    return tuple(str(x).strip() for x in (value or []) if str(x).strip())

@dataclass(frozen=True, slots=True)
class WorkflowInputs:
    required: tuple[str, ...] = field(default_factory=tuple)
    optional: tuple[str, ...] = field(default_factory=tuple)

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any] | None) -> "WorkflowInputs":
        value = value or {}
        return cls(_strings(value.get("required")), _strings(value.get("optional")))

@dataclass(frozen=True, slots=True)
class WorkflowStage:
    id: str
    agent: str
    skills: tuple[str, ...]
    consumes: tuple[str, ...]
    output: str
    handoff_to: str | None = None
    optional: bool = False

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any]) -> "WorkflowStage":
        handoff = value.get("handoff_to")
        return cls(
            id=str(value.get("id", "")).strip(),
            agent=str(value.get("agent", "")).strip(),
            skills=_strings(value.get("skills")),
            consumes=_strings(value.get("consumes")),
            output=str(value.get("output", "")).strip(),
            handoff_to=str(handoff).strip() if handoff is not None else None,
            optional=bool(value.get("optional", False)),
        )

@dataclass(frozen=True, slots=True)
class WorkflowInteraction:
    clarification_required_when: tuple[str, ...] = field(default_factory=tuple)

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any] | None) -> "WorkflowInteraction":
        value = value or {}
        return cls(_strings(value.get("clarification_required_when")))

@dataclass(frozen=True, slots=True)
class WorkflowManifest:
    schema: int
    name: str
    display_name: str
    version: str
    description: str
    instructions: str
    inputs: WorkflowInputs
    stages: tuple[WorkflowStage, ...]
    interaction: WorkflowInteraction
    tags: tuple[str, ...]
    manifest_path: Path | None = field(default=None, compare=False)

    @property
    def package_dir(self) -> Path | None:
        return self.manifest_path.parent if self.manifest_path else None

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any], *, manifest_path: Path | None = None) -> "WorkflowManifest":
        return cls(
            schema=int(value.get("schema", 0)),
            name=str(value.get("name", "")).strip(),
            display_name=str(value.get("display_name", "")).strip(),
            version=str(value.get("version", "")).strip(),
            description=str(value.get("description", "")).strip(),
            instructions=str(value.get("instructions", "")).strip(),
            inputs=WorkflowInputs.from_mapping(value.get("inputs")),
            stages=tuple(WorkflowStage.from_mapping(x) for x in (value.get("stages") or []) if isinstance(x, Mapping)),
            interaction=WorkflowInteraction.from_mapping(value.get("interaction")),
            tags=_strings(value.get("tags")),
            manifest_path=manifest_path,
        )
