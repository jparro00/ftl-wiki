---
id: source-fandom-slug-moons-question
type: source
source_kind: wiki
raw: raw/wiki/slug-moons-question.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [slug, distress, crew-reward, version-difference]
---

# Fandom — "Slug moons question"

## Summary
Community wiki page for `SLUG_DISTRESS_QUESTION`, retrieved at revision 74821. Enumerates
all four moon-count variants and maps every answer to correct or incorrect.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'SLUG_DISTRESS_QUESTION' in the
  datafiles."*
- Confirms the answer is always the moon count stated in that variant's own intro line.
- Puts numbers on the wrong-answer penalty: **35 scrap, 2–4 fuel, 1–2 drone parts** —
  matching the `item_modify steal="true"` block in the files.
- Correct answer gives a Slug crew member.
- **Records a version difference:** prior to Advanced Edition, the correct answer could be
  inferred from grammar cues in the marooned Slug's text; AE removed them. Cites a Reddit
  link to the official AE change log.
- Notes the event *"occurs at a regular beacon, but when you arrive there will be a nebula
  environment"* even though the files carry `<distressBeacon/>`.
- Cross-references a page titled "Slug trapped on a moon" for the shared answer sections —
  a redirect or alternate title for the same event.

## Events Covered
- [[event-slug-moons-question]]

## Other Pages Touched
- [[entity-slugs]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]

## Reliability Notes
`medium`; every number checks out. The AE grammar-cue note is the clearest explicit
version statement in this batch and is why this page's own `game_version` still reads
`unknown` — it describes both eras rather than declaring one.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Slug_moons_question
- [[source-events-slug]], [[source-text-events-xml]], [[source-sector-data-xml]]
