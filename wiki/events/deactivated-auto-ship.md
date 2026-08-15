---
id: event-deactivated-auto-ship
type: event
event_name: BROKEN_REBEL_DRONE
sectors: [[[sector-abandoned-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: any
hostile: false
blue_options: [[[item-sensors]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 10
tags: [rebel, auto-ship, unique, filler, blue-option, map-reveal, optional-fight]
---

# Deactivated Auto-ship — `BROKEN_REBEL_DRONE`

## Summary
A dormant Rebel auto-ship you can loot safely for `LOW` scrap, or gamble with for scrap
*and* a map reveal at the risk of waking it up. Sensors 3 turns the gamble into an informed
choice rather than removing it. One of the widest-reaching filler events in the game — it
appears in six sector families' neutral pools plus the generic filler list.

## Trigger & Where It Appears
- Sectors: [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]],
  [[sector-abandoned-sector]], [[sector-engi-controlled-sector]],
  [[sector-engi-homeworlds]], [[sector-mantis-controlled-sector]],
  [[sector-mantis-homeworlds]], [[sector-slug-controlled-nebula]],
  [[sector-slug-home-nebula]].
- Event lists: `NEUTRAL_REBEL` ([[source-events-rebel]]), `NEUTRAL_ENGI`
  ([[source-events-engi]]), `NEUTRAL_MANTIS` ([[source-events-mantis]]), `NEUTRAL_LANIUS`
  ([[source-dlcevents-anaerobic]]), `NEUTRAL` ([[source-newevents]], the hardcoded filler
  list), `OVERRIDE_NEUTRAL` ([[source-dlceventsoverwrite]]). Its entry in the Zoltan pool
  is **commented out** (`events_zoltan.xml` lines 72–74, alongside `AUTO_DEFENSE_ITEM`,
  [[source-events-zoltan]]).
- `unique="true"` — at most once per run.
- Long-range scanners show a ship ([[source-fandom-deactivated-auto-ship]]).

> ⚠️ **CONTRADICTION (reach):** [[source-fandom-deactivated-auto-ship]] additionally lists
> Zoltan Controlled Sector and Zoltan Homeworlds. In the game files the Zoltan-specific
> route is disabled — `NEUTRAL_ZOLTAN`'s `BROKEN_REBEL_DRONE` entry is inside a comment
> block ([[source-events-zoltan]]). It can still reach Zoltan sectors through the generic
> `NEUTRAL` / `OVERRIDE_NEUTRAL` filler lists, so the wiki is not wrong that it shows up
> there — but the dedicated Zoltan entry it implies does not exist. Trusting the game
> files. Exactly the same disabled pair applies to
> [[event-auto-ship-near-storage-station]].

## Text
> You find a Rebel automated scout floating near this beacon. Despite its pristine
> condition, it appears to be de-activated.

(`event_BROKEN_REBEL_DRONE_text`, per [[source-text-events-xml]])

The event loads `<ship load="REBEL_AUTO" hostile="false"/>` — the standard auto-ship,
dormant ([[source-events-rebel]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attempt to download the ship's data stores. | `hidden="true"` (no `req`) | Rolls the two-entry `DOWNLOAD_DRONE_DATA` list — see below. | unknown |
| 2 | Don't risk activating it, and just strip the ship for any useful scrap. | — | `autoReward level="LOW"` `scrap_only`. No text. Guaranteed, no risk. | 100% |
| 3 | **(Sensors)** Remotely scan the ship. | `req="sensors"`, `lvl="3"`, `hidden="true"` | Rolls the two-entry `BROKEN_REBEL_DRONE_SENSORS` list — see below. | unknown |

### `DOWNLOAD_DRONE_DATA` (choice 1)
Two entries, no weights stated ([[source-events-rebel]]):

| Entry | Text | Result |
|---|---|---|
| 1 | *"You are able to pull all of the ship's data about this sector. Your map has been updated."* | `<reveal_map/>` **and** `autoReward level="LOW"` `standard` |
| 2 | *"You accidentally reactivate the ship's AI. Its weapons immediately go online; prepare for a fight!"* | `<ship load="REBEL_AUTO" hostile="true"/>` → the ordinary auto-ship fight, `MED` `standard` on the kill via `DESTROYED_DEFAULT` |

### `BROKEN_REBEL_DRONE_SENSORS` (choice 3)
Two entries, no weights stated ([[source-events-rebel]]):

| Entry | Text | Result |
|---|---|---|
| 1 | *"Your improved Sensors indicate that it's safe to hack into the drone. You upload its map data to your navigation system and strip the ship of useful materials."* | `<reveal_map/>` **and** `autoReward level="LOW"` `standard` — the good outcome, taken straight |
| 2 | *"Your improved Sensors indicate the ship is on standby, ready to activate at a moment's notice. Will you still attempt to access the ship's data?"* | A **second choice**: *"Yes."* → rolls `DOWNLOAD_DRONE_DATA` again (so still a coin flip); *"No."* → *"You leave the ship alone and prepare to jump."*, nothing happens |

So Sensors 3 does not guarantee the reward — it guarantees you are *told* when the ship is
live, and lets you back out. Note that backing out forfeits choice 2's free `LOW`
`scrap_only` as well, since the sub-event's "No" branch pays nothing.

## Blue Options
- **[[item-sensors]] level 3** (`req="sensors" lvl="3"`) — the maximum Sensors level. It
  converts choice 1's blind coin flip into: half the time a free reveal + scrap, half the
  time an explicit warning and an opt-out. Strictly more information, not strictly more
  reward.

## Rewards & Risks
- Safe path (choice 2): `LOW` `scrap_only`, guaranteed, zero risk.
- Gamble path: `LOW` `standard` **and** a full sector map reveal, or an auto-ship fight
  (which itself pays `MED` `standard` if you win).
- Risk: the fight is against the plain `REBEL_AUTO` — no crew, no surrender, no escape
  ([[source-events-ships]]). It is a real fight but not an ambush with a twist.

## Strategy Notes
- *(Opinion.)* At full hull this is close to free money: the "bad" branch is an ordinary
  auto-ship fight that pays *more* scrap than the safe option. Take the gamble unless the
  hull is thin or the sector is deep enough that a `SHIPS_AUTO` roll is genuinely dangerous.
- With Sensors 3, take choice 3 rather than choice 1 — same upside, plus an escape hatch.
- The map reveal is the real prize in a Rebel sector; the scrap is incidental.

## Related
- [[event-auto-ship-fight]] — the fight this event can turn into, same `REBEL_AUTO` ship
- [[event-auto-ship-near-sensor-station]] — the other Sensors-3 map-reveal beacon
- [[item-sensors]]
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Weights inside `DOWNLOAD_DRONE_DATA` and `BROKEN_REBEL_DRONE_SENSORS` — two entries
      each, no `prop` attributes.
- [ ] Numeric values of `LOW` `scrap_only` vs `LOW` `standard`.
- [ ] Whether Fandom's *"weapons **and shields** immediately go online"* wording reflects an
      older text — the current file says only *"Its weapons immediately go online"*
      ([[source-text-events-xml]] vs [[source-fandom-deactivated-auto-ship]]).

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-fandom-deactivated-auto-ship]] (per `raw/wiki/deactivated-auto-ship.md`)
