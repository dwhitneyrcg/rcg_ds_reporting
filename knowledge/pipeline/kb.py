"""
kb.py - Knowledge base pipeline (mechanical parts only).

The *reasoning* (classification, summarization, novelty detection, writing
proposed entity files) is done by a Claude Code agent following EXTRACT.md.
This script owns only the deterministic, no-judgment steps:

  parse    docx weekly report  ->  plain markdown   (reporting/raw -> reporting/parsed)
  validate staged proposals     ->  pass/fail        (YAML + wikilink integrity)
  accept   staged proposals     ->  live wiki        (the human-in-the-loop gate)

Usage:
  python kb.py parse   [INPUT_DIR] [--out reporting/parsed]
  python kb.py validate CYCLE
  python kb.py accept   CYCLE [--dry-run] [--only RELPATH]

CYCLE is a folder name under _staging/ (e.g. 2026-04-24).
Zero third-party deps beyond python-docx + pyyaml (already installed).
"""
import argparse
import os
import re
import shutil
import sys

import yaml
from docx import Document

# ---- layout -----------------------------------------------------------------
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # knowledge/
ENTITY_DIRS = ("people", "projects", "programs")
RAW = os.path.join(ROOT, "reporting", "raw")
PARSED = os.path.join(ROOT, "reporting", "parsed")
STAGING = os.path.join(ROOT, "_staging")
CHANGELOGS = os.path.join(ROOT, "reporting", "changelogs")
REQUIRED_FIELDS = ("type", "name", "status")  # every entity overview must have these

# target excludes backslash so a table-escaped alias pipe (`\|`, required inside
# markdown tables) is parsed as the alias separator, not part of the target path.
WIKILINK = re.compile(r"\[\[([^\]|#\\]+)(?:#[^\]|]+)?(?:\\?\|[^\]]+)?\]\]")


# ---- docx -> markdown (mechanical, no classification) -----------------------
def _run_md(run):
    t = run.text
    if not t:
        return ""
    if run.bold and run.italic:
        t = f"***{t}***"
    elif run.bold:
        t = f"**{t}**"
    elif run.italic:
        t = f"*{t}*"
    return t


def _para_md(para):
    text = "".join(_run_md(r) for r in para.runs).strip()
    if not text:
        return ""
    style = para.style.name if para.style else ""
    if style.startswith("Heading"):
        try:
            return "#" * int(style.split()[-1]) + " " + text
        except ValueError:
            pass
    if "list" in style.lower():
        return "- " + text
    return text


def docx_to_md(path):
    """Convert one .docx to markdown text. Paragraph-order, formatting-preserving."""
    doc = Document(path)
    parts = [_para_md(p) for p in doc.paragraphs]
    out = "\n\n".join(p for p in parts if p)
    return re.sub(r"\n{3,}", "\n\n", out).strip() + "\n"


def cmd_parse(args):
    src = args.input_dir or RAW
    out = args.out or PARSED
    os.makedirs(out, exist_ok=True)
    files = sorted(f for f in os.listdir(src)
                   if f.lower().endswith(".docx") and not f.startswith("~$"))
    if not files:
        print(f"No .docx in {src}")
        return 0
    for f in files:
        md = docx_to_md(os.path.join(src, f))
        dst = os.path.join(out, os.path.splitext(f)[0] + ".md")
        with open(dst, "w", encoding="utf-8") as fp:
            fp.write(md)
        print(f"  {f} -> {os.path.relpath(dst, ROOT)} ({len(md):,} chars)")
    print(f"Parsed {len(files)} file(s) into {os.path.relpath(out, ROOT)}")
    return 0


# ---- validation (the gate's safety check) -----------------------------------
def _split_frontmatter(text):
    """Return (frontmatter_dict_or_None, error_or_None)."""
    if not text.startswith("---"):
        return None, "no YAML frontmatter"
    end = text.find("\n---", 3)
    if end == -1:
        return None, "unterminated frontmatter"
    try:
        fm = yaml.safe_load(text[3:end])
    except yaml.YAMLError as e:
        return None, f"invalid YAML: {e}"
    if not isinstance(fm, dict):
        return None, "frontmatter is not a mapping"
    return fm, None


def _entity_files(base):
    for dirpath, _, names in os.walk(base):
        for n in names:
            if n.endswith(".md") and n != "NOVELTY_REPORT.md":
                yield os.path.join(dirpath, n)


