# Skill: Tech Signal Discovery

**Command:** `/tech-signal-discovery <domain>`  
**Agent:** Researcher  
**Output:** `Tech-Trend-Watchlist`

Use this skill to discover candidate technology trends from high-signal sources after the macro regime is understood.

## Orchestration Rule

This is an orchestrator skill. It does not collect every source itself. Use source/channel skills based on the signal type:

| Signal Need | Source / Channel Skill |
|---|---|
| Web, news, blogs, reports | `research-web.md` |
| Official docs, changelog, RFC, roadmap | `research-docs.md` |
| GitHub, releases, issues, maintainer activity | `research-github.md` |
| Reddit, HN, X, Discord/Slack, forum debates | `research-community.md` |
| Existing project/shared knowledge | `rag-query.md` |
| Vendors, competitors, ecosystem category | `research-market-map.md` |
| Product launches, pricing, integrations, customer proof | `research-product-signal.md` |
| Funding, M&A, hiring, partnership | `research-funding-signal.md` |
| Platform/runtime/cloud/protocol shift | `tech-platform-shift.md` |
| Investment movement | `tech-investment-signal.md` |

## Signal Sources To Consider

```text
- official releases / changelogs
- GitHub repos, contributors, issues, releases
- package registries: npm, PyPI, crates, Maven, etc.
- Hacker News, Reddit, Discord/Slack, X/Twitter
- papers: arXiv, labs, research groups
- vendor/cloud announcements
- engineering blogs
- conference talks
- job postings and hiring signals
- benchmark sites and public case studies
```

## Goal

- Collect candidate trends/tools/patterns.
- Track signal source and signal strength.
- Separate weak buzz from repeated independent signals.
- Produce a watchlist for confirmation.

## Output Rule

Every candidate must include at least:

- Signal source.
- Source type.
- Why it may become a trend.
- What evidence is missing.
- Suggested next action: `confirm`, `monitor`, or `ignore`.

## Output Contract

Use `agents/researcher/templates/Tech-Trend-Watchlist.md`.
