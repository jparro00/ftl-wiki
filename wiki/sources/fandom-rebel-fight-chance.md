---
id: source-fandom-rebel-fight-chance
type: source
source_kind: wiki
raw: raw/wiki/rebel-fight-chance.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, sensors, blue-option, fleet-advance-risk]
---

# Fandom — "Rebel fight chance"

## Summary
Documents the rogue-Rebel hunt: four intro variants, the search sub-list, and the two
Sensors blue options. Declares the datafile id: **"This event is called `ROGUE_REBEL` in
the datafiles."** Includes a screenshot of the disabled-engines enemy ship.

## Key Takeaways
- Marks the "you find him" search result as a **duplicate entry** (`{{DuplicateEvent|2}}`)
  — two of the four search-list members are functionally the same fight.
- The slow-search result doubles Rebel Fleet pursuit for one jump.
- Sensors 2 gives a clean fight; Sensors 3 gives a fight against a ship whose engines are
  permanently disabled.

## Events Covered
- [[event-rebel-fight-chance]] (`ROGUE_REBEL`)

## Other Pages Touched
- [[item-sensors]], [[entity-rebels]], [[concept-rebel-fleet-advance]]

## Contradictions Flagged
- Fandom describes the pursuit penalty as "doubled for 1 jump"; the XML says
  `<modifyPursuit amount="1"/>`. Recorded on the event page.
- Fandom does not mark the Sensors-2 choice as hidden, matching the XML (no
  `hidden="true"` on that choice).

## Links
- https://ftl.fandom.com/wiki/Rebel_fight_chance (revision 74743, retrieved 2026-08-09)
