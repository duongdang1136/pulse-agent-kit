#!/usr/bin/env python3
from pathlib import Path
import sys
from pulse.workflow import load_workflow_manifest, validate_workflow_package

def find_root(start: Path) -> Path:
    for candidate in (start.resolve(), *start.resolve().parents):
        if (candidate / "pyproject.toml").is_file(): return candidate
    raise RuntimeError("Could not locate repository root.")

def main() -> int:
    try: root = find_root(Path.cwd())
    except RuntimeError as exc:
        print(f"ERROR: {exc}"); return 1
    workflows = root / "workflows"
    if not workflows.is_dir():
        print("ERROR: workflows directory is missing"); return 1
    errors = 0; packages = 0
    for manifest_path in sorted(workflows.glob("*/manifest.yaml")):
        packages += 1
        manifest = load_workflow_manifest(manifest_path)
        for issue in validate_workflow_package(manifest, repository_root=root):
            errors += 1
            path = issue.path or manifest_path
            try: path = path.relative_to(root)
            except ValueError: pass
            print(f"ERROR: {path}: [{issue.code}] {issue.message}")
    if errors:
        print(f"Workflow validation failed ({errors} error(s))"); return 1
    print(f"Workflow validation passed ({packages} package(s))"); return 0

if __name__ == "__main__": sys.exit(main())
