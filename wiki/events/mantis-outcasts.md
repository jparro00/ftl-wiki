---
id: event-mantis-outcasts
type: event
event_name: ZOLTAN_BOARDERS_MANTIS
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, boarding-hazard, default-rewards, forced-fight, mantis]
---

# Mantis outcasts — `ZOLTAN_BOARDERS_MANTIS`

## Summary
A Mantis boarding action inside Zoltan space: **2–3 Mantis boarders** land while a Mantis
scout engages. Fewer boarders than [[event-zoltan-border-police]], but Mantis are the
strongest melee species in the game, so this is the more lethal of the sector's two
boarding events.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: hostile; a ship is shown on Long-Ranged Scanners
  ([[source-fandom-mantis-outcasts]]). The boarders are not signalled in advance.
- Reached via the `BOARDERS_ZOLTAN` event list, allocated `min=1 max=2` beacons in both
  Zoltan sectors ([[source-sector-data-xml]]). The list has three members — this event,
  [[event-zoltan-border-police]], and `BOARDERS_HACKING`.
- `unique="true"` — at most once per sector.

## Text
> The Mantis outcasts sometimes make the mistake of taking the Zoltan for easy game. A
> scout moves in to attack while a boarding party beams aboard from a nearby transport!

(`event_ZOLTAN_BOARDERS_MANTIS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `<ship load="MANTIS_FIGHT" hostile="true"/>` + `<boarders min="2" max="3" class="mantis"/>` — **2–3 Mantis boarders aboard your ship** and a simultaneous fight with a Mantis ship ([[entity-mantis]]), **default rewards**. | 100% |

Both sources agree on the boarder count (`min="2" max="3"` / *"2-3 mantis boarders"*).
Fandom additionally notes that the `MANTIS_FIGHT` ship has **no surrender or escape
values specified** in `events_ships.xml` — it will fight to the end
([[source-fandom-mantis-outcasts]]).

## Blue Options
None.

## Rewards & Risks
- **Rewards:** default rewards for a Mantis ship at the current sector depth.
- **Risks:**
  - Mantis crew deal roughly double melee damage. Two or three of them will kill an
    unsupported crew member before help arrives, and can clear a system room quickly.
  - The `MANTIS_FIGHT` ship never surrenders or flees, so the engagement runs to a
    conclusion while you are fighting boarders.
  - The event is scripted with no preceding choice, so there is no chance to pre-vent
    rooms or reposition crew.

## Strategy Notes
- *Opinion:* treat this as more dangerous than [[event-zoltan-border-police]] despite the
  smaller party. Do not trade blows with Mantis in an open room — vent, or fight them at
  a [[item-medbay]] where your crew heals through the damage.
- Because the ship never surrenders, there is no "scare them off" outcome; plan to
  destroy it or kill its crew.
- The same `MANTIS_FIGHT` ship blueprint is used by [[event-mantis-fight-zoltan]] in the
  hostile pool, so the two encounters share an opponent.

## Related
- [[event-zoltan-border-police]] — the other unique `BOARDERS_ZOLTAN` member
- [[event-mantis-fight-zoltan]] — same ship blueprint, no boarders
- [[entity-mantis]] — the boarders
- [[entity-mantis]] — the ship

## Open Questions
- [ ] `MANTIS_FIGHT` blueprint loadout by sector depth.
- [ ] Whether the boarders arrive immediately or on a delay.

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-mantis-outcasts]] (per raw/wiki/mantis-outcasts.md)
