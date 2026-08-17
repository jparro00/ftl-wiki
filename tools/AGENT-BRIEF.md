# Agent brief — build FTL event pages

You are writing wiki pages for one batch of FTL events. Read this, then your batch file.

## Inputs

- **Batch file** (given in your prompt): JSON, `{EVENT_ID: {...}}`. This is your **work
  list and join map**: `file`, `sectors[]` (wiki slugs), `lists[]`, `unique`, `orphan`,
  `wiki_pages[]`, `wiki_mentions[]`.

  > ⚠️ Its parsed `text` / `choices[]` / `effects[]` / `sub_events{}` are a **lossy
  > preview** — they drop nested choices, deeper sub-event trees, `autoReward` payload
  > types (`standard` / `weapon` / `stuff`), and some `req` gates. Never build a page
  > from them alone.

- **The game XML is the source of truth.** For each event, read its definition in
  `raw/gamedata/<file>` (the `file` field), plus `raw/gamedata/events_ships.xml` for any
  enemy ship it references and `raw/gamedata/text_events.xml` for prose. Follow
  `load=` references to their targets.
- **Fandom pages**: `raw/wiki/<file>.md`.
  - `wiki_pages[]` = **authoritative**. That page declares this event's id in its Notes
    ("called \"X\" in the datafiles"). Read every one; this is where odds, rewards and
    strategy live.
  - `wiki_mentions[]` = **incidental, not a source for this event.** FTL reuses event ids
    as enemy-ship ids, so these are usually other events' pages that merely fight this
    ship. Ignore unless you verify otherwise; never cite one as this event's source.
- **Template**: `wiki/_templates/event.md`. **Schema**: `CLAUDE.md` §2.1, §3, §4.
- **Reference page** — match this depth and tone: `wiki/events/ancient-device.md`.

**Every path in this brief is relative to the repository root.** The orchestrator gives
you that root; it is wherever this repo is checked out, and is not a fixed location.

## Output

One file per event: `wiki/events/<slug>.md`.

- **Slug**: the Fandom page title slugified (lowercase, hyphens) when a page joins;
  otherwise the event id lowercased with `_`→`-`. `id:` = `event-<slug>`.
  Filename omits the `event-` prefix; the id keeps it.
- **Never overwrite an existing file.** If the slug is taken by a *different* event,
  append a discriminator (`-rock`, `-slug`). If it's the same event, skip it and say so.
- Set `event_name:` to the exact in-game id. This is the join key — always fill it.
- **`version:`** — `ae` means *Advanced Edition only*, not *extracted from the AE build*.
  Use `ae` for events in `dlcEvents*.xml` or reachable only via an `OVERRIDE_*` list;
  `both` for base-file events with no DLC markers. A base event with `<!--DLC-->`-wrapped
  tags is `both`, with the vanilla difference written up in-body.
- `sources:` = number of raw sources you actually used.

## Rules

1. **Never invent.** No odds, rewards, or mechanics that no source states. `unknown` is
   the correct answer. Do not fill gaps from your own FTL knowledge.
2. **Cite everything non-obvious.** Game data → `[[source-events-xml]]` /
   `[[source-text-events-xml]]`; sector facts → `[[source-sector-data-xml]]`; Fandom →
   create/cite `[[source-fandom-<slug>]]`.
3. **Source pages**: for each Fandom page you use, create `wiki/sources/fandom-<slug>.md`
   (`source_kind: wiki`, `reliability: medium`, `game_version: unknown`) if absent.
   Game-XML source pages **already exist** for every file in `raw/gamedata/` — cite them
   as `[[source-events-rock]]`, `[[source-events-ships]]`, `[[source-blueprints]]`,
   `[[source-text-blueprints]]`, etc. (filename minus `.xml`, `_`→`-`). Don't create them,
   and don't cite a bare raw path when the source page exists.
4. **Contradictions are kept, not resolved.** Where the game files and Fandom disagree
   (wording, rewards, requirements), record both with `> ⚠️ **CONTRADICTION:**`, cite each
   side, and say which you'd trust — game files (`high`) beat Fandom (`medium`). Check
   first whether it's an AE-vs-vanilla difference.
