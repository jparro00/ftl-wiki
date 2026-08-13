---
id: source-fandom-terraforming-scan
type: source
source_kind: wiki
raw: raw/wiki/terraforming-scan.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [blue-option, system-upgrade, filler, slug]
---

# Fandom — "Terraforming scan"

## Summary
Community wiki page for `TERRAFORMING_SCAN`, retrieved at revision 73895. A complete
transcription of the event's four-level choice tree, including the "Successful Scan"
sub-table that both blue options and the lucky normal scan feed into.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'TERRAFORMING_SCAN' in the
  datafiles."*
- Locations: Slug Controlled Nebula, Slug Home Nebula, with `alsooccur=filler` — matching
  `NEUTRAL`'s dual role as a sector allocation and the engine's fallback list.
- Renders the two blue options as **Improved Sensors (level 2+)** and **Zoltan crew**,
  matching `req="sensors" lvl="2"` and `req="energy"`.
- Splits the payoff into a named "Successful Scan" section reached identically from all
  three routes — the same structure as the `HIGH_SCAN_TERRAFORMING` list.
- Gives the bribe/delay scrap figures as **15–25** in both directions, matching the files,
  and notes the actual figure is shown before committing.
- `unique=true`; categorised under Trading Events, System Upgrade chance, Pirate ship
  fights, Fights with Default Rewards.

## Events Covered
- [[event-terraforming-scan]]

## Other Pages Touched
- [[event-pirate-fight]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]],
  [[concept-event-list-weighting]], [[concept-surrender-offers]]

## Reliability Notes
`medium`. Structurally faithful to the XML at every level. It gives no probabilities for
the `NORMAL_SCAN` / `HIGH_SCAN` splits — those are derived on the event page from list
membership.

## Contradictions Flagged
- Minor wording: Fandom has *"any chance you could help?"*, the game string *"any chance
  you can help?"* Recorded on [[event-terraforming-scan]]; game files trusted.

## Links
- Source URL: https://ftl.fandom.com/wiki/Terraforming_scan
- [[source-newevents]], [[source-text-events-xml]], [[source-events-ships]]
