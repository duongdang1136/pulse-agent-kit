# BA Document Template

**Dùng cho:** ITBA Agent - tài liệu handoff cho dev team  
**Điền bởi:** ITBA Agent dựa trên `Research-Intake-Execution` và các tài liệu liên quan  
**Bắt buộc trước:** `templates/Research-Intake-Execution.md`

## Section Skill Map

| Section | Required? | Skill | Why |
|---|---|---|---|
| 1. Document Header | Yes | `research-intake-execution.md` | Lấy metadata, source references, version baseline từ intake |
| 2. Executive Summary | Yes | `research-intake-execution.md` | Tóm tắt scope, why, platform, compliance đã được intake xác nhận |
| 3. Entry Points | Yes | `usecase.md`; optional `bpmn.md` | Xác định nơi user/system bắt đầu flow; flow diagram chỉ tạo khi user yêu cầu hoặc feature cần 1 flow tổng |
| 4. Use Case Summary | Yes | `usecase.md` | Tạo bảng tổng hợp UC để dev/QA scan nhanh |
| 5. Business Rule Global | Yes | `business-rules.md` | Tách rule dùng chung khỏi từng UC |
| 6. Use Case List | Yes | `usecase.md` + `acceptance-criteria.md` | Viết từng UC như capability và các scenario cụ thể bên trong UC |
| 7. Error Handling & User-Facing Copy | Yes | `screen.md` + `api-doc.md` + `acceptance-criteria.md`; optional `bpmn.md` | Gom copy, error behavior, recovery theo UI/API/UC |
| 8. UI Specific | Conditional | `wireframe-text.md` + `screen.md` | Bắt buộc khi feature có UI/user-facing state; `Wireframe Demo` chỉ dùng wireframe text |
| 9. Logging & Analyzing | Conditional | `metrics.md` | Bắt buộc khi có tracking, analytics, audit log, metric |
| 10. API Reference / Schema | Conditional | `api-doc.md` | Bắt buộc khi dev cần endpoint/schema |
| 11. CMS Tools | Conditional | `cms-tools.md` (`/cms-tools`) | Bắt buộc khi có admin/back-office/CMS vận hành |
| 12. Database | Conditional | `db-schema.md` | Bắt buộc khi có DB/table/collection/schema change |

---

## 1. Document Header

> Skill: `agents/itba/skills/research-intake-execution.md`  
> Purpose: đóng gói metadata, source baseline, disclaimer và history để dev biết tài liệu này dựa trên version nào.

```text
Feature:          [Tên feature]
Project:          [Tên project]
Version:          v1.0
Date:             [YYYY-MM-DD]
Status:           [Draft / In Review / Approved]
Owner BA:         [tên / AI]
Product Owner:    [tên / N/A]
Dev Lead:         [tên / N/A]
Designer:         [tên / N/A]
Research Intake:  [Link / reference to Research-Intake-Execution]
Prototype:        [Figma URL / N/A]
```

### 1.1 Metadata liên quan

| Field | Value |
|---|---|
| Feature ID | [ID / N/A] |
| Ticket / Epic | [link / ID / N/A] |
| Priority | [P0 / P1 / P2 / P3] |
| Target release | [release / sprint / N/A] |
| Platforms | [Web / iOS / Android / Smart TV / CMS / Backend / Other] |
| Regions | [VN / Global / Other] |
| Related teams | [team list] |

### 1.2 Miễn trừ trách nhiệm

- Tài liệu này chỉ đặc tả scope đã được xác nhận trong `Research-Intake-Execution`.
- Các assumption phải được đánh dấu rõ và cần xác nhận trước khi implement nếu ảnh hưởng business rule, API, database, tracking, compliance hoặc UX critical path.
- Recommendation từ Researcher không tự động trở thành requirement nếu chưa được xác nhận bởi user/stakeholder.

### 1.3 Tài liệu liên quan

| ID | Document | Type | Link / Reference | Notes |
|---|---|---|---|---|
| DOC-001 | Research Intake & Execution | Required input | [link] | [notes] |
| DOC-002 | Research Report | Researcher output | [link] | [notes] |
| DOC-003 | Prototype / Design | Design | [link] | [notes] |
| DOC-004 | API / Tech Spec | Technical | [link] | [notes] |

### 1.4 ChangeLog / History Version

| Version | Date | Author | Change Summary | Status |
|---|---|---|---|---|
| v1.0 | [YYYY-MM-DD] | [name] | Initial draft | Draft |

---

## 2. Executive Summary

> Skill: `agents/itba/skills/research-intake-execution.md`  
> Purpose: chuyển scope/why/platform/compliance đã xác nhận thành summary cho dev handoff.

### 2.1 Mô tả feature

[Feature làm gì, phục vụ actor nào, xuất hiện ở đâu trong product.]

### 2.2 Why

