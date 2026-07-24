# README changes

- Fix clone URL to `https://github.com/duongdang1136/pulse-agent-kit.git`.
- Replace `bash scripts/ingest.sh ...` with `python scripts/rag.py ingest ... --provider local`.
- Document `.rag/index.json` + `.rag/vectors.json` and local/OpenAI-compatible embedding providers.
- Add `python scripts/validate_repo.py` and `pytest -q` to contributor workflow.
