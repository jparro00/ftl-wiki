# How to Set Up an LLM Wiki

*A hand-off document. Give this to an agent (Claude Code or equivalent) along with a
subject and a folder, and it can stand the whole thing up.*

---

## How to read this document

**This is a description of a method, not a specification to implement literally.** It
was written without knowing your subject. Sections §0–2 and §6–9 are the load-bearing
parts and travel to any domain; §3 onward involves judgment that only makes sense once
you know what you're cataloguing.

So, before building: **read it, then argue with it.** Specifically —

- **Decide which parts don't apply.** The version/validity field (§4) is pointless in a
  domain with no drift. A `chains`-style sequence type is meaningless where nothing is
  sequential. Dropping a section deliberately is a good outcome; keeping it out of
  deference is not.
- **Say what you'd change before you start.** Present the page types (§3) and the
  per-type frontmatter to the human and get agreement. This is the decision that's
  expensive to reverse, and it's the one this document cannot make for you.
- **Treat the first ingest as a test of the schema, not just of the source.** Fields
  nobody fills in, types that split awkwardly, sections that are always empty — these
  are schema bugs. Report them and propose fixes rather than dutifully filling in
  structure that isn't earning its place.
- **Push back on the human too.** If the subject is too broad, the sources too thin, or
  a requested page type looks like it'll only ever hold two pages, say so. The method
  depends on someone exercising judgment about what belongs; you are the one with the
  data in front of you.

The failure mode this warns against is real and common: an agent implements all twelve
sections faithfully, produces a structurally perfect wiki full of `unknown` fields and
empty sections, and nobody notices for fifty pages that half the schema was wrong for
this domain.

---

## 0. What this is

An **LLM wiki** is a plain-markdown knowledge base about one subject, where a human
curates the sources and asks the questions, and an LLM does all the bookkeeping —
summarizing, filing, cross-linking, keeping it consistent.

The idea comes from [Andrej Karpathy's LLM Wiki
gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). The core
insight: the bottleneck on personal knowledge bases has never been storage or search,
it's the **labor of maintenance** — writing summaries, updating pages when new
information arrives, keeping links from rotting. That labor is now approximately free.
So build the thing that was always correct in principle but too tedious in practice: a
densely cross-linked, continuously maintained wiki.

**Design constraints that make it work:**

- **No app, no database, no lock-in.** Markdown files in a git repo. Readable in any
  editor, greppable, diffable, portable forever.
- **Two layers, one direction.** Immutable sources in, interpreted pages out. Every
  claim traces back to a source.
- **The agent's instructions live in the repo.** A `CLAUDE.md` (or `AGENTS.md`) at the
  root is the schema *and* the operating manual. It gets injected into the agent's
  context at the start of every session, so the wiki teaches whoever opens it how to
  maintain itself.
- **Small pages, dense links.** One topic per page. Link liberally.

It scales to hundreds of pages with no search index because the agent reads a catalog
file first and greps for the rest.

---

## 1. Pick the subject before anything else

The method works best on a subject with these properties:

- **Bounded but deep.** A game's mechanics, a codebase's architecture, a legal regime,
  a research literature, a company's internal systems, a hobby with a large corpus.
- **Has raw sources you can actually collect.** Docs, dumps, exports, papers, forum
  threads, transcripts, your own notes.
- **Sources disagree.** This is a feature — reconciling and *recording* disagreement is
  where a wiki earns its keep over just asking a model.
- **You'll ask it questions repeatedly.** A wiki you build once and never query is a
  waste; the value compounds with use.

Write the subject down in one sentence before starting. It goes at the top of
`CLAUDE.md` and it disciplines every later decision about what belongs.

---

## 2. Directory layout

