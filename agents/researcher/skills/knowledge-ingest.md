# Skill: Knowledge Ingest

**Command:** `/ingest <path>`  
**Agent:** Researcher  
**Output:** Knowledge ingest note

Use this optional skill after a research report is reviewed and approved for reuse.

## Rules

```text
1. Do not auto-ingest without user approval.
2. Ingest only reviewed output.
3. Keep source traceability.
4. Place shared research in knowledge/shared/pages/.
5. Place project-specific research in knowledge/projects/<project>/pages/.
```

## Output Format

```markdown
## Knowledge Ingest

**Status:** [Proposed / Approved / Done]
**Target path:** [knowledge path]
**Source report:** [Research-Report file/reference]

### Tags
[tag1, tag2, tag3]

### Notes
- [notes]
```
