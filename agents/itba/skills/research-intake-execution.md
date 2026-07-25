# Skill: Research Intake & Execution

**Command:** `/research-intake <feature>` hoặc `/execution-plan <feature>`  
**Agent:** ITBA  
**Output:** `Research-Intake-Execution`  
**Required before:** `BA-Document`

Use this skill after the Researcher Agent has produced `Research-Report`. ITBA does not recreate the Research Report. ITBA consumes it, extracts BA-relevant decisions and gaps, and prepares the execution plan for the BA document.

## Role

Senior IT Business Analyst / BA Manager.

## Goal

Convert Researcher output and user requirements into a practical BA execution document:

- confirm task brief and business context;
- extract BA-relevant findings from `Research-Report`;
- catalogue business rules and source references;
- identify blockers, risks, assumptions, and clarification needs;
- define IN/OUT scope;
- plan which BA document sections must be produced next.

## Required Inputs

```text
1. Project identifier
2. Feature identifier
3. User requirements
4. Research-Report from Researcher Agent
5. Project source references used by Researcher
6. User clarifications, if any
```

If `Research-Report` is missing, stop and ask for Researcher stage first.

## Source Priority

```text
1. Current user instructions
2. Research-Report from Researcher Agent
3. Project source documents referenced by Researcher
4. Project knowledge pages referenced by Researcher
5. User clarifications
```

Do not silently resolve conflicts. Mark them in the Ambiguity Log.

## Analysis Rules

### Rule 1 - Research Intake, Not Research Recreation

Do not perform independent research unless the workflow explicitly restarts Researcher stage.

Allowed:
- summarize Research-Report findings;
- map findings to BA output sections;
- identify missing business decisions;
- request clarification.

Not allowed:
- invent new findings;
- approve Researcher recommendations as requirements;
- create new business rules without evidence.

### Rule 2 - Evidence Mapping

Every business rule, scope item, assumption, or acceptance-criteria input must trace back to:

```text
[USER]
[RESEARCH-REPORT]
[PROJECT-SOURCE]
[PROJECT-KNOWLEDGE]
[CLARIFICATION]
[ASSUMPTION]
```

### Rule 3 - Execution Readiness

Before BA Document starts, this skill must answer:

```text
- What is confirmed?
- What is out of scope?
- What is assumed?
- What is blocked?
- Which BA sections can be produced now?
- Which BA sections require clarification?
```

## Output Contract

Produce output using `agents/itba/templates/Research-Intake-Execution.md`.

## Module Target

```text
RESEARCH INTAKE & EXECUTION TARGET

Project:          [project]
Feature:          [feature]
Requested by:     [PM / stakeholder / user]
Date:             [YYYY-MM-DD]

USER REQUIREMENTS:
[paste request]

RESEARCH REPORT:
[paste or link Research-Report]

SOURCE REFERENCES:
[project source docs / knowledge pages referenced]

USER CLARIFICATIONS:
[paste if any]
```
