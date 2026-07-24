# RFC-0003: Repository Protocol and Workflow Packages

- Status: Accepted

Pulse is not an LLM runtime. A user shares the repository, an AI reads it, then follows repository rules and workflow packages.

This RFC adds `PULSE.md`, workflow packages under `workflows/<name>/`, workflow manifest schema v1, validation tooling, and the first workflow: `feature-documentation`.

```text
Researcher
  ↓ Research-Report
ITBA
  ↓ BA-Document
```

The Research Report is evidence, not an approved requirement set.

Non-goals: provider integration, LLM API calls, runtime execution, Context Builder, and AI Handoff subsystem.
