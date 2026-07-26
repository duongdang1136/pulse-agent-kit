# COMMANDS.md - Command and CLI Reference

> `PULSE.md` is the main AI entry point.
>
> Slash commands are shorthand / legacy interaction patterns. Users do not need
> to manually paste every skill into AI.
>
> For multi-agent flows, prefer workflow packages in `workflows/`.

## Recommended Usage

```text
Read PULSE.md.
Use workflow feature-documentation.
Project: FPTPlay.
Run Researcher first, then ITBA creates Research Intake & Execution, then BA Document.
```

---

## Researcher Agent

| Command | Skill needed | Template output |
|---|---|---|
| `/research <topic>` | `agents/researcher/skills/research-plan.md` + `rag-query.md` + selected source/channel skills + `evidence-evaluation.md` + `synthesize.md` | `Research-Report.md` |
| `/research-web <topic>` | `agents/researcher/skills/research-web.md` | Web Research section |
| `/research-docs <topic>` | `agents/researcher/skills/research-docs.md` | Docs Research section |
| `/research-github <library>` | `agents/researcher/skills/research-github.md` | GitHub Research section |
| `/research-community <topic>` | `agents/researcher/skills/research-community.md` | Community Research section |
| `/research-market-map <domain>` | `agents/researcher/skills/research-market-map.md` | Market Map section |
| `/research-product-signal <domain>` | `agents/researcher/skills/research-product-signal.md` | Product Signal section |
| `/research-funding-signal <domain>` | `agents/researcher/skills/research-funding-signal.md` | Funding Signal section |
| `/compare <a> vs <b>` | `agents/researcher/skills/compare-options.md` + `evidence-evaluation.md` | `Comparison-Report.md` |
| `/benchmark <topic>` | `agents/researcher/skills/benchmark-analysis.md` + `evidence-evaluation.md` | `Benchmark-Report.md` |
| `/evaluate-evidence <topic>` | `agents/researcher/skills/evidence-evaluation.md` | Evidence Evaluation section |
| `/content-brief <topic>` | `agents/researcher/skills/content-brief.md` | `Content-Brief.md` |
| `/social-post <topic>` | `agents/researcher/skills/social-post.md` + `content-brief.md` | `Social-Post.md` |
| `/tech-macro-regime <domain>` | `tech-macro-regime.md` + macro helper skills as needed | `Tech-Macro-Regime-Report.md` |
| `/tech-signal-discovery <domain>` | `tech-signal-discovery.md` + selected source/channel skills | `Tech-Trend-Watchlist.md` |
| `/tech-trend-confirm <trend>` | `tech-trend-confirmation.md` + confirmation helper skills | `Tech-Trend-Scorecard.md` |
| `/tech-source-registry <domain>` | `agents/researcher/skills/tech-source-registry.md` + `evidence-evaluation.md` | `Tech-Source-Registry.md` |
| `/tech-trend-summary <domain>` | `agents/researcher/skills/tech-trend-summary.md` + `itba-impact-analysis.md` | `Tech-Trend-Summary.md` |
| `/rag <query>` | `agents/researcher/skills/rag-query.md` | Relevant knowledge from index |
| `/research-route <topic>` | `agents/researcher/skills/research-routing.md` | Research route plan |
| `/ingest <path>` | `agents/researcher/skills/knowledge-ingest.md` + `knowledge/README.md` | Update knowledge after review |

### Tech Trend Pipeline

```text
tech-macro-regime
  -> decide whether trend hunting is useful
  -> tech-signal-discovery
  -> call source/channel skills as needed
  -> tech-trend-confirmation
  -> output Tech-Trend-Summary, Research-Report, Social-Post, or Content-Brief
```

---

## ITBA Agent

### Research Intake & Execution

| Command | Skill needed | Template output |
|---|---|---|
| `/research-intake <feature>` | `agents/itba/skills/research-intake-execution.md` | Research Intake & Execution |
| `/execution-plan <feature>` | `agents/itba/skills/research-intake-execution.md` | Research Intake & Execution |
| `/ba <feature>` | `agents/itba/skills/research-intake-execution.md` + document skills | Research Intake & Execution -> BA Document |