[Lý do business/product/user cần feature này. Phải trace được từ user request hoặc Research Intake.]

### 2.3 In Scope / Out Of Scope

**In Scope**
- [item] - [source/reference]

**Out Of Scope**
- [item] - [source/reference]

### 2.4 Platform In Scope

| Platform | In Scope | Notes |
|---|---|---|
| Web | [Yes / No] | [notes] |
| iOS | [Yes / No] | [notes] |
| Android | [Yes / No] | [notes] |
| Smart TV | [Yes / No] | [notes] |
| CMS | [Yes / No] | [notes] |
| Backend | [Yes / No] | [notes] |

### 2.5 Region & Compliance

| Region / Compliance Area | Requirement | Impact | Source |
|---|---|---|---|
| [VN / Global / Privacy / Security / Other] | [requirement] | [impact] | [source] |

---

## 3. Entry Points

> Skill: `agents/itba/skills/usecase.md`  
> Optional skill: `agents/itba/skills/bpmn.md` chỉ dùng khi user yêu cầu flow diagram hoặc feature cần 1 flow tổng.  
> Purpose: xác định mọi điểm bắt đầu vào feature trước khi viết UC chi tiết.

| Entry Point ID | Entry Point | Actor | Trigger | Destination / Outcome | Notes |
|---|---|---|---|---|---|
| EP-001 | [screen/menu/API/event] | [actor] | [trigger] | [outcome] | [notes] |

---

## 4. Use Case Summary

> Skill: `agents/itba/skills/usecase.md`  
> Purpose: tạo index tổng hợp UC để dev/QA scan coverage.

| UC ID | Use Case | Actor | Priority | Status | Related Entry Point |
|---|---|---|---|---|---|
| UC-001 | [name] | [actor] | [Must / Should / Could] | [Draft / Approved] | EP-001 |

---

## 5. Business Rule Global

> Skill: `agents/itba/skills/business-rules.md`  
> Purpose: gom rule áp dụng nhiều UC/platform vào một nơi, tránh duplicate trong từng use case.

| Rule ID | Rule | Applies To | Source | Notes |
|---|---|---|---|---|
| BR-G-001 | [global business rule] | [all / platforms / UC IDs] | [source] | [notes] |

---

## 6. Use Case List

> Skill: `agents/itba/skills/usecase.md` + `agents/itba/skills/acceptance-criteria.md`  
> Purpose: viết từng UC như một capability/mục tiêu của actor; mỗi UC chứa nhiều scenario cụ thể. Không dùng user story format trong section này.

### 6.1 UC-001: [Tên Use Case]

**Description:**  
[Mô tả capability/chức năng ở mức use case, không kể chi tiết từng tình huống]

**Diagram User-Flow:**

```text
[Optional. Use only when user requests flow diagram or this feature needs one shared flow diagram.]
[Reference FLW-ID if created by bpmn.md]
```

**Detail UC:**

| Field | Detail |
|---|---|
| Actor | [actor] |
| Triggers | [event/action/state khiến UC bắt đầu] |
| Pre-condition | [conditions] |
| Basic Path | [normal/happy path steps hoặc SC-ID tham chiếu] |
| Post-condition | [result] |
| Alternative Path | [alternate/edge steps hoặc SC-ID tham chiếu] |
| Exception Handling | [error/failure/exception steps hoặc SC-ID tham chiếu] |

**Scenario References:**

| Scenario ID | Type | Trigger | Result | Error / Copy Ref | AC Ref |
|---|---|---|---|---|---|
| SC-UC-001-01 | Happy Path | [trigger] | [result] | [ERR-ID / N/A] | [AC IDs] |
| SC-UC-001-02 | Alternate / Exception / Edge | [trigger] | [result] | [ERR-ID / N/A] | [AC IDs] |

---

### 6.2 UC-002: [Tên Use Case]

**Description:**  
[Mô tả capability/chức năng ở mức use case, không kể chi tiết từng tình huống]

**Diagram User-Flow:**

```text
[Optional. Use only when user requests flow diagram or this feature needs one shared flow diagram.]
[Reference FLW-ID if created by bpmn.md]
```

**Detail UC:**

| Field | Detail |
|---|---|
| Actor | [actor] |
| Triggers | [event/action/state khiến UC bắt đầu] |
| Pre-condition | [conditions] |
| Basic Path | [normal/happy path steps hoặc SC-ID tham chiếu] |
| Post-condition | [result] |
| Alternative Path | [alternate/edge steps hoặc SC-ID tham chiếu] |
| Exception Handling | [error/failure/exception steps hoặc SC-ID tham chiếu] |

**Scenario References:**

