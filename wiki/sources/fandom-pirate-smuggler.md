---
id: source-fandom-pirate-smuggler
type: source
source_kind: wiki
raw: raw/wiki/pirate-smuggler.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [nebula, pirate, blue-option, weapons, fuel-reward, escape]
---

# Fandom — "Pirate smuggler"

## Summary
The community wiki page for `NEBULA_PIRATE_SMUGGLE`. Retrieved via the MediaWiki API at
revision 73780. Three choices, one nested pair under the Weapons blue option, plus a
dedicated section on the `PIRATE_SMUGGLE` enemy ship.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'NEBULA_PIRATE_SMUGGLE' in the
  datafiles."*
- Locations: Civilian Sector, Pirate Controlled Sector, Uncharted Nebula. `nebula=true`,
  `alsooccur=nebulafiller`, `LRSmap=noship+nebula`, `unique=false`.
- Blue option is **Weapon Control level 6+**, matching `req="weapons" lvl="6"`.
- Bribe reward: *"medium (2-4 fuel) fuel and scrap"*. The XML says
  `autoReward level="MED">fuel`; the 2–4 figure is Fandom's own expansion of what a MED
  fuel reward pays, not something the event states.
- **Enemy ship annotations** (the useful part): `PIRATE_SMUGGLE` *"starts to escape at
  30-40% hull with 35 seconds countdown timer"* and *"has 50% chance to surrender at
  20-40% hull"*. The XML gives `<escape timer="35" min="3" max="4">` and
  `<surrender chance="0.5" min="2" max="4">` — so the percentages are Fandom's conversion
  of raw hull thresholds, not literal file values.
- Surrender payout: *"a random amount of resources with some scrap"* =
  `autoReward level="RANDOM">stuff`.
- The destroyed/dead-crew loot tables are behind a
  `{{Pirate Smuggler / Rebel Transport}}` template that this dump does not expand.
- Categorised `Ship escape Events`, `Fuel reward opportunity`, `Pirate ship fights`.

## Events Covered
- [[event-pirate-smuggler]]

## Other Pages Touched
- [[item-weapon-control]], [[sector-uncharted-nebula]], [[sector-civilian-sector]]

## Reliability Notes
`medium`. Version unstated. Its hull-percentage figures are explicitly hedged on the page
itself as approximations of in-game values adjusted by sector progression — treat the raw
XML min/max as canonical and these as gloss.

## Contradictions Flagged
- Fandom lists three sectors; the event lists (`NEBULA`, `NEBULA_NEUTRAL`, `NEBULA_PIRATE`)
  reach four, adding Federation Space. Recorded on [[event-pirate-smuggler]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Pirate_smuggler
- [[source-events-nebula]], [[source-events-ships]], [[source-events-rebel]],
  [[source-text-events-xml]]
