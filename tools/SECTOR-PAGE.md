# Sector pages — specification

Normative spec for the FTL sector-profile pipeline. It is self-contained: an agent with no
prior context can build, verify and extend a sector page from this document alone.

> **A redesign is agreed but not implemented.** `tools/SECTOR-PAGE-REDESIGN.md` is the delta:
> it was reviewed to completion on Federation Space (mock at
> `sectors/sector-federation-space-mock.html`) and changes the page order, the glance blocks,
> the budget and the footnotes. This document still describes what the pipeline *builds today*
> and stays normative until the rollout lands. Read both before changing a sector page.

A **sector page** is a single-page, self-contained HTML profile of one FTL sector — what it
must place, everything it can throw at you, and what is worth having when you fly in. Where
an event card (`tools/EVENT-CARD.md`) answers *"what do I pick right now?"*, a sector page
answers *"what am I flying into, and what should I be ready for?"*

Sector pages are **generated**. No number and no event name is ever typed into HTML.

---

## 1. Quick start

```bash
python tools/extract-sector.py ENGI_HOME            # → sectors/data/engi-homeworlds.sector.json
# write tools/sector-copy/engi-homeworlds.json      # → the words, and only the words (§5)
python tools/build-sector.py engi-homeworlds        # → sectors/sector-engi-homeworlds.html
python tools/smoke-sector.py sectors/sector-engi-homeworlds.html
```

`--all` works on both scripts. The **sector id is the only input** to extraction; find it in
`raw/gamedata/sector_data.xml` or read `sector_id:` off `wiki/sectors/<slug>.md`. The slug
comes from the join in §4.6 — use the path the extractor prints rather than assuming one.

---

## 2. Components

| Path | Role | Hand-written? |
|---|---|---|
| `tools/extract-sector.py` | game XML + event trees → `ftl-sector-profile/1` JSON | code only |
| `tools/build-sector.py` | data + copy → the page | code only |
| `tools/sector-page-render.html` | layout, colour, type | design only — **no English** |
| `tools/sector-vocab.json` | every word the renderer emits that is not from the data | yes, shared by all pages |
| `tools/card-vocab.json` | read for `gate_labels` only — blue-option names, shared with the card pipeline | yes, but it belongs to `EVENT-CARD.md` |
| `tools/sector-copy/<slug>.json` | the words for one sector | **yes — this is the authoring surface** |
| `tools/sector-cards.js` | the loader that opens a beacon box onto its card (§6.1) | code only — **no English, no paths** |
| `tools/sector-toggle.js` | makes the blue-options box toggle from anywhere in the box, not only its summary | code only — **no English, no paths** |
| `tools/smoke-sector.py` | renders a built page as text and checks it | code only |
| `tools/smoke-inline.py` | drives a built page in a real browser and checks the boxes open | code only |
| `sectors/data/<slug>.sector.json` | generated profile (regenerable data, not a page) | never |
| `sectors/sector-<slug>.html` | the built page; publish target | never |

Inputs consumed:

- `raw/gamedata/sector_data.xml` — the allocation table: every count on a page comes from here
- `raw/gamedata/events*.xml`, `newEvents.xml`, `dlcEvents*.xml` — event-list membership
- `raw/gamedata/text_sectorname.xml` — the sector's in-game display name
- `raw/gamedata/blueprints.xml` + `dlcBlueprints.xml` + `text_blueprints.xml` — names, base
  `<rarity>`, and which ids are `crewBlueprint`s, for the rarity block (§4.3b)
- `cards/trees/*.tree.json` — **every per-event tag, gate, item and crew fact** (§4.3)
- `wiki/sectors/*.md` — the `sector_id:` → (slug, title) join (§4.6)

The event trees are a hard dependency: a sector page describes its pool by reading the cards
that already exist for those events. If an event has no tree, build it first
(`python tools/extract-event.py <ID>`) — as of this writing all 19 sectors are fully covered.

---

## 3. Invariants

These hold for every sector page. Breaking one is a bug, not a preference.

- **S1 — Numbers come from the data, never from the copy.** A stat tile names a *metric id*
  and supplies a label; `build-sector.py` fills in the number. There is no way to type a
  number into a tile, and that is deliberate.
- **S2 — Prose names events by id, not by title.** Copy writes `{{ENGI_VIRUS}}`; the renderer
  resolves the title. An id the sector cannot produce **fails the build**, so a page can never
  mention an event that is not in its pool.
- **S3 — Tags are derived, never asserted.** `fight` means the event's tree has combat at its
  root; `may-fight` means combat exists below a choice. Read from the tree, not from which
  list the event sits in.
