---
id: source-fandom-no-fuel-rebel-fleet-delay
type: source
source_kind: wiki
raw: raw/wiki/no-fuel-rebel-fleet-delay.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [out-of-fuel, rebel-fleet, odds]
---

# Fandom — "No fuel: Rebel fleet delay"

## Summary
Community wiki page for `FUEL_FLEET_DELAY`, retrieved at revision 65573. Short, but it
carries one of the two independently stated probability figures that let us validate the
uniform-selection assumption for the whole out-of-fuel family.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'FUEL_FLEET_DELAY' in the datafiles."*
- **States 9% occurrence** with the distress beacon off. The AE `NO_FUEL` list has 11
  entries and this event occupies one → 1/11 = 9.09%. The match confirms that entries in
  these `<eventList>` blocks are selected uniformly, which is the basis for every derived
  fraction across the out-of-fuel pages.
- Confirms the recursion: *"Since this event calls another event from its parent list, it is
  possible to get it recursively. The delayed jumps of the Rebel Fleet will be properly
  accumulated."*
- Lists all 7 text variants verbatim.

## Events Covered
- [[event-no-fuel-rebel-fleet-delay]]

## Other Pages Touched
- [[event-fuel-fleet-distress]] (the unreachable twin), [[concept-rebel-fleet-advance]],
  [[concept-out-of-fuel]]

## Reliability Notes
`medium`, `game_version: unknown` — but the 9% figure matches the AE list length exactly,
which is evidence the page describes Advanced Edition.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/No_fuel:_Rebel_fleet_delay
- [[source-events-fuel]], [[source-text-events-xml]]
