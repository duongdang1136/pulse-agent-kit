# Skill Pack: Phase 2 — Design & Validate 🎨

**Commands:** `/wireframe`, `/wireframe-hifi`, `/review-stakeholder`, `/review-design`  
**Agent:** ITBA  
**Output:** Wireframe description / Prototype doc / Review report

> Skill pack đóng gói 2 case routing + 4 module type + 2 review module.

---

## Case Routing

```
Case 1 — BA Wireframe First:
  BA tự tạo wireframe (text-based) → mô tả cho designer → review loop
  Dùng khi: chưa có designer, hoặc BA cần define flow trước

Case 2 — Designer Design First:
  Designer đã có design → BA review → BA viết docs
  Dùng khi: designer đã mockup, hoặc redesign từ existing product
```

---

## Sub-skill A — Wireframe Lo-fi (`/wireframe`)

**Command:** `/wireframe <feature>`  
**Dùng cho:** Case 1 — khi chưa có design

**Role:** Senior UX Designer tạo wireframe text-based mô tả layout + interaction.

**Format output:**

```markdown
## Wireframe: [Feature Name]
**Type:** Lo-fi  **Date:** [YYYY-MM-DD]
**UC covered:** [UC-01, UC-02]

### Screen: [Tên màn hình]

**Layout:**
```
┌─────────────────────────────────────┐
│ HEADER (sticky)                     │
│  Logo | Nav: [item1] [item2] [item3] │
├─────────────────────────────────────┤
│ MAIN CONTENT                        │
│  ┌───────────┐  ┌─────────────────┐ │
│  │ SIDEBAR   │  │ CONTENT AREA    │ │
│  │ - Filter  │  │ [List items]    │ │
│  │ - Sort    │  │                 │ │
│  └───────────┘  └─────────────────┘ │
├─────────────────────────────────────┤
│ FOOTER                              │
└─────────────────────────────────────┘
```

**Components:**
- [Component 1]: [mô tả, states: default/hover/active/disabled]
- [Component 2]: [mô tả]

**Interaction Notes:**
- [Trigger 1] → [Action]: [Result]
- [Trigger 2] → [Action]: [Result]

**Edge States:**
- Empty state: [mô tả]
- Loading state: [mô tả — skeleton / spinner?]
- Error state: [mô tả]
```

---

## Sub-skill B — Wireframe Hi-fi (`/wireframe-hifi`)

**Command:** `/wireframe-hifi <feature>`  
**Dùng cho:** Case 1 — sau khi lo-fi approved, cần chi tiết hơn cho designer

Tương tự Lo-fi nhưng thêm:
- Chỉ định token cụ thể: `--color-bg-primary`, `--spacing-4`
- Typography spec: font size, weight, line-height
- Animation spec: duration, easing
- Figma frame naming convention

---

## Sub-skill C — UI to Spec (Case 2 — `/screen`)

**Command:** `/screen <description hoặc screenshot>`  
**Dùng cho:** Case 2 — khi designer đã có design, BA cần đọc UI → viết spec

**Flow:**

```
Bước 1: BA tải screenshot / paste mô tả UI
Bước 2: AI phân tích UI → Flow Documentation
  - Trigger, End State
  - Step-by-step table (Happy Path + Alternative Paths)
  - Loading, Error, Drawer states
Bước 3: BA review flow → approve
Bước 4: AI generate Use Case List từ flow đã chốt
Bước 5: Export Screen Description file
```

**Screen Description output format:**

```markdown
## Screen: [Tên màn hình]
**Screen ID:** SCR-[N]

### Layout Overview
[Mô tả tổng thể layout]

### Components & Fields

**[Field/Component Name]**
- UI Control: [Textbox / Dropdown / Radio / Checkbox / Button / Upload Zone...]
- Data Type: [String / Integer / Boolean / Date / Image] ([ReadOnly / Editable / Hidden / Auto-fill])
- Rules & Validation:
  - Default: [giá trị/trạng thái mặc định]
  - Constraint: [Required / Optional]
  - Limits: [Min/Max chars, file size...]
  - Allowed: [whitelist format/ký tự hợp lệ]
  - Blocked: [blacklist/regex]
- Interaction:
  - On-action: [click field này gọi component nào lên?]
  - Outcome: [data sync đi đâu sau khi update?]
- Edge Cases:
  - Error: [text error message chính xác trên UI]
  - Fallback: [UI tự xử lý không? VD: auto uppercase]

### Flow Documentation
| Step | Actor | Action | System Response |
|---|---|---|---|
| 1 | User | [action] | [response] |

**Trigger:** [điều kiện bắt đầu flow]
**End State:** [trạng thái kết thúc]
**Alternative Paths:** [loading / error / empty / cancel]
```

---

## Sub-skill D — Review Stakeholder (`/review-stakeholder`)

**Dùng khi:** Cần stakeholder approve trước khi proceed

**Output format:**

```markdown
## Stakeholder Review — [Feature]
**Date:** [YYYY-MM-DD]  **Presenter:** [BA name]

### What we're reviewing
[1-2 câu mô tả scope]

### Design decisions made
| Decision | Rationale | Alternative considered |
|---|---|---|

### Open questions for stakeholder
| # | Question | Impact nếu không trả lời |
|---|---|---|

### Sign-off required
- [ ] [Stakeholder 1] — [role]
- [ ] [Stakeholder 2] — [role]
```

---

## Sub-skill E — Design Critique (`/review-design`)

**Dùng khi:** Internal review trước khi đưa cho stakeholder

**Framework 5 lenses:**

```
Lens 1 — Consistency: có follow Token Registry và Layout System không?
Lens 2 — Clarity: user hiểu được không ở lần nhìn đầu tiên?
Lens 3 — Completeness: đã cover đủ edge states (empty/error/loading)?
Lens 4 — Accessibility: contrast ratio, focus state, screen reader?
Lens 5 — Feasibility: dev có implement được không với tech stack hiện tại?
```

**Output format:**

```markdown
## Design Critique — [Feature]
**Date:** [YYYY-MM-DD]

### Pass ✅
- [Điểm tốt 1]

### Issues 🔴
| # | Issue | Lens | Severity | Fix suggestion |
|---|---|---|---|---|
| 1 | [mô tả] | Consistency | High | [suggestion] |

### Recommendation
[Overall recommendation: Approve / Revise / Major rework]
```
