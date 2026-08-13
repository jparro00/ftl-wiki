---
id: event-rebel-fight-engi
type: event
event_name: ENGI_REBEL_FIGHT
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

# Rebel fight (Engi) — `ENGI_REBEL_FIGHT`

## Summary
A forced Rebel fight with a single fixed intro text and default rewards. Its only flavour
contribution is establishing that the Rebel fleet is already pushing into Engi space.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]
- Beacon: hostile — the event loads a hostile ship on arrival
- Event lists: `HOSTILE_ENGI` and `OVERRIDE_HOSTILE_ENGI`. `HOSTILE_ENGI` is allocated
  `min=5 max=7` in both Engi sectors ([[source-sector-data-xml]])
- Not unique — it can recur within a run

## Text
> The rebel fighter here would seem to suggest elements of the rebel fleet are already
> making incursions on Engi space. You move to engage.

(`event_ENGI_REBEL_FIGHT_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — forced fight)* | — | `<ship load="REBEL" hostile="true"/>` — the generic Rebel ship, with **default rewards**. | 100% |

## Blue Options
None.

## Rewards & Risks
- Default rewards on victory; no source here states the amounts.
- Risk: an ordinary Rebel engagement, with no added hazard or twist
  ([[source-events-xml]], per `raw/gamedata/events_engi.xml`).

## Strategy Notes
- Nothing to decide. The generic `REBEL` ship is also reachable in Engi space through the
  plain `REBEL` entry that shares the `HOSTILE_ENGI` list ([[source-events-xml]]).

## Related
- [[event-mantis-fight-engi]], [[event-pirate-fight-engi]] — the other two `HOSTILE_ENGI` Engi entries
- [[event-engi-distress-rebel-fight]] — a Rebel fight with a reward tree behind it
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] What "default rewards" resolve to numerically at a given sector depth.
- [ ] Does the `REBEL` ship in this event surrender or escape?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-rebel-fight-engi]] (per `raw/wiki/rebel-fight-engi.md`)
