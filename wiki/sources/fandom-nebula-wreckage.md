---
id: source-fandom-nebula-wreckage
type: source
source_kind: wiki
raw: raw/wiki/nebula-wreckage.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [slug, quest-marker]
---

# Fandom — "Nebula wreckage"

## Summary
The community wiki page for `NEBULA_BATTLEFIELD`, retrieved at revision 73757. It covers
the parent event, the `BATTLEFIELD_SURVIVOR` sub-event, and the `SECRET_WORD_ABADOTH` quest
marker in one page — the only source that presents the whole ABADOTH thread as a unit.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'NEBULA_BATTLEFIELD' in the
  datafiles."* This is the join key.
- Marks the "nothing happens" investigate outcome as a triple entry (`DuplicateEvent|3`),
  matching the XML's three copies of `event_BATTLEFIELD_INVESTIGAGE_2_text`.
- States the damage outcome as **5 hull** plus 1 fire damage to a random room, where the
  files carry separate `damage 4` and `damage 1 … effect="fire"` tags.
- Describes `modifyPursuit amount="1"` as "Rebel Fleet pursuit is **doubled for 1 jump**".
- Confirms the ABADOTH password and the Zoltan-ship consequence for a wrong answer.
- Categories: `Random_Events`, `Unique_Events`, plus quest-marker, hull-damage, fire,
  system-damage, Rebel-advance and crew-reward risk/reward categories.

## Events Covered
- [[event-nebula-wreckage]]
- [[event-secret-word-abadoth]]

## Other Pages Touched
- [[sector-slug-controlled-nebula]], [[sector-uncharted-nebula]], [[entity-zoltan]]

## Reliability Notes
`medium`. States no game version, so `game_version` is `unknown`. Where it disagrees with
the extracted 1.6.x files, the files win.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** availability. Fandom lists *Slug Controlled Nebula* and
> *Uncharted Nebula* and omits *Slug Home Nebula*; the game files put `NEBULA_BATTLEFIELD`
> only in `NEBULA_NEUTRAL_SLUG`, drawn on by `SLUG_SECTOR` and `SLUG_HOME` and by no
> uncharted-nebula sector. Recorded on [[event-nebula-wreckage]].

Also recorded on [[event-secret-word-abadoth]]: the `modifyPursuit` wording, which is a
description of the tag rather than a competing value.

## Links
- Source URL: https://ftl.fandom.com/wiki/Nebula_wreckage
- [[source-events-slug]], [[source-text-events-xml]], [[source-sector-data-xml]]
