# Skill: Research Plan

**Command:** `/research <topic>`  
**Agent:** Researcher  
**Output:** Research plan for full Researcher workflow

Use this skill as the entry point for full research. It coordinates RAG lookup, routing, selected source/channel skills, evidence evaluation, and synthesis. It does not replace the channel-specific skills.

## Required Flow

```text
1. Run rag-query.
2. Run research-routing.
3. Run only selected source/channel skills:
   - research-web
   - research-docs
   - research-github
   - research-community
   - research-market-map
   - research-product-signal
   - research-funding-signal
4. Run synthesize.
5. Produce Research-Report.
6. Propose knowledge-ingest only if useful; do not auto-ingest.
```

## Output Format

```markdown
## Research Plan

**Topic:** [topic]
**Project:** [project / N/A]
**Purpose:** [why research is needed]

### Selected Inputs
| Input | Required | Notes |
|---|---|---|
| User request | Yes | [notes] |
| Project source docs | [Yes / No] | [notes] |
| Project knowledge | [Yes / No] | [notes] |
| External web | [Yes / No] | [notes] |
| Official docs / changelog / RFC | [Yes / No] | [notes] |
| GitHub | [Yes / No] | [notes] |
| Community | [Yes / No] | [notes] |
| Market map | [Yes / No] | [notes] |
| Product signal | [Yes / No] | [notes] |
| Funding / hiring signal | [Yes / No] | [notes] |

### Execution Order
1. [step]
2. [step]

### Research Questions
- [question 1]
- [question 2]
```
