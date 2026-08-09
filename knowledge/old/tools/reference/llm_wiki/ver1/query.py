"""Query pipeline: embed question → retrieve wiki pages → stream answer.

Uses prompt caching on the system prompt for cost efficiency.
With --save, files the synthesized answer back as a new wiki page (Karpathy principle:
"valuable answers become new wiki pages, enriching future sessions").
"""

from __future__ import annotations

import re
import textwrap
from datetime import datetime, timezone

import anthropic
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from llm_wiki import embeddings, prompts
from llm_wiki import wiki as wiki_mod
from llm_wiki.config import WIKI_DIR, WikiSchema
from llm_wiki.index import EmbeddingIndex
from llm_wiki.wiki import WikiPage

console = Console(legacy_windows=False)


def _slug_from_question(question: str) -> str:
    """Derive a safe wiki slug from a question string."""
    slug = question.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s-]+", "_", slug)
    return slug[:60].strip("_") or "answer"


def query(question: str, top_k: int = 5, verbose: bool = False, save: bool = False) -> None:
    emb_index = EmbeddingIndex.load()

    if not emb_index.entries:
        console.print(
            "[red]No wiki pages indexed yet.[/red] "
            "Run `llm-wiki ingest <source>` first."
        )
        return

    # ── Step 1: Embed the question ────────────────────────────────────────────
    query_vec = embeddings.embed(question)

    # ── Step 2: Retrieve top-k wiki pages by cosine similarity ───────────────
    results = emb_index.search(query_vec, top_k=top_k)

    if not results:
        console.print("[yellow]No relevant wiki pages found.[/yellow]")
        return

    if verbose:
        table = Table(title="Retrieved Wiki Pages", show_lines=True)
        table.add_column("Rank", style="dim", width=5)
        table.add_column("Page")
        table.add_column("Slug")
        table.add_column("Score", justify="right")
        for rank, (slug, score) in enumerate(results, 1):
            entry = emb_index.entries.get(slug)
            table.add_row(str(rank), entry.title if entry else slug, slug, f"{score:.4f}")
        console.print(table)

    # ── Step 3: Load page bodies and assemble context ─────────────────────────
    context_parts: list[str] = []
    source_titles: list[str] = []
    total_chars = 0
    char_cap = 30_000

    for slug, _ in results:
        page = wiki_mod.load_page(slug)
        if page is None:
            continue
        chunk = f"### {page.title}\n\n{page.body}"
        if total_chars + len(chunk) > char_cap:
            break
        context_parts.append(chunk)
        source_titles.append(page.title)
        total_chars += len(chunk)

    context = "\n\n---\n\n".join(context_parts)

    # ── Step 4: Stream the answer ─────────────────────────────────────────────
    console.print()
    console.print(Panel(f"[bold]{question}[/bold]", title="Question", border_style="blue"))
    console.print()

    client = anthropic.Anthropic()
    answer_chunks: list[str] = []

    with client.messages.stream(
        model=prompts.MODEL,
        max_tokens=1024,
        # Cache the answer system prompt — identical across all queries in a session
        system=[{
            "type": "text",
            "text": prompts.ANSWER_SYSTEM,
            "cache_control": {"type": "ephemeral"},
        }],
        messages=[{
            "role": "user",
            "content": prompts.answer_user(question, context),
        }],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            if save:
                answer_chunks.append(text)

    print()  # newline after streamed output
    console.print()
    console.print(f"[dim]Sources: {', '.join(source_titles)}[/dim]")

    # ── Step 5: File answer back as a wiki page (Karpathy compounding principle)
    if save:
        _file_answer_as_page(question, "".join(answer_chunks), source_titles, emb_index)


def _file_answer_as_page(
    question: str,
    answer_text: str,
    source_titles: list[str],
    emb_index: EmbeddingIndex,
) -> None:
    """Save the synthesized answer as a new wiki page and update the embedding index."""
    slug = _slug_from_question(question)

    # Avoid overwriting existing schema-managed pages
    existing_path = WIKI_DIR / f"{slug}.md"
    if existing_path.exists():
        # Append suffix to avoid collision
        slug = slug + "_q"

    title = question.rstrip("?") if len(question) <= 80 else question[:77] + "..."
    body = textwrap.dedent(f"""\
        ## Question

        {question}

        ## Answer

        {answer_text}

        ## See Also

        {chr(10).join(f'- [[{t.lower().replace(" ", "_")}]]' for t in source_titles)}
    """).strip()

    page = WikiPage(
        slug=slug,
        title=title,
        tags=["query-answer"],
        updated=datetime.now(timezone.utc),
        sources=source_titles,
        body=body,
    )
    page.to_file()
    console.print(f"\n  [green]OK[/green] Answer filed → wiki/{slug}.md")

    # Re-embed and add to index
    vec = embeddings.embed(page.full_text)
    emb_index.upsert(slug, title, vec)
    emb_index.save()
    console.print(f"  [green]OK[/green] Embedding updated for {slug}")
