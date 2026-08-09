"""All Claude prompt templates. No prompts live outside this module."""

MODEL = "claude-sonnet-4-6"

# ── Named query templates (sourced from Wiki_prompts.md) ─────────────────────
# These mirror the 6 categories of curated query patterns. Each template is
# injected as the user's question when `llm-wiki query --template <name>` is used.

QUERY_TEMPLATES: dict[str, tuple[str, str]] = {
    # Synthesis
    "master-summary": (
        "Synthesis",
        "Read everything in my wiki and give me the single most important insight — "
        "the idea that ties everything else together.",
    ),
    "consensus": (
        "Synthesis",
        "Based on all my sources, what do they collectively agree is the most important thing to know? "
        "Where is the consensus strongest?",
    ),
    "hierarchy": (
        "Synthesis",
        "Rank the concepts in my wiki by importance. What should someone understand first before "
        "they can understand everything else?",
    ),
    "unexpected-connection": (
        "Synthesis",
        "What's the most surprising or non-obvious connection between two ideas in my wiki "
        "that aren't already linked together?",
    ),
    "one-pager": (
        "Synthesis",
        "Summarise my entire wiki into a single 500-word article. "
        "Prioritise depth over breadth — I'd rather understand three things deeply than ten things shallowly.",
    ),
    # Gap-Finding
    "blind-spot": (
        "Gap-Finding",
        "What important topics or concepts are missing from my wiki entirely? "
        "What should I go and find more sources on?",
    ),
    "thin-coverage": (
        "Gap-Finding",
        "Which articles in my wiki have the weakest or thinnest coverage? "
        "Where am I relying on only one source when I should have several?",
    ),
    "unanswered-questions": (
        "Gap-Finding",
        "What questions does my wiki raise that it doesn't answer? List them in order of importance.",
    ),
    "next-sources": (
        "Gap-Finding",
        "Based on the gaps in my wiki, what are the five most valuable sources I should add next? "
        "Be specific — name actual books, papers, researchers, or articles if you can.",
    ),
    "assumption-check": (
        "Gap-Finding",
        "What assumptions are baked into my wiki that I've never questioned? "
        "What would change if one of those assumptions turned out to be wrong?",
    ),
    # Debate & Disagreement
    "main-debate": (
        "Debate",
        "What is the single biggest disagreement between my sources? "
        "Explain both sides as steelman arguments.",
    ),
    "nuance-finder": (
        "Debate",
        "Where do my sources appear to agree on the surface but actually disagree on the details? "
        "Find a case where the devil is in the details.",
    ),
    "outlier": (
        "Debate",
        "Is there any source in my wiki that contradicts the majority view? "
        "What's their argument and how strong is it?",
    ),
    "evolving-consensus": (
        "Debate",
        "Is there any topic in my wiki where the thinking has shifted over time — "
        "where older sources say something different from newer ones?",
    ),
    # Output
    "action-plan": (
        "Output",
        "Based on everything in my wiki, create a practical step-by-step plan I can start this week. "
        "Prioritise ruthlessly — what has the highest impact for the least effort?",
    ),
    "study-guide": (
        "Output",
        "Turn my wiki into a structured study guide. "
        "What should I learn in what order, and what are the key things to understand at each stage?",
    ),
    "cheat-sheet": (
        "Output",
        "Create a one-page reference sheet of the most important facts, frameworks, and principles "
        "from my wiki. Format it so I can scan it in under two minutes.",
    ),
    "faq": (
        "Output",
        "Write a FAQ based on my wiki — the 10 questions a smart beginner would ask, "
        "with clear concise answers drawn from my sources.",
    ),
    "slide-deck": (
        "Output",
        "Create a 10-slide presentation outline based on my wiki. "
        "Give each slide a title, a one-line summary, and the key supporting point from my sources.",
    ),
    # Wiki Health
    "consistency-check": (
        "Health",
        "Scan my wiki for contradictions or inconsistencies. "
        "Are there any articles that define the same concept differently, or make conflicting claims?",
    ),
    "orphan-finder": (
        "Health",
        "Which articles in my wiki have the fewest links to other articles? "
        "These are likely isolated — suggest where they should connect.",
    ),
    "duplication-check": (
        "Health",
        "Are there any articles in my wiki that cover the same ground and should be merged? "
        "Identify any overlaps.",
    ),
    "integrity-report": (
        "Health",
        "Give me an overall health report on my wiki. "
        "What's strong, what's weak, and what are the three most important things I should do to improve it?",
    ),
    # Personal Application
    "personal-diagnosis": (
        "Personal",
        "Based on everything in my wiki, what are the most likely mistakes I'm currently making — "
        "even if I don't know it yet? Be direct.",
    ),
}

