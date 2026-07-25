# Skill: Wireframe Hi-fi

**Command:** `/wireframe-hifi <feature>`  
**Agent:** ITBA  
**Output:** Optional high-fidelity HTML wireframe

Use this skill only when the user explicitly asks for a hi-fi wireframe. Output is HTML with visual styling, colors, and tokens.

## Rules

```text
1. Optional skill; do not run by default for BA Document.
2. Output HTML.
3. Color is allowed and expected.
4. Include visual hierarchy, component states, spacing, typography, and interaction notes.
5. Keep implementation as prototype/handoff HTML, not production code.
```

## Output Format

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>[Feature] Hi-fi Wireframe</title>
    <style>
      :root {
        --color-bg-primary: #[hex];
        --color-text-primary: #[hex];
        --spacing-4: 16px;
      }
      body {
        margin: 0;
        font-family: Arial, sans-serif;
        background: var(--color-bg-primary);
        color: var(--color-text-primary);
      }
    </style>
  </head>
  <body>
    <main>[Hi-fi prototype content]</main>
  </body>
</html>
```
