from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from pulse import __version__
from pulse.knowledge import import_knowledge, list_knowledge
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
    knowledge_list = knowledge_sub.add_parser("list", help="List normalized project knowledge pages")
    knowledge_list.add_argument("project", help="Project slug or name")

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
        )
        imported = sum(result.status == "imported" for result in results)
        skipped = len(results) - imported
        for result in results:
            print(f"{result.status.upper()}: {result.source.name} -> {result.page_path.relative_to(root)}")
        print(f"Imported: {imported}; skipped: {skipped}")
        print(f"Next: pulse rag build {read_project(root, args.project).slug}")
        return 0
    pages = list_knowledge(root, args.project)
    if not pages:
        print("No normalized knowledge pages found.")
        return 0
    for page in pages:
        print(page.relative_to(root))
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
    results = query_index(target, args.query, top_k=args.top_k)
    if not results:
        print("No relevant chunks found.")
        return 0
    for index, result in enumerate(results, start=1):
        heading = f" | {result.heading}" if result.heading else ""
        print(f"[{index}] score={result.score:.4f} | {result.document_id}{heading}")
        print(f"Source: {result.source}")
        print(result.text.strip())
        print()
    return 0


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
