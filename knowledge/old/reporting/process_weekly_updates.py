"""
Format Weekly Updates into Markdown - Tasks 1 & 2
Process raw + summarized docx files into structured markdown.

Usage:
  python process_weekly_updates.py

Requirements:
  - python-docx (pip install python-docx)
  - openpyxl (pip install openpyxl)

Source docx files:
  - knowledge/reporting/weekly_updates_raw/*.docx
  - knowledge/reporting/weekly_updates_summarized/*.docx

Output markdown files:
  - knowledge/reporting/weekly_updates_raw_md/*.md
  - knowledge/reporting/weekly_updates_summarized_md/*.md
"""
import os, re, shutil, traceback
from docx import Document

BASE = r"C:\Users\133486\OneDrive - Royal Caribbean Group\LocalDatabricks\rcg_ds_reporting\knowledge"
REPORTING = os.path.join(BASE, "reporting")
RAW_SRC = os.path.join(REPORTING, "weekly_updates_raw")
SUM_SRC = os.path.join(REPORTING, "weekly_updates_summarized")
RAW_MD = os.path.join(REPORTING, "weekly_updates_raw_md")
SUM_MD = os.path.join(REPORTING, "weekly_updates_summarized_md")
TEMP_DIR = r"C:\Users\133486"

# Ensure output dirs exist
os.makedirs(RAW_MD, exist_ok=True)
os.makedirs(SUM_MD, exist_ok=True)

# ============ REFERENCE DATA ============
# Business areas: display_name -> folder_name
BUSINESS_AREAS = {
    "PCP Pricing Automation (RCI/CEL)": "pcp_pricing_automation_(rci_cel)",
    "PCP Pricing Automation": "pcp_pricing_automation_(rci_cel)",
    "PCP Pricing": "pcp_pricing_automation_(rci_cel)",
    "Revenue Management Automation (RCI)": "revenue_management_automation_(rci)",
    "Revenue Management (RCI)": "revenue_management_automation_(rci)",
    "RCI Revenue Management": "revenue_management_automation_(rci)",
    "RCI Rev Mgmt": "revenue_management_automation_(rci)",
    "Revenue Management Automation (CEL)": "revenue_management_automation_(cel)",
    "Revenue Management (CEL)": "revenue_management_automation_(cel)",
    "CEL Revenue Management": "revenue_management_automation_(cel)",
    "CEL Rev Mgmt": "revenue_management_automation_(cel)",
    "Revenue Management Automation (SSC)": "revenue_management_automation_(ssc)",
    "Revenue Management (SSC)": "revenue_management_automation_(ssc)",
    "SSC Revenue Management": "revenue_management_automation_(ssc)",
    "Silversea Revenue Management": "revenue_management_automation_(ssc)",
    "PROPEL Targeted Offers (CEL)": "propel_targeted_offers_(cel)",
    "PROPEL Targeted Offers": "propel_targeted_offers_(cel)",
    "PROPEL": "propel_targeted_offers_(cel)",
    "Contact Center Optimization & Automation (RCI/CEL)": "contact_center_optimization_&_automation_(rci_cel)",
    "Contact Center Optimization & Automation": "contact_center_optimization_&_automation_(rci_cel)",
    "Contact Center": "contact_center_optimization_&_automation_(rci_cel)",
    "ConversationalAI": "contact_center_optimization_&_automation_(rci_cel)",
    "Conversational AI": "contact_center_optimization_&_automation_(rci_cel)",
    "AXIOM Generative-AI SEATs (Hotel Ops, Consumer Insights, Legal)": "axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)",
    "AXIOM Generative-AI SEATs": "axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)",
    "AXIOM: Generative-AI SEATs (Hotel Ops, Consumer Insights)": "axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)",
    "AXIOM: Generative-AI SEATs": "axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)",
    "AXIOM": "axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)",
    "Axiom": "axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)",
    "Project Axiom": "axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)",
    "Medallia": "axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)",
    "Marine Insights Analytics Platform (Marine Operations)": "marine_insights_analytics_platform_(marine_operations)",
    "Marine Insights Analytics Platform": "marine_insights_analytics_platform_(marine_operations)",
    "MIAP": "marine_insights_analytics_platform_(marine_operations)",
    "Marine Operations": "marine_insights_analytics_platform_(marine_operations)",
    "Marine": "marine_insights_analytics_platform_(marine_operations)",
    "Supply Chain Optimization": "supply_chain_optimization",
    "Supply Chain": "supply_chain_optimization",
    "IBP Supply Chain": "supply_chain_optimization",
    "Win-on-Waste (Hotel Operations)": "win-on-waste_(hotel_operations)",
    "Win-on-Waste": "win-on-waste_(hotel_operations)",
    "WoW": "win-on-waste_(hotel_operations)",
    "Win on Waste": "win-on-waste_(hotel_operations)",
    "Customer Lifetime Value (Corporate Planning)": "customer_lifetime_value_(corporate_planning)",
    "Customer Lifetime Value": "customer_lifetime_value_(corporate_planning)",
    "CLTV": "customer_lifetime_value_(corporate_planning)",
    "CLV": "customer_lifetime_value_(corporate_planning)",
    "Loyalty": "loyalty_program_redesign",
    "Loyalty Program Redesign": "loyalty_program_redesign",
    "Customer Targeting (E-Commerce)": "customer_targeting_(e-commerce)",
    "Customer Targeting": "customer_targeting_(e-commerce)",
    "E-Commerce": "customer_targeting_(e-commerce)",
    "Hybris Product Recommendations (Digital)": "hybris_product_recommendations_(digital)",
    "Hybris Product Recommendations": "hybris_product_recommendations_(digital)",
    "MyCruise Recommender": "hybris_product_recommendations_(digital)",
    "Product Recommendations": "hybris_product_recommendations_(digital)",
    "RoyalOne Community (Digital)": "royalone_community_(digital)",
    "RoyalOne Community": "royalone_community_(digital)",
    "RoyalOne": "royalone_community_(digital)",
    "NewBuild": "newbuild",
    "Newbuild": "newbuild",
    "New Build": "newbuild",
    "HR": "hr",
}

