# Skill: Benchmark Analysis

**Command:** `/benchmark <topic>`  
**Agent:** Researcher  
**Output:** `Benchmark-Report`

Use this skill when the user needs measured comparison or analysis using performance, cost, quality, usage, market, operational, or product metrics.

## Goal

- Define benchmark objective.
- Define metrics and units.
- Identify data sources and method.
- Report results with caveats.
- Separate measured results from inference.
- Produce `templates/Benchmark-Report.md`.

## Rules

```text
1. Do not invent benchmark numbers.
2. Every metric must define unit, source, and calculation method.
3. State whether data is measured, sourced, estimated, or assumed.
4. Explain limitations and sample bias.
5. If benchmark cannot be run or verified, output a benchmark plan instead of fake results.
```

## Output Contract

Use `agents/researcher/templates/Benchmark-Report.md`.
