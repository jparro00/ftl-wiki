---
id: source-fandom-crystalline-research-facility
type: source
source_kind: wiki
raw: raw/wiki/crystalline-research-facility.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [crystal-sector, blue-option, crew-risk, weapon-reward]
---

# Fandom — "Crystalline research facility"

## Summary
The community wiki page for `CRYSTAL_HUMAN_TESTS`. Retrieved via the MediaWiki API at
revision 74030. Maps both sub-event lists and both blue options.

## Key Takeaways
- Names the in-game id: *"This event is called 'CRYSTAL_HUMAN_TESTS' in the datafiles"*.
- **"Despite the peculiar event name, there is nothing in the code that checks if you have
  a Human crewmember."** Confirmed against the raw event, which carries no `req="human"`.
- Quantifies the MED "stuff" reward as fuel 2–4, missiles 2–4, drone parts 1, with scrap.
- Confirms the Clone Bay **does** revive the crew member killed in the accept branch,
  matching `<clone>true</clone>`.
- Documents both blue options — Rock crewmember (`req="rock"`) and Backup DNA Bank
  (`req="BACKUP_DNA"`) — and correctly distinguishes their rewards (medium standard vs a
  weapon with medium scrap), matching `autoReward MED standard` and `autoReward MED
  weapon`.
- Records that refusing carries a 1-in-3 ambush by a `CRYSTAL_SHIP_NO_SURRENDER`.
- Location: Hidden Crystal Worlds, `unique=true`, **no ship** on Long-Range Scanners.

## Events Covered
- [[event-crystalline-research-facility]]

## Other Pages Touched
- [[sector-hidden-crystal-worlds]], [[entity-crystal-men]], [[entity-rock-men]],
  [[item-backup-dna-bank]], [[concept-blue-options]]

## Reliability Notes
`medium`. No game version stated. Structurally accurate; one word of intro text differs
from the shipped string.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** intro wording.
> Fandom: *"I'm curious about your physiology"*. Game files: *"I'm **really** curious about
> your physiology"* ([[source-text-events-xml]]).
> Recorded on [[event-crystalline-research-facility]]. Game files trusted; cosmetic, and
> most likely a transcription slip rather than a version difference.

## Links
- Source URL: https://ftl.fandom.com/wiki/Crystalline_research_facility
- [[source-events-xml]], [[source-text-events-xml]]