# Active projects: area_folder -> list of (project_folder, display_name)
ACTIVE_PROJECTS = {}


def _load_projects():
    proj_file = os.path.join(BASE, "biz_areas", "business_active_projects_master.md")
    with open(proj_file, 'r', encoding='utf-8') as f:
        content = f.read()
    current_area = None
    for line in content.split('\n'):
        m = re.match(r'^## \[\[([^/]+)/', line)
        if m:
            current_area = m.group(1)
            if current_area not in ACTIVE_PROJECTS:
                ACTIVE_PROJECTS[current_area] = []
            continue
        m = re.match(r'^- \[\[([^/]+)/([^/]+)/[^|]*\|([^\]]+)\]\]', line)
        if m and current_area:
            area_f, proj_f, display = m.group(1), m.group(2), m.group(3)
            ACTIVE_PROJECTS.setdefault(area_f, []).append((proj_f, display))


_load_projects()

# People: first_name_lower -> list of {full_name, folder, business_area}
PEOPLE = {}
PEOPLE_BY_FOLDER = {}


def _load_people():
    ppl_dir = os.path.join(BASE, "people")
    for d in os.listdir(ppl_dir):
        ov = os.path.join(ppl_dir, d, f"overview_{d}.md")
        if not os.path.isfile(ov):
            continue
        with open(ov, 'r', encoding='utf-8') as f:
            content = f.read()
        nm = re.search(r'^name:\s*"([^"]+)"', content, re.MULTILINE)
        if not nm:
            continue
        full_name = nm.group(1)
        ba = re.search(r'^## Business Area\s*\n\s*(.+)', content, re.MULTILINE)
        biz = ba.group(1).strip() if ba else ""
        folder = d
        first_name = full_name.split()[0].lower()
        PEOPLE.setdefault(first_name, []).append({
            'full_name': full_name,
            'folder': folder,
            'business_area': biz,
        })
        PEOPLE_BY_FOLDER[folder] = full_name


_load_people()


# ============ UTILITY FUNCTIONS ============

def to_folder(name):
    return name.lower().replace(' ', '_')


def extract_date(filename):
    """Extract YYYYMMDD from filename and format as YYYY-MM-DD"""
    m = re.match(r'(\d{8})', filename)
    if m:
        d = m.group(1)
        return f"{d[:4]}-{d[4:6]}-{d[6:8]}"
    return "Unknown"


def match_business_area(text):
    """Match text to a business area folder name. Longest-match-first."""
    text_clean = text.strip().rstrip(':').rstrip('-').strip()
    for display, folder in sorted(BUSINESS_AREAS.items(), key=lambda x: -len(x[0])):
        if display.lower() in text_clean.lower():
            return folder, display
    text_lower = text_clean.lower()
    for display, folder in sorted(BUSINESS_AREAS.items(), key=lambda x: -len(x[0])):
        if any(word in text_lower for word in display.lower().split() if len(word) > 3):
            return folder, display
    return None, text_clean


