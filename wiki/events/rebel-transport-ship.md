---
id: event-rebel-transport-ship
type: event
event_name: REBEL_TRANSPORT
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: hostile
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [rebel, unique, filler, optional-fight, timed-escape, item-reward, crew-reward-chance]
---

# Rebel transport ship — `REBEL_TRANSPORT`

## Summary
A fleeing Rebel cargo hauler with the richest random loot table in `events_rebel.xml`:
eleven possible outcomes if you destroy it, four more if you kill the crew instead —
including weapons, drone schematics, map data and a free crew member. It runs on a timer,
it never surrenders, and if it escapes you get nothing (but pay no fleet penalty either).

## Trigger & Where It Appears
- Sectors: [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]],
  [[sector-civilian-sector]], [[sector-federation-space]],
  [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]],
  [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]].
- Event lists: `NEUTRAL_REBEL` ([[source-events-rebel]]), `NEUTRAL_MANTIS`
  ([[source-events-mantis]]), `NEUTRAL`, `NEUTRAL_EXIT`, `NEUTRAL_CIVILIAN`
  ([[source-newevents]]), plus `OVERRIDE_NEUTRAL` and `OVERRIDE_NEUTRAL_EXIT`
  ([[source-dlceventsoverwrite]]). Also an exit/filler beacon
  ([[source-fandom-rebel-transport-ship]] records `alsooccur=exitandfiller`).
- `NEUTRAL_REBEL` is allocated `min=5 max=6` per Rebel sector
  ([[source-sector-data-xml]]).
- `unique="true"` — at most once per run.
- `<img planet="NONE"/>` — deep space, no planet backdrop ([[source-events-rebel]]).
- Long-range scanners show a ship ([[source-fandom-rebel-transport-ship]]).

## Text
> You spot a small Rebel ship nearby. It seems to have been re-fitted for transport rather
> than combat. It does not seem to want to engage you and your ship.

(`event_REBEL_TRANSPORT_text`, per [[source-text-events-xml]])

Note: unlike its neutral siblings this event declares **no `<ship>` at the top level** —
nothing is present until you choose to attack ([[source-events-rebel]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Demand the surrender of their goods. | — | *"You prepare to secure their cargo by force."* → fight `<ship load="SQUAT_TRANSPORT" hostile="true"/>`, which immediately starts running. Destroy it → roll on `REBEL_TRANSPORT_DESTROYED` (11 entries). Kill the crew → roll on `REBEL_TRANSPORT_CAPTURED` (4 entries). It escapes → nothing. | 100% (deterministic) |
| 2 | Avoid the ship. | — | *"They stay outside your weapons range, and eventually jump away."* → nothing happens. | 100% |

### The `SQUAT_TRANSPORT` ship
`auto_blueprint="SHIPS_REBEL"`, `<escape timer="40" min="14" max="14">`
([[source-events-ships]]):

- Escape text: *"They look like they don't want to fight. They are trying to escape."*
- **No surrender branch** — confirmed by both the file and
  [[source-fandom-rebel-transport-ship]].
- No `gotaway` block, and therefore **no fleet-pursuit penalty** if it gets away —
  [[source-fandom-rebel-transport-ship]] states this explicitly as a Trivia note, and the
  ship definition bears it out.
- `destroyed` → `REBEL_TRANSPORT_DESTROYED`; `deadCrew` → `REBEL_TRANSPORT_CAPTURED`.

Fandom notes that despite the flavour text the ship is not generated any differently from
any other Rebel ship, and that the reward tables are identical to
`Pirate smuggler ship` ([[source-fandom-rebel-transport-ship]]).

### `REBEL_TRANSPORT_DESTROYED` — 11 entries
One drawn at random; the file states no weights, so odds are **unknown**
([[source-events-rebel]], [[source-text-events-xml]]):

| # | Summary | Reward |
|---|---|---|
| 1 | Undamaged military weaponry | `autoReward level="MED"` **`weapon`** |
| 2 | Only blueprints and broken machinery | `LOW` `standard` |
| 3 | One intact weapon | `low` `weapon` *(the level attribute is lowercase in the file — quoted as-is)* |
| 4 | Weaponry, nothing survived | `MED` `scrap_only` |
| 5 | Military-grade Drone Schematics | `MED` **`drone`** |
| 6 | Schematics destroyed, parts recovered | `MED` **`droneparts`** |
| 7 | Survey ship with detailed maps | `<reveal_map/>` **and** `MED` `scrap_only` |
| 8 | Information-gathering ship, nothing useful | `MED` `scrap_only` |
| 9 | Prisoner transport, sole survivor joins you | `<crewMember amount="1"/>` **and** `LOW` `standard` |
| 10 | Prisoner transport, all killed | `LOW` `standard` |
| 11 | Military supplies | `HIGH` `standard` |

### `REBEL_TRANSPORT_CAPTURED` — 4 entries (crew killed)
([[source-events-rebel]], [[source-text-events-xml]]):

| # | Summary | Reward |
|---|---|---|
| 1 | Military-grade weaponry | `MED` **`weapon`** |
| 2 | Prisoner transport; survivor joins in exchange for freedom | `<crewMember amount="1"/>` **and** `HIGH` `scrap_only` |
| 3 | Beacon information | `<reveal_map/>` **and** `MED` `scrap_only` |
| 4 | Military-grade Drone Schematics | `MED` **`drone`** |

The captured table is uniformly better: every entry pays at least `MED`, two of four give an
item or a crew member, and none pays nothing.

## Blue Options
None. Neither choice carries a `req=`.

## Rewards & Risks
- Reward: extremely varied — see the two tables. Best cases are a `MED` weapon, a `MED`
  drone schematic, or a free crew member with `HIGH` `scrap_only`.
- Risk: a crewed Rebel ship at sector strength that will not surrender. The real risk is
  **wasting the beacon** — the 14-unit escape window is tight and a slow loadout may not
  kill it in time.
- Choice 2 is mechanically free.

## Strategy Notes
- *(Opinion.)* One of the best neutral beacons in the game if you can burst it down.
  Boarding is doubly rewarded here: the `REBEL_TRANSPORT_CAPTURED` table strictly dominates
  the destroyed table, and a boarding crew ignores the escape timer's damage race — you
  only have to stop the FTL, not the hull.
- If you cannot kill it fast, choice 2 loses nothing. There is no penalty for letting it go,
  and no penalty for failing — the only cost is the beacon.

## Related
- [[event-rebel-ship-warning]] — the other `SQUAT_*` runner, with a fleet penalty attached
- [[event-rebel-fight]] — the standard Rebel warship
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Weights inside `REBEL_TRANSPORT_DESTROYED` (11) and `REBEL_TRANSPORT_CAPTURED` (4).
- [ ] Whether the lowercase `level="low"` on destroyed-entry 3 parses as `LOW` or falls back
      to a default — the file is inconsistent with every other entry.
- [ ] Species of the `<crewMember amount="1"/>` awards.

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-rebel-transport-ship]] (per `raw/wiki/rebel-transport-ship.md`)
