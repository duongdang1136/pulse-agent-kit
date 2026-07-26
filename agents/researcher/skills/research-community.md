# Skill: Research Community 💬

**Command:** `/research-community <topic>`  
**Agent:** Researcher  
**Output:** Channel Evidence / Community Research section trong Research-Report.md

---

## Role

Research ý kiến cộng đồng — pain points, opinions, emerging trends từ Reddit, X (Twitter), Hacker News.

---

## Khi nào dùng

- User hỏi: "Community nói gì về X?"
- User hỏi: "Dev đang dùng X như thế nào?"
- User hỏi: "Xu hướng X hiện nay ra sao?"
- Supplement sau research-web hoặc research-github

---

## Flow

### Bước 1 — SEARCH Reddit

```
web_search: "site:reddit.com/r/programming {topic}"
web_search: "site:reddit.com/r/webdev {topic}"
web_search: "site:reddit.com/r/node {topic}"       ← nếu liên quan Node/JS
web_search: "site:reddit.com {topic} experience 2025"
```

### Bước 2 — SEARCH X / Twitter

```
web_search: "{topic} twitter discussion 2025 2026"
web_search: "{topic} developer opinion twitter"
```

### Bước 3 — SEARCH Hacker News

```
web_search: "site:news.ycombinator.com {topic}"
web_search: "{topic} hacker news discussion"
```

### Bước 4 — CLASSIFY sentiment

Phân loại ý kiến:
- 👍 Positive: lý do họ thích
- 👎 Negative: pain points, complaints
- 🤔 Mixed: trade-offs, "depends on..."
- 🔥 Hot debate: điểm gây tranh cãi

### Bước 5 — SYNTHESIZE

```markdown
## 💬 Community Research — {topic}

### Overall Sentiment
[Positive / Mixed / Negative — 1 câu tóm tắt]

### What people love 👍
- [Point 1]
- [Point 2]

### Pain points 👎
- [Pain 1]
- [Pain 2]

### Hot debates 🔥
- [Debate 1]: [2 phía quan điểm]

### Emerging trends
- [Trend 1]

### Sources
- [Reddit thread URL]
- [HN discussion URL]
- [Twitter/X link]
```

---

## Output

Điền vào section **Channel Evidence / Community Research** của `templates/Research-Report.md`.
