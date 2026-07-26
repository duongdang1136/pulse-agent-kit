from __future__ import annotations

import json
from pathlib import Path

from pulse.cli import main
from pulse.docs import add_doc, doc_path, init_docs_workspace, list_docs
from pulse.project import create_project
from pulse.rag.pipeline import build_index


def make_repo(tmp_path: Path) -> Path:
    tmp_path.mkdir()
    for folder in ("agents", "knowledge", "scripts"):
        (tmp_path / folder).mkdir()
    return tmp_path


def test_docs_workspace_init(tmp_path: Path) -> None:
    workspace = tmp_path / "docs"

    docs = init_docs_workspace(workspace, "FPTPlay")

    assert docs.project == "fptplay"
    assert (workspace / "fptplay/epics").is_dir()
    assert (workspace / "fptplay/.rag").is_dir()
    manifest = json.loads((workspace / "fptplay/manifest.json").read_text(encoding="utf-8"))
    assert manifest["project"] == "fptplay"
    assert manifest["documents"] == []


def test_add_doc_places_report_by_epic_feature_and_updates_manifest(tmp_path: Path) -> None:
    workspace = tmp_path / "docs"
    source = tmp_path / "ba.md"
    source.write_text("# BA Document\n\nNotification Center rules.", encoding="utf-8")

    record = add_doc(
        workspace,
        "FPTPlay",
        source,
        doc_type="ba-document",
        epic="Notification",
        feature="Notification Center",
        status="reviewed",
    )

    expected = workspace / "fptplay/epics/notification/features/notification-center/ba-document.md"
    assert record.path == expected
    assert expected.exists()
    content = expected.read_text(encoding="utf-8")
    assert 'type: "ba-document"' in content
    assert 'status: "reviewed"' in content
    assert "Notification Center rules." in content
    manifest = json.loads((workspace / "fptplay/manifest.json").read_text(encoding="utf-8"))
    assert manifest["documents"][0]["path"] == "epics/notification/features/notification-center/ba-document.md"
    assert manifest["documents"][0]["rag_enabled"] is True


def test_add_doc_supports_sub_feature_path(tmp_path: Path) -> None:
    workspace = tmp_path / "docs"
    source = tmp_path / "rules.md"
    source.write_text("# Rules\n\nQuiet hours apply.", encoding="utf-8")

    record = add_doc(
        workspace,
        "FPTPlay",
        source,
        doc_type="business-rules",
        epic="Notification",
        feature="Notification Center",
        sub_feature="Push Notification",
    )

    assert record.path == workspace / (
        "fptplay/epics/notification/features/notification-center/"
        "sub-features/push-notification/business-rules.md"
    )


def test_list_docs_can_filter_by_type_and_feature(tmp_path: Path) -> None:
    workspace = tmp_path / "docs"
    ba = tmp_path / "ba.md"
    research = tmp_path / "research.md"
    ba.write_text("# BA", encoding="utf-8")
    research.write_text("# Research", encoding="utf-8")
    add_doc(workspace, "FPTPlay", ba, doc_type="ba-document", epic="Notification", feature="Center")
    add_doc(workspace, "FPTPlay", research, doc_type="research-report", epic="Notification", feature="Center")

    rows = list_docs(workspace, "fptplay", doc_type="ba-document", feature="Center")

    assert len(rows) == 1
    assert rows[0]["type"] == "ba-document"