def match_project(area_folder, text):
    """Try to match text content to an active project in the given business area"""
    if not area_folder or area_folder not in ACTIVE_PROJECTS:
        return None, None
    text_lower = text.lower()
    best_match = None
    best_score = 0
    for proj_folder, proj_display in ACTIVE_PROJECTS[area_folder]:
        proj_words = set(proj_display.lower().replace('-', ' ').replace('_', ' ').split())
        proj_words = {w for w in proj_words if len(w) > 2}
        score = sum(1 for w in proj_words if w in text_lower)
        if score > best_score:
            best_score = score
            best_match = (proj_folder, proj_display)
    if best_score >= 1 and best_match:
        return best_match
    return None, None


def resolve_person(first_name, area_context=""):
    """Resolve a first name to a full person, using area context for disambiguation"""
    first_lower = first_name.strip().lower()
    candidates = PEOPLE.get(first_lower, [])
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]
    if area_context:
        area_lower = area_context.lower()
        for c in candidates:
            if c['business_area'].lower() in area_lower or area_lower in c['business_area'].lower():
                return c
    # Heuristics for known ambiguous names
    if first_lower == 'david' and area_context:
        for c in candidates:
            if 'hotel' in area_context.lower() or 'axiom' in area_context.lower():
                if 'martinez' in c['folder']:
                    return c
            if 'revenue' in area_context.lower() or 'various' in c['business_area'].lower():
                if 'whitney' in c['folder']:
                    return c
    return candidates[0]


def summarize_text(text, max_sentences=3):
    """Extract first few meaningful sentences as a summary"""
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    meaningful = [s for s in sentences if len(s) > 20]
    return ' '.join(meaningful[:max_sentences]) if meaningful else text[:300]


# Patterns that indicate a sentence is about focus/next steps (forward-looking)
FOCUS_PATTERNS = re.compile(
    r'(?:Teams?\s+(?:are|is)\s+(?:focusing|currently|now|actively|planning|preparing|working))'
    r'|(?:Focus\s+areas?\s+include)'
    r'|(?:Next\s+steps?\s+(?:include|involve|are))'
    r'|(?:Teams?\s+(?:will|plan\s+to|intend\s+to|aim\s+to))'
    r'|(?:Going\s+forward)'
    r'|(?:The\s+team\s+(?:is|are)\s+(?:focusing|currently|now|actively|planning))',
    re.IGNORECASE
)


def split_achievements_focus(text):
    """Split a paragraph into achievement sentences and focus-area sentences.

    Focus-area sentences are those matching forward-looking patterns like
    'Teams are focusing on...'. Everything else is treated as achievements.
    """
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    achievement_parts = []
    focus_parts = []
    for s in sentences:
        if not s.strip():
            continue
        if FOCUS_PATTERNS.search(s):
            focus_parts.append(s)
        else:
            achievement_parts.append(s)
    achievements = ' '.join(achievement_parts).strip()
    focus_areas = ' '.join(focus_parts).strip()
    return achievements, focus_areas


# ============ TASK 1: Process Raw Updates ============