```
.
├── CLAUDE.md              ← the schema + operating manual (the most important file)
├── README.md              ← how the human operates the wiki
├── raw/                   ← IMMUTABLE source layer — the human drops files here
│   ├── <category-a>/
│   ├── <category-b>/
│   └── notes/             ← the human's own observations
└── wiki/                  ← THE AGENT'S LAYER — everything below is maintained by it
    ├── <type-a>/          ← one page per thing of that type
    ├── <type-b>/
    ├── concepts/          ← cross-cutting mechanics and themes
    ├── sources/           ← one summary page per ingested raw file
    ├── _templates/        ← copy-paste starting points, one per page type
    ├── index.md           ← the catalog the agent reads first on every query
    ├── log.md             ← append-only chronological activity record
    └── overview.md        ← human-facing snapshot of coverage
```

Rules that matter more than they look:

- **`raw/` is never edited.** Not by the agent, not to fix a typo. It's the ground
  truth; if it's wrong, that fact gets recorded in the wiki layer, not patched at the
  source.
- **Content directories under `wiki/` are created lazily.** Only `_templates/` and the
  three top-level files exist up front. The first ingest that needs a directory creates
  it. Empty scaffolding is noise.
- **Generated output goes in siblings of `wiki/`, never inside it.** If the wiki later
  grows tooling that emits HTML, JSON, or build artifacts, those live in their own
  top-level directories so that grepping `wiki/` never scans machine output.
- **Subdirectory categories under `raw/` are the human's business.** The agent should
  handle whatever shape it finds.

---

## 3. Choose the page types

This is the one genuinely subject-specific design decision, and it's worth ten minutes
of thought. **Page types are the nouns of the domain.** Get them right and everything
links cleanly; get them wrong and you'll have pages that are half one thing and half
another.

Every wiki gets these two for free:

- **`concepts/`** — mechanics and themes broader than any single page. The place for
  "how X actually works", "the economics of Y", "differences between version A and B".
- **`sources/`** — one summary page per ingested raw file. This is the *citation
  target*: wiki claims cite the source page, and the source page names the raw file.
  The indirection means you can re-summarize a source without rewriting every citation.

Then pick three to five domain nouns. Some worked examples:

| Subject | Page types |
|---|---|
| A video game's content | events, chains (multi-step quests), zones, entities, items |
| A codebase | modules, services, data models, decisions (ADR-style), runbooks |
| A research literature | papers, methods, datasets, claims, open-problems |
| A legal/regulatory domain | statutes, cases, obligations, entities, jurisdictions |
| A company's internal ops | systems, teams, processes, incidents, vendors |

Heuristics:

- **A type earns its place if you'd ask a question scoped to it** ("which *items* do
  I need for…", "what does *module* X depend on").
- **Prefer few types.** Five is plenty. When in doubt, it's a `concept`.
- **If two types always appear together, they're one type.**
- **A type that would only ever have one or two pages isn't a type.** Fold it into
  `concepts/`.

---

## 4. Page anatomy

Every page is markdown with YAML frontmatter. Templates in `wiki/_templates/`, one per
type, copied when creating a page.

### Frontmatter

Universal fields on every page:

```yaml
---
id: <type>-<slug>          # type prefix + filename slug
type: <page-type>          # matches the directory
first_seen: YYYY-MM-DD     # date it first appeared in a source
last_updated: YYYY-MM-DD
sources: 0                 # count of raw sources referencing it
tags: []
---
```

Then per-type fields — the structured facts you'd want to filter on. Keep them to a
handful, and **enumerate the allowed values in `CLAUDE.md`** so the linter can check
them. Design them so that `unknown` is always a legal value.

### The `unknown` discipline

**Give every enum field an explicit `unknown` option, and use it.** The single most
common failure mode of an LLM-maintained wiki is the model filling a gap with a
plausible-sounding fact from its training data. `unknown` is a valid, useful, *correct*
answer. It marks work to do. A confident wrong value is worse than a blank.

The same goes for numbers: a percentage without a source is a guess. Mark it `unknown`.

### A version / validity field, if your domain has drift

