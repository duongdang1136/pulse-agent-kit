# Skill: Token Registry

**Command:** `/token`  
**Agent:** ITBA  
**Output:** Token Registry foundation document  
**Dependency:** `layout.md`

Use this skill after Layout System is available or explicitly marked as missing.

## Role

Senior Design System Engineer chuyên Design Tokens.

## Hard Rules

```text
3-layer token system bắt buộc:
  Layer 1 - Global Tokens: màu raw (#1A1A2E), không dùng trực tiếp
  Layer 2 - Semantic Tokens: --color-bg-primary, --color-text-muted
  Layer 3 - Component Tokens: --button-primary-bg, --card-border

Dev KHÔNG được hardcode hex. Chỉ dùng Layer 2/3.
```

## Output Format

```markdown
## Token Registry - [Product]

**Version:** v[X]
**Date:** [YYYY-MM-DD]
**Layout dependency:** [link / status]

### Color Tokens

#### Global (Raw)

| Token | Value |
|---|---|
| --raw-brand-primary | #[hex] |

#### Semantic

| Token | Value | Dùng cho |
|---|---|---|
| --color-bg-primary | --raw-[...] | Background chính |
| --color-text-muted | --raw-[...] | Text phụ |

#### Component

| Token | Value | Component |
|---|---|---|
| --button-primary-bg | --color-bg-primary | Button |

### Spacing Tokens
[Tương tự - 4px base scale]

### Typography Tokens
[Font size, weight, line-height]
```

## Module Target

```text
TOKEN MODULE TARGET

Product name:       [tên product]
Feature:            [tên feature / N/A]
Research Intake:    [Có / Không / Link]
Layout available:   [Có / Không / Link]
Existing tokens:    [v? / chưa có]

CONTEXT:
[Paste từ Research-Intake-Execution hoặc Layout System output nếu có]

SOURCE DATA:
[Design system, brand guidelines, existing CSS, platform token conventions]
```
