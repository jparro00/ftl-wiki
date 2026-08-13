---
id: source-fandom-rebel-ship-attacking-federation-loyalists
type: source
source_kind: wiki
raw: raw/wiki/rebel-ship-attacking-federation-loyalists.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [distress, crew-reward, blue-option, quest, bugged]
---

# Fandom — "Rebel ship attacking Federation loyalists"

## Summary
The community wiki page for `REBEL_VS_FEDERATION`. Retrieved via the MediaWiki API at
revision 74715. It spells out the whole three-entry rescue table including all four blue
options on the dying-crew branch, names the skill points the rescued crew arrive with, and
reports the same missing-`<distressBeacon/>` bug seen on the pirate equivalent.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'REBEL_VS_FEDERATION' in the datafiles."*
- Quotes all three intro variants, matching `textList REBEL_VS_FEDERATION`.
- **Documents a bug**: *"This event is meant to occur at a distress beacon but won't because
  the `<distressBeacon/>` tag is missing in its definition."* Confirmed in
  ([[source-events-xml]]).
- Confirms the Rebel ship **never surrenders and never escapes**, and that `destroyed` and
  `deadCrew` pay the same medium scrap with resources.
- Full rescue table: hidden-base quest marker / dying crew / extra supplies.
- Names the crew skill points explicitly — shields 1 (Nano Med-bot), combat 1 (Teleporter),
  engines 1 (Healing Burst) — matching the `crewMember` attributes, all of which are
  `<!--DLC!-->`-marked in the XML.
- Gives the Nano Med-bot reward as *"high 3–6 fuel"* with scrap, which is how it renders
  `autoReward level="HIGH">fuel`; the 3–6 range does not appear in the XML.
- `unique=true`, `LRSmap=noship`.

## Events Covered
- [[event-rebel-ship-attacking-federation-loyalists]] — choices, fight, and full rescue table

## Other Pages Touched
- [[chain-hidden-federation-base]], [[item-nano-med-bot-dispersal]], [[item-teleporter]],
  [[item-healing-burst]], [[concept-rebel-fleet-advance]], [[entity-federation]],
  [[sector-civilian-sector]], [[sector-pirate-controlled-sector]],
  [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]],
  [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]],
  [[sector-uncharted-nebula]]

## Reliability Notes
`medium`. No game version stated, so `game_version: unknown`. The page describes the AE
version throughout — it lists the Healing Burst option and the crew skill points without
marking either as Advanced Edition content, though the XML marks all of them `<!--DLC!-->`.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** sector coverage — omits [[sector-federation-space]] despite
> `DISTRESS_BEACON min=1 max=2` in `STANDARD_SPACE` ([[source-sector-data-xml]]). Recorded on
> [[event-rebel-ship-attacking-federation-loyalists]]; game files trusted.

Not a contradiction but recorded under rule 10 on the event page: the page presents AE-only
content (Healing Burst branch, crew skill points) as unqualified, so the vanilla version of
the rescue branch has one fewer choice and unskilled crew.

## Links
- Source URL: https://ftl.fandom.com/wiki/Rebel_ship_attacking_Federation_loyalists
- [[source-events-xml]], [[source-text-events-xml]], [[source-events-ships]],
  [[source-sector-data-xml]]
