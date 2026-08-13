---
id: source-fandom-plagued-station
type: source
source_kind: wiki
raw: raw/wiki/plagued-station.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [slug, crew-loss-risk, clone-bay, blue-option]
---

# Fandom — "Plagued station"

## Summary
The community wiki page for the event the game files call `DONOR_PLAGUE`. Retrieved via
the MediaWiki API at revision 73783. A short page: three outcomes on the boarding branch,
one flat scrap outcome on the other.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'DONOR_PLAGUE' in the
  datafiles."* This is the join key.
- Confirms sector availability — Slug Controlled Nebula and Slug Home Nebula — plus
  `alsooccur=exitandfiller`, i.e. it can also turn up at an exit beacon and as filler when
  a sector runs out of allocated events. That matches its membership of `NEUTRAL_EXIT` /
  `OVERRIDE_NEUTRAL_EXIT` in the files ([[source-newevents]],
  [[source-dlceventsoverwrite]]).
- Marked `LRSmap=noship` — no ship at the beacon, so Long-Range Scanners show nothing.
- Renders the blue option as **Improved Medbay, level 2+**, matching `req="medbay" lvl="2"`.
- Spells out the Clone Bay interaction on the disease outcome: the `<clone>false</clone>`
  flag means the clone is **not** produced — *"[no effect]"*, the crew member is gone for
  good.
- Categorised `Random_Events`, `Unique_Events`, `Filler_Events`, `Donor Events`,
  `Crew loss risk`, `Clone Bay failed revival`, `Crew reward chance`.

## Events Covered
- [[event-plagued-station]]

## Other Pages Touched
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[item-medbay]],
  [[item-clone-bay]]

## Reliability Notes
`medium`. No game version stated. States no odds for the three-way boarding split, which
matches the files — the split is an `<eventList>` with no weights.

## Contradictions Flagged
None material. Fandom writes *"crew member"* where the files write *"crewmember"* in the
disease outcome.

## Links
- Source URL: https://ftl.fandom.com/wiki/Plagued_station
- [[source-events-xml]], [[source-text-events-xml]]
