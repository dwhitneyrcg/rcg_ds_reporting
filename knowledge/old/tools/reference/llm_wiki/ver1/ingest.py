"""Ingest pipeline: raw source document → synthesized wiki pages.

Supports local files, HTTP/HTTPS URLs, and YouTube URLs (transcript extraction).
All Claude API calls use prompt caching on system prompts for cost efficiency.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env if present

import anthropic
from rich.console import Console

from llm_wiki import embeddings, prompts
from llm_wiki import wiki as wiki_mod
from llm_wiki.config import INDEX_PATH, LOG_PATH, SOURCES_DIR, WikiSchema
from llm_wiki.index import EmbeddingIndex
from llm_wiki.wiki import WikiPage

console = Console(legacy_windows=False)
_client: anthropic.Anthropic | None = None


def _get_client() -> anthropic.Anthropic:
    global _client
    if _client is None:
        _client = anthropic.Anthropic()
    return _client


# ── Source resolution helpers ─────────────────────────────────────────────────

def _is_youtube_url(url: str) -> bool:
    return "youtube.com/watch" in url or "youtu.be/" in url


def _fetch_youtube_transcript(url: str) -> tuple[str, str]:
    """Return (filename_stem, transcript_text) for a YouTube URL."""
    import re as _re
    # Extract video ID
    vid_match = _re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", url)
    if not vid_match:
        raise ValueError(f"Cannot parse YouTube video ID from: {url}")
    video_id = vid_match.group(1)

    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        ytt = YouTubeTranscriptApi()
        transcript = ytt.fetch(video_id)
        lines = [f"[{int(t.start)}s] {t.text}" for t in transcript]
        text = "\n".join(lines)
        return f"youtube_{video_id}", text
    except Exception as exc:
        raise RuntimeError(
            f"Could not fetch YouTube transcript for {video_id}: {exc}\n"
            "Ensure youtube-transcript-api is installed: pip install youtube-transcript-api"
        ) from exc


def _fetch_url(url: str) -> tuple[str, str]:
    """Return (filename_stem, page_text) for a generic HTTP/HTTPS URL."""
    import urllib.request
    import urllib.parse
    import html.parser

    class _TextExtractor(html.parser.HTMLParser):
        """Minimal HTML → plain text extractor."""
        def __init__(self):
            super().__init__()
            self._skip = False
            self._chunks: list[str] = []

        def handle_starttag(self, tag, attrs):
            if tag in ("script", "style", "nav", "header", "footer"):
                self._skip = True

        def handle_endtag(self, tag):
            if tag in ("script", "style", "nav", "header", "footer"):
                self._skip = False

        def handle_data(self, data):
            if not self._skip:
                stripped = data.strip()
                if stripped:
                    self._chunks.append(stripped)

        def get_text(self) -> str:
            return "\n".join(self._chunks)

    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        raw_html = resp.read().decode("utf-8", errors="replace")

    parser = _TextExtractor()
    parser.feed(raw_html)
    text = parser.get_text()

    # Derive a filename stem from the URL path
    parsed = urllib.parse.urlparse(url)
    stem = (parsed.netloc + parsed.path).replace("/", "_").strip("_") or "webpage"
    stem = re.sub(r"[^\w_-]", "_", stem)[:80]
    return stem, text


def resolve_source(source: str) -> tuple[str, str]:
    """Resolve a source string to (display_name, text).

    Accepts:
    - Local file path (Path-like string)
    - YouTube URL  → extracts transcript
    - Any other URL → fetches and strips HTML
    """
    if source.startswith("http://") or source.startswith("https://"):
        if _is_youtube_url(source):
            console.print(f"  [dim]Fetching YouTube transcript...[/dim]")
            stem, text = _fetch_youtube_transcript(source)
        else:
            console.print(f"  [dim]Fetching URL...[/dim]")
            stem, text = _fetch_url(source)
        # Optionally persist raw transcript to sources/ for provenance
        raw_path = SOURCES_DIR / f"{stem}.txt"
        if not raw_path.exists():
            SOURCES_DIR.mkdir(parents=True, exist_ok=True)
            raw_path.write_text(text, encoding="utf-8")
            console.print(f"  [dim]Saved raw source → sources/{stem}.txt[/dim]")
        return stem + ".txt", text
    else:
        path = Path(source)
        text = path.read_text(encoding="utf-8", errors="replace")
        return path.name, text


def ingest(source_paths: list[Path], dry_run: bool = False) -> None:
    schema = WikiSchema.load()
    emb_index = EmbeddingIndex.load()

    for source_path in source_paths:
        console.rule(f"[bold blue]Ingesting: {source_path.name}")
        source_text = source_path.read_text(encoding="utf-8", errors="replace")[:50_000]
        display_name = source_path.name

        if dry_run:
            all_slugs = [p.slug for p in schema.pages]
            console.print(f"[dim]  (dry-run) Would route against: {', '.join(all_slugs)}[/dim]")
            console.print("[dim]  (dry-run) No API calls made, no files written.[/dim]")
            continue

        # ── Step 1: Route - which pages are relevant to this source? ──────────
        schema_summary = "\n".join(schema.summary_lines())
        route_resp = _get_client().messages.create(
            model=prompts.MODEL,
            max_tokens=256,
            # Cache the routing system prompt — reused across every source in the batch
            system=[{
                "type": "text",
                "text": prompts.ROUTING_SYSTEM,
                "cache_control": {"type": "ephemeral"},
            }],
            messages=[{
                "role": "user",
                "content": prompts.routing_user(schema_summary, display_name, source_text),
            }],
        )
        raw = route_resp.content[0].text.strip()
        match = re.search(r"\[.*?\]", raw, re.DOTALL)
        relevant_slugs: list[str] = json.loads(match.group()) if match else []

        if not relevant_slugs:
            console.print(f"[yellow]  No relevant wiki pages found for {display_name}[/yellow]")
            continue

        console.print(f"[green]  Relevant pages:[/green] {', '.join(relevant_slugs)}")

        # Other pages (for cross-reference awareness in synthesis prompt)
        other_pages = [
            f"- {p.slug}: {p.title}" for p in schema.pages if p.slug not in relevant_slugs
        ]

        updated_summaries: list[dict] = []

        # ── Step 2: Synthesize each relevant page ─────────────────────────────
        for slug in relevant_slugs:
            spec = schema.page_by_slug(slug)
            if spec is None:
                console.print(f"[yellow]  Slug '{slug}' not in schema - skipping[/yellow]")
                continue

            existing_page = wiki_mod.load_page(slug)
            existing_body = existing_page.body if existing_page else None

            console.print(f"  [cyan]Synthesizing[/cyan] → {spec.title}...")

            synth_resp = _get_client().messages.create(
                model=prompts.MODEL,
                max_tokens=2048,
                # Cache the synthesis system prompt — identical across all page synths
                system=[{
                    "type": "text",
                    "text": prompts.SYNTHESIS_SYSTEM,
                    "cache_control": {"type": "ephemeral"},
                }],
                messages=[{
                    "role": "user",
                    "content": prompts.synthesis_user(
                        title=spec.title,
                        description=spec.description,
                        existing_body=existing_body,
                        filename=display_name,
                        source_text=source_text,
                        other_pages=other_pages,
                    ),
                }],
            )
            new_body = synth_resp.content[0].text.strip()

            # Merge provenance sources list (preserve existing)
            prev_sources = existing_page.sources if existing_page else []
            sources = list(dict.fromkeys(prev_sources + [display_name]))

            page = WikiPage(
                slug=slug,
                title=spec.title,
                tags=spec.tags,
                updated=datetime.now(timezone.utc),
                sources=sources,
                body=new_body,
            )
            page.to_file()
            console.print(f"  [green]OK[/green] wiki/{slug}.md written")

            # Re-embed the updated page
            vec = embeddings.embed(page.full_text)
            emb_index.upsert(slug, spec.title, vec)

            # Extract first prose line for the index summary
            summary_line = next(
                (ln.strip() for ln in new_body.splitlines() if ln.strip() and not ln.startswith("#")),
                spec.description,
            )
            updated_summaries.append({
                "slug": slug,
                "title": spec.title,
                "summary": summary_line[:120],
                "tags": ", ".join(spec.tags),
                "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            })

        # ── Step 3: Persist embeddings ────────────────────────────────────────
        emb_index.save()
        console.print("  [green]OK[/green] Embeddings saved")

        # ── Step 4: Update wiki/index.md ──────────────────────────────────────
        if updated_summaries:
            _update_index(updated_summaries)

        # ── Step 5: Append to wiki/log.md ─────────────────────────────────────
        _append_log(display_name, relevant_slugs)

    console.print("\n[bold green]Ingest complete.[/bold green]")


def ingest_sources(sources: list[str], dry_run: bool = False) -> None:
    """Ingest sources that may be local file paths, HTTP/HTTPS URLs, or YouTube URLs.

    For URL sources, content is fetched and persisted to sources/ before ingestion
    so provenance is preserved and the file-based ingest pipeline runs unchanged.
    """
    resolved_paths: list[Path] = []
    for source in sources:
        if source.startswith("http://") or source.startswith("https://"):
            console.rule(f"[bold blue]Resolving URL: {source[:80]}")
            try:
                display_name, text = resolve_source(source)
                raw_path = SOURCES_DIR / display_name
                if not raw_path.exists():
                    SOURCES_DIR.mkdir(parents=True, exist_ok=True)
                    raw_path.write_text(text[:50_000], encoding="utf-8")
                    console.print(f"  [dim]Persisted → sources/{display_name}[/dim]")
                resolved_paths.append(raw_path)
            except Exception as exc:
                console.print(f"  [red]Failed to resolve {source}: {exc}[/red]")
        else:
            resolved_paths.append(Path(source))

    if resolved_paths:
        ingest(resolved_paths, dry_run=dry_run)


def _update_index(updated_pages: list[dict]) -> None:
    current_index = INDEX_PATH.read_text(encoding="utf-8") if INDEX_PATH.exists() else ""
    resp = _get_client().messages.create(
        model=prompts.MODEL,
        max_tokens=1024,
        system=[{
            "type": "text",
            "text": prompts.INDEX_SYSTEM,
            "cache_control": {"type": "ephemeral"},
        }],
        messages=[{
            "role": "user",
            "content": prompts.index_user(current_index, updated_pages),
        }],
    )
    INDEX_PATH.write_text(resp.content[0].text.strip() + "\n", encoding="utf-8")
    console.print("  [green]OK[/green] wiki/index.md updated")


def _append_log(filename: str, updated_slugs: list[str]) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    entry = f"\n## {ts} - Ingest: {filename}\n- Updated pages: {', '.join(updated_slugs)}\n"
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(entry)
    console.print("  [green]OK[/green] wiki/log.md updated")
