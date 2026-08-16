# Sector pages — the 2026-08-16 redesign

**Status: agreed on one sector, not yet implemented.** Federation Space was redesigned in a
mock over five review rounds with the user. The result is
`sectors/sector-federation-space-mock.html`, built by `sectors/mockups/mock-federation.py`.
Nothing under `tools/` has changed yet, so the other 18 pages still render the old shape.

This document is the delta against `tools/SECTOR-PAGE.md`, which remains the normative spec
for everything not listed here. Read that first; this is a change list, not a replacement.

> **Do not start by editing `build-sector.py`.** §6 below is the order of work, and it starts
> with two decisions only the user can make.

---

## 1. Why the page changed

The old page answered every question it could. In use — the user reading a sector page while
actually flying the sector — most of that was in the way:

- **Prose that restated the tables.** Nine paragraphs of explanation around blocks that were
  already legible. Every one of them was cut.
- **The pool sections duplicated the budget.** The budget rows expand onto the events a line
  places (SECTOR-PAGE.md §6.1); the pool sections below listed exactly the same rows again.
  One of the two had to go, and the budget is the one that answers the question where it is
  asked.
- **Vertical space in the glance row.** Two panels side by side, one twice the height of the
  other, on the screen area a player looks at first.

The direction, in one line: **keep every fact, delete every sentence that explains a fact the
block already shows, and spend the saved height on nothing.**

---

## 2. The changes, one by one

Each entry says what it is, where the fix belongs per SECTOR-PAGE.md §8, and what it needs
from the data. "mock" is the function in `sectors/mockups/mock-federation.py` that does it
today.

### 2.1 Header

| Change | Lands in |
|---|---|
| Lede cut to one sentence, leading with what the sector *is* to a run | `sector-copy/<slug>.json` |
| `entry beacon START_BEACON` chip dropped | `build-sector.py` `header_html()` |
| `tracks` chip relabelled **music** | `sector-vocab.json` `facts.tracks` |
| `Advanced Edition data` → **built from Advanced Edition files** | `sector-vocab.json` `facts.data` |

The lede also settled a naming question: the files call `STANDARD_SPACE` *Federation Space*
(`text_sectorname.xml`), but the game shows **Sector 1: Civilian Sector** on the map, confirmed
in game by the user. The page leads with what the player sees. **This contradiction is not yet
filed in `wiki/`** — see §5.

### 2.2 Stat tiles — removed entirely

The five tiles were deleted. Two of the numbers moved into the Beacon budget heading, which is
where they mean something:

```
Beacon budget    13–24 slots allocated · 85 events in pool
```

Both are still metrics (`beacons_min..beacons_max`, `distinct_events`) — S1 holds.

This is the change with the widest blast radius:

- `build-sector.py` drops `stats_html()` and stops requiring `stats` in `check()`
  (`COPY_KEYS`, `REQUIRED`).
- **All 19 copy files** carry a now-dead `stats` block. Either drop the key from each, or keep
  accepting and ignoring it — decide once, in §6.
- `smoke-sector.py` fails with `no stat tiles`. That check must go, and SECTOR-PAGE.md §7's
  list of failures updated with it.

### 2.3 At a glance

- Heading meta ("what this sector changes, and what it pays") removed →
  `sector-vocab.json` `headings.glance_meta`.
- **Blue options** and **Crew in stores** now measure 142px and 141px collapsed, at the real
  457px panel width. They read as a level pair, which was the point.
- The third block, **Store rarity — where this sector differs**, is **cut from the design
  entirely** (user decision, 2026-08-16: "no page needs this"). It never appeared on Federation
  Space, which declares no `rarityList`; thirteen of the 19 pages render one today and none
  will after this. Delete `rarity_html()` and its `sector-vocab.json` `rarity` block. The
  extractor keeps emitting `crew_rarity` — it costs nothing, and `crew_store_odds` is computed
  from the same effective-rarity logic (SECTOR-PAGE.md §4.3c), which stays.

### 2.4 Blue options — per level, level in the name, top four, whole box clicks

Four changes, and the first needs the extractor:

1. **One row per option *and* level.** `rollup.gates` counts an option once however many levels
   it asks for, so Sensors 2 and Sensors 3 were one row of 7. They are now separate rows of 4
   and 5. The mock rebuilds this by walking `entries[].events[].gates[]`, which carry `lvl`,
   and mapping `req` → the rollup's merged label. **This belongs in `extract-sector.py`**: emit
   the per-level breakdown in `rollup.gates` so the renderer does not re-walk the pool.
