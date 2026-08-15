---
id: concept-event-tree-grammar
type: concept
version: both
first_seen: 2026-08-09
last_updated: 2026-08-13
sources: 10
related_events: [[[event-auto-ship-attacking-civilian]], [[event-single-life-form-on-moon]], [[event-crushed-pirate]], [[event-escape-pod]]]
tags: [schema, datamining, tooling, decision-tree]
---

# The event tree grammar — how every FTL event is shaped

## Definition & Context

Every event in the game files is the same recursive structure: **one node type, three
kinds of payload, and exactly one continuation.** Once that is named, an event stops
being prose to be summarised and becomes a tree that can be walked mechanically —
which is what `tools/extract-event.py` does to build the event cards.

An `<event>` element carries:

1. **Presentation** — `<text>` (inline, `id=` into the string table, or `load=` a
   `<textList>`), `<img>` / `<imageList>` — the art pools those resolve into are in
   [[source-events-imagelist]], and are the one presentation channel the cards ignore
2. **Effects** — a closed set of ~20 tags, listed below
3. **Continuation** — any of:
   - nothing → **terminal**
   - `<choice>` children → **decision node** (the player picks)
   - membership in an `<eventList>` → **chance node** (the game picks)
   - `<ship>` → **combat node**, whose `destroyed` / `deadCrew` / `surrender` / `escape` /
     `gotaway` children are themselves events

A `<ship>` with no `load` or `name` is not a fourth continuation but a **state change**:
`<ship hostile="true"/>` (96 uses) turns the ship already present hostile, and
`<ship hostile="false"/>` (31) stands it down. The outcomes stay on the parent event's
ship. `ZOLTAN_PEACE_QUEST2` uses both forms at once — a non-hostile `REBEL` at the beacon,
and an "Attack." choice that flips it.

A non-hostile `<ship>` on an event with choices is **scenery unless something flips it**:
the player picks from the menu, so those combat branches are only reachable if the arriving
ship is hostile or an option carries a bare `<ship hostile="true"/>`. `BROKEN_REBEL_DRONE`
parks a `REBEL_AUTO` at the beacon that nothing in the event ever activates — its fight
arrives instead from a *separate* hostile `REBEL_AUTO` loaded inside one choice's outcome.

> ⚠️ **These are not mutually exclusive.** `ROCK_UNLOCK1` carries a
> `<ship load="ROCK_UNLOCK2" hostile="false"/>` **and** three `<choice>` children: a ship
> sits at the beacon while the player still gets a menu, and the ship's branches resolve
> only if combat starts. `ZOLTAN_PEACE_QUEST2` does the same with a hostile Rebel ship.
> Reading `<ship>` as *the* continuation silently drops the entire choice menu.

A fourth continuation is **deferred**: `<quest event="X"/>` does not resolve here at all.
It plants a marker on the sector map, and `X` fires when the player flies to that beacon,
possibly many jumps later. See Quest chains below.

`load=` is a subroutine call: `<event load="SAVE_CIVILIAN_LIST"/>` splices in a named
definition, which may live in a different file. That is the only cross-file mechanism,
and it is what makes single events span four or five source files.

**A decision node and a chance node are the same shape** — options, each pointing at a
child event. Only the selector differs: the player, or the RNG. This is why a rendered
event tree needs one row type, not two.

## How It Shows Up Across Sources

Counted across `raw/gamedata/events*.xml`, `newEvents.xml` and `dlcEvents*.xml`
([[source-events-xml]], [[source-newevents]], [[source-dlceventsoverwrite]]):

| Element | Count | Role |
|---|---|---|
| `<text>` | 3957 | presentation |
| `<event>` | 2953 | the node |
| `<choice>` | 1176 | decision branch |
| `<ship>` | 578 | combat |
| `<autoReward>` | 556 | effect |
| `<eventList>` | 298 | chance |
| `<item_modify>` / `<item>` | 194 / 269 | effect |
| `<destroyed>` / `<deadCrew>` | 137 / 127 | combat branches |
| `<crewMember>` | 120 | effect |
| `<damage>` | 96 | effect |
| `<status>` | 91 | effect |
| `<boarders>` | 57 | effect |
| `<quest>` | 43 | effect |
| `<escape>` / `<gotaway>` / `<surrender>` | 36 / 28 / 25 | combat branches |
| `<removeCrew>` (+ `<clone>`) | 32 (+32) | effect |
| `<modifyPursuit>` | 31 | effect |
| `<distressBeacon>` | 30 | flag |
| `<augment>` / `<weapon>` / `<upgrade>` / `<drone>` | 29 / 26 / 26 / 8 | effect |
| `<store>` | 26 | flag |
| `<reveal_map>` / `<fleet>` | 16 / 16 | effect |
| `<unlockShip>` | 12 | effect |
| `<secretSector>` / `<remove>` / `<repair>` | 2 / 2 / 1 | effect |