### Foundation - Optional

| Command | Skill needed | Output section |
|---|---|---|
| `/persona <product>` | `agents/itba/skills/persona.md` | User Persona & Mental Model |
| `/ia <product>` | `agents/itba/skills/ia.md` | Information Architecture |
| `/layout <product>` | `agents/itba/skills/layout.md` | Layout System |
| `/token <product>` | `agents/itba/skills/token.md` | Token Registry |

Foundation uses `agents/itba/templates/Foundation.md` and is created only when the user asks.

### Design & Validate

| Command | Skill needed | Output section |
|---|---|---|
| `/wireframe-text <feature>` | `agents/itba/skills/wireframe-text.md` | Required text-only wireframe for BA Document |
| `/wireframe-lofi <feature>` | `agents/itba/skills/wireframe-lofi.md` | Optional lo-fi HTML wireframe without color |
| `/wireframe-hifi <feature>` | `agents/itba/skills/wireframe-hifi.md` | Optional hi-fi HTML wireframe with color |
| `/review-stakeholder` | `agents/itba/skills/stakeholder-review.md` | Stakeholder Review |
| `/review-design` | `agents/itba/skills/design-critique.md` | Design Critique |

### Document

| Command | Skill needed | Output section |
|---|---|---|
| `/business-rules <feature>` | `agents/itba/skills/business-rules.md` | Business Rule Global |
| `/acceptance-criteria <feature>` | `agents/itba/skills/acceptance-criteria.md` | Acceptance Criteria |
| `/api-doc <feature>` | `agents/itba/skills/api-doc.md` | API Contract Doc |
| `/db-schema <feature>` | `agents/itba/skills/db-schema.md` | DB Schema Doc |
| `/metrics <feature>` | `agents/itba/skills/metrics.md` | Metrics Doc |
| `/cms-tools <feature>` | `agents/itba/skills/cms-tools.md` | CMS/admin tool specification |

### Audit & UI-to-Spec

| Command | Skill needed | Output |
|---|---|---|
| `/audit <screen>` | `agents/itba/skills/heuristic-audit.md` | Heuristic Audit |
| `/audit-component <component>` | `agents/itba/skills/component-audit.md` | Component Audit |
| `/audit-layout <page>` | `agents/itba/skills/layout-audit.md` | Layout Audit |
| `/screen <screenshot>` | `agents/itba/skills/screen.md` | Screen Specification |
| `/bpmn <flow>` | `agents/itba/skills/bpmn.md` | BPMN Flow |
| `/usecase <feature>` | `agents/itba/skills/usecase.md` | Use Case List |

---

## Knowledge Commands

| Command | Description |
|---|---|
| `/ingest <path>` | Ingest files into knowledge base |
| `/rag <query>` | Query knowledge base |
| `/rag-project <project> <query>` | Query project-specific knowledge |

---

## Local Docs CLI

Generated docs nên được lưu trong output workspace local nằm ngoài
`pulse-agent-kit/`, ví dụ `../docs`.

```bash
pulse docs init ../docs --project fptplay
pulse docs path ../docs --project fptplay --epic notification --feature notification-center --type ba-document
pulse docs add ../docs ./ba-document.md --project fptplay --epic notification --feature notification-center --type ba-document --status reviewed
pulse docs list ../docs --project fptplay
pulse docs index ../docs --project fptplay
pulse rag query fptplay "quiet hours" --include-docs --docs-workspace ../docs
```

Docs được sắp xếp theo:

```text
docs/<project>/epics/<epic>/features/<feature>/<type>.md
docs/<project>/epics/<epic>/features/<feature>/sub-features/<sub-feature>/<type>.md
```

---

## Tool Commands

| Command | Description |
|---|---|
| `/tool-add <name>` | Add a new tool to registry by copying `tools/_template/tool.md` |
| `/tool-list` | List tools in `tools/` |
