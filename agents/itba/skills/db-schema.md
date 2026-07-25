# Skill: DB Schema

**Command:** `/db-schema <feature>`  
**Agent:** ITBA  
**Output:** Database section

Use this skill when the feature requires database, table, collection, ERD, indexes, constraints, or relationship changes.

## Output Format

```markdown
## Database

### DB1: [Database / Table / Collection Name]

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

#### Indexes
- [index] - [reason]

#### Constraints
- [constraint] - [reason]
```
