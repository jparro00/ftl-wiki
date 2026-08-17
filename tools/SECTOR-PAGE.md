# Sector pages — specification

Normative spec for the FTL sector-profile pipeline. It is self-contained: an agent with no
prior context can build, verify and extend a sector page from this document alone.

A **sector page** is a single-page, self-contained HTML profile of one FTL sector — what it
must place, everything it can throw at you, and what is worth having when you fly in. Where
an event card (`tools/EVENT-CARD.md`) answers *"what do I pick right now?"*, a sector page
answers *"what am I flying into, and what should I be ready for?"*

Sector pages are **generated**. No number and no event name is ever typed into HTML.

---

## 1. Quick start

```bash
export PYTHONIOENCODING=utf-8                       # not optional on Windows — see §10
python tools/extract-sector.py ENGI_HOME            # → sectors/data/engi-homeworlds.sector.json
# write tools/sector-copy/engi-homeworlds.json      # → the words, and only the words (§5)
python tools/build-sector.py engi-homeworlds        # → sectors/sector-engi-homeworlds.html
python tools/smoke-sector.py sectors/sector-engi-homeworlds.html
```

The encoding line is part of the quick start, not a footnote to it: `smoke-sector.py` prints
the page, the page contains `↗` and `–`, and a cp1252 console kills the check mid-dump with a
`UnicodeEncodeError` that looks like a pipeline fault and is not one.

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
| `tools/build-sector-index.py` | the chooser above the nineteen (§7b) | code only |
| `tools/review-layer.html` + `tools/add-review-layer.py` | the in-browser commenting layer for a review round — `REVIEW-LAYER.md` (§7c) | layer: yes; script: code only |
| `sectors/data/<slug>.sector.json` | generated profile (regenerable data, not a page) | never |
| `sectors/sector-<slug>.html` | the built page; publish target | never |

Inputs consumed:

- `raw/gamedata/sector_data.xml` — the allocation table: every count on a page comes from here
- `raw/gamedata/events*.xml`, `newEvents.xml`, `dlcEvents*.xml` — event-list membership
- `raw/gamedata/text_sectorname.xml` — the sector's in-game display name
- `raw/gamedata/blueprints.xml` + `dlcBlueprints.xml` + `text_blueprints.xml` — names and base
  `<rarity>`, plus three membership questions nothing else answers: which ids are
  `crewBlueprint`s (§4.3b, §4.3c), which are `systemBlueprint`s — the only thing that says a
  gate's `lvl` means anything (§4.3) — and which crew carry `NOLOC="1"`, the engine's own
  dummies (§4.3c)
- `cards/trees/*.tree.json` — **every per-event tag, gate, item and crew fact** (§4.3)
- `wiki/sectors/*.md` — the `sector_id:` → (slug, title) join (§4.6)

The event trees are a hard dependency: a sector page describes its pool by reading the cards
that already exist for those events. If an event has no tree, build it first
(`python tools/extract-event.py <ID>`) — as of this writing all 19 sectors are fully covered.

---

## 3. Invariants

These hold for every sector page. Breaking one is a bug, not a preference.

- **S1 — Numbers come from the data, never from the copy.** Every figure a page shows — the
  budget counts and block odds, the heading's spread and pool size, the hit counts, the store
  percentages — is read from `sectors/data/<slug>.sector.json` by the renderer. The copy file
  has no field that takes a number, and that is deliberate: the one thing the build cannot
  check is a sentence (§5 rule 1), so nothing that *can* be checked is left to prose.
- **S2 — Prose names events by id, not by title.** Copy writes `{{ENGI_VIRUS}}`; the renderer
  resolves the title. An id the sector cannot produce **fails the build**, so a page can never
  mention an event that is not in its pool.
- **S3 — Tags are derived, never asserted.** `fight` means the event's tree has combat at its
  root; `may-fight` means combat exists below a choice. Read from the tree, not from which
  list the event sits in.
- **S4 — No invented odds.** The shipped event lists carry no weights (EVENT-CARD.md I2), so
  **no pool row ever gets a percentage**. A list that names the same event twice is `×2` —
  that repetition is the only weight the files contain. The two percentages a page does show
  are arithmetic on a stated rule, not a guess about a list: the budget's faded blocks are
  `P(roll ≥ k)` over the line's own min–max (§4.1b), and the store-crew shares are the
  engine's `6 − rarity` weighting read out of the binary (§4.3c).

  > **Sector pages are exempt from S4's disclosure half.** The card pipeline states an odds
  > figure's provenance beside it; these pages do not, because the footer that would carry it
  > was cut (user decision, 2026-08-16 — no sources, no disclosure, no link out). The evidence
  > is not lost, only off the page: `wiki/concepts/blueprint-rarity.md`,
  > `wiki/concepts/sector-event-allocation.md` and
  > `raw/modding/2026-08-16-store-crew-selection-disassembly.md` hold it. A reader of a sector
  > page cannot tell where a number came from; that is a known and accepted cost.
