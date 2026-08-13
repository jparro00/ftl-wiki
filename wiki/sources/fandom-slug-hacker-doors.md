---
id: source-fandom-slug-hacker-doors
type: source
source_kind: wiki
raw: raw/wiki/slug-hacker-doors.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [slug, hacking, system-malfunction, fire]
---

# Fandom — "Slug hacker (doors)"

## Summary
Community wiki page for `NEBULA_SLUG_DOORS`, retrieved at revision 74292. Two choices, both
fights; the useful content is the fire-weapon note and the door-state behaviour.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'NEBULA_SLUG_DOORS' in the
  datafiles."*
- **"The enemy ship will have at least one Fire Beam or Fire Bomb"** — matching the
  `weaponOverride count="1"` block on `JELLY_STATUS_DOORS` and `JELLY_STATUS_HACKING_FIRE`
  in [[source-events-ships]]. (Fandom says "at least one"; the override says exactly one.)
- **Behavioural note not in the files:** *"Upon jumping to this beacon event, doors will be
  stuck in a state they were in prior to the jump — unless the hack is countered."*
- Reward tiers match the ship definitions: `MED` destroyed / `HIGH` deadCrew for the plain
  branch, `HIGH` either way for the Hacking branch.
- Text matches `text_events.xml` verbatim.

## Events Covered
- [[event-slug-hacker-doors]]

## Other Pages Touched
- [[item-hacking]], [[item-door-system]], [[entity-slugs]]

## Reliability Notes
`medium`. The door-freeze note is an in-play observation the data cannot confirm or refute.

## Contradictions Flagged
None. "At least one" versus "exactly one" fire weapon is a looseness in phrasing, not a
conflicting claim.

## Links
- Source URL: https://ftl.fandom.com/wiki/Slug_hacker_(doors)
- [[source-events-slug]], [[source-events-ships]], [[source-text-events-xml]]
