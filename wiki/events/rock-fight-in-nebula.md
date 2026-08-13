---
id: event-rock-fight-in-nebula
type: event
event_name: NEBULA_ZOLTAN_ROCK
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: nebula
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, nebula, default-rewards, forced-fight, rock]
---

# Rock fight in nebula — `NEBULA_ZOLTAN_ROCK`

## Summary
Rock refugees hiding from the Zoltan border police open fire rather than let you leave
with their position. No choices, default rewards. The one thing that sets it apart from
the sector's other filler fights is that it happens **inside a nebula**, so sensors are
down and your FTL charges slowly.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: **nebula** (`<environment type="nebula"/>`). Long-Ranged Scanners show a ship
  plus a nebula ([[source-events-zoltan]], [[source-fandom-rock-fight-in-nebula]]).
- Reached via the `NEBULA_ZOLTAN` event list, allocated `min=2 max=6` beacons in both
  Zoltan sectors ([[source-sector-data-xml]]).
- `unique="true"` — at most once per sector.

## Text
> This nebula turns out to be the hiding place of a terrified rock crew taking refuge
> from the Zoltan border police. They don't seem prepared to risk your leaving with their
> co-ordinates, and open fire!

(`event_NEBULA_ZOLTAN_ROCK_text`, per [[source-text-events-xml]])

The Rock crew hiding from the **Zoltan border police** is a direct narrative link to
[[event-zoltan-border-police]], which is the same police force boarding you.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `<ship load="ROCK_SHIP" hostile="true"/>` in a nebula — fight a Rock ship ([[entity-rock-men]]), **default rewards**. | 100% |

## Blue Options
None. There is no option to reassure them or promise silence — the event resolves
directly to combat.

## Rewards & Risks
- **Rewards:** default rewards for a Rock ship at the current sector depth. No bonus for
  the nebula.
- **Risks:**
  - **Nebula rules apply:** sensors are disabled (you cannot see inside the enemy ship,
    and they cannot see inside yours) and FTL charge is slowed, so disengaging is harder
    than usual.
  - Rock ships are the tankiest hulls in the game and are immune to fire, removing an
    entire damage strategy.
- No boarders or scripted system damage.

## Strategy Notes
- *Opinion:* the worst combination in the sector's nebula pool for a slow-damage build —
  a high-HP hull you must chew through, with a slowed FTL so you cannot cut losses
  quickly. Prefer high burst damage here.
- Rockmen crew are fire-immune and tough in melee, so boarding for the crew-kill tier is
  a poor idea unless your party is strong.
- Sensors being down cuts both ways: the enemy AI cannot target your crew positions
  either.

## Related
- [[event-zoltan-great-eye]], [[event-pirate-ships-in-plasma-storm]] — the other unique
  `NEBULA_ZOLTAN` members
- [[event-zoltan-border-police]] — the border police this crew is hiding from
- [[entity-rock-men]] — the opponent
- [[concept-nebula-mechanics]] — the environment rules

## Open Questions
- [ ] `ROCK_SHIP` blueprint loadout by sector depth.
- [ ] Surrender/escape behaviour of `ROCK_SHIP` in this event.

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rock-fight-in-nebula]] (per raw/wiki/rock-fight-in-nebula.md)
