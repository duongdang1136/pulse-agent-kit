# RFC-0001: Agent Package Specification

- Status: Accepted
- Schema: 2

## Decision

A Pulse agent is an instruction package, not a Python agent class and not an
LLM runtime object. It may be read by a human, an AI assistant, or repository
tooling.

Pulse remains completely independent of the AI system used to execute the
instructions.

## Non-goals

The manifest does not configure providers, model names, API keys,
authentication, temperature, inference settings, tool calling, or an agent
runtime.

## Package layout

```text
agents/<name>/
├── manifest.yaml
├── agent.md
├── skills/
└── templates/
```

## Reading order

An AI should read:

1. repository-level instructions;
2. the selected agent manifest;
3. `agent.md`;
4. task-relevant skills;
5. the project workspace;
6. relevant knowledge;
7. the selected output template.

The user's AI environment is responsible for file access and execution.
Pulse defines and validates the package only.
