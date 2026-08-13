---
id: source-fandom-giant-alien-spiders
type: source
source_kind: wiki
raw: raw/wiki/giant-alien-spiders.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [distress, blue-option, crew-loss-risk, bug-report, meme]
---

# Fandom — "Giant alien spiders"

## Summary
Community wiki page for `DISTRESS_INFESTATION`, retrieved via the MediaWiki API at revision
74073. Complete on outcomes, and the only source here for the event's reputation and for a
drone-part bug the files cannot show.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'DISTRESS_INFESTATION' in the
  datafiles."*
- Locations: Civilian Sector, Engi ×2, Mantis ×2, Pirate, Rock ×2, Uncharted Nebula;
  `distress=true`, `LRSmap=noship`, `unique=true` — matching the four `DISTRESS_BEACON_*`
  memberships.
- All three blue options and their reward levels match the files exactly (`MED stuff`,
  `LOW standard`, `HIGH stuff`).
- **Bug report, twice referenced**: *"no drone part is lost if the reward includes drone
  parts, though you still need at least 1 drone part to choose this blue option."* The files
  show an unconditional `item_modify` of −1, so this is observed runtime behaviour, not data.
- **Context the files cannot give**: the event's infamy, and that the crew loss was
  unrecoverable *"especially before the Clone Bay became available with the introduction of
  the Advanced Edition"* — which is the practical meaning of the `<clone>true</clone>` flag.
- Describes choice 1 as having a *"low success rate"*. The files show a **two-entry** list,
  i.e. 1/2 under uniform selection — so "low" is an impression, not a figure.
- Gives numeric readings for `stuff` (fuel 3–6, missiles 4–8, drone parts 1–2 at `HIGH`)
  that the files do not state.

## Events Covered
- [[event-giant-alien-spiders]]

## Other Pages Touched
- [[item-anti-bio-beam]], [[item-anti-personnel-drone]], [[item-boarding-drone]],
  [[event-unknown-disease-on-mining-colony]]

## Reliability Notes
`medium`. No version stated, but it explicitly discusses the pre-AE and post-AE experience,
so it is written from an Advanced Edition standpoint.

## Contradictions Flagged
None on outcomes. Its *"low success rate"* wording sits awkwardly against a 1/2 split
derived from the data; recorded on [[event-giant-alien-spiders]] as an impression rather
than a conflicting number.

## Links
- Source URL: https://ftl.fandom.com/wiki/Giant_alien_spiders
- [[source-events-xml]], [[source-newevents]], [[source-blueprints]], [[source-sector-data-xml]]
