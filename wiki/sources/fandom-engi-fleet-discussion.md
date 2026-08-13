---
id: source-fandom-engi-fleet-discussion
type: source
source_kind: wiki
raw: raw/wiki/engi-fleet-discussion.md
game_version: unknown
ingested: 2026-08-09
reliability: medium
tags: [fandom, engi, ship-unlock, chain, quest-marker]
---

# Fandom — Engi fleet discussion

## Summary
FTL Fandom wiki page for `ENGI_UNLOCK_1` (revision 74722, retrieved 2026-08-09). Documents
the **entire Stealth Cruiser unlock chain** on one page: the Engi Homeworlds trigger, both
quest-marker beacons (real and decoy), the final Mantis-escort fight, and the payoff.

## Key Takeaways
- The chain is the Stealth Cruiser (Layout A) unlock; the ship can alternatively be
  unlocked by winning with the Rock Cruiser.
- Both quest markers are added at once and can be visited in either order.
- **The tell:** the real beacon's escape text has *no* comma ("As soon as they see you
  they power up…"), the decoy's *has* one. If the intro was skipped, the "With the ship
  gone" text inverts the tell — the real one has the comma. Both are verified against
  `raw/gamedata/text_events.xml`.
- Gives the surrender thresholds as ~50% hull (real) and ~40% hull (decoy), with a
  parenthetical that the true values may be flat hull numbers.
- Notes a bug: if the guaranteed high scrap-with-resources payout at the end rolls an
  augmentation, it overwrites the guaranteed Titanium System Casing.

## Events Covered
- [[event-engi-fleet-discussion]] — `ENGI_UNLOCK_1`
- [[event-engi-unlock-2real]] — `ENGI_UNLOCK_2REAL`
- [[event-engi-unlock-2real-surrender]] — `ENGI_UNLOCK_2REAL_SURRENDER`
- [[event-engi-unlock-2fake]] — `ENGI_UNLOCK_2FAKE`
- [[event-engi-unlock-2fake-surrender]] — `ENGI_UNLOCK_2FAKE_SURRENDER`
- [[event-engi-unlock-3]] — `ENGI_UNLOCK_3`
- [[event-engi-unlock-4]] — `ENGI_UNLOCK_4`

## Other Pages Touched
- [[chain-stealth-cruiser-unlock]], [[item-titanium-system-casing]], [[entity-engi]]

## Contradictions Flagged
- Surrender thresholds stated as percentages; game files give flat hull values (4 and 5).
- The final reward prose says "a weapon"; `text_events.xml` says "an advanced
  augmentation".
- The page omits the `destroyed` outcome of the real beacon's Rebel ship, which in the
  game files grants no quest marker and therefore fails the chain.

All three recorded on the relevant event pages.

## Links
- https://ftl.fandom.com/wiki/Engi_fleet_discussion
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
