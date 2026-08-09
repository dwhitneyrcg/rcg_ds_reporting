"""WikiPage CRUD — reads/writes markdown files with YAML front matter."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import frontmatter

from llm_wiki.config import WIKI_DIR


@dataclass
class WikiPage:
    slug: str
    title: str
    tags: list[str]
    updated: datetime
    sources: list[str]  # provenance: raw source filenames that contributed
    body: str           # markdown body (front matter excluded)

    @property
    def full_text(self) -> str:
        """Title + body — used as the embedding unit."""
        return f"# {self.title}\n\n{self.body}"

    @property
    def path(self) -> Path:
        return WIKI_DIR / f"{self.slug}.md"

    @classmethod
    def from_file(cls, path: Path) -> "WikiPage":
        post = frontmatter.load(str(path))
        slug = path.stem
        updated = post.get("updated", datetime.now(timezone.utc).isoformat())
        if isinstance(updated, str):
            try:
                updated = datetime.fromisoformat(updated)
            except ValueError:
                updated = datetime.now(timezone.utc)
        return cls(
            slug=slug,
            title=post.get("title", slug),
            tags=post.get("tags", []),
            updated=updated,
            sources=post.get("sources", []),
            body=post.content,
        )

    def to_file(self, path: Path | None = None) -> None:
        target = path or self.path
        post = frontmatter.Post(
            self.body,
            title=self.title,
            slug=self.slug,
            tags=self.tags,
            updated=self.updated.isoformat(),
            sources=self.sources,
        )
        target.write_text(frontmatter.dumps(post), encoding="utf-8")


def load_page(slug: str) -> WikiPage | None:
    path = WIKI_DIR / f"{slug}.md"
    if not path.exists():
        return None
    return WikiPage.from_file(path)


def all_pages() -> list[WikiPage]:
    """Load all wiki pages (excludes index.md and log.md)."""
    paths = [p for p in sorted(WIKI_DIR.glob("*.md")) if p.stem not in ("index", "log")]
    return [WikiPage.from_file(p) for p in paths]
