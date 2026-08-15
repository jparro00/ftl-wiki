---
id: event-auto-ship-near-storage-station
type: event
event_name: AUTO_DEFENSE_ITEM
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: hostile
hostile: false
blue_options: [[[item-cloaking]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [rebel, auto-ship, unique, filler, blue-option, item-reward, optional-fight]
---

# Auto-ship near storage station — `AUTO_DEFENSE_ITEM`

## Summary
An optional auto-ship fight guarding a military storage cache. Winning — or sneaking past
with Cloaking — earns a roll on `DEFENSE_ITEM_LIST`, which can pay a drone schematic, a
weapon, or a bundle of resources. Cloaking is the interesting line: it is a *gamble*, not a
guarantee, and half the time it just starts the fight anyway.

## Trigger & Where It Appears
- Sectors: [[sector-civilian-sector]], [[sector-federation-space]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]],
  [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]].
- Event lists: `NEUTRAL_REBEL` ([[source-events-rebel]]), `NEUTRAL_ENGI`
  ([[source-events-engi]]), `NEUTRAL`, `NEUTRAL_EXIT`, `NEUTRAL_CIVILIAN`
  ([[source-newevents]]), plus the AE lists `OVERRIDE_NEUTRAL` and `OVERRIDE_NEUTRAL_EXIT`
  ([[source-dlceventsoverwrite]]). Its entry in the Zoltan pool is **commented out**
  (`events_zoltan.xml` line 75, [[source-events-zoltan]]).
- `NEUTRAL` / `NEUTRAL_EXIT` are the hardcoded filler lists, so this also appears as an
  exit/filler beacon ([[source-fandom-auto-ship-near-storage-station]] records
  `alsooccur=exitandfiller`).
- `unique="true"` — at most once per run.
- Long-range scanners show a ship ([[source-fandom-auto-ship-near-storage-station]]).

> ⚠️ **CONTRADICTION (reach):** [[source-fandom-auto-ship-near-storage-station]] lists
> Zoltan Controlled Sector and Zoltan Homeworlds among the locations. In the game files the
> Zoltan neutral-list entry for this event is commented out
> ([[source-events-zoltan]]). It can still reach Zoltan sectors via the generic
> `NEUTRAL` / `OVERRIDE_NEUTRAL` filler lists, so the wiki is not wrong about where it can
> show up — but the Zoltan-specific route it implies does not exist. Trusting the game
> files.

## Text
> An advanced Rebel automated ship remains stationed near a small Rebel space-station.
> Sensors indicate it's a storage vessel for military goods.

(`event_AUTO_DEFENSE_ITEM_text`, per [[source-text-events-xml]])

The event loads `<ship load="REBEL_AUTO_ITEM" hostile="false"/>` — present but passive
([[source-events-rebel]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the automated ship to get to the storage cache. | — | The ship turns hostile. Destroy it → *"You salvage what you can from the broken ship."* → `autoReward level="MED"` `scrap_only`, then a hidden *"Investigate the station"* choice → rolls `DEFENSE_ITEM_LIST`. | 100% |
| 2 | Avoid provoking the ship. | — | No text, no effect — nothing happens. | 100% |
| 3 | **(Cloaking)** Attempt to cloak and access the cache. | `req="cloaking"`, `hidden="true"` | Rolls the two-entry `AUTO_DEFENSE_ITEM_CLOAK` list: **(a)** *"The ship patrols wide around the area, successfully approaching the station while avoiding detection."* → straight to `DEFENSE_ITEM_LIST`, **no fight**; **(b)** *"Before you can get close enough to scan the station, the automated ship detects you and moves in to attack!"* → the ship turns hostile, resolving as choice 1. | unknown — two entries, no weights stated |

### The `REBEL_AUTO_ITEM` ship
`auto_blueprint="SHIPS_AUTO"`. Only a `destroyed` branch — **no surrender, no escape, no
`deadCrew`** ([[source-events-ships]]). Reward is `MED` `scrap_only`, then the hidden
station choice.

### `DEFENSE_ITEM_LIST` — the cache
Four entries, one drawn at random. The file states no weights, so odds are **unknown**
([[source-events-rebel]], [[source-text-events-xml]]):

| Entry | Text | Reward |
|---|---|---|
| 1 | *"The station was either abandoned or stripped clean… You find nothing useful."* | nothing |
| 2 | *"The station was apparently designed to outfit Rebel ships with Drone Systems. You find a functioning Schematic."* | `autoReward level="LOW"` **`drone`** |
| 3 | *"The station is a storage site for military grade weapons. You find one that can be easily attached to the ship."* | `autoReward level="LOW"` **`weapon`** |
| 4 | *"The station is a storage site for various resources. You salvage everything possible."* | `autoReward level="MED"` **`stuff`** |

Note the reward *types* differ per entry — `drone` and `weapon` are item drops, `stuff` is
a resource bundle. One entry in four pays nothing at all.

## Blue Options
- **[[item-cloaking]]** (`req="cloaking"`, no level) — the system alone is the gate. It
  offers a chance to reach the cache without a fight; it is a two-entry coin flip, and the
  failure branch is the same fight you would have taken anyway. The failure branch only
  sets `<ship hostile="true"/>`, so the `MED` `scrap_only` still comes from the ship's own
  `destroyed` block ([[source-events-ships]]) — nothing is forfeited. The blue option is
  therefore **strictly non-losing**: best case you skip the fight, worst case you are
  exactly where choice 1 would have put you.

> **AE note:** [[source-fandom-auto-ship-near-storage-station]] observes that the nebula
> variant of this event (`Auto-ship near storage station in nebula`) additionally offers
> Hacking and Improved Cloaking blue options that this version lacks.

## Rewards & Risks
- Reward: `MED` `scrap_only` for the kill (fight paths only), plus one `DEFENSE_ITEM_LIST`
  roll on every path that reaches the station — a drone, a weapon, a `MED` resource bundle,
  or nothing.
- Risk: an auto-ship fight — no crew, no boarding, no surrender, no escape.
- Choice 2 is mechanically free.

## Strategy Notes
- *(Opinion.)* Take the Cloaking option every time you have Cloaking: it cannot leave you
  worse off than choice 1. Without Cloaking, choice 1 is a normal filler-fight EV call —
  `MED` scrap plus a 3-in-4 chance of something from the cache.
- The `weapon`/`drone` drops are `LOW` level, so expect the low end of the item pool rather
  than a run-defining weapon.

## Related
- [[event-auto-ship-near-sensor-station]] — sibling, map reveal, Sensors/Teleporter gates
- [[event-auto-ship-near-radar-station]] — sibling, fleet delay, Combat Drone gate
- [[item-cloaking]]
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Split between the two `AUTO_DEFENSE_ITEM_CLOAK` entries — no weights in the file.
- [ ] Weights inside `DEFENSE_ITEM_LIST` — four entries, no `prop`.
- [ ] Numeric values of `MED` `scrap_only`, `LOW` `drone`/`weapon`, `MED` `stuff`.

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-fandom-auto-ship-near-storage-station]] (per `raw/wiki/auto-ship-near-storage-station.md`)
