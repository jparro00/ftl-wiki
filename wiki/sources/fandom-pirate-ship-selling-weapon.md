---
id: source-fandom-pirate-ship-selling-weapon
type: source
source_kind: wiki
raw: raw/wiki/pirate-ship-selling-weapon.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [nebula, pirate, trading, blue-option, mind-control, scrap-risk, unique]
---

# Fandom — "Pirate ship selling weapon"

## Summary
The community wiki page for `NEBULA_WEAPONS_TRADER`. Retrieved via the MediaWiki API at
revision 74701. Fully enumerates the 45-scrap purchase gamble and the Mind Control branch,
including the nested buy/decline choices.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'NEBULA_WEAPONS_TRADER' in the
  datafiles."*
- Locations: Civilian Sector, Slug Controlled Nebula, Slug Home Nebula, Uncharted Nebula.
  `nebula=true`, `alsooccur=nebulafiller`, `LRSmap=ship+nebula`, `unique=true`.
- Purchase branch (`NEBULA_WEAPONS_TRADER_LIST`): two outcomes — weapon for 45 scrap, or
  **scrap taken and no weapon**, then attack/leave. Matches the XML.
- **Key warning, not derivable from the XML alone:** *"If the trader cheated you, the lost
  45 scrap won't be refunded even if you then attack and win the fight against him."*
- Mind Control branch (`NEBULA_WEAPONS_TRADER_LIST2`): the "better deal" is illusory — the
  text has him retract the discount, and the page's transaction still shows 45 scrap. The
  other half of the branch is an ambush.
- Enemy `PIRATE` ship annotation: *"50% chance to offer a surrender at 30-40% hull and/or
  50% chance for escape attempt at 20-40% hull"*, hedged on the page itself as an
  approximation of `<surrender chance="0.5" min="3" max="4">` /
  `<escape chance="0.5" min="2" max="4">`.
- Categorised `Fights with Default Rewards`, `Scrap loss risk`, `Trading Events`,
  `Weapon reward chance`, `Pirate ship fights`.

## Events Covered
- [[event-pirate-ship-selling-weapon]]

## Other Pages Touched
- [[item-mind-control]], [[sector-uncharted-nebula]], [[sector-slug-home-nebula]],
  [[concept-scrap-economy]]

## Reliability Notes
`medium`. Version unstated, but it documents the Mind Control option, which is AE-only
(`<!--DLC-->` in the XML), so it describes at least an AE build.

## Contradictions Flagged
- Fandom lists four sectors; the event lists (`NEBULA`, `NEBULA_NEUTRAL`,
  `NEBULA_NEUTRAL_SLUG`) reach five, adding Federation Space. Recorded on
  [[event-pirate-ship-selling-weapon]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Pirate_ship_selling_weapon
- [[source-events-nebula]], [[source-events-ships]], [[source-events-slug]],
  [[source-text-events-xml]]
