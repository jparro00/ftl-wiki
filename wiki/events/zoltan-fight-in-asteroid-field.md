---
id: event-zoltan-fight-in-asteroid-field
type: event
event_name: ZOLTAN_ASTEROID
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [unique, asteroid-field, default-rewards, forced-fight]
---

# Zoltan fight in asteroid field — `ZOLTAN_ASTEROID`

## Summary
[[event-zoltan-fight]] with an asteroid field bolted on. No choices, default rewards, and
the environment runs for the whole engagement — making it the most punishing of the
sector's filler fights for a low-shield ship.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: hostile, in an **asteroid field** (`<environment type="asteroid"/>`). Long-Ranged
  Scanners show a ship plus the asteroid field, so it is identifiable in advance
  ([[source-events-zoltan]], [[source-fandom-zoltan-fight-in-asteroid-field]]).
- Reached via `HOSTILE_ZOLTAN` (vanilla) / `OVERRIDE_HOSTILE_ZOLTAN` (AE), allocated
  `min=6 max=8` beacons in both Zoltan sectors ([[source-sector-data-xml]]).
- `unique="true"` — at most once per sector.

## Text
> You arrive in an asteroid field and are greeted by a Zoltan guard, "By attempting to
> access these closed mining fields, you are in violation of the Natural Mineral
> Protection Act. Your weaponry will be confiscated for processing." You don't have time
> for this.

(`event_ZOLTAN_ASTEROID_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `<ship load="ZOLTAN_SHIP" hostile="true"/>` in an asteroid field — fight a Zoltan ship ([[entity-zoltan]]), **default rewards**. | 100% |

## Blue Options
None.

## Rewards & Risks
- Default rewards for a Zoltan ship at the current sector depth. **No bonus is given for
  the added hazard.**
- Risk: continuous asteroid impacts on both ships for the duration. Against a Zoltan ship
  this is worse than usual — you need time to strip the Super Shield, and the asteroid
  field is charging your hull for every second of it.
- A [[item-defense-drone]] neutralises most of the hazard; the enemy Zoltan ship does not
  benefit from one unless its blueprint carries it.

## Strategy Notes
- *Opinion:* if Long-Ranged Scanners reveal this beacon (ship + asteroid field) and your
  shields are thin, route around it. The rewards are identical to
  [[event-zoltan-fight]] with strictly more risk — there is no upside to taking it
  deliberately.
- Asteroid impacts can knock out enemy systems as readily as yours; against the Super
  Shield this can occasionally work in your favour, but it is not something to plan on.

> ⚠️ **CONTRADICTION (version):** which event list supplies this event.
> - `HOSTILE_ZOLTAN` (raw/gamedata/events_zoltan.xml) — 7 entries.
> - `OVERRIDE_HOSTILE_ZOLTAN` (raw/gamedata/dlcEventsOverwrite.xml) — 8 entries, adds
>   `REBEL_PULSAR`, and replaces `HOSTILE_ZOLTAN` when AE content is enabled
>   ([[source-events-zoltan]]).
>
> A genuine **vanilla-vs-AE difference, not an error**.

## Related
- [[event-zoltan-fight]] — the same ship without the hazard
- [[event-zoltan-ship-follows-mantis-ship]] — the other Zoltan asteroid-field encounter
- [[entity-zoltan]], [[item-zoltan-shield]] — the opponent and its defence
- [[concept-asteroid-field]] — the hazard
- [[item-defense-drone]] — the counter

## Open Questions
- [ ] Which `ZOLTAN_SHIP` blueprints spawn here at each sector depth.
- [ ] Does the enemy ship ever spawn with a Defense Drone in this event?

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-zoltan-fight-in-asteroid-field]] (per raw/wiki/zoltan-fight-in-asteroid-field.md)
