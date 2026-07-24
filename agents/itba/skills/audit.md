# Skill Pack: Audit 🔍

**Commands:** `/audit`, `/audit-component`, `/audit-layout`  
**Agent:** ITBA  
**Output:** Audit Report

> Standalone skill — có thể dùng bất kỳ lúc nào, không cần chạy Phase 0-3 trước.

---

## Khi nào dùng

- Nhận design mới cần review trước khi approve
- Cần audit system đang có (periodic / post-redesign)
- QA phát hiện inconsistency, cần BA audit lại

---

## Sub-skill 1 — Heuristic Review (`/audit <screen>`)

**Role:** Senior UX Auditor — đánh giá toàn diện theo 5 heuristics custom.

**5 Heuristics:**

```
H1 — Clarity: User hiểu được mục đích màn hình trong 5 giây không?
  Check: heading rõ không? CTA rõ không? Information hierarchy đúng không?

H2 — Consistency: Follow Token Registry và Design System không?
  Check: colors, spacing, typography, component behavior có nhất quán?

H3 — Feedback: System có phản hồi với mọi user action không?
  Check: loading state, success state, error state có đầy đủ?

H4 — Error Prevention: UI có ngăn user làm sai không?
  Check: validation, confirmation dialog, undo/redo, destructive action warning?

H5 — Efficiency: User có thể hoàn thành task với ít bước nhất không?
  Check: click count, form length, shortcut, progressive disclosure?
```

**Severity scale:**

```
🔴 Critical    — Block launch. User không thể hoàn thành core task.
🟠 High        — Fix before launch. User experience bị hỏng đáng kể.
🟡 Medium      — Fix in next sprint. Annoying nhưng có workaround.
🟢 Low         — Nice-to-have. Polish khi có thời gian.
```

**Output format:**

```markdown
## Heuristic Audit — [Screen/Feature]
**Date:** [YYYY-MM-DD]  **Auditor:** [name / AI]
**Version reviewed:** [Figma link / screenshot date]

### Summary
| Severity | Count |
|---|---|
| 🔴 Critical | [N] |
| 🟠 High | [N] |
| 🟡 Medium | [N] |
| 🟢 Low | [N] |

**Overall verdict:** [Pass / Conditional Pass / Fail]

---

### Issues Found

#### 🔴 [CRITICAL-01]: [Tên issue]
**Heuristic:** H[N] — [tên]  
**Location:** [màn hình / component cụ thể]  
**Issue:** [mô tả vấn đề]  
**Impact:** [user bị ảnh hưởng như thế nào]  
**Fix:** [suggestion cụ thể]

---

#### 🟠 [HIGH-01]: [Tên issue]
[tương tự]

---

### What's Working Well ✅
- [Điểm tốt 1]
- [Điểm tốt 2]

### Recommendations
1. [Priority fix 1]
2. [Priority fix 2]
```

---

## Sub-skill 2 — Component Audit (`/audit-component <name>`)

**Role:** Senior Design System Engineer — audit component theo 4 dimensions.

**4 Dimensions:**

```
Dimension 1 — Anatomy: component có đủ parts không? (label, icon, helper text, error state...)
Dimension 2 — States: default / hover / active / focus / disabled / loading / error — đủ chưa?
Dimension 3 — Variants: các variant có consistent pattern không?
Dimension 4 — Token compliance: có dùng đúng design tokens không? Có hardcode nào không?
```

**Output format:**

```markdown
## Component Audit — [Component Name]
**Date:** [YYYY-MM-DD]

### Anatomy Check
| Part | Present | Notes |
|---|---|---|
| Label | ✅ / ❌ | [note] |
| Icon | ✅ / ❌ | |
| Helper text | ✅ / ❌ | |
| Error message | ✅ / ❌ | |

### States Check
| State | Present | Token compliant | Notes |
|---|---|---|---|
| Default | ✅ | ✅ / ❌ | |
| Hover | ✅ / ❌ | | |
| Focus | ✅ / ❌ | | |
| Disabled | ✅ / ❌ | | |
| Loading | ✅ / ❌ | | |
| Error | ✅ / ❌ | | |

### Token Violations
| Property | Current value | Should be |
|---|---|---|
| background | #1A1A2E (hardcoded) | --color-bg-primary |

### Verdict
[Pass / Needs revision — list issues]
```

---

## Sub-skill 3 — Page Layout Audit (`/audit-layout <page>`)

**Audit modes:**

```
Mode A — Pre-launch Audit:   Check trước khi go-live
Mode B — Post-redesign Audit: So sánh before/after redesign
Mode C — Periodic Audit:     Quarterly check — token drift, consistency
Mode D — Token Drift Audit:  Focused — chỉ check token violations
```

**Output format:**

```markdown
## Page Layout Audit — [Page Name]
**Mode:** [A / B / C / D]  **Date:** [YYYY-MM-DD]

### Grid Compliance
- [ ] Columns follow Layout System (X columns)
- [ ] Gutter correct (Xpx)
- [ ] Max width respected (Xpx)
- [ ] Breakpoint behavior correct

### Spacing Violations
| Element | Current | Expected | Token |
|---|---|---|---|
| [element] | 14px | 16px | --spacing-4 |

### Typography Violations
| Element | Current | Expected |
|---|---|---|

### Token Drift (Mode C/D)
| Token | Expected value | Actual value | File |
|---|---|---|---|

### Verdict
[Pass / N violations found — priority list]
```