- **S4 — No invented odds.** The shipped event lists carry no weights (EVENT-CARD.md I2), so
  no pool row gets a percentage. A list that names the same event twice is `×2` — that
  repetition is the only weight the files contain.
- **S5 — Open questions stay open.** Where the data does not say (does `OVERRIDE_X` replace
  `X`? is `unique` per sector or per run?), the page states the uncertainty rather than
  picking a side silently. §4.4 and §4.5.
- **S6 — No hand-edited HTML.** See §8 for where each class of fix belongs.
- **S7 — Deterministic.** Same inputs → byte-identical output.

---

## 4. Stage 1 — extraction

`extract-sector.py` resolves one `<sectorDescription>` into a profile.

### 4.1 The allocation table

Each `<event name= min= max=/>` inside a `sectorDescription` is one **entry**: a list (or a
single event) the sector must place between `min` and `max` times. Summing them gives the
beacon spread. Entries commented out in the XML are *not* entries — the parser drops comments
for exactly this reason, and Rock Controlled and the Civilian Sector both have one.

An entry name resolves to an `eventList` or to a single `<event>`. Three names
(`BOARDERS_PIRATE`, `NEBULA_PIRATE`, `NEBULA_REBEL`) are defined as **both**, in different
files. The extractor reads them as the list and marks the entry `ambiguous`; the page carries
a footnote saying so.

### 4.1b Placement order — the table is a queue, not a shopping list

The allocation table does not describe the map; it describes a *filling process*, and the
order of its lines is load-bearing. Per `raw/wiki/sectors.md` (which cites the community's
reverse-engineering of the generator, not the game files):

- Beacons are placed **first** — a 6×4 grid, each cell 80% likely to hold one, so **at most
  24**. The community wiki states a floor of 19; nothing else here derives it, so `at_risk`
  is computed against the ceiling only and the floor is carried as data.
- Lines are then filled **in sector-definition order**. Each line rolls its own min–max
  inclusive and is filled completely before the next begins.
- **When the beacons run out, generation stops.** A line near the bottom of the table can
  receive nothing at all. This is why stores and named set-pieces sit at the top of every
  definition, and why bottom-of-list uniques are rare.
- **Every nebula list is processed first**, out of file order, because the cloud graphics have
  to be drawn before anything else. A cloud drawn over an ordinary beacon converts it, and
  that beacon draws from the shared `NEBULA` list. Fandom words the rule as "starts with
  `NEBULA_`", but the reason it gives applies equally to the bare `NEBULA` line, and its own
  ordered listing for the starting sector puts that line first — seventh in `sector_data.xml`,
  first in the listing. The extractor therefore treats bare `NEBULA` as nebula-first too,
  which affects Federation Space and the Civilian Sector.
- Beacons still empty at the end are filled from `NEUTRAL` (`OVERRIDE_NEUTRAL` under AE).
  This is not a line in the file — the engine reaches the list by name, and the game files
  say so themselves: the comment on both list definitions reads *"This event list is
  hardcoded to fill out a sector if it ran out of all other calls for that sector"*
  (`newEvents.xml`, `dlcEventsOverwrite.xml:139`). Those beacons are as real as allocated
  ones, so `generation.fallback_beacons` sizes them and the budget renders them as a
  marked, unnumbered row (§4.1b-2, §6 item 4).
- The **exit beacon is not in the table** — it draws from a shared `EXIT_LIST`, and an exit
  inside a cloud is always empty.

So `entries` is kept in **file order** and carries `placement` (`position`, `nebula_first`,
`before_min`, `before_max`, `at_risk`). An entry is `at_risk` when the lines placed before it
could, at their maxima, consume all 24 beacons — a possibility, not a prediction. The
`generation` block carries the totals and `can_exhaust_map`.

Sorting entries into reading order — which this extractor originally did — throws that away.
The budget section renders placement order; only the pool sections re-sort for reading.

> Worth knowing: the Fandom page states outright that it does **not** reflect the real file
> order. `sector_data.xml` does, so these pages can show a placement order the community wiki
> cannot.

### 4.1b-2 The fill-in line — the beacons the table does not account for

A budget that stops at the table understates the map, sometimes badly: whatever the table
does not allocate, `NEUTRAL` fills. `generation.fallback_beacons` sizes that gap, in beacons:

| Field | Definition | Reads as |
|---|---|---|
| `max` | `GRID_BEACONS − Σ min`, clamped at 0 | most the fallback can ever fill here |
| `min` | `GRID_BEACONS_MIN − Σ max`, clamped at 0 | what it fills even on the worst roll |
| `on_full_map` | `GRID_BEACONS − Σ max`, clamped at 0 | what it must fill when the grid rolls 24 |

