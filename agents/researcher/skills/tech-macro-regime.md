# Skill: Tech Macro Regime

**Command:** `/tech-macro-regime <domain>`  
**Agent:** Researcher  
**Output:** `Tech-Macro-Regime-Report`

Use this skill to identify the current macro phase of a technology domain before discovering or confirming specific trends.

## Orchestration Rule

This is an orchestrator skill. Use helper skills only when the section is relevant to the domain:

| Section | Helper Skill | Purpose |
|---|---|---|
| Domain Lifecycle | `tech-domain-lifecycle.md` | Classify domain maturity |
| Adoption Curve | `tech-adoption-curve.md` | Measure adoption movement |
| Investment Signal | `tech-investment-signal.md` | Detect funding, hiring, M&A, budget movement |
| Platform Shift | `tech-platform-shift.md` | Detect runtime/cloud/vendor/protocol shifts |
| Regulation Risk | `tech-regulation-risk.md` | Assess compliance, security, license, policy pressure |
| Market Timing | `tech-market-timing.md` | Decide too early, right time, crowded, late, or declining |

## Regime Phases

```text
early-research       - mostly papers, prototypes, experiments
developer-adoption   - developers actively try/build with it
production-adoption  - teams deploy it in real products
enterprise-adoption  - vendors, enterprises, compliance, procurement appear
hype-cycle           - attention is high but evidence may be weak
decline              - usage/community/maintainer activity is falling
maintenance          - mature, stable, low novelty, mostly incremental change
```

## Goal

- Classify the domain phase.
- Identify macro tailwinds/headwinds.
- Define allowed research actions for the phase.
- Identify hype risk and adoption maturity.
- Decide whether to continue to `tech-signal-discovery.md`.
- Produce `templates/Tech-Macro-Regime-Report.md`.

## Decision Gate

| Regime Result | Next Action |
|---|---|
| developer-adoption / production-adoption / enterprise-adoption | Continue to `tech-signal-discovery.md` |
| early-research | Continue only for watchlist/research, not production recommendation |
| hype-cycle | Continue only with strong evidence-evaluation guardrails |
| maintenance | Continue only if the user needs comparison, benchmark, or migration evidence |
| decline | Stop or produce risk/watchlist note unless user explicitly asks |

## Output Contract

Use `agents/researcher/templates/Tech-Macro-Regime-Report.md`.