If your subject exists in multiple versions, editions, jurisdictions, or eras — and
sources routinely fail to say which one they describe — add a field for it:

```yaml
version: unknown           # <v1> | <v2> | both | unknown
```

Version mismatch is the most common source of apparent contradictions. A source that
doesn't state its version is `unknown`, **not** the current one. This one field
resolves an enormous fraction of disagreements before they turn into confusion.

### Body

Fixed section headings per type, defined in the template. Omit a section only when you
genuinely have nothing for it. Nearly every type wants:

```markdown
## Summary
One paragraph. What this is and why it matters.

## <domain-specific sections>
The actual payload. Tables are often the right shape for structured facts.

## Related
- [[other-page]] — how it relates

## Open Questions
- [ ] What we still need to confirm.

## Sources
- [[source-name]] (per raw/path/to/file)
```

**`Open Questions` is not decoration.** It's the wiki's to-do list, it's what turns a
gap into a task, and a lint pass collects it across all pages.

---

## 5. Naming, IDs, and linking

- **Slugs**: lowercase, hyphenated, human-readable.
- **Filename omits the type prefix; the `id` carries it; the folder supplies the type.**
  So `wiki/items/blue-widget.md` has `id: item-blue-widget` and is linked as
  `[[item-blue-widget]]`. Filename + type prefix = id, always. This one rule removes all
  ambiguity about what a link points at.
- **Internal links use `[[slug]]`** — Obsidian-style wikilinks. Plain text, no tooling
  required, and Obsidian/Foam/etc. will render them as a graph for free if you ever want
  that.
- **A `[[link]]` to a page that doesn't exist yet is a feature.** It's a signal that the
  page is worth creating. Orphan targets are a to-do list, not an error.
- **Backlinks are bidirectional.** When a page links to another, update the other end in
  the same pass. The lint workflow audits this.
- **External identifiers** (a database key, an in-source id, a DOI) go in a frontmatter
  field, not in the slug. The slug stays human-readable; the identifier makes grepping
  the raw layer trivial.
- **Citations** name both the source page and the raw path:
  `[[source-foo-dump]] (per raw/data/foo.xml)`. Every non-obvious claim carries one. If
  two sources support a claim, cite both.

---

## 6. Contradictions are the product

Sources disagree. That's not a defect to be smoothed over — it's often the most valuable
thing the wiki knows.

- **Never overwrite or delete a conflicting claim.** Record both, with citations and
  context.
- Mark them inline with a consistent, greppable marker:
  `> ⚠️ **CONTRADICTION:**` followed by both sides and their sources.
- **Check whether it's really a version/validity difference first.** That resolution is
  itself worth recording.
- **Define a reliability ordering for your domain** and put it in `CLAUDE.md`. E.g.
  primary data > official docs > community sources > a single anecdote. When sources
  conflict, say which side you'd bet on and why — but trusting one side does **not**
  mean deleting the other.

Give `sources/` pages a `reliability` field (`high` / `medium` / `low`) so the ordering
is machine-checkable, and a "Contradictions Flagged" section so each ingest declares
what it found (or says "none").

---

## 7. The three workflows

`CLAUDE.md` should spell these out as numbered procedures. They are the entire operating
surface of the wiki.

### 7.1 Ingest — "ingest raw/x/y.pdf" or "ingest new files"

1. **Read the raw source fully.** With no filename given, find every file in `raw/` with
   no matching page in `wiki/sources/` and process each.
2. **Extract** the entities, facts, relationships, and open questions.
3. **Create the source summary page** in `wiki/sources/` first — it anchors every
   citation from this source.
4. **Create or update the primary content pages.** New from template, or update in place
   (bump `sources`, bump `last_updated`, fill previously-unknown fields, add links).
5. **Create or update the secondary pages** for everything those reference.
6. **Create or update concept pages** for recurring themes that span pages.
7. **Check for contradictions** against what's already there; flag per §6. Check
   version differences first.
