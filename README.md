# pulse-agent-kit 🧠

Bộ kit agent AI platform-agnostic — tích hợp sẵn 2 agent chuyên biệt và hệ thống quản lý skill, tool, và knowledge (RAG).

Pull về. Paste skill vào LLM. Chạy.

---

## Agents có sẵn

| Agent | Vai trò | Command |
|---|---|---|
| `researcher` | Research web, GitHub, community — output Research Report | `/research` |
| `itba` | IT Business Analyst — BA, wireframe, audit, docs — output BA Document | `/ba`, `/audit`, `/bpmn`, `/usecase`, `/screen` |

---

## Cấu trúc thư mục

```
pulse-agent-kit/
├── agents/
│   ├── researcher/
│   │   ├── agent.md             ← Role + cách dùng
│   │   ├── skills/              ← Các skill atomic (research-web, github, community, rag-router)
│   │   └── templates/           ← Research-Report.md — output blueprint
│   │
│   └── itba/
│       ├── agent.md             ← Role + cách dùng
│       ├── skills/              ← Các skill theo phase (phase-0 đến phase-3, audit, ui-to-spec)
│       └── templates/           ← BA-Document.md, Audit-Report.md — output blueprints
│
├── tools/
│   ├── README.md                ← Hướng dẫn thêm tool mới
│   └── _template/
│       └── tool.md              ← Template cho mỗi tool entry
│
├── knowledge/
│   ├── README.md                ← Hướng dẫn ingest + quản lý knowledge
│   ├── shared/                  ← Wiki chung — researcher agent dùng
│   │   ├── .rag/index.json      ← Search index (auto-generated)
│   │   └── pages/               ← Các file .md knowledge
│   │
│   └── projects/                ← Per-project knowledge — itba agent dùng
│       └── <project-name>/
│           ├── .rag/index.json
│           └── pages/
│
└── COMMANDS.md                  ← Command reference đầy đủ
```

---

## Quickstart — 3 bước

**Bước 1: Clone**
```bash
git clone https://github.com/duongdang1136/pulse-agent-kit
cd pulse-agent-kit
```

**Bước 2: Chọn agent + command**
```
/research "streaming platform architecture"
/ba "user login với SSO"
/audit "checkout screen"
```

**Bước 3: Paste skill vào LLM**
- Mở file skill tương ứng trong `agents/<agent>/skills/`
- Paste vào ChatGPT / Claude / Cursor / bất kỳ LLM nào
- Paste thêm context của bạn → Chạy

---

## Thêm project knowledge (ITBA)

```bash
# Tạo project mới
mkdir -p knowledge/projects/fptplay/pages

# Drop file .md vào pages/
cp your-docs/*.md knowledge/projects/fptplay/pages/

# Chạy ingest (cập nhật index.json)
# Xem knowledge/README.md để biết cách ingest
```

---

## Mở rộng — Thêm agent mới

```bash
mkdir -p agents/fe-manager/{skills,templates}
# Xem agents/researcher/agent.md để biết format
```

---

## Related

- [COMMANDS.md](./COMMANDS.md) — Tất cả commands
- [knowledge/README.md](./knowledge/README.md) — RAG + ingest guide
- [tools/README.md](./tools/README.md) — Tool registry guide
