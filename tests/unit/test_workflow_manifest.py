from pathlib import Path
from pulse.workflow import load_workflow_manifest

def make_workflow(tmp_path: Path) -> Path:
    package = tmp_path / "feature-documentation"
    package.mkdir()
    (package / "workflow.md").write_text("# Workflow\n", encoding="utf-8")
    yaml = """schema: 1
name: feature-documentation
display_name: Feature Documentation
version: 1.0.0
description: Test workflow.
instructions: workflow.md
inputs:
  required: [project, feature, user_requirements]
  optional: [constraints]
stages:
  - id: research
    agent: researcher
    skills: [synthesize]
    consumes: [project_sources]
    output: Research-Report
    handoff_to: analysis
  - id: analysis
    agent: itba
    skills: [heuristic-audit]
    consumes: [research.output]
    output: BA-Document
interaction:
  clarification_required_when: [business_decision_missing]
tags: [test]
"""
    (package / "manifest.yaml").write_text(yaml, encoding="utf-8")
    return package

def test_load_workflow_manifest(tmp_path):
    manifest = load_workflow_manifest(make_workflow(tmp_path))
    assert manifest.schema == 1
    assert manifest.name == "feature-documentation"
    assert [stage.id for stage in manifest.stages] == ["research", "analysis"]
    assert manifest.stages[0].handoff_to == "analysis"
