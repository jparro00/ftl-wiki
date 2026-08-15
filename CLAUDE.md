# FTL Event Wiki — Schema & Operating Manual

This repository is a **plain-markdown knowledge base about the events of
_FTL: Faster Than Light_** (Subset Games). Its purpose: map every random event,
event chain, sector, and outcome in the game so that any question — "what does the
giant alien spiders beacon actually do?", "which blue options need Slug crew?",
"what can I get out of the Zoltan research sector?" — has a sourced answer.

It is a [Karpathy-style LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):
the human curates sources and asks questions; the LLM (you, Claude) does the
bookkeeping — summarizing, filing, cross-linking, and keeping everything consistent.

**No apps, no database, no lock-in.** Everything is human-readable markdown the user owns.

> **Your role in one line:** turn raw game data, wiki dumps, and run notes into a
> linked map of events → choices → outcomes, and answer questions with citations
> back to specific pages.

---

## 1. Two layers: `raw/` and `wiki/`

| Layer | Who writes it | Editable? | Contains |
|-------|---------------|-----------|----------|
| `raw/` | The user | **Immutable** — never edit | Original sources, dropped in as-is |
| `wiki/` | **You** | Continuously maintained | Your interpretation: events, chains, sectors, entities, items, concepts, source summaries |

`raw/` is the single source of truth. Every claim in `wiki/` must trace back to a
`raw/` file. The wiki *interprets* the sources; the sources never change.

### Directory layout

```
.
├── CLAUDE.md              ← this file (the schema)
├── README.md              ← how the user operates the wiki
├── raw/                   ← IMMUTABLE source layer (user drops files here)
│   ├── gamedata/          ← datamined game files (events.xml, sector_data.xml, blueprints.xml, …)
│   ├── wiki/              ← community wiki pages, guides, forum/reddit posts
│   ├── modding/          ← research syntheses about the file format and modding (`source_kind: research`)
│   └── runs/              ← the user's own playthrough notes and observations
├── cards/                 ← generated card output — a sibling of `wiki/`, never inside it, so
│   │                        wiki searches never scan machine output
│   ├── card-<slug>.html   ← the built cards
│   └── trees/             ← `<slug>.tree.json`, the extracted event trees
├── sectors/               ← generated sector-profile output — same sibling rule as `cards/`
│   ├── sector-<slug>.html ← the built pages, one per sector
│   └── data/              ← `<slug>.sector.json`, the extracted sector profiles
├── mods/                  ← generated game mods — another sibling of `wiki/`, same reasoning
│   └── <mod-name>/        ← `src/` is the tree that ships; `<mod-name>.ftl` is it zipped
├── tools/                 ← scripts + their contracts (`EVENT-CARD.md` is the card pipeline,
│                            `SECTOR-PAGE.md` the sector-profile pipeline, `EVENT-LABELS.md`
│                            the event-labels mod, `SAVE-WATCH.md` the save watcher that
│                            opens cards by itself); `sector-copy/` is hand-written page copy
└── wiki/                  ← YOUR layer, everything below is maintained by you
    ├── events/            ← one page per event (markdown only; trees live in `cards/trees/`)
    ├── chains/            ← one page per multi-jump event chain / quest
    ├── sectors/           ← one page per sector type
    ├── entities/          ← factions, species, and enemy ships
    ├── items/             ← weapons, drones, augments, systems, crew
    ├── concepts/          ← cross-cutting mechanics and themes
    ├── sources/           ← one summary page per ingested raw source
    ├── _templates/        ← copy-paste starting points for each page type
    ├── index.md           ← the catalog you read first on every query
    ├── log.md             ← append-only chronological activity record
    └── overview.md        ← high-level state of coverage
```

Content directories under `wiki/` are created lazily — the first ingest that needs
`wiki/events/` creates it. Only `_templates/` and the three top-level files exist up front.

---

## 2. Page types & templates

