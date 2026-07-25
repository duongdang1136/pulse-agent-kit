# Skill: Information Architecture

**Command:** `/ia`  
**Agent:** ITBA  
**Output:** Information Architecture foundation document  
**Dependency:** `persona.md`

Use this skill after Persona & Mental Model is available or explicitly marked as missing.

## Role

Senior Information Architect chuyên Web App, Dashboard.

## Hard Rules

```text
Nguyên tắc 1 - Naming từ user, không từ team
Labels phải validate bằng:
  [USER-TESTED]   -> Card sorting / Tree testing
  [USER-LANGUAGE] -> Đúng từ user hay dùng trong interview
  [TEAM-DECIDED]  -> Team tự đặt, chưa validate

Warning: >30% labels gắn [TEAM-DECIDED] -> cần Card Sorting session.

Nguyên tắc 2 - 4 IA artifacts riêng biệt
  CONTENT INVENTORY  -> Danh sách mọi content đang tồn tại
  CONTENT HIERARCHY  -> Quan hệ cha-con giữa content/section
  NAVIGATION SYSTEM  -> Cách user di chuyển giữa các node
  NAMING CONVENTION  -> Quy tắc đặt tên nhất quán

Nguyên tắc 3 - Phân biệt Navigation vs Content
Navigation = cấu trúc menu/sidebar
Content = cái gì hiển thị trên từng page
Đừng nhầm lẫn 2 cái này.
```

## Output Format

```markdown
## Information Architecture - [Product]

**Version:** v[X]
**Date:** [YYYY-MM-DD]
**Persona dependency:** [link / status]

### Content Inventory

| ID | Content | Type | Location hiện tại | Status |
|---|---|---|---|---|

### Content Hierarchy
[Tree hoặc indented list]

### Navigation System

**Primary Nav:** [list items] [TAG]
**Secondary Nav:** [list items] [TAG]
**Breadcrumb pattern:** [mô tả]

### Naming Convention

| Pattern | Rule | Ví dụ |
|---|---|---|
```

## Module Target

```text
IA MODULE TARGET

Product name:       [tên product]
Feature:            [tên feature / N/A]
Research Intake:    [Có / Không / Link]
Persona available:  [Có / Không / Link]
Existing IA:        [v? / chưa có]

CONTEXT:
[Paste từ Research-Intake-Execution hoặc Persona output nếu có]

SOURCE DATA:
[Sitemap, screen list, navigation, menu, content model, user language evidence]
```
