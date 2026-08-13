---
id: source-fandom-slocknog
type: source
source_kind: wiki
raw: raw/wiki/slocknog.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [slug, crew-reward, bug]
---

# Fandom — "Slocknog"

## Summary
Community wiki page for `SLUG_DISTRESS_RESCUE`, retrieved at revision 74823. Two choices
and a follow-up; its value is two notes about behaviour the data does not express.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'SLUG_DISTRESS_RESCUE' in the
  datafiles."*
- Confirms the 55-scrap price and that refusing leads to a **free** recruitment offer.
- **Bug note, confirmed against the files:** *"This event is meant to occur at a distress
  beacon but won't because the `<distressBeacon/>` tag is missing in its definition."* The
  tag is indeed absent from `SLUG_DISTRESS_RESCUE` while its list-mates
  `SLUG_DISTRESS_ROCK`, `SLUG_DISTRESS_QUESTION` and `SLUG_DISTRESS_MANTIS` all carry it.
- **Behavioural note not in the files:** *"The skill set can differ if you recruit Slocknog
  for free, instead of paying him."* The two `<crewMember … id="name_Slocknog"/>` tags are
  identical, so the data neither supports nor refutes this.
- Notes that crew skills are displayed before you commit on both offers.
- Categories: `Crew purchase opportunity`, `Crew reward opportunity`, `Nebula Events`.

## Events Covered
- [[event-slocknog]]

## Other Pages Touched
- [[entity-slugs]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]

## Reliability Notes
`medium`. The missing-`distressBeacon` claim is directly verifiable and correct, which
lends weight to the skills claim — but the latter remains untested here.

## Contradictions Flagged
None. The differing-skills claim is recorded as an open question on [[event-slocknog]]
rather than a contradiction, since the files are silent rather than opposed.

## Links
- Source URL: https://ftl.fandom.com/wiki/Slocknog
- [[source-events-slug]], [[source-text-events-xml]]
