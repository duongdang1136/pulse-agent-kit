# Skill: Screen Specification

**Command:** `/screen <description|screenshot>`  
**Agent:** ITBA  
**Output:** UI Specific / screen element specification

Use this skill when UI already exists and must be described, extended, or converted into structured BA documentation. Input can be screenshot, Figma frame, existing UI, or raw UI description. For a brand-new UI with no existing screen, use `wireframe-text.md` first.

## Goal

Identify screens, components, fields, states, validation rules, interactions, and edge cases so dev and QA can implement/test the UI.

## Output Format

```markdown
## Screen: [Tên màn hình]
**Screen ID:** SCR-[N]

### Layout Overview
[Mô tả tổng thể layout]

### Components & Fields

**[Field/Component Name]**
- UI Control: [Textbox / Dropdown / Radio / Checkbox / Button / Upload Zone...]
- Data Type: [String / Integer / Boolean / Date / Image] ([ReadOnly / Editable / Hidden / Auto-fill])
- Rules & Validation:
  - Default: [giá trị/trạng thái mặc định]
  - Constraint: [Required / Optional]
  - Limits: [Min/Max chars, file size...]
  - Allowed: [whitelist format/ký tự hợp lệ]
  - Blocked: [blacklist/regex]
- Interaction:
  - On-action: [click field này gọi component nào lên?]
  - Outcome: [data sync đi đâu sau khi update?]
- Edge Cases:
  - Error: [text error message chính xác trên UI]
  - Fallback: [UI tự xử lý không? VD: auto uppercase]
```
