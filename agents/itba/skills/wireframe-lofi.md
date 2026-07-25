# Skill: Wireframe Lo-fi HTML

**Command:** `/wireframe-lofi <feature>`  
**Agent:** ITBA  
**Output:** Optional low-fidelity HTML wireframe

Use this skill only when the user explicitly asks for a lo-fi wireframe. Output is HTML with structure and layout only. Do not use color.

## Rules

```text
1. Optional skill; do not run by default for BA Document.
2. Output HTML.
3. No color values, no background colors, no brand colors.
4. Use grayscale-neutral structure only if styling is necessary.
5. Prioritize layout, hierarchy, and interaction placeholders.
```

## Output Format

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>[Feature] Lo-fi Wireframe</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 0; }
      .page { display: grid; gap: 16px; padding: 24px; }
      .section { border: 1px solid #999; padding: 16px; }
      .row { display: flex; gap: 12px; }
    </style>
  </head>
  <body>
    <main class="page">
      <section class="section">[Layout block]</section>
    </main>
  </body>
</html>
```