The clamp is the whole point at both ends. The Hidden Crystal Worlds allocates 25
minimum against a 24-beacon ceiling, so its `max` is **0** — that sector can never reach the
fallback, and its row is a zero row. The Last Stand is the opposite: it allocates
at most 20, so `on_full_map` is **4** and the fallback is guaranteed on a full map. Every
other sector sits between, `min` 0 and `max` positive.

`min` is 0 for all 19 shipped sectors. It is computed rather than hardcoded because a mod
can allocate less than a small map holds, and then the fallback is not optional.

Two things this row is **not**: it is not the `NEBULA` filler (a cloud drawn over an ordinary
beacon converts it and it draws from `NEBULA` — a different list, a different cause), and it
is not the exit beacon (`EXIT_LIST`, outside the table entirely). Both are stated separately
in the generation notes so the three cannot be conflated.

### 4.1c Beacon markers — what the map shows before you jump

`<distressBeacon/>` on an event is what puts a distress marker on the sector map, and
`<store/>` marks a store. **Neither set matches the allocation entry of the same name**, which
is the single most useful thing this pipeline can tell a player:

- Events carrying the distress tag that are allocated from *other* lists still show the
  marker. `ASTEROID_DERELICT_SHIP` — the Damaged Stasis Pod — is allocated from `NEUTRAL_*`
  and shows as distress, so a sector can show more distress beacons than its distress count.
  Fandom names this exact event as its example.

  > ⚠️ Fandom explains it by saying the neutral line is filled *before* the distress line.
  > That is wrong for the sectors it applies to: in `ENGI_HOME`, `ENGI_SECTOR` and both Rock
  > sectors, `sector_data.xml` places the distress line first. The *outcome* holds — the tag
  > shows the marker wherever the event lands — but the mechanism does not, so the renderer
  > derives the before/after clause per sector rather than asserting Fandom's version.
- The reverse also happens: events allocated from a `DISTRESS_BEACON_*` list that carry no
  distress tag, and so never show the marker. Fandom calls these a mistake in the data.

`rollup.markers` carries both directions (`events`, `marked_outside_allocation`,
`allocated_but_unmarked`), plus store-marked events and an environment breakdown.

### 4.2 Sections

A section is read off the entry name, which is highly regular across all 19 sectors:
`HOSTILE*` → hostile, `BOARDERS*` → boarders, `NEUTRAL*` → neutral, `DISTRESS_BEACON*` →
distress, `ITEM*` → items, `STORE*` → store, `QUESTS*` → quests, `NOTHING*`/`NEBULA_EMPTY` →
empty, `NEBULA*`/`STORM*` → nebula.

Anything unmatched falls through to **special**, which sorts first — an unrecognised name is
a named one-off beacon (`ENGI_UNLOCK_1`, `ROCK_UNLOCK1`, `FLAGSHIP_CONSTRUCTION`,
`MANTIS_NAMED_THIEF`, `ZOLTAN_PEACE_QUEST`), and those are what lead a page.

### 4.3 Per-event facts

Every event in a pool is looked up in `cards/trees/<slug>.tree.json` by its id, and the tree
is walked — including its `chain[]`, so a multi-stage unlock is visible whole. Derived:

| Tag | Means |
|---|---|
| `fight` | the tree's root node is `combat` — arriving starts a fight |
| `may-fight` | a `combat` node exists deeper, behind a choice |
| `boarders` | a `boarders` effect anywhere |
| `crew` / `crew-loss` | `crew_gain` / `crew_loss`; a **negative** `crew_gain` is a loss, not a gain |
| `store` / `quest` / `reward` / `cost` | a store opens; a quest marker is planted; something is gained; something is spent |
| `unique` | the event's own `unique="true"` |

Also collected per event and rolled up per sector: gates (blue options, with levels), named
items, crew classes, boarder counts, quest targets and `unlockShip` ids.

**`rollup.gates` is keyed by the name a player sees, not by `req`.** A gate's `req` may name a
`blueprintList` (`WEAPONS_ION`, `COMBAT_BEAM_DRONE_LIST`), and a list has no `<title>` in the
game files, so the label is authored in `card-vocab.json`'s `gate_labels` — the same map the
card runtime uses, so an option reads identically on a card and on a sector page. Two reqs that
resolve to one label merge into one row with the union of their events, and every id that
merged in is kept in `reqs`. `WEAPONS_MISSILES` and `WEAPONS_MISSILES_EVENTS` are the case that
forces this: identical seven-weapon lists, the second being the AE file's redefinition of the
first, which would otherwise render as "Missile weapon" twice.

### 4.3b Rarity as a delta — `crew_rarity`

Each `<rarityList>` entry carries the sector's value **and** the blueprint's base `<rarity>`
from `blueprints.xml` / `dlcBlueprints.xml`, plus:

