---
id: source-fandom-free-scrap-with-resources
type: source
source_kind: wiki
raw: raw/wiki/free-scrap-with-resources.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [free-item, scrap, no-choice]
---

# Fandom — "Free scrap with resources"

## Summary
The community wiki page for the event the game files call `FREE_ITEMS`. Retrieved via the
MediaWiki API at revision 74067. A pure reward event with no choices.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'FREE_ITEMS' in the
  datafiles."* This is the join key.
- Lists all **six** intro variants; the files mark the last two `<!--DLC! added texts-->`,
  so the vanilla pool is four. The page does not distinguish them — see below.
- Reads `<autoReward level="MED">standard</autoReward>` as *"medium scrap with
  resources"*.
- Confirms availability in sixteen sectors (including both Zoltan sectors, unlike
  [[event-free-weapon]]) but **not** Hidden Crystal Worlds. `alsooccur=exit`,
  `LRSmap=noship`, `unique=false`.
- Distinct from the three faction-specific pages of the same shape already in the wiki —
  [[event-free-scrap-with-resources-engi]], [[event-free-scrap-with-resources-lanius]],
  [[event-free-scrap-with-resources-zoltan]] — which are separate events with separate ids.
- Categorised `Random_Events`.

## Events Covered
- [[event-free-scrap-with-resources]]

## Other Pages Touched
- [[event-free-drone-schematic]], [[event-free-weapon]], [[concept-autoreward-tiers]]

## Reliability Notes
`medium`. No game version stated, and the merged text pool means it describes AE.

## Contradictions Flagged
> ⚠️ **Version gap, not an error.** `text_FREE_ITEMS_5` and `text_FREE_ITEMS_6` are flagged
> `<!--DLC! added texts-->` in `events.xml` ([[source-events-xml]]). Vanilla draws from
> four strings, Advanced Edition from six. Fandom lists six with no version note.
> Recorded on [[event-free-scrap-with-resources]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Free_scrap_with_resources
- [[source-events-xml]], [[source-text-events-xml]]
