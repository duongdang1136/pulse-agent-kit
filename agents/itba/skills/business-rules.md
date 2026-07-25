# Skill: Business Rules

**Command:** `/business-rules <feature>`  
**Agent:** ITBA  
**Output:** Business Rule Global section

Use this skill to extract and normalize business rules that apply across multiple use cases, platforms, APIs, UI screens, CMS tools, logs, or database changes.

## Rules

```text
1. Do not invent rules.
2. Every rule must have source/reference.
3. Global rules live here; UC-specific behavior stays in usecase.md.
4. API/DB implementation detail should reference this rule by Rule ID.
```

## Output Format

```markdown
## Business Rule Global

| Rule ID | Rule | Applies To | Source | Notes |
|---|---|---|---|---|
| BR-G-001 | [global business rule] | [all / platforms / UC IDs / API IDs / DB IDs] | [source] | [notes] |
```
