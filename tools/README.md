# Tool Registry 🔧

Quản lý GitHub opensource tools bổ trợ cho agents. Mỗi tool = 1 folder với `tool.md`.

---

## Cấu trúc

```
tools/
├── README.md              ← file này
├── _template/
│   └── tool.md            ← template để thêm tool mới
└── <tool-name>/
    └── tool.md
```

---

## Thêm tool mới

```bash
mkdir tools/<tool-name>
cp tools/_template/tool.md tools/<tool-name>/tool.md
# Điền thông tin vào tool.md
```

---

## Tools hiện có

*(Chưa có tool nào — thêm tool đầu tiên bằng cách copy _template)*

---

## Agents có thể dùng tool nào?

Mỗi `tool.md` có field `agents` liệt kê agent nào có thể dùng tool đó.
