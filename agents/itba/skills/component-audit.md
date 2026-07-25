# Skill: Component Audit

**Command:** `/audit-component <component>`  
**Agent:** ITBA  
**Output:** Component audit report

Use this skill to audit component anatomy, states, variants, and token compliance.

## Output Format

```markdown
## Component Audit - [Component Name]
**Date:** [YYYY-MM-DD]

### Anatomy Check
| Part | Present | Notes |
|---|---|---|

### States Check
| State | Present | Token compliant | Notes |
|---|---|---|---|

### Token Violations
| Property | Current value | Should be |
|---|---|---|

### Verdict
[Pass / Needs revision]
```