`<event>` takes only `name` (473), `load` (1016), `unique` (**216** — 194 `true`, 22 `false`),
`min` / `max` (37 each).
`<choice>` takes only gating attributes:

| Attribute | Count | Meaning |
|---|---|---|
| `hidden` | 797 | present on most choices; semantics not established by any source here |
| `req` | 225 | the blue-option requirement — see [[concept-blue-options]] |
| `lvl` | 90 | minimum system level for `req` |
| `max_group` | 46 | mutual exclusion between gated variants of one choice |
| `blue` | 17 | overrides blue rendering |
| `max_lvl` | 13 | upper bound on `req` |
| `min_level` | 2 | rare variant spelling |
| `hiiden` | 1 | typo in the shipped data; inert |

That is the entire language. There is no loop, no conditional beyond `req`, and no
arithmetic — an event is a finite tree, always.

### `autoReward` is a matrix, not a number

`<autoReward level="MED">standard</autoReward>` pairs a level with a tier. The observed
combinations, most common first: `MED standard` (131), `HIGH standard` (85),
`LOW standard` (56), `LOW scrap_only` (38), `MED scrap_only` (27), `HIGH scrap_only` (21),
`MED stuff` (19), `RANDOM stuff` (16), `LOW weapon` (16), `MED fuel` (15), `HIGH fuel` (13),
`MED weapon` (11), `RANDOM standard` (10), `LOW stuff` (9), `HIGH weapon` (8),
`MED fuel_only` (7), `LOW drone` (7), `HIGH stuff` (7), `MED drone` (6), `MEDIUM standard` (4).

The numeric scrap behind each pair is **not** in the event files — see Open Questions.

### Quest chains

43 `<quest>` tags across the event files point at 30-odd targets — some events
(`ZOLTAN_PEACE_QUEST2`), some lists (`HIDDEN_FEDERATION_BASE_LIST`,
`QUEST_CONSTRUCTIONYARD_LIST`). Three properties matter:

- **A stage can plant the next marker.** `MERCHANT_INVESTIGATE` →
  `MERCHANT_INVESTIGATE_DELIVER`; `ROCK_UNLOCK1` → `ROCK_UNLOCK2` → `ROCK_UNLOCK3`. Chains
  must be followed transitively, not one hop.
- **Several paths can plant the same marker.** `ROCK_UNLOCK1` hands out `ROCK_UNLOCK2` from
  two different choices, and `ROCK_UNLOCK3` from both `ROCK_UNLOCK1`'s `gotaway` branch and
  from `ROCK_UNLOCK2` — so the chain is a graph, and needs a visited set.
- **A marker is not an outcome.** It costs nothing and resolves nowhere near the beacon
  that granted it, which is why the wiki treats chains as `chain-*` pages rather than
  as branches of the triggering event.

## Where It Applies

- **Odds.** Chance nodes are `<eventList>` members. No entry in the shipped files carries
  a weight attribute, so every fraction the wiki quotes rests on the uniform-selection
  assumption in [[concept-event-list-weighting]]. Combat branches are different: `surrender`
  and `escape` carry a real `chance="0.5"` ([[concept-surrender-offers]]).
- **Blue options** are `req=` on a choice, nothing more ([[concept-blue-options]]).
- **Version differences** are `<!--DLC-->` comments attached to individual elements, not to
  whole events. An AE-only line can sit inside an otherwise vanilla outcome — which is why
  [[event-crushed-pirate]] costs 2 hull and a system in AE but only a reduced reward in
  vanilla.
