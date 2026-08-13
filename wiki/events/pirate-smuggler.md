---
id: event-pirate-smuggler
type: event
event_name: NEBULA_PIRATE_SMUGGLE
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-uncharted-nebula]]]
beacon_type: nebula
hostile: false
blue_options: [[[item-weapon-control]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [nebula, pirate, blue-option, weapons, fuel-reward, escape, optional-fight]
---

# Pirate smuggler — `NEBULA_PIRATE_SMUGGLE`

## Summary
A smuggler tries to slip past you. You can shake him down with a big enough gun deck, rob
him outright, or let him go. The bribe is the only `MED` fuel payout in the nebula file,
and the fight behind it is unusually generous — `PIRATE_SMUGGLE` shares the Rebel transport
loot tables, which include weapons, drones, crew and a map reveal.

## Trigger & Where It Appears
- Beacon: nebula (`<environment type="nebula"/>`). **No ship on arrival** — the encounter
  is text-only until you choose (`LRSmap=noship+nebula`,
  [[source-fandom-pirate-smuggler]]).
- No `unique` attribute — it repeats.
- Lists: `NEBULA` ([[source-newevents]]), `NEBULA_NEUTRAL` and `NEBULA_PIRATE`
  ([[source-events-nebula]], [[source-events-pirate]]). `NEBULA` 0–4 in
  [[sector-federation-space]] / 0–8 in [[sector-civilian-sector]]; `NEBULA_PIRATE` 0–5 in
  [[sector-pirate-controlled-sector]]; `NEBULA_NEUTRAL` 7–8 in
  [[sector-uncharted-nebula]] ([[source-sector-data-xml]]).
- Carries the developer note `<!-- TO DO - NEED TO MAKE A NEW PIRATE SHIP THAT ATTEMPTS TO
  BRIBE YOU WHEN SURRENDERING-->` ([[source-events-nebula]]) — the bribe idea ended up on
  the choice instead of the ship.

## Text
> A pirate ship arrives shortly after you. Judging from the fact that it is attempting to
> avoid your ship, you assume that it's a smuggler trying to stay away from beacons.

(`event_NEBULA_PIRATE_SMUGGLE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the pirate. | — | *"You power up your weapons and move in to engage."* → fight `PIRATE_SMUGGLE`. | 100% |
| 2 | Ignore the ship. | — | *"It jumps away after a time."* — nothing happens. | 100% |
| 3 | **(Weapons)** Activate your advanced weapons threateningly. | `req="weapons" lvl="6"`, `hidden="true"` | *"They hail you, 'There's no need for aggression... Perhaps this would convince you to look the other way?'"* → two nested choices below. | 100% |
| 3a | ↳ Take their bribe. | — | `autoReward level="MED"` with payload **`fuel`**. Fandom expands this as *"2–4 fuel"* plus scrap. | 100% |
| 3b | ↳ Ignore their bribe and attack. | — | Fight `PIRATE_SMUGGLE`. | 100% |

### The `PIRATE_SMUGGLE` ship
Defined in `events_ships.xml` on the `SHIPS_PIRATE` blueprint pool, marked
`<!-- NEEDS ELITE TAG -->` ([[source-events-ships]]):

| Ship outcome | XML | Effect |
|---|---|---|
| Surrender | `<surrender chance="0.5" min="2" max="4">` | *"We realize our ship is no match for yours. If you let us go we can make it worth your while."* Accept → ship goes non-hostile + `autoReward level="RANDOM">stuff`. Refuse → fight continues. |
| Escape | `<escape timer="35" min="3" max="4">` | *"They look like they don't want to fight. They are trying to escape."* 35-second countdown; if it jumps, nothing happens. |
| Destroyed | `<destroyed load="REBEL_TRANSPORT_DESTROYED"/>` | An **eleven-entry** table in `events_rebel.xml`: `MED` weapon, `LOW` standard ×3, `LOW` weapon, `MED` scrap_only ×3, `MED` drone, `MED` droneparts, one entry with `<reveal_map/>`, one with **+1 crew**, one `HIGH` standard ([[source-events-rebel]]). |
| Dead crew | `<deadCrew load="REBEL_TRANSPORT_CAPTURED"/>` | The sibling table — includes `MED` weapon, **+1 crew with `HIGH` scrap_only**, and a `<reveal_map/>` entry ([[source-events-rebel]]). |

Fandom glosses the raw thresholds as *"escape at 30-40% hull"* and *"50% chance to
surrender at 20-40% hull"*, hedging on the page itself that the real values are hull points
adjusted by sector progression ([[source-fandom-pirate-smuggler]]).

## Blue Options
- **[[item-weapon-control]] level 6** (`req="weapons" lvl="6"`) — a high bar; level 6 is
  most of a fully-built weapons system. It converts a fight into a free choice between
  guaranteed fuel and a fight you may still take. It never *removes* the fight option, so
  it is strictly additive.

## Rewards & Risks
- **Bribe (3a):** `MED` / `fuel` for zero risk — the cleanest fuel source in the nebula
  pool, which matters because nebula sectors are where fuel starvation bites.
- **Fight (1 / 3b):** the richest kill table in this batch. `REBEL_TRANSPORT_DESTROYED`
  and `REBEL_TRANSPORT_CAPTURED` between them can pay a weapon, a drone schematic, drone
  parts, a crew member, or a full map reveal — outcomes the phrase "default rewards" badly
  undersells.
- **Risks:** it can escape after 35 seconds and pay nothing; and it is a fight in a nebula
  with sensors down.

## Strategy Notes
- If you are short on fuel, take the bribe. If you are not, the destroyed/captured tables
  are worth more in expectation than `MED` fuel — but only if you can stop it escaping
  inside 35 seconds. *(Opinion, from the tables above; no source recommends a line.)*
- Boarding is favoured over shooting here: `REBEL_TRANSPORT_CAPTURED` is the shorter table
  and its crew-member entry pays `HIGH` scrap alongside.
- Note the surrender pays `RANDOM` stuff — an unbounded roll, not a guaranteed floor.

## Related
- [[event-pirate-fight-in-nebula]] — the shadowed pirate fight this event effectively
  replaces in the pool
- [[event-pirate-ship-selling-weapon]] — the other pirate you can choose not to fight
- [[item-weapon-control]], [[sector-uncharted-nebula]]

## Open Questions
- [ ] Numeric values behind `MED` / `fuel` — Fandom's "2–4 fuel" is not in the files.
- [ ] Full text of the eleven `REBEL_TRANSPORT_DESTROYED` entries (only the rewards were
      read here).
- [ ] How `min`/`max` on `surrender` and `escape` convert to the hull percentages Fandom
      quotes.

## Notes on sector coverage
> ⚠️ **CONTRADICTION:** [[source-fandom-pirate-smuggler]] lists three sectors (Civilian,
> Pirate Controlled, Uncharted Nebula); the game files add [[sector-federation-space]] via
> the `NEBULA` allocation to `STANDARD_SPACE` ([[source-sector-data-xml]],
> [[source-newevents]]). Trusting the game files (`high` vs `medium`).

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-rebel]] (per raw/gamedata/events_rebel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-pirate-smuggler]] (per raw/wiki/pirate-smuggler.md)
