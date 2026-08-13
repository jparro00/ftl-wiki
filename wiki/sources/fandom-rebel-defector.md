---
id: source-fandom-rebel-defector
type: source
source_kind: wiki
raw: raw/wiki/rebel-defector.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, crew-reward-chance, quest-marker, bug-report]
---

# Fandom — "Rebel defector"

## Summary
Community wiki page for `ALISON_DEFECTOR`, retrieved via the MediaWiki API at revision
74871. Unusually complete: it walks both outcome lists entry by entry, marks the triplicated
crew outcome with a `DuplicateEvent|3` template, and documents the quest marker in its own
section.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'ALISON_DEFECTOR' in the datafiles."*
- Locations: Rebel Controlled Sector, Rebel Stronghold; `LRSmap=ship`, `unique=true` —
  matching `unique="true"` and `<ship load="REBEL" hostile="true"/>` in the files.
- Its `{{DuplicateEvent|3}}` markers independently corroborate the derivation on
  [[event-rebel-defector]]: the crew-gain entry really is written three times in a six-entry
  list.
- Documents the quest marker's two outcomes (`HIGH stuff` / `LOW scrap_only`), matching
  `ALISON_DEFECTOR_QUEST`.
- **Reports a bug** the game files cannot show: on the reject → accept path, a crew icon is
  displayed because the developers forgot to mark the crew tag hidden, telegraphing an
  outcome that was meant to be a gamble.
- Reads `modifyPursuit amount="1"` as *"Rebel Fleet pursuit is doubled"* — an interpretation,
  not a file value. See [[concept-rebel-fleet-advance]].

## Events Covered
- [[event-rebel-defector]]

## Other Pages Touched
- [[concept-rebel-fleet-advance]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]

## Reliability Notes
`medium`. No version stated. Its damage figures match the **Advanced Edition** reading of
the DLC-marked tags, so it most likely describes AE.

## Contradictions Flagged
One, recorded on [[event-rebel-defector]]: Fandom quotes *"He damages your **ship** and
steals your **flight data**"* on the accept-immediately path, where the game files say
*"damages your **engines**"*. It appears to have blended the two branches' strings.

## Links
- Source URL: https://ftl.fandom.com/wiki/Rebel_defector
- [[source-events-xml]], [[source-events-rebel]], [[source-text-events-xml]]
