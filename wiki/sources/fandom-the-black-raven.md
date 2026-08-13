---
id: source-fandom-the-black-raven
type: source
source_kind: wiki
raw: raw/wiki/the-black-raven.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [slug, donor-event, surrender-offer, named-ship, resolves-contradictions]
---

# Fandom — "The Black Raven"

## Summary
Community wiki page for `DONOR_BLACK_RAVEN`, retrieved via the MediaWiki API at revision
73896. Documents the event, the Slug mind-duel blue option and the ship's three win
conditions, plus trivia about the enemy hull that the files do not carry.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'DONOR_BLACK_RAVEN' in the datafiles."*
- Locations: Slug Controlled Nebula, Slug Home Nebula; `LRSmap=ship`, `unique=true` —
  matching `HOSTILE_SLUG` membership and `unique="true"`.
- **Confirms the surrender offer is guaranteed** — it presents the offer as an unconditional
  win condition, not a chance. The ship's file value is `<surrender chance="0" …>`, which is
  a fourth independent confirmation of the `1 − chance` reading in
  [[concept-surrender-offers]]; that page currently counts only three `chance="0"` ships
  because this one is defined in `events.xml`, not `events_ships.xml`.
- Renders the surrender's `min="3" max="4"` as *"30-40% hull"*, tagged *"[needs thorough
  verification]"* — the same hull-points-vs-percentage ambiguity the concept page flags.
- Confirms all three reward branches: surrender → `HIGH weapon`, destroyed → `MED standard`,
  dead crew → `HIGH standard`.
- **Adds a usability detail the files cannot show**: *"the weapon and the scrap amount are
  shown prior to accepting or rejecting the offer"*.
- **Trivia not in the game data**: the *Black Raven* is always a Slug Assault class, and this
  is the only event where a Slug Assault can appear as early as sector 4. The files give only
  `auto_blueprint="JELLY_TRUFFLE"`.
- Identifies the event as a **donor event** and a *Princess Bride* reference.

## Events Covered
- [[event-the-black-raven]]

## Other Pages Touched
- [[concept-surrender-offers]], [[entity-slugs]], [[sector-slug-controlled-nebula]],
  [[sector-slug-home-nebula]]

## Reliability Notes
`medium`. No version stated. The event has no DLC-marked tags, so nothing turns on it.

## Contradictions Flagged
None with the game files. It **corrects** an omission in [[concept-surrender-offers]]: a
fourth `chance="0"` ship exists, and it behaves exactly as that page predicts.

## Links
- Source URL: https://ftl.fandom.com/wiki/The_Black_Raven
- [[source-events-xml]], [[source-events-slug]], [[source-sector-data-xml]]
