"""Validation for Pulse agent instruction packages."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable

from .models import AgentManifest

_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_VERSION_PATTERN = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")


@dataclass(frozen=True, slots=True)
class ValidationIssue:
    code: str
    message: str
    path: Path | None = None
    severity: str = "error"


class AgentValidationError(ValueError):
    def __init__(self, issues: Iterable[ValidationIssue]) -> None:
        self.issues = tuple(issues)
        super().__init__("\n".join(f"[{x.code}] {x.message}" for x in self.issues))


def _md(package_dir: Path, folder: str, name: str) -> Path:
    filename = name if name.lower().endswith(".md") else f"{name}.md"
    return package_dir / folder / filename


def validate_agent_package(
    manifest: AgentManifest,
    *,
    strict: bool = False,
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []

    def add(code: str, message: str, path: Path | None = None) -> None:
        issues.append(ValidationIssue(code, message, path))

    if manifest.schema != 2:
        add("schema", "Agent manifest must declare schema: 2.")
    if not manifest.name:
        add("name.required", "Agent name is required.")
    elif not _NAME_PATTERN.fullmatch(manifest.name):
        add("name.format", "Agent name must use lowercase kebab-case.")
    if not manifest.display_name:
        add("display_name.required", "display_name is required.")
    if not manifest.version:
        add("version.required", "version is required.")
    elif not _VERSION_PATTERN.fullmatch(manifest.version):
        add("version.format", "version must use semantic versioning.")
    if not manifest.description:
        add("description.required", "description is required.")
    if not manifest.instructions:
        add("instructions.required", "instructions is required.")
    if len(set(manifest.skills)) != len(manifest.skills):
        add("skills.duplicate", "skills must not contain duplicates.")
    if len(set(manifest.templates)) != len(manifest.templates):
        add("templates.duplicate", "templates must not contain duplicates.")
    if manifest.output.template and manifest.output.template not in manifest.templates:
        add("output.template", "output.template must also appear in templates.")

    resolution = manifest.resolution
    if resolution.max_skills < 1:
        add("resolution.max_skills", "resolution.max_skills must be at least 1.")
    if len(set(resolution.fallback_skills)) != len(resolution.fallback_skills):
        add("resolution.fallback_skills", "fallback_skills must not contain duplicates.")
    for skill in resolution.fallback_skills:
        if skill not in manifest.skills:
            add(
                "resolution.skill",
                f"Fallback skill '{skill}' is not declared in skills.",
            )
    if (
        resolution.default_template is not None
        and resolution.default_template not in manifest.templates
    ):
        add(
            "resolution.template",
            f"Default template '{resolution.default_template}' is not declared.",
        )

    rule_ids: set[str] = set()
    for rule in resolution.rules:
        if not rule.id:
            add("resolution.rule.id", "Every resolution rule requires an id.")
        elif rule.id in rule_ids:
            add("resolution.rule.duplicate", f"Duplicate resolution rule id '{rule.id}'.")
        rule_ids.add(rule.id)

        if not rule.when_any:
            add(
                "resolution.rule.when_any",
                f"Resolution rule '{rule.id}' requires at least one keyword.",
            )
        for skill in rule.skills:
            if skill not in manifest.skills:
                add(
                    "resolution.rule.skill",
                    f"Rule '{rule.id}' references undeclared skill '{skill}'.",
                )
        if rule.template is not None and rule.template not in manifest.templates:
            add(
                "resolution.rule.template",
                f"Rule '{rule.id}' references undeclared template '{rule.template}'.",
            )

    package_dir = manifest.package_dir
    if package_dir is None:
        add("package.path", "manifest_path is unavailable.")
    else:
        instruction_path = package_dir / manifest.instructions
        if manifest.instructions and not instruction_path.is_file():
            add("instructions.missing", f"Missing {manifest.instructions}", instruction_path)
        for skill in manifest.skills:
            path = _md(package_dir, "skills", skill)
            if not path.is_file():
                add("skill.missing", f"Missing skills/{path.name}", path)
        for template in manifest.templates:
            path = _md(package_dir, "templates", template)
            if not path.is_file():
                add("template.missing", f"Missing templates/{path.name}", path)

    if strict and issues:
        raise AgentValidationError(issues)
    return issues
