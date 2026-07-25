# Skill: Design Critique

**Command:** `/review-design`  
**Agent:** ITBA  
**Output:** Internal design critique

Use this skill for internal review before stakeholder approval.

## Review Lenses

```text
1. Consistency: follow Token Registry and Layout System?
2. Clarity: can users understand the screen quickly?
3. Completeness: empty/error/loading states covered?
4. Accessibility: contrast, focus, screen reader baseline?
5. Feasibility: can dev implement with current stack?
```

## Output Format

```markdown
## Design Critique - [Feature]
**Date:** [YYYY-MM-DD]

### Pass
- [Điểm tốt]

### Issues
| # | Issue | Lens | Severity | Fix suggestion |
|---|---|---|---|---|

### Recommendation
[Approve / Revise / Major rework]
```
