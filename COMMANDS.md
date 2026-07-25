# COMMANDS.md — Command and CLI Reference

> `PULSE.md` là entry point chính cho AI.
>
> Các slash command trong tài liệu này là shorthand hoặc legacy interaction
> patterns. Người dùng không bắt buộc phải copy từng skill vào AI.
>
> Với flow multi-agent, hãy ưu tiên workflow package trong `workflows/`.

## Recommended usage

```text
Đọc PULSE.md.
Sử dụng workflow feature-documentation.
Project: FPTPlay.
Thực hiện Researcher trước, sau đó ITBA tạo Research Intake & Execution, cuối cùng mới tạo BA Document.
```

---

## 🔍 Researcher Agent

| Command | Skill cần paste | Template output |
|---|---|---|
| `/research <topic>` | `agents/researcher/skills/research-web.md` + `research-github.md` + `research-community.md` | `Research-Report.md` |
| `/research-web <topic>` | `agents/researcher/skills/research-web.md` | Section Web Research |
| `/research-github <library>` | `agents/researcher/skills/research-github.md` | Section GitHub Research |
| `/research-community <topic>` | `agents/researcher/skills/research-community.md` | Section Community Research |
| `/rag <query>` | `agents/researcher/skills/rag-router.md` | Relevant knowledge từ index |
| `/ingest <path>` | `knowledge/README.md` | Cập nhật `.rag/index.json` |

### Ví dụ

```
/research "Next.js App Router vs Pages Router"
→ paste: agents/researcher/skills/research-web.md
→ output: Research-Report.md

/research-github "prisma"
→ paste: agents/researcher/skills/research-github.md
→ output: GitHub analysis section

/ingest knowledge/projects/fptplay/pages/
→ cập nhật knowledge/projects/fptplay/.rag/index.json
```

---

## 🧩 ITBA Agent

### Research Intake & Execution

| Command | Skill cần paste | Template output |
|---|---|---|
| `/research-intake <feature>` | `agents/itba/skills/research-intake-execution.md` | Research Intake & Execution |
| `/execution-plan <feature>` | `agents/itba/skills/research-intake-execution.md` | Research Intake & Execution |
| `/ba <feature>` | `agents/itba/skills/research-intake-execution.md` + document skills | Research Intake & Execution → BA Document |

### Foundation — Optional

| Command | Skill cần paste | Output section |
|---|---|---|
| `/persona <product>` | `agents/itba/skills/persona.md` | User Persona & Mental Model |
| `/ia <product>` | `agents/itba/skills/ia.md` | Information Architecture |
| `/layout <product>` | `agents/itba/skills/layout.md` | Layout System |
| `/token <product>` | `agents/itba/skills/token.md` | Token Registry |

Foundation dùng template riêng `agents/itba/templates/Foundation.md` và chỉ tạo khi người dùng yêu cầu.

### Phase 2 — Design & Validate

| Command | Skill cần paste | Output section |
|---|---|---|
| `/wireframe-text <feature>` | `agents/itba/skills/wireframe-text.md` | Required text-only wireframe for BA Document |
| `/wireframe-lofi <feature>` | `agents/itba/skills/wireframe-lofi.md` | Optional lo-fi HTML wireframe without color |
| `/wireframe-hifi <feature>` | `agents/itba/skills/wireframe-hifi.md` | Optional hi-fi HTML wireframe with color |
| `/review-stakeholder` | `agents/itba/skills/stakeholder-review.md` | Stakeholder Review |
| `/review-design` | `agents/itba/skills/design-critique.md` | Design Critique |

### Phase 3 — Document

| Command | Skill cần paste | Output section |
|---|---|---|
| `/business-rules <feature>` | `agents/itba/skills/business-rules.md` | Business Rule Global |
| `/acceptance-criteria <feature>` | `agents/itba/skills/acceptance-criteria.md` | Acceptance Criteria |
| `/api-doc <feature>` | `agents/itba/skills/api-doc.md` | API Contract Doc |
| `/db-schema <feature>` | `agents/itba/skills/db-schema.md` | DB Schema Doc |
| `/metrics <feature>` | `agents/itba/skills/metrics.md` | Metrics Doc |
| `/cms-tools <feature>` | `agents/itba/skills/cms-tools.md` | CMS/admin tool specification |

### Audit & UI-to-Spec

| Command | Skill cần paste | Output |
|---|---|---|
| `/audit <screen>` | `agents/itba/skills/heuristic-audit.md` | Heuristic Audit |
| `/audit-component <component>` | `agents/itba/skills/component-audit.md` | Component Audit |
| `/audit-layout <page>` | `agents/itba/skills/layout-audit.md` | Layout Audit |
| `/screen <screenshot>` | `agents/itba/skills/screen.md` | Screen Specification |
| `/bpmn <flow>` | `agents/itba/skills/bpmn.md` | BPMN Flow |
| `/usecase <feature>` | `agents/itba/skills/usecase.md` | Use Case List |

### Ví dụ end-to-end

```
# BA full flow — từ request đến docs
/ba "màn hình checkout FPTPlay"
→ Researcher output: Research-Report
→ paste: agents/itba/skills/research-intake-execution.md
→ AI output: Research-Intake-Execution
→ Review/clarify → tiếp BA Document

/wireframe-text "checkout flow"
→ paste: agents/itba/skills/wireframe-text.md
→ AI output: Text-only wireframe for BA Document

/acceptance-criteria "checkout"
→ paste: agents/itba/skills/acceptance-criteria.md
→ AI output: Acceptance Criteria đầy đủ

# Chỉ cần một phần
/screen [paste screenshot description]
→ AI output: Screen Description structured

/bpmn "user login flow"
→ AI output: BPMN diagram + flow doc
```

---

## 📦 Knowledge Commands

| Command | Mô tả |
|---|---|
| `/ingest <path>` | Ingest files vào knowledge base |
| `/rag <query>` | Query knowledge base |
| `/rag-project <project> <query>` | Query project-specific knowledge |

---

## 🔧 Tool Commands

| Command | Mô tả |
|---|---|
| `/tool-add <name>` | Thêm tool mới vào registry (copy `tools/_template/tool.md`) |
| `/tool-list` | Xem tất cả tools trong `tools/` |
