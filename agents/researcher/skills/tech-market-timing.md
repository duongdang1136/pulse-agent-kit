# Skill: Tech Market Timing

**Agent:** Researcher  
**Used by:** `tech-macro-regime.md`, `tech-trend-confirmation.md`  
**Output section:** Market Timing

Use this skill to decide whether a domain is too early, timely, too crowded, or already exhausted for product/engineering attention.

## Timing States

```text
too-early     - signal exists but practical adoption is weak
right-time    - signal, tooling, and adoption are converging
crowded       - many entrants, unclear differentiation
late          - mature default, low novelty
declining     - usage and ecosystem movement are shrinking
```

## Output

| Timing Factor | Evidence | Source ID | Assessment |
|---|---|---|---|
| Tool maturity | [evidence] | SRC-001 | [assessment] |
| Adoption momentum | [evidence] | SRC-001 | [assessment] |
| Competition density | [evidence] | SRC-001 | [assessment] |
| Switching cost | [evidence] | SRC-001 | [assessment] |

**Timing verdict:** [too-early / right-time / crowded / late / declining]
