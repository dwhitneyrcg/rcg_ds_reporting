"""EmbeddingIndex — cosine search over wiki page embeddings, stored as JSON."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env if present
import numpy as np

from llm_wiki.config import EMBEDDINGS_PATH
from llm_wiki.embeddings import DIMENSION, MODEL_NAME


@dataclass
class EmbeddingEntry:
    title: str
    embedding: list[float]
    updated: str  # ISO-format timestamp


@dataclass
class EmbeddingIndex:
    model_name: str = MODEL_NAME
    dimension: int = DIMENSION
    entries: dict[str, EmbeddingEntry] = field(default_factory=dict)

    def upsert(self, slug: str, title: str, embedding: list[float]) -> None:
        self.entries[slug] = EmbeddingEntry(
            title=title,
            embedding=embedding,
            updated=datetime.now(timezone.utc).isoformat(),
        )

    def search(self, query_vec: list[float], top_k: int = 5) -> list[tuple[str, float]]:
        """Return top-k (slug, cosine_similarity) pairs, sorted descending."""
        if not self.entries:
            return []
        q = np.array(query_vec, dtype=np.float32)
        results = [
            (slug, float(np.dot(q, np.array(entry.embedding, dtype=np.float32))))
            for slug, entry in self.entries.items()
        ]
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:top_k]

    @classmethod
    def load(cls) -> "EmbeddingIndex":
        if not EMBEDDINGS_PATH.exists():
            return cls()
        data = json.loads(EMBEDDINGS_PATH.read_text(encoding="utf-8"))
        entries = {
            slug: EmbeddingEntry(**e)
            for slug, e in data.get("pages", {}).items()
        }
        return cls(
            model_name=data.get("model", MODEL_NAME),
            dimension=data.get("dimension", DIMENSION),
            entries=entries,
        )

    def save(self) -> None:
        EMBEDDINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "model": self.model_name,
            "dimension": self.dimension,
            "pages": {
                slug: {
                    "title": e.title,
                    "embedding": e.embedding,
                    "updated": e.updated,
                }
                for slug, e in self.entries.items()
            },
        }
        EMBEDDINGS_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")
