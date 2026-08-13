---
id: event-rebel-fight
type: event
event_name: REBEL
sectors: [[[sector-abandoned-sector]], [[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-the-last-stand]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [rebel, no-choice, default-rewards, combat, surrender-possible]
---

# Rebel fight — `REBEL`

## Summary
The baseline Rebel encounter and one of the most widely-reachable events in the game: you
arrive, a Rebel warship is already hostile, there are no choices. Three lines of XML — a
ten-string text list and `<ship load="REBEL" hostile="true"/>`. The `REBEL` ship
definition it loads is reused as the enemy by a large number of other events across every
sector family, which is why the event id turns up constantly in the data files.

## Trigger & Where It Appears
- Sectors: nearly everywhere — [[sector-rebel-controlled-sector]],
  [[sector-rebel-stronghold]], [[sector-civilian-sector]], [[sector-federation-space]],
  [[sector-abandoned-sector]], [[sector-engi-controlled-sector]],
  [[sector-engi-homeworlds]], [[sector-mantis-controlled-sector]],
  [[sector-mantis-homeworlds]], [[sector-zoltan-controlled-sector]],
  [[sector-zoltan-homeworlds]], and [[sector-the-last-stand]].
- Beacon: hostile — the event loads a hostile ship on arrival.
- Event lists it sits in: `HOSTILE_REBEL` ([[source-events-rebel]]), `HOSTILE1` and
  `HOSTILE_CIVILIAN` ([[source-newevents]]), `HOSTILE_ENGI`
  ([[source-events-engi]]), `HOSTILE_MANTIS` ([[source-events-mantis]]),
  `HOSTILE_ZOLTAN` ([[source-events-zoltan]]), `HOSTILE_LANIUS`
  ([[source-dlcevents-anaerobic]]), `BOSS_NEUTRAL` ([[source-events-boss]]), plus the AE
  replacements `OVERRIDE_HOSTILE1`, `OVERRIDE_HOSTILE2`, `OVERRIDE_HOSTILE_ENGI`,
  `OVERRIDE_HOSTILE_MANTIS`, `OVERRIDE_HOSTILE_REBEL`, `OVERRIDE_HOSTILE_ZOLTAN`
  ([[source-dlceventsoverwrite]]).
- In a Rebel sector, `HOSTILE_REBEL` is allocated `min=6 max=8` beacons
  ([[source-sector-data-xml]]).
- Not unique — it recurs freely within a run. Long-range scanners show a ship
  ([[source-fandom-rebel-fight]]).

## Text
The prose is drawn from the `REBEL` text list and **varies across ten strings**
([[source-events-rebel]], [[source-text-events-xml]]) — no single one is *the* event text.
Representative examples:

> Your ship is hailed. "We've found you at last. Prepare to die!"

> You receive a transmission: "Sorry sir, this is nothing personal but we're under
> orders." The Rebel ship's weapons go hot.

> A Rebel ship approaches cautiously. "Personally," says the captain, "I'd have stuck with
> the Federation. But I'm a soldier, sir, and I'm no use without a war to fight. Raise your
> shields!"

All ten are transcribed on [[source-fandom-rebel-fight]] and in `raw/gamedata/text_events.xml`
at `text_REBEL_1` … `text_REBEL_10`.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements)* | — | Immediate combat with `<ship load="REBEL" hostile="true"/>`, **default rewards**. | 100% |

### The `REBEL` ship
Defined in `raw/gamedata/events_ships.xml` on the `SHIPS_REBEL` auto-blueprint
([[source-events-ships]]):

| Branch | Behaviour |
|---|---|
| `surrender` | `chance="0.5"`, offered when hull is between 2 and 3, loads the shared `PIRATE_SURRENDER` event |
| `escape` | `chance="0.5"`, triggers at hull 3–4, loads `PIRATE_ESCAPE` |
| `destroyed` | `DESTROYED_DEFAULT` — `autoReward level="MED"` `standard` |
| `deadCrew` | `DEAD_CREW_DEFAULT` — `autoReward level="MED"` or `HIGH` `standard`, or `HIGH` `fuel`, drawn from a seven-entry list |

`PIRATE_SURRENDER` (in `raw/gamedata/events.xml`, [[source-events-xml]]) lets you accept
— ship becomes non-hostile, `autoReward level="RANDOM"` `stuff` — or refuse and keep
fighting.

> ⚠️ **CONTRADICTION (scope):** [[source-fandom-rebel-fight]] states the outcome flatly as
> *"Fight a Rebel ship (default rewards)"* and says nothing about the surrender or escape
> branches. The game files do define both ([[source-events-ships]]). Trusting the game
> files (`high` vs `medium`); Fandom is incomplete here rather than wrong, since
> "default rewards" is its own shorthand for the `DESTROYED_DEFAULT` payout.

## Blue Options
None.

## Rewards & Risks
- Reward: `MED` standard scrap-with-resources on destruction; a `RANDOM` `stuff` payout if
  you accept a surrender; a `MED`/`HIGH` roll if you kill the crew instead.
- Risk: an ordinary Rebel warship for the sector depth. The 50% escape chance means a
  damaged enemy may jump out before you finish it — no fleet-pursuit penalty is attached
  to that in the ship definition ([[source-events-ships]]).

## Strategy Notes
- Nothing to decide. The only lever is sector routing: a Rebel sector allocates 6–8
  `HOSTILE_REBEL` beacons and this event is one of five (six in AE) entries in that pool
  ([[source-sector-data-xml]], [[source-dlceventsoverwrite]]).
- *(Opinion.)* Killing the crew rather than destroying the hull pays better on average —
  `DEAD_CREW_DEFAULT` skews `HIGH` where `DESTROYED_DEFAULT` is flatly `MED`
  ([[source-events-xml]]).

## Related
- [[event-auto-ship-fight]] — the unmanned counterpart, same role in the same lists
- [[event-rebel-fight-with-boarders]] — the same `REBEL` ship, plus 2–3 boarders
- [[event-rebel-ship-warning]] — a Rebel ship that runs for the fleet instead
- [[event-rebel-fight-engi]], [[event-rebel-fight-crystal]] — sector-flavoured variants with their own ids
- [[concept-rebel-fleet-advance]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Notes on page joining
Three further Fandom pages were auto-matched to this event id
(`Battlefield wreckage`, `Crystal chat`, `Encrypted federation signal`). They match only
because those events also load the `REBEL` *ship*; each names a different in-game id in
its own Notes. They are **not** sources for this page.

## Open Questions
- [ ] Numeric values behind `MED`/`HIGH` `standard` at a given sector depth.
- [ ] Whether all ten text variants are equally weighted (the list states no weights).
- [ ] Composition of the `SHIPS_REBEL` auto-blueprint pool by sector.

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-rebel-fight]] (per `raw/wiki/rebel-fight.md`)