Every page is markdown with YAML frontmatter. Copy the matching file from
`wiki/_templates/` when creating a new page. **One event, chain, sector, entity, item,
concept, or source per page** — atomic pages are easy to link and update without
side effects.

### 2.0 The `version` field — on every page

FTL ships in two meaningfully different forms, and sources disagree constantly about
which one they describe:

- `ae` — Advanced Edition content only (the default modern game)
- `vanilla` — 1.0-era content, cut or changed in AE
- `both` — behaves the same in both
- `unknown` — the source didn't say (a valid, common answer — do not guess)

Version mismatches are the single most common contradiction in this domain. Treat a
source that doesn't state its version as `unknown`, not as AE.

### 2.1 Event page — `wiki/events/<slug>.md`

The heart of the wiki. One per discrete beacon encounter.

```yaml
---
id: event-giant-alien-spiders
type: event
event_name: GIANT_ALIEN_SPIDERS    # in-game event id from events.xml, if known
sectors: [[[sector-rock-homeworlds]]]  # where it can appear ([] if unknown)
beacon_type: distress              # distress | store | nebula | quest | exit | hostile | empty | any | unknown
hostile: false                     # does it start or lead to combat?
blue_options: []                   # equipment/crew that unlocks extra choices
chain: []                          # [[chain-...]] if part of a multi-jump quest
version: unknown                   # ae | vanilla | both | unknown
first_seen: 2026-08-09             # date first appeared in a source
last_updated: 2026-08-09
sources: 0                         # count of raw sources referencing it
tags: [crew-risk]
---
```

`beacon_type: unknown` is for events that occupy **no beacon at all** — tutorials, engine-invoked
combat resolutions, surrender/escape aftermaths loaded from a `<ship>` block, and cut content.
It means "this event does not sit on the map", not "we didn't look".

Body sections (omit a section only if you truly have nothing for it):

```markdown
# Giant Alien Spiders — Distress Beacon

## Summary
One paragraph: what the event is and why it matters to a run.

## Trigger & Where It Appears
Which sectors, which beacon types, any prerequisites.
- Sectors: [[sector-rock-homeworlds]]
- Beacon: distress signal

## Text
The in-game flavor text, quoted, if a source provides it verbatim.

## Choices & Outcomes
A table is usually clearest. One row per choice, with each possible result and its
odds where known:

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Send a crew member | — | Lose crew member (or) gain scrap | unknown |
| 2 | Leave | — | Nothing | 100% |

## Blue Options
- **[[item-...]] / crew requirement** — what it unlocks and why it's better.

## Rewards & Risks
Scrap, fuel, missiles, drone parts, crew, [[item-...]] drops; and what can go wrong.

## Strategy Notes
When to take it, when to skip it. Cited opinions, marked as opinion.

## Related
- [[event-...]] — variant / follow-up / commonly confused with
- [[chain-...]] — the chain this belongs to

## Open Questions
- [ ] What we still need to confirm.

## Sources
- [[source-...]] (per `raw/gamedata/....xml`)
```

### 2.2 Chain page — `wiki/chains/<slug>.md`

One per multi-jump quest line — a thread that spans several events across one or more
sectors (Rock Homeworld quest, Zoltan research facility, the Crystal sector route,
ship-unlock quests). Use when the interesting unit is the *sequence*, not one beacon.

```yaml
---
id: chain-crystal-sector
type: chain
trigger_event: []                  # [[event-...]] that starts it
steps: []                          # ordered [[event-...]] pages
sectors: []                        # [[sector-...]] it runs through
reward: ""                         # short label: ship unlock, augment, crew, …
version: unknown
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 0
tags: []
---
```

Body: Summary · How It Starts · Steps (ordered, each linking `[[event-...]]`) ·
Requirements · Reward · Failure Modes · Strategy Notes · Related · Open Questions · Sources.

### 2.3 Sector page — `wiki/sectors/<slug>.md`

One per sector type. The lens for "what can happen to me here?"

