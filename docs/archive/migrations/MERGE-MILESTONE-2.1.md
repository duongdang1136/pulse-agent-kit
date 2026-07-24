# Merge Milestone 2.1

Extract this archive over the repository root, then run:

```bash
python -m pip install -e .
python -m pytest -q
pulse rag build fptplay --provider hash
pulse rag query fptplay "Playback event and ad event tracking"
```

The first build automatically migrates the old `knowledge/projects/<project>/imports.json` into `manifest.json`. Do not delete imported pages.
