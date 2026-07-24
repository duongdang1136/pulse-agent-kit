# Apply PR #1

Extract this archive into the repository root and allow existing agent
manifest files to be replaced.

Run:

```cmd
python -m pytest -q
python scripts/validate_repo.py
git status --short
```

This PR intentionally contains no LLM provider, model, API key, or runtime
configuration.
