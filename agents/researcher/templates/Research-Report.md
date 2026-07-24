# Research Report Template 📋

**Dùng cho:** `/research <topic>` — output của Researcher Agent  
**Điền bởi:** Kết hợp research-web + research-github + research-community skills

---

## 🏷️ Report Header

```
Topic:          [tên topic / thư viện / concept]
Research date:  [YYYY-MM-DD]
Requested by:   [tên / project]
Scope:          [Web / GitHub / Community / All]
RAG status:     [WIKI SUFFICIENT / WIKI PARTIAL / WIKI MISS → NEW]
```

---

## 📌 Executive Summary

> 2–4 câu tóm tắt những gì quan trọng nhất. Người đọc chỉ cần section này để ra quyết định nhanh.

**Verdict:** [Nên dùng / Không nên / Phụ thuộc vào...]  
**Confidence:** [High / Medium / Low]

---

## 🌐 Web Research

> Skill: `skills/research-web.md`

### Overview
[Định nghĩa ngắn gọn, mục đích, vị trí trong ecosystem]

### Key Concepts
- **[Concept 1]:** [giải thích]
- **[Concept 2]:** [giải thích]

### Use Cases
- [Use case 1]
- [Use case 2]

### Best Practices
- [Practice 1]
- [Practice 2]

### Gotchas / Anti-patterns
- ⚠️ [Gotcha 1]
- ⚠️ [Gotcha 2]

### Comparison (nếu có)
| | {topic} | {alternative} |
|---|---|---|
| Performance | | |
| DX | | |
| Ecosystem | | |

---

## 🐙 GitHub Research

> Skill: `skills/research-github.md`  
> *(Bỏ qua section này nếu topic không phải library/tool)*

### Repo Stats
- Stars: [N]
- Forks: [N]
- Last release: [date] — [version]
- License: [MIT/Apache/etc]
- Maintainer activity: [Active / Slow / Abandoned]

### Top Issues / Pain Points
1. [Issue 1]
2. [Issue 2]
3. [Issue 3]

### Breaking Changes (gần nhất)
- v{X}: [thay đổi gì]

---

## 💬 Community Research

> Skill: `skills/research-community.md`  
> *(Bỏ qua section này nếu không cần community insight)*

### Overall Sentiment
[Positive / Mixed / Negative]

### What people love 👍
- [Point 1]

### Pain points 👎
- [Pain 1]

### Hot debates 🔥
- [Debate]

### Emerging trends
- [Trend 1]

---

## 🎯 Recommendations

> Tổng hợp cuối — action items cụ thể

**Nên làm:**
- [ ] [Action 1]
- [ ] [Action 2]

**Không nên làm:**
- ❌ [Anti-action 1]

**Cần research thêm:**
- [ ] [Gap 1] — lý do chưa đủ data

---

## 📎 Sources

| # | URL | Loại | Relevance |
|---|---|---|---|
| 1 | [URL] | Official docs | High |
| 2 | [URL] | GitHub | Medium |
| 3 | [URL] | Reddit | Low |

---

## 💾 Knowledge Ingest

> Sau khi review xong, ingest vào knowledge base:

```
/ingest knowledge/shared/pages/<topic-slug>.md
```

Tags: [tag1, tag2, tag3]  
Category: [TechStack / Domain / Architecture / Other]
