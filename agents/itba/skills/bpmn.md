# Skill: BPMN Flow

**Command:** `/bpmn <flow>`  
**Agent:** ITBA  
**Output:** Text-based BPMN flow and step table

Use this optional skill when the feature needs one high-level flow diagram. A feature usually needs only one flow diagram even when it has multiple use cases. Do not create one BPMN per UC unless the user explicitly asks.

## Output Format

```markdown
## BPMN Flow: [Tên Flow]
**Flow ID:** FLW-[N]  **Date:** [YYYY-MM-DD]
**UC covered:** [UC-01, UC-02]

### Trigger
[Điều kiện bắt đầu flow]

### End State
[Trạng thái kết thúc thành công]

### Happy Path
```text
[User] -> [Action 1]
       -> [System response]
       -> END STATE
```

### Step-by-step Table

| Step | Actor | Action | System Response | Notes |
|---|---|---|---|---|

### Alternative Paths

| Path | Trigger | Behavior | Recovery |
|---|---|---|---|
| Loading | [condition] | [behavior] | [recovery] |
| Error | [condition] | [message/behavior] | [recovery] |
| Empty | [condition] | [behavior] | [recovery] |
| Cancel | [condition] | [behavior] | [recovery] |
```
