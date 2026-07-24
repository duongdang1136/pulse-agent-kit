# Upgrade migration

1. Delete the obsolete parser: `rm scripts/ingest.sh`.
2. Install dependencies: `python -m pip install -r requirements.txt`.
3. For local semantic embeddings: `python -m pip install sentence-transformers`.
4. Rebuild: `python scripts/rag.py ingest knowledge/shared --provider local`.
5. Validate: `python scripts/validate_repo.py && pytest -q`.

The old shell parser used `grep`/`sed` and could misread valid YAML such as multiline values, nested objects, comments, and several list formats. The replacement uses PyYAML and creates chunk-level vector indexes.
