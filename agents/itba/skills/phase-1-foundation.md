# Skill Pack: Phase 1 — Foundation 🏛️

**Commands:** `/persona`, `/ia`, `/layout`, `/token`  
**Agent:** ITBA  
**Output:** Foundation docs — prerequisite trước khi wireframe/design

> Skill pack đóng gói 4 foundation sub-skills. Chọn sub-skill cần dùng, paste MODULE TARGET tương ứng.

---

## Khi nào cần Foundation

Foundation là "xương sống" — phải build TRƯỚC khi wireframe/design:

```
Persona & Mental Model  → Gate: phải có trước IA
Information Architecture → Gate: cần Persona ✓
Layout System           → Gate: cần IA ✓
Token Registry          → Gate: cần Layout System ✓
```

Nếu project đã có Foundation → kiểm tra version, update nếu cần, rồi bỏ qua.

---

## Sub-skill 1 — User Persona & Mental Model (`/persona`)

**Role:** Senior UX Researcher chuyên Mental Model Analysis.

**Nguyên tắc cứng:**

```
Nguyên tắc 1 — Không bịa hành vi
Mọi insight phải có tag nguồn gốc:
  [OBSERVED]   → quan sát trực tiếp / session recording
  [INTERVIEW]  → từ user interview có transcript
  [SURVEY]     → từ khảo sát có sample size
  [ANALYTICS]  → từ GA, Mixpanel, Hotjar
  [ASSUMED]    → team giả định, chưa verify
  [BORROWED]   → từ research sản phẩm tương tự

Rule: >50% claims gắn [ASSUMED] → persona chưa đủ tin, phải ghi cảnh báo.

Nguyên tắc 2 — Mental Model ≠ Demographics
Mental Model = user NGHĨ hệ thống hoạt động như thế nào
Gap giữa Mental Model và thực tế = nơi UX fail
→ Document gap này là mục tiêu chính

Nguyên tắc 3 — Persona gắn với Design Implications
Mỗi persona PHẢI có "Design Implications" section
Persona không dẫn đến quyết định design nào → vô dụng

Nguyên tắc 4 — Phân biệt Primary vs Anti-Persona
Anti-Persona: user sẽ dùng nhưng KHÔNG design for
Thiếu Anti-Persona → edge case user kéo design sai hướng
```

**Output format:**

```markdown
## Persona: [Tên Persona]
**Type:** Primary / Secondary / Anti-Persona
**Source confidence:** [High / Medium / Low — % claims có source thực]

### Demographics (context only)
[Tuổi, nghề, tech literacy — gắn tag source]

### Mental Model
**Họ nghĩ hệ thống hoạt động như thế nào:**
- [Belief 1] [TAG]
**Reality gap:**
- [Gap 1] → UX implication: [...]

### Goals & Motivations
- [Goal 1] [TAG]

### Pain Points
- [Pain 1] [TAG]

### Behavior Patterns
- [Pattern 1] [TAG]

### Design Implications
- [ ] [Decision 1 rút ra từ persona này]
- [ ] [Decision 2]
```

---

## Sub-skill 2 — Information Architecture (`/ia`)

**Role:** Senior Information Architect chuyên Web App, Dashboard.

**Nguyên tắc cứng:**

```
Nguyên tắc 1 — Naming từ user, không từ team
Labels phải validate bằng:
  [USER-TESTED]   → Card sorting / Tree testing
  [USER-LANGUAGE] → Đúng từ user hay dùng trong interview
  [TEAM-DECIDED]  → Team tự đặt, chưa validate
Warning: >30% labels gắn [TEAM-DECIDED] → cần Card Sorting session

Nguyên tắc 2 — 4 IA artifacts riêng biệt
  CONTENT INVENTORY  → Danh sách mọi content đang tồn tại
  CONTENT HIERARCHY  → Quan hệ cha-con giữa content/section
  NAVIGATION SYSTEM  → Cách user di chuyển giữa các node
  NAMING CONVENTION  → Quy tắc đặt tên nhất quán

Nguyên tắc 3 — Phân biệt Navigation vs Content
Navigation = cấu trúc menu/sidebar
Content = cái gì hiển thị trên từng page
Đừng nhầm lẫn 2 cái này
```

**Output format:**

```markdown
## Information Architecture — [Product]
**Version:** v[X]  **Date:** [YYYY-MM-DD]

### Content Inventory
| ID | Content | Type | Location hiện tại | Status |
|---|---|---|---|---|

### Content Hierarchy
[Tree hoặc indented list]

### Navigation System
**Primary Nav:** [list items] [TAG]
**Secondary Nav:** [list items] [TAG]
**Breadcrumb pattern:** [mô tả]

### Naming Convention
| Pattern | Rule | Ví dụ |
|---|---|---|
```

---

## Sub-skill 3 — Layout System (`/layout`)

**Role:** Senior UI Architect chuyên Layout Systems.

**Output format:**

```markdown
## Layout System — [Product]
**Version:** v[X]  **Date:** [YYYY-MM-DD]

### Grid System
- Columns: [12 / 16 / custom]
- Gutter: [Xpx]
- Margin: [Xpx]
- Max content width: [Xpx]

### Breakpoints
| Name | Min width | Columns | Gutter |
|---|---|---|---|
| Mobile | 0px | 4 | 16px |
| Tablet | 768px | 8 | 24px |
| Desktop | 1280px | 12 | 32px |

### Page Templates
| Template | Dùng cho | Layout mô tả |
|---|---|---|
| [Dashboard] | Trang data chính | [mô tả grid] |

### Component Placement Rules
- [Rule 1: Nav luôn sticky top]
- [Rule 2: Sidebar width cố định Xpx]
```

---

## Sub-skill 4 — Token Registry (`/token`)

**Role:** Senior Design System Engineer chuyên Design Tokens.

**Nguyên tắc cứng:**

```
3-layer token system bắt buộc:
  Layer 1 — Global Tokens:  màu raw (#1A1A2E), không dùng trực tiếp
  Layer 2 — Semantic Tokens: --color-bg-primary, --color-text-muted
  Layer 3 — Component Tokens: --button-primary-bg, --card-border

Dev KHÔNG được hardcode hex. Chỉ dùng Layer 2/3.
```

**Output format:**

```markdown
## Token Registry — [Product]
**Version:** v[X]  **Date:** [YYYY-MM-DD]

### Color Tokens
#### Global (Raw)
| Token | Value |
|---|---|
| --raw-brand-primary | #[hex] |

#### Semantic
| Token | Value | Dùng cho |
|---|---|---|
| --color-bg-primary | --raw-[...] | Background chính |
| --color-text-muted | --raw-[...] | Text phụ |

#### Component
| Token | Value | Component |
|---|---|---|
| --button-primary-bg | --color-bg-primary | Button |

### Spacing Tokens
[Tương tự — 4px base scale]

### Typography Tokens
[Font size, weight, line-height]
```

---

## MODULE TARGET — Foundation Input

```
FOUNDATION MODULE TARGET

Sub-skill:     [ ] Persona  [ ] IA  [ ] Layout  [ ] Token
Product name:  [tên product]
Phase 0 done:  [ ] Có Research Report từ Phase 0

EXISTING FOUNDATION (version đã có):
Persona:        [v? / chưa có]
IA:             [v? / chưa có]
Layout:         [v? / chưa có]
Token:          [v? / chưa có]

CONTEXT (paste từ Phase 0 Research Report nếu có):
[...]

SOURCE DATA (nếu có — interview, analytics, design files):
[...]
```
