from pathlib import Path
import pytest

from pulse.agent.manifest import load_agent_manifest
from pulse.agent.validator import AgentValidationError, validate_agent_package
from tests.unit.test_agent_manifest import make_package


def test_valid_package(tmp_path):
    manifest = load_agent_manifest(make_package(tmp_path))
    assert validate_agent_package(manifest) == []


def test_missing_skill(tmp_path):
    package = make_package(tmp_path)
    (package / "skills/analyze.md").unlink()
    issues = validate_agent_package(load_agent_manifest(package))
    assert [x.code for x in issues] == ["skill.missing"]


def test_strict_mode(tmp_path):
    package = make_package(tmp_path)
    (package / "skills/analyze.md").unlink()
    with pytest.raises(AgentValidationError):
        validate_agent_package(load_agent_manifest(package), strict=True)
