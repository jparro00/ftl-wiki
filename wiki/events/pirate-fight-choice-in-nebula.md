---
id: event-pirate-fight-choice-in-nebula
type: event
event_name: NEBULA_SLUG_PIRATE
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, combat, nebula, optional-fight, default-rewards, pirate]
---

# Pirate fight choice in nebula — `NEBULA_SLUG_PIRATE`

## Summary
A stranded pirate ship deep in Slug space. It sits in the `NEBULA_HOSTILE_SLUG` list but
the fight is **optional** — you can simply leave. One of the few free outs in the Slug
hostile pool.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — via the
  `NEBULA_HOSTILE_SLUG` event list (`min 5 / max 7` per sector)
  ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: nebula (`<environment type="nebula"/>`), `unique="true"`
- The pirate is loaded **non-hostile** at arrival — `<ship load="PIRATE" hostile="false"/>` —
  and only turns hostile if you attack ([[source-events-slug]])

## Text
> You're surprised to find a ship without Slug markings stranded all the way out here, and
> move in to provide assistance. When you see the pirate insignia on the hull you quickly
> reconsider.

(`event_NEBULA_SLUG_PIRATE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack! | — | `<ship hostile="true"/>` — the already-loaded `PIRATE` becomes hostile. Default rewards. | 100% |
| 2 | Keep your distance and hope they haven't seen you yet. | — | Nothing happens. | 100% |

### The enemy — `PIRATE`

`auto_blueprint="SHIPS_PIRATE"`; `surrender chance="0.5" min="3" max="4"` loading
`PIRATE_SURRENDER`, `escape chance="0.5" min="2" max="4"` loading `PIRATE_ESCAPE`, plus a
`gotaway` text and default destroyed/deadCrew blocks ([[source-events-ships]]). Note the
escape band (`min="2"`) is wider than the surrender band.

## Rewards & Risks
- Default rewards if you win, nothing if you leave.
- Risk is entirely opt-in — this is the only hostile-list Slug event where declining costs
  you nothing at all.

## Strategy Notes
- Free scrap if your ship is healthy, free skip if it isn't. Both choices are unhidden, so
  you know the option to leave exists before committing.
- A 50% escape chance at 20–40% hull means a damaged pirate may flee with your reward;
  the same 50% surrender roll may hand it over instead.

## Related
- [[event-slug-fight-in-nebula]], [[event-mantis-fight-in-nebula-slug]] — the other
  `NEBULA_HOSTILE_SLUG` entries
- [[entity-pirates]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Contents of `PIRATE_SURRENDER` (defined outside this file).

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-pirate-fight-choice-in-nebula]] (per raw/wiki/pirate-fight-choice-in-nebula.md)
