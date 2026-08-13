---
id: source-fandom-lanius-lone-ship
type: source
source_kind: wiki
raw: raw/wiki/lanius-lone-ship.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [lanius, neutral, blue-option, store, advanced-edition]
---

# Fandom — "Lanius lone ship"

## Summary
Community wiki page for `LANIUS_SCARED_CIVILIAN`, retrieved via the MediaWiki API at
revision 74229. Documents the four top-level choices, the three-way `LANIUS_SCARED_CIVILIAN_LIST`
roll behind the "contact them" branch, and the Lanius blue option that opens a store
outright.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'LANIUS_SCARED_CIVILIAN' in the
  datafiles."*
- Location: Abandoned Sector; `LRSmap=ship`, `unique=true`.
- Annotates the enemy as `LANIUS_SHIP` with `escape+surrender` and the parameters
  `80 | 20-40 | 2-4 | 80 | 30-40 | 3-4`, citing `dlcEvents_anaerobic.xml`, and calls the
  payout *"default Lanius rewards"*.
- Transcribes all three list outcomes (store / translator failure / forced fight) without
  stating odds.
- Categorised *Advanced Edition Content Events*, *Fights with Default Rewards (Lanius)*,
  *Store Opening opportunity*.

## Events Covered
- [[event-lanius-lone-ship]]

## Other Pages Touched
- [[sector-abandoned-sector]], [[entity-lanius]], [[event-lanius-fight]],
  [[concept-blue-options]]

## Reliability Notes
`medium`. Its `SurrenderEscape` numbers (`80`, `20-40`, `2-4`) do not map obviously onto the
XML's `chance="0.2"` and crew `min`/`max` for `LANIUS_SHIP`; see [[event-lanius-fight]],
which records the same discrepancy.

## Contradictions Flagged
- Blue-option flavour text is smoothed: *"connections with other sentient races"* and
  *"ask to see if they are selling anything"* against the files' *"connections with the
  other sentient races"* and *"ask if they are selling anything"*. Cosmetic.

## Links
- Source URL: https://ftl.fandom.com/wiki/Lanius_lone_ship
- [[source-dlcevents-anaerobic]], [[source-text-events-xml]]
