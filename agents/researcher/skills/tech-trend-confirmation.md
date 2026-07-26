# Skill: Tech Trend Confirmation

**Command:** `/tech-trend-confirm <trend|tool|pattern>`  
**Agent:** Researcher  
**Output:** `Tech-Trend-Scorecard`

Use this skill to decide whether a candidate technology trend is real, durable, useful for product/engineering work, or mostly hype.

## Orchestration Rule

This is an orchestrator skill. Use helper skills based on what needs confirmation:

| Confirmation Need | Helper Skill |
|---|---|
| Evidence quality, freshness, bias, conflict | `evidence-evaluation.md` |
| Real adoption beyond attention | `adoption-signal.md` |
| Developer/team/enterprise adoption curve | `tech-adoption-curve.md` |
| Durability vs short-term hype | `durability-check.md` |
| Regulation, security, license, governance risk | `tech-regulation-risk.md` |
| Market timing and crowdedness | `tech-market-timing.md` |
| Tool/vendor comparison | `compare-options.md` |
| Benchmark or quantified performance/cost claim | `benchmark-analysis.md` |
| ITBA/product handoff impact | `itba-impact-analysis.md` |

## Confirmation Layers

```text
1. Adoption velocity: stars/downloads/usage/case studies/jobs.
2. Production evidence: real products, reference architectures, incident learnings.
3. Ecosystem support: integrations, plugins, cloud/vendor support.
4. Maintainer health: release cadence, issue response, bus factor.
5. Community momentum: debates, repeated independent discussions, KOL analysis.
6. Risk profile: security, license, migration cost, vendor lock-in.
7. Hype/crowdedness: overpromotion, shallow content, no production proof.
```

## Goal

- Confirm trend stage.
- Score trend strength and durability.
- Define invalidation conditions.
- Identify ITBA/product impact.
- Produce `templates/Tech-Trend-Scorecard.md`.

## Confirmation Gate

Do not mark a trend as `confirmed` unless it has:

- At least two independent source types.
- Some evidence of adoption or production usage.
- A clear problem-solution fit.
- Known risks or invalidation conditions.
- ITBA impact expressed as recommendation, assumption, or open question.

## Output Contract

Use `agents/researcher/templates/Tech-Trend-Scorecard.md`.
