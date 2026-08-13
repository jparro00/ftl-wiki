---
id: source-fandom-battlefield-wreckage
type: source
source_kind: wiki
raw: raw/wiki/battlefield-wreckage.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [sensors, blue-option, salvage, filler]
---

# Fandom — "Battlefield wreckage"

## Summary
Community wiki page for `WRECKAGE_EVENT`, retrieved at revision 74021. Two things make it
useful: an explicit `{{DuplicateEvent|4}}` marker that independently confirms the four-fold
repetition inside `WRECKAGE_INVESTIGATE`, and concrete resource bands for the `MED` and
`HIGH` `stuff` rewards.

## Key Takeaways
- Names the in-game id in Notes: *"This event is called 'WRECKAGE_EVENT' in the
  datafiles."*
- Locations: Engi Controlled Sector, Engi Homeworlds, Slug Controlled Nebula, Slug Home
  Nebula, `alsooccur=exitandfiller`, `unique=false` — all consistent with membership of
  `NEUTRAL`, `NEUTRAL_ENGI` and `NEUTRAL_EXIT`.
- `{{DuplicateEvent|4}}` on the "little remains" outcome — the only independent
  confirmation that entry is weighted 4×.
- Expands the reward levels into numbers: **medium `stuff`** = fuel 2–4, missiles 2–4,
  drone parts 1; **high `stuff`** = fuel 3–6, missiles 4–8, drone parts 1–2, each with some
  scrap. These figures appear nowhere in `newEvents.xml`.
- Ship reference notes: `MANTIS_FIGHT` and `ZOLTAN_SHIP` have no surrender or escape;
  `REBEL` has 50% escape at 30–40% hull and 50% surrender at 20–30% hull.
- Renders the two blue options as **Improved Sensors (level 2)** and **Advanced Sensors
  (level 3)**.

## Events Covered
- [[event-battlefield-wreckage]]

## Other Pages Touched
- [[event-mantis-fight]], [[event-rebel-fight]], [[event-zoltan-fight]],
  [[event-nebula-wreckage]], [[concept-event-list-weighting]],
  [[concept-surrender-offers]]

## Reliability Notes
`medium`. The structure and the duplicate marker match the files exactly. The `stuff`
resource bands and the hull-percentage rendering of `min`/`max` are interpretations, not
quotations, and are attributed on the event page.

## Contradictions Flagged
None outright. The `autoReward` numeric expansion is recorded as Fandom's claim rather
than as a file fact.

## Links
- Source URL: https://ftl.fandom.com/wiki/Battlefield_wreckage
- [[source-newevents]], [[source-text-events-xml]], [[source-events-ships]],
  [[source-events-engi]]
