"""Lint pipeline: wiki health checks - orphans, broken refs, stale embeddings."""

from __future__ import annotations

import json
import re

import anthropic
from rich.console import Console
from rich.markup import escape

from llm_wiki import embeddings, prompts
from llm_wiki import wiki as wiki_mod
from llm_wiki.config import EMBEDDINGS_PATH, SOURCES_DIR, WIKI_DIR, WikiSchema
from llm_wiki.index import EmbeddingIndex

console = Console(legacy_windows=False)


def lint(deep: bool = False, fix: bool = False) -> None:
    schema = WikiSchema.load()
    pages = wiki_mod.all_pages()
    page_slugs = {p.slug for p in pages}
    schema_slugs = {s.slug for s in schema.pages}

    errors: list[str] = []
    warnings: list[str] = []
    infos: list[str] = []

    # ── Check 1: Orphan pages (in wiki/ but not in schema) ───────────────────
    for slug in page_slugs:
        if slug not in schema_slugs:
            warnings.append(f"[orphan] wiki/{slug}.md exists but is not in schema")

    # ── Check 2: Missing pages (in schema but no .md file) ───────────────────
    for spec in schema.pages:
        if spec.slug not in page_slugs:
            warnings.append(
                f"[missing-page] '{spec.slug}' defined in schema but wiki/{spec.slug}.md not found"
            )

    # ── Check 3: Broken cross-references ([[slug]] links) ────────────────────
    for page in pages:
        refs = re.findall(r"\[\[(\w+)\]\]", page.body)
        for ref in refs:
            if not (WIKI_DIR / f"{ref}.md").exists():
                errors.append(
                    f"[broken-xref] wiki/{page.slug}.md -> [[{ref}]] (does not exist)"
                )

    # ── Check 4: Stale embeddings ─────────────────────────────────────────────
    if EMBEDDINGS_PATH.exists():
        emb_data = json.loads(EMBEDDINGS_PATH.read_text(encoding="utf-8"))
        emb_pages = emb_data.get("pages", {})
        for page in pages:
            if page.slug not in emb_pages:
                warnings.append(
                    f"[stale-embedding] wiki/{page.slug}.md has no embedding entry"
                )

    # ── Check 5: Missing source files ────────────────────────────────────────
    for page in pages:
        for src in page.sources:
            if not (SOURCES_DIR / src).exists():
                infos.append(
                    f"[missing-source] wiki/{page.slug}.md references '{src}' "
                    f"not found in sources/"
                )

    # ── Check 6: Contradiction check (--deep, LLM) ───────────────────────────
    if deep:
        _contradiction_check(pages)

    # ── Auto-fix: re-embed stale pages ────────────────────────────────────────
    if fix:
        _fix_stale_embeddings(pages)

    # ── Report ────────────────────────────────────────────────────────────────
    _print_report(errors, warnings, infos, len(pages))


def _print_report(
    errors: list[str], warnings: list[str], infos: list[str], page_count: int
) -> None:
    console.rule("[bold]Lint Report")
    if errors:
        console.print(f"\n[bold red]ERRORS ({len(errors)}):[/bold red]")
        for e in errors:
            console.print(f"  {escape(e)}")
    if warnings:
        console.print(f"\n[bold yellow]WARNINGS ({len(warnings)}):[/bold yellow]")
        for w in warnings:
            console.print(f"  {escape(w)}")
    if infos:
        console.print(f"\n[dim]INFO ({len(infos)}):[/dim]")
        for i in infos:
            console.print(f"  {escape(i)}")
    if not errors and not warnings and not infos:
        console.print("\n[bold green]All checks passed.[/bold green]")
    console.print(f"\n[green]Total pages checked: {page_count}[/green]")


def _contradiction_check(pages: list) -> None:
    """Ask Claude to check tag-overlapping page pairs for factual contradictions."""
    client = anthropic.Anthropic()
    checked: set[frozenset] = set()
    console.print("\n[bold]Running contradiction check (deep)...[/bold]")

    for i, p1 in enumerate(pages):
        for p2 in pages[i + 1:]:
            pair = frozenset([p1.slug, p2.slug])
            if pair in checked:
                continue
            if set(p1.tags) & set(p2.tags):  # only check pages sharing tags
                checked.add(pair)
                resp = client.messages.create(
                    model=prompts.MODEL,
                    max_tokens=512,
                    system=[{
                        "type": "text",
                        "text": prompts.CONTRADICTION_SYSTEM,
                        "cache_control": {"type": "ephemeral"},
                    }],
                    messages=[{
                        "role": "user",
                        "content": prompts.contradiction_user(
                            p1.title, p1.body, p2.title, p2.body
                        ),
                    }],
                )
                result = resp.content[0].text.strip()
                if "no contradictions found" not in result.lower():
                    console.print(
                        f"\n[red]Contradiction ({p1.slug} <-> {p2.slug}):[/red]\n{escape(result)}"
                    )


def _fix_stale_embeddings(pages: list) -> None:
    console.print("\n[bold]Re-embedding all pages...[/bold]")
    emb_index = EmbeddingIndex.load()
    for page in pages:
        vec = embeddings.embed(page.full_text)
        emb_index.upsert(page.slug, page.title, vec)
        console.print(f"  [green]OK[/green] Re-embedded {page.slug}")
    emb_index.save()
    console.print("[green]All embeddings updated.[/green]")
