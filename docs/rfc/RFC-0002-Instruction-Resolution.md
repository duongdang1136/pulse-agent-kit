# RFC-0002: Instruction Resolution

- Status: Accepted
- Scope: Selecting files an AI should read for one task

## Decision

Pulse does not execute an agent and does not call an LLM. Pulse resolves a task
into an ordered instruction plan.

```text
Task
  ↓
Agent manifest resolution rules
  ↓
Primary agent instructions
  ↓
Relevant skills only
  ↓
Selected output template
```

The resolver is deterministic and inspectable. It does not attempt semantic
reasoning and does not require a model, provider, API key, or authentication.

## Resolution precedence

1. Explicit skill or template requested by the caller.
2. Matching rules, ordered by descending priority.
3. Fallback skills and default template.
4. The agent's output template.

Selected skills are de-duplicated and limited by `max_skills`.

## Manifest example

```yaml
resolution:
  max_skills: 3
  fallback_skills:
    - audit
  default_template: BA-Document
  rules:
    - id: ui-review
      priority: 100
      when_any:
        - ui
        - mockup
        - giao diện
      skills:
        - ui-to-spec
        - audit
      template: Audit-Report
```

## Output contract

The resolver produces:

- selected skill identifiers;
- selected template;
- matching rule identifiers;
- an ordered list of package files;
- a reason for every selected file.

Project workspace and knowledge resolution remain outside this PR.
