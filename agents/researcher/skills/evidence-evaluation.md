# Skill: Evidence Evaluation

**Command:** `/evaluate-evidence <topic>`  
**Agent:** Researcher  
**Output:** Evidence Evaluation section in `Research-Report`

Use this skill to assess the quality, reliability, freshness, bias, and conflict level of research evidence.

## Evaluation Dimensions

```text
1. Authority: official/primary source vs secondary/anecdotal.
2. Freshness: source date, event date, version relevance.
3. Directness: directly answers question or only adjacent.
4. Reproducibility: can claim be verified or repeated.
5. Bias: vendor marketing, community anecdote, outdated docs, sample bias.
6. Conflict: whether sources disagree.
```

## Output Format

```markdown
## Evidence Evaluation

| Source ID | Authority | Freshness | Directness | Bias Risk | Reliability | Notes |
|---|---|---|---|---|---|---|
| SRC-001 | [Primary / Secondary / Anecdotal] | [Fresh / Acceptable / Stale] | [Direct / Partial / Indirect] | [Low / Medium / High] | [High / Medium / Low] | [notes] |

### Conflict Resolution
| Conflict ID | Preferred Source | Reason |
|---|---|---|

### Evidence Caveats
- [caveat]
```