8. **Maintain cross-links** — both ends, in the same pass.
9. **Update `index.md`** for every page touched.
10. **Append one entry to `log.md`**: new pages, updated pages, contradictions found.
11. **Report back**: what was created/updated and anything notable.

A large source can touch hundreds of pages. That's expected — batch it, and say in the
log what was covered and what was deferred.

### 7.2 Query — "what happens when…?", "which X require Y?"

1. **Read `index.md` first** to locate relevant pages. Grep `wiki/` for finer lookup.
2. **Read the relevant pages.**
3. **Answer in whatever form fits.** Lead with the answer. Tables for structured facts.
4. **Cite every claim** back to specific wiki pages. If the wiki can't support a claim,
   **say so plainly rather than guessing from training data.** This is the discipline the
   whole method rests on.
5. **State the version / scope** the answer applies to when it matters.
6. **Persist valuable analysis.** If the answer is a reusable synthesis, offer to file it
   as a new `concepts/` page — so the insight compounds instead of vanishing into chat.
   If filed: update `index.md`, `log.md`, and cross-link it.

Step 6 is what makes the wiki grow from *use* rather than only from ingestion, and it's
the step agents most often skip. Call it out explicitly.

### 7.3 Lint — "lint the wiki" (every 5–10 ingests)

Produce a prioritized health report. Make safe fixes; propose the rest.

1. **Contradictions** — scan for conflicts; ensure each is flagged; check for version
   differences.
2. **Stale claims** — info a higher-reliability source has since superseded.
3. **Orphans** — pages with no inbound links; `[[links]]` to pages that don't exist.
   Create, link, or note for deprecation.
4. **Missing pages** — things mentioned in prose but lacking a page.
5. **Cross-reference audit** — links resolve, backlinks bidirectional. Fix.
6. **Consistency** — frontmatter valid, `id` matches slug, enums use allowed values,
   `sources` counts and dates plausible.
7. **Coverage gaps** — which areas are thin, which fields are still `unknown`, what to
   collect next.
8. **Report** the prioritized findings.
9. **Log** a `lint` entry.

---

## 8. `index.md`, `log.md`, `overview.md`

- **`index.md`** — the catalog read at the start of every query. Grouped by page type,
  one row per page:
  `[[slug]] — one-line description | <key field> | Updated: YYYY-MM-DD`.
  Refreshed on every ingest and whenever a query result is filed. Once a section grows
  past a few dozen rows, sub-group it by whatever dimension the domain uses.
  **This file is why the wiki needs no search index** — it's the map the agent loads
  before doing anything else.
- **`log.md`** — append-only, newest at the bottom. Each entry starts with a greppable
  header line: `## [YYYY-MM-DD] <ingest|query|lint|tooling> | <title>`, followed by what
  changed. This is the audit trail, and it's how a future session reconstructs why a page
  says what it says.
- **`overview.md`** — a human-facing snapshot of coverage: what's mapped, what's thin,
  the biggest open questions. Updated during lint or on request. It's a summary, **not** a
  canonical data store — nothing should live only here.

---

## 9. Operating principles (put these verbatim in `CLAUDE.md`)

- **The human curates; the agent does the bookkeeping.** The human's job is choosing
  sources, setting direction, and thinking. Everything else — summarizing, filing,
  cross-referencing, consistency — is the agent's.
- **Never invent facts.** Everything traces to `raw/`. Do not fill gaps with recalled
  knowledge from training data. "Unknown" is a valid and useful value.
- **Numbers are claims too.** A figure without a source is a guess.
- **Atomic pages, dense links.** Small, focused, richly cross-referenced.
- **Contradictions stay visible.** Source disagreement is the product, not a defect.
- **Low friction.** No confirmation steps, no busywork. Make the safe update, report
  clearly, let the human redirect.
