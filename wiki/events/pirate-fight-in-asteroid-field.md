---
id: event-pirate-fight-in-asteroid-field
type: event
event_name: PIRATE_ASTEROID
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-pirate-controlled-sector]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 9
tags: [pirate, unavoidable-fight, default-rewards, asteroid-field, cut-content]
---

# Pirate fight in asteroid field — `PIRATE_ASTEROID`

## Summary
[[event-pirate-fight]] with an asteroid field running. Same `PIRATE` ship, same default
rewards, but incoming asteroids hammer both ships for the duration and there is exactly
one choice: fight. The game files also contain a **commented-out Piloting blue option**
that would have let you leave the field first — cut content, documented below.

## Trigger & Where It Appears
- Sectors: [[sector-civilian-sector]], [[sector-engi-controlled-sector]],
  [[sector-engi-homeworlds]], [[sector-federation-space]],
  [[sector-pirate-controlled-sector]]
- Event lists: `HOSTILE_PIRATE` ([[source-events-pirate]]), `HOSTILE_CIVILIAN`
  ([[source-newevents]]), `HOSTILE_ENGI` ([[source-events-engi]]), and under Advanced
  Edition `OVERRIDE_HOSTILE2`, `OVERRIDE_HOSTILE_ENGI`, `OVERRIDE_HOSTILE_PIRATE`
  ([[source-dlceventsoverwrite]]). `HOSTILE_CIVILIAN` is what puts it in
  [[sector-federation-space]], which [[source-fandom-pirate-fight-in-asteroid-field]] omits.
- Not `unique` — can repeat within a sector ([[source-events-pirate]];
  [[source-fandom-pirate-fight-in-asteroid-field]] agrees, `unique=false`)
- Environment: `<environment type="asteroid"/>`; the beacon is drawn with
  `<img planet="NONE" back="BG_DARK"/>` ([[source-events-pirate]])
- Long-range scanners show a ship **and** the asteroid field
  ([[source-fandom-pirate-fight-in-asteroid-field]], `LRSmap=ship+asteroidfield`)

## Text
> A pirate ship was lying in wait inside this asteroid field. It immediately moves in to
> attack.

(`event_PIRATE_ASTEROID_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Turn and fight. | — | Empty `<event/>` — the fight is already running from the `<ship load="PIRATE" hostile="true"/>` in the event body. Asteroids keep striking throughout. | 100% |
| — | ~~(Piloting) Attempt to maneuver out of the asteroid field before engaging the pirate.~~ | `req="pilot" lvl="2"` | **Commented out in the game files** — see below. | n/a |

The ship is the standard `<ship name="PIRATE">`; its surrender (`chance="0.5"`, 3–4 hull),
escape (`chance="0.5"`, 2–4 hull), `DESTROYED_DEFAULT` and `DEAD_CREW_DEFAULT` branches
are documented in full on [[event-pirate-fight]] ([[source-events-ships]],
[[source-events-xml]]).

### Cut content — the Piloting escape
`raw/gamedata/events_pirate.xml` contains, commented out, a second choice and the event
list it would have loaded ([[source-events-pirate]]):

```
<choice req="pilot" lvl="2" hidden="true">
  <text>(Piloting) Attempt to maneuver out of the asteroid field before engaging the pirate.</text>
  <event load="PIRATE_ASTEROID_PILOTING"/>
</choice>
```

`PIRATE_ASTEROID_PILOTING` is itself commented out and headed `<!-- No longer used -->`.
Its two entries were: your pilot gets you clear of the field undamaged, **or** the pirate
catches you before you leave and `<environment type="asteroid"/>` stays on. Neither is
reachable in the shipped game. [[source-fandom-pirate-fight-in-asteroid-field]] notes the
same removal and points to TCRF's partially-unused-events list.

## Blue Options
None reachable. The only `req=` gate in the file (`pilot` level 2) is commented out.

## Rewards & Risks
- Rewards are identical to [[event-pirate-fight]] — MED `standard` on destruction, the
  `DEAD_CREW_DEFAULT` table on a crew kill, `RANDOM` `stuff` on an accepted surrender.
- **Risk:** the asteroid field. Hull damage accrues from the environment as well as the
  enemy, and asteroid strikes can start fires and breaches while you are already engaged.

## Strategy Notes
- *(Opinion.)* This is the pirate fight where taking the surrender is most often correct,
  because the environment keeps charging you hull for every extra second the fight runs.
- Defence drones and level-2+ shields blunt the field considerably; without either, ending
  the fight fast matters more than maximising the reward table.

## Related
- [[event-pirate-fight]] — the same fight without the hazard; full ship profile
- [[event-pirate-fight-near-sun]] — the sun-hazard sibling
- [[event-boarders-asteroid]] — asteroid field plus boarders instead of a ship fight
- [[entity-pirates]]
- [[sector-pirate-controlled-sector]], [[sector-civilian-sector]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-federation-space]]

## Open Questions
- [ ] Was the Piloting option removed in AE or already dead in 1.0? The file comment
      (`No longer used`) does not date the change.
- [ ] Asteroid strike frequency / damage is not defined in this event.

## Sources
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — `HOSTILE_CIVILIAN`)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml — `HOSTILE_ENGI`)
- [[source-fandom-pirate-fight-in-asteroid-field]] (per raw/wiki/pirate-fight-in-asteroid-field.md)