def validate(cycle):
    """Check every staged .md: valid frontmatter, required fields, resolvable links.

    Returns list of (relpath, message) errors. Empty list == pass.
    A wikilink resolves if its target exists in the live wiki OR among the
    staged files (so a new person + the project that references them both land
    together in one cycle).
    """
    proposed = os.path.join(STAGING, cycle, "proposed")
    if not os.path.isdir(proposed):
        return [(cycle, f"no staged proposals at {os.path.relpath(proposed, ROOT)}")]

    staged_rel = {os.path.relpath(p, proposed).replace("\\", "/")
                  for p in _entity_files(proposed)}
    errors = []
    for path in _entity_files(proposed):
        rel = os.path.relpath(path, proposed).replace("\\", "/")
        text = open(path, encoding="utf-8").read()
        fm, err = _split_frontmatter(text)
        is_entity = rel.split("/", 1)[0] in ENTITY_DIRS
        # Entities must have valid frontmatter + required fields. Indexes and
        # other non-entity docs need none — but everyone's wikilinks are checked.
        if is_entity:
            if err:
                errors.append((rel, err))
            else:
                for field in REQUIRED_FIELDS:
                    if not fm.get(field):
                        errors.append((rel, f"missing required field '{field}'"))
        for m in WIKILINK.finditer(text):
            target = m.group(1).strip()
            if not target.endswith(".md"):
                target += ".md"
            in_wiki = os.path.isfile(os.path.join(ROOT, target))
            in_stage = target in staged_rel
            if not (in_wiki or in_stage):
                errors.append((rel, f"orphan wikilink -> {target}"))
    return errors


def cmd_validate(args):
    errors = validate(args.cycle)
    if errors:
        print(f"FAIL ({len(errors)} issue(s)):")
        for rel, msg in errors:
            print(f"  {rel}: {msg}")
        return 1
    print(f"PASS: staged proposals for {args.cycle} are valid")
    return 0


