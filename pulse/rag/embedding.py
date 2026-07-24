from __future__ import annotations

import hashlib
import math
import re
from typing import Protocol


class Embedder(Protocol):
    name: str
    model: str
    dimensions: int
    def embed_batch(self, texts: list[str]) -> list[list[float]]: ...


class HashEmbedder:
    name = "hash"
    model = "pulse-hash-v2"

    def __init__(self, dimensions: int = 384) -> None:
        self.dimensions = dimensions

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        return [self._embed(text) for text in texts]

    def _embed(self, text: str) -> list[float]:
        vector = [0.0] * self.dimensions
        tokens = re.findall(r"[\w.-]+", text.lower(), flags=re.UNICODE)
        for token in tokens:
            digest = hashlib.blake2b(token.encode("utf-8"), digest_size=16).digest()
            index = int.from_bytes(digest[:4], "big") % self.dimensions
            sign = 1.0 if digest[4] & 1 else -1.0
            vector[index] += sign
        norm = math.sqrt(sum(value * value for value in vector)) or 1.0
        return [value / norm for value in vector]


class LocalEmbedder:
    name = "local"

    def __init__(self, model: str | None = None) -> None:
        self.model = model or "sentence-transformers/all-MiniLM-L6-v2"
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError as exc:
            raise RuntimeError("Local embeddings require sentence-transformers") from exc
        self._encoder = SentenceTransformer(self.model)
        self.dimensions = int(self._encoder.get_sentence_embedding_dimension())

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        vectors = self._encoder.encode(texts, normalize_embeddings=True, show_progress_bar=False)
        return [vector.tolist() for vector in vectors]


def create_embedder(provider: str, model: str | None = None) -> Embedder:
    if provider == "hash":
        return HashEmbedder()
    if provider == "local":
        return LocalEmbedder(model)
    raise RuntimeError("OpenAI embeddings are not enabled in the dependency-free AutoRAG foundation yet")
