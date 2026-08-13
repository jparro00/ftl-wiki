---
id: source-fandom-pirate-fight-in-nebula
type: source
source_kind: wiki
raw: raw/wiki/pirate-fight-in-nebula.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [nebula, pirate, unreachable, name-collision]
---

# Fandom — "Pirate fight in nebula"

## Summary
The community wiki page for `NEBULA_PIRATE`. Retrieved via the MediaWiki API at revision
74833. The Trivia section is the substantive part: it argues the event **can never
happen** because an `eventList` shares its name.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'NEBULA_PIRATE' in the datafiles."*
- Locations *as written*: Pirate Controlled Sector, Uncharted Nebula. `nebula=true`,
  `LRSmap=ship+nebula`, `unique=false`.
- Transcribes all five `text_NEBULA_PIRATE_*` variants; they match `text_events.xml`.
- **The name-collision claim:** *"This event can never happen. In the files, there is an
  eventList with the same name as this event, so whenever this event would load … the
  game loads a random event from that eventList instead."* It then lists the eventList's
  members. This checks out structurally — `events_pirate.xml` line 87 does define
  `<eventList name="NEBULA_PIRATE">`, and its members are exactly the ones listed.
- It makes the same claim for `NEBULA_REBEL`, which likewise has both an event
  (`events_nebula.xml`) and an eventList (`events_rebel.xml`).
- **Missing environment tag:** *"although the beacon is in a nebula on the map, the nebula
  environment will be missing upon arrival due to a missing environment tag."* Confirmed —
  the `NEBULA_PIRATE` event in `events_nebula.xml` is the only nebula event in that file
  with no `<environment type="nebula"/>`.
- Categorised `Fights with Default Rewards`, `Pirate ship fights`.

## Events Covered
- [[event-pirate-fight-in-nebula]]

## Other Pages Touched
- [[event-rebel-fight-in-nebula]], [[sector-pirate-controlled-sector]],
  [[sector-uncharted-nebula]]

## Reliability Notes
`medium`, but unusually well-argued. The existence of the shadowing eventList is verifiable
in the game files; the *resolution order* (eventList wins over event) is engine behaviour
the XML does not state, so that half rests on Fandom's authority alone.

## Contradictions Flagged
None between sources — but this page is the origin of the `unreachable` tag on
[[event-pirate-fight-in-nebula]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Pirate_fight_in_nebula
- [[source-events-nebula]], [[source-events-pirate]], [[source-events-ships]],
  [[source-text-events-xml]]
