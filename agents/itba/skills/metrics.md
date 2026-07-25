# Skill: Metrics Specification

**Command:** `/metrics <feature>`  
**Agent:** ITBA  
**Output:** Logging & Analyzing section

Use this skill when the feature requires event logging, analytics, audit logs, KPI definitions, or metric formulas.

## Output Format

```markdown
## Logging & Analyzing

### Log Define
| Log ID | Event Name | Trigger | Payload | Source | Owner |
|---|---|---|---|---|---|

### Log Update
| Log ID | Change Type | Previous Definition | New Definition | Reason | Impact |
|---|---|---|---|---|---|

### Metrics, Formula & Log Source
| Metric ID | Metric | Formula | Log Source | Notes |
|---|---|---|---|---|
```
