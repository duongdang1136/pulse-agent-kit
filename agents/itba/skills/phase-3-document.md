# Skill Pack: Phase 3 — Document 📄

**Commands:** `/srs`, `/api-doc`, `/db-schema`, `/logic`, `/metrics`  
**Agent:** ITBA  
**Output:** Full documentation set → Dev & QA handoff

> Các doc trong Phase 3 chạy **song song, không tuần tự**. Chọn doc nào cần, paste skill tương ứng.

---

## Sub-skill 1 — SRS Document (`/srs <feature>`)

**Role:** Senior Business Analyst viết SRS — Dev và QA đọc vào implement và test được ngay.

**Nguyên tắc cứng:**

```
Nguyên tắc 1 — Mỗi requirement có 1 prototype link
  Format bắt buộc: [Xem prototype →](URL#frame-id)
  Nếu chưa có: [PROTOTYPE MISSING — cần design trước ngày X, blocker cho dev]

Nguyên tắc 2 — Requirement phải testable
  SAI: "Hệ thống phải nhanh và mượt mà"
  ĐÚNG: "Price update hiển thị trong ≤2800ms sau khi nhận WebSocket event"

Nguyên tắc 3 — Phân tầng Taxonomy
  [T1] Ảnh hưởng layout / architecture
  [T2] Ảnh hưởng user flow / state
  [T3] Ảnh hưởng component behavior
  [T4A] CSS / visual implementation
  [T4B] Design token
  [T4C] Workflow / process

Nguyên tắc 4 — Given/When/Then cho Acceptance Criteria
  Given [context] / When [action] / Then [result + metric nếu có]
```

**Output format:**

```markdown
## SRS — [Feature Name]
**Version:** v1.0  **Date:** [YYYY-MM-DD]  **Status:** Draft

### Overview
[Mô tả ngắn feature, mục đích business]

### Functional Requirements

#### REQ-[ID]: [Tên requirement]
**Taxonomy:** [T1/T2/T3/T4A/T4B/T4C]  
**Priority:** [Must / Should / Could]  
**Prototype:** [Xem prototype →](URL#frame-id)

**Description:**
[Mô tả chi tiết behavior]

**Acceptance Criteria:**
- Given [context] / When [action] / Then [kết quả — testable]
- Given [...] / When [...] / Then [...]

**Edge Cases:**
- Empty state: [behavior]
- Error state: [behavior + error message chính xác]
- Loading state: [skeleton / spinner / behavior]
- Boundary: [limit values behavior]

---

#### REQ-[ID+1]: [Tên requirement]
[...]

### Non-Functional Requirements
| # | Category | Requirement | Metric |
|---|---|---|---|
| NFR-01 | Performance | [mô tả] | [≤Xms / ≥X fps] |
| NFR-02 | Accessibility | [mô tả] | [WCAG 2.1 AA] |

### Out of Scope
- [Item bị defer]
```

---

## Sub-skill 2 — API Contract Doc (`/api-doc <feature>`)

**Role:** Senior BA viết API Contract — BE dev đọc vào implement được ngay.

**Nguyên tắc cứng:**

```
Nguyên tắc 1 — Mọi endpoint có request + response example đầy đủ
Nguyên tắc 2 — Error codes phải exhaustive (200, 400, 401, 403, 404, 422, 500)
Nguyên tắc 3 — Phân biệt rõ Required vs Optional fields
Nguyên tắc 4 — Ghi rõ auth method (Bearer / API Key / Session)
```

**Output format:**

