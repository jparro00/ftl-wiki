---
id: event-boarders-rebels-in-nebula
type: event
event_name: NEBULA_REBEL_BOARDING
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: nebula
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [rebel, nebula, boarding, unique, no-choice, no-enemy-ship]
---

# Boarders: rebels in nebula — `NEBULA_REBEL_BOARDING`

## Summary
Three to four human boarders teleport onto your ship from a nearby station, and **there is
no enemy ship at all** — no target to shoot, no fight to end early, no surrender. Pure
crew combat inside a nebula, which means your Sensors are down for the duration. The
shortest event in `events_rebel.xml` and one of the most dangerous for a thin crew.

## Trigger & Where It Appears
- Sectors: [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]],
  [[sector-civilian-sector]], [[sector-federation-space]],
  [[sector-pirate-controlled-sector]], [[sector-uncharted-nebula]],
  [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]].
- Event lists: `NEBULA_REBEL` ([[source-events-rebel]]) and `NEBULA_PIRATE`
  ([[source-events-pirate]]). `NEBULA_REBEL` is allocated `min=0 max=5` per Rebel sector
  ([[source-sector-data-xml]]).
- Beacon: **nebula** — the event declares `<environment type="nebula"/>`, so it is always a
  nebula beacon regardless of which list drew it ([[source-events-rebel]]).
- `unique="true"` — at most once per run.
- Long-range scanners show a nebula and **no ship**
  ([[source-fandom-boarders-rebels-in-nebula]]).

## Text
> There appear to be a number of small stations nearby. Before you have time to scan them,
> warnings go off. A Rebel teleporter was used in one of the stations. You've been boarded!

(`event_NEBULA_REBEL_BOARDING_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements)* | — | `<boarders min="3" max="4" class="human"/>` — **3–4 human boarders** aboard your ship. No `<ship>` element: nothing to fight in space, and no reward of any kind. | 100% |

The event body is three tags: environment, text, boarders. There is no `autoReward`, no
follow-up choice, and no ship ([[source-events-rebel]]).
[[source-fandom-boarders-rebels-in-nebula]] records the same, listing only the boarders.

## Blue Options
None.

## Rewards & Risks
- **Reward: none.** Surviving is the entire outcome. This event cannot pay you.
- Risk: 3–4 boarders, one more than [[event-rebel-fight-with-boarders]] fields, and no
  enemy hull to destroy as an escape hatch — the fight ends only when the boarders are
  dead (or your crew is).
- Nebula environment: Sensors are disabled, so you fight without room visibility unless you
  have crew in the affected rooms.

## Strategy Notes
- *(Opinion.)* The worst version of a boarding event: maximum boarder count, zero payout,
  degraded information. The mitigations are structural rather than tactical — upgraded
  Doors, a Medbay you can bait them into, and not entering nebula beacons with a
  two-person crew.
- Since there is no enemy ship, weapons, drones and hacking contribute nothing. Anti-personnel
  drones and Mind Control are the systems that matter here.

## Related
- [[event-rebel-fight-with-boarders]] — Rebel boarders *with* a ship attached
- [[event-boarders-mantis]], [[event-boarders-crystal]] — other faction boarding events
- [[sector-uncharted-nebula]]
- [[concept-nebula-beacons]]
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Whether nebula ion-storm variants can stack on this beacon.
- [ ] Whether the boarder count scales with difficulty (nothing in the file suggests it).

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-boarders-rebels-in-nebula]] (per `raw/wiki/boarders-rebels-in-nebula.md`)