def test_cli_docs_commands(tmp_path: Path, monkeypatch, capsys) -> None:
    repo = make_repo(tmp_path / "repo")
    workspace = tmp_path / "docs"
    source = tmp_path / "ba.md"
    source.write_text("# BA\n\nGenerated output.", encoding="utf-8")
    monkeypatch.chdir(repo)

    assert main(["docs", "init", str(workspace), "--project", "FPTPlay"]) == 0
    assert main([
        "docs",
        "path",
        str(workspace),
        "--project",
        "FPTPlay",
        "--type",
        "ba-document",
        "--epic",
        "Notification",
        "--feature",
        "Notification Center",
    ]) == 0
    assert main([
        "docs",
        "add",
        str(workspace),
        str(source),
        "--project",
        "FPTPlay",
        "--type",
        "ba-document",
        "--epic",
        "Notification",
        "--feature",
        "Notification Center",
    ]) == 0
    assert main(["docs", "list", str(workspace), "--project", "FPTPlay"]) == 0

    output = capsys.readouterr().out
    assert "notification-center" in output
    assert "ba-document" in output


def test_docs_index_skips_draft_and_indexes_reviewed_docs(tmp_path: Path) -> None:
    workspace = tmp_path / "docs"
    draft = tmp_path / "draft.md"
    reviewed = tmp_path / "reviewed.md"
    draft.write_text("# Draft\n\nNot reviewed yet.", encoding="utf-8")
    reviewed.write_text("# Reviewed\n\nReviewed notification scheduling rules.", encoding="utf-8")
    add_doc(workspace, "FPTPlay", draft, doc_type="ba-document", epic="Notification", feature="Draft")
    add_doc(
        workspace,
        "FPTPlay",
        reviewed,
        doc_type="ba-document",
        epic="Notification",
        feature="Reviewed",
        status="reviewed",
    )

    docs = init_docs_workspace(workspace, "fptplay")
    report = build_index(docs.project_root, docs.project, provider="hash", force=True)

    assert report.indexed == 1
    chunks = (docs.project_root / ".rag/chunks.jsonl").read_text(encoding="utf-8")
    assert "Reviewed notification scheduling" in chunks
    assert "Not reviewed yet" not in chunks


def test_cli_rag_query_can_include_generated_docs(tmp_path: Path, monkeypatch, capsys) -> None:
    repo = make_repo(tmp_path / "repo")
    create_project(repo, "FPTPlay")
    knowledge_root = repo / "knowledge/projects/fptplay"
    (knowledge_root / "pages" / "notification.md").write_text(
        "---\nid: notification\n---\n\nProject notification source context.",
        encoding="utf-8",
    )
    (knowledge_root / "manifest.json").write_text(json.dumps({
        "schema_version": 2,
        "project": "fptplay",
        "documents": [{
            "id": "notification",
            "title": "Notification",
            "project": "fptplay",
            "source": "notification.txt",
            "page": "pages/notification.md",
            "checksum": "",
            "source_type": "txt",
            "status": "imported",
            "created_at": "2026-01-01",
            "updated_at": "2026-01-01",
            "index_fingerprint": "",
        }],
    }), encoding="utf-8")
    build_index(knowledge_root, "fptplay", provider="hash", force=True)

    workspace = tmp_path / "docs"
    report_source = tmp_path / "ba.md"
    report_source.write_text("# BA\n\nGenerated BA document covers quiet hours.", encoding="utf-8")
    add_doc(
        workspace,
        "FPTPlay",
        report_source,
        doc_type="ba-document",
        epic="Notification",
        feature="Notification Center",
        status="reviewed",
    )
    monkeypatch.chdir(repo)

    assert main(["docs", "index", str(workspace), "--project", "FPTPlay"]) == 0
    assert main([
        "rag",
        "query",
        "fptplay",
        "quiet hours",
        "--include-docs",
        "--docs-workspace",
        str(workspace),
        "--top-k",
        "5",
    ]) == 0

    output = capsys.readouterr().out
    assert "scope=docs" in output
    assert "quiet hours" in output


def test_doc_path_returns_canonical_target(tmp_path: Path) -> None:
    target = doc_path(
        tmp_path / "docs",
        "FPTPlay",
        "api-doc",
        "Notification",
        "Notification Center",
        "Push Notification",
    )

    assert target == tmp_path / (
        "docs/fptplay/epics/notification/features/notification-center/"
        "sub-features/push-notification/api-doc.md"
    )
