# Audit Report Template

**Dùng cho:** ITBA Agent  
**Output của:** `/audit`, `/audit-component`, `/audit-layout`

---

## Skill Map

| Audit Mode | Command | Skill | Khi dùng |
|---|---|---|---|
| Heuristic Audit | `/audit <screen>` | `agents/itba/skills/heuristic-audit.md` | Review screen/feature theo UX heuristics |
| Component Audit | `/audit-component <component>` | `agents/itba/skills/component-audit.md` | Review component anatomy, states, variants, token compliance |
| Layout Audit | `/audit-layout <page>` | `agents/itba/skills/layout-audit.md` | Review grid, spacing, typography, responsive, token drift |

---

## Report Header

```text
Audit target:      [Screen / Component / Page / Feature]
Project:           [Tên project]
Audit mode:        [Heuristic / Component / Layout]
Command:           [/audit / /audit-component / /audit-layout]
Skill:             [skill file]
Date:              [YYYY-MM-DD]
Auditor:           [tên / AI]
Version reviewed:  [Figma link / screenshot date / component version / page version]
Related document:  [BA Document / Foundation / Prototype / N/A]
```

---

## Summary

| Severity | Count |
|---|---|
| Critical | [N] |
| High | [N] |
| Medium | [N] |
| Low | [N] |

**Overall verdict:** [Pass / Conditional Pass / Fail]  
**Launch impact:** [Block launch / Fix before launch / Fix next sprint / No blocker]

---

## Mode A - Heuristic Audit

> Skill: `agents/itba/skills/heuristic-audit.md`  
> Fill this section only when `Audit mode = Heuristic`.

### Heuristic Coverage

| Heuristic | Coverage | Notes |
|---|---|---|
| H1 - Clarity | [Pass / Issue / N/A] | [notes] |
| H2 - Consistency | [Pass / Issue / N/A] | [notes] |
| H3 - Feedback | [Pass / Issue / N/A] | [notes] |
| H4 - Error Prevention | [Pass / Issue / N/A] | [notes] |
| H5 - Efficiency | [Pass / Issue / N/A] | [notes] |

### Issues By Severity

#### [SEVERITY-ID]: [Tên issue]

| Field | Detail |
|---|---|
| Heuristic | [H1-H5] |
| Location | [screen / component / section] |
| Issue | [mô tả vấn đề] |
| Impact | [user/business/dev impact] |
| Fix | [suggestion cụ thể] |
| Owner | [BA / Design / Dev / PM] |
| Status | [Open / Fixed / Accepted Risk] |

---

## Mode B - Component Audit

> Skill: `agents/itba/skills/component-audit.md`  
> Fill this section only when `Audit mode = Component`.

### Anatomy Check

| Part | Present | Required | Notes |
|---|---|---|---|
| Label | [Yes / No] | [Yes / No] | [notes] |
| Icon | [Yes / No] | [Yes / No] | [notes] |
| Helper text | [Yes / No] | [Yes / No] | [notes] |
| Error message | [Yes / No] | [Yes / No] | [notes] |

### States Check

| State | Present | Token Compliant | Notes |
|---|---|---|---|
| Default | [Yes / No] | [Yes / No / N/A] | [notes] |
| Hover | [Yes / No] | [Yes / No / N/A] | [notes] |
| Active | [Yes / No] | [Yes / No / N/A] | [notes] |
| Focus | [Yes / No] | [Yes / No / N/A] | [notes] |
| Disabled | [Yes / No] | [Yes / No / N/A] | [notes] |
| Loading | [Yes / No] | [Yes / No / N/A] | [notes] |
| Error | [Yes / No] | [Yes / No / N/A] | [notes] |

### Variant Check

| Variant | Present | Behavior Consistent | Notes |
|---|---|---|---|
| [variant] | [Yes / No] | [Yes / No] | [notes] |

### Token Violations

| Property | Current Value | Expected Token / Value | Location | Severity |
|---|---|---|---|---|
| [property] | [value] | [token/value] | [file/component] | [Critical / High / Medium / Low] |

---

## Mode C - Layout Audit

> Skill: `agents/itba/skills/layout-audit.md`  
> Fill this section only when `Audit mode = Layout`.

### Grid Compliance

| Check | Expected | Actual | Status | Notes |
|---|---|---|---|---|
| Columns | [expected] | [actual] | [Pass / Issue] | [notes] |
| Gutter | [expected] | [actual] | [Pass / Issue] | [notes] |
| Margin | [expected] | [actual] | [Pass / Issue] | [notes] |
| Max width | [expected] | [actual] | [Pass / Issue] | [notes] |

### Responsive Check

| Breakpoint | Expected Behavior | Actual Behavior | Status |
|---|---|---|---|
| Mobile | [expected] | [actual] | [Pass / Issue] |
| Tablet | [expected] | [actual] | [Pass / Issue] |
| Desktop | [expected] | [actual] | [Pass / Issue] |

### Spacing Violations

| Element | Current | Expected | Token | Severity |
|---|---|---|---|---|
| [element] | [current] | [expected] | [token] | [Critical / High / Medium / Low] |

### Typography Violations

| Element | Current | Expected | Severity |
|---|---|---|---|
| [element] | [current] | [expected] | [Critical / High / Medium / Low] |

---

## Recommendations Priority

| Priority | Recommendation | Owner | Target |
|---|---|---|---|
| Immediate | [block launch fixes] | [owner] | [date/sprint] |
| Before launch | [high fixes] | [owner] | [date/sprint] |
| Next sprint | [medium fixes] | [owner] | [date/sprint] |
| Backlog | [low fixes] | [owner] | [date/sprint] |

---

## What's Working Well

- [Điểm tốt 1]
- [Điểm tốt 2]

---

## Sign-off

| Role | Decision | Date | Notes |
|---|---|---|---|
| BA | [Approve / Request revision] | [YYYY-MM-DD] | [notes] |
| Designer | [Approve / Request revision / N/A] | [YYYY-MM-DD] | [notes] |
| Dev Lead | [Approve / Request revision / N/A] | [YYYY-MM-DD] | [notes] |
