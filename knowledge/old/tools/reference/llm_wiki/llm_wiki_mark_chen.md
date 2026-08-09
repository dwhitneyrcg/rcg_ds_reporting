In my last article, I wrote about building a simple personal knowledge base inspired by Andrej Karpathy’s LLM Wiki pattern.

The idea was beautifully plain: instead of asking an AI the same question over and over, let the AI maintain a persistent Markdown wiki. Raw sources stay separate. The wiki becomes the organized layer. A small instruction file tells the AI how to keep everything tidy.

That first version worked surprisingly well.

Then I read an article about nashsu/llm_wiki.

And suddenly my little folder-based experiment had a much bigger cousin.

As of April 29, 2026, the GitHub repository is sitting at about 4.9k stars. It is not just a prompt, not just a Claude Code trick, and not just a command-line helper. It is a full cross-platform desktop app for turning documents into an organized, interlinked personal wiki.

The article that introduced it made the project feel much more concrete to me. This was no longer just Karpathy’s pattern as a beautiful idea. Someone had turned it into a product with document import, graph views, web clipping, review queues, and search.

At first, my reaction was very human:

“Oh. They built the real thing.”

But after reading the article that introduced it and looking through the project, I realized the more useful lesson was not “I should build a desktop app too.”

The useful lesson was simpler:

I could steal the right ideas.

Not the whole product. Just the habits.

What the app helped me see
My first LLM Wiki was built around three layers:

raw sources
generated wiki pages
agent instructions
That is already enough to make a personal knowledge base useful.

But nashsu/llm_wiki shows what happens when someone takes the pattern seriously as a product.

It adds things like:

a desktop interface
document import
a Chrome web clipper
graph visualization
vector search
a review queue
persistent ingest jobs
Obsidian compatibility
purpose.md, a file that tells the wiki what it is for
For a beginner, that list can feel intimidating.

But here is the calming part: you do not need to copy all of it.

You only need to ask:

Which of these ideas would make my own small wiki better tomorrow?

For me, the answer was not “build an app.”

It was “make the agent better at maintaining the wiki.”

The most important upgrade: purpose.md
The first idea I borrowed was purpose.md.

This sounds almost too simple. It is just a Markdown file that explains why the wiki exists.

But that one file changes the mood of the whole system.

Without a purpose file, an LLM Wiki can become a clever document dump. It can summarize sources, create pages, and update indexes, but it may not know what kind of knowledge is worth preserving.

With a purpose file, the wiki has direction.

In my case, I wrote down that my wiki exists to help with:

Medium-style article writing
BI report development
KPI governance and lineage
SQL-first reporting from LN and related enterprise systems
future d/EPM and Infor Data Lake integration
That gave the agent a compass.

Now when I add a source, the question is not just “What does this document say?”

It is “What does this document help this wiki become better at?”

That distinction matters.

The second upgrade: ingest in two steps
The second idea I borrowed was two-step ingest.

My original workflow was basically:

read source -> write wiki pages

The app’s approach is more careful:

Analyze first.
Generate second.
That sounds minor, but it changes quality.

In the analysis step, the AI reads the source and identifies:

key entities
important concepts
claims or assumptions
contradictions
likely wiki destinations
items that need human review
Only after that does it write or update wiki pages.

This is especially useful for business documents, where the source may include draft notes, outdated assumptions, or context that should not become permanent guidance.

I ran into this with my KPI and BI reporting materials.

Some files were useful, but still pending update. Some reflected an older data architecture. Some were about d/EPM, while the real direction was shifting toward direct LN backend SQL.

A one-step ingest might have turned all of that into false certainty.

Two-step ingest gives the AI a moment to think before it starts rearranging the shelves.

The third upgrade: review items
The app also includes an async review system.

That idea was worth copying.

In a real knowledge base, not everything should be auto-decided by the model.

Sometimes the AI should say:

“This looks important, but Mark needs to decide.”

For my wiki, review items are useful when:

a KPI owner is unclear
a metric definition is still draft
a source conflicts with another source
a data architecture decision is changing
an external source needs verification
This is one of the healthiest patterns in AI work: let the model do the maintenance, but keep judgment with the human.

The goal is not to make the wiki autonomous.

The goal is to make it less forgetful.

Press enter or click to view image in full size

Why I created a skill instead of an app
After reading about nashsu/llm_wiki, I had an obvious question:

Should I create an app, a plugin, or a skill?

For my current stage, the answer was a skill.

Not because an app is a bad idea. The app is impressive. If you want a visual interface, graph browsing, web clipping, multi-format ingest, persistent queues, or a non-technical user experience, an app makes sense.

But I already had a working Markdown wiki inside my Codex workspace.

My real need was not another interface.

My real need was repeatable behavior.

So we created a project-level Codex skill called llm-wiki-maintainer.

The skill tells Codex how to:

read purpose.md, AGENTS.md, index.md, and log.md
ingest new sources
preserve provenance
update source summaries
synthesize durable concepts and playbooks
create review items
lint the wiki for weak links, stale notes, and duplicated concepts
This is the beginner-friendly version of the lesson:

If your knowledge base already lives in Markdown, a skill may be enough.

You can always build the app later.

What beginners can copy
If you want to build your own simple LLM Wiki, do not start with the full desktop architecture.

Start with five files and folders:

docs/llm-wiki/
  purpose.md
  AGENTS.md
  index.md
  log.md
  sources/
Then add three working habits:

Every source gets a summary page.
Every useful insight gets filed into a concept, topic, or playbook.
Every update refreshes the index and log.
That is enough to begin.

Once the wiki grows, you can borrow more advanced ideas:

add frontmatter for source traceability
add synthesis/ pages for decisions
add review/ pages for human judgment
add Obsidian links
add search or graph tooling later
The trick is not to confuse the destination with the first step.

You do not need a perfect personal knowledge system.

You need one that compounds.

What changed in my own setup
After this experiment, my wiki now has a clearer shape.

I added:

purpose.md
a source note about nashsu/llm_wiki
a synthesis page deciding “skill now, app later”
updated wiki operating rules
a local Codex skill for maintaining the wiki
This is small compared with a full app.

But it is exactly the right size for where I am.

And that may be the broader lesson from the LLM Wiki pattern.

The best knowledge system is not necessarily the one with the most features.

It is the one that fits close enough to your real work that you keep using it.

Final thought
Karpathy’s original pattern gave me the architecture.

nashsu/llm_wiki showed me how far the idea can go.

Building a Codex skill taught me the practical middle path.

For a beginner, that middle path is probably the most important part.

You do not have to jump from “I have some notes” to “I need a full AI knowledge app.”

You can start with a folder, a few Markdown files, and one clear instruction:

help me maintain this knowledge base so it gets more useful every time I touch it.

That is humble.

But it is also powerful.

Because the real promise of an LLM Wiki is not that it remembers everything.

It is that it helps your understanding accumulate instead of evaporating back into chat history.