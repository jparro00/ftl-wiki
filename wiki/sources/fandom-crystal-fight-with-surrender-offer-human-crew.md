---
id: source-fandom-crystal-fight-with-surrender-offer-human-crew
type: source
source_kind: wiki
raw: raw/wiki/crystal-fight-with-surrender-offer-human-crew.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [crystal-sector, combat, surrender, crew-reward, bug]
---

# Fandom — "Crystal fight with surrender offer (Human crew)"

## Summary
The community wiki page for `CRYSTAL_HUNTER`, the Crystalline slaver ship. Retrieved via
the MediaWiki API at revision 74034. Its value is a documented data-file bug.

## Key Takeaways
- Names the in-game id: *"This event is called 'CRYSTAL_HUNTER' in the datafiles"*.
- **Documents the missing-tag bug:** *"The surrender is lacking the usual tag to stop the
  fight in the datafiles, making it possible to receive a crewmember along with the rewards
  for defeating the ship."* Verified against the raw file — the surrender choice contains
  only `<crewMember amount="1" class="human"/>` with no `<ship hostile="false"/>`.
- Surrender-offer chance **50**, matching `<surrender chance="0.5">` exactly. This
  agreement is what makes the same template's `40` on
  [[source-fandom-crystal-fight]] look like an error rather than a convention.
- Win → medium scrap with resources.
- Location: Hidden Crystal Worlds, `unique=true`, **ship** on Long-Range Scanners.

## Events Covered
- [[event-crystal-fight-with-surrender-offer-human-crew]]

## Other Pages Touched
- [[sector-hidden-crystal-worlds]], [[entity-crystal-men]], [[concept-surrender-offers]]

## Reliability Notes
`medium`, but the key claim here is independently confirmed by the game files, which raises
confidence in it specifically.

## Contradictions Flagged
None. This page agrees with the game files everywhere checked.

## Links
- Source URL: https://ftl.fandom.com/wiki/Crystal_fight_with_surrender_offer_(Human_crew)
- [[source-events-xml]], [[source-text-events-xml]]
