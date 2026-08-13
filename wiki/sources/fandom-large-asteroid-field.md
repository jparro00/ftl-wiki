---
id: source-fandom-large-asteroid-field
type: source
source_kind: wiki
raw: raw/wiki/large-asteroid-field.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [filler, blue-option, asteroid-field, scrap-recovery-arm]
---

# Fandom — "Large asteroid field"

## Summary
Community wiki page for `ASTEROID_EXPLORE`, retrieved via the MediaWiki API at revision
74247. Categorised as a Filler Event. Lists all six outcomes of the exploration roll plus the
Scrap Recovery Arm blue option.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'ASTEROID_EXPLORE' in the datafiles."*
- Locations: Abandoned Sector, Civilian Sector, Engi ×2, Pirate, Slug ×2, Zoltan ×2, with
  `alsooccur=exitandfiller` — matching the event's membership in `NEUTRAL`,
  `NEUTRAL_CIVILIAN`, `NEUTRAL_EXIT`, `NEUTRAL_ENGI`, `NEUTRAL_PIRATE`, `NEUTRAL_ZOLTAN`,
  `NEUTRAL_LANIUS` and the two `OVERRIDE_NEUTRAL*` fallbacks.
- **Two claims worth keeping**, both confirmed by the files:
  - the same outcome list is reachable from the out-of-fuel *Explore the system* event
    (`FUEL_EXPLORE_LIST` loads `ASTEROID_EXPLORE_RESULTS` in `events_fuel.xml`) **but
    without** the blue option, which sits on the parent event;
  - it is *"the only event to utilize Scrap Recovery Arm as a blue option tool"* — no other
    `req="SCRAP_COLLECTOR"` appears in the files examined for this batch.
- Gives numeric readings for the reward levels (3–6 fuel, 2–4 missiles, 1 drone part) that
  the game files do not state.
- Names the `PIRATE` enemy ship and its 50/50 surrender and escape values.

## Events Covered
- [[event-large-asteroid-field]]

## Other Pages Touched
- [[event-no-fuel-explore-the-system]], [[item-scrap-recovery-arm]],
  [[event-pirate-fight-in-asteroid-field]]

## Reliability Notes
`medium`. No version stated; the 5-hull damage figure implies Advanced Edition.

## Contradictions Flagged
One, recorded on [[event-large-asteroid-field]]: its location list omits
[[sector-federation-space]], although `NEUTRAL_CIVILIAN` is allocated `min=2 max=4` in
`STANDARD_SPACE`. The omission recurs across Fandom's generic-event pages and reads as a wiki
convention rather than a factual claim.

## Links
- Source URL: https://ftl.fandom.com/wiki/Large_asteroid_field
- [[source-events-xml]], [[source-newevents]], [[source-events-fuel]], [[source-events-ships]]