```yaml
---
id: sector-rock-homeworlds
type: sector
sector_class: civilian             # civilian | hostile | nebula | uncharted | special
faction: [[entity-rock-men]]       # dominant faction ([] if none)
version: unknown
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 0
tags: []
---
```

Body: Summary · Character & Hazards · Event Pool (`[[event-...]]` links, the main
payload of this page) · Chains That Run Through It (`[[chain-...]]`) · Factions & Ships
(`[[entity-...]]`) · Strategy Notes · Open Questions · Sources.

### 2.4 Entity page — `wiki/entities/<slug>.md`

Factions, species, and enemy ship types. Frontmatter `entity_kind` distinguishes them.

```yaml
---
id: entity-mantis
type: entity
entity_kind: species               # faction | species | ship
hostility: hostile                 # hostile | neutral | friendly | varies | unknown
version: unknown
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 0
tags: []
---
```

Body: Summary · Traits / Stats · Where They Appear (`[[sector-...]]`) · Events
Involving Them (`[[event-...]]`) · How To Fight / Deal With Them · Related ·
Open Questions · Sources.

### 2.5 Item page — `wiki/items/<slug>.md`

Weapons, drones, augments, systems, and crew types — the things events hand out and
the things blue options require.

```yaml
---
id: item-crystal-vengeance
type: item
item_kind: augment                 # weapon | drone | augment | system | crew | unknown
rarity: unknown                    # 0–5 as in blueprints.xml, or unknown
unlocks_blue: []                   # [[event-...]] where it grants a blue option
version: unknown
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 0
tags: []
---
```

Body: Summary · Stats · How To Get It (`[[event-...]]` / store / chain) ·
Blue Options It Unlocks · Strategy Notes · Related · Open Questions · Sources.

### 2.6 Concept page — `wiki/concepts/<slug>.md`

For mechanics and themes broader than one page: "how blue options work", "scrap
economy", "the rebel fleet advance", "crew-loss risk profile", "AE vs vanilla event
pool differences". Use when a thread spans many events and items but isn't itself one.

```yaml
---
id: concept-blue-options
type: concept
version: unknown
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 0
related_events: []                 # [[event-...]]
tags: []
---
```

Body: Definition & Context · How It Shows Up Across Sources · Where It Applies
(`[[event-...]]` / `[[item-...]]`) · Implications For Play · Related · Open Questions · Sources.

### 2.7 Source summary page — `wiki/sources/<slug>.md`

One per ingested raw file. This is the citation target — every wiki claim points back
through here to the raw file.

```yaml
---
id: source-events-xml-dump
type: source
source_kind: gamedata              # gamedata | wiki | run | research
raw: raw/gamedata/events.xml
game_version: unknown              # what version the source describes
ingested: 2026-08-09               # date you processed it
reliability: high                  # high (game files) | medium (community wiki) | low (single anecdote)
tags: []
---
```

Body: Summary (2–3 sentences) · Key Takeaways (bullets) · Events Covered
(`[[event-...]]`) · Other Pages Touched · Contradictions Flagged (or "none") · Links.

**`source_kind: research`** is for a synthesis written *into* `raw/` by instruction rather than
captured from somewhere — external documentation gathered and summarised into one file. It is
never `high`: it cites sources this repo does not hold, so it inherits their uncertainty. Filing
one as `wiki` would overstate its provenance.

**Reliability convention:** datamined game files outrank the community wiki, which
outranks a single observed run. When they disagree, record all of them (§4) — but say
which one you'd bet on and why.

---

## 3. Naming, IDs, linking, citations

- **Slugs:** lowercase, hyphenated, human-readable. Events: `event-<label>`.
  Chains: `chain-<label>`. Sectors: `sector-<label>`. Entities: `entity-<label>`.
  Items: `item-<label>`. Concepts: `concept-<label>`. Sources: `source-<short-label>`
  (prefix with `<YYYY-MM-DD>-` for run notes, which are dated).