def process_raw_docx(src_path, filename):
    """Process a raw weekly updates docx into structured markdown"""
    date_str = extract_date(filename)
    temp_path = os.path.join(TEMP_DIR, "temp_raw_proc.docx")
    shutil.copy2(src_path, temp_path)

    try:
        doc = Document(temp_path)
    except Exception as e:
        return None, str(e)

    paras = [p.text for p in doc.paragraphs]

    # Split into discrete updates by blank lines
    updates = []
    current_block = []
    blank_count = 0
    for text in paras:
        stripped = text.strip()
        if not stripped or stripped == '\xa0':
            blank_count += 1
            if blank_count >= 1 and current_block:
                updates.append(current_block)
                current_block = []
                blank_count = 0
        else:
            blank_count = 0
            current_block.append(stripped)
    if current_block:
        updates.append(current_block)

    # Process each discrete update block
    structured = []
    for block in updates:
        if not block or len(block) < 1:
            continue
        if 'raw_monthly_text' in block[0].lower():
            continue

        first_line = block[0]
        people_found = []
        area_folder = None
        area_display = None

        # Check for area in parenthetical in first line
        name_clean = re.sub(r'\s*\([^)]*\)\s*', ' ', first_line).strip()
        paren_match = re.search(r'\(([^)]+)\)', first_line)
        if paren_match:
            af, ad = match_business_area(paren_match.group(1))
            if af:
                area_folder, area_display = af, ad

        # Split names by &, and, comma, /
        name_parts = re.split(r'\s*[&,/]\s*|\s+and\s+', name_clean.rstrip(':'))
        for part in name_parts:
            part = part.strip().rstrip(':')
            if not part or len(part) < 2:
                continue
            first = part.split()[0]
            person = resolve_person(first, area_display or "")
            if person:
                people_found.append(person)

        # Identify business area from second line
        content_start = 1
        if len(block) > 1 and not area_folder:
            af, ad = match_business_area(block[1])
            if af:
                area_folder, area_display = af, ad
                content_start = 2

        if not area_folder:
            af, ad = match_business_area(first_line)
            if af:
                area_folder, area_display = af, ad
                if not people_found:
                    content_start = 1

        # Extract core content
        raw_lines = block[content_start:]
        raw_update = '\n'.join(raw_lines) if raw_lines else '\n'.join(block)
        if not raw_update.strip():
            raw_update = '\n'.join(block)

        # Match project
        proj_folder, proj_display = match_project(area_folder, raw_update)
        if not proj_folder and area_folder:
            for b in block[:3]:
                pf, pd = match_project(area_folder, b)
                if pf:
                    proj_folder, proj_display = pf, pd
                    break

        summary = summarize_text(raw_update)

        tags = []
        if area_folder:
            tags.append(f"business_area/{area_folder}")
        if proj_folder:
            tags.append(f"project/{proj_folder}")
        for p in people_found:
            tags.append(p['folder'])

        structured.append({
            'date': date_str,
            'business_area': area_folder or 'unclassified',
            'business_area_display': area_display or 'Unclassified',
            'project': proj_folder,
            'project_display': proj_display,
            'people': people_found,
            'summary': summary,
            'raw_update': raw_update,
            'tags': tags,
        })

    try:
        os.remove(temp_path)
    except:
        pass

    return structured, None


def write_raw_markdown(structured_updates, filename, date_str):
    """Write structured raw updates to a markdown file"""
    md_name = os.path.splitext(filename)[0] + ".md"
    md_path = os.path.join(RAW_MD, md_name)

    all_tags = set(['weekly_update', 'raw'])
    for u in structured_updates:
        all_tags.update(u['tags'])

    tags_str = '\n'.join(f'  - {t}' for t in sorted(all_tags))

    lines = [f"""---
tags:
{tags_str}
date: "{date_str}"
type: "raw_weekly_update"
---

# Weekly Update (Raw) - {date_str}
"""]

    for i, u in enumerate(structured_updates):
        people_links = ', '.join(
            f"[[{p['folder']}/overview_{p['folder']}|{p['full_name']}]]"
            for p in u['people']
        ) if u['people'] else 'Unidentified'

        lines.append(f"## Update {i+1}")
        lines.append(f"")
        lines.append(f"**Date:** {u['date']}")
        lines.append(f"**Business Area:** {u['business_area_display']}")
        if u['project_display']:
            lines.append(f"**Business Project:** {u['project_display']}")
        lines.append(f"**People:** {people_links}")
        lines.append(f"")
        lines.append(f"### Summarized Update")
        lines.append(f"")
        lines.append(f"{u['summary']}")
        lines.append(f"")
        lines.append(f"### Raw Update")
        lines.append(f"")
        lines.append(f"{u['raw_update']}")
        lines.append(f"")
        lines.append(f"---")
        lines.append(f"")

    lines.append(f"_Source: {filename}_")

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    return md_path


# ============ TASK 2: Process Summarized Updates ============