# ---- accept (promote staging -> live wiki) ----------------------------------
def cmd_accept(args):
    cycle = args.cycle
    errors = validate(cycle)
    if errors:
        print(f"Refusing to accept: {len(errors)} validation issue(s). Run "
              f"`kb.py validate {cycle}` for details.")
        return 1

    proposed = os.path.join(STAGING, cycle, "proposed")
    files = sorted(_entity_files(proposed))
    if args.only:
        only = args.only.replace("\\", "/")
        files = [f for f in files
                 if os.path.relpath(f, proposed).replace("\\", "/") == only]
        if not files:
            print(f"--only {args.only} matched no staged file")
            return 1

    if args.dry_run:
        print(f"DRY RUN - {len(files)} file(s) would be promoted:")
        for f in files:
            print(f"  {os.path.relpath(f, proposed)}")
        return 0

    promoted = []
    for f in files:
        rel = os.path.relpath(f, proposed)
        dst = os.path.join(ROOT, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(f, dst)
        promoted.append(rel.replace("\\", "/"))

    os.makedirs(CHANGELOGS, exist_ok=True)
    log = os.path.join(CHANGELOGS, f"{cycle}.md")
    with open(log, "a", encoding="utf-8") as fp:
        fp.write(f"# Accepted cycle {cycle}\n\n")
        for rel in promoted:
            fp.write(f"- {rel}\n")
        fp.write("\n")
    print(f"Promoted {len(promoted)} file(s) into the wiki. Changelog: "
          f"{os.path.relpath(log, ROOT)}")
    return 0


# ---- seed (spreadsheet -> staged baseline) ----------------------------------
# A structured roster spreadsheet is the authoritative source for *who/what
# exists* (people, projects, programs); weekly reports layer *progress* on top.
# `seed` is a deterministic front-end (no LLM) that emits staged proposals, then
# reuses the same validate -> accept gate as a weekly cycle.
#
# ponytail: seed overwrites an existing entity file wholesale, so accepting a
# seed discards that entity's Progress Log / Weekly Progress history. Fine for
# the initial bootstrap (proof history is regenerable by re-running extract).
# Before re-seeding a wiki with real accumulated history, add a merge that
# preserves those tables for slugs that already exist.
SEED_TABS = {
    "people": ["name", "aliases", "role", "leader", "status", "programs", "projects", "tag"],
    "programs": ["program", "aliases", "status", "goal", "type", "tag"],
    "projects": ["project", "aliases", "program", "status", "summary", "tag"],
}
# `tag` is the canonical key (lowercase, spaces->_, project = <program_tag>/<project>).
# People reference programs/projects by their tag. `programs.type` is a business
# category (e.g. performance, personalization). Tag is derived if left blank.


def _slug(name):
    return re.sub(r"[^a-z0-9]+", "_", str(name).strip().lower()).strip("_")


def _split(cell):
    """Split a `;`/`,`-separated cell. Drops punctuation-only tokens like '—' or
    '-' that people use to mean "none" (a real value always has alphanumerics)."""
    if cell is None:
        return []
    return [p.strip() for p in str(cell).replace(",", ";").split(";")
            if p.strip() and any(c.isalnum() for c in p)]


def _alias_fm(cell):
    """`aliases: [...]` frontmatter line (empty string if none)."""
    al = _split(cell)
    return ("aliases: [" + ", ".join(f'"{a}"' for a in al) + "]\n") if al else ""


def _alias_aka(cell):
    """`  (aka: a, b)` index suffix so the index doubles as an alias lookup."""
    al = _split(cell)
    return f"  (aka: {', '.join(al)})" if al else ""


def tagcol(r):
    """The canonical Tag from a spreadsheet row (empty string if blank)."""
    return str(r.get("tag") or "").strip()


def _clear_dir(path):
    """Remove a directory tree, tolerating Windows read-only bits. Returns True
    if the tree is gone afterward. Does NOT swallow a persistent failure — the
    caller must check, so we never stage onto stale files (e.g. renamed tags)."""
    import stat
    if not os.path.isdir(path):
        return True

    def _onexc(func, p, _exc):
        try:
            os.chmod(p, stat.S_IWRITE)
            func(p)
        except OSError:
            pass

    try:  # onexc (py3.12+) vs onerror (older)
        shutil.rmtree(path, onexc=_onexc)
    except TypeError:
        shutil.rmtree(path, onerror=lambda f, p, e: _onexc(f, p, e))
    except OSError:
        pass
    return not os.path.isdir(path)


def _read_tab(wb, name, cols):
    if name not in wb.sheetnames:
        return None, f"missing tab '{name}'"
    rows = list(wb[name].iter_rows(values_only=True))
    if not rows:
        return [], None
    header = [str(h).strip().lower() if h is not None else "" for h in rows[0]]
    out = []
    for r in rows[1:]:
        if r is None or all(c is None or str(c).strip() == "" for c in r):
            continue
        rec = {header[i]: (r[i] if i < len(r) else None) for i in range(len(header))}
        first = str(rec.get(cols[0], "") or "").lower()
        if first.startswith("e.g.") or first.startswith("example"):  # skip template row
            continue
        out.append(rec)
    return out, None


def write_template(path):
    import openpyxl
    examples = {
        "people": ["Jane Doe", "Janie; JD", "Sr. Data Scientist", "Matt Denesuk", "Active",
                   "revenue_management_automation",
                   "revenue_management_automation/track_optimization", "jane_doe"],
        "programs": ["Revenue Management Automation", "RMA; Rev Mgmt", "Active",
                     "Automated revenue management across brands.", "performance",
                     "revenue_management_automation"],
        "projects": ["Track Optimization", "Track Opt; TO", "Revenue Management Automation",
                     "In Development", "Pricing track optimization and basket frameworks.",
                     "revenue_management_automation/track_optimization"],
    }
    wb = openpyxl.Workbook()
    first = True
    for tab, cols in SEED_TABS.items():
        ws = wb.active if first else wb.create_sheet()
        ws.title = tab
        first = False
        ws.append(cols)
        ws.append(["e.g. " + examples[tab][0]] + examples[tab][1:])
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    wb.save(path)


def cmd_seed(args):
    import openpyxl
    if args.template:
        write_template(args.template)
        print(f"Wrote blank template: {args.template}")
        return 0
    if not args.file:
        print("Provide a spreadsheet path, or --template PATH to generate one.")
        return 1

    # Read a copy, so a sheet that's open in Excel (or mid-OneDrive-sync) still works.
    import tempfile
    tmpx = os.path.join(tempfile.gettempdir(), "_kb_seed_read.xlsx")
    try:
        shutil.copy2(args.file, tmpx)
        wb = openpyxl.load_workbook(tmpx, read_only=True, data_only=True)
    except (PermissionError, OSError) as e:
        print(f"FAIL: cannot read {os.path.basename(args.file)} "
              f"({e.__class__.__name__}). Close it in Excel / wait for OneDrive "
              f"sync to finish, then retry.")
        return 1
    data = {}
    for tab, cols in SEED_TABS.items():
        recs, err = _read_tab(wb, tab, cols)
        if err:
            wb.close()
            print(f"FAIL: {err}")
            return 1
        data[tab] = recs
    wb.close()  # read_only workbooks hold the file open until closed (Windows)
    try:
        os.remove(tmpx)
    except OSError:
        pass

    def _norm(s):
        # Tag charset = [a-z0-9_-]. Lowercase; '&' -> 'and' (invalid in Obsidian
        # #hashtags); everything else non-alnum -> '_'. Keeps '-'. No whitespace,
        # no '&' — so a tag is safe as a path, a wikilink target, AND a #hashtag.
        s = str(s).strip().lower().replace("&", " and ")
        return re.sub(r"[^a-z0-9-]+", "_", s).strip("_")

    # Canonical program tag + a resolver keyed by tag, name, and every alias, so
    # references resolve by any of them. The Tag column is honored but normalized,
    # so a stray '/' in a name ("PCP/OBR") cannot break the composite separator.
    renamed = []   # tags normalization changed from what was typed (transparency)
    prog_name, prog_by_key = {}, {}
    for r in data["programs"]:
        if not r.get("program"):
            continue
        name = str(r["program"]).strip()
        ct = _norm(tagcol(r) or name)
        r["_tag"] = ct          # per-row tag (never look up by name — names repeat)
        prog_name[ct] = name
        if tagcol(r) and tagcol(r) != ct:
            renamed.append(f"program '{name}': tag '{tagcol(r)}' -> '{ct}'")
        for k in {ct, _norm(name)} | {_norm(a) for a in _split(r.get("aliases"))}:
            prog_by_key[k] = ct

    # project tag = <program_tag>/<project_slug>; the program comes from the
    # program column (robust to '/' inside the project name, e.g. "A/B Testing").
    errs = []
    proj_name, proj_by_key = {}, {}
    for r in data["projects"]:
        if not r.get("project"):
            continue
        name = str(r["project"]).strip()
        ptag = prog_by_key.get(_norm(str(r.get("program") or "")))
        if not ptag:
            errs.append(f"project '{name}': program '{r.get('program')}' is not a known program")
            continue
        ct = f"{ptag}/{_norm(name)}"
        r["_tag"] = ct          # per-row: the SAME project name in two programs
        proj_name[ct] = name    # gets two distinct tags — must not key by name
        if tagcol(r) and tagcol(r) != ct:
            renamed.append(f"project '{name}': tag '{tagcol(r)}' -> '{ct}'")
        for k in {ct, _norm(name)} | {_norm(a) for a in _split(r.get("aliases"))}:
            proj_by_key[k] = ct
    if errs:  # structural: a project with no resolvable program can't be placed
        print(f"FAIL: {len(errs)} project(s) reference an unknown program:")
        for e in errs:
            print(f"  {e}")
        return 1

    # Resolve each person's program/project refs through the alias/name maps.
    # 'all_programs' is a cross-cutting sentinel (skipped). Unresolved refs become
    # warnings (the link is dropped) rather than blocking the whole seed.
    unresolved = []

    def _resolve(r, col, by_key):
        out = []
        for ref in _split(r.get(col)):
            if _norm(ref) == "all_programs":
                continue
            ct = by_key.get(_norm(ref))
            if ct:
                out.append(ct)
            else:
                unresolved.append(f"person '{r.get('name')}' -> {col[:-1]} '{ref}'")
        return out

    for r in data["people"]:
        r["_progs"] = _resolve(r, "programs", prog_by_key)
        r["_projs"] = _resolve(r, "projects", proj_by_key)

    # alias hygiene: an alias mapping to two entities of a type defeats mapping.
    warnings = []
    for tab, keycol in (("people", "name"), ("programs", "program"), ("projects", "project")):
        canon = {str(r.get(keycol)).strip().lower() for r in data[tab] if r.get(keycol)}
        seen = {}
        for r in data[tab]:
            for a in _split(r.get("aliases")):
                k = a.lower()
                if k in seen:
                    warnings.append(f"{tab}: alias '{a}' used by both '{seen[k]}' and '{r.get(keycol)}'")
                elif k in canon:
                    warnings.append(f"{tab}: alias '{a}' collides with a canonical name")
                else:
                    seen[k] = str(r.get(keycol)).strip()

    cycle = args.cycle
    proposed = os.path.join(STAGING, cycle, "proposed")
    # start clean: else a re-seed whose tags changed (e.g. '&'->'and') leaves the
    # old-path files behind as stale duplicates that accept would also promote.
    if not _clear_dir(proposed):
        print(f"FAIL: could not clear {os.path.relpath(proposed, ROOT)} — is it open "
              f"in Excel/Explorer or mid-OneDrive-sync? Remove it and retry.")
        return 1

    def ptag_of(r):
        return _norm(tagcol(r) or r["name"])

    ppl_by_proj = {}   # project tag -> [person rows]
    for r in data["people"]:
        for pj in r["_projs"]:
            ppl_by_proj.setdefault(pj, []).append(r)

    written, collisions = {}, []

    def w(rel, text):
        if rel in written and written[rel] != text:
            collisions.append(rel)   # two entities produced the same tag/path
        written[rel] = text
        dst = os.path.join(proposed, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "w", encoding="utf-8") as f:
            f.write(text)

    def plink(t):  # project wikilink from its (composite) tag
        return f"[[projects/{t}/overview_{t.rsplit('/', 1)[-1]}|{proj_name.get(t, t)}]]"

    def glink(t):  # program wikilink from its tag
        return f"[[programs/{t}/overview_{t}|{prog_name.get(t, t)}]]"

    prog_index, proj_index, ppl_index = ["# Programs"], ["# Projects"], ["# People"]

    for r in data["programs"]:
        if not r.get("_tag"):
            continue
        name = str(r["program"]).strip()
        tag = r["_tag"]
        cat = f"category: {r.get('type')}\n" if r.get("type") else ""
        plist = "\n".join(
            f"- {plink(p['_tag'])}"
            for p in data["projects"]
            if p.get("_tag") and p["_tag"].rsplit("/", 1)[0] == tag
        ) or "_None yet._"
        w(f"programs/{tag}/overview_{tag}.md",
          f'---\ntype: program\nname: "{name}"\ntag: {tag}\n{_alias_fm(r.get("aliases"))}'
          f'{cat}status: {r.get("status") or "Active"}\n'
          f"tags: [program]\n---\n\n# {name}\n\n## Goal\n{r.get('goal') or '_TBD._'}\n\n"
          f"## Projects\n{plist}\n\n## Current Status\nSeeded {cycle}.\n")
        prog_index.append(f"- {glink(tag)}{_alias_aka(r.get('aliases'))}")

    for r in data["projects"]:
        if not r.get("_tag"):
            continue
        name = str(r["project"]).strip()
        tag = r["_tag"]
        leaf = tag.rsplit("/", 1)[-1]
        ptag = tag.rsplit("/", 1)[0]
        people = "\n".join(
            f"- [[people/{ptag_of(pr)}/overview_{ptag_of(pr)}|{str(pr['name']).strip()}]]"
            for pr in ppl_by_proj.get(tag, [])) or "_None yet._"
        w(f"projects/{tag}/overview_{leaf}.md",
          f'---\ntype: project\nname: "{name}"\ntag: {tag}\n{_alias_fm(r.get("aliases"))}'
          f'status: {r.get("status") or "Planned"}\nprogram: "{glink(ptag)}"\n'
          f"tags: [project]\n---\n\n# {name}\n\n## Summary\n"
          f"{r.get('summary') or '_TBD._'}\n\n## People\n{people}\n\n## Progress Log\n"
          f"| Date | Update | Status |\n|------|--------|--------|\n| | | |\n")
        proj_index.append(f"- {plink(tag)} — {glink(ptag)}{_alias_aka(r.get('aliases'))}")

    for r in data["people"]:
        name = str(r["name"]).strip()
        tag = ptag_of(r)
        proglinks = "\n".join(f"- {glink(pg)}" for pg in r["_progs"]) or "_None yet._"
        projlinks = "\n".join(f"- {plink(pj)}" for pj in r["_projs"]) or "_None yet._"
        leader = f"\n## Leader\n{r.get('leader')}\n" if r.get("leader") else ""
        w(f"people/{tag}/overview_{tag}.md",
          f'---\ntype: person\nname: "{name}"\ntag: {tag}\n{_alias_fm(r.get("aliases"))}'
          f'status: {r.get("status") or "Active"}\n'
          f"tags: [person]\n---\n\n# {name}\n\n## Role\n{r.get('role') or '_TBD._'}\n"
          f"{leader}\n## Programs\n{proglinks}\n\n## Active Projects\n{projlinks}\n\n"
          f"## Weekly Progress\n| Date | Project | Activity |\n|------|---------|----------|\n| | | |\n")
        ppl_index.append(f"- [[people/{tag}/overview_{tag}|{name}]]{_alias_aka(r.get('aliases'))}")

    w("indexes/programs.md", "\n".join(prog_index) + "\n")
    w("indexes/projects.md", "\n".join(proj_index) + "\n")
    w("indexes/people.md", "\n".join(ppl_index) + "\n")

    # novelty report: NEW vs already-in-wiki (by tag), and wiki tags absent from sheet
    def existing_tags(kind):
        base = os.path.join(ROOT, kind)
        if not os.path.isdir(base):
            return set()
        if kind == "projects":  # nested: programs/<prog>/<proj>
            out = set()
            for pg in os.listdir(base):
                pd = os.path.join(base, pg)
                if os.path.isdir(pd):
                    out |= {f"{pg}/{pj}" for pj in os.listdir(pd)
                            if os.path.isdir(os.path.join(pd, pj))}
            return out
        return {n for n in os.listdir(base) if os.path.isdir(os.path.join(base, n))}

    sheet = {"programs": [(str(r["program"]).strip(), r["_tag"])
                          for r in data["programs"] if r.get("_tag")],
             "projects": [(str(r["project"]).strip(), r["_tag"])
                          for r in data["projects"] if r.get("_tag")],
             "people": [(str(r["name"]).strip(), ptag_of(r))
                        for r in data["people"] if r.get("name")]}
    lines = [f"# Novelty Report — {cycle} (spreadsheet seed)", "",
             f"**Source:** {os.path.basename(args.file)}",
             f"**Proposed:** {len(data['programs'])} programs, {len(data['projects'])} projects, "
             f"{len(data['people'])} people + 3 indexes", "",
             "Seed is the canonical baseline. **EXISTING entities are overwritten on accept** "
             "(progress-log history replaced — re-run the weekly extract afterward to re-attach).", ""]
    for kind in ("programs", "projects", "people"):
        ex = existing_tags(kind)
        sheet_tags = {t for _, t in sheet[kind]}
        new = [n for n, t in sheet[kind] if t not in ex]
        upd = [n for n, t in sheet[kind] if t in ex]
        retire = sorted(ex - sheet_tags)
        lines += [f"## {kind.title()}",
                  f"- **NEW** ({len(new)}): {', '.join(new) or 'none'}",
                  f"- **EXISTING / will overwrite** ({len(upd)}): {', '.join(upd) or 'none'}",
                  f"- **In wiki but NOT in sheet** ({len(retire)}): {', '.join(retire) or 'none'}",
                  ""]
    if collisions:
        lines += ["## Tag collisions (two rows share a tag — only the last was kept!)",
                  "Fix these in the sheet (distinct names/tags) or entities are lost:"]
        lines += [f"- {c}" for c in collisions] + [""]
    if unresolved:
        lines += ["## Unresolved references (link dropped — fix in the sheet & re-seed)",
                  "These person refs matched no tag/name/alias, so the link was omitted:"]
        lines += [f"- {u}" for u in unresolved] + [""]
    if renamed:
        lines += ["## Tags normalized (stray characters adjusted from what you typed)"]
        lines += [f"- {rn}" for rn in renamed] + [""]
    if warnings:
        lines += ["## Alias warnings (ambiguous — may misroute name-mapping)"]
        lines += [f"- {wn}" for wn in warnings] + [""]
    os.makedirs(os.path.join(STAGING, cycle), exist_ok=True)
    with open(os.path.join(STAGING, cycle, "NOVELTY_REPORT.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    for label, items in (("TAG COLLISION(S) — entities lost!", collisions),
                         ("tag(s) normalized", renamed),
                         ("unresolved person ref(s)", unresolved),
                         ("ambiguous alias(es)", warnings)):
        if items:
            print(f"  note: {len(items)} {label}")
    print(f"Staged {len(written)} file(s) into _staging/{cycle}/. Review "
          f"NOVELTY_REPORT.md, then `kb.py validate {cycle}` and `kb.py accept {cycle}`.")
    return 0


# ---- extract (split=Python lossless · tag=agent · render=Python lossless) ---
# The extraction of a weekly report is split so neither tool can do the other's
# damage:
#   split  (Python)  parsed report -> numbered verbatim line-blocks (no judgment)
#   tag    (agent)   returns {block_id: {role, person, program, project, note}}
#                    choosing ONLY from the canonical vocab — it emits tags, never
#                    text, so it cannot summarize or drop content
#   render (Python)  re-attaches tags to the VERBATIM blocks; enforces (1) every
#                    tag exists in the wiki and (2) output word-count >= source
#                    (lossless guard). A wrong-but-existing tag is caught by the
#                    separate verify pass (semantic fit), not here.

def _extract_blocks(path):
    """Non-blank lines of a parsed report, in order. id == index+1. Lossless:
    the block texts are the report's content verbatim (only blank lines drop)."""
    out = []
    for line in open(path, encoding="utf-8").read().split("\n"):
        if line.strip():
            out.append(line.rstrip())
    return out


def _wiki_tagsets():
    people = {d for d in os.listdir(os.path.join(ROOT, "people"))
              if os.path.isdir(os.path.join(ROOT, "people", d))}
    programs = {d for d in os.listdir(os.path.join(ROOT, "programs"))
                if os.path.isdir(os.path.join(ROOT, "programs", d))}
    projects = set()
    base = os.path.join(ROOT, "projects")
    for pg in os.listdir(base):
        if os.path.isdir(os.path.join(base, pg)):
            projects |= {f"{pg}/{pj}" for pj in os.listdir(os.path.join(base, pg))
                         if os.path.isdir(os.path.join(base, pg, pj))}
    return people, programs, projects


def _pretty(tag):
    return tag.rsplit("/", 1)[-1].replace("_", " ").replace("-", " ").title()


def cmd_extract(args):
    blocks = _extract_blocks(args.report)
    date = re.search(r"(\d{8})", os.path.basename(args.report))
    date = f"{date.group(1)[:4]}-{date.group(1)[4:6]}-{date.group(1)[6:8]}" if date else "unknown"

    if args.mode == "split":
        payload = {"report": os.path.basename(args.report), "date": date,
                   "blocks": [{"id": i + 1, "text": t} for i, t in enumerate(blocks)]}
        out = args.out or os.path.join(STAGING, "_extract", f"{date}.{args.source}.blocks.json")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        import json
        with open(out, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=0)
        words = sum(len(t.split()) for t in blocks)
        print(f"split: {len(blocks)} blocks, {words} content words -> "
              f"{os.path.relpath(out, ROOT)}")
        return 0

    # render mode: needs a tag map {block_id: {role, person?, program?, project?, note?}}
    import json
    tagmap = json.load(open(args.tags, encoding="utf-8"))
    tagmap = {int(k): v for k, v in (tagmap.get("tags", tagmap)).items()}
    people, programs, projects = _wiki_tagsets()

    # (1) tag-existence check — Python's deterministic guarantee
    errors = []
    for bid, t in tagmap.items():
        for kind, key, valid in (("person", "person", people),
                                  ("program", "program", programs),
                                  ("project", "project", projects)):
            v = t.get(key)
            if v and v not in valid:
                errors.append(f"block {bid}: {kind} tag '{v}' does not exist in the wiki")
    if errors:
        print(f"FAIL: {len(errors)} tag(s) reference entities that don't exist:")
        for e in errors[:30]:
            print(f"  {e}")
        return 1

    # render: verbatim blocks + tags, inheriting person/program down the section
    lines, cur_person, cur_prog, unmapped = [], None, None, []
    people_seen, prog_seen, proj_seen = [], set(), set()
    for i, text in enumerate(blocks):
        t = tagmap.get(i + 1, {})
        role = t.get("role", "item")
        if role == "person":
            cur_person = t.get("person")
            if cur_person:
                people_seen.append(cur_person)
                lines.append(f"\n## [[people/{cur_person}/overview_{cur_person}|{text.replace('*','').strip()}]]")
            else:
                lines.append(f"\n## (unmapped person: {text.replace('*','').strip()})")
            cur_prog = None
            continue
        if role == "program":
            cur_prog = t.get("program")
            if cur_prog:
                prog_seen.add(cur_prog)
                lines.append(f"**Program:** [[programs/{cur_prog}/overview_{cur_prog}|{_pretty(cur_prog)}]]  ·  _{text.replace('*','').strip()}_")
            else:
                lines.append(f"**Program:** _(unmapped: {text.replace('*','').strip()})_")
            continue
        if role == "skip":
            lines.append(text)
            continue
        # item: verbatim text + its project tag (or unmapped note)
        proj = t.get("project")
        if proj:
            proj_seen.add(proj)
            lines.append(f"{text}  ·  [[projects/{proj}/overview_{proj.rsplit('/',1)[-1]}|{_pretty(proj)}]]")
        elif t.get("note"):
            unmapped.append(t["note"])
            lines.append(f"{text}  ·  _(unmapped: {t['note']})_")
        else:
            lines.append(text)

    body = "\n".join(lines)
    # (2) lossless guard — content words must not shrink
    src_words = sum(len(t.split()) for t in blocks)
    out_words = len(body.split())
    if out_words < src_words:
        print(f"FAIL lossless guard: output {out_words} words < source {src_words} "
              f"— tagging dropped content, refusing to write.")
        return 1

    fm = ["---", "type: extracted_report", f"source: {args.source}", f"date: {date}",
          "people: [" + ", ".join(dict.fromkeys(people_seen)) + "]",
          "programs: [" + ", ".join(sorted(prog_seen)) + "]",
          "projects: [" + ", ".join(sorted(proj_seen)) + "]",
          "unmapped: [" + ", ".join(dict.fromkeys(unmapped)) + "]", "---", "",
          f"# Extracted Report ({args.source}) — {date}",
          "_Original content verbatim; entity tags layered in. "
          f"Lossless: {out_words} words >= {src_words} source._", ""]
    out = args.out or os.path.join(ROOT, "reporting", "extracted", args.source, f"{date}.md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(fm) + body + "\n")
    print(f"render: {len(people_seen)} people, {len(proj_seen)} projects, "
          f"{len(unmapped)} unmapped, lossless {out_words}>={src_words} -> "
          f"{os.path.relpath(out, ROOT)}")
    return 0


def _taglist(entry, singular, plural):
    """Read a tag field that may be a single value or a list -> list."""
    v = entry.get(plural)
    if isinstance(v, list):
        return [x for x in v if x]
    v = v or entry.get(singular)
    return [v] if v else []


def cmd_pivot(args):
    """PASS-2 input: reorganize tagged blocks BY project and BY person.

    Deterministic fan-out — a block tagged with N projects lands in all N project
    buckets; a block under M people lands in all M person buckets. No judgment
    here (that was pass 1); Python just regroups the structured tags. Person is
    resolved by inheriting the current person-header down its section.
    """
    import json
    from collections import defaultdict
    blocks = _extract_blocks(args.report)
    tagmap = json.load(open(args.tags, encoding="utf-8"))
    tagmap = {int(k): v for k, v in (tagmap.get("tags", tagmap)).items()}
    m = re.search(r"(\d{8})", os.path.basename(args.report))
    date = f"{m.group(1)[:4]}-{m.group(1)[4:6]}-{m.group(1)[6:8]}" if m else "unknown"

    cur_people, cur_prog = [], None
    by_project, by_person = defaultdict(list), defaultdict(list)
    for i, text in enumerate(blocks):
        t = tagmap.get(i + 1, {})
        role = t.get("role", "item")
        if role == "person":
            cur_people = _taglist(t, "person", "people")
            continue
        if role == "program":
            cur_prog = t.get("program")
            continue
        if role == "skip":
            continue
        projs = _taglist(t, "project", "projects")
        for pr in projs:                       # fan out into each project bucket
            by_project[pr].append({"date": date, "people": cur_people,
                                   "program": cur_prog, "text": text})
        for person in cur_people:              # and into each person's bucket
            by_person[person].append({"date": date, "program": cur_prog,
                                      "projects": projs, "text": text})

    out = args.out or os.path.join(STAGING, "_extract", f"{date}.{args.source}.pivot.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"date": date, "source": args.source,
                   "by_project": by_project, "by_person": by_person}, f, indent=0)
    multi = sum(1 for v in by_project.values() if len({tuple(b["people"]) for b in v}) > 1)
    print(f"pivot: {len(by_project)} projects ({multi} drawing from >1 person), "
          f"{len(by_person)} people -> {os.path.relpath(out, ROOT)}")
    return 0


def _insert_rows(md, header, rows):
    """Insert table rows just after the separator line under `header`; drop a
    seed placeholder row if present. Returns modified md (unchanged if no table)."""
    lines = md.split("\n")
    for i, ln in enumerate(lines):
        if ln.strip() == header:
            for j in range(i + 1, min(i + 6, len(lines))):
                if re.match(r"^\|[-| ]+\|\s*$", lines[j]):   # the |---|---| separator
                    k = j + 1
                    if k < len(lines) and re.match(r"^\|\s*(\|\s*)+$", lines[k]):
                        del lines[k]                          # drop empty placeholder
                    lines[j + 1:j + 1] = rows
                    return "\n".join(lines)
    return md


def cmd_apply(args):
    """Stage entity edits from a pass-2 synth.json, through the normal gate.

    project -> append a Progress Log row (+ set status);
    person  -> append Weekly Progress rows (one per project worked).
    Reads the LIVE entity, applies the edit, writes the full file to
    _staging/<cycle>/proposed/. Then run `kb.py accept <cycle>`.
    """
    import json
    synth = json.load(open(args.file, encoding="utf-8"))
    date = synth.get("date", args.cycle or "unknown")
    cycle = args.cycle or date
    proposed = os.path.join(STAGING, cycle, "proposed")
    people, programs, projects = _wiki_tagsets()

    def stage(relpath, text):
        dst = os.path.join(proposed, relpath)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "w", encoding="utf-8") as f:
            f.write(text)

    np, npp = 0, 0
    # projects -> Progress Log row + status
    for tag, d in synth.get("projects", {}).items():
        if tag not in projects:
            print(f"  skip project '{tag}' (not in wiki)")
            continue
        leaf = tag.rsplit("/", 1)[-1]
        rel = f"projects/{tag}/overview_{leaf}.md"
        md = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        status = str(d.get("status", "")).strip()
        upd = str(d.get("update", "")).strip().replace("\n", " ").replace("|", "/")
        if status:
            md = re.sub(r"(?m)^status: .*$", f"status: {status}", md, count=1)
        md = _insert_rows(md, "## Progress Log", [f"| {date} | {upd} | {status or '—'} |"])
        stage(rel, md)
        np += 1

    # people -> Weekly Progress rows (one per project)
    for tag, rows in synth.get("people", {}).items():
        if tag not in people:
            print(f"  skip person '{tag}' (not in wiki)")
            continue
        rel = f"people/{tag}/overview_{tag}.md"
        md = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        newrows = []
        for r in rows:
            pj = r.get("project")
            act = str(r.get("activity", "")).strip().replace("\n", " ").replace("|", "/")
            if pj and pj in projects:
                link = f"[[projects/{pj}/overview_{pj.rsplit('/',1)[-1]}\\|{_pretty(pj)}]]"
            else:
                link = "—"
            newrows.append(f"| {date} | {link} | {act} |")
        md = _insert_rows(md, "## Weekly Progress", newrows)
        stage(rel, md)
        npp += 1

    print(f"staged {np} project + {npp} person edits into _staging/{cycle}/. "
          f"Next: kb.py validate {cycle} && kb.py accept {cycle}")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    pp = sub.add_parser("parse", help="docx weekly reports -> plain markdown")
    pp.add_argument("input_dir", nargs="?", default=None)
    pp.add_argument("--out", default=None)
    pp.set_defaults(func=cmd_parse)

    pv = sub.add_parser("validate", help="check staged proposals")
    pv.add_argument("cycle")
    pv.set_defaults(func=cmd_validate)

    pe = sub.add_parser("extract", help="split a report into blocks / render a tagged extract")
    pe.add_argument("mode", choices=["split", "render"])
    pe.add_argument("report", help="parsed report .md")
    pe.add_argument("--source", default="raw", choices=["raw", "program"])
    pe.add_argument("--tags", default=None, help="tag-map JSON (render mode)")
    pe.add_argument("--out", default=None)
    pe.set_defaults(func=cmd_extract)

    pv2 = sub.add_parser("pivot", help="regroup tagged blocks by project & by person (pass-2 input)")
    pv2.add_argument("report", help="parsed report .md")
    pv2.add_argument("--tags", required=True, help="verified tag-map JSON")
    pv2.add_argument("--source", default="raw", choices=["raw", "program"])
    pv2.add_argument("--out", default=None)
    pv2.set_defaults(func=cmd_pivot)

    pa2 = sub.add_parser("apply", help="stage entity edits from a pass-2 synth.json")
    pa2.add_argument("file", help="synth.json")
    pa2.add_argument("--cycle", default=None, help="staging cycle (default: synth date)")
    pa2.set_defaults(func=cmd_apply)

    ps = sub.add_parser("seed", help="spreadsheet -> staged baseline (people/projects/programs)")
    ps.add_argument("file", nargs="?", default=None, help="roster .xlsx (3 tabs)")
    ps.add_argument("--template", default=None, help="write a blank template xlsx here and exit")
    ps.add_argument("--cycle", default="seed-initial", help="staging cycle name")
    ps.set_defaults(func=cmd_seed)

    pa = sub.add_parser("accept", help="promote staged proposals into the wiki")
    pa.add_argument("cycle")
    pa.add_argument("--dry-run", action="store_true")
    pa.add_argument("--only", default=None, help="promote a single staged relpath")
    pa.set_defaults(func=cmd_accept)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
