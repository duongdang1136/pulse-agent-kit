# Foundation Template

**Dùng cho:** ITBA Agent — optional foundation document  
**Điền bởi:** Các skill độc lập `/persona`, `/ia`, `/layout`, `/token`  
**Khi dùng:** Chỉ tạo document này khi người dùng yêu cầu Foundation rõ ràng.

---

## Document Header

```text
Product:        [Tên product]
Project:        [Tên project]
Version:        v1.0
Date:           [YYYY-MM-DD]
BA:             [tên / AI]
Status:         [Draft / In Review / Approved]
Related feature:[Tên feature / N/A]
```

---

## Persona & Mental Model

**Skill:** `agents/itba/skills/persona.md`  
**Command:** `/persona`  
**Status:** [Not Started / Draft / In Review / Approved]  
**Version:** v[X]  
**Source confidence:** [High / Medium / Low]  
**Last updated:** [YYYY-MM-DD]

### Summary
[Tóm tắt persona chính, mental model quan trọng, reality gap ảnh hưởng đến product/feature]

### Linked Output
[Link hoặc paste nội dung Persona & Mental Model document]

### Design Implications
- [Decision/Implication 1]
- [Decision/Implication 2]

---

## Information Architecture

**Skill:** `agents/itba/skills/ia.md`  
**Command:** `/ia`  
**Status:** [Not Started / Draft / In Review / Approved]  
**Version:** v[X]  
**Dependency:** Persona & Mental Model  
**Last updated:** [YYYY-MM-DD]

### Summary
[Tóm tắt content inventory, hierarchy, navigation, naming rules liên quan product/feature]

### Linked Output
[Link hoặc paste nội dung Information Architecture document]

### IA Decisions
- [Decision 1]
- [Decision 2]

---

## Layout System

**Skill:** `agents/itba/skills/layout.md`  
**Command:** `/layout`  
**Status:** [Not Started / Draft / In Review / Approved]  
**Version:** v[X]  
**Dependency:** Information Architecture  
**Last updated:** [YYYY-MM-DD]

### Summary
[Tóm tắt grid, breakpoint, page template, component placement rules]

### Linked Output
[Link hoặc paste nội dung Layout System document]

### Layout Rules Applied
- [Rule 1]
- [Rule 2]

---

## Token Registry

**Skill:** `agents/itba/skills/token.md`  
**Command:** `/token`  
**Status:** [Not Started / Draft / In Review / Approved]  
**Version:** v[X]  
**Dependency:** Layout System  
**Last updated:** [YYYY-MM-DD]

### Summary
[Tóm tắt global tokens, semantic tokens, component tokens dùng cho product/feature]

### Linked Output
[Link hoặc paste nội dung Token Registry document]

### Token Rules Applied
- [Rule 1]
- [Rule 2]
