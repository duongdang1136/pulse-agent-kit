# Knowledge and RAG

Pulse separates source documents, normalized knowledge, and RAG indexes.

```text
projects/
  fptplay/
    source-docs/          original project documents

knowledge/
  shared/
    pages/                reusable cross-project knowledge
    .rag/                 shared knowledge index
  projects/
    fptplay/
      pages/              normalized project knowledge
      .rag/               project knowledge index
```

## Definitions

**Project sources** are original project files in `projects/<project>/source-docs/`.

Examples:

- product briefs
- stakeholder notes
- exported docs
- screenshots or screen descriptions
- API notes
- existing specs

Project sources are the highest-priority project evidence after current user instructions.

**Knowledge** is reviewed and normalized Markdown in `knowledge/shared/pages/` or `knowledge/projects/<project>/pages/`.

- Shared knowledge is reusable across projects.
- Project knowledge belongs to one project. It may still be reusable inside that project or product line.
- Knowledge pages should keep original source traceability.
- Do not put unreviewed assumptions into knowledge.

Promote knowledge to `knowledge/shared/pages/` only when it is generic enough for cross-project reuse.
If the knowledge is reusable but still depends on one product's behavior, vocabulary, source documents, or stakeholder decisions, keep it under `knowledge/projects/<project>/pages/`.

**RAG** is a generated retrieval index under `.rag/`.

- RAG helps find relevant knowledge pages.
- RAG does not replace source traceability.
- RAG hits must point back to knowledge pages and original sources.

## Source Priority

Use this order when sources conflict:

1. Current user instruction.
2. `projects/<project>/source-docs/`.
3. `knowledge/projects/<project>/pages/`.
4. Prior workflow outputs.
5. `knowledge/shared/pages/`.
6. External research.

## Knowledge Page Format

Each knowledge page should use frontmatter:

```markdown
---
title: "Topic or document title"
tags: [tag1, tag2]
keywords: [keyword1, keyword2]
category: TechStack | Domain | Architecture | Product | Process | Security | Other
last_updated: YYYY-MM-DD
source: [path or URL]
confidence: high | medium | low
---

# Topic

Normalized knowledge content.
```

## Upsert Flow

Use this flow when adding or refreshing project knowledge:

```text
1. Store original files in projects/<project>/source-docs/.
2. Review the source or workflow output.
3. Normalize approved content into knowledge/projects/<project>/pages/.
4. Preserve links back to original sources.
5. Rebuild the project RAG index.
6. Query RAG to verify retrieval works.
```

CLI example:

```bash
pulse knowledge import fptplay projects/fptplay/source-docs --category Product --overwrite
pulse rag build fptplay
pulse rag query fptplay "notification scheduling" --include-shared
```

Use `--no-copy` only when the original files are already in `projects/<project>/source-docs/` and should not be copied again.

`--category` defaults to `Product`. Use a more specific category when the imported knowledge matches it:

```text
TechStack     framework, library, platform, tooling
Domain        reusable business/domain concept
Architecture  system design, integration, API architecture
Product       product-specific behavior, requirements, specs
Process       workflow, operating procedure, delivery process
Security      security, privacy, compliance, risk control
Other         reviewed knowledge that does not fit the categories above
```

## Shared Knowledge Flow

Use shared knowledge only for reusable material:

```text
knowledge/shared/pages/
```

Good shared knowledge:

- technology explanation
- architecture pattern
- reusable domain concept
- general compliance note
- cross-project research summary

Do not place project-specific confidential behavior into shared knowledge.

Shared knowledge should be queried with project knowledge when broader reusable context is useful:

```bash
pulse rag query fptplay "notification scheduling" --include-shared
```

Project hits outrank shared hits by source priority when facts conflict. Shared hits are context, not authority over project sources.

## RAG Index Files

RAG files live under:

```text
knowledge/projects/<project>/.rag/
knowledge/shared/.rag/
```

The index is generated. Do not treat it as authored documentation.

If knowledge pages change, rebuild the relevant RAG index.
