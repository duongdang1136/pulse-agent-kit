# BA Document Template 📋

**Dùng cho:** ITBA Agent — output cuối của full BA flow  
**Điền bởi:** Kết hợp Phase 0 → Phase 3 skills

---

## 🏷️ Document Header

```
Feature:        [Tên feature]
Project:        [Tên project]
Version:        v1.0
Date:           [YYYY-MM-DD]
BA:             [tên / AI]
Status:         [Draft / In Review / Approved]
Prototype:      [Figma URL / N/A]
```

---

## 📌 Executive Summary

> 2–4 câu tóm tắt: feature làm gì, tại sao cần, ai dùng, scope lần này.

---

## 🔬 Research & Execution Plan

> Skill: `skills/phase-0-research-plan.md` — `/ba-plan`

### Task Brief
[Tóm tắt requirement từ Phase 0 Section A]

### Context Analysis
[Existing assets, Business Rules từ Phase 0 Section B]

### Ambiguity Log
| # | Mô tả | Type | Status |
|---|---|---|---|
| 🔴 | [BLOCKER] | Blocker | Open / Resolved |
| 🟡 | [RISK] | Risk | Open / Resolved |

### Scope
- **IN:** [list]
- **OUT:** [list]
- **ASSUMPTIONS:** [list]

### Execution Plan
| Task | Phase | Estimate | Status |
|---|---|---|---|
| [Task 1] | Phase 1 | [Xh] | Done / In Progress |

---

## 🏛️ Foundation

> Skill: `skills/phase-1-foundation.md`  
> *(Điền link hoặc paste nội dung nếu build mới)*

| Foundation | Version | Link / Status |
|---|---|---|
| Persona & Mental Model | v[X] | [link / Built in doc] |
| Information Architecture | v[X] | [link / Built in doc] |
| Layout System | v[X] | [link / Built in doc] |
| Token Registry | v[X] | [link / Built in doc] |

---

## 🖼️ Screen Description

> Skill: `skills/ui-to-spec.md` — `/screen`

### Screen: [Tên màn hình]

**[1]. Field: [Tên Field]**
- UI Control: [...]
- Data Type: [...]
- Rules & Validation:
  - Default: [...]
  - Constraint: [Required / Optional]
  - Limits: [...]
- Interaction:
  - On-action: [...]
  - Outcome: [...]
- Edge Cases:
  - Error: "[text message chính xác]"
  - Fallback: [...]

*(Thêm fields theo mẫu trên)*

---

## 🔄 BPMN Flow

> Skill: `skills/ui-to-spec.md` — `/bpmn`

### Flow: [Tên Flow]

**Trigger:** [điều kiện bắt đầu]  
**End State:** [trạng thái kết thúc]

#### Happy Path
```
[User] → [Action]
             ↓
[System] → [Response] → END STATE ✅
```

#### Step Table
| Step | Actor | Action | System Response |
|---|---|---|---|

#### Alternative Paths
| Path | Trigger | Behavior |
|---|---|---|
| Loading | [...] | [...] |
| Error | [...] | "[message]" |
| Empty | [...] | [...] |

---

## 📋 Use Case List

> Skill: `skills/ui-to-spec.md` — `/usecase`

### UC-[ID]: [Tên Use Case]

**REQ ID:** REQ-[N]  **Taxonomy:** [T1/T2/T3/T4]  **Priority:** [Must/Should/Could]

**Acceptance Criteria:**
- Given [...] / When [...] / Then [...]

**Edge Cases:**
- [AC] [...] → [...]

---

## 📄 SRS Document

> Skill: `skills/phase-3-document.md` — `/srs`

### REQ-[ID]: [Tên requirement]

**Taxonomy:** [T1/T2/T3/T4]  **Priority:** [Must/Should/Could]  
**Prototype:** {{prototype_url}}

**Acceptance Criteria:**
- Given [...] / When [...] / Then [...]

**Edge Cases:**
- Empty: [...]
- Error: [...]
- Loading: [...]

---

## 🔌 API Contract

> Skill: `skills/phase-3-document.md` — `/api-doc`

### [METHOD] /api/[path]

*(Điền theo format trong phase-3-document.md)*

---

## 🗄️ DB Schema

> Skill: `skills/phase-3-document.md` — `/db-schema`

### Table: [table_name]

*(Điền theo format trong phase-3-document.md)*

---

## ⚙️ Backend Logic

> Skill: `skills/phase-3-document.md` — `/logic`

*(Điền theo format trong phase-3-document.md)*

---

## 📊 Metrics

> Skill: `skills/phase-3-document.md` — `/metrics`

*(Điền theo format trong phase-3-document.md)*

---

## ✅ Sign-off

| Role | Name | Date | Status |
|---|---|---|---|
| BA | [...] | [...] | Approved / Pending |
| PM | [...] | [...] | Approved / Pending |
| Dev Lead | [...] | [...] | Approved / Pending |
| Designer | [...] | [...] | Approved / Pending |
