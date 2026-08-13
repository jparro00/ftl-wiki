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
