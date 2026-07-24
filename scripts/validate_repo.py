#!/usr/bin/env python3
"""
Repository validator for pulse-agent-kit.

Checks:

- Agent package manifests.
- Manifest v1 and v2 compatibility.
- Referenced instruction, skill, and template files.
- Markdown frontmatter.
- Tool registry references.
- Basic repository structure.

Run:

    python scripts/validate_repo.py
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml


REQUIRED_DIRECTORIES = (
    "agents",
    "knowledge",
    "pulse",
    "schemas",
    "scripts",
    "tests",
    "tools",
)

FRONTMATTER_DIRECTORIES = (
    "agents",
    "knowledge",
    "tools",
)

IGNORED_MARKDOWN_NAMES = {
    "README.md",
}

IGNORED_DIRECTORY_NAMES = {
    ".git",
    ".pytest_cache",
    "__pycache__",
    ".rag",
    ".venv",
    "venv",
    "node_modules",
}


@dataclass(frozen=True)
class ValidationMessage:
    level: str
    path: Path | None
    message: str

    def render(self, root: Path) -> str:
        if self.path is None:
            return f"{self.level}: {self.message}"

        try:
            display_path = self.path.relative_to(root)
        except ValueError:
            display_path = self.path

        return f"{self.level}: {display_path}: {self.message}"


class RepositoryValidator:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.errors: list[ValidationMessage] = []
        self.warnings: list[ValidationMessage] = []

    def error(self, message: str, path: Path | None = None) -> None:
        self.errors.append(
            ValidationMessage(
                level="ERROR",
                path=path,
                message=message,
            )
        )

    def warning(self, message: str, path: Path | None = None) -> None:
        self.warnings.append(
            ValidationMessage(
                level="WARNING",
                path=path,
                message=message,
            )
        )

    def validate(self) -> bool:
        self.validate_required_structure()
        self.validate_agent_packages()
        self.validate_markdown_frontmatter()
        self.validate_tool_registry()

        for message in self.errors:
            print(message.render(self.root))

        for message in self.warnings:
            print(message.render(self.root))

        if self.errors:
            print()
            print(
                f"Repository validation failed "
                f"({len(self.errors)} error(s), "
                f"{len(self.warnings)} warning(s))"
            )
            return False

        print(
            f"Repository validation passed "
            f"({len(self.warnings)} warning(s))"
        )
        return True

    def validate_required_structure(self) -> None:
        for relative in REQUIRED_DIRECTORIES:
            path = self.root / relative

            if not path.exists():
                self.error("required directory is missing", path)
            elif not path.is_dir():
                self.error("expected a directory", path)

        pyproject = self.root / "pyproject.toml"
        if not pyproject.is_file():
            self.error("required file is missing", pyproject)

    def validate_agent_packages(self) -> None:
        agents_dir = self.root / "agents"

        if not agents_dir.is_dir():
            return

        agent_dirs = sorted(
            path
            for path in agents_dir.iterdir()
            if path.is_dir()
            and path.name not in IGNORED_DIRECTORY_NAMES
            and not path.name.startswith(".")
        )

        if not agent_dirs:
            self.warning("no agent packages found", agents_dir)
            return

        for agent_dir in agent_dirs:
            self.validate_agent_package(agent_dir)

    def validate_agent_package(self, agent_dir: Path) -> None:
        manifest_path = agent_dir / "manifest.yaml"

        if not manifest_path.is_file():
            self.warning("missing manifest.yaml", agent_dir)
            return

        manifest = self.load_yaml_mapping(manifest_path)

        if manifest is None:
            return

        schema_version = manifest.get("schema")

        if schema_version == 2:
            self.validate_agent_manifest_v2(
                agent_dir=agent_dir,
                manifest_path=manifest_path,
                manifest=manifest,
            )
        else:
            self.validate_legacy_agent_manifest(
                agent_dir=agent_dir,
                manifest_path=manifest_path,
                manifest=manifest,
            )

    def validate_agent_manifest_v2(
        self,
        *,
        agent_dir: Path,
        manifest_path: Path,
        manifest: dict[str, Any],
    ) -> None:
        required_fields = (
            "schema",
            "name",
            "display_name",
            "version",
            "description",
            "instructions",
            "skills",
            "templates",
            "knowledge",
            "output",
            "tags",
        )

        for field_name in required_fields:
            if field_name not in manifest:
                self.error(
                    f"missing required field '{field_name}'",
                    manifest_path,
                )

        name = manifest.get("name")
        if not isinstance(name, str) or not name.strip():
            self.error("'name' must be a non-empty string", manifest_path)
        elif name != agent_dir.name:
            self.error(
                f"manifest name '{name}' does not match "
                f"directory name '{agent_dir.name}'",
                manifest_path,
            )

        instructions = manifest.get("instructions")

        if not isinstance(instructions, str) or not instructions.strip():
            self.error(
                "'instructions' must be a non-empty string",
                manifest_path,
            )
        else:
            instruction_path = agent_dir / instructions

            if not instruction_path.is_file():
                self.error(
                    f"instruction file does not exist: {instructions}",
                    instruction_path,
                )

        skills = self.normalize_manifest_items(
            manifest.get("skills"),
            field_name="skills",
            manifest_path=manifest_path,
        )

        templates = self.normalize_manifest_items(
            manifest.get("templates"),
            field_name="templates",
            manifest_path=manifest_path,
        )

        self.validate_referenced_markdown_files(
            agent_dir=agent_dir,
            folder_name="skills",
            item_names=skills,
            manifest_path=manifest_path,
        )

        self.validate_referenced_markdown_files(
            agent_dir=agent_dir,
            folder_name="templates",
            item_names=templates,
            manifest_path=manifest_path,
        )

        output = manifest.get("output")

        if not isinstance(output, dict):
            self.error(
                "'output' must be a mapping",
                manifest_path,
            )
        else:
            output_format = output.get("format")

            if not isinstance(output_format, str) or not output_format.strip():
                self.error(
                    "'output.format' must be a non-empty string",
                    manifest_path,
                )

            output_template = output.get("template")

            if output_template is not None:
                if not isinstance(output_template, str):
                    self.error(
                        "'output.template' must be a string",
                        manifest_path,
                    )
                elif output_template not in templates:
                    self.error(
                        "'output.template' must also be declared "
                        "in 'templates'",
                        manifest_path,
                    )

        knowledge = manifest.get("knowledge")

        if not isinstance(knowledge, dict):
            self.error(
                "'knowledge' must be a mapping",
                manifest_path,
            )
        else:
            for field_name in ("shared", "project"):
                value = knowledge.get(field_name)

                if not isinstance(value, bool):
                    self.error(
                        f"'knowledge.{field_name}' must be a boolean",
                        manifest_path,
                    )

        tags = manifest.get("tags")

        if not isinstance(tags, list):
            self.error(
                "'tags' must be a list",
                manifest_path,
            )
        elif any(not isinstance(tag, str) or not tag.strip() for tag in tags):
            self.error(
                "'tags' must contain non-empty strings",
                manifest_path,
            )

        forbidden_fields = (
            "provider",
            "model",
            "temperature",
            "api_key",
            "llm",
        )

        for field_name in forbidden_fields:
            if field_name in manifest:
                self.error(
                    f"LLM-specific field '{field_name}' is not allowed "
                    "in an agent package manifest",
                    manifest_path,
                )

    def validate_legacy_agent_manifest(
        self,
        *,
        agent_dir: Path,
        manifest_path: Path,
        manifest: dict[str, Any],
    ) -> None:
        self.warning(
            "legacy agent manifest detected; migrate to schema: 2",
            manifest_path,
        )

        instructions = (
            manifest.get("instructions")
            or manifest.get("system_prompt")
            or manifest.get("prompt")
            or "agent.md"
        )

        if isinstance(instructions, str):
            instruction_path = agent_dir / instructions

            if not instruction_path.is_file():
                self.error(
                    f"instruction file does not exist: {instructions}",
                    instruction_path,
                )

        skills = self.normalize_manifest_items(
            manifest.get("skills"),
            field_name="skills",
            manifest_path=manifest_path,
        )

        templates = self.normalize_manifest_items(
            manifest.get("templates"),
            field_name="templates",
            manifest_path=manifest_path,
        )

        self.validate_referenced_markdown_files(
            agent_dir=agent_dir,
            folder_name="skills",
            item_names=skills,
            manifest_path=manifest_path,
        )

        self.validate_referenced_markdown_files(
            agent_dir=agent_dir,
            folder_name="templates",
            item_names=templates,
            manifest_path=manifest_path,
        )

    def normalize_manifest_items(
        self,
        value: Any,
        *,
        field_name: str,
        manifest_path: Path,
    ) -> list[str]:
        """
        Support both manifest formats.

        Manifest v2:

            skills:
              - audit
              - ui-to-spec

        Legacy manifest:

            skills:
              audit: skills/audit.md
              ui-to-spec: skills/ui-to-spec.md
        """

        if value is None:
            return []

        if isinstance(value, list):
            normalized: list[str] = []

            for item in value:
                if not isinstance(item, str) or not item.strip():
                    self.error(
                        f"'{field_name}' must contain non-empty strings",
                        manifest_path,
                    )
                    continue

                normalized.append(item.strip())

            return normalized

        if isinstance(value, dict):
            normalized = []

            for key, item in value.items():
                candidate = item if isinstance(item, str) else key

                if not isinstance(candidate, str) or not candidate.strip():
                    self.error(
                        f"legacy '{field_name}' values must be strings",
                        manifest_path,
                    )
                    continue

                normalized.append(candidate.strip())

            return normalized

        self.error(
            f"'{field_name}' must be a list or legacy mapping",
            manifest_path,
        )
        return []

    def validate_referenced_markdown_files(
        self,
        *,
        agent_dir: Path,
        folder_name: str,
        item_names: Iterable[str],
        manifest_path: Path,
    ) -> None:
        seen: set[str] = set()

        for item_name in item_names:
            if item_name in seen:
                self.error(
                    f"duplicate '{folder_name}' item: {item_name}",
                    manifest_path,
                )
                continue

            seen.add(item_name)

            referenced_path = self.resolve_agent_reference(
                agent_dir=agent_dir,
                folder_name=folder_name,
                item_name=item_name,
            )

            if not referenced_path.is_file():
                try:
                    relative = referenced_path.relative_to(agent_dir)
                except ValueError:
                    relative = referenced_path

                self.error(
                    f"referenced file does not exist: {relative}",
                    referenced_path,
                )

    def resolve_agent_reference(
        self,
        *,
        agent_dir: Path,
        folder_name: str,
        item_name: str,
    ) -> Path:
        normalized = item_name.replace("\\", "/").strip()

        if normalized.startswith(f"{folder_name}/"):
            relative = Path(normalized)
        elif "/" in normalized:
            relative = Path(normalized)
        else:
            filename = (
                normalized
                if normalized.lower().endswith(".md")
                else f"{normalized}.md"
            )

            relative = Path(folder_name) / filename

        return agent_dir / relative

    def validate_markdown_frontmatter(self) -> None:
        for relative_dir in FRONTMATTER_DIRECTORIES:
            base_dir = self.root / relative_dir

            if not base_dir.is_dir():
                continue

            for path in sorted(base_dir.rglob("*.md")):
                if self.should_ignore_path(path):
                    continue

                if path.name in IGNORED_MARKDOWN_NAMES:
                    continue

                if not self.has_frontmatter(path):
                    self.warning("missing frontmatter", path)

    def validate_tool_registry(self) -> None:
        registry_path = self.root / "tools" / "registry.yaml"

        if not registry_path.is_file():
            self.warning("missing tool registry", registry_path)
            return

        registry = self.load_yaml_mapping(registry_path)

        if registry is None:
            return

        tools_value = registry.get("tools", registry)

        if isinstance(tools_value, dict):
            tool_entries = tools_value.items()
        elif isinstance(tools_value, list):
            tool_entries = enumerate(tools_value)
        else:
            self.error(
                "tool registry must contain a mapping or list",
                registry_path,
            )
            return

        for key, value in tool_entries:
            if isinstance(value, str):
                reference = value
            elif isinstance(value, dict):
                reference = (
                    value.get("path")
                    or value.get("file")
                    or value.get("definition")
                )
            else:
                self.warning(
                    f"cannot inspect tool entry '{key}'",
                    registry_path,
                )
                continue

            if not reference:
                continue

            reference_path = Path(str(reference).replace("\\", "/"))

            if reference_path.parts and reference_path.parts[0].lower() == "tools":
                tool_path = self.root / reference_path
            else:
                tool_path = self.root / "tools" / reference_path
            if not tool_path.exists():
                self.error(
                    f"tool registry references missing path: {reference}",
                    tool_path,
                )

    def load_yaml_mapping(
        self,
        path: Path,
    ) -> dict[str, Any] | None:
        try:
            value = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            self.error(f"invalid YAML: {exc}", path)
            return None
        except OSError as exc:
            self.error(f"could not read file: {exc}", path)
            return None

        if value is None:
            return {}

        if not isinstance(value, dict):
            self.error("YAML root must be a mapping", path)
            return None

        return value

    def has_frontmatter(self, path: Path) -> bool:
        try:
            content = path.read_text(encoding="utf-8-sig")
        except OSError as exc:
            self.error(f"could not read Markdown file: {exc}", path)
            return False

        lines = content.splitlines()

        if not lines or lines[0].strip() != "---":
            return False

        for line in lines[1:]:
            if line.strip() == "---":
                return True

        return False

    def should_ignore_path(self, path: Path) -> bool:
        return any(
            part in IGNORED_DIRECTORY_NAMES
            for part in path.parts
        )


def find_repository_root(start: Path) -> Path:
    current = start.resolve()

    if current.is_file():
        current = current.parent

    for candidate in (current, *current.parents):
        if (
            (candidate / "pyproject.toml").is_file()
            and (candidate / "pulse").is_dir()
        ):
            return candidate

    raise RuntimeError(
        "Could not locate repository root. "
        "Run this script inside pulse-agent-kit."
    )


def main() -> int:
    try:
        root = find_repository_root(Path.cwd())
    except RuntimeError as exc:
        print(f"ERROR: {exc}")
        return 1

    validator = RepositoryValidator(root)
    return 0 if validator.validate() else 1


if __name__ == "__main__":
    sys.exit(main())