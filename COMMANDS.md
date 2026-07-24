# COMMANDS.md — Command Reference

Mỗi command kích hoạt một skill + template cụ thể. Paste command vào LLM cùng với skill file tương ứng.

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

### Phase 0 — Research & Plan

| Command | Skill cần paste | Template output |
|---|---|---|
| `/ba <feature>` | `agents/itba/skills/phase-0-research-plan.md` | BA Document — full flow Phase 0→3 |
| `/ba-plan <feature>` | `agents/itba/skills/phase-0-research-plan.md` | Research Report + Execution Plan |
| `/ba-cr <change>` | `agents/itba/skills/phase-0-research-plan.md` + Change Request section | Change Impact Report |

### Phase 1 — Foundation

| Command | Skill cần paste | Output section |
|---|---|---|
| `/persona <product>` | `agents/itba/skills/phase-1-foundation.md` → section Persona | User Persona & Mental Model |
| `/ia <product>` | `agents/itba/skills/phase-1-foundation.md` → section IA | Information Architecture |
| `/layout <product>` | `agents/itba/skills/phase-1-foundation.md` → section Layout | Layout System |
| `/token <product>` | `agents/itba/skills/phase-1-foundation.md` → section Token | Token Registry |

### Phase 2 — Design & Validate

| Command | Skill cần paste | Output section |
|---|---|---|
| `/wireframe <feature>` | `agents/itba/skills/phase-2-design.md` → Module Lo-fi | Wireframe Lo-fi |
| `/wireframe-hifi <feature>` | `agents/itba/skills/phase-2-design.md` → Module Hi-fi | Hi-fidelity Prototype |
| `/review-stakeholder` | `agents/itba/skills/phase-2-design.md` → Review Module A | Stakeholder Review |
| `/review-design` | `agents/itba/skills/phase-2-design.md` → Review Module B | Design Critique |

### Phase 3 — Document

| Command | Skill cần paste | Output section |
|---|---|---|
| `/srs <feature>` | `agents/itba/skills/phase-3-document.md` → SRS Doc | SRS Document |
| `/api-doc <feature>` | `agents/itba/skills/phase-3-document.md` → API Contract | API Contract Doc |
| `/db-schema <feature>` | `agents/itba/skills/phase-3-document.md` → DB Schema | DB Schema Doc |
| `/logic <feature>` | `agents/itba/skills/phase-3-document.md` → Backend Logic | Backend Logic Doc |
| `/metrics <feature>` | `agents/itba/skills/phase-3-document.md` → Metrics | Metrics Doc |

### Audit & UI-to-Spec

| Command | Skill cần paste | Output |
|---|---|---|
| `/audit <screen>` | `agents/itba/skills/audit.md` → Heuristic Review | Audit Report |
| `/audit-component <component>` | `agents/itba/skills/audit.md` → Component Audit | Component Audit |
| `/audit-layout <page>` | `agents/itba/skills/audit.md` → Page Layout Audit | Layout Audit |
| `/screen <screenshot>` | `agents/itba/skills/ui-to-spec.md` → Screen Description | Screen Description |
| `/bpmn <flow>` | `agents/itba/skills/ui-to-spec.md` → BPMN section | BPMN Flow |
| `/usecase <feature>` | `agents/itba/skills/ui-to-spec.md` → Use Case Detail | Use Case List |

### Ví dụ end-to-end

```
# BA full flow — từ request đến docs
/ba "màn hình checkout FPTPlay"
→ paste: agents/itba/skills/phase-0-research-plan.md
→ AI output: Research Report + Execution Plan
→ Review → approve → tiếp Phase 1

/wireframe "checkout flow"
→ paste: agents/itba/skills/phase-2-design.md
→ chọn Module B (Lo-fi)
→ AI output: Wireframe description

/srs "checkout"
→ paste: agents/itba/skills/phase-3-document.md
→ AI output: SRS document đầy đủ

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
