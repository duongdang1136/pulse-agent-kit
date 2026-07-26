# Knowledge Manager — RAG System 🧠

Hệ thống quản lý knowledge base dạng file Markdown + JSON index. Platform-agnostic, không cần DB, không cần backend.

---

## Cấu trúc

```
knowledge/
├── shared/                     ← Wiki chung — Researcher Agent dùng
│   ├── .rag/
│   │   └── index.json          ← Search index (auto-generated)
│   └── pages/                  ← Files .md knowledge
│       ├── <topic-slug>.md
│       └── ...
│
└── projects/                   ← Per-project — ITBA Agent dùng
    └── <project-name>/         ← VD: fptplay/
        ├── .rag/
        │   └── index.json
        └── pages/
            └── <doc-name>.md
```

---

## Format file knowledge (pages/*.md)

Mỗi file knowledge có header metadata:

```markdown
---
title: "Tên topic / document"
tags: [tag1, tag2, tag3]
keywords: [keyword1, keyword2]  ← dùng để search
category: TechStack | Domain | Architecture | Product | Process
last_updated: YYYY-MM-DD
source: [URL hoặc "internal"]
confidence: high | medium | low
---

# [Tên topic]

[Nội dung knowledge...]
```

---

## Format index.json

```json
{
  "version": "1.0",
  "updated_at": "YYYY-MM-DD",
  "items": [
    {
      "id": "unique-slug",
      "title": "Tên topic",
      "path": "pages/topic-slug.md",
      "tags": ["tag1", "tag2"],
      "keywords": ["keyword1", "keyword2"],
      "category": "TechStack",
      "last_updated": "YYYY-MM-DD",
      "ttl_days": 90,
      "summary": "1-2 câu tóm tắt nội dung — dùng để quick match"
    }
  ]
}
```

**TTL theo category:**
| Category | TTL |
|---|---|
| Security | 30 ngày |
| TechStack / Framework | 90 ngày |
| Architecture | 180 ngày |
| Domain / Product | 365 ngày |
| Process | Không hết hạn |

---

## Ingest — Thêm knowledge mới

### Manual (recommended cho LLM-driven workflow)

**Bước 1:** Tạo file `.md` trong `pages/`:

```bash
# Shared knowledge
touch knowledge/shared/pages/<topic-slug>.md

# Project-specific
touch knowledge/projects/<project>/pages/<doc-slug>.md
```

**Bước 2:** Điền header metadata + nội dung theo format trên.

**Bước 3:** Cập nhật `index.json` — thêm item mới vào array `items`:

```json
{
  "id": "<unique-slug>",
  "title": "<title từ frontmatter>",
  "path": "pages/<file>.md",
  "tags": [...],
  "keywords": [...],
  "category": "...",
  "last_updated": "YYYY-MM-DD",
  "ttl_days": 90,
  "summary": "..."
}
```

### Batch ingest (khi có nhiều files)

```bash
# Copy files vào pages/
cp ./your-docs/*.md knowledge/projects/<project>/pages/

# Chạy ingest helper (xem scripts/ingest.sh)
bash scripts/ingest.sh knowledge/projects/<project>/
```

Script tự scan `pages/*.md`, đọc frontmatter, và rebuild `index.json`.

---

## Query — Tìm knowledge

**Cách LLM query:**

1. Đọc `knowledge/shared/.rag/index.json` (hoặc project index)
2. Search keyword trong `title`, `tags`, `keywords`, `summary`
3. Nếu HIT (confidence ≥ 0.75): đọc file `.md` tương ứng
4. Nếu MISS: trigger research pipeline

*(Xem chi tiết: `agents/researcher/skills/rag-query.md` và `agents/researcher/skills/research-routing.md`)*

---

## Thêm project mới

```bash
# Tạo project structure
mkdir -p knowledge/projects/<project-name>/{.rag,pages}

# Tạo index.json trống
echo '{
  "version": "1.0",
  "updated_at": "'$(date +%Y-%m-%d)'",
  "items": []
}' > knowledge/projects/<project-name>/.rag/index.json
```

---

## Ví dụ — Project FPTPlay

```bash
# Tạo project
mkdir -p knowledge/projects/fptplay/{.rag,pages}

# Thêm docs vào pages/
cp ./fptplay-docs/auth-spec.md knowledge/projects/fptplay/pages/
cp ./fptplay-docs/api-overview.md knowledge/projects/fptplay/pages/

# Cập nhật index.json
# (manual hoặc dùng scripts/ingest.sh)
```

ITBA Agent sau đó có thể query: `knowledge/projects/fptplay/.rag/index.json`

---

## Scripts

Xem `scripts/` folder:
- `scripts/ingest.sh` — rebuild index.json từ pages/*.md
- `scripts/new-project.sh` — init project structure
