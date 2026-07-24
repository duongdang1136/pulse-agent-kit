from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class DocumentRecord:
    id: str
    title: str
    project: str
    source: str
    page: str
    checksum: str
    source_type: str
    status: str = "imported"
    created_at: str = ""
    updated_at: str = ""
    char_count: int = 0
    chunk_strategy: str = ""
    chunk_count: int = 0
    index_fingerprint: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class Chunk:
    id: str
    document_id: str
    text: str
    ordinal: int
    level: str = "leaf"
    heading: str = ""
    char_start: int = 0
    char_end: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
