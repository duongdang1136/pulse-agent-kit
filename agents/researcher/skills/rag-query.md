# Skill: RAG Query

**Command:** `/rag <query>`  
**Agent:** Researcher  
**Output:** RAG lookup result from shared/project knowledge

Use this skill before new research to check whether relevant knowledge already exists.

## Goal

- Normalize the query.
- Search `knowledge/shared/.rag/index.json`.
- Search `knowledge/projects/<project>/.rag/index.json` when project context exists.
- Return HIT / PARTIAL / MISS with source paths.
- Do not trigger web/GitHub/community research.
- Do not ingest new knowledge.

## Output Format

```markdown
## RAG Query Result

**Query:** [query]
**Project:** [project / N/A]
**Status:** [HIT / PARTIAL / MISS]
**Confidence:** [High / Medium / Low]

### Matched Knowledge
| Source ID | Path | Title | Relevance | Notes |
|---|---|---|---|---|

### Coverage Check
| Question | Result |
|---|---|
| Content answers query directly? | [Yes / Partial / No] |
| Has examples/data? | [Yes / Partial / No] |
| Covers requested angle? | [Yes / Partial / No] |
| Missing aspects? | [list / N/A] |
```
