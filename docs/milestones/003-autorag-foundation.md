# Milestone 2.1 — AutoRAG Foundation

Pulse now uses a manifest-driven, incremental RAG pipeline. The CLI no longer shells out to `scripts/rag.py`.

## Pipeline

Ingestion writes `manifest.json`. Build reads only registered documents, applies adaptive chunking, embeds in batches, and atomically persists `.rag/chunks.jsonl` and `.rag/vectors.jsonl`. Query performs hybrid semantic + keyword retrieval, deduplication, reranking, and context-budget enforcement.

## Adaptive policy

- up to 3,000 characters: whole document
- 3,001–20,000: recursive structure-aware chunks
- 20,001–100,000: hierarchical section + leaf chunks
- over 100,000: streaming-hierarchical policy with bounded chunk size

## Scale behavior

Builds are incremental. Unchanged documents are skipped through checksum and index fingerprints. Embeddings are produced in bounded batches (`--batch-size`, default 64), so memory does not grow with the total knowledge-base size. Large production deployments can replace the JSONL stores behind the same pipeline interfaces later.

## Commands

```bash
pulse rag build fptplay --provider hash
pulse rag build fptplay --provider local --batch-size 32
pulse rag build fptplay --force
pulse rag query fptplay "How is ad_start tracked?" --top-k 5
```

Existing `imports.json` files are migrated automatically on the first build. `README.md` and arbitrary unregistered Markdown are never indexed.