# ── Ingest: routing ───────────────────────────────────────────────────────────

ROUTING_SYSTEM = """\
You are a knowledge router. Given a source document and a list of wiki pages,
identify which pages the document is relevant to.
Return ONLY a JSON array of page slugs. Example: ["transformers", "attention_mechanism"]
If no pages are relevant, return [].
"""


def routing_user(schema_summary: str, filename: str, source_text: str) -> str:
    return f"""\
## Wiki Pages (slug: title — description)
{schema_summary}

## Source Document: {filename}
{source_text[:20_000]}

Which wiki page slugs does this document have relevant content for?
Return a JSON array of slugs only. No explanation."""


# ── Ingest: synthesis ─────────────────────────────────────────────────────────

SYNTHESIS_SYSTEM = """\
You are a knowledge compiler maintaining a structured wiki.
Your output is ONLY the markdown body of the page (no YAML front matter, no code fences).
Write in encyclopedic, dense, cross-referential style.
Use ## headings for sections. Always include a ## See Also section at the end.
Cross-reference other wiki pages using [[slug]] notation.
Never invent facts. Synthesize only from the provided source material.
Preserve and extend existing content — never discard information already on the page.
"""


def synthesis_user(
    title: str,
    description: str,
    existing_body: str | None,
    filename: str,
    source_text: str,
    other_pages: list[str],
) -> str:
    existing = existing_body or "This page does not exist yet. Create it from scratch."
    others = "\n".join(other_pages) if other_pages else "None"
    return f"""\
## Wiki Page: {title}
Description: {description}

## Existing Page Content:
{existing}

## New Source Document: {filename}
{source_text[:12_000]}

## Other Wiki Pages (for [[cross-reference]] awareness):
{others}

Rewrite the complete page body, integrating the new source content.
Preserve all existing knowledge. Add or extend sections as needed.
Output markdown body only — no YAML front matter, no code fences."""


# ── Ingest: index update ──────────────────────────────────────────────────────

INDEX_SYSTEM = """\
You maintain a wiki index page. Output ONLY a markdown table.
The table must have exactly these columns: | Page | Slug | Summary | Tags | Updated |
One row per wiki page listed. Keep summaries under 15 words. Sort rows alphabetically by Page.
"""


def index_user(current_index: str, updated_pages: list[dict]) -> str:
    updates = "\n".join(
        f"- {p['slug']}: {p['title']} | {p['summary']} | tags: {p['tags']} | {p['updated']}"
        for p in updated_pages
    )
    return f"""\
## Current Index:
{current_index or "(empty)"}

## Updated Pages:
{updates}

Produce the complete updated index table including all pages (both existing and updated).
Output the markdown table only."""


# ── Query: answer synthesis ───────────────────────────────────────────────────

ANSWER_SYSTEM = """\
You are a knowledgeable assistant with access to a curated wiki knowledge base.
Answer the user's question using ONLY the provided wiki pages as your source.
Cite which wiki pages you drew from using [Page Title] notation.
If the wiki pages do not contain sufficient information, say so explicitly.
Be concise but complete.
"""


def answer_user(question: str, context: str) -> str:
    return f"""\
## Question
{question}

## Relevant Wiki Pages
{context}

Answer the question based on the wiki content above."""


# ── Lint: contradiction check ─────────────────────────────────────────────────

CONTRADICTION_SYSTEM = """\
You are a fact-checker reviewing two wiki pages for consistency.
List any factual contradictions between them, quoting the conflicting statements.
If there are no contradictions, respond with exactly: "No contradictions found."
"""


def contradiction_user(
    page1_title: str, page1_body: str, page2_title: str, page2_body: str
) -> str:
    return f"""\
## Page 1: {page1_title}
{page1_body[:4_000]}

## Page 2: {page2_title}
{page2_body[:4_000]}

List any factual contradictions between these two pages."""