- **Filenames vs ids.** The filename omits the type prefix; the `id` carries it, and the
  folder supplies the type. So `wiki/events/ancient-device.md` has `id: event-ancient-device`
  and is linked as `[[event-ancient-device]]`. Filename + type prefix = id, always.
- **In-game ids** (`GIANT_ALIEN_SPIDERS`) go in the `event_name` field, not the slug —
  the slug stays human-readable. Keeping the in-game id makes grepping `events.xml` trivial.
- **Internal links** use `[[slug]]` (Obsidian-style wikilinks). Link liberally.
  A `[[slug]]` that doesn't exist yet is a valid signal that the page is worth
  creating — treat orphan targets as a to-do, not an error.
- **Backlinks are bidirectional.** If an event page links an item, the item page should
  reference the event. When you add a link, update the other end in the same pass.
- **Citations to raw** use the source page plus the raw path:
  `[[source-events-xml-dump]] (per raw/gamedata/events.xml)`. Every non-obvious claim
  carries a citation. If two sources support a claim, cite both.

---

## 4. Contradictions — first-class, never hidden

Sources about FTL disagree constantly: the community wiki describes AE while a guide
describes 1.0, datamined odds contradict remembered ones, and one player's run is not
a probability distribution. Contradictions are signal, not noise.

- **Never overwrite or delete a conflicting claim.** Record both, with sources and
  version context.
- Mark them inline with `> ⚠️ **CONTRADICTION:**` followed by both sides and their citations.
- Always check whether a contradiction is really a **version difference** (`ae` vs
  `vanilla`) before treating it as an error — that resolution is itself worth recording.
- Where reliability differs, say which side you'd trust: game files > community wiki >
  single run observation. Trusting one side does **not** mean deleting the other.
- The **lint** workflow (§5.3) actively hunts these down and keeps them surfaced.

---

## 5. Workflows

### 5.1 Ingest — "ingest raw/gamedata/events.xml" (or "ingest new files")

1. **Read** the raw source fully. If no filename is given, check `raw/` for files with
   no matching `wiki/sources/` page and process each.
2. **Extract** the events, choices, outcomes, chains, sectors, entities, and items.
3. **Create the source summary** page in `wiki/sources/` (template 2.7). This anchors
   all citations from this source.
4. **Create or update event pages** — the main payload. New page from template, or
   update an existing one (bump `sources`, `last_updated`, fill in previously unknown
   outcomes/odds, add links).
5. **Create or update chain, sector, entity, and item pages** for everything the events
   reference.
6. **Create or update concept pages** for recurring mechanics that span pages.
7. **Check for contradictions** against what's already in the wiki; flag per §4.
   Check version differences first.
8. **Maintain cross-links** — ensure every new/updated page links to related pages and
   its source, and that backlinks exist on both ends.
9. **Update `index.md`** — add/refresh the catalog rows for every page touched.
10. **Append to `log.md`** — one `ingest` entry listing new pages, updated pages, and
    contradictions found.
