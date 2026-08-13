---
id: source-fandom-rebel-fight-choice-in-nebula
type: source
source_kind: wiki
raw: raw/wiki/rebel-fight-choice-in-nebula.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [nebula, rebel, blue-option, cloaking, engines, fleet-advance, unique]
---

# Fandom — "Rebel fight choice in nebula"

## Summary
The community wiki page for `NEBULA_REBEL_UNDETECTED`. Retrieved via the MediaWiki API at
revision 74848. Three top-level choices, with the middle one branching into a three-entry
sub-list that itself contains a nested blue option.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'NEBULA_REBEL_UNDETECTED' in the
  datafiles."*
- Locations: Civilian Sector, Pirate Controlled Sector, Rebel Controlled Sector, Rebel
  Stronghold, Slug Controlled Nebula, Slug Home Nebula, Uncharted Nebula, Zoltan
  Controlled Sector, Zoltan Homeworlds. `nebula=true`, `alsooccur=nebulafiller`,
  `LRSmap=ship+nebula`, `unique=true`.
- Correctly nests the **Engines level 4+** blue option *inside* the "spotted" branch of
  the concealment sub-list, rather than presenting it as a top-level choice. Matches
  `NEBULA_REBEL_UNDETECTED_LIST` entry 1.
- Top-level **Cloaking** blue option: clean escape, nothing happens.
- Sub-list entry 3: *"Rebel Fleet pursuit is doubled for 1 jump."* — the wiki's reading of
  `<modifyPursuit amount="1"/>`. Note this page adds *"for 1 jump"*, which the sibling
  pages ([[source-fandom-auto-ship-warning-in-nebula]],
  [[source-fandom-rebel-fight-chance-in-nebula]]) omit for the same XML element.
- Categorised `Fights with Default Rewards`, `Rebel Fleet advancement risk`.

## Events Covered
- [[event-rebel-fight-choice-in-nebula]]

## Other Pages Touched
- [[item-cloaking]], [[item-engines]], [[concept-rebel-fleet-advance]],
  [[concept-rebel-fleet-advance]], [[sector-uncharted-nebula]]

## Reliability Notes
`medium`. Version unstated. The choice tree is faithful to the XML; the pursuit gloss is
interpretation.

## Contradictions Flagged
- Internal to Fandom: the same `modifyPursuit amount="1"` is glossed as "doubled" on two
  sibling pages and "doubled for 1 jump" here. Recorded on
  [[event-rebel-fight-choice-in-nebula]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Rebel_fight_choice_in_nebula
- [[source-events-nebula]], [[source-events-ships]], [[source-text-events-xml]]
