# Skill Pack: UI to Spec 🖼️

**Commands:** `/screen`, `/bpmn`, `/usecase`  
**Agent:** ITBA  
**Output:** Screen Description + BPMN Flow + Use Case Detail List

> Dùng khi có UI/screenshot hoặc flow đã biết, cần convert sang structured documentation.

---

## Flow tổng thể (Khi có screenshot/design)

```
[/screen] Paste screenshot hoặc mô tả UI
    ↓
Sub-skill A: Screen Description — mô tả structured từng field/component
    ↓
[/bpmn] Từ Screen Description → Flow Documentation
    ↓
Sub-skill B: BPMN Flow — vẽ flow dạng text BPMN + step table
    ↓
[/usecase] Từ Flow đã chốt → Use Case List
    ↓
Sub-skill C: Use Case Detail — list UC theo format SRS-ready
    ↓
Export BA-Document.md
```

---

## Sub-skill A — Screen Description (`/screen`)

**Role:** Senior BA — phân tích UI và mô tả structured từng component.

**Input:** Screenshot, Figma URL, hoặc mô tả thô về màn hình

**Prompt để dùng:**

> *"Đóng vai Senior BA (ITBA-Skills Phase 2). Từ UI tôi cung cấp, phân tích và xuất ra Screen Description theo format bên dưới. Identify đủ components, fields, states, và edge cases."*

**Output format — per field/component:**

```markdown
**[Số thứ tự]. Field: [Tên Field thực tế]**

- **UI Control:** [Textbox / Dropdown Select / Radio / Checkbox / Toggle / Upload Zone / Button / Card / Table / Modal / Drawer...]
- **Data Type:** [String / Integer / Boolean / Date / Image / File] ([ReadOnly / Editable / Hidden / Auto-fill])
- **Rules & Validation:**
  - **Default:** [Dữ liệu/trạng thái tự động khi khởi tạo]
  - **Constraint:** [Required / Optional]
  - **Limits:** [Min/Max chars, file size, resolution...]
  - **Allowed (Accept):** [Whitelist — formats/ký tự hợp lệ]
  - **Blocked (Regex):** [Blacklist — formats/ký tự bị chặn]
- **Interaction:**
  - *On-action:* [Click field này có gọi component khác lên không? VD: bật calendar, dropdown, camera]
  - *Outcome:* [Data update thành công sync đi đâu? VD: App, Portal, System C]
- **Edge Cases & Error Handling:**
  - *Error:* [Text error message chính xác trên UI]
  - *Fallback:* [UI tự xử lý không? VD: auto uppercase, auto trim spaces]
```

**Cách dùng khi có bảng text vỡ (từ Word/Excel):**

> *"Đóng vai Senior BA (ITBA-Skills). Dưới đây là text bóc từ bảng Screen Description bị mất định dạng. Đọc hiểu logic và tái cơ cấu theo format Screen Description chuẩn. Giữ khắt khe validation rules."*

---

## Sub-skill B — BPMN Flow (`/bpmn`)

**Role:** Senior BA — vẽ flow BPMN text-based + step table.

**Command:** `/bpmn "<tên flow>"`

**Input:** Screen Description (từ /screen) hoặc mô tả flow

**Prompt để dùng:**

> *"Đóng vai Senior BA (ITBA-Skills). Từ màn hình/flow tôi mô tả, xuất ra BPMN Flow Documentation gồm: Flow diagram dạng text, Step table, và Alternative Paths đầy đủ (loading, error, cancel)."*

**Output format:**

```markdown
## BPMN Flow: [Tên Flow]
**Flow ID:** FLW-[N]  **Date:** [YYYY-MM-DD]
**UC covered:** [UC-01, UC-02]

### Trigger
[Điều kiện bắt đầu flow]

### End State
[Trạng thái kết thúc thành công]

### Happy Path
```
[User] → [Action 1]
             ↓
[System] → [Response 1]
             ↓
[User] → [Action 2]
             ↓
[System] → [Response 2] → END STATE ✅
```

### Step-by-step Table

| Step | Actor | Action | System Response | Notes |
|---|---|---|---|---|
| 1 | User | [action] | [response] | |
| 2 | System | [action] | [response] | |
| 3 | User | [action] | [response] | |

### Alternative Paths

**Loading State:**
| Step | Trigger | Behavior |
|---|---|---|
| [N] | [điều kiện] | Show skeleton / spinner — timeout sau Xs |

**Error State:**
| Step | Error | Message hiển thị | Recovery |
|---|---|---|---|
| [N] | [điều kiện] | "[text chính xác]" | [CTA cho user] |

**Empty State:**
| Trigger | UI shows | CTA |
|---|---|---|
| [điều kiện] | [empty state UI] | [action] |

**Cancel / Exit:**
| Step | Actor | Action | Result |
|---|---|---|---|
```

---

## Sub-skill C — Use Case Detail (`/usecase`)

**Role:** Senior BA — viết Use Case List SRS-ready với taxonomy và AC testable.

**Command:** `/usecase "<feature>"`

**Input:** Flow Documentation (từ /bpmn) hoặc mô tả feature

**Prompt để dùng:**

> *"Đóng vai Senior BA (ITBA-Skills Phase 3: SRS Doc). Từ flow đã chốt, viết Use Case List theo format bên dưới. Áp dụng tiêu chuẩn ITBA: mỗi UC là 1 REQ-[ID], phân tầng taxonomy T1-T4, AC dùng Given/When/Then và phải testable. Bổ sung Edge Cases."*

**Output format:**

```markdown
## Use Case List — [Feature]
**Version:** v1.0  **Date:** [YYYY-MM-DD]

---

### UC-[ID]: [Tên Use Case]

**REQ ID:** REQ-[N]  
**Taxonomy:** [T1/T2/T3/T4A/T4B/T4C]  
**Priority:** [Must / Should / Could]  
**Actor:** [User / System / Admin]  

**Precondition:**
- [Điều kiện phải đúng trước khi UC bắt đầu]

**Main Flow:**
1. [Bước 1]
2. [Bước 2]
3. [Bước 3]

**Acceptance Criteria:**
- Given [context] / When [action] / Then [kết quả — có metric nếu có]
- Given [...] / When [...] / Then [...]

**Alternative Flow / Edge Cases:**
- [AC] [điều kiện] → [behavior]
- [Error] [điều kiện] → [message + recovery]

**Out of scope:**
- [Item bị defer]

---

### UC-[ID+1]: [...]
```
