# Skill: Wireframe Text

**Command:** `/wireframe-text <feature>`  
**Agent:** ITBA  
**Output:** Text-only wireframe for BA Document

Use this skill for a brand-new UI that does not exist yet. It fills the required `Wireframe Demo` field in the BA Document. Output must be plain text only. Do not use HTML, CSS, color, image, Figma, or screenshot references in this skill output.

## Rules

```text
1. Text-only wireframe is required for each UI Demo in BA Document.
2. Use ASCII layout blocks and short labels.
3. Do not include colors, CSS, tokens, images, or HTML.
4. Keep the wireframe implementation-neutral.
```

## Output Format

```markdown
## Wireframe Text: [Feature Name]
**Date:** [YYYY-MM-DD]
**UC covered:** [UC-01, UC-02]

### Screen: [Tên màn hình]

```text
+------------------------------------------------+
| Header                                         |
+------------------------------------------------+
| Section / Panel                                |
| - Field / Component                            |
| - CTA                                          |
+------------------------------------------------+
| Footer / System message                        |
+------------------------------------------------+
```

### Interaction Notes
- [Trigger] -> [Action]: [Result]

### Edge States
- Empty state: [mô tả]
- Loading state: [mô tả]
- Error state: [mô tả]
```