- **S5 — Open questions stay open, in the wiki — not on the page.** The pipeline still
  refuses to resolve what the data does not state: `OVERRIDE_X` is never merged into a pool
  (§4.4), `unique` is never given a scope (§4.5), and the uniform min–max roll behind the
  block odds is an assumption (§4.1b). What changed is **where the caveat is said**. Only one
  survives on the page — the AE delta's "whether the engine uses this list instead is not
  stated by any file here", which sits inside the block it qualifies. Every other open
  question lives in `wiki/concepts/` (`event-uniqueness.md`, `sector-event-allocation.md`,
  `blueprint-rarity.md`) and in §12 of this document.

  > **This is an explicit exemption, not a lapse.** Sector pages carry no footer, no sources
  > and no standing caveats. Do not add one back to a single page; if the decision is
  > revisited it is a renderer change across all 19, and this invariant changes with it.
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
files. The extractor reads them as the list and marks the entry `ambiguous`. **Nothing on the
page says so** — the footnote that carried it is gone (§3, S5); the flag is in the data and
the ambiguity is here.

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
  marked, unnumbered row (§4.1b-2, §6 item 3).
- The **exit beacon is not in the table** — it draws from a shared `EXIT_LIST`, and an exit
  inside a cloud is always empty.

So `entries` is kept in **file order** and carries `placement` (`position`, `nebula_first`,
`before_min`, `before_max`, `at_risk`, `always_short`):

- **`at_risk`** — the lines placed before it could, at their maxima, consume all 24 beacons.
  A possibility, not a prediction. Chipped `may be cut`.
- **`always_short`** — the minima above it plus its own minimum already exceed 24, so it
  cannot be satisfied even on the best roll. Chipped `always short`, and true on exactly one
  line in the shipped data: `NEUTRAL_CRYSTAL`, the last line of Hidden Crystal Worlds.

The `generation` block carries the totals, `can_exhaust_map`, `cannot_meet_minimum`, and the
`at_risk_entries` / `always_short_entries` name lists.

**Each line rolls its count uniformly** between its `min` and `max`, which is what lets the
budget put a figure on a faded block: the k-th optional block lands whenever the roll reaches
k, so it reads `P(roll ≥ k)`, a chance of *at least* that many. The source says only "randomly
choose between the minimum and maximum (inclusive)" — uniform is the natural reading of that
and it is what the page prints, but it is an assumption stated as a number (§12).

Sorting entries into reading order — which this extractor originally did — throws that away.
The budget is the only listing of the entries and it renders placement order, so nothing on a
page re-sorts them. `entry["order"]` keeps the raw file index if anything ever needs it.

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
is not the exit beacon (`EXIT_LIST`, outside the table entirely). The cloud rule is stated in
the generation note so the two cannot be conflated; the exit beacon is not on the page at all.

**Two sectors need the row explained, and only they get a third generation line** (§6). Both
say something no block on the page can show, which is the bar for adding one:

| Condition | Where | The line says |
|---|---|---|
| `generation.cannot_meet_minimum` | Hidden Crystal Worlds | the table asks for 25 beacons against the 24 a map can hold, so its bottom is cut every time — and its fill-in row is a zero row |
| the table names `NEUTRAL` as a numbered line too | both Slug nebulas | one pool reached two ways, not a doubled row — without it the budget appears to list `NEUTRAL` twice for no reason |

The other 16 pages carry the two-paragraph note and nothing more.

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
  > shows the marker wherever the event lands — but the mechanism does not, so nothing on the
  > page asserts a fill order for it. The one line under the distress section states the
  > outcome only: some of these show up in the neutral pools, and not every beacon from the
  > `DISTRESS` pool broadcasts a signal.
- The reverse also happens: events allocated from a `DISTRESS_BEACON_*` list that carry no
  distress tag, and so never show the marker. Fandom calls these a mistake in the data.

`rollup.markers` carries both directions (`events`, `marked_outside_allocation`,
`allocated_but_unmarked`), plus store-marked events and an environment breakdown. The same two
facts are mirrored onto every event record as the `distress` and `store-marker` tags (§4.3),
computed in the same place so a row and the rollup cannot drift apart — which is what lets a
beacon box say what the map will draw *wherever it appears on the page*, not only inside the
markers sections. The environment breakdown is not rendered as a section; the budget's cloud
paragraph reads `storm` out of it (§6).

### 4.2 Sections

A section is read off the entry name, which is highly regular across all 19 sectors:
`HOSTILE*` → hostile, `BOARDERS*` → boarders, `NEUTRAL*` → neutral, `DISTRESS_BEACON*` →
distress, `ITEM*` → items, `STORE*` → store, `QUESTS*` → quests, `NOTHING*`/`NEBULA_EMPTY` →
empty, `NEBULA*`/`STORM*` → nebula.

