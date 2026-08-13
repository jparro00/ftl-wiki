---
id: event-auto-ship-fight-in-nebula
type: event
event_name: NEBULA_AUTO
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: nebula
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [nebula, rebel, auto-ship, no-choice, combat, default-rewards]
---

# Auto-ship fight in nebula — `NEBULA_AUTO`

## Summary
The nebula's baseline forced fight against a Rebel drone. Three elements of XML — a text
list, `<ship load="REBEL_AUTO" hostile="true"/>`, and `<environment type="nebula"/>` — with
no choices at all. It is the auto-ship counterpart to
[[event-rebel-fight-in-nebula]], and unlike that one it actually fires, because no
`eventList` shadows its name.

## Trigger & Where It Appears
- Beacon: nebula (sensors offline for the fight).
- Reached through four event lists — `NEBULA` (`raw/gamedata/newEvents.xml`),
  `NEBULA_HOSTILE` (`raw/gamedata/events_nebula.xml`), `NEBULA_REBEL`
  (`raw/gamedata/events_rebel.xml`) and `NEBULA_ZOLTAN`
  (`raw/gamedata/events_zoltan.xml`) ([[source-newevents]], [[source-events-nebula]],
  [[source-events-rebel]], [[source-events-zoltan]]).
- Those lists are allocated per sector by `sector_data.xml` ([[source-sector-data-xml]]):
  `NEBULA` 0–4 in [[sector-federation-space]] and 0–8 in [[sector-civilian-sector]];
  `NEBULA_PIRATE` 0–5 in [[sector-pirate-controlled-sector]] (which nests `NEBULA_REBEL`);
  `NEBULA_REBEL` 0–5 in [[sector-rebel-controlled-sector]] and [[sector-rebel-stronghold]];
  `NEBULA_ZOLTAN` 2–6 in [[sector-zoltan-controlled-sector]] and
  [[sector-zoltan-homeworlds]]; `NEBULA_HOSTILE` 5–6 in [[sector-uncharted-nebula]].
- No `unique` attribute — it can repeat within a run.
- Long-range scanners show a ship at a nebula beacon
  ([[source-fandom-auto-ship-fight-in-nebula]]).

## Text
The prose is drawn from the `NEBULA_AUTO_LIST` text list and **varies across five
strings** ([[source-events-nebula]], [[source-text-events-xml]]). Representative:

> You cross paths with an advance scout of the Rebel fleet searching this section of the
> nebula for your ship.

> The tangled wrecks of many ships wait in dormancy here. You see lights flicker on what
> looks like debris. A Rebel scout bursts out of the wreckage!

> This drone isn't looking for you. Perhaps it's scouting ahead for the Rebel expansion or
> maybe they're seeking to use this nebula for cover. Regardless, it identifies you as
> hostile.

All five are at `text_NEBULA_AUTO_LIST_1` … `_5` and are transcribed on
[[source-fandom-auto-ship-fight-in-nebula]].

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | Immediate combat with a Rebel auto-ship (`ship load="REBEL_AUTO" hostile="true"`). | 100% |

The `REBEL_AUTO` ship definition in `events_ships.xml` carries **no surrender and no
escape** — only `<destroyed load="DESTROYED_DEFAULT"/>` and
`<deadCrew load="DEAD_CREW_DEFAULT"/>` ([[source-events-ships]]). Being an auto-ship it has
no crew, so `DESTROYED_DEFAULT` is the only path that fires: `autoReward level="MED"`,
payload `standard` — what Fandom calls *"medium scrap with resources"*
([[source-events-xml]], [[source-fandom-auto-ship-fight-in-nebula]]).

## Blue Options
None.

## Rewards & Risks
- Reward: `MED` / `standard` on destruction. Nothing else.
- Risk: an ordinary Rebel drone, but fought **inside a nebula** — your sensors are down for
  the whole fight and you cannot see inside enemy rooms.

## Strategy Notes
- Nothing to decide; the only lever is route choice. In [[sector-uncharted-nebula]] this
  event sits in a `NEBULA_HOSTILE` pool allocated 5–6 beacons per sector, so expect
  several forced nebula fights there ([[source-sector-data-xml]]).
- Auto-ships have no crew, which makes them safe targets for boarding-heavy builds' worst
  matchup (nothing to kill) but immune to anti-crew weapons. That is a property of the
  `SHIPS_AUTO` blueprint pool, not of this event, and is not stated in the sources read
  here.

## Related
- [[event-auto-ship-fight-in-plasma-storm]] — same `REBEL_AUTO` fight, storm environment,
  and it gives you three escape options
- [[event-auto-ship-warning-in-nebula]] — the auto-ship that runs and calls the fleet
- [[event-auto-ship-near-storage-station-in-nebula]] — an auto-ship you can choose to fight
- [[event-rebel-fight-in-nebula]] — the crewed equivalent, which is shadowed and never fires
- [[concept-rebel-fleet-advance]], [[sector-uncharted-nebula]]

## Open Questions
- [ ] Numeric values behind `autoReward level="MED">standard`.
- [ ] Whether all five text variants are equally weighted (the list states no weights).

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-auto-ship-fight-in-nebula]] (per raw/wiki/auto-ship-fight-in-nebula.md)
