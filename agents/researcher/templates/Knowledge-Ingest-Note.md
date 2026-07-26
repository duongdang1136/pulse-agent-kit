# Knowledge Ingest Note Template

**Used by:** Researcher Agent  
**Skill:** `agents/researcher/skills/knowledge-ingest.md`  
**When:** Optional checkpoint after reviewed research output.

---

## Ingest Header

```text
Project:           [project / shared]
Source artifact:   [Research-Report / Tech-Trend-Summary / other reviewed artifact]
Requested by:      [user / project]
Status:            [Proposed / Approved / Done / Skipped]
Date:              [YYYY-MM-DD]
```

---

## Upsert Decision

| Decision Item | Value |
|---|---|
| Upsert knowledge? | [Yes / No] |
| Approval source | [User / Project owner / N/A] |
| Target scope | [Shared / Project] |
| Target path | [`knowledge/shared/pages/...` or `knowledge/projects/<project>/pages/...`] |
| Rebuild RAG? | [Yes / No] |

---

## Knowledge Page Draft

| Field | Value |
|---|---|
| Title | [title] |
| Tags | [tags] |
| Keywords | [keywords] |
| Category | [TechStack / Domain / Architecture / Product / Process / Security / Other] |
| Source | [Research artifact / source docs / URLs] |
| Confidence | [High / Medium / Low] |

### Summary

[Short normalized summary suitable for knowledge page reuse.]

### Source Traceability

| Source ID | Source | Notes |
|---|---|---|
| SRC-001 | [path / URL / report section] | [notes] |

---

## Execution Notes

```text
Suggested command if using CLI:
pulse knowledge import <project> <source-file-or-folder> --overwrite
pulse rag build <project>
```

Do not ingest unreviewed research or unresolved assumptions.
