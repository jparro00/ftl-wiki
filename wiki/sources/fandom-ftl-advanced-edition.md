---
id: source-fandom-ftl-advanced-edition
type: source
source_kind: wiki
raw: raw/wiki/ftl-advanced-edition.md
game_version: ae
date: 2026-08-15
ingested: 2026-08-15
reliability: medium
tags: [version, ae, abandoned-sector, lanius]
---

# Fandom — "FTL: Advanced Edition"

## Summary
The page describing the free April 3 2014 expansion, retrieved at revision 74567. Fetched
as the version anchor for this wiki's `ae` / `vanilla` / `both` field: it states what AE
added and, importantly, which AE changes apply even with AE content switched **off**.

## Key Takeaways
- **The AE toggle is not all-or-nothing.** "Updates to balance and to preexisting content
  are still applied even if Advanced Edition content is disabled", and some AE-added events
  can be met with AE content off. Only the `Advanced Edition Content Events` category is
  strictly gated. This is why `version: both` is a real and common value in this wiki.
- **AE added exactly one sector — the Abandoned Sector** — together with the Lanius. That is
  the only sector-level difference between the two versions.
- AE added the Hacking, Mind Control and Backup Battery systems, the Clone Bay (replacing
  Medbay, 50 scrap at a store), layout C for nearly all ships, the Lanius Cruiser, the
  ability to man Sensors and Doors, and **Hard difficulty** with lower scrap rewards.
- The pulsar hazard is AE-only (per [[source-fandom-environmental-hazards]]); this page
  corroborates the new-hazard framing but does not enumerate hazards.

## Events Covered
- None directly; anchors the `Advanced Edition Content Events` category referenced by
  [[source-fandom-sectors]] for the `override_*` event lists.

## Other Pages Touched
- [[sector-abandoned-sector]], [[entity-lanius]], [[concept-ae-vs-vanilla]],
  [[source-fandom-sectors]]

## Reliability Notes
`medium`. It is largely a transcription of Subset's own release posts (cited to
`ftlgame.com`), so the feature list is close to first-party; the "still applied with AE
off" claim is uncited wiki assertion, though it is consistent with the
`dlcEventsOverwrite.xml` / `override_*` structure in `raw/gamedata/`.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/FTL:_Advanced_Edition
- [[source-fandom-sectors]], [[source-fandom-environmental-hazards]],
  [[source-dlceventsoverwrite]]
