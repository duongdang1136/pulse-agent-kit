from pathlib import Path
from pulse.workflow import load_workflow_manifest, validate_workflow_package
from tests.unit.test_workflow_manifest import make_workflow

def make_agents(root: Path) -> None:
    for name, skill, template in [("researcher", "synthesize", "Research-Report"), ("itba", "audit", "BA-Document")]:
        agent = root / "agents" / name
        (agent / "skills").mkdir(parents=True)
        (agent / "templates").mkdir()
        (agent / "manifest.yaml").write_text("schema: 2\n", encoding="utf-8")
        (agent / "skills" / f"{skill}.md").write_text("# Skill\n", encoding="utf-8")
        (agent / "templates" / f"{template}.md").write_text("# Template\n", encoding="utf-8")

def test_valid_workflow_package(tmp_path):
    make_agents(tmp_path)
    manifest = load_workflow_manifest(make_workflow(tmp_path))
    assert validate_workflow_package(manifest, repository_root=tmp_path) == []

def test_unknown_handoff_is_rejected(tmp_path):
    package = make_workflow(tmp_path)
    path = package / "manifest.yaml"
    path.write_text(path.read_text(encoding="utf-8").replace("handoff_to: analysis", "handoff_to: missing"), encoding="utf-8")
    issues = validate_workflow_package(load_workflow_manifest(package))
    assert "stage.handoff" in [issue.code for issue in issues]
