from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
RESEARCHER = ROOT / "agents" / "researcher"


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def load_yaml(relative_path: str):
    return yaml.safe_load(read_text(relative_path))


def test_researcher_manifest_references_existing_files():
    manifest = load_yaml("agents/researcher/manifest.yaml")

    for skill in manifest["skills"]:
        assert (RESEARCHER / "skills" / f"{skill}.md").exists(), skill

    for template in manifest["templates"]:
        assert (RESEARCHER / "templates" / f"{template}.md").exists(), template

    assert (RESEARCHER / manifest["instructions"]).exists()


def test_researcher_has_no_legacy_rag_router_references():
    searchable_files = [
        "agents/researcher/manifest.yaml",
        "agents/researcher/agent.md",
        "COMMANDS.md",
        "workflows/feature-documentation/manifest.yaml",
    ]

    for relative_path in searchable_files:
        assert "rag-router" not in read_text(relative_path), relative_path


def test_tech_macro_regime_contract_includes_all_macro_helpers():
    manifest = load_yaml("agents/researcher/manifest.yaml")
    macro_rule = next(rule for rule in manifest["resolution"]["rules"] if rule["id"] == "tech-macro-regime")
    macro_skill = read_text("agents/researcher/skills/tech-macro-regime.md")
    macro_template = read_text("agents/researcher/templates/Tech-Macro-Regime-Report.md")

    required_helpers = {
        "tech-domain-lifecycle",
        "tech-adoption-curve",
        "tech-investment-signal",
        "tech-platform-shift",
        "tech-regulation-risk",
        "tech-market-timing",
    }

    assert required_helpers.issubset(set(manifest["skills"]))
    assert {"tech-macro-regime", "tech-domain-lifecycle", "tech-adoption-curve", "tech-market-timing"}.issubset(
        set(macro_rule["skills"])
    )

    for helper in required_helpers:
        assert f"{helper}.md" in macro_skill
        assert f"{helper}.md" in macro_template


def test_tech_signal_discovery_contract_includes_source_channels():
    manifest = load_yaml("agents/researcher/manifest.yaml")
    signal_rule = next(rule for rule in manifest["resolution"]["rules"] if rule["id"] == "tech-signal-discovery")
    signal_skill = read_text("agents/researcher/skills/tech-signal-discovery.md")
    watchlist_template = read_text("agents/researcher/templates/Tech-Trend-Watchlist.md")

    source_channels = {
        "rag-query",
        "research-web",
        "research-docs",
        "research-github",
        "research-community",
        "research-market-map",
        "research-product-signal",
        "research-funding-signal",
    }

    assert source_channels.issubset(set(manifest["skills"]))
    assert {"tech-signal-discovery", "research-docs", "research-github", "research-community", "research-market-map"}.issubset(
        set(signal_rule["skills"])
    )

    for channel in source_channels:
        assert f"{channel}.md" in signal_skill

    for channel in source_channels - {"rag-query"}:
        assert f"{channel}.md" in watchlist_template


def test_tech_trend_confirmation_contract_includes_analysis_helpers():
    manifest = load_yaml("agents/researcher/manifest.yaml")
    confirmation_rule = next(rule for rule in manifest["resolution"]["rules"] if rule["id"] == "tech-trend-confirmation")
    confirmation_skill = read_text("agents/researcher/skills/tech-trend-confirmation.md")
    scorecard_template = read_text("agents/researcher/templates/Tech-Trend-Scorecard.md")

    analysis_helpers = {
        "evidence-evaluation",
        "adoption-signal",
        "tech-adoption-curve",
        "durability-check",
        "tech-regulation-risk",
        "tech-market-timing",
        "compare-options",
        "benchmark-analysis",
        "itba-impact-analysis",
    }

    assert analysis_helpers.issubset(set(manifest["skills"]))
    assert {"tech-trend-confirmation", "adoption-signal", "durability-check", "itba-impact-analysis"}.issubset(
        set(confirmation_rule["skills"])
    )

    for helper in analysis_helpers:
        assert f"{helper}.md" in confirmation_skill

    for helper in {
        "evidence-evaluation",
        "adoption-signal",
        "tech-adoption-curve",
        "durability-check",
        "tech-regulation-risk",
        "tech-market-timing",
        "itba-impact-analysis",
    }:
        assert f"{helper}.md" in scorecard_template


def test_feature_documentation_research_stage_uses_expanded_source_channels():
    workflow = load_yaml("workflows/feature-documentation/manifest.yaml")
    research_stage = next(stage for stage in workflow["stages"] if stage["id"] == "research")

    required_skills = {
        "research-plan",
        "rag-query",
        "research-routing",
        "research-web",
        "research-docs",
        "research-github",
        "research-community",
        "research-market-map",
        "research-product-signal",
        "research-funding-signal",
        "evidence-evaluation",
        "synthesize",
    }

    assert required_skills.issubset(set(research_stage["skills"]))


def test_feature_documentation_has_optional_knowledge_upsert_checkpoint():
    workflow = load_yaml("workflows/feature-documentation/manifest.yaml")
    stages = {stage["id"]: stage for stage in workflow["stages"]}

    assert stages["research"]["handoff_to"] == "knowledge_upsert"
    assert stages["knowledge_upsert"]["agent"] == "researcher"
    assert stages["knowledge_upsert"]["skills"] == ["knowledge-ingest"]
    assert stages["knowledge_upsert"]["output"] == "Knowledge-Ingest-Note"
    assert stages["knowledge_upsert"]["optional"] is True
    assert stages["knowledge_upsert"]["handoff_to"] == "research_intake"
    assert "knowledge_upsert.output" in stages["research_intake"]["consumes"]
