"""Data models for provider-independent Pulse agent packages."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping


def _strings(value: Any) -> tuple[str, ...]:
    return tuple(str(item).strip() for item in (value or []) if str(item).strip())


@dataclass(frozen=True, slots=True)
class KnowledgeConfig:
    shared: bool = True
    project: bool = True

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any] | None) -> "KnowledgeConfig":
        value = value or {}
        return cls(
            shared=bool(value.get("shared", True)),
            project=bool(value.get("project", True)),
        )


@dataclass(frozen=True, slots=True)
class OutputConfig:
    format: str = "markdown"
    template: str | None = None

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any] | None) -> "OutputConfig":
        value = value or {}
        template = value.get("template")
        return cls(
            format=str(value.get("format", "markdown")).strip(),
            template=str(template).strip() if template is not None else None,
        )


@dataclass(frozen=True, slots=True)
class ResolutionRule:
    """A deterministic rule mapping task language to package resources."""

    id: str
    when_any: tuple[str, ...]
    skills: tuple[str, ...]
    template: str | None = None
    priority: int = 0

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any]) -> "ResolutionRule":
        template = value.get("template")
        return cls(
            id=str(value.get("id", "")).strip(),
            when_any=_strings(value.get("when_any")),
            skills=_strings(value.get("skills")),
            template=str(template).strip() if template is not None else None,
            priority=int(value.get("priority", 0)),
        )


@dataclass(frozen=True, slots=True)
class ResolutionConfig:
    """Instruction-selection policy declared by an agent package."""

    max_skills: int = 3
    fallback_skills: tuple[str, ...] = field(default_factory=tuple)
    default_template: str | None = None
    rules: tuple[ResolutionRule, ...] = field(default_factory=tuple)

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any] | None) -> "ResolutionConfig":
        value = value or {}
        default_template = value.get("default_template")
        rules = tuple(
            ResolutionRule.from_mapping(item)
            for item in (value.get("rules") or [])
            if isinstance(item, Mapping)
        )
        return cls(
            max_skills=int(value.get("max_skills", 3)),
            fallback_skills=_strings(value.get("fallback_skills")),
            default_template=(
                str(default_template).strip()
                if default_template is not None
                else None
            ),
            rules=rules,
        )


@dataclass(frozen=True, slots=True)
class AgentManifest:
    schema: int
    name: str
    display_name: str
    version: str
    description: str
    instructions: str
    skills: tuple[str, ...] = field(default_factory=tuple)
    templates: tuple[str, ...] = field(default_factory=tuple)
    knowledge: KnowledgeConfig = field(default_factory=KnowledgeConfig)
    output: OutputConfig = field(default_factory=OutputConfig)
    resolution: ResolutionConfig = field(default_factory=ResolutionConfig)
    tags: tuple[str, ...] = field(default_factory=tuple)
    category: str | None = None
    manifest_path: Path | None = field(default=None, compare=False)

    @property
    def package_dir(self) -> Path | None:
        return self.manifest_path.parent if self.manifest_path else None

    @classmethod
    def from_mapping(
        cls,
        value: Mapping[str, Any],
        *,
        manifest_path: Path | None = None,
    ) -> "AgentManifest":
        return cls(
            schema=int(value.get("schema", 0)),
            name=str(value.get("name", "")).strip(),
            display_name=str(value.get("display_name", "")).strip(),
            version=str(value.get("version", "")).strip(),
            description=str(value.get("description", "")).strip(),
            instructions=str(value.get("instructions", "")).strip(),
            skills=_strings(value.get("skills")),
            templates=_strings(value.get("templates")),
            knowledge=KnowledgeConfig.from_mapping(value.get("knowledge")),
            output=OutputConfig.from_mapping(value.get("output")),
            resolution=ResolutionConfig.from_mapping(value.get("resolution")),
            tags=_strings(value.get("tags")),
            category=(
                str(value["category"]).strip()
                if value.get("category") is not None
                else None
            ),
            manifest_path=manifest_path,
        )
