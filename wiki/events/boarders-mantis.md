---
id: event-boarders-mantis
type: event
event_name: MANTIS_BOARDERS
sectors: [[[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [boarding-hazard, crew-risk, unique, mantis, no-choice]
---

# Boarders: Mantis — `MANTIS_BOARDERS`

## Summary
A no-choice ambush: you arrive, and 2–4 Mantis boarders are already on your ship. There
is nothing to click and nothing to negotiate — the event's entire mechanical payload is
`<boarders min="2" max="4" class="mantis"/>` ([[source-events-xml]], per
`raw/gamedata/events_mantis.xml`). Mantis are the strongest melee species in the game, so
this is one of the more dangerous boarding events in a [[sector-mantis-homeworlds]] run.

## Trigger & Where It Appears
- Sectors: [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]
- Drawn from the `BOARDERS_MANTIS` event list, which both Mantis sector types allocate at
  `min=1 max=2` beacons ([[source-sector-data-xml]], per `raw/gamedata/sector_data.xml`).
  That list contains `MANTIS_BOARDERS` twice and `BOARDERS_SUN` once, so this event is
  the likely draw but not guaranteed ([[source-events-xml]]).
- `unique="true"` — it can only fire once per sector.
- Long-range scanners show **no ship** at the beacon ([[source-fandom-boarders-mantis]]).
  There is no enemy vessel; the boarders simply appear.

## Text
The intro prose is drawn from the `MANTIS_BOARDERS` text list — it **varies** between the
three strings below, so no single one can be quoted as *the* event text
([[source-events-xml]], [[source-text-events-xml]]):

> A derelict and still smoking Mantis vessel floats by. The battle must have been recent;
> its surviving crew beam aboard. Prepare for a fight!

> Your world, all of a sudden, changes. The Mantis are on board your ship.

> You hear a grating rattle and a soft clicking. You reach for your pistol.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | 2–4 Mantis boarders beam aboard. | 100% |

The count is a uniform range in the game files (`min="2" max="4"`); the file does not
weight it, and no source gives a distribution across 2, 3, or 4
([[source-events-xml]]). Fandom states the same range ([[source-fandom-boarders-mantis]]).

## Blue Options
None. The event exposes no `req=` gated choices at all.

## Rewards & Risks
- **No reward.** There is no `autoReward`, no scrap, no item — killing the boarders gives
  only whatever the standard boarder-kill behaviour gives.
- **Risk:** 2–4 [[entity-mantis]] boarders. Mantis have the highest melee damage of any
  crew species, and a 4-boarder draw on a low-crew ship is a run-ender. Expect system
  damage in whatever rooms they land in.

## Strategy Notes
- *(Opinion, not sourced to any strategy guide here.)* Because there is no choice, the
  only preparation is structural: door upgrades, an O2-venting plan, and a Medbay to
  fight over. Mantis sectors allocate 1–2 of these beacons plus 6–7 hostile beacons
  ([[source-sector-data-xml]]), so the boarding risk is a reason to weigh a Mantis sector
  against the alternatives at the sector-select map.

## Related
- [[event-mantis-fight]] — the plain Mantis ship fight from the same sectors
- [[event-escape-pod]] — the other Mantis-sector event that can drop a boarder on you
- [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]
- [[entity-mantis]]

## Open Questions
- [ ] Distribution of the 2/3/4 boarder count — uniform is an assumption, not stated.
- [ ] Which rooms the boarders spawn in, and whether that is random.
- [ ] What `BOARDERS_SUN` (the third entry in `BOARDERS_MANTIS`) does — not yet paged.

## Sources
- [[source-events-xml]] (per raw/gamedata/events_mantis.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-boarders-mantis]] (per raw/wiki/boarders-mantis.md)
