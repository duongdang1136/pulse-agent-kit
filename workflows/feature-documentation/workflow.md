---
name: feature-documentation
version: 1.0.0
---

# Feature Documentation Workflow

## Stage 1 - Research

Agent: `researcher`

Read the Researcher agent, stage skills, project source documents, normalized knowledge, and Research Report template.

Produce a `Research-Report` containing source inventory, evidence-backed findings, terminology, dependencies, conflicts, gaps, open questions, labeled recommendations, and source traceability.

Do not produce the BA document during this stage.

## Optional Checkpoint - Knowledge Upsert

Agent: `researcher`

Run this checkpoint only after the Research Report is reviewed and the user approves reusable knowledge capture.

Use `knowledge-ingest` to propose or perform an upsert into:

```text
knowledge/shared/pages/
knowledge/projects/<project>/pages/
```

Then rebuild the relevant RAG index if CLI tooling is being used:

```text
pulse rag build <project>
```

Do not upsert unreviewed research, unresolved assumptions, or project-specific information into shared knowledge. This checkpoint is optional and must not block ITBA handoff unless the user explicitly asks to refresh knowledge first.

## Handoff - Researcher to ITBA

Pass the Research Report, optional Knowledge Ingest Note, user requirements, project and feature identifiers, source references, assumptions, conflicts, and unresolved questions. Recommendations are not approved requirements.

## Stage 2 - Research Intake & Execution

Agent: `itba`

Read the ITBA agent, `research-intake-execution` skill, Research Report, user requirements, source references, and Research Intake & Execution template.

Produce a `Research-Intake-Execution` document. This document is mandatory before the BA Document. It converts the Research Report into task brief, evidence summary, business rules, ambiguity log, scope, execution plan, and clarification questions.

Do not recreate the Research Report during this stage. Ask the user when a missing item requires a business decision.

## Clarification Checkpoint

Ask the user when a missing item requires a business decision. Group related questions and avoid asking anything answerable from project sources.

## Stage 3 - Analysis

Agent: `itba`

Read the ITBA agent, stage skills, Research Report, Research Intake & Execution document, user clarifications, relevant project sources, and BA Document template.

Produce a `BA-Document` covering scope, objectives, actors, stakeholders, functional requirements, business rules, data/events, integrations, acceptance criteria, assumptions, and open questions.

## Iteration

When requirements change, identify affected sections, update evidence and assumptions, ask for clarification when needed, and revise the BA Document. Restart research only for a new domain, source gap, or dependency.
