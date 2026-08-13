---
id: source-fandom-zoltan-quest-primitives
type: source
source_kind: wiki
raw: raw/wiki/zoltan-quest-primitives.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [zoltan, quest-marker, weapon-reward, rebel-fleet-risk]
---

# Fandom — "Zoltan quest primitives"

## Summary
The community wiki page for `ZOLTAN_QUEST_PRIMITIVES`. Retrieved via the MediaWiki API at
revision 73912. Its whole value is the post-fight reward table, which is the only part of
the event not visible in `events_zoltan.xml`.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called
  'ZOLTAN_QUEST_PRIMITIVES' in the datafiles."*
- **Supplies what the game files do not** (these live in `events_ships.xml`):
  - Fighting the Zoltan → **Rebel Fleet pursuit doubled for 1 jump**, plus `low` scrap
    with resources (destroyed) or a random amount (crew killed).
  - Fighting the Rebel → a **weapon** with `low` scrap (destroyed) or `medium` scrap
    (crew killed). No fleet penalty.
- Confirms the event can **also** be reached as the quest marker from
  [[event-zoltan-trade-hub]] — the page body is wrapped in `<onlyinclude>` precisely so
  the trade hub page can transclude it.
- Trivia: neither `ZOLTAN_PRIMITIVES_ZOLTAN` nor `ZOLTAN_PRIMITIVES_REBEL` has
  surrender or escape values specified in `events_ships.xml`.
- Categorised `Rebel Fleet advancement risk`, `Weapon reward opportunity`,
  `Random_Events`, `Unique_Events`.

## Events Covered
- [[event-zoltan-quest-primitives]]

## Other Pages Touched
- [[event-zoltan-trade-hub]], [[entity-zoltan]], [[entity-rebels]],
  [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. States no game version. The Rebel-fleet-advance and reward-tier claims are the
sole source for those facts in this wiki — nothing in the game files ingested here
corroborates or contradicts them.

## Contradictions Flagged
None. Where this page overlaps the game files (intro text, choice text, ship loads) the
two agree.

## Links
- Source URL: https://ftl.fandom.com/wiki/Zoltan_quest_primitives
- [[source-fandom-zoltan-trade-hub]], [[source-events-zoltan]], [[source-text-events-xml]]
