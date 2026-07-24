# Apply LICENSE

Copy the `LICENSE` file to the repository root:

```text
pulse-agent-kit/
├── LICENSE
├── README.md
├── PULSE.md
└── pyproject.toml
```

Recommended `pyproject.toml` metadata:

```toml
[project]
license = { file = "LICENSE" }
```

Then commit:

```bash
git add LICENSE pyproject.toml
git commit -m "chore: add MIT license"
git push origin main
```
