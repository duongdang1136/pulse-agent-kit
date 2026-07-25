# Skill: API Contract

**Command:** `/api-doc <feature>`  
**Agent:** ITBA  
**Output:** API Reference / Schema

Use this skill when the feature requires endpoint, request, response, auth, or error schema definition.

## Output Format

```markdown
## API Reference / Schema - [Feature Name]

### Endpoint: [METHOD] [path]

**Purpose:** [endpoint dùng để làm gì]
**Auth required:** [Yes / No]

#### Request
**Headers:**
```text
Authorization: Bearer {token}
Content-Type: application/json
```

**Path params:**
| Param | Type | Required | Description |
|---|---|---|---|

**Query params:**
| Param | Type | Required | Default | Description |
|---|---|---|---|---|

**Body:**
```json
{}
```

#### Response - 200 OK
```json
{}
```

#### Error Responses
| Code | When | Response body |
|---|---|---|
```
