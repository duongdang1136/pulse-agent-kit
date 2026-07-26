# Skill: Research Routing

**Command:** `/research-route <topic>`  
**Agent:** Researcher  
**Output:** Research route plan

Use this skill after `rag-query.md` to decide which source/channel skills are needed. It selects evidence channels only; it does not decide final trend validity.

## Routing Rules

```text
1. If RAG status = HIT and coverage is sufficient, route to synthesize only.
2. If topic is a concept, product pattern, domain, policy, or feature behavior, include research-web.
3. If topic depends on official behavior, versioning, roadmap, standard, or migration, include research-docs.
4. If topic is a library, tool, repository, SDK, package, or source code dependency, include research-github.
5. If user asks about adoption, pain points, opinions, trend, or community sentiment, include research-community.
6. If topic needs vendor/category landscape, include research-market-map.
7. If topic needs launch, pricing, packaging, integration, or customer proof, include research-product-signal.
8. If topic needs funding, hiring, acquisition, partnership, or enterprise buying movement, include research-funding-signal.
9. If query is feature documentation for a project, prioritize project source docs and knowledge over external research.
```

## Output Format

```markdown
## Research Routing

**Topic:** [topic]
**RAG status:** [HIT / PARTIAL / MISS]
**Selected skills:** [research-web / research-docs / research-github / research-community / research-market-map / research-product-signal / research-funding-signal / synthesize]

### Rationale
| Skill | Use? | Reason |
|---|---|---|
| research-web | [Yes / No] | [reason] |
| research-docs | [Yes / No] | [reason] |
| research-github | [Yes / No] | [reason] |
| research-community | [Yes / No] | [reason] |
| research-market-map | [Yes / No] | [reason] |
| research-product-signal | [Yes / No] | [reason] |
| research-funding-signal | [Yes / No] | [reason] |
```
