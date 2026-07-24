# Pulse Repository Operating Protocol

Pulse is an AI-readable repository, not an LLM runtime. It requires no provider, API key, or authentication.

## Mandatory read order

1. Read this file first.
2. Identify the requested project and workflow.
3. Read the workflow manifest and `workflow.md`.
4. Read only the agent, skills, and template required by the current stage.
5. Read relevant project sources and normalized knowledge.
6. Execute stages in order and preserve handoff outputs.
7. Ask the user when a business decision cannot be derived from evidence.
8. Produce the declared output template.

## Source priority

1. Current user instructions.
2. Project source documents.
3. Project knowledge pages.
4. Earlier workflow outputs.
5. Shared knowledge.
6. External research when permitted or requested.

Never silently resolve conflicting sources.

## Non-invention rule

Do not invent requirements, business rules, acceptance criteria, system behavior, stakeholder decisions, metrics, API contracts, or data definitions. Label proposals as proposals and assumptions as assumptions.

## Workflow execution

For each stage:

1. Read the assigned agent.
2. Read the stage skills.
3. Read the output template.
4. Read stage inputs and prior handoffs.
5. Perform the work.
6. Produce the declared output.
7. Pass it to the next stage.

## Project usage

Projects live under `projects/<project>/`; normalized knowledge lives under `knowledge/projects/<project>/`. RAG is a navigation aid and does not replace source traceability.

## Default feature-documentation flow

```text
Researcher
  ↓ Research-Report
ITBA
  ↓ BA-Document
```

Researcher gathers and separates evidence, conflicts, gaps, assumptions, and recommendations. ITBA consumes that report plus user requirements and project sources, asks for unresolved business decisions, then produces the BA document.
