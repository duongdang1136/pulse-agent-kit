from pathlib import Path

import pytest

from pulse.agent.manifest import load_agent_manifest
from pulse.agent.resolver import ResolutionError, resolve_instructions


def make_package(tmp_path: Path) -> Path:
    package = tmp_path / "itba"
    (package / "skills").mkdir(parents=True)
    (package / "templates").mkdir()
    (package / "agent.md").write_text("# Agent\n", encoding="utf-8")
    for skill in ("audit", "ui-to-spec", "document"):
        (package / "skills" / f"{skill}.md").write_text(
            f"# {skill}\n", encoding="utf-8"
        )
    for template in ("Audit-Report", "BA-Document"):
        (package / "templates" / f"{template}.md").write_text(
            f"# {template}\n", encoding="utf-8"
        )
    (package / "manifest.yaml").write_text(
        """
schema: 2
name: itba
display_name: ITBA
version: 1.0.0
description: Test.
instructions: agent.md
skills: [audit, ui-to-spec, document]
templates: [Audit-Report, BA-Document]
knowledge: {shared: true, project: true}
output: {format: markdown, template: BA-Document}
resolution:
  max_skills: 2
  fallback_skills: [audit]
  default_template: BA-Document
  rules:
    - id: ui-review
      priority: 100
      when_any: [ui, giao diện]
      skills: [ui-to-spec, audit]
      template: Audit-Report
    - id: documentation
      priority: 50
      when_any: [document]
      skills: [document]
      template: BA-Document
tags: [test]
""".strip(),
        encoding="utf-8",
    )
    return package


def test_ui_task_resolves_only_relevant_skills(tmp_path):
    manifest = load_agent_manifest(make_package(tmp_path))

    plan = resolve_instructions(manifest, "Review giao diện màn hình đăng nhập")

    assert plan.skills == ("ui-to-spec", "audit")
    assert plan.template == "Audit-Report"
    assert plan.matched_rules == ("ui-review",)
    assert [item.kind for item in plan.instructions] == [
        "agent", "skill", "skill", "template"
    ]


def test_unmatched_task_uses_fallback(tmp_path):
    manifest = load_agent_manifest(make_package(tmp_path))

    plan = resolve_instructions(manifest, "Do the assigned work")

    assert plan.skills == ("audit",)
    assert plan.template == "BA-Document"
    assert plan.matched_rules == ()


def test_explicit_skill_has_precedence_and_limit(tmp_path):
    manifest = load_agent_manifest(make_package(tmp_path))

    plan = resolve_instructions(
        manifest,
        "Review UI and write document",
        requested_skills=("document",),
    )

    assert plan.skills == ("document", "ui-to-spec")


def test_unknown_explicit_skill_fails(tmp_path):
    manifest = load_agent_manifest(make_package(tmp_path))

    with pytest.raises(ResolutionError):
        resolve_instructions(manifest, "Task", requested_skills=("unknown",))
