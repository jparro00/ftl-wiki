---
id: source-fandom-zoltan-research-facility
type: source
source_kind: wiki
raw: raw/wiki/zoltan-research-facility.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [crystal-route, ship-unlock, blue-option]
---

# Fandom — "Zoltan research facility"

## Summary
The community wiki page for the event the game files call `ZOLTAN_CREW_STUDY`, step 2 of
[[chain-crystal-cruiser-unlock]]. Retrieved via the MediaWiki API at revision 74726. It
transcribes every branch including the Stasis Pod chain, and adds several engine and
allocation details the XML does not carry.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'ZOLTAN_CREW_STUDY' in the
  datafiles."* This is the join key.
- States the chain position outright: *"This event is the **2nd** step in the process of
  unlocking the Crystal Cruiser and the Ancestry achievement while using the Rock
  Cruiser."*
- Marks the duplicated `ZOLTAN_CREW_STUDY_LIST` entry with `{{DuplicateEvent|2}}` — the
  same reading of the file that [[concept-event-list-weighting]] licenses, i.e. 2/3
  peaceful, 1/3 ambush.
- Records that `PIRATE_ZOLTAN_CREW_STUDY` *"doesn't surrender, nor tries to escape"* —
  confirmed by the absence of `<surrender>` and `<escape>` on its ship block
  ([[source-events-ships]]).
- **Allocation detail only this source has:** one beacon per Zoltan sector (matching
  `min="1" max="1"` in `sector_data.xml`) but **one or two** per Engi sector, from
  observation. The XML gives no Engi count.
- **Two engine details only this source has:**
  1. the Rock Homeworlds quest marker persists only *"as long as Ruwen stays alive"*;
  2. the `stuff` reward component *"will never give a bonus weapon, drone schematic or
     augmentation, due to its interaction with a guaranteed weapon/drone schematic
     reward"*.
- Notes that a single Engi sector can supply both step 1 (the Damaged Stasis Pod, from
  [[event-dense-asteroid-field-distress]]) and step 2 of the chain.
- Categorised: `Random_Events`, `Ship_Unlocking_Events`, `Events with Quest Markers`, plus
  crew-reward / drone-schematic / boarding-risk / stuff-reward categories.

## Events Covered
- [[event-zoltan-research-facility]]

## Other Pages Touched
- [[chain-crystal-cruiser-unlock]], [[event-ancient-device]],
  [[event-dense-asteroid-field-distress]], [[item-damaged-stasis-pod]],
  [[sector-rock-homeworlds]], [[entity-crystal-men]]

## Reliability Notes
`medium`. No game version stated, so `game_version` is `unknown`. Every mechanical claim on
the page that can be checked against `events.xml` / `events_ships.xml` checks out, which
raises confidence in the three claims that cannot be — the Engi-sector count, the Ruwen
survival condition, and the `stuff` reward interaction.

## Contradictions Flagged
None. The page and the game files agree on every value that both state.

## Links
- Source URL: https://ftl.fandom.com/wiki/Zoltan_research_facility
- [[source-events-xml]], [[source-text-events-xml]], [[source-events-ships]],
  [[source-sector-data-xml]]
</content>
