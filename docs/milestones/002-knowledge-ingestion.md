# Milestone 2 — Knowledge ingestion

Pulse can now normalize project source files into Markdown knowledge pages while preserving the originals in the BA workspace.

## Supported formats

- Markdown (`.md`, `.markdown`)
- Text (`.txt`)
- PDF (`.pdf`, text extraction only; scanned PDFs require OCR outside this milestone)
- Word (`.docx`, paragraphs and tables)
- Excel (`.xlsx`, worksheets rendered as Markdown tables)

## Workflow

```bash
pulse project create "FPTPlay"
pulse knowledge import fptplay "C:\Docs\FPTPlay"
pulse knowledge list fptplay
pulse rag build fptplay --provider local
pulse rag query fptplay "What is the login flow?"
```

Every normalized page contains source metadata and a SHA-256 checksum. Importing does not automatically promote statements into decisions, assumptions, or glossary entries. Those records require an explicit extraction-and-review workflow in a later milestone.

## Duplicate behavior

Existing normalized pages are skipped by default. Use `--overwrite` to regenerate them.

```bash
pulse knowledge import fptplay "C:\Docs\FPTPlay" --overwrite
```

Use `--no-copy` when the source documents must remain outside the repository.
