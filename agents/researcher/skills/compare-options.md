# Skill: Compare Options

**Command:** `/compare <option-a> vs <option-b> ...`  
**Agent:** Researcher  
**Output:** `Comparison-Report`

Use this skill when the user needs to compare tools, vendors, libraries, approaches, architectures, product options, or implementation strategies.

## Goal

- Define decision context.
- Identify options and alternatives.
- Define evaluation criteria before comparing.
- Compare options using evidence, not preference.
- Separate facts, trade-offs, assumptions, and recommendations.
- Produce `templates/Comparison-Report.md`.

## Rules

```text
1. Do not compare without criteria.
2. Every score must have rationale and source.
3. Do not treat recommendation as final decision.
4. Label missing data as N/A or Needs Research.
5. If criteria weights are unknown, use equal weight and mark as assumption.
```

## Output Contract

Use `agents/researcher/templates/Comparison-Report.md`.
