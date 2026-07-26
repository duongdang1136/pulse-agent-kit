# Research Report Template

**Dùng cho:** Researcher Agent  
**Output của:** `/research`, `/research-web`, `/research-github`, `/research-community`  
**Handoff tới:** ITBA `Research-Intake-Execution`

---

## Report Header

```text
Topic:             [topic / feature / concept]
Project:           [project / N/A]
Research date:     [YYYY-MM-DD]
Requested by:      [user / project]
Scope:             [Project Sources / Knowledge / Web / GitHub / Community / Mixed]
RAG status:        [HIT / PARTIAL / MISS]
Confidence:        [High / Medium / Low]
Output file:       [Research-Report reference / generated filename]
```

---

## Research Plan

> Skill: `agents/researcher/skills/research-plan.md`

### Research Questions
- [Question 1]
- [Question 2]

### Selected Inputs
| Input | Used | Reason |
|---|---|---|
| Project source docs | [Yes / No] | [reason] |
| Project knowledge | [Yes / No] | [reason] |
| Shared knowledge | [Yes / No] | [reason] |
| Web research | [Yes / No] | [reason] |
| Docs / changelog / RFC research | [Yes / No] | [reason] |
| GitHub research | [Yes / No] | [reason] |
| Community research | [Yes / No] | [reason] |
| Market map / product / funding signal | [Yes / No] | [reason] |

---

## Source Inventory

| Source ID | Source | Type | Date / Version | Relevance | Confidence |
|---|---|---|---|---|---|
| SRC-001 | [path / URL / doc name] | [User / Project Source / Knowledge / Web / GitHub / Community] | [date/version] | [High / Medium / Low] | [High / Medium / Low] |

---

## Executive Summary

[2-4 câu tóm tắt evidence quan trọng nhất cho ITBA. Không biến recommendation thành requirement.]

**Verdict:** [Sufficient for ITBA / Partial / Blocked]  
**Confidence:** [High / Medium / Low]

---

## Evidence-Backed Findings

| Finding ID | Finding | Evidence | Source ID | Impact on ITBA |
|---|---|---|---|---|
| F-001 | [finding] | [fact/quote summary/data] | SRC-001 | [BA section affected] |

---

## Evidence Evaluation

> Skill: `agents/researcher/skills/evidence-evaluation.md`

| Source ID | Authority | Freshness | Directness | Bias Risk | Reliability | Notes |
|---|---|---|---|---|---|---|
| SRC-001 | [Primary / Secondary / Anecdotal] | [Fresh / Acceptable / Stale] | [Direct / Partial / Indirect] | [Low / Medium / High] | [High / Medium / Low] | [notes] |

### Conflict Resolution

| Conflict ID | Preferred Source | Reason |
|---|---|---|
| CON-001 | [SRC-ID] | [reason] |

### Evidence Caveats
- [caveat]

---

## Business Rules Found

| Rule ID | Candidate Business Rule | Source ID | Status | Notes |
|---|---|---|---|---|
| BR-C-001 | [candidate rule] | SRC-001 | [Confirmed / Conflict / Needs Clarification] | [notes] |

---

## Terminology

| Term | Meaning | Source ID | Notes |
|---|---|---|---|
| [term] | [definition] | SRC-001 | [notes] |

---

## Dependencies

| Dependency ID | Dependency | Type | Source ID | Impact |
|---|---|---|---|---|
| DEP-001 | [dependency] | [System / API / Data / Product / Legal / Ops] | SRC-001 | [impact] |

---

## Tech Trend Context

> Fill only when the topic involves a technology trend, tool, framework, platform shift, or emerging engineering practice.  
> Supporting artifacts: `Tech-Trend-Summary`, `Tech-Macro-Regime-Report`, `Tech-Trend-Watchlist`, `Tech-Trend-Scorecard`, `Tech-Source-Registry`.

### Trend Stage

[early-research / developer-adoption / production-adoption / enterprise-adoption / hype-cycle / decline / maintenance / N/A]

### Trend Signal Summary

| Signal | Source ID | Strength | Notes |
|---|---|---|---|
| [signal] | SRC-001 | [High / Medium / Low] | [notes] |

### Adoption Evidence

| Evidence | Source ID | Impact |
|---|---|---|
| [evidence] | SRC-001 | [impact] |

### Hype / Crowdedness Check

| Check | Result | Notes |
|---|---|---|
| Production proof exists? | [Yes / No / Unknown] | [notes] |
| Community debate is substantive? | [Yes / No / Unknown] | [notes] |
| Vendor narrative dominates? | [Yes / No / Unknown] | [notes] |

### Invalidation Conditions

- [condition that weakens or invalidates the trend thesis]

### ITBA Impact

| BA Area | Impact | Recommendation |
|---|---|---|
| Scope | [impact] | [recommendation] |
| Functional Requirement | [impact] | [recommendation] |
| API / Integration | [impact] | [recommendation] |
| UX / Workflow | [impact] | [recommendation] |
| Risk / Assumption | [impact] | [recommendation] |

---

## Conflicts

| Conflict ID | Description | Sources | Impact | Needs Decision |
|---|---|---|---|---|
| CON-001 | [conflict] | SRC-001 vs SRC-002 | [impact] | [Yes / No] |

---

## Gaps & Open Questions

| Question ID | Gap / Question | Why It Matters | Suggested Owner | Blocks ITBA? |
|---|---|---|---|---|
| Q-001 | [question] | [reason] | [User / PM / Dev / BA] | [Yes / No] |

---

## Channel Evidence

### Web Research

> Skill: `agents/researcher/skills/research-web.md`  
> Fill only if web research was used.

[Overview, best practices, gotchas, comparisons, sources.]

### GitHub Research

> Skill: `agents/researcher/skills/research-github.md`  
> Fill only if GitHub research was used.

[Repo stats, top issues, breaking changes, maintainer activity, sources.]

### Community Research

> Skill: `agents/researcher/skills/research-community.md`  
> Fill only if community research was used. Label anecdotal evidence clearly.

[Sentiment, pain points, debates, trends, sources.]

### Docs Research

> Skill: `agents/researcher/skills/research-docs.md`  
> Fill only if official docs, changelogs, RFCs, roadmaps, or release notes were used.

[Official claims, changelog movement, RFC status, roadmap notes, compatibility constraints.]

### Market / Product / Funding Signals

> Skills: `research-market-map.md`, `research-product-signal.md`, `research-funding-signal.md`  
> Fill only if market landscape, product launch, pricing, integration, funding, hiring, or partnership evidence was used.

[Landscape, product adoption signals, funding/hiring movement, source caveats.]

---

## Recommendations

Recommendations are proposals, not approved requirements.

| Recommendation ID | Recommendation | Rationale | Source ID | Confidence |
|---|---|---|---|---|
| REC-001 | [recommendation] | [why] | SRC-001 | [High / Medium / Low] |

---

## Handoff To ITBA

| Handoff Item | Value |
|---|---|
| Research status | [Sufficient / Partial / Blocked] |
| Required next document | `Research-Intake-Execution` |
| Must ask user before BA? | [Yes / No] |
| Blocking questions | [Q IDs / N/A] |
| Key sources | [SRC IDs] |

---

## Knowledge Ingest

> Skill: `agents/researcher/skills/knowledge-ingest.md`  
> Optional. Propose only after report review.

```text
Ingest recommendation: [Yes / No]
Target path:           [knowledge/shared/pages/... or knowledge/projects/<project>/pages/...]
Tags:                  [tag1, tag2, tag3]
Category:              [TechStack / Domain / Architecture / Project / Other]
```