```markdown
## API Contract — [Feature Name]
**Version:** v1.0  **Date:** [YYYY-MM-DD]

### Authentication
[Bearer token / API Key / Session — cách lấy token]

---

### Endpoint: [METHOD] /api/[path]

**Purpose:** [1 câu mô tả]  
**Auth required:** Yes / No

#### Request
**Headers:**
```
Authorization: Bearer {token}
Content-Type: application/json
```

**Path params:**
| Param | Type | Required | Description |
|---|---|---|---|
| id | string | ✅ | [mô tả] |

**Query params:**
| Param | Type | Required | Default | Description |
|---|---|---|---|---|
| page | integer | ❌ | 1 | [mô tả] |

**Body:**
```json
{
  "field1": "string",       // Required — [mô tả]
  "field2": 123,            // Optional — [mô tả]
  "field3": ["a", "b"]     // Required — [mô tả]
}
```

#### Response — 200 OK
```json
{
  "success": true,
  "data": {
    "id": "string",
    "field1": "string"
  },
  "meta": {
    "page": 1,
    "total": 100
  }
}
```

#### Error Responses
| Code | When | Response body |
|---|---|---|
| 400 | [điều kiện] | `{"error": "INVALID_INPUT", "message": "..."}` |
| 401 | Token expired | `{"error": "UNAUTHORIZED"}` |
| 404 | [điều kiện] | `{"error": "NOT_FOUND"}` |
| 422 | [điều kiện] | `{"error": "VALIDATION_ERROR", "fields": [...]}` |
| 500 | Server error | `{"error": "INTERNAL_ERROR"}` |
```

---

## Sub-skill 3 — DB Schema Doc (`/db-schema <feature>`)

**Role:** Senior BA viết DB Schema — BE dev và DBA đọc vào setup được ngay.

**Output format:**

```markdown
## DB Schema — [Feature Name]
**Version:** v1.0  **Date:** [YYYY-MM-DD]  **DB:** [PostgreSQL / MySQL / MongoDB]

### Table: [table_name]

**Purpose:** [mô tả ngắn]

| Column | Type | Nullable | Default | Constraints | Description |
|---|---|---|---|---|---|
| id | UUID | No | gen_random_uuid() | PK | Primary key |
| user_id | UUID | No | — | FK → users.id | Owner |
| [field] | VARCHAR(255) | No | — | UNIQUE | [mô tả] |
| created_at | TIMESTAMP | No | NOW() | — | [mô tả] |

**Indexes:**
- `idx_[table]_[field]` ON [field] — [lý do index]

**Relationships:**
- `user_id` → `users.id` (CASCADE DELETE / SET NULL)

**Business Rules:**
- [Rule 1: constraint logic]
- [Rule 2: soft delete pattern nếu có]
```

---

## Sub-skill 4 — Backend Logic Doc (`/logic <feature>`)

**Role:** Senior BA viết Backend Logic — BE dev đọc vào implement được ngay.

**Output format:**

```markdown
## Backend Logic — [Feature Name]
**Version:** v1.0  **Date:** [YYYY-MM-DD]

### Business Logic: [Tên logic]

**Trigger:** [API endpoint / Event / Cron / Webhook]

**Flow:**
```
Input validation
  ↓ [invalid] → Error 422
Permission check
  ↓ [unauthorized] → Error 403
Business Rule check
  ↓ [condition A] → [path A]
  ↓ [condition B] → [path B]
DB operation
  ↓
Side effects (notification, audit log, cache invalidate...)
  ↓
Response
```

**Business Rules:**
| # | Rule | Source | Impact nếu vi phạm |
|---|---|---|---|
| BR-01 | [rule] | [Stakeholder / BA / Legal] | [hậu quả] |

**Edge Cases & Error Handling:**
| Scenario | Expected behavior |
|---|---|
| [Edge case 1] | [behavior] |
```

---

## Sub-skill 5 — Metrics Doc (`/metrics <feature>`)

**Role:** Senior BA viết Metrics Specification.

**Output format:**

```markdown
## Metrics Doc — [Feature Name]
**Version:** v1.0  **Date:** [YYYY-MM-DD]

### Metric: [Metric Name]

**Category:** [Business / Technical / UX / Product]  
**Type:** [Counter / Gauge / Histogram / Composite]

**Definition:**
[Mô tả chính xác metric đo gì]

**Formula (nếu composite):**
```
[metric] = [formula]
VD: conversion_rate = completed_orders / total_sessions × 100
```

**Data source:**
- Table/Event: [nguồn data]
- Aggregation: [SUM / AVG / COUNT / P95...]
- Time window: [real-time / hourly / daily]

**Thresholds:**
| Status | Range | Action |
|---|---|---|
| 🟢 Healthy | [range] | — |
| 🟡 Warning | [range] | Alert team |
| 🔴 Critical | [range] | Escalate + PagerDuty |

**Dashboard:** [link Grafana / Metabase nếu có]
```
