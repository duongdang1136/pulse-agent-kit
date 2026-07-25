# Skill: Acceptance Criteria

**Command:** `/acceptance-criteria <feature>`  
**Agent:** ITBA  
**Output:** Acceptance criteria for Use Case List

Use this skill to write testable acceptance criteria for use cases and scenarios. It supports `usecase.md`; it does not create a separate SRS section.

## Rules

```text
1. AC must be testable.
2. Use Given / When / Then.
3. Reference UC ID, Scenario ID, and business rule IDs.
4. Include edge cases only when they affect acceptance.
5. Do not duplicate the full use case flow.
```

## Output Format

```markdown
## Acceptance Criteria - [Feature]

### UC-[ID]: [Tên Use Case]

| AC ID | Scenario ID | Given | When | Then | Related Rule | Notes |
|---|---|---|---|---|---|---|
| AC-001 | SC-UC-001-01 | [context] | [action] | [expected result] | [BR ID / N/A] | [notes] |

### Edge Acceptance

| AC ID | Scenario ID | Scenario | Expected Result | Recovery / Copy |
|---|---|---|---|
| AC-E-001 | SC-UC-001-02 | [edge case] | [result] | [copy / recovery] |
```
