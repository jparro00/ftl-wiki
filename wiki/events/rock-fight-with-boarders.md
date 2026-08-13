---
id: event-rock-fight-with-boarders
type: event
event_name: ROCK_BOARDERS_SHIP
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [combat, rock, boarders, crew-risk, default-rewards, unique]
---

# Rock fight with boarders — `ROCK_BOARDERS_SHIP`

## Summary
The nastiest of the plain Rock beacons: you fight a Rock ship **and** 1–3 Rockmen
teleport aboard on arrival, before you have done anything. No choices, no warning, no way
to decline. Rockmen are the hardest boarders in the game to remove — high HP, immune to
fire — so this event is a crew-loss risk even for a healthy ship.

## Trigger & Where It Appears
- Sectors: [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- Event list: `BOARDERS_ROCK`, allocated `min="1" max="2"` in both Rock sector
  definitions — so **1–2 boarding beacons are guaranteed per Rock sector**, drawn from
  this event and its two siblings ([[source-sector-data-xml]], per
  `raw/gamedata/sector_data.xml`)
- Beacon: hostile, ship present ([[source-fandom-rock-fight-with-boarders]],
  `LRSmap=ship`)
- `unique="true"` — at most once per sector ([[source-events-rock]])

## Text
Varies — `<text load="ROCK_BOARDERS_SHIP"/>` over a two-entry `textList`
([[source-events-rock]]): a Rock station that resents being scanned and launches a ship
plus a teleport, or a Rock ship docked with a damaged Mantis fighter that boards you
*using captured Mantis tech*. Both are transcribed on
[[source-fandom-rock-fight-with-boarders]].

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices)_ | — | `<boarders min="1" max="3" class="rock"/>` — 1–3 Rockmen board immediately — **and** `<ship load="ROCK_SHIP" hostile="true"/>`. Default rewards on victory. | 100% |

The boarder count is a uniform-looking `min`/`max` pair; the game files give no
distribution over 1, 2 or 3 ([[source-events-rock]]).

## Blue Options
None. There is no system, augment or crew requirement anywhere on this event — nothing
lets you pre-empt the teleport.

## Rewards & Risks
- Victory: **default rewards** for a Rock ship
  ([[source-fandom-rock-fight-with-boarders]]).
- The enemy is `ROCK_SHIP`, so the `<surrender chance="0.7" min="3" max="4">` branch can
  fire — see [[event-rock-fight]]. **Accepting surrender does not remove boarders already
  aboard**; nothing in the sources says it does, and the boarders are your problem either
  way.
- Risk: up to 3 Rockman boarders. Per [[entity-rock-men]] they are fire-immune, so
  venting-and-burning is off the table; you are fighting them with crew, drones, or by
  suffocating them in a vented room.

## Strategy Notes
- The 1–2 guaranteed `BOARDERS_ROCK` beacons per Rock sector mean you should not enter a
  Rock sector with a skeleton crew and no answer to boarders
  ([[source-sector-data-xml]]).
- Of the three `BOARDERS_ROCK` events, this one is the middle case: fewer boarders than
  [[event-boarders-rockmen-near-sun]] at the low end, but unlike that event it *also*
  gives you a hostile ship to deal with simultaneously.

## Related
- [[event-rock-fight-with-boarders-in-asteroid-field]] — 1–2 boarders, asteroid hazard
- [[event-boarders-rockmen-near-sun]] — 2–3 boarders, **no ship**
- [[event-rock-fight]] — the same enemy ship without the teleport
- [[entity-rock-men]], [[item-teleporter]], [[concept-blue-options]]

## Open Questions
- [ ] Whether the 1–3 boarder roll is uniform.
- [ ] Whether accepting the Rock ship's surrender has any effect on boarders already aboard.

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rock-fight-with-boarders]] (per raw/wiki/rock-fight-with-boarders.md)
