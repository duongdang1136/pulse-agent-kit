# Pulse Repository Operating Protocol

Pulse is an AI-readable repository, not an LLM runtime. It requires no provider, API key, or authentication.

## Mandatory Read Order

1. Read this file first.
2. Identify the requested project and workflow.
3. Read the workflow manifest and `workflow.md`.
4. Read only the agent, skills, and template required by the current stage.
5. Read relevant project sources and normalized knowledge.
6. Execute stages in order and preserve handoff outputs.
7. Ask the user when a business decision cannot be derived from evidence.
8. Produce the declared output template.

## Source Priority

1. Current user instructions.
2. Project source documents.
3. Project knowledge pages.
4. Earlier workflow outputs.
5. Shared knowledge.
6. External research when permitted or requested.

Never silently resolve conflicting sources.

## Non-Invention Rule

Do not invent requirements, business rules, acceptance criteria, system behavior, stakeholder decisions, metrics, API contracts, or data definitions. Label proposals as proposals and assumptions as assumptions.

## Workflow Execution

For each stage:

1. Read the assigned agent.
2. Read the stage skills.
3. Read the output template.
4. Read stage inputs and prior handoffs.
5. Perform the work.
6. Produce the declared output.
7. Pass it to the next stage.

## Project Usage

Pulse separates original project sources, normalized knowledge, and RAG indexes:

```text
projects/
  <project>/
    source-docs/          original documents supplied by the user/project

knowledge/
  shared/                 reusable cross-project knowledge
  projects/
    <project>/            normalized project knowledge pages and RAG index
```

Source priority:

1. `projects/<project>/source-docs/` is the source of truth for project-specific facts.
2. `knowledge/projects/<project>/pages/` is normalized project knowledge derived from reviewed sources or outputs.
3. `knowledge/shared/pages/` is reusable cross-project knowledge.
4. `.rag/` indexes are navigation aids over knowledge pages.

RAG helps find relevant knowledge quickly, but it never replaces source traceability. When RAG returns a hit, cite the underlying knowledge page and its original source, not the index itself.

## Project Output Docs

When Pulse is used from a local clone or writable workspace, generated workflow
outputs may be stored outside `pulse-agent-kit/` in a project docs workspace:

```text
<project-folder>/
  pulse-agent-kit/
  docs/
    <project>/
      epics/<epic>/features/<feature>/
```

Use this only when the user has a writable local workspace. When Pulse is used
through a GitHub URL, generated reports remain chat/session output unless the
user manually stores them.

## Knowledge Upsert

Knowledge upsert is optional and approval-gated.

Use it when reviewed research or approved source material should become reusable knowledge:

```text
projects/<project>/source-docs/       original evidence
  -> review / normalize
knowledge/projects/<project>/pages/   reusable project knowledge
  -> rebuild RAG
knowledge/projects/<project>/.rag/    generated retrieval index
```

Do not upsert unreviewed research, unresolved assumptions, or project-specific material into shared knowledge.

## Default Feature Documentation Flow

```text
Researcher
  -> Research-Report
Optional Knowledge Upsert
  -> Knowledge-Ingest-Note
ITBA
  -> Research-Intake-Execution
  -> BA-Document
```

Researcher gathers and separates evidence, conflicts, gaps, assumptions, and recommendations. The optional knowledge upsert checkpoint captures reviewed reusable knowledge. ITBA consumes the Research Report, optional Knowledge Ingest Note, user requirements, and project sources, asks for unresolved business decisions, then produces the BA document.