- `crew` — whether the id is a `crewBlueprint`. That element is the only thing in the files
  that separates a hireable species from any other blueprint in the same list.
- `change` — `unlocked` · `excluded` · `more-common` · `rarer` · `same` · `unknown`.

The verdict exists because the scale is not linear: `0` is a flag meaning "not in the random
pool", not the low end of 1–5 (`wiki/concepts/blueprint-rarity.md`). A signed delta would call
base 2 → 0 and base 0 → 2 the same size of change when they are opposites. A blueprint with no
`<rarity>` of its own answers `unknown` and is never guessed at.

**`fleet_delay` is signed, and the name is misleading.** It carries `modifyPursuit` verbatim:
**negative delays the fleet (good for you), positive advances it (bad)**. `AUTO_WARNING`'s
escape branch is `fleet_delay: 1` — the scout reporting your position, not a reprieve. Read
the sign before writing a sentence about it (EVENT-CARD.md §6 records the same trap).

### 4.3c Store crew odds — `crew_store_odds`

The one place these pages state a probability, and the only reason they may is that the
rule is read out of the game binary rather than inferred
(`raw/modding/2026-08-16-store-crew-selection-disassembly.md`, and
`wiki/concepts/blueprint-rarity.md`):

- **Candidates** = every `crewBlueprint` whose *effective* rarity is non-zero. Effective
  rarity is the sector's value where its `rarityList` names the species and the blueprint's
  base otherwise — `ResetRarities()` restores base on sector entry and `SetRarity()` writes
  only listed names, so **unlisted keeps base**. This is why the six sectors with no
  `rarityList` still get a full block.
- **Weight** = `6 − rarity`. `CREW_WEIGHT_BASE` in the extractor.
- **`share`** = `weight ÷ Σweights`, the per-slot probability.
- **`in_store`** = `1 − (1 − share)³`, the chance of at least one across the three slots.
  Three is `CREW_SLOTS`, the **Advanced Edition** count — all three hireable. Vanilla rolls
  two or three, and these pages are AE data, so the page says which it means.

Each slot is an independent `count = 1` draw, so a store can offer the same species twice.
That is not true of weapons, drones or augments, which are drawn without replacement in a
single call — noted here because it is a trap for anyone extending this block to items.

**S4 still holds.** No *beacon* gets a percentage; this is a store's internal roll, and its
provenance is stated on the block itself.

### 4.4 AE override lists — a delta, never a merge

`dlcEventsOverwrite.xml` defines twelve `OVERRIDE_<LIST>` twins. **Whether the engine
substitutes them is an open question** — see `wiki/concepts/sector-event-allocation.md`. So
the extractor never merges one into a pool. It emits the *difference* (`added`, `removed`,
`applies: "unconfirmed"`), and the renderer shows it as a separate marked block under the
entry it belongs to, with the uncertainty stated.

### 4.5 `unique` is not settled either

`unique="true"` is the files' own attribute. Whether its scope is once per sector or once per
run is contradicted between sources (`wiki/concepts/event-uniqueness.md`; the wiki's better
bet is **per sector**). The tag says only "Unique"; a standing footnote carries the scope
question. Do not resolve it in copy.

### 4.6 Title and slug

From the same kind of join the event pipeline uses: each `wiki/sectors/*.md` declares
`sector_id:` and has an H1. The filename is the slug, the H1 is the title. A page listing
several ids (`vestigial-definitions.md`) documents no single sector and is skipped — which is
why `DEEP_SPACE_SECTOR` and `ABANDONED_SECTOR` get no page.

### 4.7 Metrics

Every number a stat tile may show is precomputed under `metrics`:

- `beacons_min`, `beacons_max` — the allocation totals, **not** the map size
- `grid_beacons` (24, the map ceiling), `at_risk_entries`
- `distinct_events`, `always_fight_events`, `may_fight_events`, `crew_loss_events`,
  `crew_gain_events`, `boarder_events`, `unique_events`, `gated_events`, `quest_start_events`
- `blue_options` (distinct options after the label merge), `blue_option_hits` (events offering
  one, summed — an event gated twice by different options counts in both)
- `store_rarity_changes`, `crew_rarity_changes` — entries this sector moves off base rarity
- `crew_types_sold` — species a store here can offer (§4.3c)
- `section:<name>:min` / `:max` — e.g. `section:hostile:min`
- `entry:<NAME>:min` / `:max` — e.g. `entry:STORE_ENGI:max`

---

## 5. The copy file — the only thing written by hand

`tools/sector-copy/<slug>.json`. Unknown keys are rejected; every constraint below is enforced
by `build-sector.py`, so a violation is a build failure, not a review note.