Anything unmatched falls through to **special** — an unrecognised name is a named one-off
beacon (`ENGI_UNLOCK_1`, `ROCK_UNLOCK1`, `FLAGSHIP_CONSTRUCTION`, `MANTIS_NAMED_THIEF`,
`ZOLTAN_PEACE_QUEST`), which is why the fallback is a category and not an error.

The section drives two things and no third: the `section:<name>:min|max` metrics, and whether
a budget row paints red (`hostile` and `boarders` do). `SECTION_ORDER` still exists in the
extractor and orders the metrics; **nothing on the page is sorted by it**, because the budget
renders placement order and there is no other listing of the entries.

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
| `distress` | the event's root `<distressBeacon/>` — the map draws a **distress marker** here |
| `store-marker` | the event's root `<store/>` **or** a `store` node anywhere in its tree |

The last two are the **marker tags**, and they are not ordinary tags. Ordinary tags are capped
at three per row (`tag_limit`) and picked in `tag_order`; the marker tags sit outside that cap,
because they say what the map shows *before you jump*, which is the fact a row is read for and
the one that must never be squeezed off a busy row.

> **The per-event marker tag is `store-marker`, not `store`.** `store` means "a store opens
> somewhere in this tree". The two names are one character apart and are wired to different
> things — check which one a change is about before touching the vocabulary, the `marker_tags`
> list or the CSS.
>
> ⚠️ **`store-marker` is a strict superset of `store`, and that is a decision, not an
> oversight** (user, 2026-08-16). It fires on the root `<store/>` *or* on any store node below
> a choice, so every `store`-tagged event carries it too — `STORE_REBELSIDE` is the visible
> case, an AE-added row tagged both. Read it as "a store can open here", not as "the map draws
> a store on this beacon": the narrower map-marker fact is the root flag alone, and no page
> shows it. Narrowing the tag is a one-line change in `markers()` plus a re-extract of all 19,
> and it would change what 63 rows across the 19 sectors say.

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

**Each gate row also carries `system` and `levels_detail`**, because the page shows one row per
option *and level* and must not re-walk the pool to get there:

- **`system`** — whether any `req` behind this label names a `<systemBlueprint>`. Read from
  `blueprints.xml` + `dlcBlueprints.xml`, never a hand-written list. Only a system has a level
  to ask for; crew, augments and weapon lists have none.
- **`levels_detail`** — `[{lvl, events}]`, de-duplicated by event id *within* each level. A
  count here is always "distinct events that offer it at that level", never a sum, so the rows
  do not have to add up to `events` and the same event gated twice at one level counts once.
  `levels` is the older, flatter field: it says which levels exist, not how many events ask for
  each, which is why Sensors 2 and Sensors 3 collapsed into one row of 7 where the page wants
  two rows of 4 and 5.
- **A system gate with no `lvl` folds into level `"1"`.** `lvl` is a floor
  (`wiki/concepts/blue-options.md`) and a system you merely *have* is at level 1, so
  `req="teleporter"` with no level merges with `lvl="1"` and the row reads `Teleporter 1+`.
  Sound, but no file states it (§12).
- **A non-system gate gets one row with `lvl: null`**, rendered as the bare label.

### 4.3b Rarity as a delta — `crew_rarity`

> **Extracted, not rendered.** No page shows `crew_rarity`: the block that did was cut from
> the design (user decision, 2026-08-16 — "no page needs this"). It is still emitted because
> it costs nothing and because `crew_store_odds` is computed from the same effective-rarity
> logic, which is very much on the page (§4.3c). Treat it as available data with no consumer
> in this pipeline, not as something a page is missing.

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

- **`excluded`** = the other side of the same filter: every `crewBlueprint` whose effective
  rarity is exactly `0`, which is the flag meaning "not in the pool at all", so a store here
  can never offer it. Emitted as `[{id, label}]` beside `crew`, so the renderer never reads
  XML. A species the files give no `<rarity>` at all is `unknown`, not excluded, and appears
  in neither list.
- **`NOLOC="1"` crew are filtered out of `excluded`.** `battle` and `repair` are
  `crewBlueprint`s at rarity 0 like the excluded species, but they are the engine's drone
  stand-ins — desc "Dummy blueprint needed now." — never shown to a player. `NOLOC` is the
  files' own mark for that, which is why `excluded` carries three species and not five. The
  filter is derivable but is not a rule any file states (§12).

Each slot is an independent `count = 1` draw, so a store can offer the same species twice.
That is not true of weapons, drones or augments, which are drawn without replacement in a
single call — noted here because it is a trap for anyone extending this block to items.

**S4's no-invented-odds half still holds** — no *beacon* gets a percentage; this is a store's
internal roll. Its **disclosure** half does not: the block used to carry a provenance line and
no longer does (§3, S4).

