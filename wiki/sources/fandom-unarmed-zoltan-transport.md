---
id: source-fandom-unarmed-zoltan-transport
type: source
source_kind: wiki
raw: raw/wiki/unarmed-zoltan-transport.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [zoltan, ship-unlock, quest-marker, zoltan-cruiser]
---

# Fandom — "Unarmed Zoltan transport"

## Summary
The community wiki page for `ZOLTAN_PEACE_QUEST`. Retrieved via the MediaWiki API at
revision 73903. Uniquely valuable because it documents **both halves of the Zoltan
Cruiser unlock on one page** — the starting event and the quest-marker follow-up
(`ZOLTAN_PEACE_QUEST2`), which the game files keep as separate top-level events.

## Key Takeaways
- **Names both in-game ids**: *"This event is called 'ZOLTAN_PEACE_QUEST' in the
  datafiles."* The quest-marker section transcribes `ZOLTAN_PEACE_QUEST2` in full.
- Identifies this as **the [[entity-zoltan-cruiser]] Layout A unlocking event**, and notes
  the ship can alternatively be unlocked by **winning the game with the Federation
  Cruiser**.
- Traces the **only winning dialogue path** through `ZOLTAN_PEACE_QUEST2`: hail →
  "Perhaps there could be a reconciliation of our ideals without war?" → "True progress
  can only be achieved without bloodshed." Every other reply becomes a Rebel fight.
- States a **50% / 50%** split between the two `ZOLTAN_PEACE_QUEST_REWARD` payouts. The
  game files state no percentage.
- **Supplies what the game files do not:** the post-fight branches of the "attack them"
  path (surrender prompt on the unarmed ship, and `low`/random scrap-with-resources on
  both attack sub-events) — these live in `events_ships.xml`.
- Notes the quest marker shows a **ship** on Long-Ranged Scanners.
- Categorised `Ship Unlocking Events`, `Events with Quest Markers`,
  `Augmentation reward chance`, `Crew reward chance`, `Fights with Default Rewards`.

## Events Covered
- [[event-unarmed-zoltan-transport]] — `ZOLTAN_PEACE_QUEST`
- [[event-zoltan-peace-quest2]] — `ZOLTAN_PEACE_QUEST2`, documented here as the page's
  "Quest Marker" section rather than as its own page

## Other Pages Touched
- [[chain-zoltan-cruiser-unlock]], [[item-zoltan-shield]], [[entity-zoltan-cruiser]],
  [[entity-federation-cruiser]], [[entity-rebels]]

## Reliability Notes
`medium`. States no game version. Two of its claims go beyond the game files and should
be treated as community assertions: the **50/50** reward split, and describing Envoy as
**"maxed in all skills"** where the file says `all_skills="2"`.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** reward split.
> Fandom asserts 50%/50% between the two `ZOLTAN_PEACE_QUEST_REWARD` entries; the game
> files give an unweighted two-entry `eventList` and state no percentage
> ([[source-events-zoltan]]).

> ⚠️ **CONTRADICTION:** Envoy's skills.
> Fandom: *"maxed in all skills"*. Game files: `all_skills="2"`
> ([[source-events-zoltan]]).
> Both recorded on [[event-zoltan-peace-quest2]]. Compatible only if 2 is the cap.

## Links
- Source URL: https://ftl.fandom.com/wiki/Unarmed_Zoltan_transport
- [[source-events-zoltan]], [[source-text-events-xml]], [[source-sector-data-xml]]
