---
id: event-pirate-fight-near-sun
type: event
event_name: PIRATE_SUN
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-pirate-controlled-sector]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 9
tags: [pirate, unavoidable-fight, default-rewards, sun-hazard, unique]
---

# Pirate fight near sun — `PIRATE_SUN`

## Summary
[[event-pirate-fight]] run inside a solar flare hazard. Same `PIRATE` ship and the same
default rewards, but the star heats your systems and starts fires for as long as you stay
at the beacon. There are no choices; `unique="true"` means it can only happen once per
run.

## Trigger & Where It Appears
- Sectors: [[sector-civilian-sector]], [[sector-engi-controlled-sector]],
  [[sector-engi-homeworlds]], [[sector-federation-space]],
  [[sector-pirate-controlled-sector]]
- Event lists: `HOSTILE_PIRATE` ([[source-events-pirate]]), `HOSTILE_CIVILIAN`
  ([[source-newevents]]), `HOSTILE_ENGI` ([[source-events-engi]]), and under Advanced
  Edition `OVERRIDE_HOSTILE2`, `OVERRIDE_HOSTILE_ENGI`, `OVERRIDE_HOSTILE_PIRATE`
  ([[source-dlceventsoverwrite]]). `HOSTILE_CIVILIAN` is what puts it in
  [[sector-federation-space]], which [[source-fandom-pirate-fight-near-sun]] omits.
- `unique="true"` — once per run ([[source-events-pirate]];
  [[source-fandom-pirate-fight-near-sun]] agrees, `unique=true`)
- Environment: `<environment type="sun"/>`, drawn against `<img back="BG_DARK"/>`
  ([[source-events-pirate]])
- Long-range scanners show a ship and the red giant
  ([[source-fandom-pirate-fight-near-sun]], `LRSmap=ship+redgiant`)

## Text
> This beacon has been placed too close to a super-giant class M star! The ship will
> gradually overheat until you get out of here... or die. A pirate, apparently oblivious
> to the danger of the sun, moves in to engage.

(`event_PIRATE_SUN_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices)_ | — | `<ship load="PIRATE" hostile="true"/>` with `<environment type="sun"/>` — combat starts immediately under solar flare damage. | 100% |

The event body is a `<text>`, a hostile `<ship>` and an `<environment>` — nothing else
([[source-events-pirate]]).

The ship is the standard `<ship name="PIRATE">`: surrender `chance="0.5"` at 3–4 hull,
escape `chance="0.5"` at 2–4 hull, `DESTROYED_DEFAULT` on a kill, `DEAD_CREW_DEFAULT` on a
crew wipe. Full profile on [[event-pirate-fight]] ([[source-events-ships]],
[[source-events-xml]]).

## Blue Options
None. The event has no `req=` gates.

## Rewards & Risks
- Rewards are identical to [[event-pirate-fight]] — the "default rewards" profile.
- **Risk:** the sun hazard damages and ignites rooms on both ships for the whole
  encounter. Unlike an asteroid field this cannot be shielded away, and it burns crew and
  oxygen as well as hull.

## Strategy Notes
- *(Opinion.)* The hazard hits the enemy too, which is why letting the fight run long is
  less lopsided here than it looks — but you cannot vent and fight at the same time
  forever. Accepting the surrender is the fastest exit.
- Being `unique`, this cannot be the beacon that ends you twice in one run; it is worth
  spending a repair to clear it early if you have the hull for it.

## Related
- [[event-pirate-fight]] — the same fight without the hazard; full ship profile
- [[event-pirate-fight-in-asteroid-field]] — the asteroid-hazard sibling
- [[event-boarders-humans-near-sun]] — the same star hazard with boarders instead
- [[entity-pirates]]
- [[sector-pirate-controlled-sector]], [[sector-civilian-sector]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-federation-space]]

## Open Questions
- [ ] Solar flare tick rate / damage is not defined in this event.

## Sources
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — `HOSTILE_CIVILIAN`)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml — `HOSTILE_ENGI`)
- [[source-fandom-pirate-fight-near-sun]] (per raw/wiki/pirate-fight-near-sun.md)