```jsonc
{
  "slug": "engi-homeworlds",          // must match the data file

  "lede": "…",                        // required. 2–3 sentences: what this sector *is*
                                      // to a run. The one place a point of view belongs.

  "stats": [                          // required, 3–5 tiles
    { "metric": "beacons_min..beacons_max", "label": "Beacon spread" }
  ],                                  // metric: one id from §4.7, or "a..b" for a range

  "callout": "…",                     // optional. One boxed note under the budget —
                                      // best used to contrast this sector with its sibling.

  "section_notes": {                  // optional, keyed by entry name
    "HOSTILE_ENGI": "…"               // one line under that pool
  },

  "chain": {                          // optional. Only where a real multi-jump quest starts here.
    "title": "Stealth Cruiser · The Nesasio",
    "steps": [
      { "marker": "1", "title": "…", "detail": "…", "ref": "ENGI_UNLOCK_1" }
    ]                                 // marker: "1","2","3","✓" — last step renders green.
  },                                  // ref: free text, shown in mono. Not resolved, so it may
                                      // name events outside the pool (later quest stages).

  "panels": [                         // required, 2–4. The two generated blocks (§6.2) are
    {                                 // not panels and take no copy — do not write one.
      "title": "Blue options that pay here",
      "items": [                      // 2–6 per panel
        { "lead": "Engi ×5", "text": "…" }
      ]
    }
  ]
}
```

**Markup allowed in any string:** `**bold**`, `` `code` ``, and `{{EVENT_ID}}`. Everything
else is escaped. `{{EVENT_ID}}` must name an event in this sector's pool (S2).

### Writing rules

1. **Never type a count.** If you want to say "five events can kill a crew member", the number
   is `metrics.crew_loss_events` — read it from the data file first and make the sentence match
   it. The build cannot catch a wrong number in prose; you can, by looking it up.
2. **Say what the sector does to a run.** The data already lists what is in the pool. Copy
   exists for what the list does not show: which pools are dangerous, what is worth routing
   for, what the sector's trap is.
3. **No recommendations dressed as facts.** "Cheap if you are not flying missiles" is fine.
   "Always take this" is not.
4. **No citations, no wikilinks, no version notes** in copy. The footnotes handle provenance.
5. **Three panels is the good shape**: what pays (gates/blue options), what you can leave with
   (named items and crew), what can bite (crew loss, boarders, system damage). Deviate where a
   sector genuinely differs — a nebula sector's third panel is better spent on sensor
   blackout than on boarders.
6. **The lede carries the page.** Lead with the thing a player would want to know before
   jumping in, not with a restatement of the sector's name.
7. **Do not restate what the page already renders.** The budget carries placement order and
   the at-risk chips; the markers section carries the distress mismatch. Copy earns its place
   by saying what those mean *here* — "the distress line is last, so the guaranteed distress
   beacon is the first thing this sector drops" — not by repeating them.
8. **The beacon totals are allocation, not map size.** A sector allocating 19–35 slots does
   not have 35 beacons; it has at most 24 and discards the rest. Never write the allocation
   range as though it were the number of stops.

---

## 6. Stage 2 — rendering

`build-sector.py` validates the copy, renders the content, and injects it into
`sector-page-render.html` at the `<!--SECTOR-CONTENT-->` marker, stamping the `<title>`.
Everything is inlined; the page loads nothing at runtime, because a published artifact runs
under a CSP that blocks network requests.

Page order, all of it derived except where marked:

1. **Header** — eyebrow (`Sector profile · <ID>`), title, *lede (copy)*, fact chips
2. **Stat tiles** — *labels from copy*, numbers from metrics
3. **At a glance** — the three generated blocks (§6.2). No copy at all
4. **Beacon budget** — one row per entry **in placement order**, numbered, solid blocks for
   `min` and faded for `max − min`; hostile and boarder rows are red; `placed first` and
   `may be cut` chips from `placement`. Each row is a `<details>` that **opens onto the events
   that line can place** (§6.1); an entry resolving to no events stays a plain row. Last comes
   the **fill-in row** (§4.1b-2) — `NEUTRAL`, dashed, chipped `fill-in`, and marked `+` rather
   than numbered because the file has no such line to count; it opens onto
   `generation.fallback_events`, or stays a plain zero row where `max` is 0. Then the
   legend, the generation notes (§4.1b), the entry beacon, and the *callout (copy)*
5. **Beacon markers** (§4.1c) — the distress-marked pool, the two mismatch cases, the
   store-marked pool. Fully derived; no copy hook, because it is a data finding
6. **Pool sections** — one per entry, in section order, each row a card-derived title, id and
   tags; *section note (copy)*; the AE delta block where one exists (§4.4)