### 4.4 AE override lists — a delta, never a merge

`dlcEventsOverwrite.xml` defines twelve `OVERRIDE_<LIST>` twins. **Whether the engine
substitutes them is an open question** — see `wiki/concepts/sector-event-allocation.md`. So
the extractor never merges one into a pool. It emits the *difference* (`added`, `removed`,
`applies: "unconfirmed"`), and the renderer shows it as a marked block at the **foot of the
budget line's expansion**, headed `Advanced Edition adds — OVERRIDE_<LIST>`, with the
uncertainty stated in the block itself. That caveat is the one open question still printed on
a sector page (§3, S5), and it earns its place by sitting inside the block it qualifies.

### 4.5 `unique` is not settled either

`unique="true"` is the files' own attribute. Whether its scope is once per sector or once per
run is contradicted between sources (`wiki/concepts/event-uniqueness.md`; the wiki's better
bet is **per sector**). The tag says only "Unique", and the page says nothing more — the
footnote that used to carry the scope question went with the footer (§3, S5). The question is
live in `wiki/concepts/event-uniqueness.md` and in §12; do not resolve it in copy, and do not
write copy that implies a scope.

### 4.6 Title and slug

From the same kind of join the event pipeline uses: each `wiki/sectors/*.md` declares
`sector_id:` and has an H1. The filename is the slug, the H1 is the title. A page listing
several ids (`vestigial-definitions.md`) documents no single sector and is skipped — which is
why `DEEP_SPACE_SECTOR` and `ABANDONED_SECTOR` get no page.

### 4.7 Metrics

`metrics` is a flat map of named, precomputed numbers — the only place a figure on a page may
come from (S1). It is **wider than what any page renders**, deliberately: the cost of a metric
is a line of arithmetic, and a number that has to be derived at render time is a number that
can be derived differently in two places.

The sector page itself reads exactly two of them, both in the budget heading —
`beacons_min..beacons_max` and `distinct_events`. Everything else is read by the chooser
(§7b), by the wiki when a query needs it, or by nothing at all. Do not delete an unread
metric on that basis, and do not assume a metric is on a page because it exists.

- `beacons_min`, `beacons_max` — the allocation totals, **not** the map size
- `grid_beacons` (24, the map ceiling), `at_risk_entries`
- `distinct_events`, `always_fight_events`, `may_fight_events`, `crew_loss_events`,
  `crew_gain_events`, `boarder_events`, `unique_events`, `gated_events`, `quest_start_events`
- `blue_options` (distinct options after the label merge), `blue_option_hits` (events offering
  one, summed — an event gated twice by different options counts in both)
- `store_rarity_changes`, `crew_rarity_changes` — entries this sector moves off base rarity.
  Nothing renders these; the block they were computed for is gone (§4.3b)
- `crew_types_sold` — species a store here can offer (§4.3c)
- `section:<name>:min` / `:max` — e.g. `section:hostile:min`
- `entry:<NAME>:min` / `:max` — e.g. `entry:STORE_ENGI:max`

The copy file cannot name a metric (§5) — the days of a hand-labelled tile pointing at a
metric id are over — so a metric only reaches a page by a renderer change.

---

## 5. The copy file — the only thing written by hand

`tools/sector-copy/<slug>.json`. Unknown keys are rejected; every constraint below is enforced
by `build-sector.py`, so a violation is a build failure, not a review note.

Five keys, and there are no others. `stats` and `callout` were keys once; they are now
**rejected as unknown**, and a copy file carrying either fails the build. The blocks they fed
— the stat tiles and the boxed note under the budget — are gone from the design, and an
accepted-but-ignored key is a place for words to go quietly nowhere.

