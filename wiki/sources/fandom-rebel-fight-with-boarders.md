---
id: source-fandom-rebel-fight-with-boarders
type: source
source_kind: wiki
raw: raw/wiki/rebel-fight-with-boarders.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, boarding, default-rewards]
---

# Fandom — "Rebel fight with boarders"

## Summary
The community wiki page for `BOARDERS_REBEL_SHIP`. Retrieved via the MediaWiki API at
revision 73811. A transcription of the four-string intro list plus a one-line outcome.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'BOARDERS_REBEL_SHIP' in the
  datafiles."*
- Locations: Rebel Controlled Sector, Rebel Stronghold. `LRSmap=ship`, `unique=false` —
  matching the file, which sets `unique="false"` on the text list and declares no `unique`
  on the event.
- Transcribes all **four** `text_BOARDERS_REBEL_SHIP_*` variants; they match
  `text_events.xml`.
- Outcome: *"2-3 human boarders beam aboard your ship, and you fight a Rebel ship (default
  rewards)."* — matches `<boarders min="2" max="3" class="human"/>` and
  `<ship load="REBEL" hostile="true"/>` exactly.
- Categorised `Random_Events`, `Fights with Default Rewards`, `Boarding hazard`.

## Events Covered
- [[event-rebel-fight-with-boarders]]

## Other Pages Touched
- [[event-rebel-fight]], [[concept-rebel-fleet-advance]], [[sector-rebel-controlled-sector]],
  [[sector-rebel-stronghold]]

## Reliability Notes
`medium`. Version unstated. Fully consistent with the game files on everything it states;
it does not mention the `REBEL` ship's surrender/escape branches.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Rebel_fight_with_boarders
- [[source-events-rebel]], [[source-events-ships]], [[source-text-events-xml]]
