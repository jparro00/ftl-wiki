---
id: source-fandom-zoltan-free-map
type: source
source_kind: wiki
raw: raw/wiki/zoltan-free-map.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [zoltan, map-reveal, no-risk]
---

# Fandom — "Zoltan free map"

## Summary
The community wiki page for `ZOLTAN_FREE_MAP`. Retrieved via the MediaWiki API at
revision 73909. A one-line event and a one-line page.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'ZOLTAN_FREE_MAP' in the
  datafiles."*
- Confirms the reward: **the current sector map is revealed**, matching `<reveal_map/>`.
- Locations template gives Long-Ranged Scanners `ship` — consistent with the game file's
  `<ship load="ZOLTAN_SHIP" hostile="false"/>`, a friendly ship that never becomes
  hostile. Useful corroboration that a "ship detected" reading in a Zoltan sector is not
  automatically a fight.
- `unique=true`, both Zoltan sectors.
- Categorised `Beacon Map reveal reward`.

## Events Covered
- [[event-zoltan-free-map]]

## Other Pages Touched
- [[item-long-ranged-scanners]], [[entity-zoltan]]

## Reliability Notes
`medium`. States no game version. Does not mention the non-hostile ship in prose — only
implicitly, through the `LRSmap=ship` template parameter.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Zoltan_free_map
- [[source-events-zoltan]], [[source-text-events-xml]]
