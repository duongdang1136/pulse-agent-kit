from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from pulse import __version__
from pulse.docs import DOC_STATUSES, DOC_TYPES, add_doc, doc_path, init_docs_workspace, list_docs
from pulse.knowledge import KNOWLEDGE_CATEGORIES, import_knowledge, list_knowledge
from pulse.rag import build_index, query_index
from pulse.project import (
    create_project,
    find_repo_root,
    list_projects,
    missing_project_paths,
    read_project,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pulse", description="Pulse Agent Kit CLI")
    parser.add_argument("--version", action="version", version=f"pulse {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    project = sub.add_parser("project", help="Manage BA project workspaces")
    project_sub = project.add_subparsers(dest="project_command", required=True)
    create = project_sub.add_parser("create", help="Create a new project workspace")
    create.add_argument("name", help="Human-readable project name")
    create.add_argument("--slug", help="Folder-safe project identifier")
    create.add_argument("--description", default="", help="Project description")
    project_sub.add_parser("list", help="List existing projects")
    info = project_sub.add_parser("info", help="Show project information")
    info.add_argument("project", help="Project slug or name")

    knowledge = sub.add_parser("knowledge", help="Import and inspect project knowledge")
    knowledge_sub = knowledge.add_subparsers(dest="knowledge_command", required=True)
    knowledge_import = knowledge_sub.add_parser("import", aliases=["add"], help="Import files or a folder")
    knowledge_import.add_argument("project", help="Project slug or name")
    knowledge_import.add_argument("source", type=Path, help="File or folder to import")
    knowledge_import.add_argument("--no-copy", action="store_true", help="Do not copy original files into source-docs")
    knowledge_import.add_argument("--overwrite", action="store_true", help="Overwrite existing normalized pages")
    knowledge_import.add_argument(
        "--category",
        default="Product",
        choices=sorted(KNOWLEDGE_CATEGORIES),
        help="Knowledge category for imported pages",
    )
    knowledge_list = knowledge_sub.add_parser("list", help="List normalized project knowledge pages")
    knowledge_list.add_argument("project", help="Project slug or name")

    docs = sub.add_parser("docs", help="Manage generated project output docs")
    docs_sub = docs.add_subparsers(dest="docs_command", required=True)
    docs_init = docs_sub.add_parser("init", help="Initialize an external docs workspace")
    docs_init.add_argument("workspace", type=Path, help="Docs workspace path, for example ../docs")
    docs_init.add_argument("--project", required=True, help="Project slug or name")

    docs_add = docs_sub.add_parser("add", help="Add or update a generated doc in the docs workspace")
    docs_add.add_argument("workspace", type=Path)
    docs_add.add_argument("source", type=Path, help="Generated markdown report to store")
    docs_add.add_argument("--project", required=True)
    docs_add.add_argument("--type", required=True, choices=sorted(DOC_TYPES), dest="doc_type")
    docs_add.add_argument("--epic", required=True)
    docs_add.add_argument("--feature", required=True)
    docs_add.add_argument("--sub-feature", default="")
    docs_add.add_argument("--status", default="draft", choices=sorted(DOC_STATUSES))
    docs_add.add_argument("--title", default="")
    docs_add.add_argument("--overwrite", action="store_true")

    docs_list = docs_sub.add_parser("list", help="List generated docs in the docs workspace")
    docs_list.add_argument("workspace", type=Path)
    docs_list.add_argument("--project", required=True)
    docs_list.add_argument("--type", choices=sorted(DOC_TYPES), dest="doc_type")
    docs_list.add_argument("--epic")
    docs_list.add_argument("--feature")

    docs_path = docs_sub.add_parser("path", help="Print the target path for a generated doc")
    docs_path.add_argument("workspace", type=Path)
    docs_path.add_argument("--project", required=True)
    docs_path.add_argument("--type", required=True, choices=sorted(DOC_TYPES), dest="doc_type")
    docs_path.add_argument("--epic", required=True)
    docs_path.add_argument("--feature", required=True)
    docs_path.add_argument("--sub-feature", default="")

    docs_index = docs_sub.add_parser("index", help="Build a RAG index for reviewed/approved generated docs")
    docs_index.add_argument("workspace", type=Path)
    docs_index.add_argument("--project", required=True)
    docs_index.add_argument("--provider", default="hash", choices=["hash", "local", "openai"])
    docs_index.add_argument("--model")
    docs_index.add_argument("--batch-size", type=int, default=64)
    docs_index.add_argument("--force", action="store_true")

    rag = sub.add_parser("rag", help="Build or query the existing RAG index")
    rag_sub = rag.add_subparsers(dest="rag_command", required=True)
    rag_build = rag_sub.add_parser("build", help="Build a project's RAG index")
    rag_build.add_argument("project")
    rag_build.add_argument("--provider", default="hash", choices=["hash", "local", "openai"])
    rag_build.add_argument("--model")
    rag_build.add_argument("--batch-size", type=int, default=64)
    rag_build.add_argument("--force", action="store_true")
    rag_query = rag_sub.add_parser("query", help="Query a project's RAG index")
    rag_query.add_argument("project")
    rag_query.add_argument("query")
    rag_query.add_argument("--top-k", type=int, default=5)
    rag_query.add_argument(
        "--include-shared",
        action="store_true",
        help="Query project knowledge and shared knowledge, then merge ranked hits",
    )
    rag_query.add_argument(
        "--include-docs",
        action="store_true",
        help="Query reviewed/approved generated docs together with project knowledge",
    )
    rag_query.add_argument(
        "--docs-workspace",
        type=Path,
        default=Path("../docs"),
        help="Docs workspace path used with --include-docs",
    )

    sub.add_parser("doctor", help="Check repository and project workspace health")
    sub.add_parser("validate", help="Run the repository validator")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        root = find_repo_root()
        if args.command == "project":
            return _handle_project(root, args)
        if args.command == "knowledge":
            return _handle_knowledge(root, args)
        if args.command == "docs":
            return _handle_docs(root, args)
        if args.command == "rag":
            return _handle_rag(root, args)
        if args.command == "doctor":
            return run_doctor(root)
        if args.command == "validate":
            validator = root / "scripts" / "validate_repo.py"
            if not validator.exists():
                print("ERROR: scripts/validate_repo.py was not found", file=sys.stderr)
                return 1
            return subprocess.call([sys.executable, str(validator)], cwd=root)
    except (FileExistsError, FileNotFoundError, RuntimeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 2


def _handle_project(root: Path, args: argparse.Namespace) -> int:
    if args.project_command == "create":
        info = create_project(root, args.name, args.slug, args.description)
        print(f"Created project: {info.name} ({info.slug})")
        print(f"Workspace: {info.workspace_path}")
        print(f"Knowledge: {info.knowledge_path}")
        print(f'Next: pulse knowledge import {info.slug} "<file-or-folder>"')
        return 0
    if args.project_command == "list":
        projects = list_projects(root)
        if not projects:
            print("No projects found.")
            return 0
        for item in projects:
            print(f"{item.slug}\t{item.name}\t{item.created}")
        return 0
    info = read_project(root, args.project)
    print(f"Name: {info.name}\nSlug: {info.slug}\nDescription: {info.description or '-'}")
    print(f"Created: {info.created or '-'}\nWorkspace: {info.workspace_path}\nKnowledge: {info.knowledge_path}")
    return 0


def _handle_knowledge(root: Path, args: argparse.Namespace) -> int:
    if args.knowledge_command in {"import", "add"}:
        results = import_knowledge(
            root,
            args.project,
            args.source,
            copy_source=not args.no_copy,
            overwrite=args.overwrite,
            category=args.category,
        )
        created = sum(result.status == "created" for result in results)
        updated = sum(result.status == "updated" for result in results)
        skipped = sum(result.status == "skipped" for result in results)
        for result in results:
            print(f"{result.status.upper()}: {result.source.name} -> {result.page_path.relative_to(root)}")
        print(f"Created: {created}; updated: {updated}; skipped: {skipped}")
        print(f"Next: pulse rag build {read_project(root, args.project).slug}")
        return 0
    pages = list_knowledge(root, args.project)
    if not pages:
        print("No normalized knowledge pages found.")
        return 0
    for page in pages:
        print(page.relative_to(root))
    return 0


def _handle_docs(root: Path, args: argparse.Namespace) -> int:
    if args.docs_command == "init":
        workspace = init_docs_workspace(args.workspace, args.project)
        print(f"Docs workspace: {workspace.project_root}")
        print(f"Manifest: {workspace.manifest_path}")
        return 0
    if args.docs_command == "add":
        record = add_doc(
            args.workspace,
            args.project,
            args.source,
            doc_type=args.doc_type,
            epic=args.epic,
            feature=args.feature,
            sub_feature=args.sub_feature,
            status=args.status,
            title=args.title,
            overwrite=args.overwrite,
        )
        print(f"{record.status.upper()}: {record.id} -> {record.path}")
        return 0
    if args.docs_command == "list":
        rows = list_docs(
            args.workspace,
            args.project,
            doc_type=args.doc_type,
            epic=args.epic,
            feature=args.feature,
        )
        if not rows:
            print("No generated docs found.")
            return 0
        for item in rows:
            print(
                f"{item.get('id')}\t{item.get('type')}\t{item.get('status')}\t"
                f"{item.get('epic')}/{item.get('feature')}\t{item.get('path')}"
        )
        return 0
    if args.docs_command == "index":
        workspace = init_docs_workspace(args.workspace, args.project)
        report = build_index(
            workspace.project_root,
            workspace.project,
            provider=args.provider,
            model=args.model,
            batch_size=args.batch_size,
            force=args.force,
        )
        print(f"Indexed: {report.indexed}; skipped: {report.skipped}; removed: {report.removed}")
        print(f"Chunks: {report.chunks}; embedding: {report.provider}/{report.model}")
        return 0
    target = doc_path(
        args.workspace,
        args.project,
        args.doc_type,
        args.epic,
        args.feature,
        args.sub_feature,
    )
    print(target)
    return 0


def _handle_rag(root: Path, args: argparse.Namespace) -> int:
    project = read_project(root, args.project)
    target = root / project.knowledge_path
    if args.rag_command == "build":
        report = build_index(
            target,
            project.slug,
            provider=args.provider,
            model=args.model,
            batch_size=args.batch_size,
            force=args.force,
        )
        print(f"Indexed: {report.indexed}; skipped: {report.skipped}; removed: {report.removed}")
        print(f"Chunks: {report.chunks}; embedding: {report.provider}/{report.model}")
        return 0
    scoped_results = [("project", result) for result in query_index(target, args.query, top_k=args.top_k)]
    if args.include_shared:
        shared = root / "knowledge" / "shared"
        if _has_queryable_rag(shared):
            scoped_results.extend(
                ("shared", result) for result in query_index(shared, args.query, top_k=args.top_k)
            )
    if args.include_docs:
        docs_root = args.docs_workspace.expanduser().resolve() / project.slug
        if _has_queryable_rag(docs_root):
            scoped_results.extend(
                ("docs", result) for result in query_index(docs_root, args.query, top_k=args.top_k)
            )
    scoped_results.sort(key=lambda item: item[1].score, reverse=True)
    scoped_results = scoped_results[: args.top_k]
    results = [result for _, result in scoped_results]
    if not results:
        print("No relevant chunks found.")
        return 0
    for index, (scope, result) in enumerate(scoped_results, start=1):
        heading = f" | {result.heading}" if result.heading else ""
        print(f"[{index}] score={result.score:.4f} | scope={scope} | {result.document_id}{heading}")
        print(f"Source: {result.source}")
        print(result.text.strip())
        print()
    return 0


def _has_queryable_rag(knowledge_root: Path) -> bool:
    index = knowledge_root / ".rag" / "index.json"
    if not index.exists():
        return False
    try:
        config = json.loads(index.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    return isinstance(config, dict)


def run_doctor(root: Path) -> int:
    errors: list[str] = []
    print(f"Repository: {root}")
    for required in ("agents", "knowledge", "scripts"):
        if not (root / required).exists():
            errors.append(f"Missing repository path: {required}")
    projects = list_projects(root)
    print(f"Projects: {len(projects)}")
    for info in projects:
        missing = list(missing_project_paths(root, info))
        if missing:
            errors.extend(f"{info.slug}: missing {path.relative_to(root)}" for path in missing)
        else:
            pages = len(list_knowledge(root, info.slug))
            print(f"OK: {info.slug} ({pages} knowledge page(s))")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Pulse doctor passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
