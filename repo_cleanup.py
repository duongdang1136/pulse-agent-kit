#!/usr/bin/env python3
"""One-time repository cleanup for pulse-agent-kit."""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

MILESTONE_MOVES = {
    "docs/MILESTONE-1-PROJECT-WORKSPACE.md": "docs/milestones/001-project-workspace.md",
    "docs/MILESTONE-2-KNOWLEDGE-INGESTION.md": "docs/milestones/002-knowledge-ingestion.md",
    "docs/MILESTONE-2.1-AUTORAG-FOUNDATION.md": "docs/milestones/003-autorag-foundation.md",
}

TEST_MOVES = {
    "tests/test_autorag.py": "tests/integration/test_autorag.py",
    "tests/test_rag.py": "tests/integration/test_rag.py",
    "tests/test_project_cli.py": "tests/cli/test_project_cli.py",
    "tests/test_knowledge_cli.py": "tests/cli/test_knowledge_cli.py",
}

ROOT_FILES_TO_DELETE = {"README-UPDATE.md", "tree.txt"}
GENERATED_DIR_NAMES = {"__pycache__", ".pytest_cache", "pulse_agent_kit.egg-info"}
GITIGNORE_RULES = ["__pycache__/", "*.py[cod]", "*.egg-info/", ".pytest_cache/", ".coverage", "htmlcov/"]


class Cleaner:
    def __init__(self, root: Path, apply: bool) -> None:
        self.root = root
        self.apply = apply
        self.changed = 0
        self.skipped = 0

    @property
    def mode(self) -> str:
        return "APPLY" if self.apply else "DRY-RUN"

    def relative(self, path: Path) -> Path:
        try:
            return path.relative_to(self.root)
        except ValueError:
            return path

    def log(self, action: str, path: Path, detail: str = "") -> None:
        suffix = f" — {detail}" if detail else ""
        print(f"[{self.mode}] {action:<13} {self.relative(path)}{suffix}")

    def ensure_dir(self, relative: str) -> None:
        path = self.root / relative
        if path.is_dir():
            self.skipped += 1
            return
        self.log("CREATE DIR", path)
        if self.apply:
            path.mkdir(parents=True, exist_ok=True)
        self.changed += 1

    def move(self, source_relative: str, destination_relative: str) -> None:
        source = self.root / source_relative
        destination = self.root / destination_relative
        if not source.exists():
            if destination.exists():
                self.log("SKIP", destination, "already moved")
            else:
                self.log("SKIP", source, "source not found")
            self.skipped += 1
            return
        if destination.exists():
            raise RuntimeError(f"Destination already exists: {destination_relative}")
        self.log("MOVE", source, f"-> {destination_relative}")
        if self.apply:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(destination))
        self.changed += 1

    def delete_file(self, relative: str) -> None:
        path = self.root / relative
        if not path.exists():
            self.skipped += 1
            return
        if not path.is_file():
            raise RuntimeError(f"Expected a file: {relative}")
        self.log("DELETE FILE", path)
        if self.apply:
            path.unlink()
        self.changed += 1

    def delete_generated_artifacts(self) -> None:
        directories = sorted(
            (p for p in self.root.rglob("*") if p.is_dir() and p.name in GENERATED_DIR_NAMES),
            key=lambda p: len(p.parts),
            reverse=True,
        )
        for directory in directories:
            if not directory.exists():
                continue
            self.log("DELETE DIR", directory)
            if self.apply:
                shutil.rmtree(directory)
            self.changed += 1
        for pyc_file in sorted(self.root.rglob("*.pyc")):
            if not pyc_file.exists():
                continue
            self.log("DELETE FILE", pyc_file)
            if self.apply:
                pyc_file.unlink()
            self.changed += 1

    def delete_empty_directory(self, relative: str) -> None:
        path = self.root / relative
        if not path.exists():
            self.skipped += 1
            return
        if any(path.iterdir()):
            self.log("KEEP DIR", path, "not empty")
            self.skipped += 1
            return
        self.log("DELETE DIR", path, "empty")
        if self.apply:
            path.rmdir()
        self.changed += 1

    def update_gitignore(self) -> None:
        path = self.root / ".gitignore"
        existing = path.read_text(encoding="utf-8") if path.exists() else ""
        existing_lines = set(existing.splitlines())
        missing = [rule for rule in GITIGNORE_RULES if rule not in existing_lines]
        if not missing:
            self.log("SKIP", path, "generated-file rules already present")
            self.skipped += 1
            return
        self.log("UPDATE", path, f"add {len(missing)} ignore rule(s)")
        if self.apply:
            content = existing.rstrip()
            block = "# Python generated files\n" + "\n".join(missing)
            path.write_text(f"{content}\n\n{block}\n" if content else f"{block}\n", encoding="utf-8")
        self.changed += 1

    def patch_legacy_rag_test(self) -> None:
        path = self.root / "tests/integration/test_rag.py"
        if not path.exists():
            self.log("SKIP", path, "test file not found")
            self.skipped += 1
            return
        content = path.read_text(encoding="utf-8")
        updated, count = re.subn(
            r"Path\(__file__\)\.resolve\(\)\.parents\[1\]",
            "Path(__file__).resolve().parents[2]",
            content,
        )
        if count == 0:
            detail = "already fixed" if "Path(__file__).resolve().parents[2]" in content else "legacy lookup not found"
            self.log("SKIP", path, detail)
            self.skipped += 1
            return
        self.log("PATCH", path, "parents[1] -> parents[2]")
        if self.apply:
            path.write_text(updated, encoding="utf-8")
        self.changed += 1

    def restore_tracked_rag_script_if_missing(self) -> None:
        path = self.root / "scripts/rag.py"
        if path.exists():
            self.log("SKIP", path, "present")
            self.skipped += 1
            return
        tracked = subprocess.run(
            ["git", "cat-file", "-e", "HEAD:scripts/rag.py"],
            cwd=self.root,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        ).returncode == 0
        if not tracked:
            self.log("SKIP", path, "not present in HEAD")
            self.skipped += 1
            return
        self.log("RESTORE", path, "from Git HEAD")
        if self.apply:
            result = subprocess.run(
                ["git", "restore", "--source=HEAD", "--", "scripts/rag.py"],
                cwd=self.root,
                check=False,
            )
            if result.returncode != 0:
                raise RuntimeError("Git could not restore scripts/rag.py")
        self.changed += 1


