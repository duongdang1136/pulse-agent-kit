from pathlib import Path

from openpyxl import Workbook
from docx import Document

from pulse.cli import main
from pulse.knowledge import import_knowledge, list_knowledge
from pulse.project import create_project


def make_repo(tmp_path: Path) -> Path:
    for folder in ("agents", "knowledge", "scripts"):
        (tmp_path / folder).mkdir()
    (tmp_path / "scripts" / "rag.py").write_text("print('stub')\n", encoding="utf-8")
    return tmp_path


def test_import_markdown_and_text(tmp_path: Path) -> None:
    root = make_repo(tmp_path)
    create_project(root, "FPTPlay")
    source = tmp_path / "incoming"
    source.mkdir()
    (source / "Login Flow.md").write_text("# Login\n\nGuest cannot follow teams.", encoding="utf-8")
    (source / "notes.txt").write_text("Live Activity notes", encoding="utf-8")

    results = import_knowledge(root, "fptplay", source)

    assert len(results) == 2
    assert all(item.status == "imported" for item in results)
    pages = list_knowledge(root, "fptplay")
    assert len(pages) == 2
    login = (root / "knowledge/projects/fptplay/pages/login-flow.md").read_text(encoding="utf-8")
    assert 'source_type: "md"' in login
    assert "Guest cannot follow teams" in login
    assert (root / "projects/fptplay/source-docs/Login Flow.md").exists()


def test_import_docx_and_xlsx(tmp_path: Path) -> None:
    root = make_repo(tmp_path)
    create_project(root, "FPTPlay")

    docx_path = tmp_path / "requirements.docx"
    document = Document()
    document.add_heading("Live Activity", level=1)
    document.add_paragraph("Show match state on lock screen.")
    document.save(docx_path)

    xlsx_path = tmp_path / "rules.xlsx"
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Business Rules"
    sheet.append(["ID", "Rule"])
    sheet.append(["BR-01", "Guest cannot follow a team"])
    workbook.save(xlsx_path)

    assert import_knowledge(root, "fptplay", docx_path)[0].status == "imported"
    assert import_knowledge(root, "fptplay", xlsx_path)[0].status == "imported"
    assert "Show match state" in (root / "knowledge/projects/fptplay/pages/requirements.md").read_text(encoding="utf-8")
    assert "BR-01" in (root / "knowledge/projects/fptplay/pages/rules.md").read_text(encoding="utf-8")


def test_cli_knowledge_import(tmp_path: Path, monkeypatch) -> None:
    root = make_repo(tmp_path)
    create_project(root, "FPTPlay")
    source = tmp_path / "brief.txt"
    source.write_text("Feature brief", encoding="utf-8")
    monkeypatch.chdir(root)

    assert main(["knowledge", "import", "fptplay", str(source)]) == 0
    assert main(["knowledge", "list", "fptplay"]) == 0
    assert main(["doctor"]) == 0