7. **Quest chain** *(copy, optional)*
8. **Panels** — *copy*
9. **Footnotes** — sources, the note that generation rules are community-derived, and one
   clause per condition that applies: the `unique` scope question, the no-weights rule,
   ambiguous entries, inline outcomes with no id, missing trees

### 6.1 Beacon boxes open onto their card, in place

Every beacon box — in a budget row's expansion, in the markers section and in the pool
sections, all of them `event_html()` — is a `<details>` carrying `data-card="<slug>"`. Open
one and that event's card renders underneath it, full width, in the page. The corner `↗`
still goes to the standalone `cards/card-<slug>.html`. An event with no card stays an inert
`<div>`. The slug is the one the extractor already carries per event (`slug`, `card`).

Nothing about the card is embedded in the page. `tools/sector-cards.js` (~2 KB, inlined,
with its paths and its two strings in a config block beside it) loads three things on the
first open and none before it:

```
cards/runtime/card.js    renderer + vocabulary   once per page   ~30 KB
cards/runtime/card.css   card styling            once per box    ~7 KB
cards/data/<slug>.js     one FTLCard.define()    once per event  ~8 KB
```

Sector pages therefore grow by the loader, not by their pool: ~15 KB, not the ~600 KB–1.4 MB
their trees weigh. The card content stays where it is maintained — one file per event, built
by the card pipeline (`tools/EVENT-CARD.md` §7.3).

**Three things about this are forced, not chosen:**

- **Script tags, not `fetch`.** From `file://` a page cannot read a sibling file: `fetch`,
  `XHR` and dynamic `import()` are all blocked in Chrome and in Firefox with stock prefs. A
  classic `<script src>` is not. That single exception is why the payload is a `.js` file
  wrapping the tree rather than the tree itself.
- **A shadow root per card.** The two stylesheets collide on `wrap`, `eyebrow`, `note`,
  `fight` and `cost`, and both define the palette variables; without isolation an open card
  repaints the page around it. The page's explicit `data-theme` is copied onto the host,
  because `:host-context()` is not implemented in Firefox.
- **Published pages keep the link, not the expansion.** An artifact host cannot reach
  `cards/` at all, so on a published page the corner link is the whole story and opening a
  box shows the loader's failure line. The rich version is the local one — which is where
  these pages are read.

The budget's expansion duplicates the pool sections' rows, deliberately: the budget answers
"what does this line place?" where the question occurs, and the pool sections stay the place
to read a whole section at once. Opening the same event in both costs one payload, not two.

Two checks cover this, and they see different things (§7): `smoke-sector.py` resolves every
path the page will ask for — corner links, runtime, and one payload per box — and fails on
anything missing. `smoke-inline.py` drives a real browser over `file://` and fails if a box
does not open onto the card its own title names.

---

### 6.2 At a glance — the three generated blocks

Above the budget, because they answer "is this sector worth a detour?" before the placement
detail does. Neither takes a word of copy, and both are omitted when they would be empty — the
Last Stand gates nothing and overrides nothing, so it has no glance section at all.

**Blue options in the pool** — every option the pool gates, most-gated first, with the system
levels it asks for and a **hit count**. A hit is *one event in this pool that offers it*, not
one beacon: no file states how often an event is placed (S4), and an event listed twice is
still one event here. Six sectors gate more than 30 distinct options; the block is a reference
list, so it is never truncated.

**Crew a store can sell here** — the species a store in this sector can stock, each with its
weight, its per-slot share and its chance of appearing in at least one of the three slots
(§4.3c). Present on **all 19** sectors, including the six that declare no `rarityList`,
because those fall back to base rarity. The block carries its own provenance line: the
weighting was read out of the binary, and a page that states odds has to say so.

**Store rarity — where this sector differs** — every `<rarityList>` entry whose value differs
from the blueprint's base, shown as `base → here` with the §4.3b verdict. Crew lead the block
because which species a store can sell is the half a player acts on; everything else follows
under *Also changed*, which is what keeps the Crystal sector's 30 zeroed weapons and the Rock
sectors' Lockdown Bomb on the page. Rows equal to base are dropped — a value that changes
nothing says nothing — so the heading counts *changed of listed*.

This block replaced a panel that showed the raw `rarityList` with no base to compare against.
Sector rarity is only meaningful as a delta: `human 3` means nothing until you know human is
base 1.

## 7. Verification

```bash
python tools/smoke-sector.py sectors/sector-<slug>.html   # required before publishing
python tools/smoke-inline.py sectors/sector-<slug>.html   # or --all; needs playwright
```

Parses the built page, prints **everything it can show** — title, facts, the glance blocks,
budget rows, every event row with its tags, notes, chain steps and panels — and fails on:
unbalanced tags, an unstamped title, an empty event row, a missing budget, a blue-option row
with no hit count, a beacon box whose card link does not resolve on disk, and any `{{…}}` or
`**` that survived into the output.

