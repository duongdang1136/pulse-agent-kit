# Skill: Use Case Detail

**Command:** `/usecase <feature>`  
**Agent:** ITBA  
**Output:** Use Case Summary and Use Case List

Use this skill after Research Intake is available. If a BPMN flow exists, reference its `FLW-ID`; do not duplicate the full flow diagram inside every use case.

## Concept Rules

```text
1. Use Case = một capability/chức năng/mục tiêu hệ thống từ góc nhìn actor.
2. Scenario = một tình huống cụ thể xảy ra trong Use Case.
3. Một Use Case có thể có nhiều Scenario: success, validation failure, permission denied, empty state, timeout...
4. User Story != Use Case. Không viết "As a..., I want..." trong skill này.
5. Test Scenario != User Scenario. Không biến UC thành test case; test detail nằm ở acceptance-criteria.md.
6. BPMN/flow diagram là optional và thường chỉ cần 1 flow tổng cho feature. Nếu có, UC chỉ reference FLW-ID.
```

## Output Format

```markdown
## Use Case Summary - [Feature]
**Version:** v1.0  **Date:** [YYYY-MM-DD]

| UC ID | Use Case | Primary Actor | Goal | Priority | Scenario Count | Flow Ref |
|---|---|---|---|---|---|---|
| UC-001 | [Tên Use Case] | [Actor] | [goal] | [Must / Should / Could] | [N] | [FLW-ID / N/A] |

---

## Use Case List - [Feature]

### UC-[ID]: [Tên Use Case]

**Priority:** [Must / Should / Could]
**Primary Actor:** [User / System / Admin]
**Supporting Actor(s):** [Actor / N/A]
**Goal:** [actor muốn đạt điều gì]
**Flow Reference:** [FLW-ID / N/A]
**Related Entry Point:** [EP-ID / N/A]

**Description:**
[Mô tả capability/chức năng ở mức use case, không kể chi tiết từng tình huống]

**Precondition:**
- [Điều kiện phải đúng trước khi UC bắt đầu]

**Postcondition / Success Guarantee:**
- [Trạng thái sau khi UC thành công]

**Business Rules:**
- [BR-G-001 / BR-UC-001]

### Scenarios

#### SC-[UC-ID]-01: [Happy path / tên scenario]

**Scenario Type:** [Happy Path / Alternate / Exception / Edge]
**Trigger:** [điều kiện bắt đầu scenario]

**Steps:**
1. [Actor/System] [action/response]
2. [Actor/System] [action/response]

**Result:**
[Kết quả scenario]

**Error / Copy Reference:** [ERR-ID / N/A]

**Acceptance Criteria Reference:**
- [AC IDs from acceptance-criteria.md]

#### SC-[UC-ID]-02: [Alternate/Exception scenario]

**Scenario Type:** [Alternate / Exception / Edge]
**Trigger:** [điều kiện bắt đầu scenario]

**Steps:**
1. [Actor/System] [action/response]

**Result:**
[Kết quả scenario]

**Error / Copy Reference:** [ERR-ID / N/A]

**Acceptance Criteria Reference:**
- [AC IDs from acceptance-criteria.md]

**Out of scope:**
- [Item bị defer]
```
