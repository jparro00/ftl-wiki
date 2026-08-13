---
id: source-fandom-confused-mantis
type: source
source_kind: wiki
raw: raw/wiki/confused-mantis.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [engi, mantis, blue-option, crew-reward, crew-risk, clone-bay]
---

# Fandom — "Confused Mantis"

## Summary
The community wiki page for `CONFUSED_MANTIS`. Retrieved via the MediaWiki API at
revision 73988. Transcribes the full nested choice tree, including the "Mining Colony"
sub-page section that corresponds to the `CONFUSED_MANTIS_HOME` event, and adds one
cross-event fact the game files cannot state.

## Key Takeaways
- **Names the in-game id explicitly:** *"This event is called 'CONFUSED_MANTIS' in the
  datafiles."*
- Claims this is **the only event in the game with a Human crew blue option**. That is a
  claim about the whole event corpus, not about this event, and is not verifiable from
  any single game file.
- Locations template: Engi Controlled Sector, Engi Homeworlds, `unique=true`, Long-Range
  Scanners `noship`. Matches `NEUTRAL_ENGI` membership in `events_engi.xml`.
- Labels the three gated options **Human Crew**, **Mantis Crew** and **Mind Control** —
  matching `req="human"`, `req="mantis"`, `req="mind" lvl="1"`.
- Names the reward tiers in the wiki's own vocabulary: *low scrap with resources* for the
  Mantis-crew branch, *medium scrap with resources* for the Mind Control branch. These
  correspond to `autoReward level="LOW|MED">standard`.
- Confirms the Clone Bay revival on the crew-loss branch and the named Mantis crew reward
  ("Robert Smith").
- Categorised `Crew loss risk`, `Clone Bay revival`, `Crew reward opportunity`,
  `System Upgrade opportunity`.

## Events Covered
- [[event-confused-mantis]]

## Other Pages Touched
- [[entity-engi]], [[entity-mantis]], [[item-mind-control]], [[item-clone-bay]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]

## Reliability Notes
`medium`. States no game version, though the Mind Control blue option makes it Advanced
Edition content. Prose transcription matches `text_events.xml` word for word except for a
single dropped "are" in the Mining Colony intro, which is a transcription slip rather
than a version difference.

## Contradictions Flagged
None material. One wording slip recorded on [[event-confused-mantis]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Confused_Mantis
- [[source-newevents]], [[source-events-engi]], [[source-text-events-xml]]
