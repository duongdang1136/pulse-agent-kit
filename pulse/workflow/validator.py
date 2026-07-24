"""Validation for Pulse workflow packages."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable
from .models import WorkflowManifest

_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_VERSION = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")

@dataclass(frozen=True, slots=True)
class WorkflowValidationIssue:
    code: str
    message: str
    path: Path | None = None
    severity: str = "error"

class WorkflowValidationError(ValueError):
    def __init__(self, issues: Iterable[WorkflowValidationIssue]) -> None:
        self.issues = tuple(issues)
        super().__init__("\n".join(f"[{x.code}] {x.message}" for x in self.issues))

def validate_workflow_package(manifest: WorkflowManifest, *, repository_root: Path | None = None, strict: bool = False) -> list[WorkflowValidationIssue]:
    issues: list[WorkflowValidationIssue] = []
    def add(code: str, message: str, path: Path | None = None) -> None:
        issues.append(WorkflowValidationIssue(code, message, path))

    if manifest.schema != 1: add("schema", "Workflow manifest must declare schema: 1.")
    if not manifest.name: add("name.required", "Workflow name is required.")
    elif not _NAME.fullmatch(manifest.name): add("name.format", "Workflow name must use lowercase kebab-case.")
    if not manifest.display_name: add("display_name.required", "display_name is required.")
    if not manifest.version: add("version.required", "version is required.")
    elif not _VERSION.fullmatch(manifest.version): add("version.format", "version must use semantic versioning.")
    if not manifest.description: add("description.required", "description is required.")
    if not manifest.inputs.required: add("inputs.required", "At least one required workflow input is needed.")
    if set(manifest.inputs.required) & set(manifest.inputs.optional): add("inputs.duplicate", "Inputs cannot be both required and optional.")
    if not manifest.stages: add("stages.required", "At least one workflow stage is required.")

    ids: set[str] = set()
    for stage in manifest.stages:
        if not stage.id: add("stage.id", "Every workflow stage requires an id.")
        elif stage.id in ids: add("stage.duplicate", f"Duplicate workflow stage id '{stage.id}'.")
        ids.add(stage.id)
        if not stage.agent: add("stage.agent", f"Stage '{stage.id}' requires an agent.")
        if not stage.output: add("stage.output", f"Stage '{stage.id}' requires an output template.")

    for stage in manifest.stages:
        if stage.handoff_to and stage.handoff_to not in ids:
            add("stage.handoff", f"Stage '{stage.id}' hands off to unknown stage '{stage.handoff_to}'.")

    if manifest.package_dir is None:
        add("package.path", "manifest_path is unavailable.")
    else:
        path = manifest.package_dir / manifest.instructions
        if manifest.instructions and not path.is_file():
            add("instructions.missing", f"Missing workflow instructions: {manifest.instructions}", path)

    if repository_root is not None:
        for stage in manifest.stages:
            agent_dir = repository_root / "agents" / stage.agent
            if not (agent_dir / "manifest.yaml").is_file():
                add("stage.agent.missing", f"Stage '{stage.id}' references missing agent '{stage.agent}'.", agent_dir / "manifest.yaml")
                continue
            for skill in stage.skills:
                path = agent_dir / "skills" / (skill if skill.lower().endswith(".md") else f"{skill}.md")
                if not path.is_file(): add("stage.skill.missing", f"Stage '{stage.id}' references missing skill '{skill}'.", path)
            path = agent_dir / "templates" / (stage.output if stage.output.lower().endswith(".md") else f"{stage.output}.md")
            if stage.output and not path.is_file(): add("stage.output.missing", f"Stage '{stage.id}' references missing output template '{stage.output}'.", path)

    if strict and issues:
        raise WorkflowValidationError(issues)
    return issues
