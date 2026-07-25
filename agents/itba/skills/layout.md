# Skill: Layout System

**Command:** `/layout`  
**Agent:** ITBA  
**Output:** Layout System foundation document  
**Dependency:** `ia.md`

Use this skill after Information Architecture is available or explicitly marked as missing.

## Role

Senior UI Architect chuyên Layout Systems.

## Output Format

```markdown
## Layout System - [Product]

**Version:** v[X]
**Date:** [YYYY-MM-DD]
**IA dependency:** [link / status]

### Grid System
- Columns: [12 / 16 / custom]
- Gutter: [Xpx]
- Margin: [Xpx]
- Max content width: [Xpx]

### Breakpoints

| Name | Min width | Columns | Gutter |
|---|---|---|---|
| Mobile | 0px | 4 | 16px |
| Tablet | 768px | 8 | 24px |
| Desktop | 1280px | 12 | 32px |

### Page Templates

| Template | Dùng cho | Layout mô tả |
|---|---|---|
| [Dashboard] | Trang data chính | [mô tả grid] |

### Component Placement Rules
- [Rule 1: Nav luôn sticky top]
- [Rule 2: Sidebar width cố định Xpx]
```

## Module Target

```text
LAYOUT MODULE TARGET

Product name:  [tên product]
Feature:       [tên feature / N/A]
Research Intake: [Có / Không / Link]
IA available:  [Có / Không / Link]
Existing layout system: [v? / chưa có]

CONTEXT:
[Paste từ Research-Intake-Execution hoặc IA output nếu có]

SOURCE DATA:
[Design file, existing UI, responsive constraints, platform requirements]
```