def process_summarized_docx(src_path, filename):
    """Process a summarized weekly updates docx into structured markdown"""
    date_str = extract_date(filename)
    temp_path = os.path.join(TEMP_DIR, "temp_sum_proc.docx")
    shutil.copy2(src_path, temp_path)

    try:
        doc = Document(temp_path)
    except Exception as e:
        return None, str(e)

    paras = []
    for p in doc.paragraphs:
        text = p.text.strip()
        bold = any(r.bold for r in p.runs if r.bold) if p.runs else False
        is_list = p.style.name.startswith('List')
        paras.append({'text': text, 'bold': bold, 'is_list': is_list})

    current_section = None
    updates = []
    current_update_text = []
    current_area_display = None

    for para in paras:
        text = para['text'].strip()
        if not text or text == '\xa0':
            continue

        text_lower = text.lower().strip()
        if text_lower in ('proud', 'proud:', 'proud: ', 'concerns:', 'concerned:',
                          'concern:', 'concerns', 'concerned', 'excited', 'excited:'):
            if current_update_text and current_area_display:
                updates.append({
                    'section': current_section,
                    'area_display': current_area_display,
                    'text': '\n'.join(current_update_text)
                })
                current_update_text = []
                current_area_display = None
            current_section = text_lower.rstrip(':').strip()
            if current_section in ('concern', 'concerns', 'concerned'):
                current_section = 'concerned'
            continue

        # Remove bullet chars
        bullet_match = re.match(r'^[•\-\*]\s*(.+)', text)
        if bullet_match:
            text = bullet_match.group(1)

        # Detect business area at start: "Business Area Name: rest of text"
        area_match = re.match(r'^([^:]+?):\s*(.*)', text, re.DOTALL)
        if area_match:
            potential_area = area_match.group(1).strip()
            af, ad = match_business_area(potential_area)
            if af:
                if current_update_text and current_area_display:
                    updates.append({
                        'section': current_section,
                        'area_display': current_area_display,
                        'text': '\n'.join(current_update_text)
                    })
                current_area_display = potential_area
                remaining = area_match.group(2).strip()
                current_update_text = [remaining] if remaining else []
                continue

        # Check if whole paragraph starts with a known area (no colon)
        af, ad = match_business_area(text.split('\n')[0].split('.')[0])
        if af and not current_update_text:
            if current_update_text and current_area_display:
                updates.append({
                    'section': current_section,
                    'area_display': current_area_display,
                    'text': '\n'.join(current_update_text)
                })
            current_area_display = text.split('\n')[0].split('.')[0].strip()
            rest = text[len(current_area_display):].lstrip(':').lstrip('-').strip()
            current_update_text = [rest] if rest else []
            continue

        # Continue current update
        if current_area_display is not None:
            current_update_text.append(text)
        else:
            af, ad = match_business_area(text)
            if af:
                current_area_display = text.rstrip(':').strip()
                current_update_text = []
            else:
                current_update_text.append(text)

    # Save last update
    if current_update_text and current_area_display:
        updates.append({
            'section': current_section,
            'area_display': current_area_display,
            'text': '\n'.join(current_update_text)
        })

    # Structure the updates
    structured = []
    for u in updates:
        area_folder, area_display = match_business_area(u['area_display'])
        raw_text = u['text'].strip()
        if not raw_text:
            continue

        section = u.get('section', '')

        # Split every paragraph into achievements vs focus areas
        # based on sentence-level patterns, regardless of section
        achievements, focus_areas = split_achievements_focus(raw_text)

        # For concerned section, if nothing matched as focus, treat full text as focus
        if section == 'concerned' and not focus_areas:
            focus_areas = raw_text.strip()
            achievements = ""

        proj_folder, proj_display = match_project(area_folder, raw_text)
        if not proj_folder and area_folder:
            proj_folder, proj_display = match_project(area_folder, u['area_display'])

        tags = []
        if area_folder:
            tags.append(f"business_area/{area_folder}")
        if proj_folder:
            tags.append(f"project/{proj_folder}")

        structured.append({
            'date': date_str,
            'section': section,
            'business_area': area_folder or 'unclassified',
            'business_area_display': area_display or u['area_display'],
            'project': proj_folder,
            'project_display': proj_display,
            'achievements': achievements,
            'focus_areas': focus_areas,
            'raw_update': raw_text,
            'tags': tags,
        })

    try:
        os.remove(temp_path)
    except:
        pass

    return structured, None


