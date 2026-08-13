---
id: source-fandom-pirate-briber
type: source
source_kind: wiki
raw: raw/wiki/pirate-briber.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [pirate, moral-choice, store-chance, hull-repair-chance, fleet-delay-chance]
---

# Fandom — "Pirate briber"

## Summary
Community wiki page for `PIRATE_BRIBER`, retrieved via the MediaWiki API at revision
73759. The most detailed page in this batch: it maps the bribe, the fight, the ship's four
win branches, and the whole `PIRATE_BRIBER_WIN` follow-up tree.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'PIRATE_BRIBER' in the datafiles."*
- Locations: Abandoned Sector, Civilian Sector, Engi Controlled Sector, Engi Homeworlds,
  Pirate Controlled Sector, Slug Controlled Nebula, Slug Home Nebula, **Uncharted Nebula**,
  Zoltan Controlled Sector, Zoltan Homeworlds; `alsooccur=exitandfiller`, `LRSmap=ship`,
  `unique=true`. It lists Uncharted Nebula, which the batch's list-derived sector set does
  not — consistent with its membership in the hardcoded filler lists.
- Transcribes all three intro variants and all five `PIRATE_BRIBER_WIN` outcomes,
  matching `text_events.xml`.
- Confirms the fleet-delay outcome and adds a detail the files do not state: it has
  **no effect in The Last Stand sector**.
- Reads `HIGH` `stuff` as *fuel 3–6, missiles 4–8, drone parts 1–2* (tooltip, no source).
- Reports the ship's surrender as **70% at 30-40% hull** and escape as **60% at 30-40%
  hull**.

## Events Covered
- [[event-pirate-briber]]

## Other Pages Touched
- [[concept-rebel-fleet-advance]], [[entity-pirates]], [[entity-rebels]],
  [[sector-pirate-controlled-sector]], [[sector-uncharted-nebula]],
  [[sector-the-last-stand]]

## Reliability Notes
`medium`. No version stated. The `stuff` reward figures and the hull percentages are
community readings, not file values.

## Contradictions Flagged
- **The `chance` attribute reading.** The game file has `<surrender chance="0.3">` and
  `<escape chance="0.4">`; Fandom reports **70%** and **60%** — i.e. `1 − chance`. Same
  inversion appears on [[source-fandom-destroyed-cargo-ship]]. Recorded on
  [[event-pirate-fight]] and [[event-pirate-briber]]; the raw attribute values are trusted,
  the semantics are left open.
- Renders `min`/`max` hull **points** as hull **percentages**.

## Links
- Source URL: https://ftl.fandom.com/wiki/Pirate_briber
- [[source-events-pirate]], [[source-events-ships]], [[source-dlceventsoverwrite]]
