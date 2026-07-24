from __future__ import annotations

import re
from dataclasses import dataclass

from .models import Chunk


@dataclass(frozen=True)
class ChunkPolicy:
    strategy: str
    target_chars: int
    overlap_chars: int
    hierarchical: bool = False


def choose_policy(char_count: int) -> ChunkPolicy:
    if char_count <= 3_000:
        return ChunkPolicy("whole", max(char_count, 1), 0)
    if char_count <= 20_000:
        return ChunkPolicy("recursive", 2_200, 220)
    if char_count <= 100_000:
        return ChunkPolicy("hierarchical", 3_200, 280, True)
    return ChunkPolicy("streaming_hierarchical", 3_600, 240, True)


def chunk_document(document_id: str, text: str, policy: ChunkPolicy) -> list[Chunk]:
    text = text.strip()
    if not text:
        return []
    if policy.strategy == "whole":
        return [Chunk(f"{document_id}:0001", document_id, text, 1, char_end=len(text))]

    units = _structural_units(text)
    leaves: list[Chunk] = []
    current = ""
    heading = ""
    ordinal = 1
    cursor = 0

    def flush() -> None:
        nonlocal current, ordinal, cursor
        body = current.strip()
        if not body:
            return
        start = max(text.find(body, cursor), cursor)
        end = start + len(body)
        leaves.append(Chunk(
            id=f"{document_id}:{ordinal:04d}",
            document_id=document_id,
            text=body,
            ordinal=ordinal,
            heading=heading,
            char_start=start,
            char_end=end,
        ))
        ordinal += 1
        cursor = end
        current = ""

    for unit in units:
        if unit.startswith("#"):
            heading = unit.lstrip("# ").strip()
        if len(unit) > policy.target_chars:
            flush()
            for part in _hard_split(unit, policy.target_chars, policy.overlap_chars):
                current = part
                flush()
            continue
        candidate = f"{current}\n\n{unit}".strip() if current else unit
        if current and len(candidate) > policy.target_chars:
            previous_tail = current[-policy.overlap_chars:] if policy.overlap_chars else ""
            flush()
            current = f"{previous_tail}\n\n{unit}".strip()
        else:
            current = candidate
    flush()

    if policy.hierarchical:
        summaries = _section_parent_chunks(document_id, leaves)
        return summaries + leaves
    return leaves


def _structural_units(text: str) -> list[str]:
    # Preserve headings, tables, lists and paragraphs before falling back to hard split.
    blocks = re.split(r"\n{2,}", text.replace("\r\n", "\n").replace("\r", "\n"))
    return [block.strip() for block in blocks if block.strip()]


def _hard_split(text: str, target: int, overlap: int) -> list[str]:
    parts: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + target, len(text))
        if end < len(text):
            boundary = max(text.rfind(". ", start, end), text.rfind("\n", start, end), text.rfind(" ", start, end))
            if boundary > start + target // 2:
                end = boundary + 1
        parts.append(text[start:end].strip())
        if end >= len(text):
            break
        start = max(end - overlap, start + 1)
    return [part for part in parts if part]


def _section_parent_chunks(document_id: str, leaves: list[Chunk]) -> list[Chunk]:
    grouped: dict[str, list[Chunk]] = {}
    for chunk in leaves:
        grouped.setdefault(chunk.heading or "Document", []).append(chunk)
    parents: list[Chunk] = []
    for ordinal, (heading, chunks) in enumerate(grouped.items(), start=1):
        preview = "\n\n".join(chunk.text[:700] for chunk in chunks[:4])
        parents.append(Chunk(
            id=f"{document_id}:section:{ordinal:03d}",
            document_id=document_id,
            text=f"Section: {heading}\n\n{preview}"[:3000],
            ordinal=ordinal,
            level="section",
            heading=heading,
            metadata={"child_ids": [chunk.id for chunk in chunks]},
        ))
    return parents
