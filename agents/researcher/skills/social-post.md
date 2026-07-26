# Skill: Social Post

**Command:** `/social-post <topic>`  
**Agent:** Researcher  
**Output:** `Social-Post`

Use this skill to turn `Content-Brief` into publish-ready social content.

## Required Inputs

```text
1. Content-Brief
2. Source artifact:
   - Research-Report, or
   - Comparison-Report, or
   - Benchmark-Report
3. Target platform/format
4. Tone/voice constraints, if any
```

If `Content-Brief` is missing, create it first.

## Supported Formats

```text
- LinkedIn post
- X/Twitter thread
- Facebook post
- Short tips list
- Workflow breakdown
- Carousel outline
```

## Rules

```text
1. Do not add unsupported claims.
2. Do not use clickbait that changes meaning.
3. Preserve caveats that materially affect interpretation.
4. If a post is opinion, label it as opinion/takeaway.
5. Keep claims traceable to source IDs.
```

## Output Contract

Use `agents/researcher/templates/Social-Post.md`.
