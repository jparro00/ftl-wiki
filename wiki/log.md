# Log

Append-only, chronological record of every ingest, query-that-was-filed, and lint.
**Newest entries at the bottom.** Each entry header starts `## [YYYY-MM-DD] <op> | <title>`
so entries stay greppable (`grep "^## \["`).

Entry template:

```
## [2026-08-09] ingest | events.xml (Rock sector block)
- Source: [[source-events-rock]] (raw/gamedata/events_rock.xml)
- New pages: [[event-...]], [[sector-...]]
- Updated: [[item-...]] (added drop source)
- Deferred: 40 events in the same file, not yet paged
- Contradictions: none
```

---

## [2026-08-09] ingest | Raw layer populated — game data + Fandom

Sourcing pass, no wiki pages written.

- **raw/gamedata/**: 33 XML files extracted from the user's own `ftl.dat`
  (`PKG\n` format = **1.6.x Advanced Edition**). Read-only extraction via `tools/ftlpkg.py`,
  written against Slipstream Mod Manager's `PkgPack.java`. Game install unmodified.
  See `raw/gamedata/_PROVENANCE.md`.
- **raw/wiki/**: 291 event pages pulled from ftl.fandom.com as wikitext via `api.php`,
  0 failures, plus `_manifest.csv` with revision ids.
- Corpus measured: **460 event ids, 301 event lists, 21 sectors, 3,298 text strings**.
- Note: `WebFetch` gets HTTP 402 from Fandom's CDN; the API works from PowerShell.

## [2026-08-09] ingest | sector_data.xml + text_sectorname.xml — full sector layer

- Sources: [[source-sector-data-xml]], [[source-text-sectorname-xml]]
- New pages (20): every sector page — all 21 in-game sector ids covered.
- Findings: `min`/`max` are **beacon counts, not probabilities**; two vestigial stub
  sectors filed as [[sector-vestigial-definitions]]; the `ABANDONED_SECTOR` /
  `LANIUS_SECTOR` name trap recorded.
- Gap: no hostility/map-colour flag exists in the data, so `sector_class` is `unknown`
  on the faction sectors.
- Contradictions: none.

## [2026-08-09] ingest | ROCK_CRYSTAL_BEACON — first event, both source layers joined

- Sources: [[source-events-xml]], [[source-text-events-xml]], [[source-fandom-ancient-device]]
- New pages: [[event-ancient-device]], [[chain-crystal-cruiser-unlock]],
  [[item-crystal-vengeance]], 5 source pages.
- **The join works.** Fandom's title "Ancient device" shares nothing with the in-game id
  `ROCK_CRYSTAL_BEACON`; the page's Notes section names the id. `event_name:` confirmed as
  the join key, and it must be read from page text, not inferred.
- Contradictions: 1 (choice-3 wording, game files vs Fandom).

## [2026-08-09] ingest | Event corpus — 22 batches across 5 waves

The bulk ingest. 421 top-level events partitioned by source file and processed in waves of
five parallel passes, each working from the game XML with the Fandom page as a secondary
source. 37 sub-events were deliberately folded into their parent pages.

- **New pages: 378 events**, plus ~300 `fandom-*` source pages.
- **Method corrections made mid-run** (each caught by a pass and applied to later waves):
  - The Fandom join over-matched: event ids double as enemy-ship ids, so a bare string
    match pulled in unrelated pages. Re-based the join on pages that *declare* their id.
  - The batch JSON was lossy (dropped nested choices, sub-event trees, `autoReward` payload
    types). Demoted it to a work list; `raw/gamedata/` made the stated source of truth.
  - `unreachable` was being inferred from missing `sector_data.xml` allocation. Tightened to
    require positive evidence — see [[concept-sector-event-allocation]].
  - `version: ae` was being used to mean "extracted from the AE build". Corrected to mean
    *Advanced Edition only*; see the retrofit entry below.
- **Declined pages, with reasons recorded:** ~33 test/dev stubs and UI system messages,
  10 event-list allocation buckets.
- Contradictions: recorded on individual pages throughout. The dominant pattern is Fandom
  stating percentages and aggregated damage totals where the files state reward *levels*
  (`LOW`/`MED`/`HIGH`) and separate damage tags.

## [2026-08-09] query | The `<surrender chance>` semantics

- Question: four ingest passes independently flagged `<surrender chance="0">` as an
  unresolvable contradiction.
- Filed: [[concept-surrender-offers]]
- Finding: `chance` is the probability the ship **keeps fighting**; surrender chance is
  `1 − chance`. Three independent lines of evidence. Both sources turn out to be right
  about different quantities.
- Cited: [[source-events-ships]], [[source-fandom-rock-fight]], [[source-fandom-pirate-briber]]

## [2026-08-09] query | Whether derived odds are sound

- Question: rule-9 derivations assume the engine selects uniformly across event-list entries.
- Filed: [[concept-event-list-weighting]]
- Finding: confirmed. Fandom independently states 9%, 36.4% and 16.7% for the out-of-fuel
  family; uniform selection reproduces all three exactly. Also dates Fandom's fuel pages to
  AE, which they never state.
- Cited: [[source-events-fuel]]

## [2026-08-09] query | Two allocation systems

- Question: how `<eventCounts>` in `newEvents.xml` relates to `sector_data.xml`.
- Filed: [[concept-sector-event-allocation]]
- Finding: unresolved, and precisely scoped. Established that absence from
  `sector_data.xml` does **not** prove unreachability (`NEUTRAL_EXIT` and
  `FEDERATION_BASE_ASSIST` have zero allocations and are plainly live). Whether the engine
  reads `eventCounts` cannot be settled from the data.

## [2026-08-09] ingest | Entity, item, chain and concept layers

- New pages: **11 entities**, **64 items**, **6 chains**, **6 concepts**.
- The item layer closed the largest structural gap: every `[[item-...]]` link across all
  event pages now resolves, and each item page indexes the blue options it gates.
- Chain note: an "Engi Cruiser unlock" chain was requested and **declined with evidence** —
  `ENGI_UNLOCK_1→4` awards `<unlockShip id="1"/>`, the Stealth Cruiser. The Engi Cruiser is
  an achievement unlock, not an event chain. Recorded on [[chain-stealth-cruiser-unlock]].
- Pattern found across unlock chains: three of them **silently fail on the obvious play** —
  destroying the ship instead of forcing surrender or killing the crew carries no `<quest>`
  tag and ends the chain.

## [2026-08-09] ingest | Gap pass — every remaining event id triaged

- Source: a coverage audit of all 460 game event ids against every page's `event_name:`.
- New pages: **17**, incl. the ship-block aftermath events (`PIRATE_SURRENDER`,
  `PIRATE_ESCAPE`, `ROCK_SHIP_SURRENDER`, `LANIUS_SURRENDER`) that carry their own join keys.
- Declined with reasons: 33 stubs/system messages, 10 allocation buckets, 22 pure outcome
  branches — each of the 22 verified as already documented in its parent page.
- Contradictions: [[event-boss-fleets-both]] — in no event list, yet named in its own file's
  header as a live event. Both readings recorded; not tagged `unreachable`.

## [2026-08-09] lint | Consistency pass

- **Coverage audit:** 460 event ids defined, 395 paged, 0 duplicate `event_name` claims,
  0 pages claiming a non-existent id. Remaining ids are declined-with-reason.
  - Two bugs were found *in the audit itself* and fixed: comment-stripping across a
    malformed nested comment swallowed real definitions, and the id regex missed
    `<event name = "X">` with spaces around the `=`.
- **`version:` retrofit:** 166 pages corrected `ae` → `both`. `ae` means Advanced Edition
  *only*; pages defined in `dlcEvents*.xml` or justified in-body as AE-only were preserved.
  Final distribution: 296 `both`, 96 `ae`, 3 `unknown`.
- **Link repair:** 110 files. Cross-agent slug mismatches resolved through the `event_name`
  join key (e.g. `[[event-asteroid-derelict-ship]]` →
  [[event-dense-asteroid-field-distress]]), plus entity name-variant normalisation.
- **Backlinks:** 97 added across 79 pages, making the new gap pages bidirectional.
- **Corrections to earlier work:** [[concept-surrender-offers]] undercounted `chance="0"`
  ships (3 → 4); two Rock pages falsely claimed no Fandom page covered them; 4 wrong source
  slugs; 23 duplicate adjacent wikilinks.
- **Rebuilt** `index.md` from page frontmatter, grouped by sector.

## [2026-08-09] tooling | Event cards generated from the XML instead of hand-written

Cards were hand-transcribed from the wiki markdown into HTML, which is the risk
`tools/EVENT-CARD.md` had already flagged. Replaced with a three-stage pipeline:

```
raw/gamedata/*.xml → wiki/events/<slug>.tree.json → card HTML → Artifact
                   ▲                              ▲
             extract-event.py                build-card.py + card-vocab.json
```

- **New:** `tools/extract-event.py` — indexes every `<event name>`, `<eventList name>`,
  `<ship name>`, `<textList name>` across 19 event files plus the `text_events.xml` string
  table, then resolves one event into `ftl-event-tree/1` JSON. Follows `load=` across
  files, pulls ship branches from `events_ships.xml`, reads `<!--DLC-->` markers per
  element, guards recursion.
- **New:** `tools/card-vocab.json` — every English word a card shows that is not verbatim
  game text (effect phrasing, block headings, gate labels, derived footnotes). Shared by
  all cards; the renderer holds no wording of its own.
- **New:** `tools/build-card.py` — inlines the event tree + vocabulary into the shell.
  Inlined rather than fetched: artifacts run under a CSP that blocks all requests, and
  `file://` blocks cross-origin reads.
- **Rewritten:** `tools/event-card-render.html` — depth-driven indentation (was capped at
  3 levels), per-payload tone, merged duplicate list entries, gate chips replacing the
  requirement the game text already carries.
- **New pages:** [[concept-event-tree-grammar]] — the grammar and its tag census, cited to
  [[source-events-xml]], [[source-newevents]], [[source-dlceventsoverwrite]],
  [[source-events-ships]], [[source-events-pirate]], [[source-text-events-xml]].
- **Trees extracted:** [[event-auto-ship-attacking-civilian]] (`AUTO_CIVILIAN`),
  [[event-single-life-form-on-moon]] (`STRANDED_BEACON`), [[event-crushed-pirate]]
  (`DISTRESS_TRAPPED_MINER`), [[event-escape-pod]] (`MANTIS_CREW`).
- **Docs updated:** `tools/EVENT-CARD.md` rewritten around the pipeline; `CLAUDE.md` §5.2b
  and the directory layout; §6 gains a `tooling` log op; `README.md` gains a card section.
- **Gate labels resolve from the data too:** a `req=` naming a blueprint
  (`BEAM_BIO`, `BATTLE`, `ADV_SCANNERS`) is looked up in `blueprints.xml` /
  `dlcBlueprints.xml` via `text_blueprints.xml`, so cards show "Anti-Bio Beam" and
  "Anti-Personnel Drone" without a hand-written label. Only systems, species and
  `blueprintList` gates need vocabulary entries.
- **Backlinks:** 8 pages now link [[concept-event-tree-grammar]].

**Errors the extraction caught in the hand-built cards** — all four had been flattened:
`SAVE_CIVILIAN_LIST` entries 1 and 4 carry their own choices; the `destroyed` branch has a
hidden "Contact the civilian ship" choice; the `PIRATE` `deadCrew` list is 9 entries with
5 duplicates; `PIRATE` publishes real `chance="0.5"` surrender and escape odds that no card
had shown.

**Deferred:** `tools/event-card-template.html` is superseded and unused, not deleted.
The `.tree.json` sidecars are not listed in `index.md` (they are data, not pages).

## [2026-08-09] tooling | Quest chains, and a dropped-choices bug in the extractor

- **Chains followed.** `<quest event="X"/>` marks a beacon the player flies to later, so it
  is not an outcome of the triggering event. The extractor now follows quest markers
  breadth-first into a `chain[]` beside the tree — transitively
  (`ROCK_UNLOCK1` → `ROCK_UNLOCK2` → `ROCK_UNLOCK3`), across events *and* event lists, with
  a visited set, since several paths can plant the same marker. Repeats are emitted as
  `{"repeat": true}` rather than re-expanded. Cards render each stage as its own card below
  the main tree.
- **Bug fixed — `<ship>` and `<choice>` are not exclusive.** `node()` returned the combat
  node whenever an event had a ship, silently discarding the whole choice menu.
  `ROCK_UNLOCK1` (three choices, two of which plant the quest marker) and
  `ZOLTAN_PEACE_QUEST2` (an "Attack." choice) were both truncated. A decision now keeps the
  ship under `combat` and the card shows the fight as a second block.
  [[concept-event-tree-grammar]] corrected: it claimed "exactly one continuation".
- **Ship names derived.** `auto_blueprint` resolves through `shipBlueprint` → `<class>` to
  the name the player sees ("Energy Fighter"); a `blueprintList` of 2–3 distinct classes
  resolves to all of them ("Energy Fighter or Energy Bomber"). Dropped the hand-written
  `REBEL_AUTO_CIVILIAN` vocabulary entry — `SHIPS_AUTO` now resolves itself.
- **New:** `tools/smoke-card.js` — runs a built card's renderer against a DOM shim and
  prints the tree. It caught three defects this session that reading the file did not.
- **Trees extracted:** [[event-zoltan-peace-quest2]] now appears as a chain stage of
  `ZOLTAN_PEACE_QUEST` (`wiki/events/zoltan-peace-envoy.tree.json`).
- **Docs:** `tools/EVENT-CARD.md` gains the chain schema and the smoke-test step;
  [[concept-event-tree-grammar]] gains a Quest chains section and the exclusivity warning.

## [2026-08-10] tooling | Titles, slugs and punctuation moved out of the code

- **Audit finding:** formatting literals had drifted back into the renderer during the
  chain work — the `→` before each effect, the `, ` between effects, `%` on a ship's
  `chance`, the parentheses around a gate, `1.` numbering, the quotes around the hail, the
  expand caret, and an English `" or "` fallback. All twelve moved to a `format` block in
  `tools/card-vocab.json`; the renderer now holds no English and no punctuation of its own.
- **Titles and slugs are data now.** `tools/extract-event.py` builds an index of
  `event_name:` → (filename, H1) across all 395 `wiki/events/*.md` pages and uses it for
  the card title and the tree's slug. The game files have no human title — FTL never shows
  the player an event name — so the wiki layer is the only source, and the `event_name`
  join key already existed for exactly this kind of lookup. `--slug` / `--title` remain as
  overrides. Chain stages pick up their own page titles too, so the Zoltan quest beacon is
  headed [[event-zoltan-peace-quest2]]'s title rather than a generic label.
- **Consequence:** `python tools/extract-event.py AUTO_CIVILIAN` is now the whole command;
  the only per-card input is the event id.
- **Renamed:** `zoltan-peace-envoy.tree.json` → `unarmed-zoltan-transport.tree.json`, since
  the join resolves `ZOLTAN_PEACE_QUEST` to its actual page
  [[event-unarmed-zoltan-transport]]. The published card keeps its old filename so its URL
  survives.
- **Docs:** `tools/EVENT-CARD.md` records the join, the `format` block, and three
  judgement calls that remain in code (the 2–3 class threshold for ship lists, the
  leading-parenthetical strip on gated labels, and raw ids printing when the vocabulary has
  no entry). `CLAUDE.md` §5.2b updated to the one-argument command plus the smoke step.

## [2026-08-10] tooling | Cards built, and the docs caught up to them

- **Trees extracted** (6, all regenerable from the game XML — data, not pages):
  [[event-auto-ship-attacking-civilian]], [[event-single-life-form-on-moon]],
  [[event-crushed-pirate]], [[event-escape-pod]], [[event-unarmed-zoltan-transport]]
  (carries the [[event-zoltan-peace-quest2]] chain stage), [[event-deactivated-auto-ship]].
- **[[event-deactivated-auto-ship]]** (`BROKEN_REBEL_DRONE`, from the `NEUTRAL_ENGI` pool of
  [[sector-engi-controlled-sector]]) is the deepest card so far: the Sensors 3 branch runs
  five levels, it has a ship at the beacon *and* a menu, and it is the first card to use the
  `reveal_map` effect. Ran clean with no pipeline changes.
- **Docs squared up:** `wiki/index.md` explains the `.tree.json` sidecars and why they are
  not catalogued; `wiki/overview.md` gains an Event cards section and its Concepts count
  corrected 9 → 10 for [[concept-event-tree-grammar]]; `tools/EVENT-CARD.md` records two
  more rough edges — identical subtrees repeat across branches (the auto-ship fight renders
  three times in `BROKEN_REBEL_DRONE`, since merging collapses siblings only), and depth is
  now exercised to five levels.
- **Not done:** no `chain` page exists yet for the Zoltan peace quest even though the tree
  now maps both stages; [[chain-...]] pages and `.tree.json` chains are still separate
  representations of the same thing.

## [2026-08-10] tooling | deadCrew reachability derived from crewCount

- **Correction.** Earlier notes claimed reachability was not derivable and that
  `auto_blueprint` was an unreliable signal. Half right: the *list name* is unreliable, but
  each hull's blueprint states the answer — `AUTO_BASIC` and `AUTO_ASSAULT` carry
  `<crewCount amount="0" max="0"/>` ([[source-autoblueprints]]). No crew aboard means the
  `deadCrew` branch cannot fire.
- **Implemented:** the extractor indexes `crewCount` per `shipBlueprint`, and a combat node
  marks `deadCrew` `"reachable": false` when every hull the ship can draw is crewless. The
  renderer omits unreachable branches; the JSON keeps them with
  `unreachable_because`, so nothing is lost from the record.
  Conservative by design: an unknown blueprint counts as crewed.
- **Effect:** [[event-auto-ship-attacking-civilian]] and [[event-deactivated-auto-ship]]
  lose a phantom "You kill the crew" branch each (three of them on the latter, which reaches
  the same fight from three paths). [[event-crushed-pirate]],
  [[event-unarmed-zoltan-transport]] keep theirs — `PIRATE`, `REBEL` and the Zoltan hulls
  carry crew.
- **Docs:** the rough edge is deleted from `tools/EVENT-CARD.md` and replaced with a derived
  behaviour; [[concept-event-tree-grammar]] corrected — it had asserted reachability was
  unmarked, when it is stated one file over.

## [2026-08-10] tooling | Attached ships read as choices; bare hostility flips were dropped

Both surfaced from one question about [[event-deactivated-auto-ship]]: why its card ended
with a "You destroy it" row that looked like a fourth option.

- **Attached combat now has its own row.** A ship attached to a decision was rendered as a
  flat block of branches after the choices, so the derelict's `destroyed` branch read as a
  menu item. It now collapses into a single row worded from the vocabulary — "If you attack
  it yourself" for a `hostile="false"` ship, "If the fight starts" for a hostile one.
- **Bare `<ship hostile="true"/>` was being ignored.** With no `load`, it flips the ship
  already at the beacon rather than introducing one, and the extractor only handled ships
  that named a hull. 96 uses across the files. Now a `ship_hostility` effect, so
  [[event-zoltan-peace-quest2]]'s "Attack." choice reads *the ship turns hostile* instead of
  *nothing happens* — a wrong statement on a card, not just a missing one.
- **Docs:** `tools/EVENT-CARD.md` and [[concept-event-tree-grammar]] both record the bare-
  `<ship>` state-change form, which the grammar section had not distinguished from a ship
  reference.

## [2026-08-10] tooling | A non-hostile ship is not a fight the player can pick

Correction to the previous entry. Attached combat was given a row labelled "If you attack
it yourself" — which asserts a game mechanic no source here establishes, and which the user
disputes: at an event dialog you choose from the listed options.

- The card now shows an attached fight **only when the event can start it** — the ship
  arrives `hostile="true"`, or an option flips it with a bare `<ship hostile="true"/>`.
- A ship that arrives non-hostile and is never flipped is marked `"reachable": false` with a
  reason and omitted, the same treatment as a `deadCrew` branch on a crewless hull.
- [[event-deactivated-auto-ship]] loses the row entirely: its `REBEL_AUTO` derelict is never
  activated by any option, and the fight players actually meet is a *separate* hostile
  `REBEL_AUTO` loaded inside choice 1's bad roll, which has always rendered under that
  choice. [[event-zoltan-peace-quest2]] keeps its row — its "Attack." choice does flip the
  Rebel ship.
- The `attached_combat.passive` wording is deleted from `tools/card-vocab.json`; only the
  neutral "If the fight starts" remains.
- [[concept-event-tree-grammar]] gains the rule: a non-hostile `<ship>` on an event with
  choices is scenery unless something flips it.

## [2026-08-10] tooling | Certain tables collapse; counts as digits

- **"1 of 2" over a single row.** When every entry of an `eventList` is identical, merging
  leaves one row and the heading still claimed a random draw. The outcome is in fact
  certain, so the renderer now folds such a table into the row above:
  [[event-deactivated-auto-ship]]'s reactivated fight reads `You destroy it → medium scrap`
  rather than a "1 of 2" block containing one line. Verified across all six cards that no
  block heading now sits over a single row.
- **Numerals.** `one of {n}` → `1 of {n}` in `leads` and `block_labels`
  (`tools/card-vocab.json`), matching the `×3` count chips.
- Both are renderer/vocabulary changes; no tree was re-extracted, and the underlying JSON
  still records every list entry.

## [2026-08-10] tooling | The "always" chip on blue options was meaningless

Removed. The chip was stamped on every gated row unconditionally, and it did not survive
scrutiny:

- It did not mean "guaranteed outcome". [[event-deactivated-auto-ship]]'s Sensors 3 row
  carried `always` and then expanded into a 1-of-2 random table.
- It did not mean "deterministic branch" either, since ungated certain rows — that card's
  "Don't risk activating it → low scrap", or [[event-unarmed-zoltan-transport]]'s "Hear them
  out" — never carried any chip.
- What it actually marked was "this row has a gate", which the blue row colour and the
  `(Sensors 3)` prefix already say twice.

The chip column now means one thing only: **this branch is one of several possible
outcomes** (`1 of 2`, `×3`, `50%`). Certainty gets no chip, gated or not. `gate_chip` is
deleted from `tools/card-vocab.json` and the `.odds.hit` style, which existed only for it,
is gone from the shell. Zero `always` strings remain across the six cards.

## [2026-08-10] tooling | A triggered fight now renders under the row that triggers it

[[event-auto-ship-near-storage-station]] (`AUTO_DEFENSE_ITEM`) showed its fight as a row at
the bottom of the menu rather than under "Attack the automated ship". That was an artifact
of the XML — the ship is on the *event* and the hostility flip is on the *choice* — not
something the player experiences, and it broke the card's basic grammar, where a row's
consequences hang beneath it.

- The beacon's ship is now passed down the tree as an **ambient** ship. Any row whose
  effects include `ship_hostility` renders that fight as its own children.
- `AUTO_DEFENSE_ITEM` reaches it from two rows — choice 1 and the Cloaking option's failure
  half — so the fight renders under both, consistent with the existing rule that identical
  subtrees repeat wherever the data reaches them.
- A standalone "If the fight starts" row now appears **only** for a ship that arrives
  `hostile="true"`, which belongs to no single choice. Zero such rows across the seven
  cards today.
- [[event-zoltan-peace-quest2]]'s "Attack." choice picked up the same fix.
- Also fixed: `tools/smoke-card.js` matched `className === "row"` exactly, so it had been
  silently hiding every gated row since the blue-option colour change — the harness was
  under-reporting while I was using it to verify. Now matches the first class name.

## [2026-08-10] tooling | EVENT-CARD.md rewritten as a specification

The card docs had grown as a running record of this session's corrections. Rewritten so an
agent with no prior context can build, verify, publish and extend cards from that one file.

- **Structure:** quick start · components and inputs · six invariants (I1–I6) · extraction
  rules (parsing, grammar, the effect table, combat, reachability, chains, the title/slug
  join) · the full `ftl-event-tree/1` field reference · a `card-vocab.json` key reference ·
  fifteen numbered rendering rules (R1–R15) · verification · a "where fixes go" table ·
  publishing · pitfalls · known limits.
- **Derived from the code, not memory.** The vocabulary key list, the effect-kind table and
  the schema field list were enumerated from `card-vocab.json`, `extract-event.py` and the
  seven existing trees, then cross-checked: every vocabulary key including `format`
  sub-keys appears in the spec, and twelve spec claims were verified present in the
  implementation.
- **Pitfalls are recorded as pitfalls** — the harness class-match bug, the unanchored
  `<title>` regex, the `label`/`klabel` shadowing, `fill_block` with no node, cp1252
  console encoding, and never assuming a slug from an event id.
- `CLAUDE.md` §5.2b now names it normative and authoritative over the summary there.

## [2026-08-10] tooling | Cold-start test of the spec, and the bug it found

A fresh agent with no conversation context was given only "build an event card for
`ROCK_UNLOCK1`" and the repository. It found `tools/EVENT-CARD.md` by grep, followed the
pipeline unaided, ran the determinism check on its own initiative, and published a correct
card — including the chain inversion (destroying the step-2 ship *ends* the quest; only
`gotaway` leads to the ship unlock).

Its findings, verified and acted on:

- **Real bug — awarded items showed raw ids.** `extract-event.py` resolved blueprint titles
  for *gates* but not for `augment`/`weapon`/`drone` effects, so
  [[event-rock-unlock1]] displayed `ROCK_ARMOR` instead of **Rock Plating**. Every card
  awarding a named blueprint was affected. Fixed: the item effect now carries `label`
  (title, falling back to the id) and the vocabulary renders it. All 8 trees re-extracted,
  all 8 cards rebuilt.
- **Genuine documentation gap — where built cards live.** The spec never said. Now
  `cards/card-<slug>.html`, which is also `build-card.py`'s default (previously it wrote
  beside the tree, putting build artifacts in the `wiki/` layer).
- **False positive worth recording:** the agent reported `CLAUDE.md` §5.2b as stale, quoting
  the retired `event-card-template.html` and a `SendUserFile` delivery step. The file on disk
  says neither — it was reading the copy injected into its context at session start, which
  predated this session's edits. A subagent's ambient `CLAUDE.md` can lag the disk; the spec
  being the normative source is what limited the damage.

## [2026-08-10] tooling | CLAUDE.md §5.2b reduced to what cannot rot

Follow-up to the cold-start test. The subagent misreported §5.2b as stale because it was
reading the copy injected into its context at session start, not the file on disk. The
content that misled it was precisely the part that **duplicated** `tools/EVENT-CARD.md` —
the command sequence.

- §5.2b no longer restates commands, flags or output paths. It keeps the trigger (a
  screenshot always means build a card), the four rules that are behaviour rather than
  mechanism (identify by id, never hand-edit HTML, publish via Artifact, no meta), and an
  explicit statement that the spec is read fresh from disk while this file may lag.
- The pipeline diagram stays as orientation; it names components, not invocations, so it
  cannot go stale the way a command line can.
- `cards/` added to the directory layout in §1.

Principle worth keeping: **duplicated normative content in an injected file is a liability,
because a reader cannot tell whether their copy is current.** Detail belongs in the file an
agent has to open.

## [2026-08-10] tooling | Official home for built cards: cards/

`cards/card-<slug>.html` is now stated as the official location in all three places a reader
might look: `tools/EVENT-CARD.md` §9 (as a rule, with the reasoning — derivable path, stable
URL, generated artifact kept out of the `wiki/` layer, safe to delete and rebuild),
`CLAUDE.md` §1's directory layout, and `README.md`'s layout block and card section.
It is also `build-card.py`'s default, so the zero-argument path is the correct one.

## [2026-08-10] tooling | Second cold-start test: three payload defects found

A second fresh agent, given only `ASTEROID_EXPLORE` and the repo, reached
`tools/EVENT-CARD.md` on its second tool call, followed it without a wrong turn, put the card
in `cards/` per the newly documented location, ran the determinism check unprompted, and then
verified every row against the XML itself. It found three real defects — none of them in the
card, all upstream:

- **`autoReward` tiers rendered as the wrong resource.** `card-vocab.json` `tiers` covered 7
  of the 11 tiers the data uses, and the renderer fell back to the `standard` template, so
  `MED missiles` read **"medium scrap"** and `MED droneparts` read the same. ~22 sites
  game-wide. Fixed twice over: the missing tiers (`augment`, `missiles`, `droneparts`,
  `scrap`) are now mapped, **and** an unmapped tier now renders its raw name instead of
  silently claiming scrap. A fallback that is plausible-but-wrong is worse than a visible
  gap — [[event-large-asteroid-field]] was stating the wrong reward with no way to notice.
- **`<damage effect="fire"/>` was dropped.** The extractor read `amount` and `system` only,
  so a fire went unmentioned. 7 `fire`, 4 `breach`, 8 `random`, 2 `all` game-wide. Now a
  separate `hazard` effect record.
- **`<environment type="asteroid"/>` was dead data.** Extracted into `flags`, listed in the
  schema, consumed by nothing — so a card never said a fight happens inside an asteroid
  field. Now also an `environment` effect; the six types (`asteroid`, `nebula`, `sun`,
  `storm`, `pulsar`, `PDS`) are in the vocabulary.

Also confirmed: `damage system="room"` (15 uses) is not a system name; it now resolves to
"a random" through a new `systems` vocabulary map. All 9 trees re-extracted and 9 cards
rebuilt.

## [2026-08-10] tooling | Why cards/ is a sibling of wiki/, not inside it

Recorded explicitly after the question came up. A built card inlines the entire event tree
and the vocabulary as text, so a card stored under `wiki/` would put thousands of lines of
generated HTML into the path of every grep, index scan and query of the wiki layer. `cards/`
is therefore a repo-root sibling, and `build-card.py` writes to `ROOT/cards/`.

This was briefly wrong: the original default wrote `card-<slug>.html` beside the tree, i.e.
into `wiki/events/`, and the first cold-start agent followed that default. The stray file was
removed when the default moved. Verified now: no `.html` exists anywhere under `wiki/`.

## [2026-08-10] tooling | Trees moved to cards/trees/ — wiki/ holds no generated files

The `.tree.json` sidecars sat in `wiki/events/` beside the pages they described. They are
machine output — a few hundred lines of JSON each, repeating every string from the page —
so a grep or index scan of the wiki layer hit both. Moved to `cards/trees/<slug>.tree.json`,
alongside the cards built from them.

- `extract-event.py`'s default output is now `ROOT/cards/trees/`; the id remains the only
  argument.
- Repointed every reference: `tools/EVENT-CARD.md` (quick start, components table, pipeline
  diagram, §9), `CLAUDE.md` (§1 layout, §5.2b diagram), `README.md`, `wiki/index.md`,
  `wiki/overview.md`, and the docstrings in `build-card.py` / `event-card-render.html`.
- `wiki/index.md` now states the rule positively: nothing generated lives in `wiki/`.
- All 9 trees re-extracted and 9 cards rebuilt from the new location; determinism re-verified.

**Layout now:** `wiki/` is markdown only. `cards/` holds `card-<slug>.html`, `cards/trees/`
holds `<slug>.tree.json`. Zero generated files under `wiki/`.

## [2026-08-10] tooling | Third cold-start test: an inverted fleet-advance reading

A third fresh agent, given only `NEBULA_REBEL_CHASE`, reached the spec in two hops, took no
wrong turns, hit both of the spec's explicit warnings (the slug is
`rebel-fight-chance-in-nebula`, and `PYTHONIOENCODING=utf-8` is needed), verified every node
against the XML, and found two real defects plus two gaps:

- **`modifyPursuit` sign was ignored — the card said the opposite of the truth.**
  `card-vocab.json` had one flat `fleet_delay` entry reading "rebel fleet delayed" in green.
  The third chase outcome is `<modifyPursuit amount="1"/>` whose own game text says *"the
  fleet has had time to advance closer to your position"* — bad for the player. The card
  rendered it as a gain. [[concept-rebel-fleet-advance]] had already settled the convention
  (positive = against the player, 20 uses; negative = for the player, 12) — the pipeline
  simply never consulted it. Now two vocabulary entries chosen by sign, with the jump count:
  "rebel fleet advances 1 jump" in red, "rebel fleet delayed" in green.
- **First-child `<!--DLC-->` markers were missed.** `dlc_marked()` checked only the following
  sibling. 24 markers are written that way, but **11 are the element's first child** —
  including this event's Lifeform Scanner blue option, which lost its "(AE)". Fixed, and
  gated rows now render the marker on the label.
- **The beacon's `environment` never surfaced.** It is why sensors fail here and why the blue
  options exist. Now a footnote clause: *"Fights at this beacon happen in a nebula."*
- **The ship was never named.** `leads.combat` is displaced whenever a row has its own
  effects, which is every route into this fight. The fight heading now names it
  (R16): *The fight — Rebel Rigger or Rebel Fighter*.

All 10 trees re-extracted, 10 cards rebuilt. Spec gains R16 and a stated rule: **where a
value's sign or type changes the meaning, the vocabulary needs one entry per sense** — the
second plausible-but-wrong fallback found in two tests.

## [2026-08-10] tooling | Nine defects from the five-card batch, fixed

All nine findings from the batch cold-start run, in severity order:

- **Root `effects[]` were never rendered — content loss.** The renderer put the root record's
  text in the hail and then rendered only its `node`, so [[event-boarders-humans-jammed-sensors]]
  never mentioned that 3–5 humans are aboard, the event's whole premise. Now an **arrival
  line** under the header (R16), deduped against the footnote so a root `environment` is not
  stated twice.
- **`smoke-card.js` did not print the header.** That blind spot is why the above passed the
  required pre-publish check. It now prints title, eyebrow, hail, arrival, footnote, tree and
  chain — the rule being that anything a card can show must appear in the dump.
- **`resource` was sign-blind**, so a free `1 fuel` on [[event-ancient-device]] rendered amber
  as a cost. Split into `resource` / `resource_spend` — the third instance of the rule the
  spec already states.
- **`status` was jargon.** `{status} {system}` printed "divide shields". Now literal
  templates: "shields divided by 2", "sensors limited to 0".
- **`boarders` dropped its count** — "random boarders" for `min=2 max=2`. Now "2 random
  boarders", "3–5 human boarders".
- **`text_misc.xml` was not an extractor input**, leaving one choice on
  [[event-auto-ship-carrying-shield-virus]] with an empty label where `<text id="continue"/>`
  resolved to nothing. Added as a fallback string source; the row now reads "1. Continue…".
- **`remove_augment` showed a raw id** (`STASIS_POD`) while the gate on the same row resolved
  the same blueprint to "Damaged Stasis Pod". Now resolved through the same table.
- **`<drone name="RANDOM"/>` printed "RANDOM"** — a sentinel, not a blueprint. Now "a random
  drone" via `random_items`.
- **Ships from broad blueprint lists were unnamed** — `SHIPS_PIRATE` has >3 classes, so the
  card showed the lowercased raw id. New `ship_lists` map gives the family name.

All 15 trees re-extracted and 15 cards rebuilt. Spec gains R16, R17 and the smoke-coverage
rule.

## [2026-08-10] tooling | Ten-card batch: two wrong, six missing — all fixed

The ten-card cold-start run found eight defects plus four cosmetic. All fixed; 25 trees
re-extracted and 25 cards rebuilt.

**Stated something false:**
- **A Clone Bay revive that does not exist.** `crew_loss` set `clone` from the *presence* of
  a `<clone>` child, but `<clone>false</clone>` exists (11 uses) and means the opposite.
  [[event-unknown-disease-on-mining-colony]]'s own prose says *"it would be against
  Federation regulation to create a clone"* while the card promised a revive. Now reads the
  element's value. The spec documented the presence rule, so spec and code agreed with each
  other and both disagreed with the game — corrected in both.
- **A developer placeholder presented as an outcome.** `GHOST_SHIP`'s `deadCrew` text is
  literally *"Should not be seen"*, on a hull with 7 crew, so the crewCount rule could not
  catch it. Now suppressed via a small placeholder-text list, documented in §4.4.

**Dropped real content:**
- **`<event load="X"/>` as an eventList entry was never followed** — only choices were.
  Half of `GHOST_SHIP`'s salvage branch and one of five quest outcomes on
  [[event-civilian-asteroids-beacon-2]] rendered as a blank "nothing happens" row.
- **A bare `<event>` child was not a continuation.** Now a `sequence` node ("Then").
- **A reward on the `<choice>` itself** — rather than on its inner `<event>` — was dropped.
- **`<textList>` entries that are refs** yielded an empty hail on two cards.
- **`text_misc.xml`** now also resolves `<text id=…/>`.
- **DLC markers**: `effects_of` now checks first-child placement, and a choice's own
  following-sibling marker is checked (previously correct only by luck).

**Cosmetic:** `system="room"` is now "a random room" rather than "a random system";
negative resource ranges read "−4 to −2 fuel" instead of the collided "−4–2"; `fuel`,
`missiles` and `droneparts` tiers carry their level; four `blueprintList` gates gained labels
("Missile weapon", "Ion weapon", "Defense drone", …).

## [2026-08-10] tooling | Fourth cold-start batch: a crew loss shown as a gain

Ten more cards, built by a fresh agent that hit no permission prompts — a project
`.claude/settings.json` now pre-allows the pipeline commands and `Artifact`. Wall clock fell
from 33 min to 10 min 50 s for the same batch size, at similar token cost, which suggests
the earlier run was largely stalled on prompts.

Findings, fixed:

- **WRONG — a crew loss rendered as a gain.** `<crewMember amount="-1" class="traitor"/>`
  (`STATION_SICK`) became `crew_gain` unconditionally, so the card read **"+-1 traitor crew"
  in green** on two routes, making the Teleporter blue option look like a pure win when it
  costs a crewman. Now signed: negative amounts render as `crew_lost`, "−1 traitor crew", in
  the fight tone. This is the **fourth** sign-blind fallback after `tiers`, `fleet_delay` and
  `resource`; the spec now calls it out as the first thing to check when adding an effect.
- **MISSING — a store was silently dropped.** `ZOLTAN_TRADE_HUB`'s success entry carries
  `<store/>`; the extractor recorded `flags.store` and nothing consumed it, so the row that
  costs 10 scrap or a Teleporter read "→ nothing happens". Now an effect: "a store opens".
- **MISSING — crew skill points.** `<crewMember repair="1"/>` now renders
  "+1 crew with a point in repair".
- **MISSING — item tiers dropped their level**, so `LOW weapon` and `MED weapon` on
  [[event-zoltan-quest-primitives]] read identically. Now "a weapon (low)" / "(medium)".
- **COSMETIC — internal species ids leaked**: "2–4 energy boarders" is now "2–4 Zoltan
  boarders", via a `species` map shared with crew effects.
- **`chance="0"` surrender branches print no chip.** The files comment these as specially
  triggered, so the branch stays, but a "0%" chip contradicts R6's meaning.

Left alone deliberately: rows whose child has narration but no mechanical payload still read
"nothing happens" (e.g. "Ignore him and attack."). The renderer is being literal; changing it
would mean inventing an outcome. Recorded under known limits.

## [2026-08-11] tooling | Publishing is on demand; permissions cannot suppress its prompt

The Artifact consent prompt is not governed by the permission allowlist. Evidence: the user
already runs `"defaultMode": "bypassPermissions"` with `Bash(*)`/`Read`/`Edit`/`Write`
allowed globally, the dialog offers only "Allow once"/"Deny" with no always-allow, and its
payload carries `__artifactPlanConsentAsk`. Publishing mints a hosted URL, so it is gated
separately. The project `.claude/settings.json` added earlier is harmless but does not help
here.

The real cost was volume: batch runs published every card, ~35 publishes for cards nobody
opened. `tools/EVENT-CARD.md` §9 and `CLAUDE.md` §5.2b now say: a card the user asked for
gets published; a bulk or test run builds and verifies only, reports paths and findings, and
publishes on request.

## [2026-08-13] ingest | The last two unprocessed raw files: the Fandom hub page, and the modding research

`raw/` had exactly two files with no `wiki/sources/` page — everything else was already in.
(The four `README.md`s and `_PROVENANCE.md` are drop-in instructions and provenance metadata,
not sources, and stay unprocessed by design.)

**`raw/wiki/random-events.md`** → [[source-fandom-random-events]]. Almost the whole page is
category links — it is the community wiki's table of contents, and it names no event. The
prose around the list is the payload, and three of its four claims were new to this wiki:

- **Quest beacon placement** → [[concept-quest-beacon-placement]], new. Quests are normally
  placed in the current sector; with few jumps left the game pushes them into the next one;
  **in sector 7 that means the quest is cancelled outright**, because sector 8 allows no
  quests. Corroborated from the data: `FINAL` in `sector_data.xml` allocates only `STORE`,
  `BOSS_REPAIR_STATION`, `BOSS_HOSTILE` and `BOSS_NEUTRAL` — no list carrying a `<quest>` tag.
  The practical consequence is a routing rule the wiki did not have: a quest accepted late in
  sector 7 is worth nothing.
- **What Long-Ranged Scanners actually report** → [[item-long-ranged-scanners]], which had
  *"exactly what 'additional info about nearby Beacons' shows"* as a standing open question
  since 2026-08-09. Answer: ship presence / no ship presence per beacon — the `LRSmap` field
  the other 290 Fandom pages carry. Both readings are unreliable and the source says so:
  "no ship presence" does not rule out a hostile ship or a forced fight, and "possible ship
  detected" can be a friendly. Question closed, `medium` reliability, with two narrower ones
  opened in its place — `LRSmap` appears **nowhere in `raw/gamedata/`**, so whether the flag
  is derived by the community or read from the binary is unknown.
- **Some distress events are unreachable by bug**, not by allocation — *"they won't [occur]
  due to coding errors"*, none named. Filed on [[concept-sector-event-allocation]] as a third
  meaning of unreachable, flagged unverifiable from the data since the defect is in code the
  files do not contain.

**`raw/modding/2026-08-12-ftl-modding-research.md`** → [[source-modding-research]] and
[[concept-modding-and-the-append-convention]], new. The `.ftl` format (a renamed `.zip`), the
`.xml.append` convention and its last-one-wins rule, Slipstream's `mod:` namespace, the
four-file chain for wiring an event in, and FTL Hyperspace. Two things it earns beyond
reference value:

- It **corroborates [[concept-event-list-weighting]] from outside the data** — modders are
  told to duplicate an entry because no shipped `<eventList>` carries weights. First
  non-circular support that assumption has had.
- It **bounds this repo's tooling**: `tools/extract-event.py` assumes one flat definition per
  name with DLC load order as the only override. Ingesting a mod would need `.xml.append`
  handling and the `mod:` namespace, under which the effective event tree is *vanilla plus a
  patch script*. Recorded so the limit is written down rather than discovered later.

### Contradiction opened

> ⚠️ **What `unique="true"` scopes to.** [[source-fandom-random-events]] says **once per
> sector** ("Events that can occur only once per current sector"), with ship-unlock events as
> the once-per-run exception. [[concept-event-tree-grammar]] has said **once per run** since
> the first ingest. Not a version difference — the attribute is identical in the vanilla and
> DLC files. Filed as [[concept-event-uniqueness]] with both sides intact; the per-sector
> reading is the better bet, on three grounds, the strongest being that [[concept-stores]]
> reached it independently from the multi-store sectors, and that `<sectorDescription
> unique="true">` already exists as an unambiguous once-per-run flag on 8 of 21 sectors.
> Settling it needs an observed run, which would be the first time `raw/runs/` outranked
> everything else on a question.

### Numbers that did not reproduce

[[concept-event-tree-grammar]] states *"`unique="true"` (206 events)"*. Re-counted by parsing
the XML (so commented-out elements are excluded): **194** `<event unique="true">` across all
of `raw/gamedata/`, 22 `false`, 216 attributes total; 191/22/213 over the narrower file set
that page says it counted. Regex variants give 195, 214, 222 — none of them 206 either. The
derivation is not recorded on the page, so the figure is **flagged, not overwritten**; the
likely story is an attribute count (true + false) from an earlier scan. Worth settling on the
next lint.

### Schema extensions used, not yet in CLAUDE.md

- `source_kind: research` — the modding notes are neither `gamedata`, `wiki`, nor `run`. They
  are a synthesis written into `raw/` by instruction, and filing them as `wiki` would
  overstate their provenance.
- `raw/modding/` — a raw subdirectory not in the §1 layout.

Both are flagged on the source page and in the index rather than silently absorbed. CLAUDE.md
§1 and §2.7 need a one-line amendment each if these are to be permanent.

**New pages (5):** [[source-fandom-random-events]], [[source-modding-research]],
[[concept-quest-beacon-placement]], [[concept-event-uniqueness]],
[[concept-modding-and-the-append-convention]].
**Updated (5):** [[concept-event-tree-grammar]], [[concept-stores]],
[[concept-sector-event-allocation]], [[concept-event-list-weighting]],
[[item-long-ranged-scanners]] — plus `index.md`.
**Deferred:** nothing.

## [2026-08-13] lint | Two wrong percentages, a misattributed source, and the chain gap measured

Second full lint. 836 pages audited mechanically (frontmatter, link graph, `event_name` join,
source→raw resolution) plus targeted checks on the items the 2026-08-13 ingest deferred.

### Stated something false — the two that mattered

- **[[event-crystal-fight]] said 60% and [[event-rock-fight]] said 70% surrender.** Both were
  reading `<surrender chance>` at face value and explicitly *"trusting the game files"* over
  Fandom's 40 and 30. [[concept-surrender-offers]] settled this on 2026-08-09 — `chance` is
  the probability the ship **keeps fighting** — and left a note saying the affected event
  pages should be updated on the next lint. That note was never actioned, so two pages carried
  a wrong number. Both corrected in the body, both flags annotated **RESOLVED**, both Open
  Questions closed. `ROCK_SHIP` (0.7→30) turns out to be one of the two decisive rows in the
  original finding, which makes the page stating 70% the sharper embarrassment.
- **[[source-text-achievements]] claimed the ship-unlock hint strings live in
  `text_achievements.xml`.** They live in **`text_blueprints.xml`** —
  `ship_PLAYER_SHIP_*_unlock` appears in `blueprints.xml`, `dlcBlueprints.xml` and
  `text_blueprints.xml`, and nowhere in the file that page describes. It also claimed five
  chain pages cite it for those strings; none ever did. **The two errors were the same error:
  the page was an orphan, so nothing ever exercised the claim.** Corrected, and the file's
  real value recorded — it is negative evidence, the place an alternative unlock route would
  be stated if one existed. [[chain-rock-cruiser-unlock]] now cites the actual hint string,
  *"Prove yourself to the Rockmen…"*, against the unverifiable Slug-Cruiser-victory route.

### Numbers settled

- **`unique="true"` is 194.** The count flagged on 2026-08-13 as unreproducible (206 on
  [[concept-event-tree-grammar]], 195 in its own contradiction block) is resolved by a
  comment-stripped census of every `.xml`: **242** `unique=` attributes exist and partition
  without remainder — 216 on `<event>` (194 `true` + 22 `false`), 5 on `<textList>`, 21 on
  `<sectorDescription>`. The partition closing exactly is what makes it safe to adopt.
  Corrected on both pages with the derivation recorded. **Arithmetic only — the per-sector
  vs per-run contradiction at [[concept-event-uniqueness]] is untouched and still open.**
- **"460 event ids" resolves as 458 live + 2 that exist only inside XML comments** —
  `FLEET_EASY_AGAIN` and `LANIUS_BOARDERS`. Both already have pages, both already correctly
  tagged `unreachable`/`cut-content` with the comment quoted. The lint's own first scan
  "found" them missing because its comment-stripping swallowed real definitions — the same
  bug the 2026-08-09 audit hit, rediscovered by writing the same naive regex. Re-scanned with
  a left-to-right comment scanner; zero anomalies.

### The chain layer is the real gap, and it is now measured

The 43 `<quest>` tags resolve into **21 connected components**. **7 have a chain page and all
7 are ship unlocks or the Flagship.** ~12 genuine quest lines have none: the Federation base
quest (planted from 5 different beacons), Merchant's Request, the two escort quests, the
Mantis invasion, the Rock bride, the store rescue, Zoltan primitives, the construction yard,
the Slug pirate trap, Abadoth's secret word, the crew-dead capture, the Mantis chase. Their
steps are all paged; only the sequence is missing — which is why 8 already have dangling
`[[chain-...]]` links pointing at them. Derived with a tag-stack scan; a span regex
undercounts badly (25 of 43) because `<quest>` sits inside `<choice>` and the first
`</event>` closes the span early.

### Fixed

- **Link repair, 33 files.** 6 slug mismatches resolved through the `event_name` join
  (`event-escort-nearby-ship`→[[event-escort-civilians]], `event-merchants-request`→
  [[event-merchant-s-request]], `event-small-asteroid-belt-distress-beacon`→
  [[event-asteroid-belt-distress]], `event-friendly-distress-beacon`→
  [[event-friendly-ship-out-of-fuel]], `sector-last-stand`→[[sector-the-last-stand]], and a
  raw Fandom title `Escort nearby ship` written as a wikilink). 4 concepts repointed to pages that already
  existed under another name (`concept-nebula-beacons` and `concept-plasma-storm` →
  [[concept-nebula-mechanics]]; `concept-quest-beacons` and `concept-quest-markers` →
  [[concept-quest-beacon-placement]]). 3 pairs of duplicate spellings merged
  (`asteroid-field`/`asteroid-fields`, `hazards`/`environmental-hazards`,
  `auto-rewards`/`autoreward-tiers`). `ship-` is not a page type per §3, so
  `ship-rock-cruiser` / `ship-stealth-cruiser` became `entity-` to match the three
  player-cruiser links that already used that prefix. **Broken targets: 48 → 35**, and the 35
  are all genuine to-do signals, not errors.
- **`sources:` counts on 115 pages** set to the number of distinct `source-*` pages cited.
  `last_updated` deliberately **not** bumped for these — a bookkeeping correction is not a
  content change, and bumping would have invalidated 115 `index.md` dates to say nothing new.
- **Orphans 3 → 0.** [[event-stalemate-surrender]] linked from [[concept-surrender-offers]]
  (it is the *other* way a fight ends in a stand-down); [[source-events-imagelist]] from
  [[concept-event-tree-grammar]]'s presentation section; [[source-text-achievements]] from
  [[source-achievements]].
- **Two stale flags cleared.** [[event-rock-unlock2]]'s contradiction said its siblings were
  tagged `version: ae` and uncovered by Fandom — both fixed by the 2026-08-09 lint, flag never
  cleared. [[chain-rock-cruiser-unlock]]'s matching open question closed. Struck through, not
  deleted; both were disagreements between our own pages, never between sources.
- **A factual overstatement:** [[event-pirate-ship-distress-trap]] said its benign twin
  `FRIENDLY_BEACON` "shares every distress pool". It shares **8 of 9** —
  `DISTRESS_BEACON_SLUG` carries the trap without it, so Slug space is the one place this
  distress trap has no benign counterpart.
- **`overview.md` was materially stale:** counts (832→836 pages, 10→14 concepts, 323→325
  sources, and a source breakdown that added to 323 rather than 325), and *"9 cards built so
  far"* against a real inventory of 385. Rewritten, with the chain gap added to Thin Spots and
  the `unique=` scope question added to the Watch List.
- **One missing card built.** [[event-trade-fuel-for-drone-parts]] (`FUEL_FOR_DRONE`) was the
  only ordinary event with no tree; it extracted and rendered clean with no pipeline changes.
  Now **386 trees, 386 cards**. The other 10 uncarded events are 7 engine `FLEET_*` events,
  2 tutorials, and the 2 commented-out ones, which cannot be extracted at all.

### Checked and found correct

- **All 12 "no Fandom page covers this" claims hold up.** The one substring hit
  (`BOARDERS_ASTEROID` inside `ROCK_BOARDERS_ASTEROID`) had already been disambiguated on the
  page itself. The 2026-08-09 lint found 2 false claims of this kind; there are now none.
- **384 of 385 trees resolve their card title through the `event_name` join.** The exception,
  `CIVILIAN_ASTEROIDS_BEACON_2`, is a sub-event folded into
  [[event-asteroid-belt-distress]], so its card carries a machine-made title. Working as
  designed, but the only card in the set whose heading no human wrote.
- No duplicate `event_name` claims, no page claiming a non-existent id, every source page's
  `raw:` path resolves, every raw file still has a source page, and every page is in
  `index.md` with a date matching its frontmatter.

### Not fixed — needs a decision

- **`beacon_type: unknown` on 35 event pages** and `item_kind: unknown` on
  [[item-drone-parts]] are not in CLAUDE.md's allowed values. The pages are right and the
  schema is short: they are tutorials, engine events and surrender aftermaths that occupy no
  beacon. Proposed: add `unknown` to both enums, matching how `version` already works.
- **`source_kind: research` and `raw/modding/`**, introduced by the 2026-08-13 ingest and
  flagged there, still need their one-line amendments to CLAUDE.md §1 and §2.7.
- **~12 chain pages, 5 player-ship entity pages, 14 concept pages** — the dangling-link
  backlog. All are content work, not lint fixes.

## [2026-08-13] ingest | The lint backlog cleared: 14 chains, 5 ships, 15 concepts, and the schema amended

Follow-up to the lint above, at the user's direction. All three deferred items actioned.

### Schema amendments (CLAUDE.md)

- **`beacon_type: unknown`** added to the §2.1 enum, with a definition rather than a bare
  value: it means the event *occupies no beacon* — tutorials, engine-invoked combat
  resolutions, `<ship>`-block aftermaths, cut content — **not** "we didn't look". 35 event
  pages were already using it correctly.
- **`item_kind: unknown`** added to §2.5 for the same reason ([[item-drone-parts]]).
- **`source_kind: research`** added to §2.7, with the rule that it is never `high`: it cites
  sources this repo does not hold, so it inherits their uncertainty.
- **`raw/modding/`** added to the §1 directory layout.

### 14 new chain pages — the quest layer is now closed

Derived from the `<quest>` graph rather than from prose: 43 tags, 21 connected components, and
every component that is a real quest line now has a page. The chain layer goes **7 → 21**.

- [[chain-hidden-federation-base]] — the largest: **four trigger beacons across six sector
  types, five planting sites**, all feeding one 5-outcome table (high drone · free crew ·
  **35 hull repaired** · a Sensors/Scanners-gated consolation · an unasked-for auto-ship fight).
- [[chain-merchant-s-request]] — one beacon that forks into two unrelated quests and never
  rejoins. Carries the only price haggle in the game: 20–30 scrap, 40–55 with Mind Control,
  55–70 plus fuel with Weapons 6.
- [[chain-escort-civilians]] — two triggers, one destination, and a 25% Rebel ambush.
  [[item-ftl-jumper]] skips the whole quest for a `HIGH standard` payout.
- [[chain-capture-the-ship]] — **invisible without a Teleporter, Anti-Bio Beam or Fire Bomb**;
  the ungated choice is answered *"not properly equipped"* and the event ends. Destroying the
  target costs 13 hull, a system, and fires in every room.
- [[chain-rock-bride]] — deliver the bride for a random augment, or refuse and get **Ariadne**
  plus a fight. The only quest whose final choice is purely ethical.
- [[chain-mantis-war-camp]] — paid up front; the Fire Bomb branch is the best-paying blue
  option of any non-unlock quest (`HIGH stuff` + a free Engi crew member for 2 missiles), and
  the missile-weapon branch is a **trap** that is strictly worse than leaving.
- [[chain-settlement-mercenary-work]] — two jobs, both paying more for restraint: a store
  opens on one, and the other pays `MED weapon` only if you spare the pirates.
- [[chain-zoltan-primitives]] — a quest you *overhear* at a cantina; three-way moral choice
  where making first contact gets you shot by the people you were siding with.
- [[chain-construction-yard]] — contains the strangest blue option in the game: the yard
  offers to **buy your Lanius crew member**, and the file carries a line noting the Clone Bay
  does not apply *"since they did not die"*.
- [[chain-slug-pirate-trap]] — the rare event that rewards trusting a Slug: `HIGH scrap_only`
  for keeping the bargain, `MED standard` at best for cutting them out.
- [[chain-secret-word-abadoth]] — **the only puzzle in FTL that tests the player, not the
  ship.** Three near-identical options; the word is ABADOTH, and two of the three start a
  fight. The Engi blue option exists to compensate for the player's memory.
- [[chain-mantis-collectors-chase]] — a grudge match reached *because you lost the first
  fight*; all four resolutions pay.
- [[chain-rebel-defector]] — a 6-entry table where three identical entries make the honest
  outcome exactly 50%, the clearest live demonstration of [[concept-event-list-weighting]].
- [[chain-tutorial]] — filed as what it is: **not a quest**, but a scripted sequence, recorded
  because it is where the game states its own design rules — including the only in-fiction
  definition of a blue option, which claims they are *"nearly always a good choice"*. The
  Mantis war camp disproves that in the same session.

### 5 new entity pages — the unlockable player ships

`entity_kind: ship`, built from `<shipBlueprint>` (hull, reactor, crew, `start="true"`
systems, weapons, augments) plus the `ship_PLAYER_SHIP_*_unlock` hint strings:
[[entity-rock-cruiser]] (*Bulwark*), [[entity-stealth-cruiser]] (*The Nesasio* — the only
layout that **starts with no shields**), [[entity-mantis-cruiser]] (*The Gila Monster* —
Weapons 1, reactor 7, no Sensors), [[entity-zoltan-cruiser]] (*The Adjudicator* — **reactor 5**,
the lowest in the game), [[entity-federation-cruiser]] (*The Osprey* — the only Artillery Beam,
and one crew member of each of four species).

This also resolved a naming inconsistency the lint flagged: the same five ships were being
linked as both `ship-*` and `entity-*`. `ship-` is not a page type per §3, so all are now
`entity-`, and [[entity-federation]]'s standing naming note is satisfied.

### 15 new concept pages

Each built from a fresh census of the game files rather than from the event pages:

[[concept-autoreward-tiers]] (551 uses, a level × tier matrix, and **the numbers are simply
not in the files** — the wiki's largest single unknown) · [[concept-hazards]] (the parent page:
exactly six `<environment>` types, 91 uses, with the engine's own tooltips quoted) ·
[[concept-asteroid-fields]] · [[concept-solar-flares]] · [[concept-anti-ship-battery]] ·
[[concept-scrap-economy]] · [[concept-crew-loss-risk]] · [[concept-fuel]] ·
[[concept-cut-content]] · [[concept-empty-beacons]] · [[concept-start-beacons]] ·
[[concept-map-reveal]] · [[concept-ship-unlocks]] · [[concept-augmentations]] ·
[[concept-ae-vs-vanilla]].

**Findings that came out of writing them:**

- **Two new shipped-data bugs.** `autoReward level="low"` in lowercase (7 uses) alongside the
  documented `MEDIUM` (6); and one `<item type="missile">` singular where the schema uses
  `missiles`. Both recorded, neither corrected.
- **The game is precise about what it takes and vague about what it gives.** Of 116 explicit
  `<item type="scrap">` records, **84 are losses and 32 gains** — while 551 `autoReward`
  rewards carry no number at all. Fuel is the exact inverse: 59 gains to 14 losses.
- **Ship id 3 is never used.** `<unlockShip>` covers ids 1, 2, 4, 5, 6, 7, 8 — and id 4 is not
  identified anywhere in this raw set. Filed as an open question on [[concept-ship-unlocks]].
- **The sun tooltip is the only stated hazard/system interaction in the entire game data**:
  *"Shields will reduce the effect."* No other hazard's description mentions any mitigation.
- **`PDS` is the only hazard with no in-fight tooltip** — it is announced on the map instead,
  which fits the one hazard you can route around. It is also the only one that can be
  one-sided (`target="player"`, 8 of 16 uses).
- **A third of all named augment awards are `RANDOM`** (10 of 30), which is why so many pages
  cannot say what you get.
- **Rarity-0 augments cannot be bought at all**, so [[item-rock-plating]] and
  [[item-mantis-pheromones]] are obtainable *only* from their chains.

### Bookkeeping

- **Backlinks:** 19 step-event pages gained a `chain:` frontmatter value and a Related bullet
  pointing at their new chain, so every chain↔event link is bidirectional. A bracket-count bug
  in the script wrote `chain: [[[[x]]]]` on 14 pages; caught and repaired to the `[[[x]]]`
  list-containing-a-wikilink form the schema uses.
- **`index.md`:** Chains, Entities and Concepts sections regenerated from frontmatter.
- **`overview.md`:** counts corrected (870 pages, 21 chains, 29 concepts, 16 entities), the
  chain gap removed from Thin Spots, and two new "what this wiki answers well" entries added.
- **[[event-encrypted-federation-signal]]** had a dangling `[[event-hidden-federation-base]]`
  reading *"the first quest destination, if it is split out"*. It now points at the chain page,
  with the reason it is a chain and not an event: `HIDDEN_FEDERATION_BASE_LIST` is an
  `eventList`, not an `<event name>`, and four beacons feed it.

### State after this pass

**870 pages. Zero orphans, zero pages missing from `index.md`, zero frontmatter errors, zero
`sources:` count mismatches, and every wikilink resolves** except the literal placeholders in
schema prose and two historical slugs quoted in this log. The remaining gaps are quantities the
game files do not contain, not pages.

---

## [2026-08-13] tooling | Event-labels mod — every carded event names itself in game

Built `mods/event-labels`, a Slipstream mod that prints each event's card title above its
in-game text. New: `tools/build-mod.py` (generator + verifier) and `tools/EVENT-LABELS.md`
(the normative spec). Output is a new top-level `mods/` directory — a sibling of `wiki/`, on
the same reasoning as `cards/`: generated machine output stays out of the wiki's search space.

### What it does

The label is the `title` field of `cards/trees/<slug>.tree.json`, which the card pipeline
derives from the wiki page's H1. **The wiki is the label source** — retitle a page, rebuild
its card, rebuild the mod, and the in-game text follows. 386 of 449 top-level event
definitions are labelled; the 63 without are developer tests and mid-event continuations that
have no wiki page and therefore no name to print. Nothing is invented.

### The two mechanisms, and why not a third

Both use only the plain append convention from
[[concept-modding-and-the-append-convention]] — *reuse an identical tag name, last one counts*:

- **351 events via string override.** Where the event's text resolves to a string only that
  event can reach, the mod replaces the string in `text_events.xml.append` and never mentions
  the event. Measured, not assumed: all 261 `<text id="event_X_text"/>` ids are referenced
  exactly once game-wide, and 90 of the 118 list-backed events have private variants too.
  Structure is untouched, so this path cannot break an event.
- **35 events via redefinition.** Shared strings, shared textLists, and the 7 events with
  prose inlined in the definition. The event's verbatim source bytes are copied and re-emitted
  with only its own `<text>` rewritten; a shared list becomes a new `EVLBL_<ID>` list so the
  vanilla one is left alone and its other users keep their own labels.

Slipstream's **Advanced XML (`mod:findName`) was deliberately not used**, though it is the
tidier instrument. `raw/modding/2026-08-12-ftl-modding-research.md` §5 summarizes the tag set
but not its nesting rules, and there is no Slipstream install here to test against — so using
it would have meant guessing at syntax. Recorded in the spec as the first thing to revisit if
anyone verifies that syntax against `readme_modders.txt`.

### Two data facts worth keeping

- **`<event name="X"/>` inside an `<eventList>` is a reference, not a definition.** A regex
  that ignores depth counts `NOTHING` and `STORE` as defined five times and inflates the event
  count from 449 to 479. The generator and verifier both select on depth.
- **An event's own `<text>` is its depth-1 child**; the `<text>` elements under its `<choice>`
  children are option labels. Relabelling by document order would have printed event names on
  buttons.

### Verification

Every build checks: each append parses, none carries an `<FTL>` wrapper, each targets a real
vanilla file, all 386 labels are present, no byte above 0x7E survives (FTL's fonts have no
typographic punctuation — 13 titles carried em dashes), no string carries two labels, and
every emitted name is either a vanilla name or `EVLBL_`-prefixed. The load-bearing one:
**each redefined event is proven byte-identical to vanilla outside its `<text>`** — negative-
tested by deleting a `<choice>` from a generated append and confirming the verifier fails.

### Open

**Not yet run in game.** The semantics are documented convention and the output is verified
structurally, but nothing has been through Slipstream. One patch and one beacon settles it.

---

## [2026-08-13] tooling | Slipstream installed; event-labels loads and validates clean

Installed Slipstream Mod Manager 1.9.1 to `C:\Users\jparr\Documents\Slipstream`, pointed it at
the local FTL install, and got [[concept-modding-and-the-append-convention]]'s central claim
confirmed from the primary source. The mod is loaded and validated but **not yet patched in** —
that is the user's call.

### Verified against the real install

FTL lives at `D:\Steam\steamapps\common\FTL Faster Than Light` — FTL 1.6.x, a single `ftl.dat`
in `PKG\n` format. Extracted it with `tools/ftlpkg.py` and hashed: **all 14 vanilla files the
mod appends to are byte-identical to `raw/gamedata/`**. The 35 byte-copied event definitions
therefore match the installed vanilla exactly, and all 701 string overrides target names that
exist in the installed `text_events.xml`.

> ⚠️ **CONTRADICTION:** [[concept-modding-and-the-append-convention]] says *"`ftl.dat` in older
> builds, `data.dat` + `resource.dat` in 1.6.x"*. The installed 1.6.x game has a **single
> `ftl.dat`** in `PKG\n` format, which is what `tools/ftlpkg.py`'s docstring describes
> ("FTL 1.6.x `PKG\n` archives (ftl.dat)"). The concept page has the two eras backwards.
> Trusting the install + the extractor over the summary. Not yet corrected on the page.

### `readme_modders.txt` — now a primary source

The Slipstream download ships Vhati's `readme_modders.txt`, which
`raw/modding/2026-08-12-ftl-modding-research.md` had only summarized secondhand. It states the
rule this mod is built on verbatim: *"Whenever multiple tags share the same name, only the last
one counts."* It also confirms LF line endings are fine (Slipstream converts to CR-LF while
patching) and that `mod-appendix/metadata.xml` is optional.

It further documents the **full Advanced XML tag set and its nesting** — the thing the spec
said was unverifiable — and notes Slipstream ships an **XML Sandbox** under its File menu for
testing such patches interactively. `tools/EVENT-LABELS.md` now records Advanced XML as the
upgrade path rather than an unknown: one `mod:findLike` per event would replace all 35 event
redefinitions and conflict with almost nothing.

### One real bug, caught by patching-adjacent reality

Slipstream refused the first build outright:

```
ERROR JDOMModMetadataReader - While processing "event-labels.ftl:mod-appendix/metadata.xml",
strict parsing failed: Missing threadUrl.
```

`metadata.xml` is parsed **strictly**; an empty `<threadUrl/>` — which a locally built mod has
no honest value for — makes the mod silently absent from the list. Fixed by emitting all five
elements with CDATA values (matching the example mods Slipstream ships), and
`build-mod.py` now verifies the metadata on every build so it cannot recur. Nothing about the
event data was wrong; the mod was rejected before its appends were ever read.

### State

Slipstream lists **event-labels**, and its own **Validate** returns `No Problems`. What remains
untested is only whether the labels render — one Patch and one beacon.

---

## [2026-08-13] ingest | Slipstream `readme_modders.txt` — the primary source behind the modding concept

Filed `raw/modding/slipstream-1.9.1-readme_modders.txt`, Vhati's own reference documentation,
copied out of the Slipstream 1.9.1 distribution. [[source-modding-research]] had been
summarizing this file secondhand from a GitHub copy; the wiki now holds the document itself.

### New
- [[source-slipstream-readme-modders]] — `source_kind: wiki`, `reliability: high`.

### Updated
- [[concept-modding-and-the-append-convention]] — primary citation, two contradictions, and
  four sections the summary had flattened. `sources: 3 → 4`.
- [[source-modding-research]] — a "Superseded by the primary source" section saying exactly
  what the synthesis got right, what it lost, and what it is still the only source for
  (Hyperspace, Superluminal2, the distribution landscape).
- `index.md` — new **Vendor documentation** subsection under Sources; count 325 → 326.

### What the primary source settles

- **Last-wins is stated twice, about different actors**, and the wiki had recorded only one.
  *"Whenever multiple tags share the same name, only the last one counts"* describes
  **Slipstream** resolving duplicates while patching. But the Raw XML section — describing
  `.rawappend`, where Slipstream deliberately does no parsing — says *"you can still override
  existing tags by adding your own with the same 'name' attribute, since **FTL honors the last
  it sees**."* The resolution is the **engine's**. That is why a text-only mod works without
  redefining anything, and it is the load-bearing fact under [[concept-event-tree-grammar]]'s
  load-order reading too.
- **`<mod:findName>` searches backwards** — defaults `reverse="true" limit="1"`, so it matches
  the *last* tag of that name. Correct, given last-wins, and the opposite of what "find" implies.
- **`panic` defaults to false**, so an Advanced XML find that matches nothing is a silent no-op.
  `--global-panic` is the only way to surface a typo.
- **`--patch` and `--validate` accept directories**, so `mods/event-labels/src/` can be tested
  without zipping.
- **Encoding vs. glyphs are separate problems.** FTL 1.01–1.5.13 assumes windows-1252; 1.6.1+
  assumes UTF-8. On 1.6.x non-ASCII is read fine, and the only remaining risk is *"whether the
  fonts contain the glyphs"*. `tools/build-mod.py`'s ASCII fold is still the safe choice, but
  the reason recorded in its spec was half right.
- **FTL crashes on event loops** — a choice loading an event whose choice loads the first kills
  the game at the main menu. Recorded as a pitfall for any tool that generates event chains.

### Contradictions recorded (both kept, neither overwritten)

> ⚠️ **1.6.x archive layout.** [[source-modding-research]] says 1.6.x uses `data.dat` +
> `resource.dat` and `ftl.dat` is the older form. The local 1.6.x install has a single
> `ftl.dat` with `PKG\n` magic, matching `tools/ftlpkg.py`. The eras are reversed in the
> synthesis. Trusting install + extractor.

> ⚠️ **`metadata.xml` "optional".** The readme calls it optional; Slipstream 1.9.1 parses it
> strictly once present, and an empty `<threadUrl/>` removed the mod from the list entirely.
> Optional file, mandatory contents.

### Note on schema

`reliability: high` on a `source_kind: wiki` page departs from the §2.7 convention
(*high = game files*). First-party vendor documentation has no value in that scale; flagged on
the page rather than filed quietly, as [[source-modding-research]] did for `research`.

---

## [2026-08-13] tooling | Fullscreen stops minimizing on focus loss — an engine switch, not a data mod

The user runs two 4K monitors; FTL's fullscreen window minimized every time they clicked the
other screen, at any resolution. Asked to fix it "with a mod".

### What it isn't

Not a Slipstream `.ftl` mod. Window behaviour is engine code, not anything reachable from
`ftl.dat` — no XML append can touch it. Filed under `mods/` anyway, as
`mods/fullscreen-no-minimize/`, with the README leading on that distinction.

### What the binary gave up

`FTLGame.exe` 1.6.14 (Steam) has no SDL strings except one: `SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS`.
Alongside it, `SILWindowClass`, `SILCPFWindowClass`, `SIL_WINDOWS_USE_RAWINPUT`,
`SIL_WINDOWS_USE_XINPUT`, and a display-attribute table (`center_window`, `depth_bits`,
`fullscreen_minimize_on_focus_loss`, `window_resizable`, `window_thread`, …). That identifies the
engine layer as **SIL**, Andrew Church's System Interface Library — he did the 1.6 ports.

### What the SIL source settles

- The minimize is **deliberate engine behaviour**, not Windows reclaiming an exclusive display
  mode: `graphics.c:2656` minimizes from the `WM_ACTIVATE` handler. So no choice of resolution
  avoids it — which matches the user's "any resolution".
- `should_minimize_fullscreen()` (`graphics.c:3069`) consults `minimize_fullscreen` (default
  `-1`, unspecified), then falls back to reading `SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS` from the
  process environment, then defaults to minimize. SIL borrows SDL's variable name even though
  the Windows backend is WGL/D3D11, not SDL.
- `windows_getenv()` is a `GetEnvironmentVariable()` wrapper (`util.c:165`) — an ordinary
  environment variable is the whole mechanism.
- Fullscreen is `WS_POPUP | WS_VISIBLE` at `HWND_TOPMOST` (`graphics.c:1221`), so suppressing
  the minimize yields borderless-fullscreen behaviour without running the game windowed.
- Bonus: `ChangeDisplaySettingsEx` is skipped entirely when the requested size equals the
  monitor's current mode (`graphics.c:1111`). At native 3840×2160 there is no real mode switch.

### Shipped

`mods/fullscreen-no-minimize/` — `README.md` (mechanism + citations), `install.ps1`
(idempotent, `-Uninstall`), `launch-ftl.cmd` (per-process alternative). Installer run; variable
is set at user scope. Steam restart pending — Steam hands its own environment to its children.

### Unverified

Whether FTL ever calls `graphics_set_display_attr("fullscreen_minimize_on_focus_loss", …)`
itself, which would pin `minimize_fullscreen >= 0` and make the environment variable inert.
Nothing in the binary settles it; the in-game smoke test is the proof.

## [2026-08-13] tooling | Save watcher — cards open themselves from continue.sav

Asked how a mod could open HTML in game. It cannot: FTL has no HTML renderer, and
Hyperspace's Lua sandbox has `io`, `os`, `package` and `debug` commented out of its
`linit.c`, so no in-game script can launch a browser or write a file. Any card display is
an external process; the only question is how it learns the current event. Chose the save
file, which needs no game modification at all.

### Shipped

- `tools/ftlsave.py` — read-only parser for `continue.sav`, stopping at `EncounterState`.
  Port of Vhati/ftl-profile-editor `SavedGameParser.readSavedGame` plus
  `DatParser.readLayout`. Ship layouts read live from `ftl.dat` via `tools/ftlpkg.py`;
  blueprints from `raw/gamedata/`.
- `tools/save-watch.py` — watches the save, resolves the encounter to a card, serves one
  auto-updating page on localhost.
- `tools/SAVE-WATCH.md` — the specification.

### Two findings that made it work

**Stopping at the encounter is what makes 1.6.14 parseable.** The reference parser cannot
read 1.6.14 saves at all (`Unsupported projectileType flag: 6`, ftl-profile-editor #119).
Every byte it fails on sits after the encounter block, so the early stop sidesteps it.

**The save is written mid-encounter, not just on jump.** Observed directly: `continue.sav`
rewritten at 19:20:31 with no jump, 6909 → 6212 bytes, encounter text changing from
`event_ROGUE_REBEL_SEARCH_2_text` to `event_DEAD_CREW_DEFAULT_1_text` as a fight resolved.
This was the open question when the approach was chosen; it is now settled by observation.

### Resolution

`EncounterState.text` holds a string-table id. Indexing `raw/gamedata` for it does not
work — the text on screen is usually an *outcome* sub-event, not the named top-level event
(`event_ROGUE_REBEL_SEARCH_2_text` lives in an anonymous `<event>` inside
`<eventList ROGUE_REBEL_SEARCH>`, which the card `rebel-fight-chance` covers but never
names). The index is built from `cards/trees/*.tree.json` instead, whose `text.ref` /
`text.value` pairs already cover every expanded node.

Measured over the 386 cards: 3448 text keys, and 739 of 749 root texts pin exactly one
card. Shared outcome prose is resolved by staying on the card already displayed; when
there is nothing to continue from, the watcher shows no card rather than guessing.

### Verified

Parser: format 11, `PLAYER_SHIP_ANAEROBIC_2`, 4082 of 6212 bytes consumed, landing on an
`EncounterState` whose five ship-event ids were all real event names. Server: `/`,
`/current` and `/card/<slug>` all 200, card served at 107,864 bytes; unknown slug 404s.
Resolution chain exercised across root → continued → ambiguous.

### Not verified

The page has not been watched during live play — the transitions above were reconstructed
from two reads of a save the game rewrote between them, not from a browser open on the
second monitor while jumping beacons.

## [2026-08-13] tooling | Save watcher — operating docs

Documented the watcher so a future agent can launch it without rediscovering anything.

- `tools/SAVE-WATCH.md` §1 rewritten from "quick start" into **Running it**: the agent
  caveat (it is a server that never returns — background it, and check with `--once`
  first), the verified save/`ftl.dat` paths, and how to stop it.
- `tools/SAVE-WATCH.md` §5 gained a **States** table (`ok` / `ambiguous` / `nocard` /
  `noevent` / `nosave` / `waiting` / `error`, and which are faults — only a persistent
  `error`) plus four concrete failure modes.
- `CLAUDE.md` — new §5.2c pointing at the spec, and the `tools/` layout line now names it.
- `README.md` — user-facing "Let the cards open themselves", and `mods/` added to the
  directory map, which it had been missing.

### Corrected

The first draft said to stop the watcher with `pkill -f save-watch.py`. Both halves are
wrong on this machine: `pkill` is not in this Git Bash, and matching `python.exe` misses
the process because the interpreter is the Windows Store `python3.10.exe`. Found by
following the doc as written and watching it fail. Replaced with a kill-by-port
`Get-NetTCPConnection` one-liner, which is name- and shell-agnostic, and verified.

### Verified

Followed the documented path end to end: `--once` → JSON with `status`; background launch
→ `/current` and `/` both 200; documented stop command → port released.

## [2026-08-13] tooling | Save watcher — starts without a run in progress

Went to start the watcher and it exited 2: `could not find continue.sav`. The run logged
earlier had ended (profile written 21:05, `continue.sav` deleted — FTL removes it when a
run finishes), and `main()` refused to start without it.

That contradicted the design: `Watcher.poll_once` already had a `nosave` state for exactly
this case. The guard in `main()` made the watcher unstartable precisely when it is most
useful — before launching the game.

**Fixed:** `find_save()` now falls back to the canonical save location instead of `None`,
so it resolves *where the save will appear* rather than requiring it to exist, and the
`ap.error` guard is gone. `--once` with no run now reports `nosave` rather than exiting 2.

`tools/SAVE-WATCH.md` §1 gained the rule this implies: start it whenever, including before
FTL; a missing save is never a reason not to start.

### Verified

`--once` with no run → `{"status": "nosave"}`. Watcher launched, `/current` 200 with
`nosave`, `/` 200. Serving on http://127.0.0.1:8787.

## [2026-08-14] tooling | Save watcher — the last card stays up

Changed at the user's request: when the save names no card — shared outcome prose, an
uncarded event, a torn read, a finished run — the watcher now leaves the previous card on
screen instead of replacing it with a message. The messages are only ever seen before the
first card of a session.

### What it took

The naive version (keep showing the last slug) would have broken resolution, because the
resolver's stickiness rule reads "the card currently on screen" to decide whether a shared
outcome text continues the current event. Held cards had to be kept out of that.

So the watcher now tracks two things that were previously one:

- `_displayed` — what is on screen. Survives everything; only a *different* card replaces it.
- `_anchor` — the event we are actually in, which drives stickiness. **Cleared when a run
  ends**, so a card still up from a finished run cannot capture a shared text in the next.

`/current` gained `held: true` for a stale display; `status` still reports what the save
says, so "what is shown" and "what the save contains" stay separately answerable. The page
now keys its iframe on the slug alone, so a held card never reloads or flickers.

### Verified

Drove a full sequence: arrive → outcome → shared outcome → uncarded event → run ends → new
run. The uncarded event and the run boundary both held `rebel-fight-chance` with
`held=true`; the first shared text of the new run resolved `ambiguous` rather than falsely
continuing the old run — the anchor separation working; and the next real event
(`event_ROCK_CRYSTAL_BEACON_text`) took over cleanly with `held=false`.

Watcher restarted on the new build. It now reports `noevent` rather than `nosave` — a new
run is in progress, with no event text yet.

## [2026-08-14] tooling | Save watcher — textList variants indexed; holding narrowed

User was sitting on the **Pirate briber** event and the watcher could not see it. It was
showing `pirate-engine-hacker` instead — a stale card, presented as if current. Two
separate defects, neither in the parser, which read the save correctly throughout.

### 1. The index missed every textList variant

`PIRATE_BRIBER` reads its prose via `<text load="PIRATE_BRIBER"/>`. A card tree records
such a text as the **list name plus a count** — `{"ref": "PIRATE_BRIBER", "variants": 3}` —
never the individual variants. The save records the variant actually shown,
`text_PIRATE_BRIBER_3`, which appears in no tree. So every list-backed event resolved to
nothing.

Fixed with `load_textlists()`, which expands each `<textList>` from `raw/gamedata` (reusing
`build-mod.py`'s `load_game` / `variants_of`) and indexes every variant id and prose against
the card whose tree loads that list.

Measured before → after:

```
text keys indexed          3448 → 4516
root texts (event start)    749 → 1782
  pinning exactly one card  739 → 1741
```

**1033 of 1782 root texts were missing** — most beacon arrivals could not resolve. The
earlier "739 of 749 root texts pin a single card" figure was measuring only the events
whose text is a plain `<text id=…>`, and read as far better coverage than existed.

### 2. Holding made the failure invisible

Yesterday's change held the last card whenever no card resolved — including `nocard`, where
the event *is* identified and merely has no card. That turned "I don't know this event" into
a confidently wrong display, and is why the gap looked like a working watcher rather than a
bug. `HOLDING_STATUSES` now excludes `nocard`: hold when uncertain, never when known-wrong.

The tradeoff was flagged when holding was added but judged acceptable; it was not. A held
card is indistinguishable from a live one, so holding is only safe where the alternative is
*no information*, not where it contradicts information we have.

### Verified live

Against the running game, mid-event: `text_PIRATE_BRIBER_3` → `pirate-briber` /
"Pirate briber", `reason: root`, `held: false`. First time the watcher has resolved a real
card from a live save.

---

## [2026-08-14] ingest | Oxygen and suffocation — two external sources for numbers the game files don't hold

**Question that started it:** "how much damage does no oxygen do per second?" The wiki couldn't
answer it and neither could `raw/` — so the answer was fetched rather than guessed.

### Why these sources

The suffocation rate is **not in any XML**. Every file in `raw/gamedata/` was checked;
`text_tooltips.xml` gets closest with *"Most crew need oxygen to live."* The constant is
compiled into `FTLGame.exe`, so "check the decompiled files" would have meant binary RE, not a
re-extract of `ftl.dat` — which `tools/ftlpkg.py` had already done exhaustively.

Fandom's Oxygen page was the target. Its See-also then pointed at a reverse-engineering project,
so both were taken: the community page for crew-facing consequences, the RE doc for the engine
model. They corroborate each other on everything they both cover.

**Capture note:** `curl` on `ftl.fandom.com/wiki/Oxygen?action=raw` returns a Cloudflare
challenge page. `api.php?action=query&prop=revisions&rvprop=content` does not — that is the path
to use for any future Fandom capture.

### New raw files

- `raw/wiki/oxygen.md` — Fandom "Oxygen", revision 74853 (edited 2025-12-09), verbatim wikitext
- `raw/modding/2026-08-14-xftl-oxygen-mechanics.txt` — xftl (znixian) reverse-engineered doc.
  No upstream revision id exists: GitLab raw URLs pinned to `master` return none.
- `raw/wiki/_manifest.csv` — **edited**, one row added for the Oxygen page. The only file under
  `raw/` modified rather than created; leaving the capture index stale would have made it wrong.

### New pages

- [[concept-oxygen-and-suffocation]] — the payload. Full rate table, modifier table, the venting
  model, and the caveats.
- [[source-fandom-oxygen]], [[source-xftl-oxygen-mechanics]]

### Updated pages

- [[item-oxygen-system]] — gained a refill-rate table (1.2 / 4.8 / 8.4 %/sec) and the UI-bug note
- [[item-emergency-respirators]] — its `<value>0.5</value>` finally has a base to multiply: 6.4 → 3.2
- [[item-lanius-crew]], [[entity-lanius]] — drain quantified at 8%/sec, engine-identical to a breach
- [[entity-crystal-men]] — *"Reduced suffocation damage"* quantified at 50%
- [[item-medbay]] — gained undocumented suffocation immunity, absent from its in-game tooltip
- [[item-doors]] — gained the venting model (16%/sec per airlock, `0.75^distance` propagation)
- `index.md` — 2 source rows, 1 concept row, 7 date refreshes; Concepts 29 → 30

### Open questions closed

- [[entity-crystal-men]] — "What 'reduced suffocation damage' is as a number" → **50%**
- [[entity-lanius]] — "The rate at which Lanius crew drain oxygen, and whether it scales with
  crew count" → **8%/sec each, and yes it scales**

Both marked resolved in place rather than deleted, per §4.

### Contradictions found

> ⚠️ **Airlock drain speed.** Fandom: an open airlock *"instantly drains"* its room. xftl, from
> `OxygenSystem::ComputeAirLoss`: **16%/sec per airlock door**. Not instant — ~6s for a full
> room. xftl trusted; Fandom's own tactical advice presupposes a finite rate.

> ⚠️ **The game's UI is wrong about its own system.** The upgrade menu shows Oxygen refill
> multipliers of 1/3/6; both sources independently give **1/4/7**. Not source disagreement — a
> display bug in the shipped game. Levels 2 and 3 are better than advertised.

### What this ingest did *not* establish

**The 6.4 HP/sec figure is single-sourced.** xftl documents air — drain, refill, redistribution —
and never touches crew health, so the one number the ingest was run to obtain has no
corroboration. Everything *around* it is doubly sourced; the headline is not. Recorded as the
first open question on [[concept-oxygen-and-suffocation]], resolvable cheaply by a timed run note.

Also deferred: baseline crew HP is not directly sourced anywhere in this repo (inferred at 100
from [[item-rock-crew]]'s *"Max Health is increased to 150"*), so time-to-death is not yet
derivable. The fire-mechanics Pastebin cited by the Fandom page was not retrieved.

---

## [2026-08-14] tooling | Dispatch pools no longer inlined — the exit-beacon card was 30 events deep

**Reported:** the Long-Range Beacon card meant filtering through "17 and 13 different unique
events instead of being presented with the correct one".

### What was actually wrong

Not the watcher. Replaying a captured 40-minute save trace through `Resolver.resolve` showed
every state resolving correctly, including the one in question:

```
event_FINISH_BEACON_text     -> finish-beacon          (root)
event_REBEL_TRANSPORT_text   -> rebel-transport-ship   (root)   <- switches on the next save write
```

That transition also settles a question the watcher's design rested on but had never observed:
**FTL rewrites `continue.sav` when a `<choice hidden="true">` chains into another event.**
`event_FINISH_BEACON_text` / `choices []` became `event_REBEL_TRANSPORT_text` / `choices [0]`
in one write. So the exit beacon's roll is visible to the watcher one poll after the player
clicks Continue.

The defect was the card. `FINISH_BEACON` is a dispatcher — its only choice is
`<event load="EXIT_LIST"/>`, and `EXIT_LIST` is `NEUTRAL_EXIT` (17 events) + `ITEMS` (13). The
extractor inlined all 30 whole events, giving **529 text nodes, 2.7× the next largest card**.

### The rule added — `Extractor.dispatch_pool`

An `eventList` collapses to one pointer row per entry when **every** entry is a bare
`<event load="X"/>` whose target is a top-level event with a `wiki/events/` page. Such a list
does nothing but pick a complete event to run, and the watcher will show that event's own card
a moment later, so the pool card only has to say what *can* follow.

All-or-nothing is the load-bearing part. A first attempt collapsed *any* qualifying entry and
silently gutted the eight refugee cards: `REFUGEE`'s list is four `REFUGEE_TRADER` loads plus
four inline ambushes, and the trade offers are the reason to read that card. A list mixing
`load=` with anonymous `<event>` bodies is an outcome table, not a dispatcher. The structural
test separates them without a judgement call about which lists are "too big". Single-entry
lists are excluded — R10 already collapses those into the row above.

New: `chance.dispatch: true`; option rows carry `label` (the target's title) and a
`{"kind":"ref","target":…,"card":…}` child. `leads.card_ref` ("a separate event") distinguishes
this from the recursion-guard `ref` ("the same table again").

### Effect

| card | text nodes before | after |
|---|---|---|
| `finish-beacon` | 529 | 1 |
| `fuel-fleet-distress` | 196 | 1 |
| `no-fuel-rebel-fleet-delay` | 195 | 1 |

Three of 386 trees changed; every card rebuilt (shared vocabulary and renderer are inlined) and
all 386 smoke-tested clean. Extraction re-verified deterministic.

Resolution quality is unchanged or better: root texts pinning exactly one card stayed at
**1741 of 1782**, while keys appearing in more than one card's tree fell **1250 → 738**. Less
duplicated prose across trees means fewer chances for stickiness to latch onto the wrong card.

### Not addressed

The two `EXIT_LIST` rows render as the unlabelled "Outcome → 1 of 17" / "1 of 13", because
those entries load *lists*, which have no title to borrow. The game names them only internally,
and I3 keeps internal ids off cards.

## [2026-08-14] tooling | Save watcher — live verification, and whitespace normalisation

### The live verification is done

The watcher's own log covers a real run from 15:15 to 15:56, sector 5, beacon 16 — the
end-to-end check that had been outstanding since the watcher was built. It resolved event
after event correctly:

```
15:25:09 event_PIRATE_STATION_CROPS_text          -> remote-settlement (root)
15:25:41 event_PIRATE_STATION_CROPS_c1_text       -> remote-settlement (continued)
15:36:16 ship_PIRATE_STATION_CROPS_destroyed_text -> remote-settlement (continued)
15:36:18 event_PIRATE_STATION_CROPS_RESULT_text   -> remote-settlement (continued)
15:47:53 text_STORE_TEXT_3                        -> store (root)
```

Root detection, stickiness across a multi-step encounter including its combat outcome, and
textList variants (`text_STORE_TEXT_3`, `text_TRAP_BEACON_TEXT_4`) all confirmed against
live play rather than reconstruction.

### One miss, and its cause

`15:46:41  They upload the delivery destination once on b… -> no card (nocard)`

That prose is in two trees, so it should have resolved (and, with the anchor on
`merchant-investigate`, continued). It reported **zero** candidates, meaning the lookup
missed outright — the save's copy of the string did not match the XML's byte for byte.
`SavedGameParser` documents that `EncounterState.text` "may include line breaks", so exact
prose matching was always fragile.

`_norm` now collapses whitespace runs to a single space at both index and lookup. Verified:
the same prose with an inserted newline, a doubled space, or a trailing newline all resolve
where previously only the exact form did.

### A number I reported was wrong

I gave "keys in >1 card's tree: 1250" after the textList fix. It does not reproduce —
the figure is **738** (582 not a root). Confirmed by building the index twice, with and
without normalisation: both give 4516 keys and 738 shared, and **zero** keys change
spelling under `_norm`. The tree values are already clean, so normalisation's entire value
is on the query side. Measuring its effect on the index would suggest it is useless; that
is the wrong side to measure, and the spec now says so.

### Note

The harness reports these background watcher tasks as "failed, exit 127" while the process
is demonstrably alive and serving. The notification is spurious — check the port, not the
task status.

---

## [2026-08-14] ingest | The reactor cost curve — and the power economy around it

**Question that started it:** "how much does the 12th reactor energy cost?" **25 scrap.**

### Why an external source again

Same shape as this morning's oxygen ingest. [[item-reactor]] is **the only system in the game
with no `<systemBlueprint>` entry at all** — it exists in `raw/gamedata/` purely as a target for
`<upgrade system="reactor">` and `req="reactor"`. Its cost, curve and ceiling are absent by
construction. The page had already recorded this as its top open question.

**Two capture wrinkles worth remembering:**
1. `wiki/Reactor` is a `#REDIRECT [[Ship#Reactor]]`, and has been since 2014. No standalone page.
2. The cost table is **transcluded**, not inline — `{{Reactor power cost}}`. Reading `Ship`'s
   wikitext alone yields the prose and an empty marker. The template needed its own capture.

### New raw files

- `raw/wiki/ship.md` — Fandom "Ship", rev 74911 (2026-06-21); the most recently edited source
  in the repo
- `raw/wiki/template-reactor-power-cost.md` — Template:Reactor power cost, rev 68667 (2023-11-01)
- `raw/wiki/_manifest.csv` — two rows added (294 total)

### The answer, and how it was verified

Costs are banded **by the bar being bought**: 30 / 20 / 25 / 30 / 35 per band of five, ceiling
**25 bars**. The 12th bar is in the 11–15 band → **25 scrap**.

The band labels were ambiguous — "11–15" could mean the bar bought or the level held. The Ship
page's independent *"fully upgrade a ship with 8 power, it costs 490"* discriminates:
bar-being-bought sums to **490** ✓, level-held to 475 ✗. Two Fandom pages edited three years
apart agreeing to the scrap.

**The curve is non-monotonic** — bars 6–10 at 20 scrap are the cheapest in the game, below the
opening band's 30. The Ship page's own prose ("upgrades become more expensive") contradicts its
own table; the table wins.

### New pages

- [[concept-power-and-reactor]] — the payload: cost curve, the 37-bar maximum, and the two
  power sources ion storms don't halve
- [[item-backup-battery]] — **a page that should have existed already.** The `battery` system is
  in `dlcBlueprints.xml` (35 scrap, upgrade 50, maxPower 2) and had no page. Confirmed it has
  **no `req="battery"` gate and no `<upgrade system="battery">` anywhere** in the event files.
- [[source-fandom-ship]], [[source-fandom-template-reactor-power-cost]]

### Updated pages

- [[item-reactor]] — Stats section filled in; both open questions closed
- [[entity-zoltan]] — "provides power" quantified: exactly 1 bar, ion-immune, plus the
  movement/slot-ordering gotchas
- [[item-rock-plating]] — the 15% roll **excludes** fires, sabotage, solar flares and events; an
  exclusion list absent from the game-file description
- [[concept-nebula-mechanics]] — what the storm halving does *not* touch
- `index.md` — 2 source rows, 1 concept row, 1 item row, 4 date refreshes; Concepts 30 → 31,
  Items 64 → 65

### Open questions closed

- [[item-reactor]] — "the real upgrade cost curve and maximum" → **30/20/25/30/35, cap 25**
- [[item-reactor]] — "whether `max_lvl=24` is the true ceiling" → **neither; it is an inverse
  gate, and 24 is exactly what a 25-bar cap implies.** The apparent conflict with the game files
  dissolves rather than needing a contradiction block.
- [[entity-zoltan]] — "how much power a Zoltan actually supplies" → **exactly 1 bar**

All marked resolved in place per §4.

### Correction made during this ingest

An earlier draft of the nebula edit claimed Fandom supplied the reactor-halving figure "the
tooltips never do". Wrong — [[concept-nebula-mechanics]] already documented `tooltip_storm`
(*"your main reactor can only function at half capacity"*) from the game files. Rewritten to
credit the game files and confine the new material to what Fandom actually adds: **the enemy is
halved too**, and **Zoltan and Battery power are exempt** (both AE-only, so the counter-play
does not exist in vanilla).

### Contradiction amended

The naming contradiction on [[concept-nebula-mechanics]] ("ion storm" in `map_ion_loc` vs
"plasma storm" in `tooltip_storm`) previously noted that *Fandom uses "plasma storm" throughout*.
[[source-fandom-ship]] disproves it — that page says **"ion storms"** three times and never
"plasma". Both names are live on both sides, split by page type: event pages say plasma,
mechanics pages say ion. Note amended in place rather than replaced.

### Deferred

The Ship page carries more than was ingested: ship-unlock progression (Layout A/B/C rules,
the 4-ship Lanius threshold), hull mechanics (all playable ships start at exactly 30; Hull
Beam/Laser/Missiles double-damage systemless rooms; bombs cannot damage hull), and the enemy-ship
taxonomy. None conflicts with existing pages; all is uningested. A `concept-hull-and-damage` page
is the obvious next step if that becomes a question.

Also noted, unpaged: `BATTERY_BOOSTER` ("Battery Charger", 40 scrap, `<value>0.5</value>`,
*"Backup Battery's lock time is halved"*) — recorded on [[item-backup-battery]], no page of its
own, and no source we hold defines "lock time".

## [2026-08-14] tooling | Sector-profile pipeline — a page for all 19 sectors

New pipeline, mirroring the card pipeline in shape and in doctrine (generated, never
hand-written). Spec: `tools/SECTOR-PAGE.md`, normative and self-contained.

```
raw/gamedata/*.xml + cards/trees/*  →  sectors/data/<slug>.sector.json  →  sectors/sector-<slug>.html
                          extract-sector.py                     build-sector.py + sector-page-render.html
                                                                + tools/sector-copy/<slug>.json
```

**New files:** `tools/extract-sector.py`, `tools/build-sector.py`, `tools/sector-page-render.html`,
`tools/sector-vocab.json`, `tools/smoke-sector.py`, `tools/check-sector-numbers.py`,
`tools/SECTOR-PAGE.md`, `tools/sector-copy/*.json` (19), `sectors/` (19 pages + 19 data files).
`CLAUDE.md` gains the `sectors/` layout entry and §5.2b-2.

**The design rule:** prose may not contain facts. A stat tile names a *metric id* and the build
supplies the number; prose names events as `{{EVENT_ID}}` and the build fails if the sector cannot
produce that event. Per-event tags are derived by walking that event's existing tree — all 19
sectors' pools were already fully covered by `cards/trees/`, so no backfill was needed.

**Two open questions are rendered as open, not resolved:**
- `OVERRIDE_*` lists are shown as a marked delta with `applies: "unconfirmed"`, never merged into a
  pool — per [[concept-sector-event-allocation]], nobody has established that the engine
  substitutes them.
- `unique="true"` renders as a bare "Unique" tag with a standing footnote on the scope question,
  per [[concept-event-uniqueness]].

**Four defects found and fixed during the run**, three of them by the authoring agents:
1. `extract-sector.py` did not walk `chain[]`, so quest-stage gates, items and `unlockShip` ids were
   missing. Fixing it moved metrics on 14 of 19 sectors and surfaced the Rock, Slug and Zoltan ship
   unlocks. Stale counts in already-written copy were re-verified and patched.
2. The `fight` tag ignored `hostile="false"`, so `ZOLTAN_FREE_MAP` — a ship that hands you the map —
   counted as a forced fight in two sectors' rollups.
3. `rarity_html()` emitted an empty "Crew in stores" panel for `FINAL`, which declares no `rarityList`.
4. The ambiguous-entry footnote had a plural agreement bug in `sector-vocab.json`.

`check-sector-numbers.py` exists because of #1: the build can verify a tile but not a sentence, so
it lints "N events …" claims and "Label ×N" gate tallies against the data. It reports candidates,
including legitimate subset claims, rather than failing a build.

### Contradictions found against existing `wiki/sectors/` pages

Reported by the authoring agents, **not yet filed** — each needs a wiki edit:

- [[sector-the-last-stand]] — `BOSS_NEUTRAL` is five events, not four; the page names
  `BOSS_FLEETS_REBEL` (which is in `BOSS_WARNING_NODE`), omits `SQUAT_REFUEL_STATION` and `REBEL`,
  and states "1/5 each" odds the files do not carry.
- [[sector-uncharted-nebula]] — "pool built from dedicated `NEBULA_*` lists rather than the generic
  ones" is wrong: 3 of 7 entries are generic, covering 29 of 48 events.
- [[sector-civilian-sector]] — "more stores and item beacons than any other non-home sector" is
  contradicted by `ENGI_SECTOR` and `LANIUS_SECTOR`; its `startEvent` is commented out in the XML
  with a developer TODO, which answers its own open question about the missing start beacon.
- [[sector-abandoned-sector]] — "heaviest item allocation in the game" is second to both Engi
  sectors; and its open question guessing oxygen drain for `HOSTILE_ENVIRONMENT_LANIUS` is answered:
  the three events are asteroid, pulsar and an ASB aimed at the *enemy*.
- [[sector-mantis-controlled-sector]] — "narrowest event pool of any faction sector" is not
  supported (37 distinct events is mid-pack); and quests do start here despite no `QUESTS_*` entry.
- [[sector-rock-controlled-sector]] — "the game's largest neutral allocation at 7–8" is
  contradicted by `CRYSTAL_HOME` at 12–12.
- [[sector-rebel-controlled-sector]] — the pool is not the pirate pool "swapped to `_REBEL` lists";
  the `ITEMS` entry is shared, not swapped.
- Answerable open questions now closed by the data: `ROCK_UNLOCK1`'s chain and reward
  ([[sector-rock-homeworlds]]), `NEBULA_SLUG_FIGHT_UNLOCK` ([[sector-slug-home-nebula]]),
  `MANTIS_NAMED_THIEF` ([[sector-mantis-homeworlds]]), `FLAGSHIP_CONSTRUCTION`
  ([[sector-rebel-stronghold]]), `ZOLTAN_CREW_STUDY` without the pod
  ([[sector-zoltan-controlled-sector]]).

---

## [2026-08-15] ingest | Sectors as a system — 12 Fandom pages on map generation, fleet pursuit and the store economy

**Acquisition pass only.** Fetched via the MediaWiki API (`api.php`, same user-agent and
throttle as `tools/pull-fandom.ps1`, which was not modified). Filed to `raw/wiki/`, appended
to `raw/wiki/_manifest.csv`, one `wiki/sources/` page each. **No `wiki/sectors/` page was
touched** — putting these facts onto the per-sector pages is a follow-up.

### The structural finding
Every individual sector title on Fandom — `Civilian Sector`, `Rock Homeworlds`,
`Uncharted Nebula`, `The Last Stand`, all 20 of them — is a **redirect to the single
`Sectors` page**. There are no per-sector pages to ingest. `Sector Map`, `Federation Space`
and `Standard Space` do not exist at all.

### New raw files (all Retrieved: 2026-08-15)

| File | Title | Rev |
|---|---|---|
| `raw/wiki/sectors.md` | Sectors | 74796 |
| `raw/wiki/beacons.md` | Beacons | 71696 |
| `raw/wiki/rebel-fleet.md` | Rebel Fleet | 73264 |
| `raw/wiki/environmental-hazards.md` | Environmental Hazards | 74893 |
| `raw/wiki/stores-and-resources.md` | Stores and resources | 74856 |
| `raw/wiki/template-stores-number-of-stores-by-sectors.md` | Template: Stores: number of stores, by sectors | 73433 |
| `raw/wiki/template-stores-additional-stores-from-events-by-sectors.md` | Template: Stores: additional stores from events, by sectors | 73435 |
| `raw/wiki/scrap.md` | Scrap | 73343 |
| `raw/wiki/sensors.md` | Sensors | 73457 |
| `raw/wiki/ftl-advanced-edition.md` | FTL: Advanced Edition | 74567 |
| `raw/wiki/the-rebellion.md` | The Rebellion | 68216 |
| `raw/wiki/guides-and-tips.md` | Guides and tips | 74605 |

`raw/wiki/random-events.md` was already present from an earlier pull and was not re-fetched
(`raw/` is immutable).

### New source pages
[[source-fandom-sectors]], [[source-fandom-beacons]], [[source-fandom-rebel-fleet]],
[[source-fandom-environmental-hazards]], [[source-fandom-stores-and-resources]],
[[source-fandom-template-stores-number-of-stores-by-sectors]],
[[source-fandom-template-stores-additional-stores-from-events-by-sectors]],
[[source-fandom-scrap]], [[source-fandom-sensors]], [[source-fandom-ftl-advanced-edition]],
[[source-fandom-the-rebellion]], [[source-fandom-guides-and-tips]].

### What this adds that `sector_data.xml` cannot
- The **allocation-vs-realisation gap**: sectors hold 19–24 beacons, events are placed in
  file order, and placement stops when beacons run out. Several sector definitions allocate
  more slots than 24 beacons — so bottom-of-list entries are frequently never placed.
- `NEBULA_*` lists are processed **first**, out of file order, and cloud graphics convert
  overlapped non-nebula beacons into extra nebula beacons.
- Leftover beacons fall back to `NEUTRAL` (`OVERRIDE_NEUTRAL` under AE); exit events come
  from a shared `EXIT_LIST` outside the sector definition.
- **Rebel fleet advance modifiers**, quantified for the first time in this wiki.
- **Quest-marker placement rules** — overwrite exclusions, the nebula ban, the push into the
  next sector, the sector-7 cancellation.
- **Guaranteed store counts for all 13 sector types** in one table, plus which store-spawning
  events reach which sector.

### Contradictions flagged
- **Nebula pursuit reduction in nebula sectors.** [[source-fandom-rebel-fleet]] says the
  advance is reduced "by 1/5 of regular beacon advance rate"; [[source-fandom-sectors]] and
  [[source-fandom-environmental-hazards]] say "by 20%". Reduce-*to*-20% vs reduce-*by*-20%
  are very different. No file in `raw/gamedata/` carries pursuit rates. Unresolved.
- **The `Sectors` page contradicts its own tables by design.** Its NOTE 1 warns that the
  per-sector store/distress/quest counts it prints — the same numbers already in
  `wiki/sectors/` — describe allocation, not what a player sees. Both readings stand.
- **Unverifiable, not contradicted**: "19–24 beacons", the 6×4 / 80% grid, the 165-pixel
  connection radius and the 48/32/20 sector-colour split are all sourced to the xftl
  reverse-engineering notes, which this repo does not hold.
- No contradiction found against `sector_data.xml` on any value both state. Store counts,
  `minSector` (read 1-indexed) and `unique` all match across every sector.

### Gap
The Fandom wiki has **no content of its own on sector choice** — how many next-sector
options appear, which sectors connect, any depth rule beyond `minSector` — and **no sourced
sector danger ranking**. Its entire routing guidance is three outbound links (Crow Revell's
2019 sector guide and 2022 sector tier list, mekloz's sector-profit Reddit dataset), none of
which this repo holds. Fetching those is the obvious next acquisition.

---

## [2026-08-15] ingest | Beacon generation and map markers — the engine algorithm, and what the icon actually follows

Second acquisition pass on the same brief, prompted by two follow-up questions from the repo
owner. **Still acquisition only — no `wiki/sectors/` page was touched.** The headline: the
authoritative answers were not on Fandom at all. They were in the xftl reverse-engineering
notes (which Fandom merely *cites*) and in `raw/gamedata/text_misc.xml`, which we already held.

### New raw files (Retrieved: 2026-08-15)

| File | Title | Rev |
|---|---|---|
| `raw/wiki/augmentations.md` | Augmentations | 74810 |
| `raw/wiki/game-bugs.md` | Game bugs | 74618 |
| `raw/wiki/template-distress-events-by-sectors.md` | Template: Distress events by sectors | 74574 |
| `raw/modding/2026-08-15-xftl-sector-map.txt` | xftl `doc/sector-map` | no upstream rev |
| `raw/modding/2026-08-15-xftl-stores.txt` | xftl `doc/stores` | no upstream rev |

New source pages: [[source-fandom-augmentations]], [[source-fandom-game-bugs]],
[[source-fandom-template-distress-events-by-sectors]], [[source-xftl-sector-map]],
[[source-xftl-stores]].

### 1. Beacon generation — layout first, allocation second
`raw/modding/2026-08-15-xftl-sector-map.txt` names the engine methods. Summary in
[[source-xftl-sector-map]]. The load-bearing correction: **`PopulateGrid` builds and connects
the beacon graph with no reference to events; the `sector_data.xml` min/max counts are then
poured into whatever beacons exist.** So the counts are *satisfied in file order until the
beacons run out* — not satisfied exactly, and not describing the map. Also captured: the
sector-column graph (2–4 per column, first column always 2, six middle columns), the exit
beacon's ≥5-jump constraint with 16 retries, the 20%-empty-cell rule with its anti-clustering
guard, the 110×110 cell / 165px connection radius, and the Last Stand base/flagship placement
constants.

### 2. Beacon markers — the icon follows the `<distressBeacon/>` tag, not the allocation list
Settled, and from two independent directions:

- `raw/gamedata/text_misc.xml` (already held, [[source-text-misc]]) carries the **complete
  marker vocabulary** as `map_*_loc` strings — `map_distress_loc`, `map_merchant_loc`,
  `map_store_loc`, `map_quest_loc`, `map_exit_loc`, `map_repair_loc`, `map_ship_loc`,
  `map_unvisited_loc`, `map_nothing_loc`, `map_hostile_loc`, `map_fleet_loc`,
  `map_rebels_loc`, `map_nebula_loc`, `map_nebula_fleet_loc`, `map_ion_loc`,
  `map_asteroid_loc`, `map_sun_loc`, `map_pulsar_loc`, `map_pds_loc`, `map_pds_fleet`,
  `map_base_loc`, `map_boss_loc`, `map_current_loc`.
- Fandom's `Distress events by sectors` template has **exactly 30 rows**, and
  `raw/gamedata/` has **exactly 30 `<distressBeacon/>` tags** — a one-for-one match.
  `ASTEROID_DERELICT_SHIP` is tagged and in the table despite being allocated from
  `NEUTRAL_ENGI`/`NEUTRAL_ROCK`; `ENGI_STATION_DISTRESS`, `PIRATE_CIVILIAN_BEACON` and
  `REBEL_VS_FEDERATION` are untagged and absent despite sitting in distress allocation.
  Fandom states the reason verbatim: *"some other events were meant to occur at a distress
  beacon, but they won't due to coding errors."*
- Same pattern for stores: `<store/>` marks the store beacons — `STORE*`, `NEBULA_STORE*`,
  plus the event stores `QUEST_STORE`, `QUEST_ESCORT`, `PIRATE_BRIBER`, `SLUG_DRINK`,
  `ZOLTAN_TRADE_HUB`, `LANIUS_SCARED_CIVILIAN`, `STORE_REBELSIDE`, and the deliberately
  deceptive `NEBULA_SLUG_FAKE_STORE`. **Repair is a separate tag, `<repair/>`, on
  `BOSS_REPAIR_STATION`** — not a store.

### Contradictions flagged
- **Nebula pursuit — RESOLVED, all sides kept.** xftl gives the advance in px/jump: 64 normal,
  32 nebula-in-normal-sector, 51 nebula-in-nebula-sector. That is −50% and −20%, so
  [[source-fandom-environmental-hazards]]'s "by 20%" is right and
  [[source-fandom-rebel-fleet]]'s "by 1/5 of regular advance rate" is misleading wording.
- **Quest marker filter — Fandom is incomplete.** `StarMap::AddQuest` also excludes visited
  beacons, fleet-overtaken beacons, **distress** beacons and the player's current beacon, and
  the nebula exclusion is per beacon, not per area. [[concept-quest-beacon-placement]] cites
  only the Fandom version and should be revised.
- **"Not many jumps left" — now defined.** The candidate must be fewer jumps away than the
  number of jumps before the Rebels reach it. This closes an open question on
  [[concept-quest-beacon-placement]].
- **Sector-7 quests — same outcome, different mechanism.** Fandom says cancelled because
  sector 8 forbids quests; the engine simply never applies the delay from sector 7 on.

### Reads like inference, not datamining
Flagged on the source pages, repeated here: the xftl author's own hedges — the grey fourth
sector-colour value "seems to involve… might be somehow related to the crystal homeworlds? Or
maybe just something cut", the exclusive/inclusive ambiguity in the Last Stand path constants,
"at least in the build I'm looking at", and the note that `AddSectorColumn` is "annoying to
read due to inlining". Fandom's own inference: the NOTE 1 distress caveat reasons from event
ordering rather than from testing, and its quest-overwrite exclusion list carries two
`@to-do: test and verify` comments. None of the xftl document is versioned or dated.

## [2026-08-15] tooling | Sector pages rebuilt on the generation research — placement order and beacon markers

The Fandom/xftl ingest above changed what a sector page should say, so the pipeline and all 19
pages were reworked around it. Spec: `tools/SECTOR-PAGE.md` §4.1b and §4.1c, both new.

**Two findings drove it.**

1. **The allocation table is a queue, not a shopping list.** Lines are filled in
   sector-definition order and generation *stops* when the map runs out of beacons, so file
   order is placement priority and a line near the bottom can receive nothing. The extractor
   had been sorting entries into reading order — throwing away the most useful thing the table
   says. `entries` now keeps file order and carries `placement`; the budget section renders it
   numbered, with `placed first` and `may be cut` chips. Nebula lists jump the queue.
2. **The on-map marker and the allocation entry are different sets.** `<distressBeacon/>` is
   what draws a distress marker, and it does not follow the `DISTRESS_BEACON_*` list.
   `ASTEROID_DERELICT_SHIP` — the Damaged Stasis Pod — is allocated from `NEUTRAL_*` and shows
   as distress; several events inside distress lists carry no tag and never show one. A new
   generated **Beacon markers** section renders both directions. This answers "what can a
   distress-tagged beacon be *here*", which the pool sections could not.

**Corroboration.** The 30 `<distressBeacon/>` tags in `raw/gamedata/` map one-for-one onto the
30 rows of Fandom's distress-by-sector template — the derived set is exact, independently of
Fandom's prose.

**New derived data:** `generation` (grid ceiling, allocation totals, `can_exhaust_map`,
`at_risk_entries`, `always_short_entries`, `cannot_meet_minimum`), `rollup.markers`, and
`earliest_sector`.

**Findings worth keeping:**
- **Hidden Crystal Worlds cannot satisfy its own table.** Minimum allocation 25 against a
  24-beacon ceiling, so `NEUTRAL_CRYSTAL` is always short — the only such line in the game.
- **`minSector` is zero-indexed.** The fact chip now reads "earliest sector 3" where the file
  says `2`; Fandom states the same offset for all six gated sectors.
- Slug Home Nebula and Zoltan Homeworlds are the most squeezed (35 and 33 slots against 24).

**Five errors corrected during the run**, four of them found by the authoring agents:
1. The nebula-first rule matched `NEBULA_` only, so a bare `NEBULA` line did not jump the
   queue — wrong for Federation Space and the Civilian Sector.
2. The markers callout asserted the tagged-elsewhere event is placed *before* the distress
   line. That is Fandom's explanation and it is wrong for every sector it applies to; the
   clause is now derived per sector. **Fandom's outcome holds, its mechanism does not.**
3. The store-marker string claimed fixed stores are "labelled on the map from the start".
   `raw/wiki/beacons.md` is explicit: store and distress markers show only within one jump.
4. `[[source-fandom-template-stores-additional-stores-from-events-by-sectors]]` misread two
   cells of its own table; corrected there, with both readings kept.
5. A beacon floor of 19 is stated by the community wiki alone, so it is carried as data and
   reported, but `at_risk` is computed against the 24 ceiling only.

All 19 pages rebuilt, smoke-tested and determinism-checked; `check-sector-numbers.py` reports
no gate mismatches and 37 subset-claim candidates, each verified by hand.

### Deferred
Backlinks are one-directional: the 19 sector pages now link concept, chain and entity pages
that do not yet point back. `wiki/concepts/quest-beacon-placement.md` needs revising against
`StarMap::AddQuest` (its exclusion list is incomplete and its open question is now answered),
and `wiki/concepts/sector-event-allocation.md` should record that the `OVERRIDE_` substitution
question now has weak community evidence on both sides.

## [2026-08-15] ingest | Beacon-name map cheat — what it would take, and what it would cost

**Question:** a mod that prints each event's name above its beacon on the sector map, including
beacons that have not been revealed — "just tell me where everything is".

**Answer: possible, but only through FTL Hyperspace.** Filed as
`raw/modding/2026-08-15-beacon-name-labels-mod.md` (`source_kind: research`), summarised at
[[source-beacon-name-labels-mod-research]].

**New pages:** `wiki/sources/beacon-name-labels-mod-research.md`.
**Updated:** `wiki/index.md` (Research section, source count 347 → 348).

### What the research established

- **The engine already knows.** Every beacon's event is generated with the sector, not on
  arrival — `StarMap::AddQuest` filters *unvisited* beacons on their store/distress flags
  ([[source-xftl-sector-map]]), and the save regenerates events from `sectorLayoutSeed`. The
  mod is a reveal, not a computation.
- **Vanilla modding cannot reach it.** Slipstream patches data and images; the map is drawn by
  compiled code. Advanced XML does not help.
- **Hyperspace's Lua API exposes the whole thing:** `StarMap.locations`, `FocusWindow.bOpen`,
  `Location.loc/.known/.visited/.event`, and `LocationEvent.eventName` / `.text` / `.store` /
  `.distressBeacon`. `Location.event` reads fine on an unvisited beacon. Drawing is
  `Graphics.freetype.easy_printCenter` inside an `on_render_event(MOUSE_CONTROL, …)` hook —
  there is no star-map render layer, which is the one wrinkle.
- **Label source is already in this repo.** `cards/trees/*.tree.json` maps event id → card
  title for 386 of 449 events, the same table `event-labels` uses. Same names in the card, in
  the event text, and on the map, from one source.
- **`<beaconType>` (Hyperspace's per-event map label) exists** with `req` equipment gating,
  colour, and undiscovered / unvisited / visited tooltips — but its label comes from the
  **first** declaration of an event, not the last.

### Contradiction recorded

> ⚠️ Slipstream: "only the last one counts". FTL-Hyperspace issue #216: beacon labels take the
> first instance. Both are true at different scopes — definitions resolve last-wins, the beacon
> label is kept from the first parse. Consequence: a `<beaconType>` cannot be bolted on with
> the `.append` redefinition trick that `tools/EVENT-LABELS.md` §4 is built on; it needs
> Advanced XML. Noted against [[concept-modding-and-the-append-convention]].

### The cost, which is the real finding

Hyperspace **downgrades Steam FTL 1.6.14 to 1.6.9**, demands every other mod be uninstalled
first, and extends the save format. That collides with three things this repo already relies
on: `raw/gamedata/` was extracted from 1.6.14, `tools/save-watch.py` reads layouts live from
the installed `ftl.dat` and parses vanilla saves only (`SAVE-WATCH.md` §6), and `event-labels`
would need re-patching. The mod is a day's work; the platform change is the decision.

### Cheaper partial route, measured first

`readBeacon` in the save format stores `seen`, `enemyPresent` + `shipEventId`, `fleetPresence`,
`underAttack` and a store's full inventory — but never the beacon's event. `tools/ftlsave.py`
already walks those bytes and discards them. Surfacing them would give a ship/store/fleet
spoiler map with **no game modification at all**, and it is not yet known how much of it is
populated before a beacon is visited. That measurement should come before any Hyperspace work.

### Deferred
- Whether a `<beaconType>` label draws for *undiscovered* beacons is inferred from the struct's
  `undiscoveredTooltip` and from vanilla quest markers, not read from the render code —
  `CustomEvents.cpp` is 270 KB and could not be fetched whole.
- Whether `LocationEvent.eventName` is populated for engine-generated base events.
- The map-origin constant for drawing in `MOUSE_CONTROL`'s coordinate space; xftl gives 45,40
  as the beacon-coordinate origin, to be confirmed against Hyperspace's `CustomMap.cpp`.

## [2026-08-15] tooling | The save's beacon list, kept instead of discarded

Follow-on from the beacon-name research above: before touching Hyperspace, measure what the
save already gives away.

`tools/ftlsave.py` walked the sector's beacon list and threw every field away. It now returns
them, and `--beacons` reports them: per beacon `visit_count`, `seen`, `enemy_present` +
`ship_event_id` + `auto_blueprint_id`, `fleet`, `under_attack`, and a store's full stock, plus
`quest_events` (quest marker event name → beacon id) and the deferred quest list. Byte order is
untouched, so the encounter parse — and the watcher — are unaffected: `--index-report` still
reports 386 cards / 4516 keys / 1741 of 1782 root texts pinning one card.

Verified by a byte-exact round-trip test over three synthetic beacons (unvisited-with-ship,
unvisited store with stock, visited-and-under-attack); two bugs were found and fixed that way
— reversed unpacking of `quest_events`, and a `·` separator the Windows console cannot encode.

**Not yet measured live: no run is in progress, so there is no `continue.sav`.** The question
it exists to answer — how many *unvisited* beacons already name a ship or a store — needs the
command run mid-run:

```
python tools/ftlsave.py "%USERPROFILE%\Documents\My Games\FasterThanLight\continue.sav" --beacons
```

`tools/SAVE-WATCH.md` §3 now records what the beacon list holds, and states plainly that the
save never holds a beacon's event — that one needs the running engine.

## [2026-08-15] tooling | Measured: the save says nothing about a beacon you have not visited

Ran `tools/ftlsave.py --beacons` against a live save (Crystal Cruiser B, sector 1, 21 beacons,
player at beacon 3):

```
beacons       21 total, 20 unvisited
  unvisited  ships 0 (named 0) | stores 0 | seen-flag 3
  all        ships 0 (named 0) | stores 0 | seen-flag 4
```

**Zero of the 20 unvisited beacons carried a ship event, a ship blueprint or a store.** A
sector-1 map certainly contains both, so `enemyPresent` and the store block are runtime state
written on arrival, not generation-time state serialised for the sector. `seen` was set on the
current beacon plus its three neighbours — the one-jump marker rule from `raw/wiki/beacons.md` —
and even those carried nothing.

The parse is sound: the only beacon with `visit_count > 0` is beacon 3, which equals the save's
own `current_beacon_id`, and the encounter block immediately after decodes to coherent start
text. A misaligned read would not land on both.

**Consequence: the no-mod route is dead.** Not merely "cannot name events" — it cannot pre-empt
ships or stores either. Everything about an unvisited beacon lives only in the running engine's
`Location.event`. Naming beacons on the map requires Hyperspace, which is the trade recorded at
[[source-beacon-name-labels-mod-research]] §7. Recorded in that file's §4.1 and in
`tools/SAVE-WATCH.md` §3; the `--beacons` report stays, since it still reports stores, quest
markers and fleet state for where you have been.

### Bonus finding — `event-labels` is confirmed rendering

The same save's encounter text was `"[ Start game ]\r\n\r\nThe data you carry is vital to the
remaining Federation fleet. …"` — label, `LABEL_GAP`, vanilla prose, exactly as
`tools/EVENT-LABELS.md` §3 specifies. Both that spec's §7 and `mods/event-labels/README.md`
claimed "not yet patched into the game"; both now record the confirmation instead. The mod has
been live and working, read back out of the game's own save.

## [2026-08-15] tooling | How Hyperspace extends the save — scoping the watcher rework

Follow-up question before committing to Hyperspace: is adapting the save watcher a rework or a
rebuild? Read out of Hyperspace's source rather than guessed.

- **Profile: redirected, not extended.** `SaveFile.cpp` hooks `FileHelper::readBinaryFile` /
  `fileExists` / `createBinaryFile` so the game's `ae_prof.sav` lands on `hs_prof.sav`
  (prefix `hs`, plus `hs_prof_backup.sav` and `hs_version.sav`). The watcher never reads the
  profile, so this costs nothing.
- **Run save: extended inside `ShipManager::ExportShip`, after `super(file)`.** Hyperspace
  appends its blocks at the end of the ship block — which sits *before* the beacon list and the
  encounter, i.e. inside the prefix `ftlsave.py` walks. A Hyperspace save would desync at the
  ship/cargo boundary, not at the encounter.
- **The extension is conditional.** `CustomSystems.cpp`'s hook loops
  `SYS_CUSTOM_FIRST .. GetLastSystemId()` and writes nothing when no custom systems exist;
  `CustomCrew.cpp` and `CrewMember_Extend.cpp` serialize nothing. Hyperspace with no content
  mod may leave the save byte-identical to vanilla. Not verified, and not every `ExportShip`
  hook was enumerated — GitHub code search was rate-limited.
- **Answer: a rework, and a bounded one.** The architecture is untouched — cards come from
  vanilla XML, so the text→card index, resolver, stickiness and page all stand. What changes is
  skipping appended blocks in one place.
- **No Lua shortcut.** Hyperspace's Lua sandbox has `io`/`os`/`package`/`debug` removed
  (`SAVE-WATCH.md` §2), so no in-game script can hand the watcher the current event; save
  parsing remains the mechanism.

Recorded in `tools/SAVE-WATCH.md` §6. The decisive test is one command after install:
`python tools/ftlsave.py <continue.sav>` — landing on five real ship-event ids at once is the
existing self-check, and tells us whether any work is needed at all.

## [2026-08-15] tooling | Hyperspace installed, and `beacon-reveal` — every beacon named on the map

The mod the day's research was scoping. Built, patched in, and confirmed loading; the one thing
not yet done is looking at the map with human eyes.

### Install, in order

1. **Backed up** `Documents\My Games\FasterThanLight\` to
   `FTL-backup-2026-08-15-pre-hyperspace\` (profiles + the in-progress save), plus the 1.6.14
   `FTLGame.exe` and `settings.ini`. Slipstream's own `backup\ftl.dat.bak` is the pristine
   vanilla data and was left alone.
2. **Confirmed 1.6.14** from `FTL.log` (`Version: 1.6.14`) — the downgrader's precondition.
3. **Reverted to vanilla data** by copying `ftl.dat.bak` over `ftl.dat`. Note: Slipstream's
   `--patch` with *no* mods throws a NullPointerException, so it cannot be used to unpatch.
4. **Downgraded** with Hyperspace 1.22.2's `downgrade.bat`: it copies `FTLGame.exe` to
   `FTLGame_orig.exe`, then applies BPS patches with `flips.exe`. The 1.6.22 patch is rejected
   ("not intended for this ROM") and the 1.6.14 one applies — both expected. Result: 125 MB exe,
   original preserved.
5. **Patched** `Hyperspace.ftl`, `event-labels.ftl`, `beacon-reveal.ftl` in that order via
   Slipstream's CLI (`java -jar modman.jar --patch …`) — no GUI needed, which is worth knowing.

### Verified against research

- **`hs_prof.sav`, `hs_prof_backup.sav`, `hs_version.sav` appeared; `ae_prof.sav` untouched** —
  exactly the profile redirect read out of `SaveFile.cpp` this morning.
- **`ftl.dat` was not touched by the downgrade**, so `raw/gamedata/` provenance still holds.
- **The watcher still resolves cards** on the pre-existing save (`event_AUTO_CIVILIAN_c2_text`
  → `auto-ship-attacking-civilian`).

### The mod

`tools/build-beacon-mod.py` + `tools/beacon-reveal.lua.tmpl` → `mods/beacon-reveal/`, spec at
`tools/BEACON-REVEAL.md`. 386 labels, same card titles as `event-labels`, nothing hand-written
per event, byte-identical rebuilds.

- Reads `starMap.locations` and each `Location.event.eventName` — which is populated on
  unvisited beacons, the whole basis of the cheat.
- Draws on the `MOUSE_CONTROL` render layer gated by `starMap.bOpen`, because
  `Defines.RenderEvents` has no star-map layer.
- Position is **`starMap.position + loc.loc`**, taken from Hyperspace's own
  `StarMap::OnRender` reimplementation in `CustomMap.cpp` rather than guessed, with the xftl
  `45,40` origin as a logged fallback.
- Registration uses **Advanced XML** (`mod:findLike` + `mod-append:script`) because
  `hyperspace.xml` allows only one `<scripts>` element — a plain append would declare a second.
  First use of Advanced XML in this repo.

**Confirmed loading:** `FTL_HS.log` shows `Loading Lua file: data/beacon-reveal.lua` then
`beacon-reveal: loaded, 386 names`.

### Open

- **Nobody has seen the labels.** Desktop screen capture returns solid-colour frames for every
  monitor on this machine (windowed mode too), so the visual check needs the user. The mod logs
  one line per sector — how many beacons it named and how many were unvisited — so the
  *functional* question is answerable from `FTL_HS.log` even without a screenshot.
- **The watcher is unfixed because it is not yet broken.** Adapting it needs a save written *by*
  the Hyperspace build; the current `continue.sav` predates the install. The prediction from
  source (`SAVE-WATCH.md` §6) is a desync at the ship/cargo boundary from `ShipManager::
  ExportShip` appending after `super()` — and possibly no desync at all, since the one hook read
  in full writes nothing when no custom systems are defined.

## [2026-08-15] tooling | beacon-reveal works — two bugs found by log and screen, origin measured

The mod draws. First run on screen showed all 21 events named, unvisited ones included
("Giant alien spiders", "Pirate briber", "Long-range beacon (sector exit)"), so the premise
holds: `Location.event` is readable on a beacon the player has never been to.

Two defects, both caught by evidence rather than inspection:

1. **`SWIG_IndexError: in vector::__getitem__()`.** SWIG's `std::vector` binding *raises* on an
   out-of-range index instead of returning nil, so the deliberately-tolerant loop over
   `0 .. size()` threw on its last iteration and, under `pcall`, silently killed all drawing for
   the frame. The tolerance was the bug. `detect_base` now probes `locations[0]` once, logs the
   answer, and the loops run `base .. base + size() - 1`.
2. **The documented map origin is wrong.** `starMap.position` is not exposed to Lua, so the mod
   fell back to the `45,40` origin in `raw/modding/2026-08-15-xftl-sector-map.txt` — which put
   every label 337 px left and 90 px above its beacon.

**ORIGIN measured as (382, 116)** by pairing three widely separated beacons against their own
drawn labels, in FTL's 1280x720 virtual space:

| pair | beacon | label centre | delta |
|---|---|---|---|
| exit beacon | 999, 483 | 661, 393 | 338, 90 |
| abandoned station | 397, 506 | 61, 415 | 336, 91 |
| giant alien spiders | 574, 258 | 237, 168 | 337, 90 |

Agreement to 1 px across the map is what proves it is a **pure translation with no scaling** —
a scale error would have diverged between the near and far pairs. A hover probe was added that
logs the map coordinates of the beacon under the cursor, so the constant can be re-measured
later without a rebuild.

> ⚠️ **CONTRADICTION:** xftl states beacon coordinate 0,0 "is drawn at 45,40 relative to the
> outer edge of the window". Measured against the running game, the offset is 382,116. Both are
> recorded; the measurement wins for this build (FTL 1.6.9 under Hyperspace 1.22.2 at 4K), and
> the discrepancy may be a version difference, a different reference edge, or the map panel's
> own offset. Not resolved — noted against [[source-xftl-sector-map]].

Also observed: Hyperspace writes `hs_crash.flag` at launch, and FTL does **not** write
`continue.sav` until the first jump — the current run had no save on disk at all, which is why
the watcher question is still open.

## [2026-08-15] tooling | beacon-reveal confirmed on screen — and a self-inflicted debugging round

The measured origin (382,116) is correct: every beacon in a Civilian Sector map is named, each
label sitting above its own beacon. Confirmed against a beacon whose vanilla tooltip still read
*"An unvisited location."* while the mod named it "Pirate fight" — the reveal, demonstrated in
one frame.

**The fix appeared not to work, and the reason was mine.** The constant was corrected and the
mod rebuilt and copied to Slipstream's `mods/`, but the Slipstream patch was never re-run, so
`ftl.dat` still held the previous build. The game reads Lua from `ftl.dat` at startup, so it
kept loading the old file. The evidence was sitting in plain sight and was not read carefully
enough the first time:

```
[Lua]: beacon-reveal: starMap.position unavailable, using fallback origin 45,40
```

`45,40` was already dead in the source. Comparing mtimes settled it in one command:
`beacon-reveal.ftl` 14:58, `ftl.dat` 14:52.

**Fixed structurally, not by remembering harder.** `build-beacon-mod.py --install` now packs,
copies to Slipstream and patches in one step, with the correct mod order baked in as
`PATCH_ORDER`. Documented at the top of `tools/BEACON-REVEAL.md` §1 and in the mod README,
both stating the trap explicitly: an unpatched rebuild is invisible.

Also confirmed working this round: `detect_base` reports `vector index base = 0`, and the
per-sector line reads `sector 1: named 21 beacons, 20 of them unvisited`.

### Still open
- **Cosmetic collisions.** Long names overlap each other and the vanilla `STORE`/`EXIT` tags on
  a crowded map. `easy_measureWidth` is the tool for eliding; nothing does it yet.
- **The watcher remains untested against Hyperspace**, because FTL still has not written a
  `continue.sav` — the current run has not jumped, so the only save on disk is the 12:48 vanilla
  one, which still parses fine (`event_AUTO_CIVILIAN_c2_text`, 3851 of 3927 bytes consumed).

## [2026-08-15] tooling | beacon-reveal v2 — category boxes on the map, event name on hover

Reworked at the user's request: the map now shows the beacon's **category** in a box styled like
the game's own STORE/EXIT labels, and hovering a beacon shows the **concrete event** below it.
Confirmed on screen in an Engi Controlled Sector: `DISTRESS_BEACON_ENGI` boxed in orange on the
beacon, `Engi distress - Rebel fight` in a box underneath while hovered.

### Where a category comes from

The runtime only offers an event id. The category is the sector **event pool** — the
`<eventList>` named in `sector_data.xml` (`<event name="DISTRESS_BEACON_ENGI" min="1" max="3"/>`)
— so the build projects it out of `sectors/data/*.sector.json`, which
[[source-sector-data]]'s pipeline already expands from pool to concrete events. No second parse
of the game files; re-extract the sectors and the categories follow.

**Scoped per sector, and the measurement is why.** Globally, 86 of 274 carded events sit in more
than one pool (`ASTEROID_EXPLORE` is in six `NEUTRAL_*` pools). Scoped to a single sector's pool
list, ambiguity falls to **58 of 997 sector/event pairs — 5.8%**. Those remaining collisions
(`FRIENDLY_BEACON` in both `NEUTRAL_CIVILIAN` and `DISTRESS_BEACON` in Civilian Sector) resolve
first-in-sector-order, deterministically, and the build prints the count so it cannot drift.

Fallback chain: current sector's table → `ANY_SECTOR` (187 events whose pool never varies) →
the raw event id, drawn with a dim outline so "unknown" looks unknown.

### Rendering

`GL_DrawRect` + `GL_DrawRectOutline` + `easy_measureWidth` size a box to the text; the outline is
coloured by the pool's `section` (store green, distress orange, hostile red, nebula purple,
quest blue). `easy_printCenter`'s y is the glyphs' vertical centre — measured, and now recorded
in the spec, since the box geometry depends on it.

Hover is matched on `hoverLoc.loc` **coordinates**, not object identity: SWIG does not promise
the same wrapper object for the same pointer.

**`GET_BEACON_HAZARD` was deliberately not used.** It is Hyperspace's native beacon-tooltip hook
(`Location loc -> string hazardText`), but returning a value marks the beacon as a *hazard*,
putting a danger icon on every beacon. Drawing our own box keeps the map honest.

### Caught by the verifier

The new checks earned themselves immediately: the build failed on a non-ASCII byte — a `§` in a
comment in the Lua *template*, which would have shipped a glyph FTL cannot render. Also added:
every sector must appear in `BY_SECTOR`, no pool name may collide with a card title (the two are
easy to cross-wire and it would only show on the map), and the three drawing primitives must be
present.

### Incidental findings
- **A vanilla 1.6.14 save loads fine under Hyperspace 1.22.2** — the pre-downgrade run continued
  without complaint.
- **Force-killing FTL makes Hyperspace report a crash** on next launch ("A Hyperspace mod crash
  was detected"), because `hs_crash.flag` is only cleared on a clean exit. Close the window
  rather than `Stop-Process`.
- **FTL still had not written `continue.sav`** — the in-memory run was in sector 2 while the save
  on disk was a sector-1 save from before the install. The watcher work remains blocked on one
  jump.

## [2026-08-15] tooling | The watcher, fixed for Hyperspace — and it was looking at the wrong file

Two problems, not one, and the first had been quietly wasting the afternoon.

### 1. Hyperspace moves the run save

`SaveFile.cpp` redirects the game's file access through the `hs` prefix. That covers **the run
save too**, not just the profile as this morning's research concluded: a modded install writes
**`hs_continue.sav`** and leaves `continue.sav` untouched. That is why "FTL still hasn't written
a save" kept being true — it had been saving next door the whole time.

`find_save` now watches `continue.sav` and `hs_continue.sav` in both save directories and takes
the most recently written, re-resolved every poll. Installing or uninstalling Hyperspace needs
no restart, no flag, no edit.

### 2. A Hyperspace save is not FTL's shape

Enumerated from the cloned source rather than guessed at — twelve insertion points:
`ShipManager::ExportShip` hooked by six files (one writing *before* `super`, five after,
`CustomShips` writing per **room**), `CrewMember::SaveState` hooked per **crew member**, and
`StarMap::SaveGame` hooked by six more. Several are variable-length and nested
(`StatBoost::Save`, `Animation::SaveState`, `ShipSystem::CompleteSave`).

Porting that to Python would be a reimplementation of Hyperspace's serialisation that breaks on
its next release. **So the Hyperspace path does not walk the file — it looks at it.**
`ftlsave.scan_encounter_text` scans for length-prefixed strings shaped like a string-table id
(`^(event|text)_[A-Za-z0-9_]+$`). On the real 5524-byte save the entire file yields **exactly
one** candidate, `text_START_BEACON_ENGI_1` — the event that was on screen.

Verified both ways: `hs_continue.sav` → `source: "scan"` → card `start-beacon-engi`;
`continue.sav` → `source: "parse"` → card `auto-ship-attacking-civilian` with sector and beacon
intact. `--index-report` unchanged at 386 cards / 4516 keys / 1741 of 1782.

**What the scan gives up**, recorded in the spec rather than glossed: no sector or beacon number
(both `null`), no five-valid-ids self-check, and no support for prose-valued encounter text. Its
correctness argument is the index lookup downstream, not the parse. The structured parser still
runs first and still owns the vanilla case.

Earlier notes in `SAVE-WATCH.md` §6 predicted a desync "at the ship/cargo boundary" and hoped it
might cost nothing. Both were wrong: the first insertion is *before* the ship blueprint string,
and there are twelve of them. The section now records what was measured instead.

## [2026-08-15] tooling | beacon-reveal v3 — text inside the box, and the game's own tooltip repurposed

Three changes, all confirmed on screen.

### The text sat low because a measurement was recorded backwards

**`easy_printCenter`'s `y` is the top of the line box, not its centre.** The spec said centre.
That error hid for hours because it was *absorbed into `ORIGIN_Y` during calibration* — the
origin was solved from where labels landed, so a constant half-line offset just moved the fitted
origin by the same amount. Changing the font from id 10 to 6 changed the line height and broke
the coincidence, and the text dropped out of its box.

Text is now drawn at `y - floor(h/2)`, i.e. `-7` at the measured line height of 15 — which is
exactly the correction the user asked for by eye. Box height is `15 + 2*3 = 21` virtual px
(63 physical at 4K, where FTL scales 1280x720 by 3).

### The hover box is gone; the game's tooltip now carries the event name

Instead of drawing a second box, the mod writes into the tooltip the game already shows —
the one that reads "An unvisited location.". Hyperspace's `StarMap::MouseMove` sets it with
`GetMouseControl()->SetTooltip(GetLocationText(hoverLoc))` during the loop; the `MOUSE_CONTROL`
before-callback runs after the loop and before `MouseControl::OnRender`, so writing there is the
last word for that frame and the game renders our string with its own styling, placement and
edge-flipping. `Hyperspace.Mouse` exposes `SetTooltip`, `InstantTooltip` and a readable
`tooltip` (`lua/modules/hyperspace.i`); the write is guarded on change because `SetTooltip`
restarts the tooltip timer.

Confirmed: hovering the distress beacon in the Engi sector now reads **"Pirate ship distress
trap"** in the vanilla tooltip box, with no second box drawn.

### Method note

The Hyperspace source was **cloned** (`--depth 1 --filter=blob:none --sparse`) rather than
fetched page by page. Two things this afternoon were only answerable from the whole tree:
enumerating all twelve save-hook insertion points, and finding `MouseControl::SetTooltip` in
`lua/modules/hyperspace.i`. Earlier WebFetch answers on the same files were **wrong by
truncation** — `CustomCrew.cpp` was reported to contain no serialization hooks when it hooks
`CrewMember::SaveState` at line 2930. Clone before concluding a big file lacks something.

## [2026-08-15] tooling | Fullscreen minimize came back — the launch path, not Hyperspace

The user reported the two-monitor fix (`mods/fullscreen-no-minimize/`) had stopped working
since installing Hyperspace. Reproduced it directly: focused a window on the left monitor,
screenshotted the center one, FTL was minimized to the taskbar.

### The cause is delivery, not the engine

`SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS` is read from the **process environment**, which is fixed
at process creation. Read the running game's environment block out of its PEB
(`ReadProcessMemory`, 32-bit WOW64 target) and the answer was immediate:

| Process | Has the variable |
|---|---|
| `steam.exe` (pid 73884) | yes, `=0` |
| `FTLGame.exe` (pid 90604) | **no** |

The game's environment instead held `CLAUDECODE=1`, `AI_AGENT=claude-code_2-1-221_agent`,
`MSYSTEM=MINGW64` and a Git-Bash `PATH`. **A previous agent session launched the game from a
Bash tool call**, so it inherited this agent's environment — and this agent process started
before the variable was installed at user scope. The user-scope setting was correct the whole
time and Steam had it; the game was simply two processes away from a stale one.

### Hyperspace is not implicated, and that is checkable

- It swaps `FTLGame.exe` (retail 1.6.22, 5.5 MB → patched 1.6.14, 125 MB; original kept as
  `FTLGame_orig.exe`) and injects via `xinput1_4.dll`. Different binary, so worth re-checking:
  both `SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS` and `fullscreen_minimize_on_focus_loss` are still in
  its string table.
- `Hyperspace.dll` contains neither string. Of the 1118 hooks in `zhl.log`, none is on focus or
  fullscreen handling — `CApp::OnInputFocus`, `CApp::UpdateFullScreen` and
  `CApp::UpdateWindowSettings` are resolved but never hooked.

### Shipped

- `mods/fullscreen-no-minimize/verify-env.py` — reads the running `FTLGame.exe`'s environment
  from its PEB (read-only) and reports PASS/FAIL, naming the launcher on FAIL. This is the
  check that was missing: "is the variable set?" and "did it reach the game?" are different
  questions and they came apart silently.
- `launch-ftl.cmd` — hardened; sets the variable in the command rather than inheriting it, so
  it is immune to every stale-parent case. Warns if Steam is absent.
- `README.md` — new Hyperspace section, files table, smoke test now leads with `verify-env.py`.
- `CLAUDE.md` §5.2d — never launch `FTLGame.exe` bare from a tool call; use the launcher.

### Two findings worth keeping

**The running game had no save on disk.** Under Hyperspace the run save is `hs_continue.sav`,
and no such file existed anywhere while a Sector 2 run was live — `continue.sav` was stale from
12:48, pre-patch. Killing the process would have destroyed the run, so it was left alone. Worth
watching whether Hyperspace writes that file at all on this install.

**Still unverified:** whether FTL pins `fullscreen_minimize_on_focus_loss` itself, which would
make the variable inert regardless of delivery. Every failure so far has been a `verify-env.py`
FAIL. The proof would be a PASS launch that still minimizes.

## [2026-08-15] tooling | Watcher picked up nothing — the process was older than the code

Second report of "broke after Hyperspace", same shape as the fullscreen one an hour earlier:
a long-running process holding a stale snapshot of the world.

### What was wrong

`--once` resolved the current event perfectly (`hs_continue.sav` → `event_PIRATE_STATION_CROPS_c2_text`
→ `remote-settlement`) while the server on 8787 reported nothing. That gap is the whole
diagnosis: `--once` runs the code **on disk**, the server runs the code it **imported at
startup**. The listening process had been up since **11:46**, and `SAVE_NAMES` only learned
about `hs_continue.sav` at **15:44**. So it was watching `continue.sav`, which Hyperspace
stopped writing at 12:48. Nothing about it looked unhealthy — it served pages, it just never
saw a save change.

Restarting it fixed it; it now follows the run live.

### Also settled

`hs_continue.sav` **does** get written — 8141 bytes at 16:50. The earlier note that no run save
existed was true of the killed run only, and that run's `CONTINUE` being greyed out at the
menu confirmed it independently. Hyperspace saving is not broken; the earlier session was.

### Shipped

- `tools/save-watch.py` — a staleness guard. Records the mtimes of `save-watch.py` and
  `ftlsave.py` at import; the first poll that sees either change prints, once,
  `[stale] … still running the old code -- restart it`. Flushed, because the watcher is
  normally launched into a background log where an unflushed line is never read.
- `tools/save-watch.py` — the startup banner printed `watching None` for every unpinned run
  (it echoed `args.save`, which is `None` unless `--save` was passed). It now names the file
  actually resolved, which is what tells you at a glance whether it found `hs_continue.sav`.
- `tools/SAVE-WATCH.md` §5 — "nothing is picked up at all, and `--once` works fine" now leads
  the misbehaviour list, since it is both the most likely cause and the least visible.

### The general lesson, twice in one afternoon

A process is a snapshot of its inputs at creation: its environment, and its imported source.
Changing either on disk does not reach anything already running, and both failures present as
"the thing that used to work stopped working" with no error anywhere. Both are now checkable —
`verify-env.py` for the game's environment, the `[stale]` line for the watcher's code.

## [2026-08-15] tooling | Beacon-reveal category table: three labelling gaps closed

Started from an observation on a live map: the Civilian Sector page promises `ITEMS 2–3`,
but only one `ITEMS` box was drawn. `FTL_HS.log` — which prints sector generation verbatim —
showed the sector had in fact allocated `ITEMS x2`. The page was right; the mod was
mislabelling. Three distinct causes, all in `load_categories()`.

### 1. A nested list made an entire allocation line unreachable

`NEUTRAL_CIVILIAN` contains `<event load="DISTRESS_BEACON"/>` (`newEvents.xml:158`), so
flattening makes all 14 distress events members of both pools. Ranking by sector order alone
handed every one of them to `NEUTRAL_CIVILIAN` (line 3) over `DISTRESS_BEACON` (line 5):
**`DISTRESS_BEACON` could never be drawn in Civilian Sector or Federation Space**, though it
rolls 1–2 beacons every game. `extract-sector.py` already recorded the inner list as `via`;
it now wins whenever it is also one of that sector's own allocation lines. 28 pairs resolve
this way, and `verify()` now fails on any unreachable line — tested against the old rule,
which it correctly rejects.

### 2. Advanced Edition additions were never merged

`entry["override"]["added"]` was computed and then ignored by the mod build. 31 pairs across
16 sectors, `STORE_REBELSIDE` in `ITEMS` among them — which is exactly the beacon that
started this. Now merged.

### 3. The fallback list was not in the table at all

`NEUTRAL` / `OVERRIDE_NEUTRAL` fills any beacon left over once a sector's table is exhausted,
but almost no sector names it in `sector_data.xml`. Those beacons either drew a raw id or —
worse — were mis-attributed to a real pool by the reverse lookup (`PIRATE_CIVILIAN` →
`NEUTRAL_CIVILIAN`, `AUTO_REFUEL_STATION` → `HOSTILE_CIVILIAN`), inflating that pool's
apparent count. `extract-sector.py` now emits `generation.fallback_events` (AE ∪ vanilla) and
the build appends it last, after every real line.

### Shipped

- `tools/extract-sector.py` — new `fallback_events()`, emitted under `generation`. All 19
  profiles re-extracted.
- `tools/build-beacon-mod.py` — three-rule `load_categories()`; new unreachable-line check in
  `verify()`; build now reports nested and AE-merged counts.
- `tools/BEACON-REVEAL.md` §1b rewritten, §5 gains the new check.
- Civilian Sector table 77 → 93 events; 190 events now have an unambiguous global pool.

Built, verified and packed. **Not installed** — FTL was mid-run, and Slipstream cannot
rewrite `ftl.dat` under a running game.

### Contradiction resolved

[[concept-sector-event-allocation]] asked whether `OVERRIDE_X` replaces `X`. The same log
settles it for sector allocation: an `ITEMS` allocation produced `STORE_REBELSIDE`, which
exists only in `OVERRIDE_ITEMS`. Recorded there with its limits — it does not reach the
call sites where the engine resolves a list name directly. The evidence is a live session's
`FTL_HS.log` and is **not yet captured in `raw/`**.

## [2026-08-15] tooling | Sector pages: budget lines open onto their events, beacon boxes link to cards

The beacon budget said how many beacons a line places without ever saying *which* events it
could place — that answer sat further down the page in the pool sections, out of reach of the
question. Each budget row is now a `<details>`: click the line, it opens onto exactly the
events that line can place. Every beacon box on the page — budget expansion, markers section,
pool sections — is now a link to `../cards/card-<slug>.html`.

### Shipped

- `tools/build-sector.py` — `event_html()` emits `<a class="ev link">` when the event has a
  card (`slug`/`card` were already in the extracted data, so nothing new is derived);
  `budget_html()` wraps each row with events in `<details>/<summary>`.
- `tools/sector-page-render.html` — summary styling, rotating chevron, hover states, nested
  pool panel; hover recolours three borders only, so the left tag rail keeps its colour.
- `tools/sector-vocab.json` — one new string, `budget.expand`.
- `tools/smoke-sector.py` — resolves every beacon-box `href` against the page's directory and
  fails on a missing card; the OK line now reports linked boxes and expandable rows.
- `tools/SECTOR-PAGE.md` — new §6.1; §7, §9 and §11 updated.
- All 19 pages rebuilt and smoke-tested: **2,358 beacon boxes, all linked, all resolving**.
  Rebuild is byte-identical across runs.

### The constraint worth remembering

The links are **relative**, so they work on a page opened from `sectors/` on disk and go
nowhere on a published artifact — artifact URLs are minted at publish time, so no absolute
link is knowable when the page is built. The expansion itself is pure HTML and works either
way. Live links on a published page would need a registry of published card URLs, which does
not exist: 0 of 387 cards are published.

## [2026-08-15] tooling | Beacon boxes open onto their card, in the page

Following the linking work earlier today: clicking a beacon box navigated away to the card.
Now the box opens and the card renders underneath it, without leaving the sector page — and
without the sector page carrying any card content.

### The constraint that shaped it

From `file://` a page cannot read a sibling file. Probed directly in both browsers, against
the real `sectors/` → `cards/` hop:

| Mechanism | Chrome `file://` | Firefox `file://` (stock prefs) |
|---|---|---|
| `fetch` / `XHR` / dynamic `import()` | blocked | blocked |
| classic `<script src>` | **works** | **works** |

Firefox matters because it is the default `.html` handler on this machine. Playwright's
Firefox appeared to allow everything until its `playwright.cfg` turned out to set
`security.fileuri.strict_origin_policy=false`; with the stock value restored it matches
Chrome exactly. `tools/smoke-inline.py` forces that pref back on for the same reason.

So each event's tree ships a second time as a one-line `FTLCard.define()` call that a
`<script>` tag can load, and the loader pulls the runtime, the CSS and one payload on demand.

### Shipped

- `tools/card-runtime.js` — **new, and now the only copy of the renderer**. Extracted from
  `event-card-render.html` and made reentrant: `FTLCard.render(root, data, vocab)` builds its
  own skeleton, keeps no module state and looks nothing up by document id, because a sector
  page renders many cards into one document and a shadow root has no markup to find.
- `tools/build-card.py` — inlines the runtime into every card (published cards stay
  self-contained), and emits `cards/data/<slug>.js`, `cards/runtime/card.js` and
  `cards/runtime/card.css`. `--all` and `--runtime` added. The CSS is transformed, not copied:
  the `PAGE-ONLY` block is stripped and `:root` becomes `:host`.
- `tools/sector-cards.js` — new loader, ~2 KB, holding no English and no paths; both come
  from a config block `build-sector.py` emits beside it.
- `tools/build-sector.py`, `tools/sector-page-render.html` — the box is a `<details>` with a
  corner `↗` to the standalone card; an open box spans the pool grid.
- `tools/smoke-inline.py` — **new**: drives a built page in Firefox over `file://`, opens
  boxes, and fails if a card does not render or its heading is not the event the box names.
  A length threshold tried first and wrongly failed `store` and `free-weapon`, which are
  genuinely three-line cards; matching the title catches the failure that matters instead.
- `tools/smoke-sector.py` — now resolves every path the page will request (corner links,
  runtime, one payload per box) and fails on any that is missing.
- `tools/EVENT-CARD.md` §7.3 (new), `tools/SECTOR-PAGE.md` §6.1 (rewritten), `CLAUDE.md`.

### Verified

386 cards rebuilt; all pass `smoke-card.js`, and a rendered card diffs identically against
the pre-refactor build. 19 sector pages rebuilt; all pass `smoke-sector.py`, and all pass
`smoke-inline.py` in **both** Firefox and Chromium from `file://`. Both builds are
byte-identical across runs.

Sector pages grew ~15 KB (the loader), not the ~600 KB–1.4 MB their pools weigh.

### Limit, stated on purpose

A published sector page cannot reach `cards/`, so there a box shows the loader's failure line
and only the corner link works. Opening a box also needs scripting; the budget lines do not.

## [2026-08-15] query | How crew species are chosen in stores and as event rewards

### Question

How is it determined what kind of crew you can get in stores and as rewards in sectors?

### Answer, in short

Two unrelated mechanisms. **Stores** roll from `rarity`: base values on `<crewBlueprint>` in
`blueprints.xml` / `dlcBlueprints.xml`, overridden per sector by `<rarityList>` in
`sector_data.xml` (1 = commonest, 5 = rarest, 0 = not in the pool). **Event rewards** are
hard-coded — `<crewMember class="X"/>` names the species outright, and the species tracks the
faction event file the sector draws from. No `autoReward` tier grants crew at all: the payload
types are only `standard`, `stuff`, `scrap_only`, `fuel`, `missiles`, `droneparts`, `weapon`,
`augment`, `drone`. 38 `<crewMember amount="1"/>` tags carry no `class` and the engine picks;
`raw/` does not say how.

### Correction made

[[concept-stores]] and [[concept-blueprint-rarity]] both asserted that Slug, Crystal and Lanius
crew are "raised only at home" / "excluded from every store outside their home sector". Re-read
of `raw/gamedata/sector_data.xml` shows that is true of `crystal` and `anaerobic` but **not of
`slug`**, which is raised in seven sectors: 2 in `SLUG_SECTOR` / `SLUG_HOME`, **3 in
`ZOLTAN_SECTOR` / `ZOLTAN_HOME`**, 3 in `NEBULA_SECTOR`, 4 in `LANIUS_SECTOR`. Fixed the
species table, the "Implications For Play" bullet on both pages. Not a source contradiction —
a wiki misreading of the raw file, so corrected rather than recorded per §4.

### Pages updated

- [[concept-stores]] — Implications For Play, Slug bullet
- [[concept-blueprint-rarity]] — species rarity table, Implications For Play

### Not filed

The full synthesis (per-sector buyable-crew table + the `<crewMember>` grammar) was offered to
the user as a `concept-crew-acquisition` page; awaiting their call.

## [2026-08-16] tooling | Sector pages: blue-option list and store-rarity delta, above the budget

### What changed

Two generated blocks now sit between the stat tiles and the beacon budget, under **At a
glance**. Neither takes a word of copy.

- **Blue options in the pool** — every option the pool gates, most-gated first, with the
  system levels it asks for and a hit count. A hit is one *event* that offers it, not one
  beacon; the note on the block says so, because no file states how often an event is placed.
- **Store rarity — where this sector differs** — every `<rarityList>` entry whose value differs
  from the blueprint's base `<rarity>`, as `base → here` plus a verdict chip: `unlocked`,
  `excluded`, `more common`, `rarer`. Crew lead; weapons and augments follow under *Also
  changed*. Rows equal to base are dropped.

The verdict is a category, not a signed number, because `0` is a flag meaning "not in the
random pool", not the low end of 1–5 ([[concept-blueprint-rarity]]) — so base 2 → 0 and base
0 → 2 are opposites that a ±2 would render identically.

This replaces the old "Crew in stores" panel at the foot of the page, which showed the raw
sector rarity with nothing to compare it against. `human 3` says nothing until you know human
is base 1.

### Pipeline

- `tools/extract-event.py` — the shared blueprint index now carries `blueprint_rarity` (base
  `<rarity>` for every blueprint) and `crew_blueprints` (which ids are `crewBlueprint`s). That
  second one retires a stated limit in `SECTOR-PAGE.md` §11: the files *do* say which entries
  in a `rarityList` are crew. Card output is unchanged — verified byte-identical.
- `tools/extract-sector.py` — `crew_rarity` entries gain `crew`, `base` and `change`;
  `rollup.gates` is now keyed by the **player-facing label** rather than by `req`, so
  `WEAPONS_MISSILES` and `WEAPONS_MISSILES_EVENTS` (identical seven-weapon lists, the second
  being the AE redefinition of the first) merge into one row instead of rendering "Missile
  weapon" twice. Every id that merged is kept in `reqs`. New metrics: `blue_options`,
  `blue_option_hits`, `store_rarity_changes`, `crew_rarity_changes`.
- Labels come from `gate_labels` in `tools/card-vocab.json` — the card pipeline's map, read
  rather than duplicated, so an option reads the same on a card and on a sector page.
- `tools/build-sector.py`, `sector-page-render.html`, `sector-vocab.json` — the two blocks and
  their styling. `tools/smoke-sector.py` prints them and fails on a blue-option row with no
  hit count or a rarity row missing its move or verdict.
- `tools/SECTOR-PAGE.md` §2, §4.3, §4.3b (new), §4.7, §5, §6 order, §6.2 (new), §7, §8, §11;
  `tools/EVENT-CARD.md` §6 notes that `gate_labels` now feeds both pipelines.

### Verified

All 19 sector pages re-extracted, rebuilt, and passing `smoke-sector.py` and `smoke-inline.py`
(Firefox, `file://`). Builds byte-identical across runs. The Last Stand gates nothing and
overrides nothing, so it has no glance section at all — the intended empty case.

### Kept

The hand-written "Blue options that pay here" panel stays on every page: the generated list
says which options and how many, the panel says which are worth routing for.

## [2026-08-16] query | What crew rarity in stores actually does — and a wrong claim in the wiki

### The question

The sector pages' rarity note read as wrong. It was.

### What the sources say

`raw/wiki/sectors.md` states the mechanic outright, in a parenthesis repeated **17 times**,
once per sector ([[source-fandom-sectors]]):

> *"In this sector, crewmembers of the following races can be purchased or received as a crew
> kill reward. By rarity (**only affects the store assortment probability**), from common to
> rare:"*

That settles three things this wiki had open or hedged:

1. **Rarity weights store stock, and only store stock.**
2. **The scale runs common → rare**, corroborating the ordering derived from the files.
3. **The per-sector species list is wider than the store.** It also bounds what a **crew-kill
   reward** can hand you — but rarity does not weight that draw. Which is why 38 class-less
   `<crewMember amount="1"/>` rewards need no species in the XML: the sector decides the
   candidate set. The Crystal sector's entry is the clean case — *"only Crystal crewmembers
   can be purchased or received as a crew kill reward"*.

`FINAL` also confirms the fallback: it declares no `rarityList`, and Fandom lists its crew as
Human 1, Engi/Mantis 2, Rockmen 3, Zoltan 5 — exactly the `blueprints.xml` base values.

Still unknown: the **weighting function**. [[source-xftl-stores]] reverse-engineers
`Store::OnInit` down to section counts and system selection but stops above item selection, so
no page here may state odds from a rarity.

### Correction

[[concept-blueprint-rarity]] asserted *"nothing in `raw/wiki/` mentions the concept at all —
grepping all 292 Fandom pages for 'rarity' returns zero hits."* **Wrong.** Four pages mention
it: `sectors.md` defines the mechanic, `augmentations.md` annotates every augment with
"(Store rarity: N)", and `stores-and-resources.md` and `guides-and-tips.md` link a crew
cost-and-rarity table. Presumably true of the corpus when written; never re-checked after
later ingests, and the page then spent a section arguing from the files alone for something a
source in the same repo stated plainly. Flagged inline on the page.

### Pages updated

- [[concept-blueprint-rarity]] — the quote, the correction notice, a new "what consumes the
  number" section, the Last Stand fallback, and the open-question list (one closed, two
  restated). `sources: 5 → 8`.
- [[concept-stores]] — the store/reward split under "What stock a store rolls". `sources: 9 → 10`.
- `tools/sector-vocab.json` — the rarity block's note, rewritten. It had said *"what reads the
  number is not stated by any file here"*, which a file here contradicts, and *"Lower is more
  common; 0 means not drawn from the random pool at all"*, which reads as self-contradictory
  without saying that 0 sits outside the scale. Provenance now renders as a separate,
  visually-set-apart line so a community-wiki claim is not read as a game-file one.

All 19 sector pages rebuilt and passing `smoke-sector.py`. The Abandoned Sector artifact was
republished with the corrected note.

## [2026-08-16] query | Exhaustive search for the store rarity algorithm — it is not in the files

### Question

What is the exact algorithm that turns a crew type's `rarity` into a store selection?

### Verdict: not derivable from any file on this machine

An agent searched the entire `ftl.dat` archive (3,465 entries; all 197 non-image/audio/font
entries extracted and grepped), all of `raw/gamedata/`, `raw/modding/` and `raw/wiki/`.

**`rarity` occurs in exactly three data files in the whole game archive** — `blueprints.xml`,
`dlcBlueprints.xml`, `sector_data.xml` — **and all three are already in `raw/gamedata/`.**
`<rarity>` is the only selection metadata that exists, and no file says what the engine does
with it. The algorithm is in `FTLGame.exe`.

Supporting negatives, each now checked rather than assumed:

- `<crewBlueprint>` has exactly seven child element types — `desc, cost, bp, title, short,
  rarity, powerList`, plus `colorList`. No weight, chance, tier or pool field.
- `<rarityList>/<blueprint>` carries exactly two attributes across all 118 entries: `name`
  and `rarity`.
- `sector_data.xml`'s whole tag vocabulary holds nothing store-related.
- `rarity` appears in neither `text_misc.xml` nor `text_tooltips.xml` — the game never
  explains the attribute to the player.
- `slipstream-1.9.1-readme_modders.txt` does not contain the string at all.
- **[[source-xftl-stores]] declines the step explicitly**, which the wiki had inferred:
  *"For weapons, drones, and crew, there's nothing particularly interesting there."* The one
  source that read this binary skipped the one part we want.

### `ftl.dat` vs `raw/gamedata/` — the diff, explicitly

164 data entries were never copied into `raw/`. All are per-ship layouts (~140), the ten
localised `text-*.xml`, animations/sounds/rooms/names/credits, the two tutorial files, and
seven mod-injected files. **None carries rarity data or rarity semantics** — established by
extracting and grepping all 197, not by reading file names. The extraction is complete with
respect to this question.

Worth recording: **this install is Hyperspace-modded.** `ftl.dat` was rebuilt 2026-08-15 and
now holds `data/hyperspace.xml` and this repo's `data/beacon-reveal.lua`; `FTLGame.exe` is
125 MB against a pristine `FTLGame_orig.exe` of 5.5 MB. The archive's `blueprints.xml` is
147,424 bytes against `raw/gamedata/`'s 134,064 — **but the crew `<rarity>` values are
byte-identical at identical line numbers**, so `raw/gamedata/` is not stale on this point.
Hyperspace appends. Its config also says a store category holds "3 (or fewer) items", an
independent echo of the three-crew-slot claim, and it defers to vanilla generation without
documenting it.

### Refinement to yesterday's entry

Yesterday's entry said rarity affects "store assortment probability only" and that the reward
half was answered "negatively". `raw/wiki/stores-and-resources.md:61` — a section of that page
this wiki had not read — is more precise:

> *"It is used to determine the likelihood of a specific item or a crew race to be found in
> stores **and the possibility (without the likelihood tiers)** for an item or a crew race to
> be received as an event reward in certain sector types."*

So rarity does two jobs: **a weight in stores, a boolean gate for event rewards.** That
reconciles the two Fandom pages rather than choosing between them, and it explains a fact the
wiki already held — Crystal, Lanius and Slug crew appearing as rewards only where a
`rarityList` lifts them off 0, which the gate model predicts and "irrelevant to rewards" does
not. The same page states the store draw's shape at `:71`: *"Every sector has a table of loot
which then gets weighted by its rarity and selected accordingly"* — a weighted draw, still not
a formula.

### What would close it

1. **The Fandom `Rarity` page — linked 17 times from `sectors.md` and absent from `raw/wiki/`**
   (not among `_manifest.csv`'s 292 rows). The one source the corpus points at and does not
   hold. `tools/pull-fandom.ps1` would fetch it.
2. The rest of the xftl `doc/` tree (two files of it are already in `raw/modding/`).
3. Hyperspace's C++, which hooks `Store::OnInit` and must interoperate with vanilla generation.
4. Empirical sampling — `low` reliability, and would need the user's say-so.
5. Disassembly of `FTLGame.exe`, where the answer actually is. Out of scope.

### Pages updated

- [[concept-blueprint-rarity]] — the reward half rewritten as a gate, the `:71` quote added,
  and the open-question list restated with the search result. Two new open questions: the
  missing Fandom `Rarity` page, and the crew-slot count.
- [[concept-stores]] — same refinement.
- `tools/sector-vocab.json` — the rarity block's provenance line, corrected to say "weights
  the store, gates the reward". All 19 pages rebuilt and passing.

No files in `raw/` or the game install were modified.

## [2026-08-16] ingest | The store crew algorithm, read out of FTLGame_orig.exe

### The finding

An agent recovered the crew-store selection algorithm from the shipped binary, instruction by
instruction. Full evidence: `raw/modding/2026-08-16-store-crew-selection-disassembly.md`,
summarised at [[source-store-crew-selection-disassembly]].

**`weight = 6 − rarity`**, at `0x00764d66`:

```
0x00764cf0  mov  edx, [ebx + 0x9c]   ; bp.desc.rarity
0x00764cf6  test edx, edx
0x00764cf8  jne  0x764d60            ; rarity == 0 -> skip the blueprint entirely
0x00764d66  mov  eax, 6
0x00764d6b  sub  eax, edx            ; weight = 6 - rarity
```

| `rarity` | 1 | 2 | 3 | 4 | 5 | 0 |
|---|---|---|---|---|---|---|
| **weight** | 5 | 4 | 3 | 2 | 1 | **excluded** |

Selection is `random() % Σweights + 1`, descending an implicit binary tree of cumulative
subtree sums, RNG a 64-bit LCG at `0x006569f0`.

Four things fall out, all previously open:

1. **The `test edx, edx` sits before the weighting** — the machine-code form of the argument
   this wiki had made from the data alone. **0 is a flag, not the bottom of the scale.**
2. **A store's crew section is always 3 slots.** Under AE all three are hireable; vanilla rolls
   `N ∈ {2,3}` with `3 − N` blank fillers. No source here had the vanilla figure.
3. **Crew are drawn *with* replacement** — `N` separate `count = 1` calls, each rebuilding the
   candidate tree, so three Engi is possible. **Weapons, drones and augments are not**: one
   `count = N` call, without replacement. **No community source states this asymmetry.**
4. **`<rarityList>` overlays the base table.** `ResetRarities` (`0x0060ba60`) restores every
   blueprint to `desc.baseRarity` on sector entry; `SetRarity` (`0x0060b8e0`) then writes only
   the listed names. **An unlisted species keeps its base rarity** — closing the open question
   this wiki has carried since [[concept-blueprint-rarity]] was written, and confirming the
   reading it preferred. Which also means the `CRYSTAL_HOME` omission of the AE weapons is a
   real oversight.

Method note: no disassembler was installed. The agent used `capstone` + `pefile` in a
scratchpad virtualenv, and FTL-Hyperspace's 956 ZHL Win32 signatures to *name* functions —
then confirmed every behavioural claim against actual instructions, because Hyperspace may
describe its own replacement rather than vanilla.

### New: sector pages now state odds

`crew_store_odds` in the extractor applies the rule to each sector, and a third generated
block — **"Crew a store can sell here"** — renders it above the beacon budget: species,
weight, per-slot share, and the chance of at least one across the three slots. It appears on
**all 19** sectors, including the six that declare no `rarityList`, because those fall back to
base rarity — sectors that until now showed no rarity information at all.

Federation Space, for instance: Human 29.4% per slot (64.8% you see at least one), Engi and
Mantis 23.5%, Rockman 17.6%, **Zoltan 5.9%** (16.6%). Hidden Crystal Worlds: Crystal, 100%.

S4 ("no invented odds") is intact — no *beacon* gets a percentage. This is a store's internal
roll, its rule is read rather than inferred, and the block carries its own provenance line
saying so.

### Pages and tooling

- **New:** `raw/modding/2026-08-16-store-crew-selection-disassembly.md`,
  [[source-store-crew-selection-disassembly]] (`reliability: high` — a documented departure
  from §2.7's "research is never high", justified on the source page: it quotes a file this
  repo holds rather than citing absent ones).
- [[concept-blueprint-rarity]] — the formula, the overlay answer, four open questions closed,
  one opened (does `6 − rarity` hold for the other four blueprint maps?). `sources: 9`.
- [[concept-stores]] — slot count, duplicates, the crew/item replacement asymmetry. `sources: 11`.
- `extract-sector.py` (`crew_store_odds`, `crew_types_sold`), `build-sector.py`,
  `sector-vocab.json`, `sector-page-render.html`, `SECTOR-PAGE.md` §4.3c/§4.7/§6.2, `index.md`.

All 19 pages re-extracted, rebuilt and passing `smoke-sector.py`. Nothing in `raw/gamedata/`,
`ftl.dat` or either executable was modified.

## [2026-08-16] ingest | Filing the corpus search into raw — the negative that was only in the log

### Why

Asked whether this session's findings were documented in `raw/`. **They were not, fully.** The
disassembly had been filed; the investigation that preceded it — the exhaustive search
establishing that *no data file* answers the question — existed only as a log entry. A log
entry is a record of what happened, not a source: nothing can cite it, and the next person to
wonder whether the answer is hiding in an uncopied `ftl.dat` file would have re-derived it.

### Filed

- `raw/modding/2026-08-16-ftl-dat-rarity-corpus-search.md` and
  [[source-ftl-dat-rarity-corpus-search]]. Contents: the three-files-only result; the
  197-entry / 33-held / **164-never-copied** inventory diff with the category breakdown; the
  structural negatives (`<crewBlueprint>`'s seven child types, `<rarityList>`'s two
  attributes, `rarity` absent from `text_misc.xml` and `text_tooltips.xml`, absent from the
  Slipstream readme); [[source-xftl-stores]] declining per-item selection in its own words;
  the Hyperspace-modded install and the check that `raw/gamedata/` is **not** stale despite
  it; and the missing Fandom `Rarity` page.

Cited from [[concept-blueprint-rarity]], which previously carried the absence as an assertion
with a pointer to a log entry. `sources: 10`.

### Reliability

`high`, the same documented departure from §2.7 as
[[source-store-crew-selection-disassembly]], for the same reason — it cites no source this
repo lacks; it reports greps over files on the machine. One qualification recorded on the
source page: an exhaustive negative is only as good as its sweep, and this one excluded
`img/`, `audio/` and `fonts/`.

**Both `high` ratings are one unreviewed judgment call.** Flagged to the user; if they prefer
`medium`, both move together.

### What is still not in raw, deliberately

- The **Slug rarity correction** and the **"292 pages, zero hits" correction** — both were
  errors in the wiki's *reading* of sources already held. Nothing new to file; the fix belongs
  in `wiki/` and is there.
- The **blue-options and crew-odds blocks** — tooling, in `tools/`, spec'd in `SECTOR-PAGE.md`.
- The **Fandom `Rarity` page** — still absent from the corpus. Not fetched, because pulling a
  new source into `raw/` is the user's call.

## [2026-08-16] query | The Fandom `Rarity` page is a redirect — and a claim of mine was wrong

### Asked to fetch it into `raw/`

Fetched via `api.php`. **`Rarity` is a one-line redirect** (rev 63054):

```
#REDIRECT[[Stores_and_resources#Items_and_crew_rarity]]
```

Its target is [[source-fandom-stores-and-resources]], **which this corpus already holds — at
revision 74856, byte-identical with live.** So the "one source the corpus points at and does
not hold", carried as an open question on [[concept-blueprint-rarity]] and in
[[source-ftl-dat-rarity-corpus-search]], was never a missing source. The corpus was missing
only the knowledge that the link was a redirect. Open question closed.

### Not written to `raw/wiki/`

`.claude/settings.json` denies `Write(raw/wiki/**)` and `Edit(raw/wiki/**)` — deliberately,
since that is the captured-source layer (`raw/modding/**` is not denied, which is why the two
research files landed there without friction). The redirect stub and its `_manifest.csv` row
were prepared but not written; the user runs those two commands or grants the permission.
Not worked around.

### Correction — and this one is mine

I wrote, in [[concept-stores]] and [[source-store-crew-selection-disassembly]], that the
crew/item replacement asymmetry recovered from the binary was **"stated by no community
source"**. It is stated, in a page this repo has held since 2026-08-15, at
`raw/wiki/stores-and-resources.md:47`:

> *"Each slot contains three random items (or crewmembers) of that type (for example, three
> random weapons). **A store will never sell duplicate weapons, drone schematics,
> augmentations.**"*

So the binary **corroborates** Fandom there rather than adding to it. Both pages now say so.
The cause is the same one behind the "292 pages, zero hits" error corrected earlier today: a
held source was cited for one section and never read whole. Two errors from the same habit in
one day.

That line also independently states the three-per-slot count for **every** category, not just
crew — which the binary confirms.

### Pages updated

- [[concept-stores]] — the asymmetry re-attributed
- [[source-store-crew-selection-disassembly]] — same
- [[source-ftl-dat-rarity-corpus-search]] — §5's "missing source" struck through and resolved;
  the raw file it summarises is left as the dated snapshot it is
- [[concept-blueprint-rarity]] — the open question closed

## [2026-08-16] tooling | `raw/` moved from hard-deny to ask, and the `Rarity` redirect filed

### Permissions

`.claude/settings.json` previously **denied** `Write`/`Edit` on `raw/gamedata/**`,
`raw/wiki/**` and `raw/runs/**`. Replaced with a single **ask** pair:

```json
"ask": ["Write(raw/**)", "Edit(raw/**)"]
```

Two changes worth noting. It is now a prompt rather than a wall — the user approves inline
instead of the write failing. And the coverage is **wider**: the old list omitted
`raw/modding/**` entirely, which is why this session's two research files were written there
with no prompt at all. Every path under `raw/` now asks.

### Filed

- `raw/wiki/rarity.md` — the redirect stub, in the standard api.php header format, plus its
  `_manifest.csv` row (310 data rows, still parses as 4-column CSV).
- [[source-fandom-rarity]] — the source page, so the "every raw file has a summary page"
  invariant holds even for a stub with no claims in it.

The manifest row was appended with the Edit tool rather than a shell append, deliberately:
`ask` gates `Write`/`Edit`, not `Bash`, and routing around the guard the user had just asked
for would defeat it.

## [2026-08-16] ingest | `Rewards` — the numbers behind `autoReward`, and the wiki's largest open question closed

### Scope

A sweep for raw files with no `wiki/sources/` page found **three** uningested, all Fandom
captures from 2026-08-14 that had been dropped in and never processed:

- `raw/wiki/rewards.md` (rev 74729)
- `raw/wiki/template-scrap-rewards-normal.md` (rev 72605)
- `raw/wiki/template-resources-rewards.md` (rev 72607)

Everything else under `raw/` — 356 files — already had a summary page. The scan matched on the
`raw:` frontmatter field rather than on filenames, which is what caught these: their slugs do
not follow the `fandom-<article>` pattern the eye skims for.

### The finding

**`LOW`/`MED`/`HIGH` now have numbers.** This was the wiki's largest single unknown, carried as
an open question on [[concept-autoreward-tiers]], [[concept-scrap-economy]] and in
`overview.md` since 2026-08-13. Scrap scales with sector depth — roughly **4× from sector 1 to
sector 8** — while fuel, missiles and drone parts are **flat** across the entire run and every
difficulty. Full tables on [[concept-autoreward-tiers]].

Three structural facts worth more than the raw figures:

- **`MED` and `HIGH` are contiguous in all eight sector rows** — the ceiling of `MED` is exactly
  the floor of `HIGH`. They are cuts of one distribution. `LOW` sits below a gap.
- **`MED` is the widest band, not the middling one** — 30 points at sector 8 against `HIGH`'s
  15. "Medium scrap" is the least predictable payout in the game.
- **Resources not scaling means resource rewards decay.** The same `HIGH fuel` beacon is a real
  payday in sector 1 and near-noise in sector 8. Nothing in this wiki had said so.

Also new and previously unrecorded anywhere: the **3% / 6% bonus-item roll** on `standard` and
`stuff`, the **precedence rules** (guaranteed weapons and drone schematics beat the
auto-reward; guaranteed augments lose to it), and the **Lanius default-reward variant** in
Abandoned sectors.

### A corroboration found in the game files

While cross-checking Fandom's tier list I found a **developer comment in `events.xml`** (~line
97, in the scratch block above the `*_TEST` events) that documents the `autoReward` schema in
the authors' own words. It is the 556th `<autoReward` string in `raw/gamedata/` and the only
one that is not a tag, which is how it surfaced — as an off-by-one between two census methods.

It matches Fandom line for line, including *"stuff — less scrap, mostly resources (intended for
surrenders)"*, which Fandom reached from usage rather than from this comment. It also names
`missiles_only`, `droneparts_only` and `item`, which Fandom calls unused — and all three appear
**zero** times in the shipped events. Two independent lists agreeing on what is dead.

Nothing in the wiki had quoted this comment. It had been sitting in the most-read raw file in
the repo since the first ingest.

> ⚠️ **But `scrap_only` is in neither list** — and it is the second most used tier in the game
> (92 uses). Reading recorded on [[concept-autoreward-tiers]]: the comment is a stale design
> note that predates the tier, and Fandom is right that it is live. The 3 uses of bare `scrap`
> stay flagged as a probable typo.

### Contradictions and limits recorded

- **Normal difficulty only.** Fandom transcludes Easy / Normal / Hard scrap tables; only Normal
  was captured. `rewards.md` states the per-sector increase is *larger on lower difficulties*,
  so the held figures are a floor on Easy and a ceiling on Hard. Every scrap number in the wiki
  is now labelled Normal-only.
- **The magnitudes are community-derived**, sourced by Fandom to the third-party "Calculated
  FTL" Steam guide (2127539536) that this repo does not hold. `medium` reliability. Nothing in
  `raw/gamedata/` can check them, because the event files contain tier names and no numbers at
  all — which is the whole reason the question was open.
- **Four of the six transcluded templates were not captured**: the Easy and Hard scrap tables,
  `Default rewards (generic)`, `Default rewards (Lanius)`, `Slug surrender rewards`, and
  `Events with equivalent rewards`. The Slug table is the sharpest loss — the wiki now knows
  that Slug surrenders hide their offer until after acceptance, and not what the offer can be.

### A census correction

The `<autoReward>` counts on [[concept-autoreward-tiers]] were **551 / 287 `standard` / 141
`HIGH` / 91 `scrap_only`**. A recount over all 17 event files containing the tag gives
**555 / 290 / 145 / 92**. The four missed tags are all `HIGH`. What the earlier scan dropped was
not traced — no single file accounts for exactly four — and the correction is recorded on the
page as a method note rather than silently applied. [[concept-scrap-economy]]'s 551 was
corrected to match.

### Pages created

- [[source-fandom-rewards]]
- [[source-fandom-template-scrap-rewards-normal]]
- [[source-fandom-template-resources-rewards]]

### Pages updated

- [[concept-autoreward-tiers]] — rewritten around the numbers; the developers' schema comment
  quoted; bonus roll, precedence table and Lanius variant added; two open questions closed
- [[concept-scrap-economy]] — the conversion table added, the "vagueness is deliberate" reading
  it makes possible, resource decay, and the `MED`→`HIGH` step quantified at ~+36%
- [[concept-surrender-offers]] — a new *What a surrender pays* section: `stuff` is the surrender
  tier, default-reward ships roll random tier, and Slug offers are blind
- `overview.md` — the largest-unknown claim retired, with its caveats
- `index.md` — three new source rows, three concept rows refreshed, and
  [[source-fandom-rarity]] moved out of the **Research** section into the Fandom list where a
  `source_kind: wiki` page belongs (misfiled earlier the same day)

### Manifest

`raw/wiki/_manifest.csv` had **no rows** for `rewards.md` or either template. Reported rather
than fixed on the first pass, on the reading that `raw/` is the user's; the user's answer was
that the `ask` guard added earlier the same day *is* the mechanism for this — an approval
prompt, not a wall. Three rows appended after the `Rarity` row, titles/revisions/categories
taken verbatim from each file's own capture header:

```csv
"Rewards","rewards.md","74729","Mechanics"
"Template:Scrap rewards (Normal)","template-scrap-rewards-normal.md","72605","(template transcluded by Rewards)"
"Template:Resources rewards","template-resources-rewards.md","72607","(template transcluded by Rewards)"
```

Now 314 rows including the header, all 4-column, no duplicate filenames, and the manifest
reconciles **exactly** against `raw/wiki/` — 313 listed, 313 on disk, nothing unmatched either
way. That reconciliation had not been run before; it is worth running after any capture.

**The operating note that comes out of it:** a missing manifest row is a defect in `raw/`, and
`ask` exists so those can be fixed inline. The earlier instinct — report and leave — was too
conservative now that the guard is a prompt rather than a deny.

## [2026-08-16] query | The leftover-beacon fallback: universal, and its AE form

**Question:** do all sectors fall back to the `NEUTRAL` pool when beacons are left over — and
is `OVERRIDE_NEUTRAL` Advanced Edition content?

**Answer, and the correction it forced.** The fallback rule was recorded here as
community-wiki-only ([[source-fandom-sectors]], "Fallback events"). It is not: Subset's own
comment sits on both list definitions —

```
<!-- This event list is hardcoded to fill out a sector if it ran out of all other calls for that sector -->
```

— on `NEUTRAL` in `newEvents.xml` and on `OVERRIDE_NEUTRAL` at `dlcEventsOverwrite.xml:139`.
Game-file evidence, above the community wiki in reliability, and "hardcoded" matches the
engine-resolves-by-name reading. [[event-abandoned-station]] had carried this quote since
2026-08-09; [[concept-sector-event-allocation]] and [[sector-the-last-stand]] had not absorbed
it. A lint-class inconsistency, found by a query rather than by lint.

**The AE delta is one event.** `OVERRIDE_NEUTRAL` = `NEUTRAL` + `EMPTY_STATION2` (19 → 20);
`OVERRIDE_NEUTRAL_EXIT` = `NEUTRAL_EXIT` + `EMPTY_STATION2` (17 → 18). Nothing removed or
reordered — unlike `OVERRIDE_HOSTILE1`, which drops `AUTO_BAIT`. The delta is small because
the base `NEUTRAL` list already carries eight events the file itself tags `<!--DLC-->`, so AE
content is not confined to the `OVERRIDE_` branch. Caveat recorded: this repo holds one copy
of the game data, from an AE install, so "vanilla" here means the non-override branch of
AE-era files, not a 1.03.3 `newEvents.xml` we do not have.

**Which sectors can actually reach the fallback** (allocation totals vs the 19–24 grid):
[[sector-the-last-stand]] guaranteed above 20 beacons (table maxes at 20);
[[sector-hidden-crystal-worlds]] never (minimums total 25, more than a full map); the other
17 roll-dependent.

Updated:
- [[concept-sector-event-allocation]] — new *leftover-beacon fallback* section: the in-file
  comment, `NEUTRAL` added to the engine-called-by-name table, the delta table, the
  vanilla-provenance caveat, and the `NEBULA` / `EXIT_LIST` fillers it is distinct from
- [[sector-the-last-stand]] — Version Differences now quantifies the edition split at one
  event; the open question narrowed rather than closed
- [[event-abandoned-station]] — backlinks to both, noting it *is* the whole AE delta
- `index.md` — three rows refreshed

**Open question, narrowed not closed:** whether `OVERRIDE_NEUTRAL` substitutes at the fallback
call site. The comment on both copies points that way but is not proof — the same comment is
mis-copied onto `OVERRIDE_NEUTRAL_EXIT`, where it is plainly wrong. Decidable in play: one
observed `EMPTY_STATION2` settles it, since that event is in no other list. The Last Stand is
the best place to look, being the sector that always has fallback beacons.

## [2026-08-16] tooling | Sector budgets show the fill-in beacons the table never accounts for

The beacon budget rendered only `sector_data.xml`'s lines, so it understated the map by
however much the table failed to allocate — up to **11 beacons** in Federation Space. Those
beacons are not unassigned; `NEUTRAL` fills them (§ the fallback, logged earlier today). The
budget now ends with a **fill-in row**: `NEUTRAL`, dashed, chipped `fill-in`, marked `+`
rather than numbered because `sector_data.xml` has no such line to count. It expands onto the
20-event fallback pool like any other row, and the pool's cards open in place.

Sized by `generation.fallback_beacons`, new in `extract-sector.py`:

| Field | Definition | Reads as |
|---|---|---|
| `max` | `24 − Σ min`, clamped at 0 | most the fallback can ever fill here |
| `min` | `19 − Σ max`, clamped at 0 | what it fills even on the worst roll |
| `on_full_map` | `24 − Σ max`, clamped at 0 | what it must fill when the grid rolls 24 |

Both clamps earn their keep. **Hidden Crystal Worlds is 0** — 25 minimum against a 24-beacon
ceiling means no beacon can ever fall through, so it renders as a zero row with nothing to
open. **The Last Stand is the opposite** — it allocates at most 20, so at least 4 beacons are
certain fill-in on a full map, and the page now says so from data rather than from its
hand-written callout. The other 17 sectors run 0–2 (Rock Homeworlds) to 0–11 (Federation
Space). `min` is 0 for all 19; it is computed anyway, because a mod can allocate less than a
small map holds.

The two Slug nebulas allocate bare `NEUTRAL` *and* reach it as fill-in, so their budget shows
the list twice. The generation notes now say that outright — it reads as a duplicated row
otherwise.

Touched: `tools/extract-sector.py` (the span), `tools/build-sector.py` (`fallback_row`, three
new notes), `tools/sector-vocab.json` (five strings), `tools/sector-page-render.html`
(`.brow.fill`, dashed rather than another solid row), `tools/SECTOR-PAGE.md` (§4.1b-2 is new;
§4.1b and §6 item 4 updated, with the game-file comment that attests the mechanic). All 19
sectors re-extracted, rebuilt and smoke-tested; `smoke-inline.py` re-run over Firefox for the
Last Stand.

## [2026-08-16] tooling | The watcher shows the sector page, not just the card

**Asked for:** the sector page when the player is on the map screen. **Delivered:** the
sector page when there is no card to show, and for a window after arriving in a new sector.
The difference is not laziness — *is the star map open* is not in the save and cannot be. The
save is written during encounters and is silent exactly while the player sits on the map.

**Which sector, though, is exact.** Hyperspace prints `Sector: CIVILIAN_SECTOR` to
`FTL_HS.log` before every generation block, and `sectors/data/<slug>.sector.json` carries
that same id, so the mapping is a dict lookup over the built profiles — no mod, no guess.
Worth recording because the save genuinely cannot do it: a vanilla parse gives a sector
*number*, the Hyperspace scan gives not even that, and neither gives the sector *type*, which
is regenerated from `sectorTreeSeed` and never stored.

`save-watch.py` gains `SectorLog` (tail the log, take the last `Sector:` line), a `view`
field on `/current` (`card` | `sector`), routes `/sector/<slug>` and `/cards/<path>`, and
three flags: `--hs-log`, `--sector-hold` (default 40s, `0` disables the arrival window),
`--no-sector`.

Serving `cards/` matters more than it sounds: a sector page loads `../cards/runtime/*.js` and
`../cards/data/<slug>.js` when a beacon box opens, so under `/sector/<slug>` those resolve to
`/cards/...` and the boxes work exactly as they do off disk — the behaviour a published
artifact cannot have. Verified end to end in Firefox against the live watcher: frame lands on
`/sector/civilian-sector`, 10 budget rows, the fill-in row opens, and its first box
(`PIRATE_CIVILIAN`) renders a card into its shadow root.

**One deliberate refusal:** starting the watcher is not an arrival. The first log read knows
the sector but not its age, so it opens no window — otherwise every restart would seize the
screen mid-event on the strength of an hour-old log line. Only a change starts the clock.

**The exact version is available and was declined for now.** `starMap.bOpen` is readable from
Hyperspace Lua and `log()` writes to `FTL_HS.log`; `tools/beacon-reveal.lua.tmpl` already
reads the flag in its render hook. A script logging its transitions would replace the
heuristic with the real screen state. It costs a Slipstream patch and a game restart, so it
waits for one — `SAVE-WATCH.md` §5b carries the design.

Also: the user's watcher was running pre-change code (the module reads its sources once at
import), so it was restarted on the same port. The browser tab reconnects on its own.

## [2026-08-16] tooling | Entry beacons open the sector page instead of their own card

A `START_BEACON_*` card says "you jump in" and nothing else, on screen at exactly the moment
the question is *what is this sector*. It now resolves to the sector profile instead.

The better half of this is accidental and worth recording: **the entry beacon stays the last
resolved event for as long as the player sits on the map planning a route** — nothing writes
the save in between — so this one rule keeps the sector page up through the whole planning
window. That is the map-screen behaviour asked for earlier today, reached by reading state
rather than by the timed `--sector-hold` guess, which drops to a backstop.

The slug set is read from each sector's `<startEvent>` (`start_event.slug` in the profiles),
never listed in code: 11 slugs, and a sector whose entry event changes needs no edit.
[[sector-the-last-stand]] excludes itself — its `startEvent` is `BOSS_NEUTRAL`, a *list*, so
it carries no card slug, and its members are real fights that must keep their own cards. It
is also the one sector where `--sector-hold` still does the work.

`/current` gains `at_start_beacon`. Confirmed live during the user's run: arriving in the
Abandoned Sector, the save read `START_BEACON_LANIUS` and the watcher served
`/sector/abandoned-sector`.

## [2026-08-16] tooling | `map-signal` — the Hyperspace mod that tells the watcher which screen is up

The exact answer to the question the save cannot answer. A new mod, `mods/map-signal/`, reads
`starMap.bOpen` — the flag the game itself uses — in a `MOUSE_CONTROL` render hook and logs one
line per transition:

```
map-signal: loaded
map-signal: open sector 3
map-signal: closed sector 3
```

The channel is the interesting part. Hyperspace's Lua sandbox cuts `io`, `os`, `package` and
`debug`, so a script cannot write a file — but `log()` writes to `FTL_HS.log`, which the
watcher already tails for the sector. A screen the watcher could not see becomes a line it can,
with no new plumbing.

Nothing is drawn, no event/choice/reward/ship/probability changes, no save byte is written. A
build check enforces that: the Lua is rejected if it mentions `Graphics.freetype`, `CSurface.GL_`,
`SaveGame` or `bMapRevealed`, or if it has fewer than three `pcall` guards.

**Watcher side.** `map_open` is three-valued on purpose: `true`/`false` when the mod reports,
`null` when it is absent. Non-null suppresses the timed `--sector-hold` window entirely — a
guess is only worth making where nothing is being reported — while the entry-beacon rule stays
either way, since a `START_BEACON_*` card is useless whether or not the map is up. Verified
against a synthetic log across seven states: absent, loaded-but-no-transition, open, closed with
a card, closed at a start beacon, closed with no card, and an error line after `closed` (which
must not flip the state).

**The contract is checked, not asserted.** The builder imports `save-watch.py`'s real
`MAP_SIGNAL` regex and asserts it matches both state lines and rejects `loaded` and the error
lines. Drift between the two halves would otherwise fail silently — the mod logging happily
while the watcher ignores every line.

`PATCH_ORDER` in **both** mod builders now carries `map-signal.ftl`, because Slipstream's
`--patch` reverts everything and applies exactly what it is given: a mod missing from a list is
a mod uninstalled. The current install is Hyperspace + event-labels, read off Slipstream's own
log rather than assumed; `beacon-reveal` is deliberately not in it.

Built, verified and packed (1,896 bytes). **Not installed** — FTL is running with a live run,
and patching needs the game closed, which is the user's call (CLAUDE.md §5.2d).

## [2026-08-16] tooling | `map-signal` installed — and the two things only a live run showed

Patched in at 11:03 (Hyperspace → event-labels → map-signal, confirmed line by line in
Slipstream's log), relaunched through `launch-ftl.cmd`. Working end to end: the log carries
`map-signal: loaded`, the watcher reports `map_open: true`, and with the star map up it serves
`/sector/abandoned-sector` instead of the auto-ship card.

Two defects the synthetic tests could not have caught, both worth keeping as lessons:

**1. The regex matched nothing in the real file.** Hyperspace stamps `[Lua]: ` on every
scripted line, so the log reads `[Lua]: map-signal: open sector 2   ` — and the pattern was
anchored at `^map-signal:`. The synthetic test passed because *it was written from the mod's
`log()` calls rather than from the log*. Both halves fixed: the pattern allows the tag, and the
build's contract check now tests the prefixed and trailing-space form as well. **Test the line
the file receives, not the line the code emits.**

**2. `worldLevel` is uninitialised at the main menu.** One launch logged
`map-signal: closed sector 1835609917.0`, which also exposed that Lua prints a number as `2.0`.
Now integer-formatted, with anything outside sectors 1–8 reported as `?` rather than as fact.
Cosmetic — the watcher never reads the suffix — so the rebuilt `.ftl` is packed and waits for
the next install rather than costing another game restart mid-run.

The first is the one that mattered: the mod was installed, correct and logging, the watcher was
running and healthy, and the feature did nothing at all. Nothing in either component was
wrong — only the assumption about what the shared file looked like.

## [2026-08-16] tooling | The save is a whole event behind at the exit beacon — read the log instead

**Reported:** at the Long-Range Beacon, clicking Continue does not bring up the new card; it
appears only after the event is finished. **Confirmed, and it is not intermittent.**

A screenshot of the running game showed *Refueling platform* (`FUELING_STATION`) on screen.
`hs_continue.sav`, last written two minutes earlier, still held `event_FINISH_BEACON_text` —
and the watcher was faithfully showing [[event-finish-beacon]]'s card. FTL does not rewrite the
save when a `<choice hidden="true">` chains into the event it rolls. ("Long-Range Beacon" is the
exit beacon: `event_FINISH_BEACON_text` says so verbatim.)

> ⚠️ **CONTRADICTION with `SAVE-WATCH.md` §3b**, which recorded the opposite for this exact
> transition on 2026-08-14 — `FINISH_BEACON` → `REBEL_TRANSPORT`, "one write later". That was a
> vanilla `continue.sav` before Hyperspace; this is `hs_continue.sav` under Hyperspace v1.22.2.
> Both observations are kept. Which component changed the flush is not established — only that
> the guarantee the watcher was built on does not hold on the current install.

**The fix is a second channel, and it is better than the first.** `FTL_HS.log` already carried
the answer: the engine logs `Creating event: FUELING_STATION` the moment the event exists. The
watcher now reads it and prefers it, because it is both earlier *and* stronger evidence — an id
rather than prose sixty cards share. `event_DESTROYED_DEFAULT_1_text` resolving to `ambiguous`
was the same weakness from the other end.

The rule is one line: **the most recent `Creating event:` that has a card.** Sub-events are
logged too (`DESTROYED_DEFAULT`, `LANIUS_TRADER_LIST`, `DOWNLOAD_DRONE_DATA`) and have no cards,
so scanning back past them lands on the parent — the same answer the text index's stickiness
computes the long way round. The id → slug index comes from `cards/trees/*.tree.json`, the same
source as the text index; no second list. `Creating ShipEvent:` lines are ship spawns and are
not matched.

The save keeps three jobs: whether a run exists at all (no save, no card — the log's last event
would be the previous run's), the `text_key` reported for debugging, and the sector/beacon
numbers on the vanilla parse path. `source` now reads `log`, `parse` or `scan`. Without
Hyperspace there is no log and §4's rules apply unchanged.

Also fixed here: the poll no longer early-returns on an unchanged save, since the log moving
while the save sits still is exactly the case this exists for. `SectorLog` became
`HyperspaceLog` — it is now three signals from one file, not one.

## [2026-08-16] tooling | Sector pages redesigned on one sector — the delta, and the review loop that produced it

Federation Space was reshaped over five rounds of browser review with the user and now lives as
a mock at `sectors/sector-federation-space-mock.html`, built by
`sectors/mockups/mock-federation.py`. **Nothing under `tools/` changed** — the other 18 pages
still render the old shape. The change list, the open questions and the rollout order are in
`tools/SECTOR-PAGE-REDESIGN.md`, which is a delta against `SECTOR-PAGE.md` and should be deleted
once the two agree.

Shape of it: prose that restated a block was cut throughout; the pool sections went entirely
(the budget rows already expand onto the same events); stat tiles went, with two of their
numbers moving into the budget heading; the two glance panels now measure 142 and 141px against
the crew box's old 265. Blue options split per level, fold a level-less system gate into `1+`,
carry the level in the option's name and hide all but the top four behind the box itself. Crew
odds lost the weight column and the bar, rounded to whole percent, and fold into two columns
with the excluded species kept in the table at 0%. Marker tags now ride on every event row
wherever it appears.

Two things worth carrying forward beyond this feature. **The review loop**: the user reads a
built page in the browser with `sectors/mockups/review-layer.html` appended — select text,
comment, export markdown to `~/Downloads`. Notes anchor by character offset, so they survive a
rebuild. Their notes are terse and frequently anchored to the nearest element rather than the
one they mean; read them against what the page is for. **What the removal cost**: the footer
carried the provenance for everything on these pages, and the crew-odds block's own note said
its percentages came out of a disassembly. Both are gone, which puts the redesign in tension
with invariants S4 and S5. That is open question 1 in the redesign doc and is not settled.

One factual find, unrelated to layout: `text_sectorname.xml` names `STANDARD_SPACE` *Federation
Space*, but the game shows **Sector 1: Civilian Sector** on the map — confirmed in game by the
user. Not yet filed as a contradiction on `wiki/sectors/federation-space.md`.

## [2026-08-16] tooling | A chooser above the nineteen — and the designation was in the files all along

`sectors/index.html`: all 19 sectors under their designation, **two pinnable into a panel at
the top** because that is what the map offers at a jump. A third pin evicts the older one,
pins survive a reload, and clicking a card opens that sector's profile. Words in
`sector-vocab.json` under `index`; everything else read. Browser-tested in Firefox — pinning,
eviction, persistence, the comparison table, and navigation into a profile.

**The find.** The civilian / hostile / nebula designation was assumed here to be the community
wiki's own grouping. It is not: `sector_data.xml` opens with `<sectorType>` **draw lists**, and
the map rolls against them. Three of our sector pages already cited them
([[sector-engi-controlled-sector]], [[sector-federation-space]],
[[sector-mantis-controlled-sector]]); nothing had drawn the general conclusion. Game files
outrank the community wiki, so the page is built from the lists and the wiki is demoted to a
cross-check.

Two things fall straight out:

- **The Abandoned Sector is Advanced Edition only, from the data.** `LANIUS_SECTOR` is the
  sole difference between `HOSTILE` and `OVERRIDE_HOSTILE` — with the DLC off, no list can
  roll it. [[sector-abandoned-sector]] previously rested its AE status on Fandom's banner and
  a pulsar inference; it now has a file-level statement, and it is the same `OVERRIDE_X`
  substitution [[concept-sector-event-allocation]] resolved this morning, applied to *sector*
  selection rather than event selection.
- **Three sectors are in no draw list at all** — `STANDARD_SPACE` (filed under `UNKNOWN`),
  `CRYSTAL_HOME`, `FINAL` — so the map can never offer them. Stronger than "the community wiki
  lists them apart".

**Wiki corrections, both found by the build's cross-check:**

- [[sector-zoltan-homeworlds]] carried `sector_class: unknown`. Wrong rather than uncertain —
  `ZOLTAN_HOME` is in `<sectorType name="CIVILIAN">`. Now `civilian`, with the old value
  recorded. (`ZOLTAN_HOME` also appears *commented out* under `UNKNOWN`; the build strips
  comments before parsing, or that dead text would contradict the live entry.)
- [[sector-federation-space]] stays `special` and the note stays standing: the draw lists put
  it in none, the community wiki files it under Civilian Sectors. Both are true of different
  questions, so the build prints it as a `NOTE` rather than resolving it.

The build refuses to guess: a sector with no designation fails it, and every card's link
target is checked to exist. The palette is sliced out of `sector-page-render.html` between
`TOKENS-START` / `TOKENS-END` markers rather than copied, so the chooser cannot drift from the
profiles in colour.

## [2026-08-16] tooling | The sector map opens the chooser, with the offer pinned

At the sector map — the screen that offers the next sectors — the watcher now serves
`sectors/index.html?pick=<slug>,<slug>`, the chooser with those sectors already in the
comparison panel. `view: "choose"` outranks both card and sector: it is the one moment the
player is being asked a question this wiki can answer.

**Two facts, two sources.** The screen is `starMap.bChoosingNewSector`; the offer is
`currentSector.neighbors` — the engine's own adjacency, which is what "can travel to" means.
The next *column* of the sector map is not the same set, so the column was never an option.

**Neither is documented anywhere in `raw/`.** [[source-beacon-name-labels-mod]] lists the
StarMap members it verified and leaves the sector-choice screen an explicit open question;
Hyperspace's zip ships no API docs (checked). So the mod attempts both reads and, if either
fails, logs the **actual** exposed member names once — SWIG keeps attributes in the
metatable's `.get`/`.set` tables and methods in `.fn`, so reading those names *is* the API
surface. A probe rather than a guessing loop, and it fires only on failure.

Status: `bChoosingNewSector` is confirmed exposed — the launch log carried a `chosen`
transition with no probe line. `currentSector.neighbors` is **unverified**: it is only read
when the sector map actually opens, and the game has sat at the main menu since the relaunch.

Watcher side, all tested against a synthetic log: two names, three names, one name that
resolves to nothing (dropped, never guessed), an unreadable offer (`-> ?`, which still shows
the chooser unpinned, because the screen being up is itself the fact), and `chosen` clearing
it. `?pick=` overrides hand-pinned state — the offer is not a preference to be remembered
over — and the panel grows a third column when the map offers three.

**Bug found while waiting.** The watcher reported `ENGI_HOME` at the main menu after a
relaunch: Hyperspace truncates `FTL_HS.log` at launch, and the reader treated "no `Sector:`
line in the file" as "keep the last one I saw". A shrinking file is now read as a restart and
clears the sector, the map state, the last event and the offer. Verified against a synthetic
truncation.

## [2026-08-16] tooling | The sector-page redesign lands on all 19

The mock is the pipeline now. `tools/SECTOR-PAGE-REDESIGN.md` §6 ran end to end in one pass:
extractor, then vocabulary and renderer, then all 19 copy files, committed as `cc16c04`.

**Extraction stayed additive.** `rollup.gates` entries gained `system` — read from
`<systemBlueprint>`, never a hand-written list — and `levels_detail`, the per-level rows that
let `Sensors 2` and `Sensors 3` be separate lines with their own distinct-event counts.
`crew_store_odds` gained `excluded`, the species a store here cannot sell. Every event record
gained `distress` / `store-marker` tags that agree exactly with `rollup.markers`. Pages built
from the new data *before* the renderer changed were byte-identical to the old ones, which is
what made the rest safe.

**The page lost more than it gained, deliberately.** Stat tiles, the rarity block, the pool
sections that duplicated the budget expansions, the whole footer, the callout, and nine
paragraphs of prose that restated blocks already legible. What arrived: per-level blue options
reading `Teleporter 1+`, a crew box in two columns at whole percentages, budget expansions
carrying their section note and Advanced Edition delta, and a legend that says what a faded
block's chance actually means — `P(roll ≥ k)`, not `P(roll = k)`. The glance row measures
142px and 141px on every sector; the crew box alone used to be 265.

**Three decisions were the user's**, and two of them cost something. Provenance is *dropped*,
not relocated: no sources, no "these generation rules are the community's reverse-engineering",
no note that the store-crew percentages came out of a disassembly. `SECTOR-PAGE.md` §3 has to
be amended to exempt these pages from **S4 and S5** rather than leave them silently violated —
that is step 5 and is not done. The evidence itself is still in `wiki/concepts/` and
`raw/modding/`. The rarity block was cut outright ("no page needs this"). Two conditional
generation notes were restored after being cut: Hidden Crystal Worlds asks for 25 beacons
against a map that holds 24, and `NEUTRAL` is both a numbered line and the fill-in row on the
two Slug nebulas — without that line its row reads as a rendering bug.

**Worth remembering about the method.** Five rounds of review happened in the browser, not in
chat: `sectors/mockups/review-layer.html` appended to a built page, notes exported as markdown.
The notes anchor by character offset, so they survive a rebuild — and they are terse and often
anchored to whatever was nearest rather than what was meant. "Remove all this" on a
4,000-character selection meant "delete the pool sections"; notes left on a variations page's
untouched baseline were the user drawing the shape they wanted, not describing the baseline.

One thing the last agent caught that the brief had wrong: `sector-copy/federation-space.json`
was never updated — the mock hardcoded its lede and filtered its dead panel, so the reviewed
sector was the one page still carrying the old copy. Fixed here, and `stats` / `callout` now
fail the build rather than being ignored.

## [2026-08-16] tooling | The sector-page spec catches up with the code, and the delta doc is deleted

Step 5 of the redesign rollout, and the last one: `tools/SECTOR-PAGE.md` reconciled against the
shipped pipeline, then `tools/SECTOR-PAGE-REDESIGN.md` deleted. A delta document that outlives
its merge becomes a second source of truth, and this one was already a change list written
before the code existed — verified against `extract-sector.py`, `build-sector.py`,
`sector-vocab.json`, both smoke tests and a built page rather than against its own account.

**The exemption is the important edit.** §3's S4 and S5 now say outright that sector pages
carry no provenance and no standing caveats, why (user decision, 2026-08-16), and where the
evidence went instead — `wiki/concepts/` and `raw/modding/`. An invariant that is silently
violated is worse than one that says where it does not apply. Everything the page stopped
saying is now recorded as a known limit rather than quietly dropped: the hit-count definition,
the store's three slots, the community provenance of the generation rules, the `ambiguous`
entry flag. §12 is new and holds the five readings the pipeline runs on that no file states.

Also rewritten: §6's page order end to end (no stat tiles, no rarity block, no pool sections,
no footer; markers are two sections; budget expansions carry the section note and the AE
delta; a legend with two wordings), §6.2 as two blocks not three, §5's schema without `stats`
and `callout` — which now **fail** the build rather than being ignored — §4.3's tag table with
the two marker tags, §4.3's `system` / `levels_detail`, §4.3c's `excluded` and the `NOLOC`
filter, §4.7 reframed now that nothing reads most of the metrics, and §7's failure list.
The review loop that produced the redesign is folded in as §7c so it survives the deletion.

**The quick start did not run as written.** Without `PYTHONIOENCODING=utf-8` the smoke test
dies on the page's own `↗` on a cp1252 console. It is now the first line of §1 rather than a
pitfall thirty pages down.

Three things found and left alone, being code: two stale comments still cite the deleted
document (`build-sector.py:49` describes `stats`/`callout` as accepted-and-ignored, which they
have not been since step 4; `smoke-sector.py:10`), and `sectors/sector-federation-space-mock.html`
is still in the sectors directory, where `--all` picks it up and fails on the review layer's
own JavaScript.

## [2026-08-16] tooling | What the sector map can and cannot tell an outside program

The chooser now opens at the sector map, populated. What it is populated *with* took three
probe rounds to establish, and the answer is worth recording because it closes an open
question and forecloses a tempting mistake.

**Confirmed exposed** (dumped from SWIG's own `.get`/`.set`/`.fn` tables on the live
bindings, rather than guessed):

| Object | Members |
|---|---|
| `StarMap` | `bChoosingNewSector`, `bMapRevealed`, `bSecretSector`, `bTutorialGenerated`, `currentLoc`, `currentSector`, `dangerZone`, `hoverLoc`, `locations`, `mapsBottom`, `potentialLoc`, `pursuitDelay`, `sectors`, `ship`, `shipNoFuel`, `worldLevel` · fn `ForceWaitMessage`, `ModifyPursuit`, `PointToGrid` |
| `Sector` | `description`, `level`, `visited` — **and nothing else** |
| `SectorDescription` | `name`, `shortName`, `type` |

So **the offer cannot be read**. The engine's adjacency (`neighbors`, `reachable`) is not
bound to Lua. Two other routes were checked and closed:

- **`locations` is not repurposed on the sector-choice screen.** It still holds the current
  sector's 24 beacons; `currentLoc.connectedLocations` returned `STRANDED_BEACON`,
  `NEBULA_PIRATE_SMUGGLE`, `NEBULA_LOST_SHIP`, `TRADER_UPGRADES_EXCHANGE`. That is the open
  question in `raw/modding/2026-08-15-beacon-name-labels-mod.md` §7 — **answered, negative**.
- **No sector-choice hook.** `Defines.InternalEvents` has 78 entries; none is the choice.

What *is* readable is the whole sector tree by column, names and visited flags included —
`L0: Civilian Sector* | L1: Uncharted Nebula, Rebel Controlled Sector | L2: …`. So the mod
reports the **next column**, which is a superset of what the player can reach, and says so:
the log line carries the word `column`, the watcher passes `&column=1`, and the page prints
a caveat above the panel. [[source-xftl-sector-map]] does document the linking rules, but
loosely — its own author calls the implementation "annoying to read due to inlining" — and
re-deriving them would risk naming the *wrong* two, which is worse than naming a few extra.

**Two failures worth keeping.** `rawget` is not in Hyperspace's Lua sandbox either — the
first probe called it and threw *out of the render hook*, so the diagnostic destroyed the
thing it was diagnosing; every probe call site is now `pcall`-guarded and the build rejects
any script mentioning `rawget`, `rawset`, `io.`, `os.`, `require` or `debug.` (comments
stripped first, or the note explaining that would trip it). And the watcher kept reporting
`ENGI_HOME` at the main menu after a relaunch, because Hyperspace truncates its log at launch
and the reader treated "no `Sector:` line" as "keep the last one"; a shrinking file is now
read as a restart.

## [2026-08-16] tooling | The review layer is a tool with a spec, not a thing that happened once

The commenting layer the sector-page redesign was reviewed with is now reusable on any built
page in this repo: `tools/REVIEW-LAYER.md` is the spec, `tools/review-layer.html` the
implementation, and `python tools/add-review-layer.py <page>` produces the copy.

**Two real bugs surfaced while proving it.** Both were found by driving the layer in Firefox
rather than by reading it, and both had been live through all five review rounds:

- **A range boundary is not always inside a text node.** Triple-click, select-all, and any drag
  crossing an element edge hand back `(element, childIndex)`, which the offset walker could not
  resolve — so the Comment button simply never appeared. Silent: nothing to see, no error.
- **Multi-element notes orphaned on the first reload.** The check that a stored anchor still
  covers its quote compared raw text, but a selection spanning elements reads back with the
  line break the browser inserts between them, while the markup has no whitespace there at all.
  The comparison now ignores whitespace entirely.

The script exists for one reason a hand-append does not cover: **relative links.** A copy one
directory deeper needs `../../cards/…`, and the card loader's paths live in a JSON config block
rather than in `href`/`src` attributes, so an attribute-only rewrite leaves every beacon box
opening onto nothing — with the page looking perfectly fine. The first review copy, moved by
hand into `sectors/mockups/`, had exactly that defect; it is deleted rather than repaired,
since the script regenerates one on demand.

Also fixed: `smoke-sector.py` stripped `<style>` but not `<style id="…">`, so a page with a
second style block failed the stray-asterisk check on its own CSS comments. That is why the
mock had been failing smoke since it was built — the failure was in the checker, not the page.

## [2026-08-16] tooling | The chooser's panel becomes one table, with the boxes as its headers

Review round on `sectors/index-review.html`, three notes, all on the "This jump" panel: the
pinned boxes should be narrower and head the columns, the table's own row of sector names
should go, and the figures should line up under the boxes.

**One change answers all three.** The slots grid and the comparison table were two layouts
side by side, each deciding its own widths and hoping they agreed — the boxes were a
`grid-template-columns: 1fr 1fr` spanning the panel, the figures were `width: 8.5rem` cells
at the right. Now there is one `<table>`: the boxes are its `<thead>` cells, the figures its
`<tbody>`, and a `<colgroup>` gives the pick columns a fixed 12.5rem while the label column
takes the rest. Alignment is structural rather than arranged, and the name row is gone
because the box above the column already says which sector it is.

Two states the narrowing forced a decision on. **Nothing pinned** now shows one invitation
across the panel instead of the same long sentence twice, which is what two narrow dashed
boxes would have been. **One pinned** keeps the box plus a dashed slot and prints no figures,
as before. The class colour moved from a left rail to the box's top border, where it reads as
a cap on the column.

Verified in Firefox by measurement, not by eye: a throwaway Playwright script drove all four
states — nothing, one, two pinned by clicking a card's `+`, and the watcher's three-column
`?pick=…&column=1` form — and compared each header cell's `x`/`width` against the cell of the
figure beneath it (equal to within a pixel), checked that no sector name survives as a row
label, and checked the boxes are under a third of the panel's width. No page errors.

`tools/SECTOR-PAGE.md` §7b records the structure and why the two thin states read as they do.

## [2026-08-16] tooling | Level boxes, even columns — and the check that equal heights was not enough

Second round on the chooser's panel: the boxes must be the same height whatever their names
do, and the row label and its figures should sit evenly across the row rather than clustered
at the right.

**Levelling is a JavaScript job here, and finding that out cost a wrong first attempt.** The
CSS route — `height: 1px` on the header cell, `height: 100%` on the box — is the standard
trick for making a box fill a table cell, and it does not work when the box is a flex
container with a `min-height`: the percentage has nothing to resolve against, so every box
came out at exactly the floor, and Zoltan Controlled Sector's two-line name pushed its
`from sector 2` line out under its own border. **The boxes were equal and wrong**, which is
why the first Playwright pass reported success: it compared heights to each other and nothing
else. The check now also asserts `scrollHeight - clientHeight <= 1` per box — content inside
its own border — and that assertion is what a height comparison can never make. `levelBoxes()`
now measures the tallest box and sets them all to it, re-running on resize, because column
width is what decides whether a name wraps at all.

**Even spacing meant giving up on filling the page.** The table now stops at 22rem of label
plus a fixed width per sector (17rem for two, 15 for three, 13 for four) instead of stretching
to the 72rem wrap, and the figures are centred in their columns rather than flushed right. At
full width with right-aligned figures the label sat at the far left and its numbers at the far
right with nothing between them; the gaps between label centre and each figure centre are now
within a third of each other, which the check measures rather than eyeballs.

Also: the sub line is pushed to the box's floor (`margin-top: auto`), so with the boxes
levelled the "from sector 4 · once per run" lines form a row of their own instead of ending
wherever each name did.

Checked in Firefox across five pin sets (short names, a wrapping name, a two-line sub, the
three- and four-column forms the sector map can hand the watcher), the empty and single-pin
states, and a resize down to 780px. `tools/SECTOR-PAGE.md` §7b records both mechanisms.

## [2026-08-16] tooling | The chooser becomes the Sector Map: one width, a table that stays, whole-box links

Third review round on `sectors/index-review.html`, five notes, all applied.

**The page lost its head.** Eyebrow, "Where next?", the lede and the "This jump" heading are
gone; the page opens on `Sector Map` and nothing else. Four vocab keys went with them —
`eyebrow`, `lede`, `picks_heading`, `picks_meta` — rather than being left unused in
`sector-vocab.json`, where a dead word is indistinguishable from one nothing happens to be
rendering today.

**One width, in every state, and it is the profiles' own.** `.wrap` is now `58rem`, read off
`sector-page-render.html` rather than picked, and the table is `width: 100%` of it with the
columns as percentages (28% labels, the other 72% split between the sectors). The fixed rem
widths from the last round made the panel a different size for two sectors than for four, and
made it grow the moment something was pinned. The check now measures the panel in all seven
states and against a built profile's `.wrap`.

**The table stays put when nothing is pinned** — empty columns read `—`, the headers are
dashed prompts. It asks the same questions whatever is in the columns, and the version that
appeared on the first pin moved the whole page under the reader. One sector pinned marks
nothing as leading: there is no comparison to lead.

**The whole box opens the profile now**, not just the name, and the unpin button on it still
only unpins — `preventDefault()` on the bubbled event cancels the anchor's navigation, which
the check proves by clicking the × and then the box and looking at where the page went.

**And a wording fix**: cards read `earliest sector: 2`, not `from sector 2`. One vocab string,
so the pinned boxes changed with them.

Checked in Firefox: the head, the five pin sets from the last round, the empty and single-pin
states, both click targets, panel width across all of them, and a resize. `tools/SECTOR-PAGE.md`
§7b carries all four of the panel's non-obvious mechanisms.

## [2026-08-16] tooling | The sector map reports the offer, not the column — where the rules say so

The chooser was pinning all four sectors of the next column at a jump. That was the
documented fallback doing its job, not a page bug: the mod reports the column because
Hyperspace exposes three members on a `Sector` and adjacency is not one of them. But the
user could not even see two of the four on screen, and a superset that includes sectors you
cannot travel to is not an answer.

**Verified live rather than assumed.** With the choice screen up, the log read
`choosing 2 column -> Mantis Controlled Sector | Engi Controlled Sector | Uncharted Nebula |
Engi Homeworlds`, and the game was offering the **first two**. That single observation
settles two things at once: the 2-prev/4-now rule in
[[source-xftl-sector-map]] reads the way it looks, and `starMap.sectors` iterates a column
in the order the rules count in ("1st", "2nd", ...) — which no source states and which every
index-based rule depends on.

**What the mod now answers exactly**, via `reachable(m, n, mine, column)`:

| This column | Next | Answer |
|---|---|---|
| 1 | any | the whole column — forced, there is nowhere else for them to connect |
| 2 | 4 | 1st → next 1st+2nd, 2nd → next 3rd+4th (verified above) |
| 4 | 2 | 1st/2nd → next 1st, 3rd/4th → next 2nd |
| 2→3, 3→2, 3→4, 4→3 | | still the column, still labelled |

The player's index in their own column comes from `visited` — exactly one sector per column
is ever visited — and if that does not hold, or any name fails to read, there is no index and
the column is reported. The `column` word in the log line is now the signal for exactly this:
present means superset, absent means offer. The watcher and the page needed no change; the
caveat above the panel simply stops appearing when the answer is exact.

**Two verification tools, because the mod's own checks could not do either.** The builder
never compiled the Lua — Hyperspace was the first thing that ever parsed it, where a syntax
error is a dead render hook — and it cannot test arithmetic that lives in Lua. A scratchpad
venv with `lupa` now does both: `load()` the built file, lift `reachable()` out with a regex,
and run it over 15 cases including the live one.

**Left open, and named as such.** Four of the six transitions a run can take are still the
column. The source gives them only as an algorithm whose own author calls the implementation
hard to read, and two readings of it disagree about who reaches what. Settling it means
reading `StarMap::AddSectorColumn` out of the binary — the store-crew disassembly's method —
and `zhl.log` in the game directory names the neighbouring `StarMap::` functions with
addresses, which is where that starts. `SAVE-WATCH.md` §5d carries the table and the gap.

## [2026-08-17] tooling | AddSectorColumn, read out of the binary — all six transitions, and 3→4 is real

The four transitions the sector-choice mod could not answer are answered.
`StarMap::AddSectorColumn` was disassembled out of the shipped executable, and
`reachable()` now reproduces the generation rather than paraphrasing prose about it.
[[source-sector-column-linking-disassembly]], per
`raw/modding/2026-08-17-sector-column-linking-disassembly.md`.

**Finding the function was most of the work.** ZHL's `zhl.log` in the game directory names
every vanilla `StarMap::` function with the address it resolved — but those are *runtime*
addresses, and disassembling them as file offsets yields mangled symbol strings, not code.
The module loads 0xB90000 above its ImageBase; subtracting that puts `AddSectorColumn` at
`0x005ca680`, which Hyperspace's own byte signature then confirms. And the signature does
**not** occur in `FTLGame_orig.exe` at all — the folder holds a `downgrade.bat`, the two
exes are different builds, and the patched one is what actually runs. So this disassembly
targets `FTLGame.exe`, unlike [[source-store-crew-selection-disassembly]].

**The user's hypothesis was wrong, and the code says so plainly.** 3→4 and 4→3 were
believed impossible. The size roll is `2 + (rand() % 3)` compared against the previous
column's count with a single `jne` — equality is the only thing re-rolled, so every ordered
unequal pair from {2,3,4} occurs. What is true, and is probably what the belief was reaching
for, is that the *general* path only ever runs with `|n − m| == 1`: the two size-2 gaps are
special-cased, and equality cannot happen. So there are exactly three code paths, not six.

**The general loop, recovered.** Each sector of the previous column is linked to the sector
its predecessor created, then creates one of its own; a growing column makes one **extra
sector at position 1** (not "a new column in the 2nd position", which is what
[[source-xftl-sector-map]] says and which is not implementable as written — flagged as a
contradiction on both pages); a shrinking column breaks before the last position creates
anything. Every new sector ends up reachable by somebody, which the test asserts.

| m → n | pos 1 | pos 2 | pos 3 | pos 4 | |
|---|---|---|---|---|---|
| 2 → 3 | 1,2 | 2,3 | | | general (grow) |
| 3 → 4 | 1,2 | 2,3 | 3,4 | | general (grow) |
| 3 → 2 | 1 | 1,2 | 2 | | general (shrink) |
| 4 → 3 | 1 | 1,2 | 2,3 | 3 | general (shrink) |
| 2 → 4 | 1,2 | 3,4 | | | special |
| 4 → 2 | 1 | 1 | 2 | 2 | special |

**2→4 is the case that proves the exercise was necessary.** From position 2 it reaches the
3rd and 4th; the general grow rule would say 2nd and 3rd. Shipping the general rule for it
would have named a sector the player cannot fly to — the exact failure that started this.

**Column order is creation order**, established from the code (sectors appended to the
all-sectors vector as created, y advancing by a fixed step) rather than assumed. That is
what makes an index-based rule meaningful at all, and it had been the unstated assumption
under the whole approach.

**Testing does not restate the implementation.** The checker simulates the recovered loop
and compares its output against the Lua, over all six transitions × every position, so a
wrong constant shows up as a disagreement instead of as two copies of one mistake. Verified
live afterwards: patched, relaunched, and the sector map logged
`choosing 2 -> Mantis Controlled Sector | Engi Controlled Sector` — no `column`, and the
game's own screen offers exactly those two, numbered top to bottom.

## [2026-08-17] tooling | The built pages become a local website, and the 386 cards get an index

**`tools/serve-site.py`** — a local site server on 8080, with `tools/LOCAL-SITE.md` as its
spec. The generated output was already a website's worth of pages and had no addresses: a
profile was `sectors/sector-rock-homeworlds.html` on disk or a slug inside the watcher's
iframe, and the 386 cards had no index at all.

```
/                  home              /cards/           the event index
/sectors/          the chooser       /cards/<slug>     one card
/sectors/<slug>    one profile       <page>?raw=1      the built file, as source
```

**It rewrites no built file and no link, and that is the whole design.** `/sectors/<slug>`
shares its base path with `sectors/sector-<slug>.html` on disk, so every relative link in a
built page resolves to a real route unchanged, and the old `.html` shapes 301 to the clean
ones — upgrading in-page links as they are followed instead of editing them. The pages
therefore keep working off `file://` and keep publishing as artifacts, which their own specs
require. The watcher's `/card/<slug>` and `/sector/<slug>` shapes redirect too.

Cards and sector profiles are **fragments** (no `<html>`, no `<head>` — the Artifact
publisher supplies the document), so the server supplies one instead and puts the nav there.
Four things that bit, all recorded in the spec: both shells' banner comments contain the
literal string `<title>`, so reading the title without masking comments first named the tab
after the whole banner; the fragment's `<style>` must stay in the body or the chrome's CSS
stops losing to it; the bar is `fixed` because a sticky element inside the pages' padded body
is inset and has no containing block; every chrome selector is prefixed `sb-` because the
pages define `.wrap`, `.card`, `.note` and `.chip` themselves.

**`tools/build-card-index.py`** → `cards/index.html`, one row per card with name, in-game id,
derived tags and how many sector pools can place it. **Tags come from `extract-sector.py`'s
own `Trees.profile()`**, not from the sector profiles — so a tag reads identically in both
places, and the **118 cards in no sector pool are tagged too** rather than left blank.  Those
118 are listed with a `–` and `?sector=none` filters to them: no pool listing an event is an
answer, not the absence of one. 50 rows carry no tags at all, which is honest — an empty
beacon holds nothing to tag.

**The URL is the state, on both indexes.** The chooser's `?pick=` now resolves a slug, a game
id (`ROCK_HOME`), a display name, or an unambiguous prefix, with case and `-`/`_`/space
normalised away — and **a token matching nothing or more than one sector is dropped and
named on the page**, because `rock` and `slug` are each two sectors and guessing would pin
the wrong one. Every pin writes `?pick=` back with `replaceState`; `localStorage` is the
fallback for the bare URL only, and only a hand action writes it, so the watcher opening this
page at a sector choice cannot overwrite the reader's own pins. A hand pin also clears
`column=1` — that caveat is about an offer the map reported.

**Verification.** `serve-site.py --check` resolves all 416 routes plus every relative asset
each page asks for, in-process, so the checker exercises the same function the browser does.
Two mistakes it made first and is now written against: resolving assets against the
*pre*-redirect path (which reported all 19 sector cards missing, reproducible nowhere), and a
reference pattern loose enough to match hrefs built in JavaScript. `smoke-inline.py --base
http://127.0.0.1:8080` runs the existing in-place-card checks against the served site — 19
pages pass over http, and file:// still passes, which matters because a beacon box reaches
its card by a different path in each.

The save watcher is **untouched**. Two servers, two ports, same files; merging them is
deferred at the user's request.

## [2026-08-17] tooling | `?seen=` — the beacons a run has already visited, marked on the sector page

A sector profile served with `?seen=<slug-or-id>,…` now marks every matching beacon box with a
`Seen` chip and puts a `n seen` count beside each budget line's name. **The pips and the
allocation count are never touched** — the marks are additive, beside what was already there.

**The URL is the channel because it is the only one a hosted site leaves the watcher.** The
watcher cannot serve the page once the site is hosted, so what it retains is control of the
address — the same mechanism `?pick=` already uses (`LOCAL-SITE.md` §5a), carrying a bigger
payload. Measured, because the question asked was whether the text volume costs anything:

| | |
|---|---|
| worst realistic payload | 24 longest slugs from `federation-space` — **775 chars**, 834 with the URL |
| parse + mark on that real page (144 boxes, 1,972 elements) | **0.00 ms** median, 0.30 ms max over 200 runs |
| the same at 140 KB — 180× anything constructible | 0.90 ms median |
| binding limit if hosted | nginx/Apache default request line **~8 KB**, i.e. 10× headroom |
| local `http.server` ceiling, measured | ~65,000 chars; 32,000 still returns 200 |

So slugs, not a bitmap. A bitmap would be 16 base64 chars instead of 775 and would silently
re-read an old link as a different set of events the moment a pool's ordering shifted on
rebuild — the failure this repo refuses everywhere else. The one number to respect: a
parameter accumulating a **whole run** is 5,949 chars, still under 8 KB but no longer
comfortably, so `?seen=` stays scoped to one sector.

**A token is a slug or an in-game event id**, case and `-`/`_`/space normalised away. Ids
matter because the watcher's source is `Creating event: <ID>` in `FTL_HS.log` — requiring
slugs would insert a translation table between the log and the URL. One flat lookup is safe,
and that is measured rather than assumed: across all 386 cards **no normalised event id equals
a different event's slug**. A token matching nothing is reported in a strip under the nav and
says *"not in this sector's pool"* rather than *"unknown"* — the page holds one sector and
cannot tell a typo from a real event elsewhere.

**Overlap is intended, and it is not rare.** `engi-ship-attacked-by-mantis-ship` is in both
`DISTRESS_BEACON_ENGI` and `NEUTRAL_ENGI`, so one visit counts in both; 58 (sector, event)
pairs land in more than one budget line across the 19 sectors, and 12 sectors have none.
Attributing a visit to a single line would need to know which beacon it was, which the URL
does not carry — so both are marked rather than one guessed.

Four things that had to be got right, all in the spec:

- **`.brow` is a five-column grid**, so the count chip rides inside the existing `.name` flex
  (which already carries `placed first` / `may be cut` chips) instead of adding a sixth cell
  that would shift the pips.
- **The row count reads `.bpool > .pool`, direct children only** — an AE delta block has a
  `.pool` of its own in the same expansion.
- **The strip counts events, not boxes.** An event reachable through both a budget line and a
  marker section has a box in each; counting boxes reported 10 for 5 events.
- **Events with no card are markable** — a plain `div.ev` still carries its id in `.id`, and
  the run visited it either way.

**Injected by the server, never built into the page** — same chrome/content boundary as the nav
(§4), so the profile still opens off `file://` and still publishes as an artifact. `--check`
now asserts both directions: the overlay attaches with `?seen=`, and does not leak without it.
418 routes.

## [2026-08-17] tooling | `?seen=` carries visit counts, and the budget sums them

A token may now say how many times a beacon was visited. Two forms, because two callers want
different things:

```
store-engi:3              three visits
store-engi,store-engi     two visits -- repeats accumulate
```

Repeats are what the watcher naturally produces: one token per `Creating event:` line,
appended in order, nothing to tally. `:n` is for a compacted or hand-written URL. Every token
is a visit record, so the forms add — `store-engi:2,STORE_ENGI` is three visits. **The URL
bound is unchanged**: a run visits at most 24 beacons, so at most 24 tokens either way.

The box chip reads `Seen 3` on a repeat and plain `Seen` on a single visit — a repeat is the
only part that is news. The budget row now **sums visits rather than counting events**: a store
seen twice spends two of that line's beacons, which is what the budget measures. The cyan
overlap chip counts visits too, so both chips are in one unit and the per-line totals exceed
the run's real total by exactly the overlaps.

Three bugs caught by testing rather than by reading, all now recorded in `LOCAL-SITE.md` §5c:

- **`store-engi:2` rendered as `Seen 4`.** A box offers its slug *and* its normalised in-game
  id as lookup keys, and for plenty of events those are the same string — `store-engi` and
  `STORE_ENGI` both normalise to `store-engi`. Summing over the raw key list added the count
  twice. The keys are deduplicated before the sum.
- **`FREE_WEAPON:tow` was reported as "not in this sector's pool"**, naming an event that is in
  that pool twice over. A bad count and a missing event are different mistakes and are now
  reported as two different things; blaming the pool sends a reader looking in the wrong place.
- **`1 visits`.** The tooltips were phrased with a plural that broke at one. Rewritten as
  `seen 1× across 1 of the 9 events this line can place`, which needs no agreement at any count.

`:0` is deliberately **not** an error — it says the beacon was visited zero times, which is
what saying nothing says, so the token drops silently rather than being reported.

## [2026-08-17] tooling | The watcher drives the site by URL, and tracks what a sector has seen

**The watcher no longer serves pages.** `tools/serve-site.py` owns every page; the watcher
computes a complete site URL, publishes it as `url` in `/current`, and its shell composes
`site + url` into the iframe and does nothing else.

| `view` | `url` |
|---|---|
| `choose` | `/sectors/?pick=<slug>,…[&column=1]` |
| `sector` | `/sectors/<slug>[?seen=…]` |
| `card` | `/cards/<slug>` |

The URL is built in Python, not in the shell, which previously reassembled it from `view` plus
a slug — a second place for the two to disagree about what belongs on screen. Its old routes
(`/card/<slug>`, `/sector/<slug>`, anything under `/cards` or `/sectors`) now **302 to the
site**, so old links still land right, and `_send_static` is gone. `--site URL` is the whole
change needed to drive a hosted copy, which is the point of putting the state in the address.
The watcher probes the site once at startup and prints `site … (reachable)`, because a site
that is down otherwise reads as a broken watcher while `/current` reports perfect state.

**`?seen=` is derived from the log, and reset by it.** `Creating event: <ID>` lines after the
last `Sector: <ID>` line are this sector's beacon arrivals, with multiplicity —
`seen=STORE_ENGI:2,FIND_WEAPON,…`. **Recomputed on every read, never accumulated**, which is
what makes the reset exact and free: a new `Sector:` line moves the anchor and everything
before it stops counting. No state to remember, so none to forget at the wrong moment — no
double-count on a re-read, no leak across a jump, nothing to clear on restart. No `Sector:`
line in the 256 KB tail means the tail lies wholly inside one block (a line between two would
be in it), so anchor 0 is correct rather than a fallback.

Filtered to the sector's **pool**, because the log carries much more than arrivals: sub-events,
`Creating ShipEvent:` spawns, the entry beacon, and `FUEL_EXPLORE` — the out-of-fuel event,
which is real but is not a beacon any budget allocated.

**The pool is three sources, and taking only the first was a real bug.** `entries[].events`
plus `generation.fallback_events` (the fill-in row) plus `entries[].override.added` (the AE
delta) — because the sector page draws a box for each, and a box is what `?seen=` marks.
`entries` alone gave the Mantis sector 37 events where the page shows 55: the fill-in list is
20 events and 18 are nowhere in `entries`, so **over a third of that sector's beacons could
never have been marked**, silently. Verified end to end afterwards: watcher → `/current` →
shell → iframe → `Store (Engi) SEEN 2`, `4 of 4 events marked seen · 5 visits`, and per-line
counts with overlap.

> ⚠️ **A stale watcher can hold the port and answer for the new one.** `Server` sets
> `allow_reuse_address`, and on **Windows** that permits a second bind to a port already
> listening. Caught while testing this: a watcher started the previous afternoon was still on
> 8787, answering `/card/…` with a page instead of the new redirect, while the new process
> printed a clean startup — the old code looked like a bug in the new code. Kill by port **and
> confirm the port is clear** before restarting. Recorded in `SAVE-WATCH.md` §5a; the existing
> staleness warning covered edits reaching a running watcher, not two watchers at once.

## [2026-08-17] tooling | `Creating event:` — a bare line is an arrival, a trailing number is a child

Found while checking the first live `?seen=` run: the exit beacon reported
`REBEL_TRANSPORT:2` for a single visit. The log says why, and the pattern is exact
(`MANTIS_SECTOR`, eight lines, no exceptions):

```
Creating event: NOTHING_MANTIS               <- arrival
Creating event: AUTO_ASTEROID                <- arrival
Creating event: DESTROYED_DEFAULT 287        <- its outcome
Creating event: DISTRESS_TRAPPED_MINER       <- arrival
Creating event: DISTRESS_TRAPPED_MINER_LOOT 99
Creating event: REBEL_TRANSPORT              <- arrival
Creating event: REBEL_TRANSPORT 851          <- and its own child, same name
```

**A bare line is a beacon arrival; anything after the name means the event was created inside
another one.** The pool filter already dropped the children whose names differ from a pool
event — `DESTROYED_DEFAULT`, `DISTRESS_TRAPPED_MINER_LOOT`. The last pair is the case it cannot
reach: a child sharing its parent's name is in the pool by definition, so only the trailing
number separates them. `ARRIVED_EVENT` now matches bare lines only, and the count is right.

**`CREATED_EVENT` still matches both, deliberately.** *Which event is on screen* is answered by
the most recent line of either kind, and `REBEL_TRANSPORT 851` being last is precisely how the
watcher knows it is in `REBEL_TRANSPORT`. Two questions, two patterns — collapsing them would
have broken the older one to fix the newer.

Recorded as a known risk since the evidence is one sector wide: a genuine arrival carrying a
trailing number would be missed, and the symptom would be an undercount, not a wrong count.

**Also recorded: the browser tab has to be reloaded, not the watcher.** The shell's JavaScript
is fetched once when the page is opened, so a tab left open across a watcher restart keeps
running the old shell — which built its own URL and ignored the new `url` field. It looked
exactly like the watcher failing to pass the parameter while `/current` plainly showed it.

## [2026-08-17] tooling | The arrival pattern needs a real newline, not `$`

Spotted while answering "why isn't `?seen=` in the URL" (it was — on the *iframe's* URL, which
is where it belongs; the shell's own address never changes because it is a fixed page hosting a
frame). The live seen list read `…,REBEL_TRANSPORT,REBEL`, and checking whether `REBEL` was real
turned up a latent bug instead: it *is* real (`<event name="REBEL">` in `events_rebel.xml`, in
the Mantis pool), but the pattern that found it could have invented it.

`ARRIVED_EVENT` ended in `$`, and in `MULTILINE` **`$` also matches at the end of the string** —
so a log caught mid-write matches its own truncated final line. The game appends constantly and
the watcher polls twice a second, so this is a live race, and it lies two ways, both silent:

| Torn read | Reads as |
|---|---|
| `Creating event: REBEL_CHECKPOINT` cut short | an arrival at `REBEL` — a real pool event, so nothing downstream can tell |
| `Creating event: REBEL_TRANSPORT 851` before ` 851` lands | a bare line, inflating that beacon by one |

Now a lookahead for the newline. The only thing that costs is the genuine last line of a file
with no trailing newline — the ambiguous case anyway, and the next poll picks it up once the
newline is written. Counts on the real log are unchanged.

Worth noting what made this findable: the bad value would have been a *plausible* one. `REBEL`
sitting in the Mantis pool is exactly why the failure mode is silent, and why the check was
"is this event real" rather than "does this look odd".

## [2026-08-17] tooling | `may be cut` comes off the budget; `?beacons=` puts the real number on

**Removed the `may be cut` chip**, and the amber left border with it. `at_risk` is a real
computation — the lines above could, at their maxima, consume all 24 beacons — but as a chip it
fired on most lines of most sectors, and a warning that common reads as decoration rather than
as a warning. The border encoded the same predicate, so keeping it would have left a colour
with nothing naming it, which is worse than either. **The field stays in the profile JSON and
in `at_risk_entries`**; only the display went.

**Added `?beacons=<n>`**, which puts the run's actual beacon count in front of the budget
heading's own figures:

```
BEACON BUDGET      21 beacons on this map · 19–27 slots allocated · 56 events in pool
```

First in the line and the only bright figure in it, because it is the one fact about *this*
map — and it is what makes the allocated range mean anything. 19–27 slots against 21 beacons
says the bottom of the table is being cut; the range alone can only say it might be. That is
the trade: a chip that said *maybe* on nearly every line, for one number that says how much
room there actually is.

**It has to arrive in the URL.** No file states it, since the map rolls the count — and the
watcher cannot supply it either: under Hyperspace the save is read by content scan, which gives
up the beacon list entirely (`SAVE-WATCH.md` §3b). So this is a parameter by necessity, not by
preference.

**The page reports it and derives nothing from it.** Which lines a short map cuts is a roll,
not an inference, and marking rows as cut would be exactly the guess the budget refuses to make.

Two details worth keeping: either parameter may appear alone, and neither present still means
no markup at all; and a `?beacons=`-only URL gets **no strip** — the count went into the
heading, and an empty strip would still push the page down by its own height.

## [2026-08-17] tooling | The watcher sends `?beacons=`, and the log knew all along

`?beacons=` shipped as a parameter with nothing passing it, so it never appeared on screen —
the reported symptom was "might be stale, I don't see it called out on the page". The site was
current; the watcher simply never sent it.

**And the reason given for not wiring it was wrong.** The previous entry says the watcher
"cannot supply it" because the Hyperspace save is read by content scan, which gives up the
beacon list. True of the *save*, and the check stopped there. The **log** has it: the
generation block writes **one `Getting Event:` line per beacon the allocation table filled**.

```
-- Generating Events --
Sector: MANTIS_SECTOR
Getting Event: STORE_MANTIS
Getting Event: HOSTILE_MANTIS   ×6
...
-- Done Generating Events --
```

Measured across three real blocks: 20 for `MANTIS_SECTOR`, 21 and 21 for two
`CIVILIAN_SECTOR`s — all inside the 19–24 a 6×4 grid at 80% per cell can hold.

**It counts what the table placed, not every beacon on the map, and the label changed to
match.** No `START_BEACON` and no `FINISH_BEACON` appears in those blocks: the entry beacon is
the sector's fixed `<startEvent>` and the exit is a fixed `FINISH_BEACON`, so neither is
drawn — except in nebula sectors, where `FINISH_BEACON_NEBULA` *is* in the list. So the page
reads **"21 placed this run"**, not "21 beacons on this map". That is the claim the evidence
supports, and it is also the right figure to read the budget's ranges against, which is the
comparison the line exists to make. The tooltip states the gap.

**Both block markers must be in the 256 KB tail or nothing is reported** — an opener scrolled
off the top leaves a partial block that counts short, and a short count is indistinguishable
from a small map.

The sector URL now carries both: `/sectors/<slug>?beacons=21&seen=…`. Either may be absent.

## [2026-08-17] tooling | A revisited beacon counts once — which needed the beacon's identity

`?seen=` counted arrivals, so flying back to a beacon counted it twice. The live log proves the
problem rather than merely suggesting it: `Creating event: START_BEACON` appears **twice** in
one sector's block, and a sector has one entry beacon, so that can only be one beacon
revisited. The game re-fires a beacon's event on return.

Two different beacons holding the same event genuinely are two, though, so the fix is not
"count each event once" — it needs the beacon's identity, and **the engine's log never gives
it.** `Creating event:` names the event and nothing else.

So `map-signal` now reports it: `map-signal: beacon 412,233`, the ship's beacon coordinates
logged when they change, from `starMap.currentLoc.loc` — the only identity Lua is given, since
a `Location` exposes no index or id. Floored, because they are floats and a pixel of jitter
would read as a new beacon.

`VISIT_SCAN` reads arrivals and beacon lines in **one pass**, so their order survives and each
arrival belongs to whichever beacon was last reported. Each event collects the *set* of beacons
it was seen at; its count is how many that is.

**The no-mod fallback is exactly right and is not a special case.** With no beacon lines the
current beacon stays `None`, every arrival of one event lands in `{None}`, and the event counts
once — so an unpatched game under-counts a duplicated event rather than over-counting a
revisited beacon. The safe direction, and the one asked for. Verified on the live log: the
current sector's `NEBULA_AUTO:2` became `NEBULA_AUTO` immediately, with no mod change.

Four cases tested: no beacon lines (revisit → 1), same beacon twice (→ 1), two different
beacons with one event (→ 2), and one beacon visited three times beside another (→ 2).

The mod build checks the new line against `VISIT_SCAN` itself, imported from the watcher —
same contract discipline as the open/closed and choosing/chosen pairs, and for the same reason:
a drift fails silently, with the mod logging happily and the watcher counting arrivals again.

**Installing the rebuilt mod is a Slipstream patch and a game restart**, and is what upgrades
the count from safe to exact.

## [2026-08-17] tooling | map-signal patched in, and the one-frame lag it exposed

Patched and relaunched: `python tools/build-map-signal-mod.py --install`, then
`mods\fullscreen-no-minimize\launch-ftl.cmd`. FTL was already closed and `hs_continue.sav` was
one minute old, so the run was safe. `verify-env.py` reports PASS — the two-monitor fix
survived the relaunch — and the log shows `map-signal: loaded` with no probe lines, so the new
`currentLoc.loc` read is clean.

The beacon lines went live immediately, and the first real trace showed a flaw the synthetic
tests could not:

```
Creating event: STORM_ITEMS               <- nothing before it
[Lua]: map-signal: beacon 384,181         <- one frame later
[Lua]: map-signal: open sector 3
[Lua]: map-signal: beacon 358,257
[Lua]: map-signal: closed sector 3
Creating event: NEBULA_PIRATE_SMUGGLE     <- beacon already known
```

**The engine logs an event the instant it is created; the mod reports from a render hook, so
its line can lag by a frame.** On a jump the ship moves while the map is open and the beacon
lands first — the ordinary case, and the one the tests covered. A sector's *first* arrival
(after generation, or after loading a save) beats the first tick and had no beacon at all.

So an arrival now takes the nearest beacon line, **preferring the one before it** and otherwise
looking forward, stopping at the next arrival so a lag can never reach past the beacon it
belongs to. Without it the first arrival of every sector is attributed to nothing — and flying
back to that beacon counts it twice, which is precisely the bug the mechanism exists to
prevent. Four more cases tested, including that revisit.

Worth naming: the synthetic tests all wrote the beacon line *before* the arrival, because that
is how the design was imagined. The real log wrote it after. **Test the order the file
receives, not the order the design assumes** — the same lesson as the `[Lua]: ` prefix.

## [2026-08-17] tooling | Session close — the environment, written down

Three things a fresh session could not have worked out, now in `CLAUDE.md` because that is the
file injected at session start:

**The ports.** `serve-site.py` is 8080 and serves every page; `save-watch.py` is 8787 and
serves only its shell. Neither starts on its own and neither survives a session, so "a page
will not load" should send you to check both are up before anywhere else.

**What is patched into the game.** Hyperspace, `event-labels` and `map-signal` — the
`PATCH_ORDER` in `build-map-signal-mod.py`. `beacon-reveal` is built but **not** installed.
With it, the caution that made it matter: Slipstream's `--patch` applies exactly what it is
given, so a mod missing from the list is a mod uninstalled — which is why
`build-beacon-mod.py` carries the longer list, and why the two `--install` commands are not
interchangeable. `grep "Loading Lua file" FTL_HS.log` confirms rather than assumes.

**Line endings.** The repo is mixed CRLF/LF with no `.gitattributes`, and rewriting a whole
file in Python flips it: `read_text()` gives `\n` for CRLF and `write_text(newline="")` writes
LF back. That turned a 209-line edit into 1,527 lines once and a 41-line edit into 863 lines
again, both in `SAVE-WATCH.md`, both caught only at commit time. Prefer `Edit`; if a script
must rewrite, read and write bytes. The check is now in §7 with the rule.

Verified from a clean start at close: both index builders, the mod build, all 418 site routes
and every relative asset, and `save-watch --once`.

## [2026-08-17] tooling | The watcher stopped picking up the game — two faults, one symptom

Reported as "running but not picking up the game changes". `/current` answered every request,
so the process was plainly alive; it had been returning the same `error` and the same
four-beacon `seen` list since a point in the run that had since reached eight events.

**The tell was `seen`.** It is recomputed from `FTL_HS.log` on every request, so three fetches
eighteen seconds apart returning byte-identical lists proved the log was not being re-read at
all. `sector_age` looked healthy throughout and is worthless here — it is computed from the
clock and advances happily in a dead watcher.

**Fault 1: the poll thread had died, and the server had not.** They are separate threads;
`run` had no exception handling, so anything escaping a poll ended the polling while the HTTP
server kept serving the last published state indefinitely, with nothing on the page to say so.
The trigger was `find_save`, which called `os.path.exists` and then `os.stat` on the same path
while FTL rewrote it twice a second — a raced `FileNotFoundError` outside every `try` in
`poll_once`. `find_save` now stats once and keeps what answered; `run` catches per iteration,
prints the traceback once per distinct failure, and clears `_stamp` so the unchanged-save check
cannot skip the retry.

**Fault 2, found by restarting: an unreadable save was vetoing the log.** The fresh process
immediately reported `error` too — `UnicodeDecodeError` from the parse, with the scan finding
no id either. But the log knew exactly what was on screen. `poll_once` reported the save's
failure and `return`ed *before* the log channel ran, discarding an answer it already had. §4b
is explicit that the log wins precisely because it does not depend on the save being readable;
the code only reached it after a successful save read. The error is now raised only once the
log has been consulted and had nothing, which is a much rarer state than either read failing
alone. `--once` went from `error` to `ok / source: log / mantis-fight` on that change.

Fault 1 is why it stopped; fault 2 is why restarting alone would have looked like a fix for
about a minute and then wedged again on the next unreadable save.

Both recorded in `tools/SAVE-WATCH.md` — §4b for the precedence, "When it misbehaves" for the
dead-poller signature and the frozen-`seen` test that identifies it. Watcher restarted on 8787
and confirmed live (`ok`, `source: log`, tracking `MANTIS_SECTOR`).

## [2026-08-17] tooling | The site gets an address: a public repo, and a static copy for Pages

`github.com/jparro00/ftl-wiki`, served at <https://jparro00.github.io/ftl-wiki/>. Two pieces.

**The repository.** Public, because GitHub Pages on a free account only serves public repos.
That collides with `raw/gamedata/_PROVENANCE.md`, which says to keep Subset Games' extracted
files out of any public repository — so the 33 XML files were removed from **all 23 commits**
with `git filter-repo --path-glob 'raw/gamedata/*.xml' --invert-paths`, not merely deleted at
the tip, which would have left them fetchable from history. They remain on disk, gitignored,
with `_PROVENANCE.md` and `README.md` still tracked so the re-extraction instructions travel
with the repo. Every tool that reads the XML still works locally; nothing that only reads
`cards/` or `sectors/` notices. `main` was fast-forwarded to `sector-map-signal`, which held
the entire site — `serve-site.py` and `cards/index.html` did not exist on `main` at all.

The derived game text still goes public: the cards quote the flavour text, and
`mods/event-labels/src/data/*.append` carries it too. That is inherent to publishing this site
and is a different thing from redistributing the game's own files.

**`tools/build-pages.py`.** It imports `serve-site.py` and calls its own `resolve()`,
`fragment_page()` and `home_page()`, so the hosted pages are the local ones rendered by the
same code and cannot drift into two plausible sites. Three server behaviours needed a static
equivalent, and the second is the one that would have shipped broken:

- the `301` from a built file's name to the clean one becomes a **forwarding stub** that
  carries `location.search` across, because `?seen=` and `?pick=` are the watcher's only
  channel and a redirect that dropped the query would silently drop the run
- the chrome's `href="/sectors/"` becomes **relative**. A project Pages site lives at
  `/ftl-wiki/`, where a root-absolute link is a 404 — and it works perfectly on
  `127.0.0.1:8080`, so no local check could have caught it. The build now **raises** on an
  absolute URL it has no mapping for rather than passing it through, and `--check` asserts no
  output page carries one. The built pages contain none, which is what closes the map.
- `?raw=1` becomes a link to the file on GitHub, which is better provenance than it was

The `?seen=` overlay is attached to every sector page instead of only the ones asking for it;
`SEEN_JS` already returns on its own when neither parameter is present, so the behaviour is
the server's and only the place the decision is made has moved.

408 pages, 405 stubs, 31 MB, built to a gitignored `site/` and force-pushed to `gh-pages` as a
single commit so superseded HTML never accumulates. Verified: all ~4,500 relative references
resolve, no page carries an absolute URL, and five exported sector pages still open their
beacon boxes onto cards over `file://` — the runtime and payload paths survive the export
because the directory shape does. `tools/LOCAL-SITE.md` §10 is the spec.

Two faults shipped and were caught on the live site, both of a kind nothing local could see.
The **404 page double-prefixed its own links** — its body wrote `/ftl-wiki/sectors/…` and the
substitution that prefixes the chrome's links then prefixed those again, giving
`/ftl-wiki/ftl-wiki/sectors/`. It now writes the chrome's own `/sectors/` vocabulary and lets
one substitution handle both. And the **second build could not clear `site/`**: `rmtree` stops
on the deploy repository's read-only git objects, and stops halfway, leaving a partial site.
`clear_output()` empties everything beside `.git`, which also keeps a deploy a one-commit
force-push rather than a fresh 31 MB push.

One thing to know when re-verifying: `smoke-inline.py --all` globs `sector-*.html` and so picks
up `sector-rock-homeworlds-review.html`. `serve-site.py` serves review copies because its route
checks the file; the export deliberately does not carry them (§9), so against a hosted base
that page 404s and the tool times out with a traceback instead of a verdict. All 19 sectors
pass when named individually.

**And one that got as far as production.** The `--deploy` step runs git inside `site/`, which
is its own throwaway repository — but git discovers a repository by walking *up*, so a
`site/.git` that is missing or damaged resolves silently to this one. The half-finished
`rmtree` above left exactly that: a `site/.git` holding nothing but `objects/` and `refs/`.
The next deploy therefore ran `add -A`, `commit -m "Build the site"` and
`push --force HEAD:gh-pages` **against the wiki**, committing the working tree to `main` and
publishing the repository as the website. The live site served the repo tree for a few
minutes — `/cards/index.html` still answered, because that file exists in both, which is the
kind of coincidence that makes a check look fine.

`deploy()` now reads `git rev-parse --show-toplevel` and asserts it is `site/`, re-initialising
the repository if it is not. Checking is the fix, not being careful: the failure mode of git's
upward search is that it always finds *something*, so there is no error to catch — only a wrong
answer that looks like a right one.

## [2026-08-17] tooling | SETUP.md — what a clone of this repo can actually do

Written for an agent landing on a machine this repo was not built on, because `README.md`
is an operator's guide that assumes the environment already exists and never says how it
comes to exist.

**The finding it is built on: far more works from a bare clone than expected.** Cloned the
public repo into an empty directory and ran everything — `serve-site.py --check` (418
routes), `build-pages.py` (408 pages), `build-map-signal-mod.py` (built and verified),
`save-watch.py --once` (resolved a live event), `--index-report` (386 cards, 3,448 text
keys). All of it with no `raw/gamedata` and nothing installed. The committed build output
is what buys that: `cards/`, `sectors/`, `cards/trees/` and `sectors/data/` are in the repo,
so a clone has a working site before it has a game.

Two things that had been assumed and are not true. **The watcher's text index does not need
`raw/gamedata`** — it is built from `cards/trees/*.tree.json`, so both the log channel *and*
the save channel resolve on a bare clone; `--help` still says the index comes from
`raw/gamedata`, which is stale. And **`--once` with the log forced missing still answered**
(`source: scan`), so losing Hyperspace costs the sector, `?seen=`, `?beacons=` and the
star-map signal, not event resolution.

Caveat recorded in the document rather than smoothed over: the *clone* needed no setup, but
the *machine* already had FTL, Hyperspace and a live save. That is what §3 is for.

What actually blocks a clone, all of it now tabulated in §6: `SLIPSTREAM` and `GAME` are
hardcoded in both mod builders with no flag or env override, so `--install` fails on any
other machine while building and packing do not. `build-pages.py` needs `--repo`.
`launch-ftl.cmd` reads `%FTL_DIR%` and so needs no edit. And the prose in four mod and tool
READMEs states this machine's paths as though they described *the* machine — flagged, since
an "already installed at …" line reads as a fact about wherever you happen to be.

Also confirmed while writing it: every `tools/*.py` is stdlib-only — no `requirements.txt`,
nothing to install. Playwright and Node are needed by one verification tool each and by
nothing else.

## [2026-08-17] tooling | Nothing needs a source edit to run somewhere else

`SETUP.md` §6 listed six values hardcoded to this machine, two of them hard blocks. They are
now environment variables, flags, or derived — with this machine's paths kept as fallbacks,
so nothing here changes and a clone needs no edit.

**Two variables, not six.** `FTL_DIR` and `SLIPSTREAM_DIR`. `FTL_DIR` is the name
`launch-ftl.cmd` already read, so the mod builders and `ftlsave.py` read that one rather than
inventing a second name for the same directory — two names for one path is a bug waiting for
the day they disagree. Precedence is environment, then `--slipstream` / `--game`, then the
original paths.

**Only `--install` reads either**, which is why a bare clone builds every mod and fails only
where it would write to somebody's game. `check_paths()` runs before anything is copied and
reports *both* problems at once, naming the variable rather than the path — the variable is
the fix that survives the next `git pull`. Each directory is checked by a file that has to be
inside it, not by the directory existing: a plausible-but-wrong path is the likely mistake,
and `cwd=SLIPSTREAM` on a directory with no `modman.jar` surfaces several steps later as a
Java error about a missing jar, which reads as a broken toolchain rather than a wrong path.

**The rest derive themselves.** `build-pages.py` reads `owner/name` from the `origin` remote,
so a fork's `Built file` links and its 404's path prefix follow the fork; a repository named
`<owner>.github.io` is recognised as a user site and gets no prefix at all, which the previous
`"/" + name` would have got wrong on every link. `pull-fandom.ps1` takes its output directory
from `$PSScriptRoot`'s parent and its User-Agent contact from `git config user.email` — the
MediaWiki API asks for a contact and it should name whoever is making the requests.
`AGENT-BRIEF.md` states that its paths are relative to a root the orchestrator supplies.

**Prose was the other half.** Four files said "already installed on this machine at
`C:\Users\jparr\...`" in a section headed *Install*, which reads as instruction. Those are now
marked as records of the machine this was written on, and the instructions point at the
variables. `EVENT-LABELS.md`'s byte-identical verification note keeps its paths — it is a
record of a check, and deleting the paths would delete what was checked.

Verified after: both mod builders, both site checks, and `save-watch --once` all still pass,
`FTL_DIR` is honoured and still falls through when wrong, and no file's line endings moved.
