#!/usr/bin/env python3
from pathlib import Path
from datetime import date
import argparse, re, shutil
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(); p.add_argument("name"); a=p.parse_args()
if not re.fullmatch(r"[a-z0-9][a-z0-9-]*",a.name): raise SystemExit("Use lowercase letters, digits, hyphens")
src=ROOT/"knowledge/projects/_template"; dst=ROOT/"knowledge/projects"/a.name
if dst.exists(): raise SystemExit(f"Already exists: {dst}")
shutil.copytree(src,dst)
cfg=dst/"project.yaml"; cfg.write_text(cfg.read_text().replace("name: template",f"name: {a.name}").replace("2026-07-24",date.today().isoformat()))
print(dst.relative_to(ROOT))
