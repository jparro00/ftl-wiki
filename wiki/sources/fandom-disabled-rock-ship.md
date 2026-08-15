---
id: source-fandom-disabled-rock-ship
type: source
source_kind: wiki
raw: raw/wiki/disabled-rock-ship.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rock, salvage, blue-option, bug-claim]
---

# Fandom — "Disabled Rock ship"

## Summary
Community wiki page for `ROCK_LOOTING`, retrieved via the MediaWiki API at revision 74042.
Full choice tree with all three sub-lists, the Slug blue option, and — in HTML comments —
two claims about game *behaviour* that the XML alone cannot show.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'ROCK_LOOTING' in the datafiles."*
- Locations: Rock Controlled Sector, Rock Homeworlds; `LRSmap=noship`, `unique=true`.
- Documents the Slug blue option (`req="slug"`) and correctly shows that **both** of its
  outcomes pay scrap with no fight.
- Tags the "leave it alone / nothing happens" outcome `{{DuplicateEvent|2}}`, confirming
  the 2-of-3 weighting in `eventList ROCK_LOOTING_LEAVE`.
- **Bug claim (`autoReward` case):** repeated HTML comment — *"GAME CODE has `<autoReward
  level=>` line with 'low' value, while it should have been 'LOW' - and the game treats
  this as 'RANDOM' value"*. The lowercase `low` is verifiable in the game files; the
  claimed `RANDOM` fallback behaviour is not. Flagged on [[event-disabled-rock-ship]].
- **Surrender template numbers:** carries
  `{{SurrenderEscape(alt)|surrenderofferchance|ROCK_SHIP|events_ships.xml|30|30-40|3-4}}`
  for the `ROCK_SHIP` enemy, where the game files declare
  `chance="0.7" min="3" max="4"`. Flagged on [[event-rock-fight]] — this is the only page
  in the batch carrying surrender numbers at all.

## Events Covered
- [[event-disabled-rock-ship]]
- Referenced in passing (enemy ship only): [[event-rock-fight]]

## Other Pages Touched
- [[item-slug-crew]], [[concept-autoreward-tiers]]

## Reliability Notes
`medium`. No version stated. Its two behavioural claims (reward-level fallback, surrender
numbers) are the most valuable and the least verifiable content on the page — both are
recorded as contradictions rather than adopted.

## Contradictions Flagged
> ⚠️ `autoReward level="low"` — file value vs. claimed `RANDOM` runtime behaviour.
> Recorded on [[event-disabled-rock-ship]].

> ⚠️ Surrender numbers `30 / 30-40 / 3-4` vs. `chance="0.7" min="3" max="4"`.
> Recorded on [[event-rock-fight]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Disabled_Rock_ship
- [[source-events-rock]], [[source-text-events-xml]]
