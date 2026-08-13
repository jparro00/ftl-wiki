---
id: event-rebel-fight-in-plasma-storm
type: event
event_name: STORM_REBEL
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: nebula
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [plasma-storm, rebel, no-choice, combat, default-rewards, unique]
---

# Rebel fight in plasma storm — `STORM_REBEL`

## Summary
Three elements of XML: text, a Rebel ship, a plasma storm. No choices, no blue options, no
escape. It is the crewed counterpart to [[event-auto-ship-fight-in-plasma-storm]] — and
notably, where that event hands you three ways out, this one hands you none.

## Trigger & Where It Appears
- Beacon: **plasma storm** (`<environment type="storm"/>`).
- `unique="true"` — once per run.
- Lists: `NEBULA` ([[source-newevents]]), `NEBULA_HOSTILE` ([[source-events-nebula]]),
  `NEBULA_REBEL` ([[source-events-rebel]]) and `STORM_SLUG` ([[source-events-slug]]).
  The `STORM_SLUG` membership is what gives it the widest sector reach in this batch
  alongside [[event-nebula-lost-ship]] — `STORM_SLUG` is allocated 1–3 per Slug sector
  ([[source-sector-data-xml]]).
- Long-range scanners show a ship
  ([[source-fandom-rebel-fight-in-plasma-storm]]).

## Text
> You arrive in the middle of a plasma storm. Despite the harsh conditions, a Rebel scout
> seems to be waiting for you.

(`event_STORM_REBEL_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | Immediate combat with a `REBEL` ship, default rewards. | 100% |

The `REBEL` ship definition ([[source-events-ships]]):
`<surrender chance="0.5" min="2" max="3" load="PIRATE_SURRENDER"/>` — accepting pays
`autoReward level="RANDOM">stuff`; `<escape chance="0.5" min="3" max="4"
load="PIRATE_ESCAPE"/>`; `<destroyed load="DESTROYED_DEFAULT"/>` →
`autoReward level="MED">standard`; `<deadCrew load="DEAD_CREW_DEFAULT"/>`
([[source-events-xml]]).

Unlike the auto-ship, this enemy **can** surrender or run — so the fight has partial
outcomes even though the event does not.

## Blue Options
None.

## Rewards & Risks
- Reward: `MED` / `standard` on a kill, or a `RANDOM` / `stuff` roll on an accepted
  surrender.
- Risk: a crewed Rebel warship in a plasma storm, with sensors down.
- **Slug-sector pursuit trap:** [[source-fandom-rebel-fight-in-plasma-storm]] notes that
  when reached through `STORM_SLUG` the beacon can sit **outside** the nebula region of the
  map — you still get the storm environment, but you pay **full** fleet pursuit on the jump
  out rather than the reduced nebula rate. The same note appears on
  [[source-fandom-boarders-humans-in-plasma-storm]], the other `STORM_SLUG` member.

## Strategy Notes
- Nothing to decide. Route choice is the only lever, and the `STORM_SLUG` membership means
  Slug sectors carry 1–3 guaranteed storm beacons of which this is one of three entries
  ([[source-sector-data-xml]], [[source-events-slug]]).
- The 50% surrender chance makes this a reasonable fight to start and a reasonable one to
  break off from.

## Related
- [[event-auto-ship-fight-in-plasma-storm]] — the same beacon type, uncrewed enemy, three
  escape options
- [[event-boarders-humans-in-plasma-storm]] — the other `STORM_SLUG` member, shares the
  pursuit note
- [[event-rebel-fight-in-nebula]] — the shadowed nebula equivalent that never fires
- [[concept-rebel-fleet-advance]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Numeric values behind `DESTROYED_DEFAULT` and `PIRATE_SURRENDER`'s `RANDOM`/`stuff`.
- [ ] The exact nebula fleet-pursuit rate the Fandom note compares against (it says 80%).

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rebel-fight-in-plasma-storm]] (per raw/wiki/rebel-fight-in-plasma-storm.md)
