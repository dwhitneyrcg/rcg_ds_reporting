# Obsidian Wikilink Conventions

> **Source:** [https://obsidian.md/help/links](https://obsidian.md/help/links)

---

## Overview

Internal links (wikilinks) connect notes together, enabling a network of knowledge within an Obsidian vault. Obsidian can automatically update links when files are renamed.

---

## Supported Link Formats

| Format | Syntax | Notes |
|---|---|---|
| **Wikilink** (preferred) | `[[Note Name]]` | Compact; Obsidian default |
| **Markdown link** | `[Note Name](Note%20Name.md)` | Spaces must be percent-encoded (`%20`) |

> Both formats are equivalent and render identically.

---

## Wikilink Syntax Reference

### Link to a File
```
[[Note Name]]
[[Note Name.md]]
[[Figure 1.png]]     ← non-Markdown files require file extension
```

### Link to a Heading (Anchor Link)
```
[[#Heading in same note]]                          ← within current note
[[Other Note#Heading]]                             ← heading in another note
[[Other Note#Parent Heading#Sub Heading]]          ← subheading (chain with #)
[[## search term]]                                 ← search all headings in vault
```

### Link to a Block
```
[[Note Name#^block-id]]          ← link to a specific block
[[^^search term]]                ← search all blocks across vault
```

Block identifiers:
- Auto-generated: `^37066d` (random hex)
- Human-readable: `^quote-of-the-day` (Latin letters, numbers, dashes only)
- Placement: end of paragraph line, or on a **separate line** (with blank lines before/after) for lists, quotes, callouts, and tables

> **Note:** Block references are Obsidian-specific and won't work outside of Obsidian.

### Custom Display Text (Aliases in-line)
```
[[Note Name|Custom Label]]               ← display "Custom Label", link to Note Name
[[Note Name#Heading|Section Label]]      ← display "Section Label", link to heading
```

> Use inline display text for **one-off** customizations.  
> Use [Aliases](https://obsidian.md/help/aliases) for reusable alternate note names across the vault.

### Embedding (Transcluding) Content
Prefix a wikilink with `!` to embed the linked content inline:
```
![[Note Name]]
![[Figure 1.png]]
```

---

## Invalid Characters in Links

Avoid the following characters in file/note names used as links:

```
#  |  ^  :  %%  [[  ]]
```

These characters may cause links to break.

---

## Settings & Behavior

| Setting | Default | Notes |
|---|---|---|
| Use `[[Wikilinks]]` | Enabled | Disable for Markdown-only links |
| Automatically update internal links | Enabled | Obsidian updates links on file rename |
| Autocomplete (`[[`) | Always active | Works even when wikilinks are disabled |

> When wikilinks are disabled, typing `[[` still triggers autocomplete but generates Markdown-format links on selection.

---

## Quick Reference

| Goal | Syntax |
|---|---|
| Link to a note | `[[Note Name]]` |
| Link to a heading | `[[Note Name#Heading]]` |
| Link to a subheading | `[[Note Name#H1#H2]]` |
| Link to a block | `[[Note Name#^block-id]]` |
| Custom display text | `[[Note Name\|Label]]` |
| Embed content | `![[Note Name]]` |
| Search headings in vault | `[[## keyword]]` |
| Search blocks in vault | `[[^^ keyword]]` |

---

*Conventions document created for use with AI coding agents building Obsidian markdown databases.*
