# Audit Report Template 🔍

**Dùng cho:** ITBA Agent — output của `/audit`, `/audit-component`, `/audit-layout`

---

## 🏷️ Report Header

```
Screen/Component: [Tên]
Project:          [Tên project]
Audit type:       [Heuristic / Component / Layout]
Date:             [YYYY-MM-DD]
Auditor:          [tên / AI]
Version reviewed: [Figma link / screenshot date / component version]
```

---

## 📊 Summary

| Severity | Count |
|---|---|
| 🔴 Critical | [N] |
| 🟠 High | [N] |
| 🟡 Medium | [N] |
| 🟢 Low | [N] |

**Overall verdict:** [Pass / Conditional Pass (fix before launch) / Fail]

---

## 🔴 Critical Issues

> Skill: `skills/audit.md` — phải fix trước khi launch

### [CRITICAL-01]: [Tên issue]
- **Type:** [Heuristic H1-H5 / Component Dim 1-4 / Layout]
- **Location:** [màn hình / component / section cụ thể]
- **Issue:** [mô tả vấn đề]
- **Impact:** [user bị ảnh hưởng như thế nào]
- **Fix:** [suggestion cụ thể]

---

## 🟠 High Issues

### [HIGH-01]: [Tên issue]
- **Type:** [...]
- **Location:** [...]
- **Issue:** [...]
- **Fix:** [...]

---

## 🟡 Medium Issues

### [MED-01]: [Tên issue]
[tương tự]

---

## 🟢 Low Issues (Polish)

- [Low-01]: [mô tả ngắn] → [fix suggestion]
- [Low-02]: [...]

---

## ✅ What's Working Well

- [Điểm tốt 1]
- [Điểm tốt 2]
- [Điểm tốt 3]

---

## 📋 Component/Token Violations (nếu có)

| Property | Current value | Should be | File/Location |
|---|---|---|---|
| background | #1A1A2E (hardcoded) | --color-bg-primary | Button.tsx |
| spacing | 14px | --spacing-4 (16px) | Card.tsx |

---

## 🎯 Recommendations Priority

1. **Immediate (block launch):** [list Critical fixes]
2. **Before launch:** [list High fixes]  
3. **Next sprint:** [list Medium fixes]
4. **Backlog:** [list Low fixes]

---

## ✅ Sign-off

| Role | Decision | Date |
|---|---|---|
| BA | [Approve / Request revision] | [...] |
| Designer | [Approve / Request revision] | [...] |
