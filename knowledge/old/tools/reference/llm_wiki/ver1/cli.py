"""CLI entry point - ingest / query / lint / init / status commands."""

from __future__ import annotations

import json
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from llm_wiki.config import (
    EMBEDDINGS_PATH, INDEX_PATH, LOG_PATH, META_DIR, SCHEMA_PATH, SOURCES_DIR, WIKI_DIR,
)

console = Console(legacy_windows=False)

_DEFAULT_SCHEMA = {
    "wiki_name": "ML Fundamentals",
    "pages": [
        {
            "slug": "neural_networks",
            "title": "Neural Networks",
            "description": "Core concepts, architectures, and properties of artificial neural networks",
            "tags": ["ml", "deep-learning"],
        },
        {
            "slug": "backpropagation",
            "title": "Backpropagation",
            "description": "Gradient computation via chain rule, computational graphs, and training dynamics",
            "tags": ["ml", "deep-learning", "optimization"],
        },
        {
            "slug": "attention_mechanism",
            "title": "Attention Mechanism",
            "description": "Self-attention, queries/keys/values, and multi-head attention",
            "tags": ["ml", "nlp", "deep-learning"],
        },
        {
            "slug": "transformers",
            "title": "Transformers",
            "description": "Full transformer architecture, encoder-decoder, positional encoding",
            "tags": ["ml", "nlp", "deep-learning"],
        },
        {
            "slug": "applications",
            "title": "Applications",
            "description": "Real-world uses of transformers and deep learning in NLP, vision, and biology",
            "tags": ["ml", "applications"],
        },
    ],
}


@click.group()
def cli() -> None:
    """LLM Wiki - RAG over synthesized wiki pages (Karpathy pattern)."""


@cli.command()
def init() -> None:
    """Create wiki directory structure and schema template."""
    WIKI_DIR.mkdir(exist_ok=True)
    META_DIR.mkdir(exist_ok=True)
    SOURCES_DIR.mkdir(exist_ok=True)

    if SCHEMA_PATH.exists():
        console.print("[yellow]schema.json already exists - skipping.[/yellow]")
    else:
        SCHEMA_PATH.write_text(json.dumps(_DEFAULT_SCHEMA, indent=2), encoding="utf-8")
        console.print(f"[green]OK[/green] Created {SCHEMA_PATH}")

    if not INDEX_PATH.exists():
        INDEX_PATH.write_text("# Wiki Index\n\n*(empty - run `ingest` to populate)*\n", encoding="utf-8")
        console.print(f"[green]OK[/green] Created {INDEX_PATH}")

    if not LOG_PATH.exists():
        LOG_PATH.write_text("# Ingest Log\n\n", encoding="utf-8")
        console.print(f"[green]OK[/green] Created {LOG_PATH}")

    console.print("\n[bold green]Wiki initialized.[/bold green]")
    console.print(f"  Wiki dir:    [cyan]{WIKI_DIR}[/cyan]")
    console.print(f"  Sources dir: [cyan]{SOURCES_DIR}[/cyan]")
    console.print(f"  Schema:      [cyan]{SCHEMA_PATH}[/cyan]")
    console.print("\nNext steps:")
    console.print("  1. Add source documents to [cyan]sources/[/cyan]")
    console.print("  2. Run [cyan]python main.py ingest sources/<file>[/cyan]")
    console.print("  3. Run [cyan]python main.py query \"your question\"[/cyan]")


@cli.command()
@click.argument("sources", nargs=-1)
@click.option("--dry-run", is_flag=True, help="Show which pages would be updated without writing.")
def ingest(sources: tuple[str, ...], dry_run: bool) -> None:
    """Ingest SOURCE documents into the wiki.

    SOURCE can be one or more:
      - Local file paths (or a directory — ingests all files in it)
      - YouTube URLs  (transcript is extracted automatically)
      - HTTP/HTTPS URLs  (page text is fetched and stripped)

    Examples:
      llm-wiki ingest sources/paper.pdf
      llm-wiki ingest https://www.youtube.com/watch?v=VRub1w-APTc
      llm-wiki ingest https://arxiv.org/abs/2305.10601
    """
    from llm_wiki.ingest import ingest as _ingest, ingest_sources as _ingest_sources

    url_sources: list[str] = []
    file_paths: list[Path] = []

    for s in sources:
        if s.startswith("http://") or s.startswith("https://"):
            url_sources.append(s)
        else:
            p = Path(s)
            if not p.exists():
                console.print(f"[red]Path not found: {s}[/red]")
                continue
            if p.is_dir():
                file_paths.extend(sorted(p.iterdir()))
            else:
                file_paths.append(p)

    if not url_sources and not file_paths:
        console.print("[red]No source files or URLs specified.[/red]")
        return

    if url_sources:
        _ingest_sources(url_sources, dry_run=dry_run)
    if file_paths:
        _ingest(file_paths, dry_run=dry_run)