| Scenario ID | Type | Trigger | Result | Error / Copy Ref | AC Ref |
|---|---|---|---|---|---|
| SC-UC-002-01 | Happy Path | [trigger] | [result] | [ERR-ID / N/A] | [AC IDs] |
| SC-UC-002-02 | Alternate / Exception / Edge | [trigger] | [result] | [ERR-ID / N/A] | [AC IDs] |

---

## 7. Error Handling & User-Facing Copy

> Skill: `agents/itba/skills/screen.md` + `agents/itba/skills/api-doc.md` + `agents/itba/skills/acceptance-criteria.md`  
> Optional skill: `agents/itba/skills/bpmn.md` nếu cần đối chiếu flow tổng.  
> Purpose: chuẩn hóa lỗi, copy hiển thị, system behavior và recovery cho UI/API/UC.

| Error ID | Scenario | User-Facing Copy | System Behavior | Recovery / CTA | Applies To |
|---|---|---|---|---|---|
| ERR-001 | [scenario] | "[copy]" | [behavior] | [recovery] | [UC / UI / API] |

---

## 8. UI Specific

> Skill: `agents/itba/skills/wireframe-text.md` + `agents/itba/skills/screen.md`  
> Skill bổ trợ: `agents/itba/skills/screen.md`  
> Optional prototype skills: `agents/itba/skills/wireframe-lofi.md`, `agents/itba/skills/wireframe-hifi.md` chỉ dùng khi user yêu cầu.  
> Purpose: mô tả UI đủ để designer/dev/QA hiểu layout, element, state, validation và note implement.

### 8.1 UI Demo 1: [Tên màn hình / component]

**Wireframe Demo:**

```text
[Paste wireframe text only. Do not paste HTML, Figma link, screenshot reference, image, or color spec here.]
```

**Element Specifics:**

| # | Element | State | Rule / Notes |
|---|---|---|---|
| 1 | [element] | [default / loading / error / empty / disabled / success] | [rule/notes] |

---

### 8.2 UI Demo 2: [Tên màn hình / component]

**Wireframe Demo:**

```text
[Paste wireframe text only. Do not paste HTML, Figma link, screenshot reference, image, or color spec here.]
```

**Element Specifics:**

| # | Element | State | Rule / Notes |
|---|---|---|---|
| 1 | [element] | [default / loading / error / empty / disabled / success] | [rule/notes] |

---

## 9. Logging & Analyzing

> Skill: `agents/itba/skills/metrics.md`  
> Purpose: định nghĩa event log, thay đổi log, metric, công thức và nguồn log.

### 9.1 Log Define

| Log ID | Event Name | Trigger | Payload | Source | Owner |
|---|---|---|---|---|---|
| LOG-001 | [event_name] | [trigger] | [payload schema] | [client/server/CMS] | [owner] |

### 9.2 Log Update

| Log ID | Change Type | Previous Definition | New Definition | Reason | Impact |
|---|---|---|---|---|---|
| LOG-001 | [add/update/remove] | [previous] | [new] | [reason] | [impact] |

### 9.3 Metrics, Formula & Log Source

| Metric ID | Metric | Formula | Log Source | Notes |
|---|---|---|---|---|
| MET-001 | [metric] | [formula] | [LOG IDs] | [notes] |

---

## 10. API Reference / Schema

> Skill: `agents/itba/skills/api-doc.md`  
> Purpose: đặc tả endpoint, auth, request/response/error schema để BE/FE implement.

### Endpoint: [METHOD] [path]

**Purpose:** [endpoint dùng để làm gì]  
**Auth:** [required / optional / N/A]  
**Used By:** [UC IDs / UI IDs / CMS]

#### Request Schema

```json
{
  "field": "value"
}
```

#### Response Schema

```json
{
  "field": "value"
}
```

#### Error Schema

```json
{
  "code": "ERROR_CODE",
  "message": "User-facing or system message"
}
```

---

## 11. CMS Tools

> Skill: `agents/itba/skills/cms-tools.md` — `/cms-tools`  
> Purpose: đặc tả công cụ vận hành/admin/CMS nếu feature cần cấu hình hoặc quản trị nội dung.

| Tool / Module | User Role | Action | Data Managed | Validation Rules | Notes |
|---|---|---|---|---|---|
| [CMS module] | [role] | [create/update/delete/view] | [data] | [rules] | [notes] |

---

## 12. Database

> Skill: `agents/itba/skills/db-schema.md`  
> Purpose: đặc tả DB/table/collection, ERD, schema, constraints và relationship.

### 12.1 DB1: [Database / Table / Collection Name]

**Description:**  
[Mô tả database/table/collection và vai trò trong feature]

**Diagram ERD:**

```text
[Entity A] 1---n [Entity B]
```

**Mô tả Diagram:**

[Giải thích entity, relationship, cardinality, ownership, lifecycle.]

#### Schema

| Field | Type | Required | Description | Notes |
|---|---|---|---|---|
| [field] | [type] | [Yes / No] | [description] | [notes] |