- **Reachability is not marked on the branch, but it is derivable.** `<ship>` blocks define
  a `deadCrew` branch for every hull, including automated ships that carry nobody — as on
  [[event-auto-ship-attacking-civilian]] and [[event-deactivated-auto-ship]]. The event
  files say nothing, but the ship's blueprint does: `AUTO_BASIC` and `AUTO_ASSAULT` both
  declare `<crewCount amount="0" max="0"/>` ([[source-autoblueprints]]), so no crew can die
  aboard them and that branch cannot fire. The blueprint-list *name* (`SHIPS_AUTO`) is not
  the signal — `crewCount` on each member hull is.

## Implications For Play

- If an event has no `<choice>` children anywhere, nothing you do changes it.
- If a branch's only payload is `<autoReward>`, the outcome is scrap-shaped and the
  variance is in the tier, not in whether you profit.
- A `<removeCrew>` with a `<clone>` child is a **different event** with a Clone Bay
  installed — the file encodes that rescue directly, with no choice presented.
- `unique="true"` (**194** events) means the encounter cannot repeat; there is no grinding a
  good table.

  > ⚠️ **CONTRADICTION:** [[source-fandom-random-events]] scopes `unique="true"` to **one
  > sector**, not one run — *"Events that can occur only once per current sector (unique)"* —
  > and singles out ship-unlock events as the once-per-run exception. [[concept-stores]]
  > independently argues the per-sector reading from the multi-store sectors. Neither reading
  > is datamined; the files carry the flag without documenting its scope. Both sides and the
  > argument are at [[concept-event-uniqueness]].

  > **Count corrected (lint, 2026-08-13).** This page said 206 and the contradiction block
  > said 195; neither reproduces. A comment-stripped census of every `.xml` in
  > `raw/gamedata/` gives **242** `unique=` attributes in total, and they partition exactly:
  > 216 on `<event>` (194 `true` + 22 `false`), 5 on `<textList>` (all `false`), 21 on
  > `<sectorDescription>` (8 `true` + 13 `false`). 194 is therefore the event count and 216
  > the attribute count — the figures the two sentences above now carry. The earlier numbers'
  > derivations were never recorded, so they are corrected rather than reconciled.

## How This Wiki Uses It

`tools/extract-event.py` implements the grammar above: it indexes every `<event name>`,
`<eventList name>`, `<ship name>` and `<textList name>` across all event files plus the
`text_events.xml` string table, then resolves one event into `ftl-event-tree/1` JSON —
following `load=` across files, pulling ship branches from
`raw/gamedata/events_ships.xml` ([[source-events-ships]]), reading `<!--DLC-->` markers,
and guarding recursion. `tools/EVENT-CARD.md` documents the schema and the card pipeline
built on it.

The practical consequence: event cards are generated rather than transcribed, so a
flattened branch or a dropped nested choice is a bug in one script rather than a mistake
repeated per page.

## Related
- [[concept-event-cards]] — what the cards generated from this grammar promise

- [[concept-event-list-weighting]] — the assumption every chance-node fraction rests on
- [[concept-blue-options]] — the `req=` gate in detail
- [[concept-surrender-offers]] — the one place the files do publish odds
- [[concept-sector-event-allocation]] — how a root event gets chosen in the first place
- [[concept-event-uniqueness]] — what `unique="true"` scopes to, and the open disagreement
- [[concept-modding-and-the-append-convention]] — the same grammar from the mod author's
  side, and the `<FTL>` wrapper / last-one-wins rules the extractor implements
- [[event-auto-ship-attacking-civilian]], [[event-single-life-form-on-moon]],
  [[event-crushed-pirate]], [[event-escape-pod]] — the four events extracted so far

## Open Questions

- [ ] What does `hidden="true"` on a `<choice>` actually do? It is on 797 of 1176 choices,
      and no source in `raw/` explains it.
- [ ] What are the scrap values behind each `level` × tier pair of `autoReward`? Not in the
      event files; possibly not datamined at all.
- [ ] Are `<eventList>` entries selected uniformly? Nothing weights them.
- [ ] Does `blue="false"` suppress blue rendering while keeping the gate, or the reverse?
- [ ] Does a `<damage>` entry naming a system also cost hull? Open on
      [[event-single-life-form-on-moon]] too.

## Sources

- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-fandom-random-events]] (per `raw/wiki/random-events.md`) — the competing reading of
  `unique="true"`
- [[source-modding-research]] (per `raw/modding/2026-08-12-ftl-modding-research.md`) — the
  `<FTL>` wrapper and last-definition-wins override, from the modding side
