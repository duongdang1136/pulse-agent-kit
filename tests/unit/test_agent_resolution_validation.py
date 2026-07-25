from pathlib import Path

from pulse.agent.manifest import load_agent_manifest
from pulse.agent.validator import validate_agent_package
from tests.unit.test_instruction_resolver import make_package


def test_valid_resolution_config(tmp_path):
    manifest = load_agent_manifest(make_package(tmp_path))
    assert validate_agent_package(manifest) == []


def test_rule_cannot_reference_undeclared_skill(tmp_path):
    package = make_package(tmp_path)
    manifest_path = package / "manifest.yaml"
    text = manifest_path.read_text(encoding="utf-8")
    text = text.replace("skills: [screen, heuristic-audit]", "skills: [missing]")
    manifest_path.write_text(text, encoding="utf-8")

    issues = validate_agent_package(load_agent_manifest(package))

    assert "resolution.rule.skill" in [issue.code for issue in issues]
