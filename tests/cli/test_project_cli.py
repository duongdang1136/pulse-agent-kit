from pathlib import Path

from pulse.cli import main
from pulse.project import create_project, list_projects, read_project, slugify


def make_repo(tmp_path: Path) -> Path:
    for folder in ("agents", "knowledge", "scripts"):
        (tmp_path / folder).mkdir()
    return tmp_path


def test_slugify() -> None:
    assert slugify("FPT Play") == "fpt-play"
    assert slugify("  Live Activity  ") == "live-activity"


def test_create_project_builds_workspace_and_knowledge(tmp_path: Path) -> None:
    root = make_repo(tmp_path)
    info = create_project(root, "FPTPlay", description="Streaming platform")

    assert info.slug == "fptplay"
    assert (root / "projects/fptplay/project.yaml").exists()
    assert (root / "projects/fptplay/workspace/decisions.yaml").exists()
    assert (root / "knowledge/projects/fptplay/pages/README.md").exists()
    assert (root / "knowledge/projects/fptplay/.rag/index.json").read_text() == "[]\n"

    loaded = read_project(root, "fptplay")
    assert loaded.name == "FPTPlay"
    assert loaded.description == "Streaming platform"
    assert [project.slug for project in list_projects(root)] == ["fptplay"]


def test_cli_project_create_and_doctor(tmp_path: Path, monkeypatch) -> None:
    make_repo(tmp_path)
    monkeypatch.chdir(tmp_path)

    assert main(["project", "create", "FPTPlay"]) == 0
    assert main(["project", "info", "fptplay"]) == 0
    assert main(["doctor"]) == 0


def test_duplicate_project_is_rejected(tmp_path: Path) -> None:
    root = make_repo(tmp_path)
    create_project(root, "FPTPlay")
    try:
        create_project(root, "FPTPlay")
    except FileExistsError:
        pass
    else:
        raise AssertionError("Expected duplicate project to be rejected")
