---
id: source-fandom-slug-oxygen-malfunction
type: source
source_kind: wiki
raw: raw/wiki/slug-oxygen-malfunction.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [slug, mantis, blue-option, crew-loss, bug]
---

# Fandom — "Slug oxygen malfunction"

## Summary
Community wiki page for `SLUG_DISTRESS_TRICK`, retrieved at revision 74820. Three choices,
a three-entry outcome list, and a confirmed missing-tag bug.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'SLUG_DISTRESS_TRICK' in the
  datafiles."*
- Confirms all three list outcomes: **high scrap** (scrap only), **1–3 Slug boarders** plus
  a default-rewards fight, or a **lost crew member** plus a default-rewards fight.
- Confirms the Clone Bay revival on the crew-loss entry — matching `<clone>true</clone>` in
  the files.
- Confirms the Mantis blue option gives **high scrap** with no fight.
- **Bug note, confirmed against the files:** *"This event is meant to occur at a distress
  beacon but won't because the `<distressBeacon/>` tag is missing in its definition."* The
  tag is indeed absent, as it is on [[event-slocknog]].
- Categories: `Nebula Events`, `Fights with Default Rewards`, `Crew loss risk`,
  `Clone Bay revival`, `Boarding risk`.

## Events Covered
- [[event-slug-oxygen-malfunction]]

## Other Pages Touched
- [[event-slocknog]], [[entity-mantis]], [[entity-slugs]], [[item-clone-bay]]

## Reliability Notes
`medium`; agrees with the files on every mechanical point, and the missing-tag claim is
directly verifiable.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Slug_oxygen_malfunction
- [[source-events-slug]], [[source-text-events-xml]], [[source-sector-data-xml]]
