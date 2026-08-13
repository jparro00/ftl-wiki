# FTL Event Wiki

A plain-markdown knowledge base about the events of **FTL: Faster Than Light** — every
beacon encounter, choice, outcome, blue option, quest chain, and sector event pool.
You own every file — no apps, no database, no vector store, no lock-in. You feed it
sources and ask Claude questions; Claude keeps the event map organized and cited.

It follows Andrej Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
method. The full schema and conventions live in **[`CLAUDE.md`](./CLAUDE.md)** — that
file tells Claude how to behave. This README is the quick operator's guide.

## The two layers

- **`raw/`** — you drop sources here. Never edited. The source of truth.
  - `raw/gamedata/` — datamined game files (`events.xml`, `sector_data.xml`, `blueprints.xml`, …)
  - `raw/wiki/` — community wiki pages, guides, forum and reddit posts
  - `raw/runs/` — your own playthrough notes and observations
- **`wiki/`** — Claude maintains this: a page per event (`events/`), per quest chain
  (`chains/`), per sector (`sectors/`), per faction/species/ship (`entities/`), per
  weapon/drone/augment/system (`items/`), per mechanic (`concepts/`), and a summary per
  source (`sources/`), tied together by [`index.md`](./wiki/index.md) and
  [`log.md`](./wiki/log.md).

## How you use it

### Drop in a source
Save the file into the right `raw/` subfolder with a descriptive name, e.g.
`raw/gamedata/events.xml`, `raw/wiki/rock-homeworlds-page.md`,
`raw/runs/2026-08-09-kestrel-run.md`. Any text format is fine — paste the XML, the
wiki page, or your notes.

### Ingest it
Tell Claude:
> **"Ingest `raw/gamedata/events.xml`"**
> or just **"Ingest the new files in raw/"**

Claude reads it, writes a source summary, creates/updates the event, chain, sector,
entity, and item pages it covers, flags contradictions with what's already known,
updates the index and log, and reports what changed.

### Query it
Ask questions in plain English:
> - "What are all the outcomes of the giant alien spiders event?"
> - "Which blue options need a Slug crew member?"
> - "What can appear at a distress beacon in the Rock Homeworlds?"
> - "Walk me through the full crystal sector route."
> - "Which events can cost me a crew member with no warning?"

Claude reads the index, pulls the relevant pages, and answers **with citations** back
to specific wiki pages and raw sources. If an answer is a reusable analysis, ask
Claude to **file it** as a concept page so it sticks.

### Get a card for what's on screen
Pause the game, photograph or screenshot the event, and send it. No words needed —
a screenshot means "build me the card."

Claude identifies the event, generates its decision tree straight from the game files,
and hands you a link: every choice, every random outcome, every blue option, expandable,
colour-coded, readable on a phone in a couple of seconds. No advice, no spoiler-y
recommendations — just what each option does.

Cards are **generated, never hand-written**: `raw/gamedata/*.xml` →
`cards/trees/<slug>.tree.json` → `cards/card-<slug>.html`. Every built card is kept in
`cards/`, one file per event, so a card's link stays stable when it is rebuilt. Quoted text is verbatim from the game's own
string table, and no odds appear unless the files publish them. The pipeline and its
schema are documented in [`tools/EVENT-CARD.md`](./tools/EVENT-CARD.md); the grammar it
relies on is [[concept-event-tree-grammar]].

### Lint it
Every so often (say, every handful of ingests):
> **"Lint the wiki."**

Claude checks for contradictions, superseded claims, orphan/missing pages, broken
cross-links, and coverage gaps, then hands you a prioritized to-do list. This is where
version drift and half-mapped quest chains get caught.

## Conventions worth knowing

- **Everything is cited.** Claims trace back to a `raw/` file through a `sources/` page.
  Claude will not fill gaps from memory — unsourced means **unknown**.
- **Version matters.** Every page carries `version: ae | vanilla | both | unknown`.
  Advanced Edition changed the event pool substantially, and most source disagreements
  turn out to be version differences.
- **Reliability is ranked.** Datamined game files > community wiki > a single observed
  run. When sources disagree, both are recorded, with a note on which to trust.
- **Contradictions are kept, not resolved.** Two sources claiming different outcomes
  both stay on the page, dated and cited.
- **Odds without a source stay `unknown`.** No invented percentages.
- **Links use `[[slug]]`.** Opens cleanly in [Obsidian](https://obsidian.md) if you want
  a graph view, but it's just markdown — any editor works.

## Optional
The wiki is plain files, so `git init` here gives you version history and lets you see
exactly what Claude changed on each ingest. Not required.

## Where things are
```
CLAUDE.md            ← the schema (how Claude operates this wiki)
README.md            ← you are here
raw/{gamedata,wiki,runs}/   ← your sources go here
cards/               ← generated: card-<slug>.html, plus trees/<slug>.tree.json
tools/               ← scripts: event extraction, card building, source pulls
wiki/events/         ← one page per beacon encounter (markdown only)
wiki/chains/         ← multi-jump quest lines
wiki/sectors/        ← sector types and their event pools
wiki/entities/       ← factions, species, enemy ships
wiki/items/          ← weapons, drones, augments, systems, crew
wiki/concepts/       ← mechanics and cross-cutting themes
wiki/sources/        ← one summary per ingested source
wiki/_templates/     ← copy-paste starting points
wiki/index.md        ← the catalog
wiki/log.md          ← activity history
wiki/overview.md     ← coverage at a glance
```
