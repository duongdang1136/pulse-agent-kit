"""Manifest-driven AutoRAG pipeline for Pulse."""

from .pipeline import build_index, query_index

__all__ = ["build_index", "query_index"]
