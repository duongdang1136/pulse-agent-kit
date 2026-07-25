# Research Intake & Execution Template

**Dùng cho:** ITBA Agent  
**Skill:** `agents/itba/skills/research-intake-execution.md`  
**Bắt buộc trước:** `agents/itba/templates/BA-Document.md`  
**Input chính:** `Research-Report` từ Researcher Agent + user requirements + source references.

---

## Document Header

```text
Project:          [Tên project]
Feature:          [Tên feature]
Version:          v1.0
Date:             [YYYY-MM-DD]
BA:               [tên / AI]
Status:           [Draft / In Review / Approved]
Research Report:  [Link / reference]
```

---

## Research Intake

**Research status:** [Complete / Partial / Blocked]  
**Research confidence:** [High / Medium / Low]  
**Researcher output:** [Link hoặc paste Research-Report]

### Source Inventory

| Source ID | Source | Type | Used For | Confidence |
|---|---|---|---|---|
| SRC-001 | [doc/link] | [User / Project Source / Knowledge / Research Report] | [mục đích] | [High / Medium / Low] |

### Key Findings For BA

| Finding ID | Finding | Source ID | Impact on BA Document |
|---|---|---|---|
| F-001 | [finding] | SRC-001 | [section bị ảnh hưởng] |

---

## Task Brief

### User Request Summary
[Tóm tắt yêu cầu người dùng/stakeholder]

### Feature Objective
[Mục tiêu business/product của feature, chỉ dùng thông tin có evidence hoặc ghi assumption]

### Actors & Stakeholders

| Actor / Stakeholder | Role | Evidence |
|---|---|---|
| [actor] | [role] | [Source ID / ASSUMPTION] |

---

## Business Rules Extracted

| Rule ID | Business Rule | Source ID | Status |
|---|---|---|---|
| BR-001 | [rule] | SRC-001 | [Confirmed / Conflict / Assumption / Needs Clarification] |

---

## Ambiguity Log

| ID | Description | Type | Owner | Impact | Status |
|---|---|---|---|---|---|
| AMB-001 | [mô tả] | [Blocker / Risk / Assumption] | [User / PM / BA / Dev] | [section affected] | [Open / Resolved] |

---

## Scope

### In Scope
- [item] — [Source ID]

### Out Of Scope
- [item] — [Source ID / Clarification]

### Assumptions
- [assumption] — [reason / source]

---

## BA Execution Plan

| Task ID | BA Output Section | Action | Depends On | Status |
|---|---|---|---|---|
| BA-001 | Executive Summary | [write/update] | [Research Intake] | [Ready / Blocked] |
| BA-002 | Entry Points | [write/update] | [AMB-? / Source ID] | [Ready / Blocked] |
| BA-003 | Use Case Summary | [write/update] | [AMB-? / Source ID] | [Ready / Blocked] |
| BA-004 | Business Rule Global | [write/update] | [AMB-? / Source ID] | [Ready / Blocked] |
| BA-005 | Use Case List | [write/update] | [AMB-? / Source ID] | [Ready / Blocked] |
| BA-006 | Error Handling & User-Facing Copy | [write/update] | [AMB-? / Source ID] | [Ready / Blocked] |
| BA-007 | UI Specific | [write/update] | [AMB-? / Source ID] | [Ready / Blocked] |
| BA-008 | Logging & Analyzing | [write/update] | [AMB-? / Source ID] | [Ready / Blocked] |
| BA-009 | API Reference / Schema | [write/update] | [AMB-? / Source ID] | [Ready / Blocked] |
| BA-010 | CMS Tools | [write/update] | [AMB-? / Source ID] | [Ready / Blocked] |
| BA-011 | Database | [write/update] | [AMB-? / Source ID] | [Ready / Blocked] |

### BA Section Skill Routing

| BA Output Section | Skill |
|---|---|
| Document Header | `research-intake-execution.md` |
| Executive Summary | `research-intake-execution.md` |
| Entry Points | `usecase.md`; optional `bpmn.md` |
| Use Case Summary | `usecase.md` |
| Business Rule Global | `business-rules.md` |
| Use Case List | `usecase.md` + `acceptance-criteria.md` |
| Error Handling & User-Facing Copy | `screen.md` + `api-doc.md` + `acceptance-criteria.md`; optional `bpmn.md` |
| UI Specific | `wireframe-text.md` + `screen.md` |
| Logging & Analyzing | `metrics.md` |
| API Reference / Schema | `api-doc.md` |
| CMS Tools | `cms-tools.md` (`/cms-tools`) |
| Database | `db-schema.md` |

---

## Clarification Questions

Only ask questions that cannot be answered from Research Report, project sources, or user instructions.

| Question ID | Question | Why Needed | Blocks |
|---|---|---|---|
| Q-001 | [question] | [reason] | [BA section / requirement] |
