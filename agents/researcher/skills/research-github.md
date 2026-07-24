# Skill: Research GitHub 🐙

**Command:** `/research-github <library>`  
**Agent:** Researcher  
**Output:** GitHub Research section trong Research-Report.md

---

## Role

Research một library/tool cụ thể trên GitHub — repo stats, common issues, community patterns, breaking changes.

---

## Khi nào dùng

- User hỏi: "Research {library} trên GitHub"
- User hỏi: "Top issues của {library} là gì?"
- User hỏi: "{library} còn được maintain không?"
- Được gọi bởi RAG Router khi topic là library/framework cụ thể

---

## Flow

### Bước 1 — SEARCH repo + stats

```
web_search: "site:github.com {library} README"
web_search: "{library} github stars forks 2025 2026"
web_search: "{library} github releases changelog"
```

Extract:
- Stars, forks, last release, license
- Maintainer activity (còn active không?)

### Bước 2 — SEARCH issues + discussions

```
web_search: "site:github.com {library} issues"
web_search: "{library} github common issues 2025"
web_search: "{library} github breaking changes"
web_search: "{library} discussions performance"
```

Extract top 3–5 pain points từ community.

### Bước 3 — SEARCH migration + changelog

```
web_search: "{library} migration guide v{major}"
web_search: "{library} breaking changes {year}"
web_search: "{library} deprecated {feature}"
```

### Bước 4 — SYNTHESIZE

```markdown
## 🐙 GitHub Research — {library}

### Repo Stats
- Stars: [N]
- Forks: [N]
- Last release: [date] — [version]
- License: [MIT/Apache/etc]
- Maintainer activity: [Active / Slow / Abandoned]

### Top Issues / Pain Points
1. [Issue 1] — [link nếu có]
2. [Issue 2]
3. [Issue 3]

### Breaking Changes (gần nhất)
- v{X}: [thay đổi gì]
- v{Y}: [thay đổi gì]

### Community Sentiment
[Tóm tắt cảm nhận chung từ GitHub discussions]

### Sources
- [repo URL]
- [issues URL]
- [changelog URL]
```

---

## Output

Điền vào section **GitHub Research** của `templates/Research-Report.md`.
