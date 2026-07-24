from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any


def cosine(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b)) / ((math.sqrt(sum(x*x for x in a)) or 1.0) * (math.sqrt(sum(y*y for y in b)) or 1.0))


def tokenize(text: str) -> list[str]:
    return re.findall(r"[\w.-]+", text.lower(), flags=re.UNICODE)


def keyword_score(query: str, text: str) -> float:
    q = Counter(tokenize(query))
    d = Counter(tokenize(text))
    if not q or not d:
        return 0.0
    overlap = sum(min(count, d[token]) for token, count in q.items())
    phrase_bonus = 1.0 if query.lower() in text.lower() else 0.0
    return min(1.0, overlap / max(sum(q.values()), 1) + 0.25 * phrase_bonus)


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    tmp.replace(path)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows
