---
id: source-fandom-lanius-ship-salvager
type: source
source_kind: wiki
raw: raw/wiki/lanius-ship-salvager.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [lanius, neutral, blue-option, advanced-edition]
---

# Fandom — "Lanius ship salvager"

## Summary
Community wiki page for `LANIUS_SOLO_SALVAGE`, retrieved via the MediaWiki API at revision
74241. Transcribes all five intro variants and the three-way blue-option roll, including the
nested attack-or-leave choice on the "they scoff" branch.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'LANIUS_SOLO_SALVAGE' in the
  datafiles."*
- Location: Abandoned Sector; `LRSmap=ship`, **`unique=false`** — correctly flagging that
  the XML event carries no `unique` attribute.
- All five `LANIUS_SOLO_SALVAGE_TEXT` strings transcribed.
- Annotates the enemy as `LANIUS_SHIP` with `escape+surrender` and the parameters
  `80 | 20-40 | 2-4 | 80 | 30-40 | 3-4`, calling the payout *"default Lanius rewards"*.
- Documents the blue option's three results (medium scrap / nothing / scoffing, with an
  optional fight) without stating odds.

## Events Covered
- [[event-lanius-ship-salvager]]

## Other Pages Touched
- [[sector-abandoned-sector]], [[entity-lanius]], [[event-lanius-fight]]

## Reliability Notes
`medium`. Same unexplained `SurrenderEscape` numbers as the other `LANIUS_SHIP` pages.

## Contradictions Flagged
- *"they stop what they **are** doing"* vs the files' *"…what they **were** doing"* in one
  of the two copies of that line.
- Third intro variant transcribed with *"striped"* where the files read *"stripped"*.

Both read as transcription slips, not version differences.

## Links
- Source URL: https://ftl.fandom.com/wiki/Lanius_ship_salvager
- [[source-dlcevents-anaerobic]], [[source-text-events-xml]]