def detect_repo_root(script_path: Path) -> Path:
    for candidate in [Path.cwd(), script_path.parent, script_path.parent.parent]:
        candidate = candidate.resolve()
        if (candidate / "pyproject.toml").is_file() and (candidate / "pulse").is_dir():
            return candidate
    raise RuntimeError("Could not locate repository root.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="One-time cleanup for pulse-agent-kit.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        root = detect_repo_root(Path(__file__).resolve())
        cleaner = Cleaner(root, args.apply)
        print(f"Repository: {root}")
        print(f"Mode:       {cleaner.mode}\n")

        for directory in ["docs/milestones", "tests/cli", "tests/integration", "tests/unit", "tests/fixtures"]:
            cleaner.ensure_dir(directory)
        for source, destination in MILESTONE_MOVES.items():
            cleaner.move(source, destination)
        for source, destination in TEST_MOVES.items():
            cleaner.move(source, destination)

        cleaner.patch_legacy_rag_test()
        cleaner.restore_tracked_rag_script_if_missing()

        for relative in sorted(ROOT_FILES_TO_DELETE):
            cleaner.delete_file(relative)
        cleaner.delete_generated_artifacts()
        cleaner.delete_empty_directory("pulse/templates")
        cleaner.update_gitignore()

        print(f"\nPlanned/applied changes: {cleaner.changed}")
        print(f"Skipped:                 {cleaner.skipped}")
        if args.apply:
            print("\nCleanup completed.")
            print("Next commands:")
            print("  python -m pytest -q")
            print("  python scripts/validate_repo.py")
            print("  git status --short")
            print("  tree /F /A > tree.txt")
        else:
            print("\nNo files were changed. Run again with --apply to execute.")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
