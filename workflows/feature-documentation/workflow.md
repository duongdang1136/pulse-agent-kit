---
name: feature-documentation
version: 1.0.0
---

# Feature Documentation Workflow

## Stage 1 — Research

Agent: `researcher`

Read the Researcher agent, stage skills, project source documents, normalized knowledge, and Research Report template.

Produce a `Research-Report` containing source inventory, evidence-backed findings, terminology, dependencies, conflicts, gaps, open questions, labeled recommendations, and source traceability.

Do not produce the BA document during this stage.

## Handoff — Researcher to ITBA

Pass the Research Report, user requirements, project and feature identifiers, source references, assumptions, conflicts, and unresolved questions. Recommendations are not approved requirements.

## Clarification checkpoint

Ask the user when a missing item requires a business decision. Group related questions and avoid asking anything answerable from project sources.

## Stage 2 — Analysis

Agent: `itba`

Read the ITBA agent, stage skills, Research Report, user clarifications, relevant project sources, and BA Document template.

Produce a `BA-Document` covering scope, objectives, actors, stakeholders, functional requirements, business rules, data/events, integrations, acceptance criteria, assumptions, and open questions.

## Iteration

When requirements change, identify affected sections, update evidence and assumptions, ask for clarification when needed, and revise the BA Document. Restart research only for a new domain, source gap, or dependency.
