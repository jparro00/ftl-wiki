---
id: sector-the-last-stand
type: sector
sector_id: FINAL
sector_class: special
faction: [[[entity-rebels]]]
min_sector: 7
unique: true
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 13
tags: [endgame, flagship]
---

# The Last Stand

## Summary
The final sector. Its pool is entirely boss-specific — no ordinary event lists appear
at all — and it is one of only two sectors whose allocation table **cannot exhaust the
map**, so every line it declares is placed in full and the beacons left over are filled
from the galaxy-wide fallback list instead.

## Character & Hazards
`unique="true"`, `minSector="7"`. Every list is a `BOSS_*` list except a single store.
3 guaranteed repair stations, 6 guaranteed hostile beacons.
(per [[source-sector-data-xml]])

`minSector` is zero-indexed: the attribute reads 7, and the sector a player counts is
**8**. [[source-fandom-sectors]] states it outright — "This sector is always sector 8. As
the final sector, it can occur only once per game" — which confirms the offset the
generated sector pages apply.

Sector-specific behaviour, none of it expressible in `sector_data.xml`
(per [[source-fandom-sectors]], per raw/wiki/sectors.md):
- Arriving pays **10 hull repaired and 10 fuel**. This matches the files exactly:
  `LAST_STAND_START` carries `<damage amount="-10"/>` and `<item type="fuel" min="10"
  max="10"/>` ([[source-events-boss]]). No contradiction.
- The **Rebel Flagship** orbits a beacon on the map and jumps once every two jumps you
  make; the next beacon it will take is drawn with a dotted or solid line. Sharing a
  beacon with it starts the fight.
- The **Federation Base** spawns slightly right of centre. If the Flagship spends **3
  consecutive jumps** on the base you lose the run. The base can never be overtaken, is
  returned to Federation control if the Flagship is pushed off, and otherwise behaves as
  an empty beacon.
- You may **wait at a beacon even with fuel in the tank**. Waiting ticks every map action
  forward, and a fight entered after a wait starts with your FTL fully charged.
- The repair beacons give 15 hull, 22–44 scrap, 5 fuel, 4 missiles, 5 drone parts; each is
  single-use and **can be overtaken before you reach it**.

## Map Generation & Placement
The generation rules below come from the community's reverse-engineering of the map
generator, not from any game file — [[source-fandom-sectors]] for the process,
[[source-xftl-sector-map]] for the engine methods behind it. Treat them as
medium-reliability. See [[concept-sector-event-allocation]].

- **Beacons are laid out before any event is assigned.** A 6×4 grid, each cell 80% likely
  to hold a beacon, so **at most 24**. [[source-xftl-sector-map]] adds the guard that keeps
  the count from collapsing: once one cell is empty and empties reach 20% of the cells
  placed so far, the next cell is filled regardless. [[source-fandom-sectors]] states the
  resulting range as **19–24 beacons per sector**; the sector-page pipeline deliberately
  declines to infer a floor from the algorithm, so `sectors/sector-the-last-stand.html`
  claims only the ceiling.
- **The table is a queue.** Lines are filled in sector-definition order, each rolling its
  own min–max inclusive and completing before the next begins; when the beacons run out,
  generation stops and the remaining lines get nothing.
- **This sector is the exception.** Its allocation totals **17–20** against a 24-beacon
  ceiling, so the queue can never run dry: every line is placed in full every run, nothing
  is ever cut, and the placement order — load-bearing everywhere else — decides nothing
  here. The only other sector with this property is [[sector-federation-space]] (13–24,
  which fills a full map exactly).
- **The leftovers go to the shared `NEUTRAL` list** (`OVERRIDE_NEUTRAL` under AE), so on a
  full map at least four beacons carry ordinary galaxy events that appear nowhere in this
  sector's table ([[source-newevents]], [[source-dlceventsoverwrite]]). Independently
  confirmed for this sector: [[source-fandom-template-stores-additional-stores-from-events-by-sectors]]
  notes that The Last Stand has no sector-specific store-opening events, "however,
  [[event-pirate-briber]] can occur in these sectors" — and `PIRATE_BRIBER` sits in the
  `NEUTRAL`/`OVERRIDE_NEUTRAL` fallback and in no `BOSS_` list. [[event-the-mercenary]]
  (`MERCENARY`) is on the same fallback list.
- **No nebula line is allocated**, so the nebula-first pass that reorders every other
  sector's generation does nothing here.
- **No exit beacon exists.** [[source-fandom-beacons]]: "Sectors other than The Last Stand
  all contain an Exit Beacon." The shared `EXIT_LIST` therefore never runs in this sector,
  and the generic exit note on the generated sector page does not apply.
- **Where the set pieces land**, per [[source-xftl-sector-map]] (the only source that
  describes this at all): the Federation Base reuses the exit-beacon placement routine —
  X drawn from grid columns {2,3} on easy/normal and {3,4} on hard, with the path from your
  start beacon required to be 4 jumps on easy/normal and 5–6 on hard, retried up to 16
  times before the constraint is abandoned. The Flagship is placed after map generation
  completes, in one of the **two right-most columns**, with a Flagship→base path of **4–6
  jumps inclusive of both endpoints** — i.e. at minimum two beacons between them.

