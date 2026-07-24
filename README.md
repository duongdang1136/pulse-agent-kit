# Pulse Agent Kit

Pulse là một repository protocol độc lập với AI provider, dùng để tổ chức:

- agent instructions;
- reusable skills;
- output templates;
- multi-agent workflows;
- project source documents;
- normalized knowledge và RAG indexes.

Pulse không phải LLM runtime.

Pulse không gọi OpenAI, Anthropic, Gemini hoặc model provider nào. Không cần API key. Người dùng đưa repository cho một AI có khả năng đọc file hoặc GitHub, sau đó AI tuân thủ `PULSE.md` để thực hiện công việc.

## Use case chính

```text
User cung cấp repository Pulse
        ↓
AI đọc PULSE.md
        ↓
AI xác định project và workflow
        ↓
Researcher phân tích nguồn tài liệu
        ↓
Research Report
        ↓
ITBA nhận report và yêu cầu người dùng
        ↓
Trao đổi các business decision còn thiếu
        ↓
BA Document
```

Ví dụ hiện tại:

```text
Project: FPTPlay
Workflow: feature-documentation
Agents: Researcher → ITBA
```

## Quick start

### 1. Clone repository

```bash
git clone https://github.com/duongdang1136/pulse-agent-kit.git
cd pulse-agent-kit
```

Hoặc cung cấp trực tiếp URL repository cho AI:

```text
https://github.com/duongdang1136/pulse-agent-kit
```

### 2. Yêu cầu AI đọc protocol

```text
Hãy đọc repository pulse-agent-kit này.

Đọc PULSE.md trước và tuân thủ repository operating protocol.
Không tự bịa requirement hoặc business rule.
```

### 3. Giao task

```text
Sử dụng workflow feature-documentation.

Project: FPTPlay
Feature: Notification Center

Yêu cầu:
- hỗ trợ push notification và in-app notification;
- segmentation;
- scheduling;
- tracking;
- audit log.

Thực hiện Researcher stage trước.
Sau đó dùng Research Report làm input cho ITBA.
Hỏi tôi khi cần business decision không thể suy ra từ tài liệu.
```

AI phải thực hiện theo trình tự:

```text
PULSE.md
  ↓
workflows/feature-documentation/
  ↓
agents/researcher/
  ↓
Research-Report
  ↓
agents/itba/
  ↓
BA-Document
```

## Repository structure

```text
pulse-agent-kit/
├── PULSE.md
├── README.md
├── COMMANDS.md
│
├── agents/
│   ├── researcher/
│   │   ├── manifest.yaml
│   │   ├── agent.md
│   │   ├── skills/
│   │   └── templates/
│   │
│   └── itba/
│       ├── manifest.yaml
│       ├── agent.md
│       ├── skills/
│       └── templates/
│
├── workflows/
│   └── feature-documentation/
│       ├── manifest.yaml
│       └── workflow.md
│
├── projects/
│   └── fptplay/
│       └── source-docs/
│
├── knowledge/
│   ├── shared/
│   └── projects/
│       └── fptplay/
│
├── tools/
├── schemas/
├── scripts/
├── pulse/
└── tests/
```

## Core concepts

### Repository protocol

`PULSE.md` là entry point bắt buộc cho AI.

Nó định nghĩa:

- thứ tự đọc repository;
- source priority;
- non-invention rules;
- workflow execution;
- agent handoff;
- clarification protocol;
- output traceability.

### Agent package

Agent package chứa:

```text
agents/<agent>/
├── manifest.yaml
├── agent.md
├── skills/
└── templates/
```

Agent là instruction package, không phải Python object và không cần model provider.

### Workflow package

Workflow package chứa:

```text
workflows/<workflow>/
├── manifest.yaml
└── workflow.md
```

Workflow xác định:

- required inputs;
- ordered stages;
- agent được dùng ở từng stage;
- skills cần đọc;
- output template;
- handoff giữa các agent;
- điều kiện phải hỏi lại người dùng.

### Project sources

Tài liệu gốc của dự án nằm tại:

```text
projects/<project>/source-docs/
```

AI ưu tiên tài liệu nguồn trước normalized knowledge.

### Knowledge và RAG

Normalized knowledge nằm tại:

```text
knowledge/projects/<project>/
```

RAG được dùng để tìm vùng nội dung liên quan, không thay thế source traceability.

## CLI

CLI là supporting tool dùng để duy trì repository, không phải AI runtime.

Các nhóm chức năng chính:

```bash
pulse workspace ...
pulse knowledge ...
pulse rag ...
```

Ví dụ:

```bash
pulse knowledge import fptplay projects/fptplay/source-docs --no-copy --overwrite
pulse rag build fptplay
pulse rag query fptplay "notification scheduling"
```

CLI hỗ trợ:

- khởi tạo workspace;
- import tài liệu;
- normalize knowledge;
- build và query RAG;
- validate repository artifacts.

AI vẫn có thể sử dụng Pulse bằng cách đọc trực tiếp repository mà không cần chạy CLI.

## Development

Cài project và development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Chạy validation:

```bash
python scripts/validate_repo.py
python scripts/validate_workflows.py
```

Chạy test:

```bash
python -m pytest -q
```

## Current workflow

Workflow end-to-end hiện có:

```text
feature-documentation
```

Nó phối hợp:

```text
Researcher
    ↓ Research-Report
ITBA
    ↓ BA-Document
```

Xem:

```text
workflows/feature-documentation/
```

## Principles

Pulse tuân thủ các nguyên tắc:

1. Provider independent.
2. Repository native.
3. AI readable.
4. Evidence before inference.
5. Không tự bịa business requirements.
6. Agent handoff phải giữ traceability.
7. Python chỉ là supporting tooling.
8. Workflow và instruction quality quan trọng hơn runtime complexity.

## Documentation

- [`PULSE.md`](PULSE.md) — protocol AI phải đọc đầu tiên.
- [`COMMANDS.md`](COMMANDS.md) — CLI và legacy command reference.
- [`workflows/`](workflows/) — workflow packages.
- [`agents/`](agents/) — agent packages.
- [`knowledge/README.md`](knowledge/README.md) — knowledge và RAG.
- [`tools/README.md`](tools/README.md) — tool registry.