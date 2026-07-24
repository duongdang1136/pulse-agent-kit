from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from pulse import __version__
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

    sub.add_parser("doctor", help="Check repository and project workspace health")
    sub.add_parser("validate", help="Run the repository validator")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        root = find_repo_root()
        if args.command == "project":
            if args.project_command == "create":
                info = create_project(root, args.name, args.slug, args.description)
                print(f"Created project: {info.name} ({info.slug})")
                print(f"Workspace: {info.workspace_path}")
                print(f"Knowledge: {info.knowledge_path}")
                print("Next: add source files to the workspace and normalize knowledge into pages/.")
                return 0
            if args.project_command == "list":
                projects = list_projects(root)
                if not projects:
                    print("No projects found.")
                    return 0
                for item in projects:
                    print(f"{item.slug}\t{item.name}\t{item.created}")
                return 0
            if args.project_command == "info":
                info = read_project(root, args.project)
                print(f"Name: {info.name}")
                print(f"Slug: {info.slug}")
                print(f"Description: {info.description or '-'}")
                print(f"Created: {info.created or '-'}")
                print(f"Workspace: {info.workspace_path}")
                print(f"Knowledge: {info.knowledge_path}")
                return 0
        if args.command == "doctor":
            return run_doctor(root)
        if args.command == "validate":
            validator = root / "scripts" / "validate_repo.py"
            if not validator.exists():
                print("ERROR: scripts/validate_repo.py was not found", file=sys.stderr)
                return 1
            return subprocess.call([sys.executable, str(validator)], cwd=root)
    except (FileExistsError, FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 2


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
            print(f"OK: {info.slug}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Pulse doctor passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
