# Skill: Content Brief

**Command:** `/content-brief <topic>`  
**Agent:** Researcher  
**Output:** `Content-Brief`

Use this skill to turn a research artifact into a content direction before writing a social post, thread, tips list, workflow breakdown, or carousel outline.

## Required Inputs

```text
1. Topic
2. Source artifact:
   - Research-Report, or
   - Comparison-Report, or
   - Benchmark-Report
3. Target audience
4. Target platform/format, if known
```

If no research artifact exists, run research/compare/benchmark first or mark the brief as evidence-incomplete.

## Goal

- Select the strongest angle.
- Define target audience.
- Identify source-backed claims.
- Separate facts, opinions, anecdotes, and assumptions.
- Choose content format.
- Define tone, hook direction, CTA, caveats, and risk.
- Produce `templates/Content-Brief.md`.

## Rules

```text
1. Do not invent claims.
2. Do not turn community anecdote into fact.
3. Label opinion/takeaway clearly.
4. Keep source traceability for material claims.
5. If evidence is weak, say the post should be framed as opinion or learning note.
```

## Output Contract

Use `agents/researcher/templates/Content-Brief.md`.
