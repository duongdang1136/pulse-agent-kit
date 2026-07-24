"""Deterministic instruction resolution for Pulse agent packages.

This module does not call an LLM. It only decides which package files an AI
should read for a task.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import unicodedata

from .models import AgentManifest, ResolutionRule


@dataclass(frozen=True, slots=True)
class ResolvedInstruction:
    kind: str
    path: Path
    reason: str


@dataclass(frozen=True, slots=True)
class ResolutionPlan:
    agent: str
    task: str
    skills: tuple[str, ...]
    template: str | None
    instructions: tuple[ResolvedInstruction, ...]
    matched_rules: tuple[str, ...]


class ResolutionError(ValueError):
    pass


def _normalize(text: str) -> str:
    value = unicodedata.normalize("NFKD", text.casefold())
    value = "".join(char for char in value if not unicodedata.combining(char))
    return re.sub(r"\s+", " ", value).strip()


def _contains_keyword(task: str, keyword: str) -> bool:
    normalized_task = _normalize(task)
    normalized_keyword = _normalize(keyword)
    if not normalized_keyword:
        return False

    # Multi-word phrases and punctuation-bearing tokens are matched as substrings.
    if " " in normalized_keyword or not normalized_keyword.isalnum():
        return normalized_keyword in normalized_task

    return re.search(
        rf"(?<![\w-]){re.escape(normalized_keyword)}(?![\w-])",
        normalized_task,
    ) is not None


def _matching_rules(
    manifest: AgentManifest,
    task: str,
) -> list[ResolutionRule]:
    matched = [
        rule
        for rule in manifest.resolution.rules
        if any(_contains_keyword(task, keyword) for keyword in rule.when_any)
    ]
    return sorted(matched, key=lambda rule: (-rule.priority, rule.id))


def _resolve_markdown(package_dir: Path, folder: str, name: str) -> Path:
    filename = name if name.lower().endswith(".md") else f"{name}.md"
    return package_dir / folder / filename


def resolve_instructions(
    manifest: AgentManifest,
    task: str,
    *,
    requested_skills: tuple[str, ...] | list[str] = (),
    requested_template: str | None = None,
) -> ResolutionPlan:
    """Create an ordered read plan for an AI handoff.

    Resolution precedence:

    1. Explicitly requested skills/template.
    2. Matching manifest rules, ordered by priority.
    3. Manifest fallback skills/default template.
    4. Agent output template.

    Skills are de-duplicated and capped by ``resolution.max_skills``.
    """

    if not task.strip():
        raise ResolutionError("Task must not be empty.")

    package_dir = manifest.package_dir
    if package_dir is None:
        raise ResolutionError("Manifest path is required to resolve package files.")

    known_skills = set(manifest.skills)
    known_templates = set(manifest.templates)

    selected_skills: list[str] = []
    skill_reasons: dict[str, str] = {}

    def add_skill(skill: str, reason: str) -> None:
        if skill not in known_skills:
            raise ResolutionError(
                f"Agent '{manifest.name}' does not declare skill '{skill}'."
            )
        if skill not in selected_skills:
            selected_skills.append(skill)
            skill_reasons[skill] = reason

    for skill in requested_skills:
        add_skill(str(skill).strip(), "explicitly requested")

    matched_rules = _matching_rules(manifest, task)
    for rule in matched_rules:
        for skill in rule.skills:
            add_skill(skill, f"matched resolution rule '{rule.id}'")

    if not selected_skills:
        for skill in manifest.resolution.fallback_skills:
            add_skill(skill, "fallback skill")

    max_skills = manifest.resolution.max_skills
    if max_skills < 1:
        raise ResolutionError("resolution.max_skills must be at least 1.")
    selected_skills = selected_skills[:max_skills]

    template = requested_template
    template_reason = "explicitly requested"

    if template is None:
        for rule in matched_rules:
            if rule.template:
                template = rule.template
                template_reason = f"matched resolution rule '{rule.id}'"
                break

    if template is None:
        template = manifest.resolution.default_template
        template_reason = "resolution default"

    if template is None:
        template = manifest.output.template
        template_reason = "agent output default"

    if template is not None and template not in known_templates:
        raise ResolutionError(
            f"Agent '{manifest.name}' does not declare template '{template}'."
        )

    instructions: list[ResolvedInstruction] = [
        ResolvedInstruction(
            kind="agent",
            path=package_dir / manifest.instructions,
            reason="always read the agent's primary instructions",
        )
    ]

    instructions.extend(
        ResolvedInstruction(
            kind="skill",
            path=_resolve_markdown(package_dir, "skills", skill),
            reason=skill_reasons[skill],
        )
        for skill in selected_skills
    )

    if template is not None:
        instructions.append(
            ResolvedInstruction(
                kind="template",
                path=_resolve_markdown(package_dir, "templates", template),
                reason=template_reason,
            )
        )

    return ResolutionPlan(
        agent=manifest.name,
        task=task,
        skills=tuple(selected_skills),
        template=template,
        instructions=tuple(instructions),
        matched_rules=tuple(rule.id for rule in matched_rules),
    )
