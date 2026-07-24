# Apply PR #3

Extract into the repository root, then run:

```cmd
python -m pytest -q
python scripts/validate_workflows.py
python scripts/validate_repo.py
git status --short
```

Primary AI instruction:

```text
Read PULSE.md first. Use the feature-documentation workflow for project FPTPlay. Run Researcher before ITBA. Preserve sources, assumptions, conflicts, and open questions.
```
