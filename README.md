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

## Các cách sử dụng và giới hạn tính năng

Pulse có thể được dùng theo nhiều cách. Tính năng dùng được phụ thuộc vào việc
AI có quyền ghi vào repository và có chạy được CLI hay không.

### Mode 1 - Đọc từ GitHub URL

Dùng cách này khi bạn đưa link repository đã publish cho AI:

```text
https://github.com/duongdang1136/pulse-agent-kit
```

Ở mode này, Pulse hoạt động như một instruction protocol dạng read-only.

Dùng được:

- đọc `PULSE.md`, workflows, agents, skills, và templates;
- chạy theo workflow feature-documentation;
- tạo Research Report, BA Document, audit, brief, và recommendation trong chat/session;
- dùng các file có sẵn trong repository làm context nếu AI đọc được GitHub.

Mặc định không dùng được:

- tạo hoặc update file trong repository;
- chạy `pulse knowledge import`;
- upsert knowledge pages;
- rebuild `.rag/` indexes;
- lưu report đã generate ngược lại vào repo;
- commit hoặc push changes.

Nếu AI tạo report hoặc đề xuất update knowledge trong mode này, người dùng cần
tự đưa nội dung đó vào repository, hoặc chạy lại task trong local clone /
writable workspace.

### Mode 2 - Local clone hoặc writable workspace

Dùng cách này khi repository đã được clone về local và AI/tooling có quyền ghi
filesystem:

```bash
git clone https://github.com/duongdang1136/pulse-agent-kit.git
cd pulse-agent-kit
python -m pip install -e ".[dev]"
```

Dùng được:

- toàn bộ tính năng read-only protocol;
- tạo project và workspace files;
- import/upsert project knowledge bằng `pulse knowledge import`;
- set import category bằng `--category`;
- rebuild và query RAG indexes;
- query project knowledge cùng shared knowledge bằng `--include-shared`;
- validate repository artifacts;
- tạo commit và push changes khi có Git access.

Với project thật, nên tách protocol repo và output docs ra hai folder cùng cấp:

```text
fptplay/
  pulse-agent-kit/        protocol, CLI, agents, workflows
  docs/                   report và deliverable do AI generate
```

`pulse-agent-kit/` là nơi chứa protocol/tooling. `docs/` là project output
workspace, dùng để lưu Research Report, BA Document, audit, API doc, business
rules, acceptance criteria, metrics, và các report khác theo phân cấp nghiệp vụ.

### Lưu ý về write access

Không cấp direct commit/push access cho third-party AI tools, trừ khi bạn thật
sự tin môi trường đó và muốn nó chỉnh repository. Cách dùng bình thường là đưa
GitHub URL như read-only context, hoặc làm việc trong local clone để bạn kiểm
soát thay đổi nào được commit và push.

### 2. Mở session chat AI và yêu cầu AI đọc protocol

```text
Hãy đọc repository pulse-agent-kit này.

Đọc PULSE.md trước và tuân thủ repository operating protocol.
Không tự bịa requirement hoặc business rule.
```

### 3. Giao task trong cùng session chat

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

Hãy chạy đúng workflow đã khai báo trong repository.
Không tự bịa requirement hoặc business rule.
Hỏi tôi khi cần business decision không thể suy ra từ tài liệu.
```

AI sẽ đọc workflow và thực hiện theo trình tự đã khai báo:

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

### Project Sources, Knowledge, and RAG

Pulse separates original project inputs from reusable knowledge and search indexes.

```text
projects/
  fptplay/
    source-docs/          original project documents supplied by user/project

knowledge/
  shared/                 reusable cross-project knowledge
  projects/
    fptplay/              normalized project knowledge
      pages/              Markdown knowledge pages
      .rag/               generated search index/vector files
```

**Project sources** live in `projects/<project>/source-docs/`.

- Original files: briefs, specs, screenshots, meeting notes, exported docs, API notes.
- Source of truth for project-specific facts.
- Higher priority than normalized knowledge when sources conflict.
- Should remain traceable; do not overwrite them with AI summaries.

**Knowledge** lives in `knowledge/shared/` and `knowledge/projects/<project>/`.

- `knowledge/shared/pages/` contains reusable cross-project knowledge.
- `knowledge/projects/<project>/pages/` contains reviewed, normalized project knowledge.
- Knowledge pages are derived from approved sources or reviewed workflow outputs.
- Knowledge is optimized for reuse; it is not a replacement for source evidence.

**RAG** lives under each knowledge scope in `.rag/`.

- RAG indexes knowledge pages so AI/CLI can find relevant context quickly.
- RAG is a navigation aid, not an authority layer.
- When RAG returns a hit, cite the knowledge page and its original source.

Typical upsert flow:

```text
1. Put original docs in projects/<project>/source-docs/.
2. Import/normalize reviewed docs into knowledge/projects/<project>/pages/.
3. Build or rebuild the RAG index.
4. Researcher queries RAG, then verifies against sources when needed.
```

CLI example:

```bash
pulse knowledge import fptplay projects/fptplay/source-docs --overwrite
pulse rag build fptplay
pulse rag query fptplay "notification scheduling"
```

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
- lưu generated docs theo epic / feature / sub-feature;
- build và query RAG;
- validate repository artifacts.

AI vẫn có thể sử dụng Pulse bằng cách đọc trực tiếp repository mà không cần chạy CLI.

## Project output docs

Khi dùng local clone, generated docs nên được lưu ngoài `pulse-agent-kit/`:

```text
fptplay/
  pulse-agent-kit/
  docs/
    fptplay/
      manifest.json
      epics/
        notification/
          features/
            notification-center/
              ba-document.md
              research-report.md
              sub-features/
                push-notification/
                  business-rules.md
      .rag/
```

Mỗi file được lưu theo:

```text
docs/<project>/epics/<epic>/features/<feature>/<type>.md
docs/<project>/epics/<epic>/features/<feature>/sub-features/<sub-feature>/<type>.md
```

CLI chính:

```bash
pulse docs init ../docs --project fptplay
pulse docs path ../docs --project fptplay --epic notification --feature notification-center --type ba-document
pulse docs add ../docs ./ba-document.md --project fptplay --epic notification --feature notification-center --type ba-document --status reviewed
pulse docs list ../docs --project fptplay
pulse docs index ../docs --project fptplay
pulse rag query fptplay "quiet hours" --include-docs --docs-workspace ../docs
```

Chỉ docs có `status` là `reviewed` hoặc `approved` mới được bật `rag_enabled`
mặc định và được index vào docs RAG. Draft report vẫn được lưu trong manifest
nhưng không nên dùng làm reusable context.

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
