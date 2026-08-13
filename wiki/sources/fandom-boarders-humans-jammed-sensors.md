---
id: source-fandom-boarders-humans-jammed-sensors
type: source
source_kind: wiki
raw: raw/wiki/boarders-humans-jammed-sensors.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [pirate, zoltan, boarding-hazard, hacking, system-malfunction]
---

# Fandom — "Boarders: Humans jammed sensors"

## Summary
Community wiki page for `BOARDERS_HACKING`, retrieved via the MediaWiki API at revision
74289. Short, but its Notes section carries three runtime behaviours the game files cannot
express.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'BOARDERS_HACKING' in the datafiles."*
- Locations: Pirate Controlled Sector, Zoltan Controlled Sector, Zoltan Homeworlds;
  `LRSmap=noship`, `unique=true` — matching the live `BOARDERS_PIRATE` and `BOARDERS_ZOLTAN`
  allocations. It omits Federation Space, whose only route is the dead `HOSTILE_BOARDING`
  list.
- Confirms 3–5 human boarders on **both** branches, matching the `<boarders>` tag's position
  before the choices in the file.
- **Three behavioural notes not derivable from the data:**
  - *"If you don't counter the jam, the Sensors functionality is not restored till you jump
    to another beacon."* — this is the practical meaning of
    `<status type="limit" target="player" system="sensors" amount="0"/>`.
  - *"If you counter the jam, the Hacking system is not disabled."* — i.e. the blue option is
    free, which the absence of any `item_modify` in the branch supports.
  - *"The event texts are unaltered when you don't have Sensors subsystem."*
- Presents the Hacking option without marking it as Advanced Edition content, although the
  file tags it `<!--DLC - added -->`.

## Events Covered
- [[event-boarders-humans-jammed-sensors]]

## Other Pages Touched
- [[event-boarders-humans-pirate]], [[item-hacking]], [[sector-zoltan-controlled-sector]],
  [[sector-pirate-controlled-sector]]

## Reliability Notes
`medium`. No version stated. It documents the AE-only Hacking blue option as if it were
always present, which is a mild signal that the page describes Advanced Edition.

## Contradictions Flagged
None on outcomes. The unmarked AE-only blue option is recorded as a version difference on
[[event-boarders-humans-jammed-sensors]], not as a conflict.

## Links
- Source URL: https://ftl.fandom.com/wiki/Boarders:_Humans_jammed_sensors
- [[source-events-xml]], [[source-events-pirate]], [[source-events-zoltan]], [[source-sector-data-xml]]
