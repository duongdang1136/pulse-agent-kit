# Skill: Tech Trend Summary

**Command:** `/tech-trend-summary <domain>`  
**Agent:** Researcher  
**Output:** `Tech-Trend-Summary`

Use this skill to summarize tech trend artifacts into a quick-scannable overview for Researcher, ITBA, product, or engineering stakeholders.

## Inputs

```text
1. Tech-Macro-Regime-Report
2. Tech-Trend-Watchlist
3. Tech-Trend-Scorecard
4. Tech-Source-Registry
5. Research-Report, if available
```

Not all inputs are required, but missing artifacts must be listed.

## Goal

- Give a quick macro snapshot.
- Identify top candidate trends.
- Mark confirmed, rejected, or watchlist trends.
- Surface high-signal sources.
- Summarize ITBA/product impact.
- Define next actions.
- Produce `templates/Tech-Trend-Summary.md`.

## Output Contract

Use `agents/researcher/templates/Tech-Trend-Summary.md`.
