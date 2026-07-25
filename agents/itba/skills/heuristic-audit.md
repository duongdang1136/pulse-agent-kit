# Skill: Heuristic Audit

**Command:** `/audit <screen>`  
**Agent:** ITBA  
**Output:** Heuristic audit report

Use this skill to review a screen or feature before approval or launch.

## Heuristics

```text
H1 - Clarity: User hiểu mục đích màn hình nhanh không?
H2 - Consistency: Follow Token Registry và Design System không?
H3 - Feedback: System có phản hồi mọi user action không?
H4 - Error Prevention: UI có ngăn user làm sai không?
H5 - Efficiency: User hoàn thành task với ít bước hợp lý không?
```

## Output Format

```markdown
## Heuristic Audit - [Screen/Feature]
**Date:** [YYYY-MM-DD]  **Auditor:** [name / AI]
**Version reviewed:** [Figma link / screenshot date]

### Summary
| Severity | Count |
|---|---|
| Critical | [N] |
| High | [N] |
| Medium | [N] |
| Low | [N] |

**Overall verdict:** [Pass / Conditional Pass / Fail]

### Issues Found

#### [SEVERITY-ID]: [Tên issue]
**Heuristic:** H[N] - [tên]
**Location:** [màn hình / component]
**Issue:** [mô tả]
**Impact:** [impact]
**Fix:** [suggestion]

### Recommendations
1. [Priority fix]
```