@cli.command()
@click.argument("question", required=False, default=None)
@click.option("--top-k", default=5, show_default=True, help="Number of wiki pages to retrieve.")
@click.option("--verbose", is_flag=True, help="Show retrieved pages and similarity scores.")
@click.option("--save", is_flag=True, help="File the answer back as a new wiki page (Karpathy compounding principle).")
@click.option("--template", "-t", default=None, help="Use a named query template (run `llm-wiki prompts` to list).")
def query(question: str | None, top_k: int, verbose: bool, save: bool, template: str | None) -> None:
    """Answer QUESTION using wiki pages as context (RAG).

    With --save, the synthesized answer is filed back as a new wiki page so
    future sessions benefit from the compiled knowledge (compounding principle).

    With --template, load a pre-built query from Wiki_prompts.md categories
    (run `llm-wiki prompts` to see all available templates).

    Examples:
      llm-wiki query "What is attention mechanism?"
      llm-wiki query --template blind-spot --save
      llm-wiki query --template integrity-report
    """
    from llm_wiki.query import query as _query
    from llm_wiki.prompts import QUERY_TEMPLATES

    if template:
        if template not in QUERY_TEMPLATES:
            console.print(f"[red]Unknown template '{template}'.[/red] Run `llm-wiki prompts` to see available templates.")
            return
        _, resolved_question = QUERY_TEMPLATES[template]
        console.print(f"[dim]Template:[/dim] [cyan]{template}[/cyan]")
    elif question:
        resolved_question = question
    else:
        console.print("[red]Provide a QUESTION or use --template.[/red]")
        return

    _query(resolved_question, top_k=top_k, verbose=verbose, save=save)


@cli.command("prompts")
@click.option("--category", "-c", default=None, help="Filter by category (Synthesis, Gap-Finding, Debate, Output, Health, Personal).")
def list_prompts(category: str | None) -> None:
    """List all built-in query templates from Wiki_prompts.md.

    Use these with: llm-wiki query --template <name>
    """
    from llm_wiki.prompts import QUERY_TEMPLATES

    by_category: dict[str, list[tuple[str, str]]] = {}
    for name, (cat, text) in QUERY_TEMPLATES.items():
        by_category.setdefault(cat, []).append((name, text))

    for cat, items in by_category.items():
        if category and category.lower() not in cat.lower():
            continue
        console.print(f"\n[bold cyan]── {cat} ──[/bold cyan]")
        for name, text in items:
            console.print(f"  [green]{name}[/green]")
            # Wrap the prompt text at 70 chars, indented
            wrapped = text[:120] + ("..." if len(text) > 120 else "")
            console.print(f"    [dim]{wrapped}[/dim]")

    console.print(
        "\n[dim]Usage: llm-wiki query --template <name> [--save][/dim]"
    )


@cli.command()
@click.option("--deep", is_flag=True, help="LLM contradiction check across related pages (slow).")
@click.option("--fix", is_flag=True, help="Auto-fix stale embeddings by re-embedding all pages.")
def lint(deep: bool, fix: bool) -> None:
    """Check wiki health: orphans, broken cross-refs, stale embeddings."""
    from llm_wiki.lint import lint as _lint

    _lint(deep=deep, fix=fix)


@cli.command()
def status() -> None:
    """Show wiki overview: page count, sources, embedding health, recent activity."""
    import json as _json

    console.rule("[bold]Wiki Status")

    # ── Page count ────────────────────────────────────────────────────────────
    wiki_pages = [p for p in sorted(WIKI_DIR.glob("*.md")) if p.stem not in ("index", "log")]
    console.print(f"\n[bold cyan]Wiki pages:[/bold cyan] {len(wiki_pages)}")

    # ── Schema ────────────────────────────────────────────────────────────────
    if SCHEMA_PATH.exists():
        data = _json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        schema_count = len(data.get("pages", []))
        console.print(f"[bold cyan]Schema pages:[/bold cyan] {schema_count}")
        console.print(f"[bold cyan]Wiki name:[/bold cyan] {data.get('wiki_name', '—')}")
    else:
        console.print("[yellow]No schema.json — run `llm-wiki init` first.[/yellow]")

    # ── Sources ───────────────────────────────────────────────────────────────
    source_files = list(SOURCES_DIR.glob("*")) if SOURCES_DIR.exists() else []
    console.print(f"[bold cyan]Source files:[/bold cyan] {len(source_files)}")

    # ── Embeddings ────────────────────────────────────────────────────────────
    if EMBEDDINGS_PATH.exists():
        emb_data = _json.loads(EMBEDDINGS_PATH.read_text(encoding="utf-8"))
        emb_count = len(emb_data.get("pages", {}))
        console.print(f"[bold cyan]Embedded pages:[/bold cyan] {emb_count} "
                      f"(model: {emb_data.get('model', '?')})")
        stale = len(wiki_pages) - emb_count
        if stale > 0:
            console.print(f"[yellow]  ⚠ {stale} page(s) missing embeddings — run `llm-wiki lint --fix`[/yellow]")
    else:
        console.print("[yellow]No embeddings index — run `llm-wiki ingest` to build it.[/yellow]")

    # ── Page table ────────────────────────────────────────────────────────────
    if wiki_pages:
        console.print()
        table = Table(title="Wiki Pages", show_lines=False, header_style="bold")
        table.add_column("Slug", style="cyan")
        table.add_column("Title")
        table.add_column("Tags", style="dim")
        table.add_column("Updated", style="dim")

        import frontmatter as _fm
        for p in wiki_pages:
            try:
                post = _fm.load(str(p))
                table.add_row(
                    p.stem,
                    post.get("title", p.stem),
                    ", ".join(post.get("tags", [])),
                    str(post.get("updated", ""))[:10],
                )
            except Exception:
                table.add_row(p.stem, "—", "—", "—")
        console.print(table)

    # ── Recent log entries ────────────────────────────────────────────────────
    if LOG_PATH.exists():
        log_lines = LOG_PATH.read_text(encoding="utf-8").splitlines()
        recent = [ln for ln in log_lines if ln.startswith("## ")][-5:]
        if recent:
            console.print("\n[bold cyan]Recent activity (last 5):[/bold cyan]")
            for entry in recent:
                console.print(f"  [dim]{entry[3:]}[/dim]")