> The `no stat tiles`, `stat tile is not a number` and `rarity row missing its move or its
> verdict` checks were removed on 2026-08-16 with the blocks they guarded: the stat tiles, the
> footnotes and the rarity block are all cut from the design (`SECTOR-PAGE-REDESIGN.md` §2.2,
> §2.3, §2.9). A check that requires a block the page no longer has is a false failure.

It does not check CSS, layout, colour or theming. It cannot check whether a sentence is true —
that is what rule 1 in §5 is for. And it cannot see a card at all: those are rendered into a
shadow root at open time and exist only in a live page, which is what `smoke-inline.py` is
for. That one opens boxes in Firefox over `file://` — the browser and the scheme that
constrain the design — and fails on a page error, a box that never becomes ready, an empty
shadow root, a card whose heading is not the event the box names, or a row inside a card that
will not expand.

Determinism check — build twice and diff:

```bash
python tools/build-sector.py <slug> -o /tmp/a.html
python tools/build-sector.py <slug> -o /tmp/b.html
diff /tmp/a.html /tmp/b.html
```

---

## 7b. The chooser — `sectors/index.html`

One page above the nineteen, for the moment the map offers you a jump.

```bash
python tools/build-sector-index.py            # → sectors/index.html
python tools/build-sector-index.py --verify   # check the built page
```

It lists all 19 under their designation, and **two can be pinned into a panel at the top**,
side by side, because two is what the map gives you. A third pin pushes the older one out.
Pins survive a reload (`localStorage`); clicking anywhere else on a card opens that sector's
profile. No copy file — the words are in `sector-vocab.json` under `index`, and everything
else is read.

### The designation is in the game data

Not a taxonomy of ours, and not the community wiki's grouping: `sector_data.xml` opens with
`<sectorType>` draw lists, and the map rolls against them.

| List | Sectors | Note |
|---|---|---|
| `CIVILIAN` | 5 | green |
| `HOSTILE` | 7 | red |
| `OVERRIDE_HOSTILE` | 8 | the AE form — `HOSTILE` **plus `LANIUS_SECTOR`** |
| `NEBULA` | 3 | purple |
| `UNKNOWN` | `STANDARD_SPACE` | plus four commented-out members |

Three sectors are in **no** draw list — `STANDARD_SPACE` (under `UNKNOWN`), `CRYSTAL_HOME`
and `FINAL` — and the map can never offer them. That is a stronger statement than "the
community wiki lists them apart", and it is the file's own.

Two consequences the page shows because the data does:

- **The Abandoned Sector is Advanced Edition only** — `LANIUS_SECTOR` is the sole difference
  between `HOSTILE` and `OVERRIDE_HOSTILE`, so with the DLC off nothing can roll it. Same
  `OVERRIDE_X` substitution as the event lists (§4.4).
- **Comments are stripped before parsing.** `UNKNOWN` carries commented-out `ZOLTAN_HOME` and
  `ROCK_HOME` entries; reading them would contradict their live entries elsewhere.

The community wiki is still read, for two things only: the cross-check, and the one fact the
draw lists cannot state — that a sector is pinned to a position ("always and only Sector 1",
"always sector 8"), which the page shows instead of an earliest-sector chip.

### Disagreements are notes, never overrides

The build prints a `NOTE` where the draw lists, the community wiki's grouping, and our own
`sector_class:` frontmatter disagree. It never silently resolves one against another — one of
the three is a game file and the other two are interpretations of it. The standing one:
Federation Space is in no draw list (so: special), while the community wiki files it under
Civilian Sectors as the "Civilian (Starting) Sector". Both readings are true of different
questions, which is exactly why the note stays.

---

## 8. Where fixes go

| Symptom | Fix in | Never in |
|---|---|---|
| A sentence reads wrong | `tools/sector-copy/<slug>.json` | the built HTML |
| A shared word or heading reads wrong | `tools/sector-vocab.json` | the renderer |
| A blue option is named by its raw id, or two rows share one name | `gate_labels` in `tools/card-vocab.json`, then re-extract | `extract-sector.py` |
| A pool is missing an event, or a tag is wrong | `extract-sector.py`, then re-extract | the data JSON by hand |
| A tag is wrong *for one event* | that event's tree — `extract-event.py` | `extract-sector.py` |
| Layout, colour, spacing | `sector-page-render.html` (changes all 19 pages) | one page |
| A beacon box will not open onto its card | `tools/sector-cards.js`, or rebuild the payloads with `build-card.py --all` | the built page |
| The embedded card itself looks or behaves wrong | the card pipeline — `card-runtime.js`, `event-card-render.html` (EVENT-CARD.md §7.3) | anything under `sectors/` |
| The sector title is wrong | the wiki page's H1 | anywhere else |