11. **Report back** to the user: what you created/updated and anything notable (an event
    with unknown odds, a chain that's now fully mapped, a version conflict).

A large source like `events.xml` touches hundreds of pages. That is expected — batch it,
and say in the log what you covered and what you deferred.

### 5.2 Query — "what happens at a Slug distress beacon?", "which events need a Crystal crew member?"

1. **Read `index.md` first** to locate relevant pages. Scale to hundreds of pages
   without any search index; grep `wiki/` if you need finer lookup.
2. **Read the relevant pages.**
3. **Answer** in whatever form fits — prose, a table, a list. Lead with the answer.
   Outcome tables are usually the right shape for event questions.
4. **Cite every claim** back to specific wiki pages (and through them to raw). If the
   wiki can't support a claim, say so plainly rather than guessing from training data —
   *especially* here, where half-remembered FTL trivia is easy to produce and wrong.
5. **State the version** the answer applies to when it matters.
6. **Persist valuable analysis.** If the answer is a reusable synthesis (e.g. "every
   blue option gated behind Zoltan crew", "the full crystal-sector route"), offer to file
   it as a new `wiki/concepts/` page so the insight compounds instead of vanishing into
   chat. If filed, update `index.md` and `log.md` and cross-link it.

### 5.2b Event card — "make me a card for this" (usually with a screenshot)

The user plays paused, screenshots an event, and wants the decision tree fast.

**A screenshot always means build the card.** Never ask, never stop at a chat answer —
including when that event already has a card from earlier in the session.

Cards are **generated from the game XML, never hand-written.** `tools/EVENT-CARD.md` is the
**normative specification** — self-contained, and authoritative over anything below if they
ever disagree. Read it before changing card behaviour. The pipeline is:

```
raw/gamedata/*.xml → cards/trees/<slug>.tree.json → cards/card-<slug>.html → Artifact
                   ▲                              ▲
             extract-event.py                build-card.py + card-vocab.json
```

**Read `tools/EVENT-CARD.md` and follow it.** The commands, the schema, the rendering rules
and the pitfalls live there and only there — deliberately, because this file is injected
into context at session start and can lag the working tree, while the spec is always read
fresh from disk. Where the two disagree, the spec wins.

What stays true regardless, and is why this section exists at all:

1. **Identify the event** — match the on-screen text against `wiki/events/` or
   `raw/gamedata/text_events.xml` to get its `event_name`. That id is the only input the
   pipeline needs.
2. **Build it with the pipeline, and smoke-test before publishing.** Never hand-edit card
   HTML: wording belongs in `tools/card-vocab.json`, a missing or wrong branch belongs in
   `tools/extract-event.py`. Both fixes then apply to every card.
3. **Publish with the Artifact tool** and give the user the URL — for a card they asked
   for. Publishing has its own consent prompt that no permission setting suppresses, so a
   bulk run builds and verifies only and publishes on request. A raw HTML file sent with
   SendUserFile does not render — the card is a fragment the publisher wraps.
4. No citations, ids, version notes or recommendations — on the card or in chat.

### 5.2b-2 Sector page — "what am I flying into?", "show me the Rock homeworlds"

The sector-scale companion to the event card: what a sector must place, its whole event pool
with derived tags, the blue options that pay there, and what can bite. One page per sector,
19 of them, in `sectors/sector-<slug>.html`.

```
raw/gamedata/*.xml  →  sectors/data/<slug>.sector.json  →  sectors/sector-<slug>.html → Artifact
   + cards/trees/*  ▲                                    ▲
              extract-sector.py            build-sector.py + sector-page-render.html
                                                         + tools/sector-copy/<slug>.json
```

**Read `tools/SECTOR-PAGE.md` and follow it** — same reasoning as the card spec: this file is
injected at session start and can lag the working tree, so the spec is authoritative.

What stays true regardless:

1. **Numbers come from the data, never from prose.** A stat tile names a metric id and the
   build fills in the number. Prose names events as `{{EVENT_ID}}` and the build fails if the
   sector cannot produce that event.
2. **Only the copy file is hand-written.** `tools/sector-copy/<slug>.json` holds the words and
   nothing else; the pool, the counts and the tags are all generated.
3. **Open questions stay open on the page.** Whether `OVERRIDE_X` replaces `X`, and whether
   `unique="true"` is per sector or per run, are unresolved in this wiki — the page shows the
   delta and the caveat rather than picking a side.

### 5.2c Save watcher — "start the watcher", "open cards automatically"

The same cards as §5.2b, but the user never has to ask. `tools/save-watch.py` reads the
game's save file, works out which event is on screen, and serves one page that swaps
itself to that event's card. The user parks it on the second monitor; a screenshot request
becomes unnecessary while it runs.

**Read `tools/SAVE-WATCH.md` and follow it** — the commands, the resolution rules and the
failure modes live there, kept out of this file for the same reason as the card spec: this
file is injected at session start and can lag the working tree.

Three things that are easy to get wrong and cost a wasted turn:

1. **It is a server that never returns.** Launch it with Bash `run_in_background: true`.
   A foreground call blocks until timeout and tells you nothing.
2. **Check with `--once` first.** It parses the current save, prints one JSON object and
   exits — that is how you verify the pipeline without starting anything.
3. **Nothing here modifies the game.** It reads `continue.sav` and the installed `ftl.dat`.
   If a question needs a *mod*, that is a different job — and note FTL cannot display HTML
   at all, so no mod can open a card in game.

`status: nosave` means no run is in progress; `ambiguous` and `nocard` are normal, defined
outcomes, not faults. Only a persistent `error` is worth investigating.

### 5.3 Lint — "lint the wiki" (run periodically, e.g. every 5–10 ingests)

Produce a prioritized health report; make safe fixes, propose the rest.

1. **Contradictions** — scan for conflicting outcomes, odds, and requirements; ensure
   each is flagged per §4 and check whether it's really a version difference.
2. **Stale or superseded claims** — flag info a higher-reliability source has since
   overwritten; suggest updates.
3. **Orphans** — pages with no inbound links, and `[[links]]` pointing to pages that
   don't exist yet. Create the missing page, add a link, or note for deprecation.
4. **Missing pages** — events, items, or sectors mentioned in text but lacking a page.
5. **Cross-reference audit** — verify links resolve and backlinks are bidirectional; fix.
6. **Consistency** — frontmatter present and valid; `id` matches slug; `sources` counts
   and `last_updated` dates look right; `version`, `beacon_type`, `entity_kind`,
   `item_kind`, `reliability` use allowed values.
7. **Coverage gaps** — which sectors have thin event pools, which events have unknown
   odds or unmapped blue options, which chains are missing steps. Suggest what to
   datamine or play to fill them.
8. **Report** the prioritized findings to the user.
9. **Log** a `lint` entry in `log.md`.

---

## 6. `index.md` and `log.md`

- **`index.md`** — the catalog you read at the start of every query. Grouped by type
  (Events, Chains, Sectors, Entities, Items, Concepts, Sources). One row per page:
  `[[slug]] — one-line description | key field | Updated: YYYY-MM-DD`. Refresh it on
  every ingest and whenever you file a query result. See the file for the row format.
  Once the event list grows past a few dozen, group the Events section by sector.
- **`log.md`** — append-only, newest at the bottom. Each entry starts
  `## [YYYY-MM-DD] <ingest|query|lint|tooling> | <title>` so entries are greppable
  (`tooling` covers changes to `tools/` — extractors, the card pipeline), followed by
  what changed. See the file for the format.

`overview.md` is a human-facing snapshot of coverage (what's mapped, what's thin, the
biggest open questions). Update it during lint or when the user asks — it's a summary,
not a canonical data store.

---

## 7. Operating principles

- **The user curates; you do the bookkeeping.** Their job is choosing sources, setting
  direction, and thinking. Your job is everything else: summarizing, filing,
  cross-referencing, keeping it consistent.
- **Never invent facts.** Everything traces to `raw/`. Do not fill gaps with recalled
  FTL knowledge from training data — if no source says it, the answer is "unknown",
  which is a valid and useful value.
- **Odds are claims too.** A percentage without a source is a guess. Mark it `unknown`
  rather than inventing a plausible number.
- **Atomic pages, dense links.** Small focused pages, richly cross-referenced.
- **Contradictions stay visible.** Version drift and source disagreement are the
  product, not a defect.
- **Low friction.** Don't add confirmation steps or busywork. Make the safe update,
  report clearly, and let the user redirect.
- **The dates are real.** Use today's date for `ingested:` / `last_updated:` / log
  entries, and the source's own date where it has one.
