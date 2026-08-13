---
id: event-mantis-fight-zoltan
type: event
event_name: ZOLTAN_MANTIS
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [unique, default-rewards, forced-fight, mantis]
---

# Mantis fight (Zoltan) — `ZOLTAN_MANTIS`

## Summary
A straight Mantis ambush in Zoltan space. No choices, default rewards, no boarders. The
Mantis presence in a Zoltan sector is flavour — mechanically this is a plain filler
fight, distinguished only by the opponent's species.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: hostile; a ship is shown on Long-Ranged Scanners
  ([[source-fandom-mantis-fight-zoltan]]).
- Reached via `HOSTILE_ZOLTAN` (vanilla) / `OVERRIDE_HOSTILE_ZOLTAN` (AE), allocated
  `min=6 max=8` beacons in both Zoltan sectors ([[source-sector-data-xml]]).
- `unique="true"` — at most once per sector.

## Text
> You pick up the last broadcast from a rupturing Zoltan freighter: "The Mantis, they're
> here, please-" You're interrupted by fire off the port bow!

(`event_ZOLTAN_MANTIS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `<ship load="MANTIS_FIGHT" hostile="true"/>` — fight a Mantis ship ([[entity-mantis]]), **default rewards**. | 100% |

Fandom notes the `MANTIS_FIGHT` ship has **no surrender or escape values specified** in
`events_ships.xml` — it will not flee or offer terms
([[source-fandom-mantis-fight-zoltan]]).

## Blue Options
None.

## Rewards & Risks
- **Rewards:** default rewards for a Mantis ship at the current sector depth.
- **Risks:** no environment hazard and no scripted boarders — but Mantis ships commonly
  carry a teleporter in their blueprints, so an unscripted boarding is still possible
  depending on which `MANTIS_FIGHT` blueprint spawns. No source ingested here confirms
  the loadout, so treat that as unverified.
- The ship never surrenders or escapes, so the fight runs to completion.

## Strategy Notes
- *Opinion:* a welcome beacon in a Zoltan sector — a Mantis ship has no Super Shield, so
  laser-heavy builds that struggle with [[event-zoltan-fight]] handle this one easily.
- Keep crew off the hull-side rooms if the enemy blueprint turns out to carry a
  teleporter.

> ⚠️ **CONTRADICTION (version):** which event list supplies this event.
> - `HOSTILE_ZOLTAN` (raw/gamedata/events_zoltan.xml) — 7 entries.
> - `OVERRIDE_HOSTILE_ZOLTAN` (raw/gamedata/dlcEventsOverwrite.xml) — 8 entries, adds
>   `REBEL_PULSAR`, replaces `HOSTILE_ZOLTAN` when AE content is enabled
>   ([[source-events-zoltan]]).
>
> A genuine **vanilla-vs-AE difference, not an error**.

## Related
- [[event-mantis-outcasts]] — same `MANTIS_FIGHT` ship blueprint, plus 2–3 boarders
- [[event-zoltan-fight]], [[event-pirate-fight-zoltan]], [[event-engi-fight]] — the rest
  of the hostile pool
- [[entity-mantis]] — the opponent

## Open Questions
- [ ] `MANTIS_FIGHT` blueprint loadout by sector depth — specifically whether it can
      carry a teleporter.

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-mantis-fight-zoltan]] (per raw/wiki/mantis-fight-zoltan.md)
