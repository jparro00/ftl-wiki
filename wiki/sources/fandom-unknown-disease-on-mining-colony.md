---
id: source-fandom-unknown-disease-on-mining-colony
type: source
source_kind: wiki
raw: raw/wiki/unknown-disease-on-mining-colony.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [distress, blue-option, crew-loss-risk, clone-bay-failed-revival, weapon-reward]
---

# Fandom — "Unknown disease on mining colony"

## Summary
Community wiki page for `DISTRESS_STATION_DISEASE`, retrieved via the MediaWiki API at
revision 73904. Complete on outcomes, including the stacked Medbay → Engi Med-bot Dispersal
branch.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'DISTRESS_STATION_DISEASE' in the
  datafiles."*
- Locations: Civilian Sector, Mantis ×2, Pirate, Rock ×2, Uncharted Nebula; `distress=true`,
  `LRSmap=noship`, `unique=true` — matching the four `DISTRESS_BEACON_*` memberships.
- Marks the Clone Bay line explicitly as **`[no effect]`**, which is the practical reading of
  `<clone>false</clone>` — the crewmember is alive on the station, so no clone is made. This
  is the only event in the batch where the flag is `false`, and the page is the reason we can
  be confident about what that means in play.
- Records the Adv. Medbay gate as `level=2+` and the Engi Med-bot Dispersal option as nested
  **inside** it, matching `req="medbay" lvl="2"` wrapping `req="NANO_MEDBAY"`.
- Gives numeric readings for `MED stuff` (fuel 2–4, missiles 2–4, 1 drone part) that the
  files do not state.
- Confirms all four gates pay `MED stuff` and only the augment branch pays `HIGH weapon`.

## Events Covered
- [[event-unknown-disease-on-mining-colony]]

## Other Pages Touched
- [[item-medbay]], [[item-engi-med-bot-dispersal]], [[entity-rock-men]], [[entity-engi]],
  [[event-giant-alien-spiders]]

## Reliability Notes
`medium`. No version stated. The event has no DLC-marked tags, so nothing turns on it except
whether a Clone Bay exists at all.

## Contradictions Flagged
None. Every choice, gate and reward level matches the game files.

## Links
- Source URL: https://ftl.fandom.com/wiki/Unknown_disease_on_mining_colony
- [[source-events-xml]], [[source-newevents]], [[source-blueprints]], [[source-sector-data-xml]]
