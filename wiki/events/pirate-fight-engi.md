---
id: event-pirate-fight-engi
type: event
event_name: ENGI_PIRATE_FIGHT
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [forced-fight, default-rewards, no-choice]
---

# Pirate fight (Engi) — `ENGI_PIRATE_FIGHT`

## Summary
A forced pirate fight with a single fixed intro text and default rewards. The plainest
event in the Engi pool: no choices, no branches, no blue options.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]
- Beacon: hostile — the event loads a hostile ship on arrival
- Event lists: `HOSTILE_ENGI` and `OVERRIDE_HOSTILE_ENGI`. `HOSTILE_ENGI` is allocated
  `min=5 max=7` in both Engi sectors ([[source-sector-data-xml]])
- Not unique — it can recur within a run

## Text
> There must have been rich pickings for pirates around here up until war broke out. The
> pirate you encounter here looks worn down, but hungry. You'll have to fight!

(`event_ENGI_PIRATE_FIGHT_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — forced fight)* | — | `<ship load="PIRATE" hostile="true"/>` — the generic pirate ship, with **default rewards**. | 100% |

## Blue Options
None.

## Rewards & Risks
- Default rewards on victory; no source here states the amounts.
- Risk: an ordinary pirate engagement. The event adds no environmental hazard, no boarders,
  and no ambush twist ([[source-events-xml]], per `raw/gamedata/events_engi.xml`).

## Strategy Notes
- Nothing to decide. Worth noting only that the generic `PIRATE` ship is also reachable in
  Engi space through the plain `PIRATE`, `PIRATE_CHOICE`, `PIRATE_ASTEROID`, `PIRATE_SUN`
  and `PIRATE_NO_ESCAPE` entries that share the `HOSTILE_ENGI` list
  ([[source-events-xml]]) — this is the Engi-flavoured variant of a common encounter.

## Related
- [[event-mantis-fight-engi]], [[event-rebel-fight-engi]] — the other two `HOSTILE_ENGI` Engi entries
- [[entity-pirates]]

## Open Questions
- [ ] What "default rewards" resolve to numerically at a given sector depth.
- [ ] Does the `PIRATE` ship in this event surrender or escape?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-pirate-fight-engi]] (per `raw/wiki/pirate-fight-engi.md`)
