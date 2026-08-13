---
id: event-auto-ship-attacking-outpost
type: event
event_name: AUTO_REFUEL_STATION
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: hostile
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [rebel, auto-ship, unique, optional-fight, filler, stacked-reward]
---

# Auto-ship attacking outpost — `AUTO_REFUEL_STATION`

## Summary
An optional auto-ship fight where the reward is paid twice: a `LOW` payout for the kill,
then a grateful outpost adds a `MED` payout on top. Simple, safe as auto-ship fights go
(no crew, no surrender, no escape), and one of the better filler beacons in the generic
pools.

## Trigger & Where It Appears
- Sectors: [[sector-civilian-sector]], [[sector-federation-space]],
  [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]].
- Event lists: `HOSTILE1`, `HOSTILE_CIVILIAN`, `NEUTRAL`, `NEUTRAL_EXIT`
  ([[source-newevents]]) and the AE lists `OVERRIDE_HOSTILE1`, `OVERRIDE_HOSTILE2`,
  `OVERRIDE_NEUTRAL`, `OVERRIDE_NEUTRAL_EXIT` ([[source-dlceventsoverwrite]]).
- `NEUTRAL` and `NEUTRAL_EXIT` are the hardcoded **filler** lists used to top a sector up
  once its other allocations are exhausted ([[source-newevents]]) — so this event also
  appears as an exit/filler beacon
  ([[source-fandom-auto-ship-attacking-outpost]] records `alsooccur=exitandfiller`).
- `unique="true"` — at most once per run.
- The event sets `<img planet="PLANET_POPULATED_SMALL"/>` — a small populated planet
  backdrop ([[source-events-rebel]]).
- Long-range scanners show a ship ([[source-fandom-auto-ship-attacking-outpost]]).

> ⚠️ **CONTRADICTION (reach):** [[source-fandom-auto-ship-attacking-outpost]] lists
> Civilian Sector, Slug Controlled Nebula and Slug Home Nebula. It sits in `HOSTILE1` /
> `OVERRIDE_HOSTILE1` as well, which [[sector-federation-space]] draws on
> ([[source-newevents]], [[source-dlceventsoverwrite]]). Trusting the game files.

## Text
> You detect an automated Rebel scout attacking a small refueling outpost.

(`event_AUTO_REFUEL_STATION_text`, per [[source-text-events-xml]])

The event loads `<ship load="REBEL_AUTO_REFUEL" hostile="false"/>` — the ship is present
but **not hostile** until you choose to intervene ([[source-events-rebel]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Intervene to defend the outpost. | — | *"Detecting the higher threat, the automated ship moves in to engage your ship."* → the ship turns hostile. Destroy it → `autoReward level="LOW"` `standard`, then a hidden follow-up → `autoReward level="MED"` `standard`. | 100% (deterministic) |
| 2 | Avoid the conflict. | — | *"You steer clear of the conflict. The outpost receives a beating but the ship stops its attack before it's destroyed."* → nothing happens. | 100% |

### The `REBEL_AUTO_REFUEL` ship
`auto_blueprint="SHIPS_AUTO"`. Only a `destroyed` branch is defined — **no surrender, no
escape, no `deadCrew`** ([[source-events-ships]]):

- *"The ship breaks apart and you quickly salvage what you can."* → `autoReward level="LOW"`
  `standard`, followed by a hidden `continue` choice:
  > The outpost hails you after the scout was destroyed, "Thanks for the help. We've been
  > harassed non-stop by those scouts. Take this on the house."
  → `autoReward level="MED"` `standard`.

Both payouts are `standard` (scrap with resources), and the second is unconditional — it is
a `hidden="true"` continue, not a gated choice.

## Blue Options
None.

## Rewards & Risks
- Reward: `LOW` `standard` **plus** `MED` `standard`, stacked, on a guaranteed path. No
  randomness at all once you commit.
- Risk: an auto-ship fight of the sector's difficulty. No boarding, no escape, no surrender
  — the fight runs to a hull kill, so a slow weapon loadout means a long exchange.
- Choice 2 is mechanically free.

## Strategy Notes
- *(Opinion.)* One of the cleanest positive-EV filler beacons: deterministic double reward,
  no dice roll on the outcome, and an enemy with no crew (so no boarding risk and no
  anti-personnel counterplay needed). Take it unless hull is critical.
- Contrast [[event-rebel-ship-attacking-refueling-outpost]], which is the same setup with a
  *crewed* Rebel ship and a fuel reward instead — that one is riskier and pays fuel.

## Related
- [[event-rebel-ship-attacking-refueling-outpost]] — the crewed twin (`SQUAT_REFUEL_STATION`)
- [[event-auto-ship-attacking-civilian]] — the same "intervene or not" shape with a rescue table
- [[event-auto-ship-fight]] — the unavoidable auto-ship fight
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Numeric values of `LOW` and `MED` `standard` at a given sector depth.
- [ ] Whether the outpost follow-up can ever be skipped (the choice is `hidden="true"`, i.e.
      auto-taken, but this is not stated explicitly anywhere).

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-fandom-auto-ship-attacking-outpost]] (per `raw/wiki/auto-ship-attacking-outpost.md`)
