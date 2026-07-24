# Merge Milestone 2

```cmd
mkdir milestone-2
tar -xf pulse-agent-kit-milestone-2.zip -C milestone-2
xcopy milestone-2\* . /E /I /Y
rmdir /S /Q milestone-2
python -m pip install -e .
python -m pytest -q
python scripts\validate_repo.py
pulse doctor
```

Commit implementation only:

```cmd
del MERGE-MILESTONE-2.md
git add pyproject.toml pulse tests docs\MILESTONE-2-KNOWLEDGE-INGESTION.md
git commit -m "feat: add project knowledge ingestion CLI"
git pull --rebase origin main
git push origin main
```
