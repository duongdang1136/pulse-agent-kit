# Skill: CMS Tools Specification

**Command:** `/cms-tools <feature>`  
**Agent:** ITBA  
**Output:** CMS Tools section for BA Document

Use this skill when a feature requires back-office, admin, moderation, configuration, campaign, content, or operational tools.

## Goal

Define CMS/Admin requirements so internal users and dev teams understand:

- who can use the tool;
- what data can be created, viewed, updated, deleted, approved, published, scheduled, or audited;
- validation rules;
- permission rules;
- operational states;
- dependencies with APIs, database, logging, and user-facing app behavior.

## Required Inputs

```text
1. Research-Intake-Execution
2. Use Case List
3. Business Rule Global
4. API Reference / Schema, if available
5. Database section, if available
6. Existing CMS/admin source docs, if any
```

## Output Format

```markdown
## CMS Tools

### CMS Module: [Tên module]

**Purpose:** [module dùng để làm gì]  
**Users/Roles:** [Admin / Operator / Editor / Approver / Viewer]  
**Related UC:** [UC IDs]  
**Related API:** [endpoint IDs]  
**Related DB:** [DB/table IDs]

#### Actions

| Action | Role Allowed | Behavior | Validation | Audit Log |
|---|---|---|---|---|
| Create | [role] | [behavior] | [rules] | [LOG ID] |
| Update | [role] | [behavior] | [rules] | [LOG ID] |
| Delete | [role] | [behavior] | [rules] | [LOG ID] |
| Publish | [role] | [behavior] | [rules] | [LOG ID] |

#### Field Specification

| Field | Type | Required | Editable | Validation | Notes |
|---|---|---|---|---|---|
| [field] | [type] | [Yes / No] | [Yes / No] | [rules] | [notes] |

#### States

| State | Meaning | Allowed Actions | Next State |
|---|---|---|---|
| Draft | [meaning] | [actions] | [state] |
| Published | [meaning] | [actions] | [state] |

#### Permission Matrix

| Role | View | Create | Update | Delete | Approve | Publish |
|---|---|---|---|---|---|---|
| Admin | Yes | Yes | Yes | Yes | Yes | Yes |
| Operator | Yes | [Yes/No] | [Yes/No] | [Yes/No] | [Yes/No] | [Yes/No] |
```
