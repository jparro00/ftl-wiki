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
| `tools/sector-copy/<slug>.json` | the words for one sector | **yes — this is the authoring surface** |
| `tools/smoke-sector.py` | renders a built page as text and checks it | code only |
| `sectors/data/<slug>.sector.json` | generated profile (regenerable data, not a page) | never |
| `sectors/sector-<slug>.html` | the built page; publish target | never |

Inputs consumed:

- `raw/gamedata/sector_data.xml` — the allocation table: every count on a page comes from here
- `raw/gamedata/events*.xml`, `newEvents.xml`, `dlcEvents*.xml` — event-list membership
- `raw/gamedata/text_sectorname.xml` — the sector's in-game display name
- `raw/gamedata/blueprints.xml` + `text_blueprints.xml` — crew names for the rarity panel
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

**`fleet_delay` is signed, and the name is misleading.** It carries `modifyPursuit` verbatim:
**negative delays the fleet (good for you), positive advances it (bad)**. `AUTO_WARNING`'s
escape branch is `fleet_delay: 1` — the scout reporting your position, not a reprieve. Read
the sign before writing a sentence about it (EVENT-CARD.md §6 records the same trap).

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

- `beacons_min`, `beacons_max`
- `distinct_events`, `always_fight_events`, `may_fight_events`, `crew_loss_events`,
  `crew_gain_events`, `boarder_events`, `unique_events`, `gated_events`, `quest_start_events`
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

  "panels": [                         // required, 2–4. A fifth, "Crew in stores", is added
    {                                 // automatically from the data — do not write one.
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

---

## 6. Stage 2 — rendering

`build-sector.py` validates the copy, renders the content, and injects it into
`sector-page-render.html` at the `<!--SECTOR-CONTENT-->` marker, stamping the `<title>`.
Everything is inlined; the page loads nothing at runtime, because a published artifact runs
under a CSP that blocks network requests.

Page order, all of it derived except where marked:

1. **Header** — eyebrow (`Sector profile · <ID>`), title, *lede (copy)*, fact chips
2. **Stat tiles** — *labels from copy*, numbers from metrics
3. **Beacon budget** — one row per entry, solid blocks for `min`, faded for `max − min`;
   hostile and boarder rows are red. Then the legend, the entry beacon, and the *callout (copy)*
4. **Pool sections** — one per entry, in section order, each row a card-derived title, id and
   tags; *section note (copy)*; the AE delta block where one exists (§4.4)
5. **Quest chain** *(copy, optional)*
6. **Panels** — *copy*, plus the generated crew-rarity panel
7. **Footnotes** — sources, and one clause per condition that applies: the `unique` scope
   question, the no-weights rule, ambiguous entries, inline outcomes with no id, missing trees

---

## 7. Verification

```bash
python tools/smoke-sector.py sectors/sector-<slug>.html   # required before publishing
```

Parses the built page, prints **everything it can show** — title, facts, tiles, budget rows,
every pool row with its tags, notes, chain steps, panels and footnotes — and fails on:
unbalanced tags, an unstamped title, a stat tile that is not a number, an empty event row, a
missing budget, and any `{{…}}` or `**` that survived into the output.

It does not check CSS, layout, colour or theming. It cannot check whether a sentence is true —
that is what rule 1 in §5 is for.

Determinism check — build twice and diff:

```bash
python tools/build-sector.py <slug> -o /tmp/a.html
python tools/build-sector.py <slug> -o /tmp/b.html
diff /tmp/a.html /tmp/b.html
```

---

## 8. Where fixes go

| Symptom | Fix in | Never in |
|---|---|---|
| A sentence reads wrong | `tools/sector-copy/<slug>.json` | the built HTML |
| A shared word or heading reads wrong | `tools/sector-vocab.json` | the renderer |
| A pool is missing an event, or a tag is wrong | `extract-sector.py`, then re-extract | the data JSON by hand |
| A tag is wrong *for one event* | that event's tree — `extract-event.py` | `extract-sector.py` |
| Layout, colour, spacing | `sector-page-render.html` (changes all 19 pages) | one page |
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

- A pool row shows the event's title and tags, not its outcomes. The card is one click away in
  `cards/card-<slug>.html`, but the pages do not link to each other — artifact URLs are minted
  at publish time and are not knowable at build time.
- `distinct_events` counts every event any entry can produce, including the store and empty-
  beacon events. It is a measure of pool breadth, not of interesting encounters.
- **Every metric covers the allocated pool only — the `startEvent` is excluded.** That matters
  on Hidden Crystal Worlds, where `START_BEACON_CRYSTAL` itself plants the ship-unlock quest
  marker and `quest_start_events` still reads 0. Check `start_event` in the data before
  writing that a sector has none of something.
- The crew-rarity panel reads `rarityList`, which also carries non-crew blueprints in some
  sectors (`BOMB_LOCK` in Rock Controlled). They are shown as listed rather than filtered,
  because the file gives no way to tell a crew blueprint from any other.
- Two allocation systems exist in the data and this pipeline reads only the first
  (`sector_data.xml`). If `<eventCounts>` in `newEvents.xml` is live, some sectors draw from
  lists no page here shows. See `wiki/concepts/sector-event-allocation.md`.