2. **A system gate with no `lvl` folds into level 1 and reads `1+`.** `lvl` is a floor
   (`wiki/concepts/blue-options.md`), and a system you merely *have* is at level 1, so
   `req="teleporter"` with no level merges with `lvl="1"`. Teleporter went from `any 6` + `1 1`
   to **Teleporter 1+ 7** (distinct events, not a sum).
3. **A non-system gate carries no level at all.** Crew, augments and weapon lists have no
   level to ask for. Which ids are systems is read from `<systemBlueprint name=…>` in
   `blueprints.xml` + `dlcBlueprints.xml` — never a hand-written list. **This also belongs in
   the extractor**, as a per-gate `system: true|false`.
4. **The level lives in the option's name** — `Teleporter 1+`, `Sensors 3+` — in the blue
   option colour. The separate `.lv` chip is gone.

Also: **top 4 rows shown**, the rest behind the box itself, and the box is the toggle. A
`<details>` only toggles from its `<summary>`, so an open box could not be closed by clicking
its body; the mock adds a click handler on the box that ignores clicks inside the summary and
clicks that end a text selection. That script holds no English and no paths, so it belongs
beside `sector-cards.js`.

The explanatory note under the block ("A hit is one event…") is gone. **The hit-count
definition it carried is not stated anywhere else on the page** — §5.

### 2.5 Crew in stores

The panel was a 5-column table of 9 rows. It is now 2 columns of 5 lines, 141px against 265px:

- **Title is `CREW IN STORES`**, and it rides in the empty label cell of the first column's
  sub-header, so the heading costs no line of its own.
- **The `5 of 8 species · 3 slots` meta is gone.** With it went the only statement on the page
  that a store rolls three slots and that three species are excluded — §5.
- **Weight column dropped** (it is `6 − rarity`, and nothing is played off it). **Bar dropped.**
- **Percentages rounded to whole numbers.**
- **Two columns, down then across**: Human/Engi/Mantis/Rockman left, Zoltan plus the three
  never-sold right. Column-major keeps the rank scan top-to-bottom and lands the excluded
  species together as one block. It falls on a real boundary here — everything ≥44% in-store
  left, ≤17% right — which will not hold on every sector; check it per sector.
- **Species a store cannot sell stay in the table at 0%**, greyed. They are the
  `crewBlueprint`s whose effective rarity is 0 — here Slug, Crystal, Lanius. The mock reads
  the blueprints directly; **the extractor should emit them** in `crew_store_odds` (an
  `excluded: [{id, label}]` list) so the renderer never parses XML.
- Both prose notes, including the provenance line, are gone — §5.

The alternatives considered, with measured heights at the real width, are in
`sectors/mockups/crew-box-variations.html` (baseline 265px; the chosen shape 163px in
isolation, 141px on the page). Read it before proposing a different one.

### 2.6 Beacon budget

- **Each line's expansion now carries its section note and its Advanced Edition delta**, at the
  bottom, headed `Advanced Edition adds — OVERRIDE_<LIST>`, with the "whether the engine
  substitutes this list is not stated" caveat kept. Only lines with an AE twin get one — here
  `ITEMS`, `QUESTS`, `HOSTILE1`.
- **A legend replaces the old caption.** Three rows: solid blocks (blue and red together) =
  must be placed if the map has room; faded = may be placed; red = beacons that always put you
  in a fight.
- **Faded blocks state a chance, and it is "at least".** The line rolls one count between min
  and max, every outcome equally likely, so the k-th optional block is `P(roll ≥ k)`. `NEBULA`
  rolls 0–4: each count 20%, so the blocks read 80 / 60 / 40 / 20. Each block carries its own
  figure as a `title` tooltip.
- **The fill-in `NEUTRAL` row gets no percentages** — no roll governs it; it takes whatever the
  table leaves. Its blocks say so in their tooltip instead.
- **Generation notes cut from eight paragraphs to two**: the 6×4 grid at 80% per cell → at most
  24 beacons, lines filled top to bottom until they run out, remainder from `NEUTRAL`; then
  clouds, which convert a beacon to the `NEBULA` list, of whose 16 events 4 are plasma storms.
- The **entry-beacon line** and the **copy `callout`** are gone.

All of the above is `build-sector.py` + `sector-vocab.json`, except the callout, which is a
copy-file change in all 19 files.

### 2.7 Markers → two sections

`Beacon markers` split into two plain-titled sections: **DISTRESS SIGNALS** and **STORES**. All
four prose notes gone. The distress section keeps one italic line: *not every beacon from the
`DISTRESS` pool broadcasts a distress signal, and some of these show up in the neutral pools*.