5. **Blue options**: `req="X"` on a choice is the gate. Name what it needs (crew species,
   system, augment) and what it unlocks.
6. **Sub-events** (`sub_events`, and any `loads` target): document as outcomes **inside**
   the parent page. They do not get their own pages.
7. **Effects**: `effects[]` holds the mechanical payload (`autoReward`, `crewMember`,
   `damage`, `augment`, `ship`, …). Translate it into the Outcome column. `autoReward`
   levels (`LOW`/`MED`/`HIGH`) are the game's own words — quote them, don't convert to numbers.
8. **Text that "varies"**: `[varies: textList X]` means the prose is drawn from a list.
   Say so rather than quoting one variant.
9. **Odds you may legitimately derive.** When a choice loads an `<eventList>`, the members
   are the outcome pool. If an entry is duplicated, state the weighting as a fraction
   (`ROCK_ATHIEST_GOOD` appears twice in a 3-member list → 2/3) and **say explicitly that
   it assumes uniform selection across list entries**. This is derivation from the data,
   not invention — it is the one case where a number without a stated percentage is
   allowed. Everything else stays `unknown`.
10. **Version differences are findable.** A tag or branch wrapped in `<!--DLC-->` inside a
   base event file is Advanced Edition content, so the vanilla behaviour is the event
   *without* it. When you find one, record both editions and set `version` accordingly
   rather than defaulting to `ae`. Cross-check `dlcEventsOverwrite.xml`: if it redefines a
   list your event belongs to, the AE and vanilla pools differ.
9. **Cross-link liberally**: `[[sector-...]]` slugs are given in `sectors[]`.
   Link `[[item-...]]`, `[[entity-...]]`, `[[chain-...]]` freely — targets that don't
   exist yet are valid to-dos, not errors.

## Orphans (`"orphan": true`)

Not reachable from any sector's event lists. Classify:

- **Test/dev stub** (`*_TEST`, `DUMMY`, `DEMO_*`, placeholder prose like "Oh no enemies!"):
  **no page.** List it in your report.
- **System message** (`AUGMENT_FULL`, `EQUIP_FULL`, `CASH_IN_DRONE` — UI text, not an
  encounter): **no page.** List it in your report.
- **Real event reached another way** (quest marker, fleet pursuit, boss sequence — e.g.
  `CRYSTAL_UNLOCK`, `BOSS_TEXT_*`, `ENGI_UNLOCK_3`): **make a page**, set
  `beacon_type: quest` (or `unknown`), and note in *Trigger* that it is not in any sector
  event list and how it is actually reached.
- **Complete but unreachable content** — fully authored (prose, choices, rewards) but in
  no live list, or its only list entry is commented out: **make a page**, tag it
  `unreachable` (add `cut-content` if a dev note suggests it was pulled), and document the
  disabled reference in *Trigger*. Do not silently drop shipped content; do not present it
  as playable either.

  > ⚠️ **`unreachable` needs positive evidence**: a commented-out sole reference, or no
  > reference anywhere in `raw/gamedata/`. A list having no `sector_data.xml` allocation is
  > **not** sufficient — `NEUTRAL_EXIT` and `FEDERATION_BASE_ASSIST` have zero allocations
  > and are plainly live (the engine calls some lists by name). In that case set
  > `sectors: []`, add an open question, and cite
  > [[concept-sector-event-allocation]] — do not tag `unreachable`.

**Surrender / aftermath events** loaded from a ship block in `events_ships.xml` (not from
the parent's `loads`) **do get their own pages** — they carry their own `event_name` join
key, and folding them in would lose it. Cross-link parent ↔ aftermath both ways.

## Do not touch

`index.md`, `log.md`, `overview.md`, anything in `raw/`, other agents' event pages, or
existing pages you didn't create. The orchestrator updates the catalog afterwards.

## Report back

Return only: pages created (slug — event id), pages skipped and why, source pages
created, contradictions flagged, and anything that needs a human decision. Keep it terse.
