---
id: source-fandom-slug-hacker-medical
type: source
source_kind: wiki
raw: raw/wiki/slug-hacker-medical.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [slug, hacking, boarding, system-malfunction]
---

# Fandom — "Slug hacker (medical)"

## Summary
Community wiki page for `NEBULA_SLUG_MEDBAY`, retrieved at revision 74293. Three choices,
all leading to the same boarding fight with 2 Slug boarders and a different Medbay state.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'NEBULA_SLUG_MEDBAY' in the
  datafiles."*
- Confirms **2 Slug boarders on every branch** — matching the event body's
  `<boarders min="2" max="2" class="slug"/>`.
- Confirms the reward is `high` scrap-with-resources on every branch — matching
  `JELLY_STATUS_MEDBAY`'s `HIGH standard` on both `destroyed` and `deadCrew`.
- Notes the enemy ship *"doesn't have surrender or escape chances specified in the
  datafiles"* — correct, and it names `JELLY_STATUS_MEDBAY` in an HTML comment.
- Presents choice 1 as disabling **Medbay / Clone Bay**, matching the two `status limit`
  tags in the files.
- Categories: `Boarding hazard`, `System malfunction hazard`.

## Events Covered
- [[event-slug-hacker-medical]]

## Other Pages Touched
- [[item-hacking]], [[item-medbay]], [[item-clone-bay]], [[entity-slugs]]

## Reliability Notes
`medium`; every mechanical claim checks out against the files.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** intro wording. Fandom: *"your **medical bay** shuts off"*; game
> files: *"your **system** shuts off"*. Minor; recorded on [[event-slug-hacker-medical]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Slug_hacker_(medical)
- [[source-events-slug]], [[source-events-ships]], [[source-text-events-xml]]