**Every event row anywhere on the page now carries its marker tags** — `Distress signal` and
`Store marker` — derived from `rollup.markers`, so a row in a budget expansion says what the
map will show before you jump. In the mock this is a wrapper around `tags_html()`; it belongs
in `extract-sector.py` as two more derived per-event tags (§4.3's table), with `sector-vocab`
labels and a `.tg.distress` colour.

### 2.8 Pool sections — removed

Section 6 of the old page order is gone entirely. Every event it listed is one click into the
budget line that places it. This is what makes the page short enough for the rest to matter.

### 2.9 Footnotes — removed

The whole `<footer>` is gone. **This is the change most in tension with the spec** — S5 and
§6 item 9 exist precisely to keep provenance and open questions visible. §5 below.

---

## 3. The mock and how to run it

```bash
PYTHONIOENCODING=utf-8 python sectors/mockups/mock-federation.py
# → sectors/sector-federation-space-mock.html
```

`mock-federation.py` imports `tools/build-sector.py` as a module, reuses its data loading,
`event_html()`, `inline()`, `chain_html()`, `panels_html()` and `loader_html()`, and replaces
the parts that changed. **Every number still comes from
`sectors/data/federation-space.sector.json`** — the mock invents nothing, which is why it can
be trusted as a review surface. Its English is hardcoded, which is exactly what has to be
undone when this lands: those strings belong in `sector-vocab.json` and the copy file.

It appends `sectors/mockups/review-layer.html` to its output — see §4.

Two known smoke failures on the mock, both artifacts of it being a mock:
`no stat tiles` (§2.2) and `literal '*'`, which comes from the review layer's own JavaScript.

---

## 4. How the review loop works

The user reviews in the browser, not in chat. `sectors/mockups/review-layer.html` is a
self-contained commenting layer appended to any built page:

- Select text → **Comment** → type → save. The selection is highlighted.
- Notes persist in `localStorage`, keyed by filename, and survive a rebuild.
- **Copy for Claude** / **Download .md** exports them as markdown — quote plus note, in page
  order. The user drops the file in `~/Downloads`; read the newest `review-notes*.md` there.

Anchoring is by character offset into the page's visible text, not DOM paths, so a rebuild
keeps the highlights. A note whose quoted text no longer matches is kept as an orphan — still
exported, no longer highlighted. Consequences worth knowing when you edit a page under live
notes: **anything you add above an anchor shifts it**, and CSS pseudo-element content is not a
text node, so labels added that way do not move anchors at all.

The exported notes are terse and often anchor to the wrong element — the user selects whatever
is nearest to what they mean. Two from this round, both of which meant something other than
they said:

- *"remove all this"* on a 4,000-character selection meant "delete the pool sections", because
  the budget already shows those rows.
- Notes anchored to **Variation 0** of a variations page were not about the baseline; the user
  was using it as a canvas to draw the shape they wanted.

**Read a note against what the page is for, and say what you concluded when you report back.**

---

## 5. Open questions

Three were put to the user on 2026-08-16 and are **settled** — recorded here because the
reasoning matters later, not because anything is left to decide:

- **Provenance is dropped, not relocated.** No footer, no disclosure, no link out. The pages
  carry no sources, no "generation rules are community-derived" caveat, no `unique`-scope
  question, and no note that the store-crew percentages were read out of a disassembly.
  **`SECTOR-PAGE.md` §3 must be amended to exempt sector pages from S4 and S5 explicitly**, and
  §7's checks with it. An invariant that is silently violated is worse than one that says where
  it does not apply — and the evidence itself is not lost: it stays in `wiki/concepts/`
  (`blueprint-rarity.md`, `sector-event-allocation.md`, `event-uniqueness.md`) and in
  `raw/modding/2026-08-16-store-crew-selection-disassembly.md`.
- **`stats` is deleted from all 19 copy files**, and `build-sector.py` stops accepting the key.
- **The rarity block is cut from the design** (§2.3).

Still open, and none of them block the rollout:

1. **Is the min–max roll uniform?** The pages now print per-block percentages. The source says
   only "randomly choose between the minimum and maximum (inclusive)"
   (`raw/wiki/sectors.md`, community reverse-engineering). Uniform is the natural reading and
   is what the mock computes; it is still an assumption stated as a number on the page.
2. **Is a level-less system gate the same as level 1?** §2.4 merges them. Sound for systems
   (having one means level 1), but no file says so.
3. **What is lost with the removed meta**: the store slot count (3, AE) and the fact that some
   species are excluded now appear only as tooltips and 0% rows. Acceptable, or does one line
   come back?
4. **The hit-count definition** ("a hit is one event that offers it, not one beacon") no longer
   appears anywhere.
5. **File the naming contradiction** from §2.1 in `wiki/sectors/federation-space.md` per
   CLAUDE.md §4 — game files vs what the map shows.
6. **Two dummy `crewBlueprint`s**, `battle` and `repair`, are rarity 0 like the three excluded
   species but are never shown to a player — the files mark them `NOLOC="1"` with the desc
   "Dummy blueprint needed now." The extractor filters on `NOLOC`, so `excluded` carries three
   species rather than five. Derivable, but not a rule any file states.

---

## 6. Rolling this out to the other 18 sectors

Order matters.

1. ~~**Settle the blocking decisions with the user.**~~ **Done, 2026-08-16** — §5.
2. ~~**Extractor first.**~~ **Done, 2026-08-16.** `rollup.gates` entries now carry `system` and
   `levels_detail` (per-level rows, de-duplicated by event id, a level-less system gate folded
   into `"1"` and a non-system gate as one `lvl: null` row); `crew_store_odds.excluded` lists
   the species a store here cannot sell; and every event record carries `distress` /
   `store-marker` tags matching `rollup.markers` exactly. All 19 re-extracted, additive only —
   pages built from the new data are byte-identical to the old.

   Two things step 3 must know. **The marker tag is `store-marker`, not `store`** — `store`
   already means "a store opens in this tree", which is a narrower set, so the mock's
   `.tg.store` CSS has to be pointed at the new name deliberately. And the built pages in the
   tree are **stale against `sector-page-render.html`** by a 5-line CSS comment block that
   predates all of this; it lands on the next rebuild and is not a regression.
3. ~~**Vocabulary and renderer.**~~ **Done, 2026-08-16.** `sector-vocab.json` rewritten (rarity,
   footnotes, pool-section and stat-tile words gone; legend, block tooltips, marker tags and the
   two generation paragraphs in); `build-sector.py` drops `stats_html`, `rarity_html`,
   `pool_sections` and `footnotes`, and `sector-page-render.html` carries the mock's CSS.
   `tools/sector-toggle.js` is the new toggle script, inlined the way `sector-cards.js` is.

   Three things step 4 must know. **`stats` and `callout` are accepted and ignored**, not
   rejected — a hard failure before the copy pass would leave the tree unbuildable; they are
   `DEAD_KEYS` in `build-sector.py` and should leave `COPY_KEYS` once all 19 copy files are
   clean. **The legend's worked example needed a second wording**: the mock's "80% for one" is
   only true where the example line's minimum is 0, so a line that already guarantees blocks
   renders `legend.may_offset` instead. And **two of the eight old paragraphs came back as
   conditional third lines** (user decision, 2026-08-16), because both state something no block
   on the page shows: `generation.fallback_also_allocated` on the two Slug nebulas, where
   `NEUTRAL` is a numbered line *and* the fill-in row and the budget otherwise reads as a
   doubled row, and `generation.cannot_meet_minimum` on Hidden Crystal Worlds, which allocates
   25 against a 24-beacon ceiling. The other 16 pages keep the two-paragraph note exactly.
4. **Copy files.** Every sector needs: a shortened lede, `callout` removed, `stats` deleted,
   and any panel that duplicated a now-deleted section removed — on Federation Space that was
   **Reading the map here**, whose cloud paragraph moved into the generation note. Expect the
   same panel to exist under other names elsewhere.
5. **Update `SECTOR-PAGE.md`.** §6's page order, §6.2's block descriptions (the rarity block is
   gone), §7's failure list (no stat tiles, no footnotes), §4.3's tag table (the two marker
   tags), §5's copy schema (no `stats`, no `callout`), and §3's S4/S5 exemption per §5 here.
   When this document and the spec agree, delete this document.
6. **Verify per sector**: `smoke-sector.py` and `smoke-inline.py`, plus a real look at the
   glance row — the two panels are only level because their content happens to balance on this
   sector, and nothing enforces it.
7. **Review with the user, one sector at a time**, using §4's loop. Do not batch 18 pages into
   one review; the notes come back anchored to a page, and they are worth more per page than in
   bulk.

Sectors likely to stress the new shape: **Hidden Crystal Worlds** (allocates 25 against a
24-beacon ceiling, so its fill-in row is a zero row), **The Last Stand** (no glance section at
all — nothing to level the crew box against), the two **Slug nebulas** (allocate the fallback
list by name as well), and the thirteen sectors whose pages lose a whole glance block when the
rarity panel goes (§2.3) — check the remaining two still balance there.
