---
id: caveman
name: Caveman
version: external
status: optional
type: prompt-skill
homepage: https://github.com/JuliusBrussee/caveman
license: MIT
capabilities: [token-efficient-writing, concise-agent-communication]
agents: [researcher, itba]
---

# Caveman

External Claude Code skill for reducing token usage through aggressively concise communication.

Use it only as an optional **output compression layer** after reasoning and evidence gathering. It is not a research source, RAG engine, or correctness tool.

## Guardrails

- Never remove citations, assumptions, risks, acceptance criteria, or unresolved questions.
- Avoid it for legal, security, incident, compliance, and formal BA deliverables where nuance matters.
- Follow upstream installation instructions and pin a reviewed commit/tag before production use.
- Never auto-execute unreviewed remote content.
