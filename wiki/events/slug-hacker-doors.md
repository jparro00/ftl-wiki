---
id: event-slug-hacker-doors
type: event
event_name: NEBULA_SLUG_DOORS
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: true
blue_options: [hacking system]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, combat, nebula, system-malfunction, fire-risk, blue-option]
---

# Slug hacker (doors) — `NEBULA_SLUG_DOORS`

## Summary
A forced fight in which your Door system is hacked offline and the enemy is guaranteed a
fire weapon — the worst possible pairing, since doors are how you vent fires. A Hacking
system of your own converts it into an ordinary fight.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — via the
  `NEBULA_HOSTILE_SLUG` event list (`min 5 / max 7` per sector)
  ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: nebula (`<environment type="nebula"/>`), `unique="true"`
- The event definition carries a dev note: `<!-- NEEDS CODE TO GIVE FIRE WEAPONS-->`. The
  fire weapons are in fact supplied by the enemy ship's `weaponOverride`
  ([[source-events-slug]], [[source-events-ships]])

## Text
> There are few more vicious beasts in the galaxy than a Slug with his back to the wall.
> The faltering ship armed with fire-weapons uses a remote hacking tool to try and disable
> your door system - they're going to burn you out!

(`event_NEBULA_SLUG_DOORS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | *Continue…* | — | `<status type="limit" target="player" system="doors" amount="0"/>` + `<ship load="JELLY_STATUS_DOORS" hostile="true"/>` — fight with your **Door system offline**. Destroyed: `MED standard`; crew killed: `HIGH standard`. | 100% |
| 2 | **(Hacking System)** Counter the remote hacking. | `req="hacking"` | "Your hacking system automatically counters the digital assault…" → `<ship load="JELLY_STATUS_HACKING_FIRE" hostile="true"/>` + `<status type="limit" target="player" system="hacking" amount="0"/>` — doors work, your **Hacking** is offline. Destroyed and crew killed: `HIGH standard`. | 100% |

Choice 1 is not hidden; choice 2 is `hidden="true"` and marked `<!-- CHANGED - added -->`
in the source, i.e. an Advanced Edition addition ([[source-events-slug]]).

### The enemies

Both ships are `auto_blueprint="SHIPS_JELLY"` with a forced fire weapon
([[source-events-ships]]):

```
<weaponOverride count="1">
    <name>BEAM_FIRE</name>
    <name>BOMB_FIRE</name>
</weaponOverride>
```

so the Slug carries **exactly one** of Fire Beam or Fire Bomb. Neither ship has a surrender
or escape block. Winning clears the imposed status (`doors`, `oxygen`, `hacking` for
`JELLY_STATUS_DOORS`; `hacking` for `JELLY_STATUS_HACKING_FIRE`).

## Blue Options
- **Hacking system** (`req="hacking"`) — keeps your doors, costs you your Hacking for the
  fight, and upgrades the hull-kill reward from `MED` to `HIGH`.

## Rewards & Risks
- `MED standard` (hull kill) or `HIGH standard` (crew kill) on choice 1; `HIGH standard`
  either way on choice 2.
- Risk: fire with no door control. Fires spread freely and can only be fought by crew
  standing in the burning room.
- Fandom notes that on arrival **the doors freeze in whatever state they were in before the
  jump**, unless the hack is countered ([[source-fandom-slug-hacker-doors]]) — so if you
  happened to jump in with doors open, the venting works in your favour.

## Strategy Notes
- If you have Hacking, always take choice 2 — it removes the one handicap that interacts
  badly with the enemy's guaranteed fire weapon, and pays better.
- Without Hacking: kill the weapon or the ship fast. Crew-killing pays `HIGH`, but boarding
  into a ship while your own doors are locked is its own problem.

## Related
- [[event-slug-hacker-choice]], [[event-slug-hacker-oxygen]], [[event-slug-hacker-medical]]
- [[item-hacking]], [[item-door-system]]
- [[entity-slugs]]

## Open Questions
- [ ] Whether `BEAM_FIRE` / `BOMB_FIRE` are chosen with equal probability.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-slug-hacker-doors]] (per raw/wiki/slug-hacker-doors.md)
