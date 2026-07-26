# Skill: Research Web 🌐

**Command:** `/research-web <topic>`  
**Agent:** Researcher  
**Output:** Channel Evidence / Web Research section trong Research-Report.md

---

## Role

Research topic từ web — tổng hợp thành knowledge item chuẩn. Dùng khi cần hiểu overview, best practices, hoặc so sánh alternatives.

---

## Khi nào dùng

- Được gọi bởi RAG Router khi WIKI MISS
- User gõ: `/research-web "X"`
- Topic là concept, pattern, architecture, framework tổng quát

---

## Flow

### Bước 1 — PLAN

Trước khi search, lập kế hoạch rõ:

```
🔍 [RESEARCH PLAN]
Topic: {query}
Angles cần cover:
  1. Định nghĩa / overview
  2. Use cases thực tế
  3. Best practices / gotchas
  4. So sánh với alternatives (nếu có)
Queries sẽ dùng:
  - "{query} overview 2025"
  - "{query} best practices"
  - "{query} vs {alternative}"
```

### Bước 2 — SEARCH

Chạy **3–5 web_search** với cách diễn đạt khác nhau:

```
web_search: "{query} overview"
web_search: "{query} best practices 2025 2026"
web_search: "{query} when to use"
web_search: "{query} pros cons"
web_search: "{query} vs {alternative}"  ← nếu có alternative rõ ràng
```

### Bước 3 — EXTRACT + DEDUPLICATE

Từ kết quả search:
- Loại bỏ duplicate / thông tin trùng lặp
- Ưu tiên nguồn: `official docs > GitHub > tech blogs > StackOverflow`
- Ghi chú URL nguồn cho từng điểm

### Bước 4 — REFLECT

Tự kiểm tra trước khi synthesize:

```
□ Đã cover định nghĩa / overview?
□ Đã có ít nhất 1 ví dụ thực tế (code, case study)?
□ Đã mention use cases thực tế?
□ Đã có ít nhất 1 gotcha / anti-pattern?
□ Có alternative nào đáng so sánh không?
```

Nếu thiếu → chạy thêm search trước khi output.

### Bước 5 — SYNTHESIZE

Output theo format Research-Report.md, section Web Research:

```markdown
## 🌐 Web Research

### Overview
[Định nghĩa ngắn gọn, mục đích]

### Key Concepts
- [Concept 1]: [giải thích]
- [Concept 2]: [giải thích]

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
| | {query} | {alternative} |
|---|---|---|
| [Dimension] | | |

### Sources
- [URL 1] — [mô tả ngắn]
- [URL 2] — [mô tả ngắn]
```

---

## Output

Điền vào section **Channel Evidence / Web Research** của `templates/Research-Report.md`.
