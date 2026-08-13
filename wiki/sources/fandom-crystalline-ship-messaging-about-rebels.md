---
id: source-fandom-crystalline-ship-messaging-about-rebels
type: source
source_kind: wiki
raw: raw/wiki/crystalline-ship-messaging-about-rebels.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [crystal-sector, blue-option, fleet-delay, fleet-advance]
---

# Fandom — "Crystalline ship messaging about Rebels"

## Summary
The community wiki page for `CRYSTAL_REQUEST`. Retrieved via the MediaWiki API at revision
74031. Documents the flight-plan trade, including the sector's only Rebel-fleet **delay**
opportunity.

## Key Takeaways
- Names the in-game id: *"This event is called 'CRYSTAL_REQUEST' in the datafiles"*.
- Distinguishes the two `modifyPursuit` directions in plain language: `amount="1"` as
  *"pursuit is doubled for 1 jump"* and `amount="-1"` as *"pursuit is delayed for 1 jump"*.
- Documents the Distraction Buoy blue option (`req="FLEET_DISTRACTION"`) as a guaranteed
  version of the good half of the lying branch.
- Records the bad half: 1–2 Crystal boarders **plus** a `CRYSTAL_SHIP_NO_SURRENDER` fight,
  matching `<boarders min="1" max="2" class="crystal"/>` and `<ship hostile="true"/>`.
- All three paying outcomes are **high scrap** (`autoReward HIGH scrap_only`).
- Location: Hidden Crystal Worlds, `unique=true`, **ship** on Long-Range Scanners.

## Events Covered
- [[event-crystalline-ship-messaging-about-rebels]]

## Other Pages Touched
- [[sector-hidden-crystal-worlds]], [[entity-crystal-men]], [[concept-rebel-fleet-advance]],
  [[item-distraction-buoys]], [[concept-rebel-fleet-advance]], [[concept-blue-options]]

## Reliability Notes
`medium`. No game version stated. Consistent with the game files. Its two pursuit phrasings
("doubled" vs "delayed") are not obviously symmetric descriptions of `+1`/`-1`, which is
recorded as an open question on the event page.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Crystalline_ship_messaging_about_Rebels
- [[source-events-xml]], [[source-text-events-xml]]
