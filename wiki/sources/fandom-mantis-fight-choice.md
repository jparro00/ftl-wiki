---
id: source-fandom-mantis-fight-choice
type: source
source_kind: wiki
raw: raw/wiki/mantis-fight-choice.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [mantis, blue-option, cloaking, optional-fight]
---

# Fandom — "Mantis fight choice"

## Summary
The community wiki page for `MANTIS_FIGHT_CHOICE`. Retrieved via the MediaWiki API at
revision 74255. Documents the three choices and — usefully — flags which outcome branches
have duplicate entries in their event list.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'MANTIS_FIGHT_CHOICE' in the
  datafiles."*
- Locations: Engi Controlled Sector, Engi Homeworlds, Mantis Controlled Sector, Mantis
  Homeworlds; `LRSmap=ship`, `unique=false`.
- Marks the Cloaking option with the `{{Blue Option|Cloaking}}` template — confirming
  it is a system gate, not a crew gate. The files add the detail Fandom omits: `lvl="1"`,
  i.e. merely having Cloaking installed suffices.
- Uses `{{DuplicateEvent|2}}` on the fight branch of "Attempt to remain concealed" and on
  the escape branch of "Cloak to stay hidden" — an explicit statement that those branches
  occupy **two of three** list slots. This is the same structure visible in
  `MANTIS_FIGHT_CHOICE_AVOID` and `MANTIS_FIGHT_CHOICE_CLOAK`, and it is the closest
  thing to odds that either source provides. Neither gives percentages.
- Transcribes all six intro variants and all six outcome texts verbatim; they match
  `text_events.xml`.
- Categorised `Random_Events`, `Fights with Default Rewards`.

## Events Covered
- [[event-mantis-fight-choice]]

## Other Pages Touched
- [[item-cloaking]], [[entity-mantis]], [[sector-mantis-controlled-sector]],
  [[sector-mantis-homeworlds]], [[sector-engi-controlled-sector]],
  [[sector-engi-homeworlds]]

## Reliability Notes
`medium`. Version unstated. Its `DuplicateEvent` annotations agree exactly with the event
list contents in `events_mantis.xml`, which is good corroboration for how that template
should be read on other pages.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Mantis_fight_choice
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