After any renderer or vocabulary change, rebuild **every** page and smoke-test them. These
files are shared; a local fix is a global change.

---

## 9. Publishing

**Built pages live in `sectors/sector-<slug>.html`** — a sibling of `wiki/`, never inside it,
for the reason `cards/` is: generated output would otherwise pollute every grep and index scan
of the wiki layer. Generated data lives beside it in `sectors/data/`.

Publishing is gated by its own consent prompt that no permission setting suppresses, so:

- **"Show me sector X"** → build, verify, publish, hand over the URL.
- **Bulk runs** → build and verify only. Report paths and findings; publish on request.

Republishing the **same file path** keeps the same URL, so keep a page's output filename
stable. A raw HTML file sent with SendUserFile does not render.

Say what publishing costs: the beacon boxes link to cards by relative path, so on a published
page they go nowhere (§6.1). The page a player opens from `sectors/` in a browser is the one
where the links work.

---

## 10. Pitfalls

- **Windows console is cp1252.** Use `PYTHONIOENCODING=utf-8` when running any of these
  scripts, or the em dash and `–` raise `UnicodeEncodeError`.
- **A number in prose is unverifiable by the build.** §5 rule 1 exists because the one thing
  this pipeline cannot check is a sentence that says "four" when the data says five.
- **`{{ID}}` resolves against the pool only.** Later quest stages (`ENGI_UNLOCK_3`) are not in
  the pool; put those in a chain step's `ref`, which is free text, or in `` `code` ``.
- **Do not merge an `OVERRIDE_` list into a pool** to make a page tidier. §4.4.
- **Section classification is a naming heuristic**, not something the data states. A new or
  modded sector with unusual list names lands everything in `special` — visibly wrong rather
  than silently wrong, which is the intended failure.
- **`min="0"`** is real: Rock Controlled allocates `QUESTS_ROCK` 0–1, and Federation Space
  allocates `HOSTILE_BOARDING` 0–0. A zero-max entry renders with a note; it is not a bug.

---

## 11. Known limits

- A pool row shows the event's title and tags; its outcomes are one click away in the card the
  box opens onto. That works **only off disk**: an artifact host cannot reach `cards/`, so on a
  published page a box shows the loader's failure line and only the corner link is any use
  (§6.1).
- Opening a box needs scripting. With JavaScript off, the budget lines still expand — those are
  plain `<details>` — but a beacon box opens onto an empty panel, and the corner link is the
  way through.
- `distinct_events` counts every event any entry can produce, including the store and empty-
  beacon events. It is a measure of pool breadth, not of interesting encounters.
- **Every metric covers the allocated pool only — the `startEvent` is excluded.** That matters
  on Hidden Crystal Worlds, where `START_BEACON_CRYSTAL` itself plants the ship-unlock quest
  marker and `quest_start_events` still reads 0. Check `start_event` in the data before
  writing that a sector has none of something.
- **What reads `rarity` at all is not stated by any file here.** The rarity block says what a
  sector *changes*, not what a store will stock: no file names a store, a reward roll or a
  generator as the consumer, and no file gives the weighting either, so nothing on these pages
  turns a rarity into odds. `wiki/concepts/blueprint-rarity.md` holds the evidence and the
  open questions.
- **A blueprint a sector's `rarityList` does not name is assumed to keep its base rarity.**
  That reading is not stated anywhere; it is preferred because the alternative — unlisted
  means excluded — would leave the eight sectors with no `rarityList` selling nothing. It
  matters for `CRYSTAL_HOME`, which zeroes 31 vanilla weapons but names none of the AE
  additions, so the block shows no row for them.
- Two allocation systems exist in the data and this pipeline reads only the first
  (`sector_data.xml`). If `<eventCounts>` in `newEvents.xml` is live, some sectors draw from
  lists no page here shows. See `wiki/concepts/sector-event-allocation.md`.
- **The generation rules in §4.1b are not from the game files.** They come from the community's
  reverse-engineering (`raw/wiki/sectors.md`, citing an xftl teardown this repo does not hold).
  The 24-beacon ceiling, the 80%-per-cell grid and the stop-when-full rule are all inherited
  uncertainty, and the pages say so in a footnote. `at_risk` is derived from that ceiling, so
  it inherits it too.
- The map's **beacon floor is unknown**, so nothing on these pages claims a minimum number of
  stops — only the allocation minimum, which is a different quantity.
- Whether a marker is drawn from `<distressBeacon/>` alone is Fandom's account, not something
  `raw/gamedata/` states. The *membership* data behind the markers section is exact; the claim
  about what the map draws is medium-reliability.
