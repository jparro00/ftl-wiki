---
id: event-rock-pirates-fight
type: event
event_name: ROCK_PIRATE
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [combat, rock, pirate, default-rewards]
---

# Rock pirates fight — `ROCK_PIRATE`

## Summary
An unavoidable fight against a Rock **pirate** ship. Mechanically identical in structure
to [[event-rock-fight]] — no choices, jump in and fight — but it loads a different enemy
ship blueprint, `SHIPS_ROCK_PIRATE`, crewed entirely by Rockmen.

## Trigger & Where It Appears
- Sectors: [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- Event list: `HOSTILE_ROCK` (allocated `min="6" max="8"` per Rock sector,
  [[source-sector-data-xml]])
- Beacon: hostile, ship present ([[source-fandom-rock-pirates-fight]], `LRSmap=ship`)
- Not `unique` — it can repeat within a sector ([[source-events-rock]])

## Text
Varies — `<text load="ROCK_PIRATE"/>` over a `textList` that names 4 distinct text ids
across 9 slots (`_1` ×2, `_2` ×3, `_3` ×3, `_4` ×1), so the variants are **not uniformly
weighted** ([[source-events-rock]]). [[source-fandom-rock-pirates-fight]] transcribes three
of them. The fourth, `text_ROCK_PIRATE_4`, is a near-duplicate of `_1` differing only in
spelling — *"intergalactic"* vs *"inter-galactic"* ([[source-text-events-xml]]) — which is
presumably why Fandom lists only three.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices)_ | — | Fight a Rock pirate ship (`<ship load="ROCK_PIRATE" hostile="true"/>`). Default rewards. | 100% |

## Blue Options
None.

## Rewards & Risks
- Victory: **default rewards** ([[source-fandom-rock-pirates-fight]]). The ship uses
  `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` and specifies no `autoReward` of its own
  ([[source-events-ships]]).
- **No surrender offer.** Unlike `ROCK_SHIP`, the `ROCK_PIRATE` ship definition has no
  `<surrender>` element — this fight goes to the end ([[source-events-rock]]).
- Crew: `<crewMember type="rock" prop="1"/>` — an all-Rockman crew, so fire and asphyxiation
  tactics are poor and boarding is dangerous ([[source-events-rock]], [[entity-rock-men]]).

## Strategy Notes
- The all-Rock crew is the practical difference from [[event-rock-fight]]: no Engi or
  human filler to pick off, and no surrender to cash in. Plan on destroying the hull.

## Related
- [[event-rock-fight]] — the non-pirate version, which *does* offer surrender
- [[event-rock-pirates-fight-in-asteroid-field]] — same fight, asteroid environment
- [[event-rock-pirates-fight-near-sun]] — same fight, solar environment
- [[entity-rock-men]]

## Open Questions
- [ ] The prose of `text_ROCK_PIRATE_4`, and whether Fandom simply missed it.
- [ ] Exact scrap values behind "default rewards" for `SHIPS_ROCK_PIRATE`.

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rock-pirates-fight]] (per raw/wiki/rock-pirates-fight.md)
