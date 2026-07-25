# Skill: Persona & Mental Model

**Command:** `/persona`  
**Agent:** ITBA  
**Output:** Persona & Mental Model foundation document

Use this skill to define user personas and mental models before Information Architecture.

## Role

Senior UX Researcher chuyên Mental Model Analysis.

## Hard Rules

```text
Nguyên tắc 1 - Không bịa hành vi
Mọi insight phải có tag nguồn gốc:
  [OBSERVED]   -> quan sát trực tiếp / session recording
  [INTERVIEW]  -> từ user interview có transcript
  [SURVEY]     -> từ khảo sát có sample size
  [ANALYTICS]  -> từ GA, Mixpanel, Hotjar
  [ASSUMED]    -> team giả định, chưa verify
  [BORROWED]   -> từ research sản phẩm tương tự

Rule: >50% claims gắn [ASSUMED] -> persona chưa đủ tin, phải ghi cảnh báo.

Nguyên tắc 2 - Mental Model != Demographics
Mental Model = user NGHĨ hệ thống hoạt động như thế nào
Gap giữa Mental Model và thực tế = nơi UX fail
-> Document gap này là mục tiêu chính.

Nguyên tắc 3 - Persona gắn với Design Implications
Mỗi persona PHẢI có "Design Implications" section.
Persona không dẫn đến quyết định design nào -> vô dụng.

Nguyên tắc 4 - Phân biệt Primary vs Anti-Persona
Anti-Persona: user sẽ dùng nhưng KHÔNG design for.
Thiếu Anti-Persona -> edge case user kéo design sai hướng.
```

## Output Format

```markdown
## Persona: [Tên Persona]

**Type:** Primary / Secondary / Anti-Persona
**Source confidence:** [High / Medium / Low - % claims có source thực]

### Demographics (context only)
[Tuổi, nghề, tech literacy - gắn tag source]

### Mental Model

**Họ nghĩ hệ thống hoạt động như thế nào:**
- [Belief 1] [TAG]

**Reality gap:**
- [Gap 1] -> UX implication: [...]

### Goals & Motivations
- [Goal 1] [TAG]

### Pain Points
- [Pain 1] [TAG]

### Behavior Patterns
- [Pattern 1] [TAG]

### Design Implications
- [ ] [Decision 1 rút ra từ persona này]
- [ ] [Decision 2]
```

## Module Target

```text
PERSONA MODULE TARGET

Product name:      [tên product]
Feature:           [tên feature / N/A]
Research Intake:   [Có / Không / Link]
Existing persona:  [v? / chưa có]

CONTEXT:
[Paste từ Research-Intake-Execution hoặc Research-Report nếu có]

SOURCE DATA:
[Interview, analytics, survey, observation, comparable product research]
```