def write_summarized_markdown(structured_updates, filename, date_str):
    """Write structured summarized updates to a markdown file"""
    md_name = os.path.splitext(filename)[0] + ".md"
    md_path = os.path.join(SUM_MD, md_name)

    all_tags = set(['weekly_update', 'summarized'])
    for u in structured_updates:
        all_tags.update(u['tags'])

    tags_str = '\n'.join(f'  - {t}' for t in sorted(all_tags))

    lines = [f"""---
tags:
{tags_str}
date: "{date_str}"
type: "summarized_weekly_update"
---

# Weekly Update (Summarized) - {date_str}
"""]

    sections = {}
    for u in structured_updates:
        sec = u.get('section', 'general') or 'general'
        sections.setdefault(sec, []).append(u)

    section_order = ['proud', 'excited', 'concerned', 'general']
    section_titles = {
        'proud': 'Proud', 'excited': 'Excited',
        'concerned': 'Concerned', 'general': 'Updates'
    }

    for sec_key in section_order:
        if sec_key not in sections:
            continue
        lines.append(f"## {section_titles.get(sec_key, sec_key.title())}")
        lines.append(f"")

        for u in sections[sec_key]:
            lines.append(f"### {u['business_area_display']}")
            lines.append(f"")
            lines.append(f"**Date:** {u['date']}")
            lines.append(f"**Business Area:** {u['business_area_display']}")
            if u['project_display']:
                lines.append(f"**Business Project:** {u['project_display']}")
            if u['achievements']:
                lines.append(f"")
                lines.append(f"**Achievements:**")
                lines.append(f"{u['achievements']}")
            if u['focus_areas']:
                lines.append(f"")
                lines.append(f"**Focus Areas:**")
                lines.append(f"{u['focus_areas']}")
            lines.append(f"")
            lines.append(f"**Raw Update:**")
            lines.append(f"{u['raw_update']}")
            lines.append(f"")
            lines.append(f"---")
            lines.append(f"")

    lines.append(f"_Source: {filename}_")

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    return md_path


# ============ MAIN ============

def main():
    # --- TASK 1: Raw Updates ---
    print("=== TASK 1: Process Raw Weekly Updates ===")
    raw_files = sorted([
        f for f in os.listdir(RAW_SRC)
        if f.endswith('.docx') and not f.startswith('~')
    ])
    raw_success = 0
    raw_errors = []

    for fname in raw_files:
        src = os.path.join(RAW_SRC, fname)
        date_str = extract_date(fname)
        updates, err = process_raw_docx(src, fname)
        if err:
            raw_errors.append((fname, err))
            print(f"  ERROR: {fname}: {err}")
            continue
        if updates:
            write_raw_markdown(updates, fname, date_str)
            raw_success += 1
        else:
            md_name = os.path.splitext(fname)[0] + ".md"
            md_path = os.path.join(RAW_MD, md_name)
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(
                    f"---\ntags:\n  - weekly_update\n  - raw\n"
                    f"date: \"{date_str}\"\ntype: \"raw_weekly_update\"\n---\n\n"
                    f"# Weekly Update (Raw) - {date_str}\n\n"
                    f"_No structured updates extracted._\n\n_Source: {fname}_\n"
                )
            raw_success += 1

    print(f"  Processed: {raw_success}/{len(raw_files)} files")
    if raw_errors:
        print(f"  Errors: {len(raw_errors)}")
        for fn, e in raw_errors:
            print(f"    {fn}: {e}")

    # --- TASK 2: Summarized Updates ---
    print("\n=== TASK 2: Process Summarized Weekly Updates ===")
    sum_files = sorted([
        f for f in os.listdir(SUM_SRC)
        if f.endswith('.docx') and not f.startswith('~')
    ])
    sum_success = 0
    sum_errors = []

    for fname in sum_files:
        src = os.path.join(SUM_SRC, fname)
        date_str = extract_date(fname)
        updates, err = process_summarized_docx(src, fname)
        if err:
            sum_errors.append((fname, err))
            print(f"  ERROR: {fname}: {err}")
            continue
        if updates:
            write_summarized_markdown(updates, fname, date_str)
            sum_success += 1
        else:
            md_name = os.path.splitext(fname)[0] + ".md"
            md_path = os.path.join(SUM_MD, md_name)
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(
                    f"---\ntags:\n  - weekly_update\n  - summarized\n"
                    f"date: \"{date_str}\"\ntype: \"summarized_weekly_update\"\n---\n\n"
                    f"# Weekly Update (Summarized) - {date_str}\n\n"
                    f"_No structured updates extracted._\n\n_Source: {fname}_\n"
                )
            sum_success += 1

    print(f"  Processed: {sum_success}/{len(sum_files)} files")
    if sum_errors:
        print(f"  Errors: {len(sum_errors)}")
        for fn, e in sum_errors:
            print(f"    {fn}: {e}")

    # Cleanup any leftover temp files
    for t in ['temp_raw_proc.docx', 'temp_sum_proc.docx']:
        try:
            os.remove(os.path.join(TEMP_DIR, t))
        except:
            pass

    print(f"\n=== SUMMARY ===")
    print(f"Raw: {raw_success} MD files from {len(raw_files)} docx")
    print(f"Summarized: {sum_success} MD files from {len(sum_files)} docx")
    print(f"Total errors: {len(raw_errors) + len(sum_errors)}")
    print("=== DONE ===")


if __name__ == "__main__":
    main()
