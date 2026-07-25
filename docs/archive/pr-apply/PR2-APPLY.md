# Apply PR #2

Extract this archive into the repository root and replace existing files when
prompted.

Run:

```cmd
python -m pytest -q
python scripts/validate_repo.py
git diff --stat
```

Expected behavior:

- A UI task resolves `screen` and `heuristic-audit`.
- An audit task resolves only `heuristic-audit`.
- A task with no matching rule uses fallback skills.
- No LLM, provider, model, API key, or authentication is involved.
