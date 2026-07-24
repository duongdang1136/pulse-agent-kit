#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_yaml(value):
    """Convert PyYAML-native date values into JSON-schema-friendly strings."""
    if isinstance(value, (dt.date, dt.datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: normalize_yaml(item) for key, item in value.items()}
    if isinstance(value, list):
        return [normalize_yaml(item) for item in value]
    return value


def validate(instance, schema, label: str):
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.path)
        suffix = f" ({location})" if location else ""
        ERRORS.append(f"{label}: {error.message}{suffix}")


def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        return None
    value = yaml.safe_load(match.group(1)) or {}
    if not isinstance(value, dict):
        raise ValueError("frontmatter must be a YAML object")
    # Existing files commonly use `name`; treat it as title for compatibility.
    if "title" not in value and isinstance(value.get("name"), str):
        value["title"] = value["name"]
    return normalize_yaml(value)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate pulse-agent-kit metadata and references")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Require frontmatter on every agent, skill, template, tool, and knowledge Markdown file",
    )
    args = parser.parse_args()

    frontmatter_schema = load_json(ROOT / "schemas/frontmatter.schema.json")
    markdown_files = sorted(
        {
            *ROOT.glob("agents/**/*.md"),
            *ROOT.glob("tools/*/tool.md"),
            *ROOT.glob("knowledge/**/pages/*.md"),
        }
    )

    for path in markdown_files:
        label = str(path.relative_to(ROOT))
        try:
            frontmatter = parse_frontmatter(path)
        except Exception as exc:
            ERRORS.append(f"{label}: invalid YAML: {exc}")
            continue

        if frontmatter is None:
            message = f"{label}: missing frontmatter"
            if args.strict:
                ERRORS.append(message)
            else:
                WARNINGS.append(message)
            continue
        validate(frontmatter, frontmatter_schema, label)

    manifest_schema = load_json(ROOT / "schemas/agent-manifest.schema.json")
    for path in sorted(ROOT.glob("agents/*/manifest.yaml")):
        label = str(path.relative_to(ROOT))
        try:
            manifest = normalize_yaml(yaml.safe_load(path.read_text(encoding="utf-8")) or {})
            validate(manifest, manifest_schema, label)
        except Exception as exc:
            ERRORS.append(f"{label}: invalid YAML: {exc}")
            continue

        for skill in manifest.get("skills", {}).values():
            skill_path = skill.get("path") if isinstance(skill, dict) else None
            if skill_path and not (ROOT / skill_path).is_file():
                ERRORS.append(f"{label}: missing {skill_path}")
        for key in ("entrypoint", "output_template"):
            referenced_path = manifest.get(key)
            if referenced_path and not (ROOT / referenced_path).is_file():
                ERRORS.append(f"{label}: missing {referenced_path}")

    registry_path = ROOT / "tools/registry.yaml"
    if registry_path.is_file():
        try:
            registry = normalize_yaml(yaml.safe_load(registry_path.read_text(encoding="utf-8")) or {})
            validate(registry, load_json(ROOT / "schemas/tool-registry.schema.json"), "tools/registry.yaml")
            for tool in registry.get("tools", []):
                tool_path = tool.get("path") if isinstance(tool, dict) else None
                if tool_path and not (ROOT / tool_path).is_file():
                    ERRORS.append(f"tools/registry.yaml: missing {tool_path}")
        except Exception as exc:
            ERRORS.append(f"tools/registry.yaml: invalid YAML: {exc}")
    else:
        ERRORS.append("tools/registry.yaml: missing file")

    for path in sorted(ROOT.glob("knowledge/**/.rag/*.json")):
        try:
            load_json(path)
        except Exception as exc:
            ERRORS.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")

    for warning in WARNINGS:
        print(f"WARNING: {warning}")
    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}")
        return 1

    print(f"Repository validation passed ({len(WARNINGS)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
