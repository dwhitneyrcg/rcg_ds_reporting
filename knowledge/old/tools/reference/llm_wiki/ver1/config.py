from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path


def find_root() -> Path:
    """Walk up from cwd to find project root (directory with pyproject.toml).
    Override with LLM_WIKI_ROOT env var."""
    if root := os.environ.get("LLM_WIKI_ROOT"):
        return Path(root)
    current = Path.cwd()
    for parent in [current, *current.parents]:
        if (parent / "pyproject.toml").exists():
            return parent
    return current


ROOT = find_root()
WIKI_DIR = ROOT / "wiki"
META_DIR = WIKI_DIR / ".meta"
SOURCES_DIR = ROOT / "sources"
SCHEMA_PATH = META_DIR / "schema.json"
EMBEDDINGS_PATH = META_DIR / "embeddings.json"
INDEX_PATH = WIKI_DIR / "index.md"
LOG_PATH = WIKI_DIR / "log.md"


@dataclass
class PageSpec:
    slug: str
    title: str
    description: str
    tags: list[str] = field(default_factory=list)


@dataclass
class WikiSchema:
    wiki_name: str
    pages: list[PageSpec]

    @classmethod
    def load(cls) -> "WikiSchema":
        if not SCHEMA_PATH.exists():
            raise FileNotFoundError(
                f"Schema not found at {SCHEMA_PATH}.\nRun `python main.py init` first."
            )
        data = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        pages = [PageSpec(**p) for p in data["pages"]]
        return cls(wiki_name=data["wiki_name"], pages=pages)

    def page_by_slug(self, slug: str) -> PageSpec | None:
        return next((p for p in self.pages if p.slug == slug), None)

    def summary_lines(self) -> list[str]:
        """One-line summary per page, for the routing prompt."""
        return [f"- {p.slug}: {p.title} — {p.description}" for p in self.pages]