```jsonc
{
  "slug": "engi-homeworlds",          // must match the data file

  "lede": "…",                        // required. One or two sentences: what this sector *is*
                                      // to a run. The one place a point of view belongs, and
                                      // the only prose above the fold.

  "section_notes": {                  // optional, keyed by entry name
    "HOSTILE_ENGI": "…"               // one line inside that budget line's expansion,
  },                                  // under its events and above the AE delta

  "chain": {                          // optional. Only where a real multi-jump quest starts here.
    "title": "Stealth Cruiser · The Nesasio",
    "steps": [
      { "marker": "1", "title": "…", "detail": "…", "ref": "ENGI_UNLOCK_1" }
    ]                                 // marker: "1","2","3","✓" — last step renders green.
  },                                  // ref: free text, shown in mono. Not resolved, so it may
                                      // name events outside the pool (later quest stages).

  "panels": [                         // required, 2–4. The whole of the page's prose below
    {                                 // the budget. The two generated blocks (§6.2) are not
                                      // panels and take no copy — do not write one.
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
4. **No citations, no wikilinks, no version notes** in copy — and there is nowhere else on the
   page for them either. A sector page carries no provenance at all (§3, S5); do not smuggle
   it back in through a panel item.
5. **Three panels is the good shape**: what pays (gates/blue options), what you can leave with
   (named items and crew), what can bite (crew loss, boarders, system damage). Four is the
   ceiling and one sector uses it. Deviate where a sector genuinely differs — a nebula
   sector's third panel is better spent on sensor blackout than on boarders. **A panel that
   restates a generated block is the failure mode to watch for**: there is no section left on
   the page for prose to duplicate except the budget and the two glance blocks, and every one
   of those already reads cleanly on its own.
6. **The lede is one or two sentences.** It is the only prose above the fold, so it says what
   this sector is to a run and stops — not a restatement of the sector's name, not a summary
   of the blocks below it. Where the game's own display name and the map's label disagree, the
   lede leads with what the player sees on the map.
7. **Do not restate what the page already renders.** The budget carries placement order, the
   chips and the block odds; the distress section carries the marker mismatch; every event row
   carries its own tags. Copy earns its place by saying what those mean *here* — "the distress
   line is last, so the guaranteed distress beacon is the first thing this sector drops" — not
   by repeating them.
8. **The beacon totals are allocation, not map size.** A sector allocating 19–35 slots does
   not have 35 beacons; it has at most 24 and discards the rest. Never write the allocation
   range as though it were the number of stops.

---

## 6. Stage 2 — rendering

`build-sector.py` validates the copy, renders the content, and injects it into
`sector-page-render.html` at the `<!--SECTOR-CONTENT-->` marker, stamping the `<title>`.
Every asset is inlined — CSS, both scripts, the loader's config — so the page needs no network
at load, which is what a published artifact's CSP requires. The one thing fetched later is a
card, on demand, off disk, and only when a reader opens a box (§6.1).

Page order, all of it derived except where marked. Seven blocks and two scripts — the page is
short on purpose, and every section that survived is one a player reads *while flying the
sector*:

1. **Header** — eyebrow (`Sector profile · <ID>`), title, *lede (copy)*, fact chips: earliest
   sector, unique-or-repeatable, music tracks, and `built from Advanced Edition files`
2. **At a glance** — the two generated blocks (§6.2). No copy at all, and **omitted entirely**
   when a sector has neither: the Last Stand gates nothing, so it has no glance section
3. **Beacon budget** — the spine of the page. The heading carries the two surviving metrics
   (`13–24 slots allocated · 85 events in pool`), then:
   - one row per entry **in placement order**, numbered, solid blocks for `min` and faded for
     `max − min`; hostile and boarder rows are red; `placed first`, `may be cut` and
     `always short` chips from `placement` (§4.1b). Every block carries its own chance as a
     `title` tooltip — solid says "always placed, if the map has room", faded says `P(roll ≥ k)`
   - each row is a `<details>` whose expansion holds **the events that line can place** (§6.1),
     then that line's *section note (copy)*, then the **AE delta** where the list has an
     `OVERRIDE_` twin (§4.4). An entry with none of the three stays a plain, unexpandable row
   - the **fill-in row** last (§4.1b-2) — `NEUTRAL`, chipped `fill-in`, marked `+` rather than
     numbered because the file has no such line to count. Its blocks carry "filled only if the
     table leaves room" instead of a percentage, since no roll governs it. Where `max` is 0 it
     is a plain zero row that opens onto nothing
   - the **legend** — three rows: solid = must be placed, faded = may be placed with the odds
     worked once on this sector's widest line, red = always a fight. The worked example has two
     wordings, and which one is used matters: `legend.may` reads "80% for one" and is only true
     where the example line's minimum is 0; a line that already guarantees blocks gets
     `legend.may_offset`, which says "for the first faded one"
   - the **generation notes** (§4.1b) — two paragraphs, plus a conditional third on three
     sectors (§4.1b-2). The cloud paragraph counts the plasma storms in the shared `NEBULA`
     list only where the sector allocates that list itself; elsewhere it states the conversion
     rule alone
4. **Distress signals** (§4.1c) — the distress-marked pool, and one italic line saying the
   marker and the allocation list do not match in either direction. Fully derived, no copy hook
5. **Stores** — the store-marked pool. Same, without the note
6. **Quest chain** *(copy, optional)*
7. **Panels** — *copy*. No heading of their own; the panel titles are the headings
8. **The two inlined scripts** — the card loader with its JSON config (§6.1) and
   `sector-toggle.js`, which makes the blue-options box toggle from anywhere in the box

There is **no footer**. Provenance and open questions are off the page by decision, not by
omission — §3, S4 and S5, and §12.

### 6.1 Beacon boxes open onto their card, in place

Every beacon box — in a budget row's expansion, in its AE delta, in the fill-in row and in the
two marker sections, all of them `event_html()` — is a `<details>` carrying
`data-card="<slug>"`. Open
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

**The budget's expansion is the only place a pool is listed.** A page used to carry pool
sections below the budget repeating the same rows; that duplication is what made the page too
long for any of it to matter, and the budget is the copy that survived — it answers "what does
this line place?" where the question is asked. An event reachable two ways (a marker section
and a budget line) still costs one payload, not two.

Two checks cover this, and they see different things (§7): `smoke-sector.py` resolves every
path the page will ask for — corner links, runtime, and one payload per box — and fails on
anything missing. `smoke-inline.py` drives a real browser over `file://` and fails if a box
does not open onto the card its own title names.