## Beacon Markers
`<distressBeacon/>` puts a distress marker on the map and `<store/>` marks a store; neither
set has to match the allocation entry of the same name ([[source-fandom-sectors]]).

- **One store marker**, from the `STORE` entry.
  [[source-fandom-template-stores-number-of-stores-by-sectors]] independently lists this
  sector as **1 guaranteed store**, matching `sector_data.xml`. Nothing in the pool can
  open a second; only the fallback list can ([[event-pirate-briber]]). Hull bought there is
  at its most expensive in the game — the price per hull point is set by the sector number
  ([[source-fandom-stores-and-resources]]) — which is what makes the three free repair
  stations the sector's real economy.
- **No distress marker is possible here.** No `DISTRESS_*` line is allocated, no event in
  the pool carries the tag, and none of the fallback `NEUTRAL` events carries it either —
  so the mismatch that inflates distress counts in other sectors cannot occur.
- **Repair stations are marked in their own right.** [[source-fandom-beacons]] documents a
  repair-station beacon type ("Federation Repair Station. Repairs hull and provides
  supplies.") and states there are 3 in this sector. That marker comes from neither
  `<distressBeacon/>` nor `<store/>`, so the generated sector page's markers section cannot
  show it — it is derived from those two tags only.

## Event Pool

| Event list | min | max | Resolves to |
|---|---|---|---|
| `STORE` | 1 | 1 | a store beacon |
| `BOSS_REPAIR_STATION` | 3 | 3 | [[event-repair-station-in-last-stand]] |
| `BOSS_HOSTILE` | 6 | 6 | [[event-fight-in-last-stand]] (listed 3× → always this event) |
| `BOSS_NEUTRAL` | 7 | 10 | five events: [[event-rebel-ship-attacking-civilians-in-last-stand]] (`BOSS_SCOUT_RESCUE`), [[event-rebel-fight-among-federation-and-rebel-fleets]] (`BOSS_FLEETS_BOTH_FIGHT`), [[event-empty-beacon-last-stand]] (`BOSS_FLEETS_FED`), [[event-rebel-ship-attacking-refueling-outpost]] (`SQUAT_REFUEL_STATION`), [[event-rebel-fight]] (`REBEL`) |

Plus, on a full map, at least four beacons from the shared `NEUTRAL` / `OVERRIDE_NEUTRAL`
fallback (see above).

> **Correction (2026-08-15).** This table previously listed `BOSS_NEUTRAL` as four events
> "1/5 each", and named `BOSS_FLEETS_REBEL` among them. Both were wrong.
> [[source-events-boss]] (per raw/gamedata/events_boss.xml) lists **five** entries in
> `BOSS_NEUTRAL` — `BOSS_SCOUT_RESCUE`, `BOSS_FLEETS_BOTH_FIGHT`, `BOSS_FLEETS_FED`,
> `SQUAT_REFUEL_STATION`, `REBEL`. `BOSS_FLEETS_REBEL`
> ([[event-rebel-fight-among-rebel-fleet]]) belongs to `BOSS_WARNING_NODE`, a different
> list. The **"1/5 each" odds were unsourced**: the shipped event lists carry no weights at
> all (see [[concept-event-list-weighting]]), so the correct value is `unknown` — a list of
> five entries is not evidence of a uniform draw.

Start beacon: `BOSS_NEUTRAL` — the XML comments it "STUPID, since it's starting you at the
'exit'" ([[source-sector-data-xml]]). Entry to the sector is [[event-last-stand-start]]
(+10 fuel, +10 hull).

Every allocation here is fixed except `BOSS_NEUTRAL` — the only sector in the game with
almost no randomness in its beacon mix. `BOSS_HOSTILE` lists `BOSS_SCOUT` three times, so
every hostile beacon here is the same encounter.

Note the name collision: the sector's own `BOSS_NEUTRAL` list and the engine's shared
`NEUTRAL` fallback share no events.

## The Rebel Fleet Here
The pursuit does not work the way it does anywhere else
([[source-fandom-sectors]], [[source-fandom-rebel-fleet]]; see
[[concept-rebel-fleet-advance]]):

- Instead of advancing en masse from the left, the fleet **overtakes random individual
  beacons each turn**, flagged with a flashing red outline. The Flagship additionally
  overtakes whatever beacon it occupies.
- An overtaken beacon **loses its event and its environmental hazard** and becomes a Rebel
  Elite Fighter fight, usually under an anti-ship battery. The reward for the kill is
  **1 fuel** (4 if you were out of fuel), so there is nothing to farm there — this applies
  to a repair station you were saving as much as to anything else.
- ASBs will never occur at exit beacons on Easy — moot in this sector, which has none.

> ⚠️ **CONTRADICTION — do fleet-delay effects mean anything here?** The pursuit modifiers
> catalogued in [[concept-rebel-fleet-advance]] (`modifyPursuit`, nebula jumps, Distraction
> Buoys, [[event-the-mercenary]]) are all described against a fleet that advances as a
> front. No source in this repo states what they do in a sector where the fleet takes
> scattered beacons instead, and `MERCENARY` can reach this sector through the fallback
> list. Recorded as unresolved rather than assumed either way.

## Quests
No `QUESTS*` line is allocated and no event in the pool plants a marker, which two sources
independently confirm is deliberate rather than an omission:

- [[source-fandom-beacons]]: a quest triggered too late is pushed into the next sector, but
  "if this happens in sector 7, the quest will be 'cancelled', because quests are not
  allowed in sector 8."
- [[source-fandom-sectors]] NOTE 1: "sector 8 cannot have any quests at all."

> ⚠️ **CONTRADICTION (partial) — the mechanism, not the outcome.** The two Fandom pages
> above describe a sector-8 prohibition. [[source-xftl-sector-map]] reads `StarMap::AddQuest`
> as never *delaying* a quest into the next sector "in sector 7 or later" — the same
> player-visible result (the quest is lost) reached by a different mechanism (it is never
> carried forward, rather than blocked on arrival). The engine account is the better bet;
> both are recorded. Filed identically on [[concept-quest-beacon-placement]].

Player-facing consequence either way: a quest marker earned late in sector 7 is wasted — the jumps spent
setting it up buy nothing.

## Chains That Run Through It
- The Flagship fight, in three phases: [[event-boss-text-1]] → [[event-boss-text-2]] →
  [[event-boss-text-3]], ending in [[event-boss-destroyed]] or [[event-boss-escaped]].
  See also [[event-federation-base]] and [[event-boss-automated]].
  _A `[[chain-the-flagship]]` page is still to be written._

## Factions & Ships
- [[entity-rebels]] — the Flagship
- [[entity-flagship]]

## Version Differences
The endgame is where Advanced Edition diverges most sharply. Per the `_DLC` blueprints in
`bosses.xml` ([[source-bosses]]):
- **Phase 1** gains **Hacking** (power 3) in AE.
- **Phase 3** gains **Mind Control** (power 3); max power rises 31 → 32.
- **Phase 2** is unchanged.
- All `_EASY_DLC` variants **lose the vanilla Easy-mode shield discount** (6 → 8 shield
  power), so Easy difficulty is harder in AE than in vanilla.

`dlcEventsOverwrite.xml` does not touch any `BOSS_*` list — the event pools themselves are
identical across editions; only the Flagship's loadout changes. The one edition-sensitive
part of this sector's generation is the fallback: `NEUTRAL` in vanilla,
`OVERRIDE_NEUTRAL` under AE ([[source-fandom-sectors]], [[source-dlceventsoverwrite]]).

## Strategy Notes
- Routing to reach all three repair stations before engaging a Flagship phase is the
  obvious play; the fleet taking beacons at random is what puts a clock on it.
  *(Opinion, derived from the allocation and the overtake rules; no source states it.)*
- Fandom's danger and routing commentary about sectors generally is unsourced opinion and
  is not carried here.

## Open Questions
- [ ] `blueprints.xml` defines unsuffixed `BOSS_1`/`BOSS_2`/`BOSS_3` carrying systems the
      `bosses.xml` difficulty variants lack (teleporter, sensors, drones). No file states
      which set the game actually loads.
- [ ] `BOSS_WARNING_NODE` is allocated by no `sectorDescription`. The marker it plausibly
      feeds is now described by a source — [[source-fandom-sectors]] documents beacons
      flagged for imminent Rebel takeover, and the XML comment on `BOSS_FLEETS_REBEL` reads
      "areas that the fleet took over (or will take over soon) have the /!\ symbol on the
      map" ([[source-events-boss]]) — but no file or source states that the engine loads
      `BOSS_WARNING_NODE` for it.
- [ ] Whether the AE `OVERRIDE_NEUTRAL` list actually substitutes for `NEUTRAL` in the
      engine. [[source-fandom-sectors]] says it does; the game files state no substitution
      mechanism ([[concept-sector-event-allocation]]).
- [ ] What the store here stocks in crew. `sector_data.xml` declares **no `rarityList`** for
      `FINAL`, yet [[source-fandom-sectors]] lists a full crew rarity spread for this sector
      (Human 1; Engi, Mantis 2; Rockmen 3; Zoltan 5) — identical to the Civilian sector's.
      Recorded as a discrepancy rather than a contradiction: the likeliest reading is an
      engine default that no file here documents. See [[concept-stores]].
- [ ] Whether pursuit-modifying effects do anything in this sector (see the contradiction
      above).

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-bosses]] (per raw/gamedata/bosses.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-sectors]] (per raw/wiki/sectors.md)
- [[source-fandom-beacons]] (per raw/wiki/beacons.md)
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md)
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md)
- [[source-fandom-template-stores-number-of-stores-by-sectors]] (per raw/wiki/template-stores-number-of-stores-by-sectors.md)
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]] (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md)
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt)

[[source-fandom-the-rebellion]] (per raw/wiki/the-rebellion.md) was reviewed for this pass
and contributes nothing to this sector: it is lore about the Rebel faction with no
mechanics, and is not counted above.
