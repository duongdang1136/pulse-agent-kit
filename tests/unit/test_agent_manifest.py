from pathlib import Path
import pytest

from pulse.agent.manifest import AgentManifestError, load_agent_manifest


def make_package(tmp_path: Path) -> Path:
    package = tmp_path / "example"
    (package / "skills").mkdir(parents=True)
    (package / "templates").mkdir()
    (package / "agent.md").write_text("# Agent\n", encoding="utf-8")
    (package / "skills/analyze.md").write_text("# Analyze\n", encoding="utf-8")
    (package / "templates/Report.md").write_text("# Report\n", encoding="utf-8")
    (package / "manifest.yaml").write_text(
        '''
schema: 2
name: example
display_name: Example
version: 1.0.0
description: Example agent.
instructions: agent.md
skills: [analyze]
templates: [Report]
knowledge: {shared: true, project: true}
output: {format: markdown, template: Report}
tags: [example]
'''.strip(),
        encoding="utf-8",
    )
    return package


def test_load_manifest(tmp_path):
    manifest = load_agent_manifest(make_package(tmp_path))
    assert manifest.name == "example"
    assert manifest.skills == ("analyze",)
    assert manifest.output.template == "Report"


def test_manifest_is_llm_independent(tmp_path):
    manifest = load_agent_manifest(make_package(tmp_path))
    assert not hasattr(manifest, "provider")
    assert not hasattr(manifest, "model")
    assert not hasattr(manifest, "temperature")


def test_reject_non_mapping_yaml(tmp_path):
    path = tmp_path / "manifest.yaml"
    path.write_text("- invalid\n", encoding="utf-8")
    with pytest.raises(AgentManifestError):
        load_agent_manifest(path)
