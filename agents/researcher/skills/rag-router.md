# Skill: RAG Router 🗂️

**Command:** `/rag <query>`  
**Agent:** Researcher  
**Output:** Relevant knowledge từ index, hoặc trigger research pipeline nếu MISS

---

## Role

Điều phối query flow — check knowledge base trước khi research. Tránh research lại những gì đã biết.

---

## Khi nào dùng

Trước **mọi** research query. RAG Router là entry point bắt buộc:
- "Mày biết gì về X?"
- "Research X cho tôi"
- "Cần context về X để..."

---

## Flow

```
Query nhận được
    ↓
[Step 1] Pre-processing — chuẩn hóa query
    ↓
[Step 2] Wiki Lookup — đọc .rag/index.json
    ↓ HIT (confidence ≥ 0.75, ≥ 2 items)        ↓ MISS
[Step 3a] Load content                    [Step 3b] Trigger research pipeline
    ↓                                              ↓
Dynamic eval (4 câu)                      research-web.md
    ↓                                     + research-github.md (nếu là library)
SUFFICIENT → trả lời                      + research-community.md (nếu cần)
PARTIAL → augment
INSUFFICIENT → research mới
```

---

## Step 1 — Query Pre-processing

Chuẩn hóa query trước khi lookup:

```
Rewrite: chuyển query lóng/viết tắt thành biến thể chuẩn
  VD: "cái auth kia xài jwt ko" → "hệ thống authentication có dùng JWT không?"

Domain detect: xác định topic thuộc domain nào
  → TechStack (React, NestJS, Docker, OAuth...)
  → Domain (E-commerce, EdTech, workflow...)
  → Unknown → tiếp tục bình thường
```

---

## Step 2 — Wiki Lookup

```
file_read: knowledge/shared/.rag/index.json
  (hoặc knowledge/projects/<project>/.rag/index.json nếu có project context)
```

Tìm items khớp với query (keyword search trong `title`, `tags`, `keywords`).

**HIT:** confidence ≥ 0.75 VÀ có ít nhất 2 items liên quan  
**MISS:** không khớp hoặc confidence thấp

---

## Step 3a — Dynamic Eval (khi HIT)

Load content rồi tự đặt 4 câu hỏi:

```
□ Content có trả lời trực tiếp query này không?
□ Có ví dụ / code / số liệu cụ thể phù hợp không?
□ Query hỏi về khía cạnh X — Wiki item có cover X không?
□ Có missing_aspects rõ ràng không?
```

**3-4/4 YES** → `WIKI SUFFICIENT` → prefix `📚 [WIKI]`, trả lời + source path  
**1-2/4 YES** → `WIKI PARTIAL` → research thêm, prefix `📚 [WIKI] + 🔍 [RESEARCH AUGMENTED]`  
**0/4** → `WIKI INSUFFICIENT` → bỏ wiki, research mới, prefix `🆕 [NEW]`

---

## Step 3b — Research Pipeline (khi MISS)

Chọn pipeline dựa trên query type:

| Query type | Pipeline |
|---|---|
| "X là gì?", "giải thích X" | → `skill: research-web` |
| "library X có issues gì?", "X còn maintain không?" | → `skill: research-github` |
| "community nói gì về X?", "X có trend không?" | → `skill: research-community` |
| Query phức tạp, nhiều chiều | → Kết hợp cả 3 |

Prefix output: `🆕 [NEW] ← Kiến thức này chưa có trong Wiki`

Sau khi research xong → auto-ingest vào knowledge base.

---

## Freshness Check

Nếu query có "mới nhất / latest / 2026":
- Check `last_updated` trong index item
- TTL: security 30d / framework 90d / architecture 180d
- Quá TTL → badge `⏳ Dữ liệu có thể chưa mới nhất` + trigger research mới
