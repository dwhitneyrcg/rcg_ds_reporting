"""
roster.py
---------
Team roster and name-resolution data for the raw weekly update extraction pipeline.

This file is the SINGLE SOURCE for nickname/alias mappings used by extract_raw_updates.py.
When a new team member joins or a new nickname appears in the weekly reports,
add entries here -- not in the extraction script.

To add a new person:
  1. Add their first-name (lowercase) to ROSTER.
  2. If their first name collides with someone else, add entries to LAST_INITIAL_MAP.
  3. If they use a non-obvious nickname, add an extra ROSTER entry.
"""

# ──────────────────────────────────────────────
# First-name / nickname  →  Full roster name
# ──────────────────────────────────────────────
ROSTER: dict[str, str] = {
    # -- Active team members --
    "aagam": "Aagam Shah",
    "arya": "Arya Cheeti",
    "ayon": "Ayon Ghosh",
    "bao": "Bao Le",
    "ben": "Benjamin Fowler",
    "benjamin": "Benjamin Fowler",
    "caleb": "Caleb Sharkey",
    "camila": "Camila Aichele",
    "carlos": "Carlos Gonzalez Andarcio",
    "cihan": "Cihan Ulus",
    "cristian": "Cristian Villamarin-Villamil",
    "danusio": "Danusio Guimares",
    "david m": "David Martinez",
    "david w": "David Whitney",
    "doug": "Douglas Bedell",
    "douglas": "Douglas Bedell",
    "eddie": "Edward Baffa",
    "edward": "Edward Baffa",
    "erick a.": "Erick Alfaro",
    "erick": "Erick Alfaro",
    "eswar": "Thokala Eswar",
    "evan": "Evan McFall",
    "glen-erik": "Glen-Erik Cortez",
    "gourish": "Gourish Pisal",
    "ignacio": "Ignacio Villasmil",
    "javier": "Nelson Javier Buitrago-Aza",
    "jesse": "Jesse Bausell",
    "kartik": "Kartik Ullal",
    "kevin": "Kevin Diaz",
    "lamis": "Lamis Amer",
    "lekha": "Srilekha Reddy Madupu",
    "luis": "Luis Vargas",
    "mahshad": "Mahshad Shariatnasab",
    "mehdi": "Mehdi Assefi",
    "mert": "Mert Ersoz",
    "michelle": "Michelle Manfrini",
    "mirielle": "Mireille Pascaline Feudjio Tsague",
    "mireille": "Mireille Pascaline Feudjio Tsague",
    "osvaldo": "Osvaldo Velazquez",
    "parimala": "Parimala Kettymuthu",
    "reza": "Reza Bahadori",
    "rodrigo": "Rodrigo Briguido",
    "srilekha": "Srilekha Reddy Madupu",
    "srileka": "Srilekha Reddy Madupu",
    "will": "William Borges",
    "william": "William Borges",
    "anand": "Anand Shah",
    "neila": "Neila Bennamane",
    "nicolas": "Nicolas Tobon",
    "ram": "Ram Sirusanagandla",
    "anneke": "Anneke Augenbroe",
    "nico": "Nicolas Tobon",
    "santiago": "Santiago Baquero",
}

# ──────────────────────────────────────────────
# (first_name_lower, last_initial_lower) → Full name
# Used when reports say "David M." or "Erick A."
# ──────────────────────────────────────────────
LAST_INITIAL_MAP: dict[tuple[str, str], str] = {
    ("ayon", "g"): "Ayon Ghosh",
    ("carlos", "a"): "Carlos Gonzalez Andarcio",
    ("carlos", "g"): "Carlos Gonzalez Andarcio",
    ("cristian", "v"): "Cristian Villamarin-Villamil",
    ("danusio", "g"): "Danusio Guimares",
    ("david", "m"): "David Martinez",
    ("david", "w"): "David Whitney",
    ("erick", "a"): "Erick Alfaro",
    ("erick", "g"): "Erick Alfaro",
    ("evan", "m"): "Evan McFall",
    ("glen-erik", "c"): "Glen-Erik Cortez",
    ("kevin", "d"): "Kevin Diaz",
    ("mirielle", "t"): "Mireille Pascaline Feudjio Tsague",
    ("osvaldo", "v"): "Osvaldo Velazquez",
    ("rodrigo", "b"): "Rodrigo Briguido",
    ("nico", "t"): "Nicolas Tobon",
}