---

### 6.2 At a glance — the two generated blocks

Side by side above the budget, because they answer "is this sector worth a detour?" before the
placement detail does. Neither takes a word of copy. The section is omitted when both are
empty — the Last Stand gates nothing, so it has no glance section at all.

They are laid out as a **level pair**, and nothing enforces that: the two boxes balance because
their content happens to, at the real panel width. When a page is reviewed, look at the glance
row on the page rather than trusting that it held on the last sector.

**Blue options in the pool** — one row per option **and level**, most-gated first, each with a
**hit count**. The level lives in the option's name (`Teleporter 1+`, `Sensors 3+`) in the blue
option colour, not in a chip beside it; a non-system gate carries no level at all (§4.3). The
top four rows are visible and the rest are behind the box, which is **its own toggle** —
`tools/sector-toggle.js`, because a `<details>` only toggles from its `<summary>`, so an open
box could otherwise be opened from the visible rows and never closed from the rows it revealed.

> A hit is *one event in this pool that offers it*, not one beacon: no file states how often an
> event is placed (S4), and an event listed twice is still one event. **The page no longer says
> this anywhere** — the note that carried the definition went with the rest of the prose. A
> reader who assumes hits are beacons will read the block high (§12).

**Crew in stores** — the species a store in this sector can stock: two columns of rows, each
with its per-slot share and its chance of appearing in at least one of the three slots, rounded
to whole numbers (§4.3c). The panel's title rides in the empty label cell of the first column's
sub-header, so the heading costs no line of its own. Weight is not shown — it is `6 − rarity`
and nothing is played off it.

Present on **all 19** sectors, including the six that declare no `rarityList`, because those
fall back to base rarity. **Species a store cannot sell stay in the table at 0%, greyed** —
`crew_store_odds.excluded`, the `crewBlueprint`s whose effective rarity is 0. Rarity 0 is a
flag meaning "not in the pool", and a zero row says that where a player is already looking.

The layout is **column-major**: the rows are split in half and read down, then across, which
keeps the rank scan top-to-bottom and lands the excluded species together at the foot of the
second column. Two things the block used to say and no longer does: that a store rolls three
slots, and that some species are excluded at all. Both are now inferable only from a tooltip
and a 0% row (§12).

## 7. Verification

```bash
python tools/smoke-sector.py sectors/sector-<slug>.html   # required before publishing
python tools/smoke-inline.py sectors/sector-<slug>.html   # or --all; needs playwright
```

Parses the built page, prints **everything it can show** — title, facts, the glance blocks,
budget rows, every event row with its tags, notes, chain steps and panels — and fails on:

- unbalanced tags: an unclosed or stray element
- a title that was never stamped (still the template's placeholder)
- an empty event row
- no beacon-budget rows at all
- a blue-option row whose last cell is not a hit count
- a card link, a runtime file or a card payload the page asks for that is not on disk,
  resolved the way the browser will resolve it — relative to the page's own directory
- a beacon box with no `data-card` slug, or a missing card-loader config block
- any `{{…}}`, `**` or unfilled `<!--SECTOR-CONTENT-->` that survived into the output
- a *paired* `*…*` in the text — someone reached for italics, which the copy layer does not
  support and renders literally. Single asterisks are legitimate and must not fire

**Every check maps to something the page still has.** A check for a block the page no longer
carries is a false failure, which is worse than no check: it trains a reader to ignore the
output. Delete a check with the block it guarded, in the same pass.

The dump prints under fixed headings — `TITLE`, `HEADING`, `LEDE`, `FACTS`, `GLANCE`,
`BUDGET`, then the sections and `PANELS` — and the `GLANCE` block is the only way a wrong
label or a missing count in the two generated panels ever becomes visible, since they carry
no copy for a human to have reviewed.

It does not check CSS, layout, colour or theming. It cannot check whether a sentence is true —
that is what rule 1 in §5 is for. And it cannot see a card at all: those are rendered into a
shadow root at open time and exist only in a live page, which is what `smoke-inline.py` is
for. That one opens boxes in Firefox over `file://` — the browser and the scheme that
constrain the design — and fails on a page error, a box that never becomes ready, an empty
shadow root, a card whose heading is not the event the box names, or a row inside a card that
will not expand.

> **`--all` globs `sectors/sector-*.html`**, so anything else parked in that directory is
> checked as though it were a sector page. Keep the directory to the nineteen; a stray page
> there turns a clean bulk run into a failure that is nothing to do with the pipeline.

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

**The panel is one table, and the pinned boxes are its header cells** (`<thead>`), not a
separate row of boxes above it. So a sector's box and its figures are the same table column
and cannot drift apart, and the table carries **no row of sector names** — the box already
says which sector the column is. (Review rounds, 2026-08-16.)

Four things about that panel are less obvious than they look:

- **The table is there whether or not anything is pinned.** Empty columns show `—` and the
  header is a dashed prompt. The questions it asks are the same ones whatever is in the
  columns, and a panel that appears on the first pin moves the whole page under the reader.
- **The panel is the content width in every state** — `.wrap` is `58rem`, the width the
  sector profiles themselves are read at, and the table is `width: 100%` of it with the
  columns as **percentages** (28% for the labels, the remaining 72% split between the
  sectors). Fixed rem widths would make the panel a different size for two sectors than for
  four. Figures are **centred** in their column: flushed right they cluster at one edge with
  a gulf between a label and its own numbers.
- **The boxes are levelled in JavaScript, not in CSS.** `levelBoxes()` sets them to `auto`,
  measures the tallest and gives them all that height, and re-runs on resize. A percentage
  height inside a `<th>` has nothing to resolve against, so the box falls back to its own
  content — or, given a `min-height` floor, to the floor, and a name that wraps then spills
  out under its own border. That failure looks like equal boxes to any check that only
  compares heights; the check that catches it is `scrollHeight > clientHeight`.
- **The whole box is the link to the profile**, with the unpin button sitting on top of it.
  The click handler's `preventDefault()` runs on the bubbled event, which cancels the
  anchor's navigation — so unpinning from the box does not also open the sector.

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

## 7c. Reviewing a page with the user

Neither smoke test can tell you a page is *good*, and the user reviews in the browser, not in
chat. Hand over a review copy — a built page with the commenting layer appended:

```bash
python tools/add-review-layer.py sectors/sector-rock-homeworlds.html
```

The user selects text, attaches notes to it, and exports them as markdown to `~/Downloads`;
read the newest `review-notes*.md` there. **`tools/REVIEW-LAYER.md` is the spec** — how the
notes anchor, what survives a rebuild, and what to check after changing the layer. The one
thing to carry while editing a page under live notes: anchors are character offsets into the
visible text, so **anything added above an anchor shifts it**, while CSS pseudo-element content
is not a text node and moves nothing.

**Read a note against what the page is for.** The exports are terse and often anchor to
whatever was nearest to what the user meant — a note on a 4,000-character selection reading
"remove all this" meant "delete the duplicated section", not "delete these facts". Say what you
concluded when you report back.

**Review one sector at a time.** The notes come back anchored to a page and are worth more per
page than in bulk.

---

## 8. Where fixes go

| Symptom | Fix in | Never in |
|---|---|---|
| A sentence reads wrong | `tools/sector-copy/<slug>.json` | the built HTML |
| A shared word or heading reads wrong | `tools/sector-vocab.json` | the renderer |
| A blue option is named by its raw id, or two rows share one name | `gate_labels` in `tools/card-vocab.json`, then re-extract | `extract-sector.py` |
| A pool is missing an event, or a tag is wrong | `extract-sector.py`, then re-extract | the data JSON by hand |
| A tag is wrong *for one event* | that event's tree — `extract-event.py` | `extract-sector.py` |
| A blue option shows the wrong level, or one row where two belong | `levels_detail` in `extract-sector.py`, then re-extract | `build-sector.py` |
| A marker tag is on the wrong event | `extract-sector.py` — the same `marker` dict feeds the tag and `rollup.markers`, so fix it once | the tag list in `sector-vocab.json` |
| The blue-options box will not close from its own body | `tools/sector-toggle.js` | the built page |
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
- **`{{ID}}` resolves against what the sector can produce**, which is the allocated pool plus
  three things easy to forget: the events an `OVERRIDE_` list *adds*, the `startEvent`, and the
  ids named as quest targets. Later quest stages (`ENGI_UNLOCK_3`) are in none of those; put
  those in a chain step's `ref`, which is free text, or in `` `code` ``.
- **Do not merge an `OVERRIDE_` list into a pool** to make a page tidier. §4.4.
- **Section classification is a naming heuristic**, not something the data states. A new or
  modded sector with unusual list names lands everything in `special` — visibly wrong rather
  than silently wrong, which is the intended failure.
- **`min="0"`** is real: Rock Controlled allocates `QUESTS_ROCK` 0–1, and Federation Space
  allocates `HOSTILE_BOARDING` 0–0. A zero-max entry renders as a `zero` row, styled apart and
  still expandable onto the events it would place; it is not a bug.
- **`store` and `store-marker` are different tags.** §4.3.
- **Two names for one hazard.** `always_short` (a line that cannot be satisfied) and
  `cannot_meet_minimum` (a *table* that cannot fit the map) are related but not the same
  field — the first is per entry, the second is per sector, and only the second drives a
  generation note.

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
- **What reads `rarity` outside the crew draw is not stated by any file here.** The store's
  crew selection is known, out of the binary (§4.3c). Nothing says what consumes a *weapon*,
  drone or augment rarity — no file names a store, a reward roll or a generator as the reader,
  and no file gives that weighting — so no page here turns a non-crew rarity into anything.
  `wiki/concepts/blueprint-rarity.md` holds the evidence and the open questions.
- **A blueprint a sector's `rarityList` does not name is assumed to keep its base rarity.**
  `ResetRarities()` restoring base on sector entry supports it, but the reading is not stated
  outright; it is preferred because the alternative — unlisted means excluded — would leave
  the six sectors with no `rarityList` selling no crew at all.
- **`crew_rarity` has no consumer on the page.** It is extracted and shipped in the data; the
  block that rendered it is cut (§4.3b). A sector's non-crew rarity changes — the Crystal
  sector's zeroed weapons, the Rock sectors' Lockdown Bomb — are in the JSON and nowhere else.
- Two allocation systems exist in the data and this pipeline reads only the first
  (`sector_data.xml`). If `<eventCounts>` in `newEvents.xml` is live, some sectors draw from
  lists no page here shows. See `wiki/concepts/sector-event-allocation.md`.
- **The generation rules in §4.1b are not from the game files.** They come from the community's
  reverse-engineering (`raw/wiki/sectors.md`, citing an xftl teardown this repo does not hold).
  The 24-beacon ceiling, the 80%-per-cell grid and the stop-when-full rule are all inherited
  uncertainty. `at_risk`, `always_short`, the fill-in row's size and every faded block's
  percentage are derived from them, so they inherit it too — and **the page no longer says
  so**, because the footnote that did went with the footer (§3, S5). A page states these
  numbers flatly; the caveat lives here and in `wiki/concepts/sector-event-allocation.md`.
- The map's **beacon floor is unknown**, so nothing on these pages claims a minimum number of
  stops — only the allocation minimum, which is a different quantity.
- Whether a marker is drawn from `<distressBeacon/>` alone is Fandom's account, not something
  `raw/gamedata/` states. The *membership* data behind the markers section is exact; the claim
  about what the map draws is medium-reliability.
- **Two definitions the page assumes its reader already has**: that a blue-option hit is one
  event and not one beacon (§6.2), and that a store rolls three slots. Both were stated on the
  page once. Neither is now.

---

## 12. Open questions

The pipeline runs on five readings that no file in this repo states outright. None of them
blocks anything; all of them would change a number or a row if answered the other way, and
none appears on a page (§3, S5). They are listed here because this document is where a sector
page's uncertainty lives now.

1. **Is the min–max roll uniform?** The source says only "randomly choose between the minimum
   and maximum (inclusive)" (`raw/wiki/sectors.md`, community reverse-engineering). Uniform is
   the natural reading and is what every faded block's percentage assumes — an assumption
   printed as a number.
2. **Is a level-less system gate the same as level 1?** `lvl` is a floor and a system you have
   is at level 1, so `req="teleporter"` with no level folds into the `1+` row (§4.3). Sound,
   unstated. Answering it the other way splits several rows.
3. **Is `NOLOC="1"` the right filter for dummy crew?** It is what keeps `battle` and `repair`
   out of the excluded-species list, leaving three species rather than five (§4.3c). Derivable
   from the files' own mark; not a rule any file states.
4. **Is `unique="true"` per sector or per run?** §4.5, `wiki/concepts/event-uniqueness.md`.
   The wiki's better bet is per sector.
5. **Does `OVERRIDE_X` replace `X`?** §4.4, `wiki/concepts/sector-event-allocation.md`. The
   whole delta-not-merge design exists because this is unanswered.

One more that is a question for the user rather than for the files — do not settle it by
writing spec text around it:

6. **Is alphabetical the right order for the excluded species?** `crew_store_odds.excluded` is
   sorted by label, so the 0% rows at the foot of the crew block read in no order a player
   cares about — the candidates above them are ranked by weight. Nothing depends on the
   current order.

And one contradiction that belongs in `wiki/`, not here: the files call `STANDARD_SPACE`
*Federation Space* (`text_sectorname.xml`) while the game shows **Sector 1: Civilian Sector**
on the map, confirmed in game by the user. The lede leads with what the player sees. File it
in `wiki/sectors/federation-space.md` per CLAUDE.md §4 if it is not there yet.
