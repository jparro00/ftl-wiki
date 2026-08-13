---
id: event-mantis-fight-in-nebula-slug
type: event
event_name: NEBULA_SLUG_MANTIS
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, combat, nebula, default-rewards, mantis]
---

# Mantis fight in nebula (Slug) — `NEBULA_SLUG_MANTIS`

## Summary
A Mantis raider hunting Slugs on their own turf. No choices — you fight a standard Mantis
ship at default rewards, in a nebula, with no surrender and no escape available to the
enemy.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — via the
  `NEBULA_HOSTILE_SLUG` event list (`min 5 / max 7` per sector)
  ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: nebula (`<environment type="nebula"/>`), `unique="true"`

## Text
> The Mantis attack ship here looks to have been hunting Slugs on their home turf - a rare
> test of honor for the mightiest Mantis crews. Weapons up!

(`event_NEBULA_SLUG_MANTIS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | (none) | — | `<ship load="MANTIS_FIGHT" hostile="true"/>` — fight a Mantis ship, default rewards. | 100% |

### The enemy — `MANTIS_FIGHT`

`auto_blueprint="SHIPS_MANTIS"`, `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT`, and **no
surrender or escape block at all**. Crew composition is specified
([[source-events-ships]]):

| Species | Proportion |
|---|---|
| Mantis | 0.80 |
| Engi | 0.20 |

## Rewards & Risks
- Default rewards on a kill.
- Risk: a Mantis crew fights hard in boarding actions, and the fight is in a nebula so your
  sensors are down. The enemy cannot flee or surrender, so it is a fight to the finish.

## Strategy Notes
- Because `MANTIS_FIGHT` has no escape block, this is a safe target for slow crew-kill
  strategies — the ship will not run.
- The 20% Engi share means the crew is not uniformly Mantis; a boarding party may meet
  weaker defenders than the ship type suggests. ([[source-events-ships]])

## Related
- [[event-slug-fight-in-nebula]] — the Slug-crewed fight from the same list
- [[event-mantis-ship-attacking-slug-ship]] — the distress-beacon Mantis event in these
  sectors
- [[entity-mantis]]

## Open Questions
- [ ] Whether the crew `prop` values set counts or per-slot probabilities.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-mantis-fight-in-nebula-slug]] (per raw/wiki/mantis-fight-in-nebula-slug.md)
