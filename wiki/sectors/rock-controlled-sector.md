---
id: sector-rock-controlled-sector
type: sector
sector_id: ROCK_SECTOR
sector_class: hostile
faction: [[[entity-rock-men]]]
min_sector: 1
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 15
tags: [hostile, no-nebula, distress-heavy]
---

# Rock Controlled Sector

## Summary
Rock space: a repeatable red sector with two guaranteed stores, six to eight fights that
start with weapons live, and no nebula content at all. Its allocation table is unusually
**front-loaded** — stores, empty beacons, the distress line and the entire hostile line are
placed before anything else — while its deepest pool, `NEUTRAL_ROCK` at 7–8, is the last
line filled and therefore the one a full map starves. Grouped under *Hostile Sectors* on
the community wiki, and it can occur several times in a run.
([[source-sector-data-xml]], [[source-fandom-sectors]])

> ⚠️ **SUPERSEDED CLAIM (this page's own):** an earlier revision said Rock Controlled
> "carries the game's largest neutral allocation at 7–8 beacons". That is wrong.
> `CRYSTAL_HOME` allocates `NEUTRAL_CRYSTAL` **12–12**, and `NEBULA_SECTOR` allocates
> `NEBULA_NEUTRAL` **7–8** — a tie. 7–8 is the largest `NEUTRAL_*` allocation among the
> ordinary on-map sectors, nothing more. (per raw/gamedata/sector_data.xml,
> [[source-sector-data-xml]])

## Trigger & Where It Appears
- `minSector="1"`, `unique="false"` — repeatable, and not the first sector of a run
  ([[source-sector-data-xml]]). Fandom states only "can occur multiple times per game"
  ([[source-fandom-sectors]]).
- Start beacon: `START_BEACON_ROCK`. The exit beacon is **not** in the table — every sector
  draws it from the shared `EXIT_LIST` ([[source-fandom-sectors]]).
- Soundtrack `rock`, `wasteland`; dominant faction [[entity-rock-men]].

## Character & Hazards

**The map, before the table.** Beacons are laid out first and events assigned second. The
map is a 6×4 grid; each cell has an ~80% chance of holding a beacon, with a guard against
too many empty cells — so **at most 24 beacons**, and the floor is not stated by anything
in `raw/gamedata/` ([[source-xftl-sector-map]], [[source-fandom-sectors]]).

> ⚠️ **CONTRADICTION — how many beacons is a sector?** [[source-fandom-sectors]] opens by
> stating a sector holds "between 19 and 24 beacons", but the generation algorithm it cites
> on the same page yields only a ceiling of 24 with an unstated floor. Both come from the
> same xftl teardown ([[source-xftl-sector-map]]), which this repo holds as research, not as
> game data. Nothing in `raw/gamedata/` states a beacon count at all. **Bet:** 24 is a real
> ceiling; treat 19 as an unverified floor and never derive anything from it.

**No nebula content.** This sector allocates no `NEBULA_*` line, so no purple cloud graphics
are drawn over it and no beacon converts to a nebula. Consequences that matter to a run:
sensors work everywhere, no jump inside this sector halves the Rebel advance, and the exit
can never be a nebula-empty exit ([[source-fandom-sectors]],
[[source-fandom-environmental-hazards]], [[concept-nebula-mechanics]]). The pursuit therefore
advances at its full per-jump rate the whole way across —
64px per jump, against 32px from a nebula beacon in a normal sector
([[source-xftl-sector-map]], [[source-fandom-rebel-fleet]], [[concept-rebel-fleet-advance]]).

**Hazards come from events, not from the map.** Five of the eight events across
`HOSTILE_ROCK` and `BOARDERS_ROCK` place you in a hazard on arrival — three asteroid fields
([[event-rock-fight-in-asteroid-field]], [[event-rock-pirates-fight-in-asteroid-field]],
[[event-rock-fight-with-boarders-in-asteroid-field]]) and two red giants
([[event-rock-pirates-fight-near-sun]], [[event-boarders-rockmen-near-sun]]). Asteroid
fields and solar flares both impose permanent **IN DANGER** while you stay: no ship-menu
upgrades, no cargo-bay weapon swaps, no crew management until you leave. Shields up holds a
flare to 1–2 fires; shields down and it is 3–6 ([[source-fandom-environmental-hazards]],
[[concept-hazards]], [[concept-solar-flares]]).

**Stores.** Fixed at 2 — no roll — and Fandom's per-sector store table independently prints
2 guaranteed stores for Rock ([[source-fandom-template-stores-number-of-stores-by-sectors]]).
A commented-out generic `<event name="STORE" min="2" max="4"/>` sits in the definition and is
not an entry ([[source-sector-data-xml]]).

**Store rarity list.** Rockmen (1), Human (2), Zoltan (3); Engi, Mantis and Slug are rarity 0
and are not sold here. `BOMB_LOCK` — the [[item-crystal-lockdown-bomb]] — is rarity **4**
here, against 2 in [[sector-rock-homeworlds]] and 3 in [[sector-hidden-crystal-worlds]];
Fandom says the same in words ("high rarity (4)") ([[source-sector-data-xml]],
[[source-fandom-sectors]], [[concept-blueprint-rarity]]).

## Event Pool

The table is a **queue**, not a shopping list: lines are filled top to bottom, each rolling
its own count inclusive, and generation stops the moment the beacons run out
([[source-fandom-sectors]], [[source-xftl-sector-map]], [[concept-sector-event-allocation]]).

| # | Event list | min | max | Slots placed before it (min–max) |
|---|---|---|---|---|
| 1 | `STORE_ROCK` | 2 | 2 | 0–0 |
| 2 | `NOTHING_ROCK` | 2 | 3 | 2–2 |
| 3 | `DISTRESS_BEACON_ROCK` | 1 | 2 | 4–5 |
| 4 | `HOSTILE_ROCK` | 6 | 8 | 5–7 |
| 5 | `BOARDERS_ROCK` | 1 | 2 | 11–15 |
| 6 | `ITEMS` | 1 | 2 | 12–17 |
| 7 | `QUESTS_ROCK` | 0 | 1 | 13–19 |
| 8 | `NEUTRAL_ROCK` | 7 | 8 | 13–20 |

Start beacon: `START_BEACON_ROCK`. Totals: **20–28 allocated slots against at most 24
beacons** — an allocation, *not* a number of stops. (per raw/gamedata/sector_data.xml;
placement columns derived in `sectors/data/rock-controlled-sector.sector.json`)

### What the order means here
- **Nothing at the top can be squeezed out.** Stores, empties, distress and the whole
  hostile line are placed inside the first 15 slots at worst, well under the 24-beacon
  ceiling. The two stores and the 6–8 fights are effectively promises.
- **The shortfall lands on `NEUTRAL_ROCK`.** Up to 20 slots can precede it, and it asks for
  7–8. On a full map it is cut — and it is both the deepest pool (10 events) and the only
  one carrying a named item, [[item-damaged-stasis-pod]] at
  [[event-dense-asteroid-field-distress]]. The start of the Crystal route is the first thing
  this sector drops.
- **Quests are unreliable twice over**: `QUESTS_ROCK` is `min="0"` *and* second-to-last
  ([[concept-sector-event-allocation]] on `min="0"` entries).
- Fandom's printed beacon list for this sector — 2 stores, 2–3 empty, 1–2 distress, 6–8
  hostile, 1–2 boarders, 1–2 items, 0–1 quests, 7–8 neutral — matches the XML **line for
  line and in the same order**, even though the same page warns that its ordering does not
  generally reflect the file order ([[source-fandom-sectors]]).
- Beacons still empty after the last line are filled from the shared `NEUTRAL` list
  (`OVERRIDE_NEUTRAL` under AE) ([[source-fandom-sectors]]).

### Pools, in summary
50 distinct events across the eight lines; 8 that are combat at the root, 18 that can turn
into combat, 5 that can kill a crew member, 4 that put boarders aboard, 22 carrying at least
one blue option, 8 that can start a quest. (derived in
`sectors/data/rock-controlled-sector.sector.json` from [[source-events-rock]] and the event
trees; see [[concept-blue-options]], [[concept-crew-loss-risk]])

`DISTRESS_BEACON_ROCK` is the standout: 12 events for 1–2 beacons, holding **10 of the
sector's 22 blue-option events** and **4 of its 5 crew-killers**
([[event-giant-alien-spiders]], [[event-fire-on-research-station]],
[[event-unknown-disease-on-mining-colony]], [[event-single-life-form-on-moon]]; the fifth is
[[event-rock-live-mine]] in `NEUTRAL_ROCK`). Because that line sits **third**, the risk and
the reward both arrive early.

## Beacon Markers
What the map draws is the `<distressBeacon/>` tag, **not** the allocation entry
([[source-fandom-template-distress-events-by-sectors]], [[source-fandom-beacons]]).

- **11 events in this sector's pool can show a distress marker**, against a distress
  allocation of only 1–2. Fandom's distress-events table lists exactly 11 rows with a Rock
  column mark, and they are the same 11 the extractor derives from the tags — an exact
  cross-check between the community table and `raw/gamedata/`.
- **Marked but not from the distress line:** [[event-dense-asteroid-field-distress]]
  (`ASTEROID_DERELICT_SHIP`) is allocated from `NEUTRAL_ROCK` and carries the tag. Fandom
  uses this exact event to explain how a sector can show more distress beacons than its
  distress count — but its worked example is the Engi sector, where `NEUTRAL_ENGI` precedes
  the distress line. **In Rock Controlled the order is reversed**: `NEUTRAL_ROCK` is last, so
  the extra marker is the one most likely never to be placed.
- **Allocated from the distress line but unmarked:**
  [[event-pirate-ship-attacking-civilian-distress]] and
  [[event-rebel-ship-attacking-federation-loyalists]] carry no tag and show no marker.
  Fandom's `Random Events` page calls this class of mismatch a coding error and leaves the
  events out of its distress category ([[source-fandom-random-events]]).
- **Long-Ranged Scanners** ([[item-long-ranged-scanners]]) resolve a marked beacon only
  coarsely: of the 11, three report *"Possible ship detected"* —
  [[event-friendly-ship-out-of-fuel]], [[event-escort-civilians-ftl-haywire]],
  [[event-pirate-ship-distress-trap]] — and the other eight report a plain unvisited
  location. It never names the event
  ([[source-fandom-template-distress-events-by-sectors]]).
- **Store markers** come from four events: [[event-store-rock]] (the two fixed beacons),
  plus [[event-escort-civilians]], [[event-escort-civilians-ftl-haywire]] and
  [[event-settlement-mercenary-work]], which open a shop as an outcome. Distress and store
  markers are only visible within 1 jump ([[source-fandom-beacons]]).

> ⚠️ **CONTRADICTION — extra store events.** [[source-fandom-template-stores-additional-stores-from-events-by-sectors]]
> marks [[event-large-trade-station]] as a Rock store-opener, but `STORE_REBELSIDE` reaches
> this sector only through `OVERRIDE_ITEMS` in `dlcEventsOverwrite.xml`
> ([[source-dlceventsoverwrite]]), and whether the engine substitutes an `OVERRIDE_` list is
> unresolved ([[concept-sector-event-allocation]]). The same table marks
> [[event-pirate-briber]] grey for Rock, i.e. reachable only "as a filler or as an exit
> beacon event in any sector" — consistent with the `NEUTRAL` fallback and `EXIT_LIST`
> routes, neither of which appears in this sector's table. **Bet:** Fandom is describing AE
> with content on; under vanilla the Large trade station route is absent.

## Chains That Run Through It
- [[chain-crystal-cruiser-unlock]] — only its **first step** is here:
  [[event-dense-asteroid-field-distress]] hands out the [[item-damaged-stasis-pod]]. The
  wormhole itself (`ROCK_CRYSTAL_BEACON`) is a named beacon in
  [[sector-rock-homeworlds]] only.
- [[chain-rock-bride]] — starts at [[event-rock-bride]] in `QUESTS_ROCK`; the only
  Rock-specific quest starter here.
- [[chain-hidden-federation-base]] — three events can plant its marker:
  [[event-asteroid-belt-distress]], [[event-rebel-ship-attacking-federation-loyalists]]
  (both in the distress line) and [[event-encrypted-federation-signal]] in `QUESTS_ROCK`.
- [[chain-escort-civilians]], [[chain-settlement-mercenary-work]] and
  [[chain-capture-the-ship]] all have starters in the pool.

Quest markers are placed by a separate rule and can fail: a candidate beacon must be
unvisited, non-nebula, not the exit, not fleet-taken, not already a quest, **not a store,
not a distress beacon**, not your current beacon, and reachable before the Rebels take it.
Otherwise the quest is pushed to the next sector — and from sector 7 on it is simply lost
([[source-xftl-sector-map]], [[source-fandom-beacons]], [[concept-quest-beacon-placement]]).
In this sector that filter permanently excludes the two store beacons and every distress-
marked beacon on the map.

## Factions & Ships
- [[entity-rock-men]] — dominant faction; every event in `HOSTILE_ROCK` is a Rock ship.

## Strategy Notes
- The distress line is the sector's payload and it is placed early: 10 of 22 blue-option
  events and 4 of 5 crew-killers sit in 1–2 beacons that will exist. Knowing which of the 11
  marker-bearing events can appear is worth more here than in most sectors.
- Rock Plating ([[item-rock-plating]]) and a Rockman are the two keys that pay repeatedly:
  three gated events each ([[concept-blue-options]]), and Rockmen are rarity 1 here, i.e.
  the crew most likely to be on offer in a store or as a crew-kill reward
  ([[concept-blueprint-rarity]] — rarity governs assortment probability, not price).
- Nothing here slows the fleet by route choice, because there are no nebula beacons to jump
  to ([[concept-rebel-fleet-advance]]).
- _Opinion, unsourced by data:_ Fandom's own framing warns that the red/green/purple colour
  coding is a poor guide to danger and that sectors should be judged individually
  ([[source-fandom-sectors]]). Its danger and routing commentary carries no measurement.

## Open Questions
- [x] ~~Which events populate each list.~~ Resolved: all eight lines extracted, 50 distinct
      events, in `sectors/data/rock-controlled-sector.sector.json` (per
      [[source-events-rock]] and the shared lists in [[source-events-xml]]).
- [ ] Does `OVERRIDE_ITEMS` replace `ITEMS` here? It would add
      [[event-large-trade-station]] — a third store route
      ([[concept-sector-event-allocation]]).
- [ ] What is the actual **floor** on beacons per sector? Fandom says 19; the algorithm it
      cites states only a ceiling.
- [ ] Is `unique="true"` once per sector or once per run? 36 of the 50 events here are
      unique, so the answer changes how much of the pool one visit can consume
      ([[concept-event-uniqueness]]).
- [ ] Observation wanted: on a full 24-beacon map, how many `NEUTRAL_ROCK` beacons actually
      appear? The placement maths predicts a shortfall against its 7–8.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml) — the shared `ITEMS`, `QUESTS` members
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml) — `OVERRIDE_ITEMS`
- [[source-fandom-sectors]] (per raw/wiki/sectors.md) — placement order, fallback, exit list,
  beacon count, the sector's printed beacon table
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt) — grid layout,
  quest-marker filter, fleet advance in pixels
- [[source-fandom-beacons]] (per raw/wiki/beacons.md) — marker visibility, quest beacons
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md) — pursuit modifiers
- [[source-fandom-environmental-hazards]] (per raw/wiki/environmental-hazards.md) — asteroid,
  red giant, IN DANGER
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md)
- [[source-fandom-template-stores-number-of-stores-by-sectors]]
  (per raw/wiki/template-stores-number-of-stores-by-sectors.md) — 2 guaranteed stores
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]]
  (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md)
- [[source-fandom-template-distress-events-by-sectors]]
  (per raw/wiki/template-distress-events-by-sectors.md) — the 11 marked events and their LRS
  readings
- [[source-fandom-random-events]] (per raw/wiki/random-events.md) — untagged distress events
