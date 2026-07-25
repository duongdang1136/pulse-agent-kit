# Skill: Layout Audit

**Command:** `/audit-layout <page>`  
**Agent:** ITBA  
**Output:** Page layout audit report

Use this skill to audit grid, spacing, typography, responsive behavior, and token drift at page level.

## Output Format

```markdown
## Page Layout Audit - [Page Name]
**Mode:** [Pre-launch / Post-redesign / Periodic / Token Drift]
**Date:** [YYYY-MM-DD]

### Grid Compliance
- [ ] Columns follow Layout System
- [ ] Gutter correct
- [ ] Max width respected
- [ ] Breakpoint behavior correct

### Spacing Violations
| Element | Current | Expected | Token |
|---|---|---|---|

### Typography Violations
| Element | Current | Expected |
|---|---|---|

### Verdict
[Pass / N violations found]
```