- **Disagree when you have grounds to.** If a source looks unreliable, a requested page
  type isn't pulling its weight, or an instruction in this file is producing bad pages
  for this domain, say so plainly and propose the alternative. Silent compliance with a
  bad schema is the most expensive failure available, because it's invisible until the
  wiki is large. Raise it once, clearly; if the human reaffirms, do it their way and
  move on.
- **The dates are real.** Use today's actual date for `last_updated` and log entries, and
  the source's own date where it has one.

---

## 10. Bootstrapping, in order

1. `git init` a new repo. Commit early and often — the git history is the undo button,
   and it's the reason none of this needs a database.
2. Write the one-sentence subject statement.
3. Decide the page types (§3).
4. Write `CLAUDE.md`: subject statement · the two-layer model · directory layout · a
   frontmatter + body spec for each page type · naming and linking rules · contradiction
   policy and reliability ordering · the three workflows · the operating principles.
   **This file is the whole project.** Everything else follows from it.
5. Write one template per page type into `wiki/_templates/`.
6. Create empty `wiki/index.md`, `wiki/log.md`, `wiki/overview.md` with their format
   documented inline at the top.
7. Write `README.md` for the human: how to drop a source in, the phrasings that trigger
   each workflow, and what to expect back.
8. Drop the **first real source** into `raw/` and run an ingest.
9. **Read the output critically — this is the agent's job, not only the human's.** The
   first ingest is where the schema gets debugged. Go back through what you just wrote
   and ask: which fields came out `unknown` on every page and will they *ever* be
   filled? Which sections are empty because the domain has nothing to put there? Did any
   page fight its type — half one thing, half another? Are the links real relationships
   or filler? Report the answers with proposed schema changes, fix `CLAUDE.md`, re-run.
10. Ingest a few more, then lint. Adjust again.

Steps 8–10 are the real design process. Don't over-engineer the schema before any data
has touched it.

---

## 11. Failure modes to watch for

| Symptom | Cause | Fix |
|---|---|---|
| Pages state confident facts no source supports | The agent is answering from training data | Strengthen the "never invent facts" rule; make `unknown` explicit in every enum; spot-check citations |
| Links rot, backlinks one-directional | Cross-linking treated as optional | Make it a numbered step in ingest; audit it in lint |
| `index.md` drifts out of date | Ingest ends at the page writes | Make index + log the last two mandatory steps of every workflow |
| Everything becomes a `concept` page | Page types too narrow or badly chosen | Revisit §3 — the domain nouns are wrong |
| Contradictions silently resolved | Agent defaults to "being helpful" | Explicit rule: never overwrite a conflicting claim; lint hunts for them |
| Wiki grows but is never queried | No feedback loop | Query it deliberately; file the good answers as concept pages (§7.2 step 6) |
| `CLAUDE.md` and reality diverge | Instructions grew stale as tooling changed | Keep detailed tooling specs in separate files read fresh from disk; `CLAUDE.md` points to them and declares them authoritative |

That last row matters once the wiki grows any tooling: `CLAUDE.md` is injected at session
start, so it reflects whatever was true when the session began. A spec file the agent
reads from disk at the moment of use is always current. Keep `CLAUDE.md` as the stable
schema, and push volatile procedural detail into files it points at.

---

## 12. Optional extensions, once it's working

Only after the plain-markdown core is earning its keep:

- **Scripts in `tools/`** that extract structured data from `raw/` deterministically —
  worth it when a source is machine-readable and hand-transcription would be lossy.
  Pair each script with a markdown contract describing its input, output, and pitfalls.
- **Generated views** — HTML pages, JSON, diagrams built from the wiki. Keep the output
  in a sibling of `wiki/`, never inside it, and never hand-edit generated files: fix the
  generator so the fix applies everywhere.
- **Obsidian** opened on the repo, for the graph view and backlink pane. The `[[slug]]`
  convention makes this work with zero configuration.
- **A GitHub remote**, for backup and for reading the wiki from a phone.

None of these are load-bearing. The wiki is the markdown.
