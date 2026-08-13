---
id: source-fandom-rebel-fight-in-nebula
type: source
source_kind: wiki
raw: raw/wiki/rebel-fight-in-nebula.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [nebula, rebel, unreachable, name-collision]
---

# Fandom — "Rebel fight in nebula"

## Summary
The community wiki page for `NEBULA_REBEL`. Retrieved via the MediaWiki API at revision
74835. Seven intro-text variants, one fight — and a Trivia section claiming the event is
unreachable because an `eventList` shadows its name.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'NEBULA_REBEL' in the datafiles."*
- Locations *as written*: Civilian Sector, Pirate Controlled Sector, Rebel Controlled
  Sector, Rebel Stronghold, Uncharted Nebula, Zoltan Controlled Sector, Zoltan Homeworlds.
  `nebula=true`, `alsooccur=nebulafiller`, `LRSmap=ship+nebula`, `unique=false`.
- Transcribes all seven `text_NEBULA_REBEL_LIST_*` variants; they match `text_events.xml`.
- **The name-collision claim:** *"This event can never happen. In the files, there is an
  eventList with the same name as this event, so whenever this event would load … the game
  loads a random event from that eventList instead."* Verified structurally:
  `events_rebel.xml` line 78 defines `<eventList name="NEBULA_REBEL">`, and its eleven
  members match the list on the page.
- Consequence worth noting: every reference to `NEBULA_REBEL` inside the nebula pools
  (`NEBULA`, `NEBULA_HOSTILE`, `NEBULA_PIRATE`, `NEBULA_ZOLTAN`) becomes a **re-roll into
  a broader nebula table**, not a Rebel fight. That is why so many of these events reach
  so many sectors.
- Categorised `Fights with Default Rewards`.

## Events Covered
- [[event-rebel-fight-in-nebula]]

## Other Pages Touched
- [[event-pirate-fight-in-nebula]], [[concept-rebel-fleet-advance]], [[sector-uncharted-nebula]]

## Reliability Notes
`medium`, well-argued. The shadowing eventList is verifiable in the files; the resolution
order is engine behaviour Fandom asserts and the XML does not state.

## Contradictions Flagged
None between sources — this page is the origin of the `unreachable` tag on
[[event-rebel-fight-in-nebula]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Rebel_fight_in_nebula
- [[source-events-nebula]], [[source-events-rebel]], [[source-events-ships]],
  [[source-text-events-xml]]
