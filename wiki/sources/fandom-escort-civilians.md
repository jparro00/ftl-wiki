---
id: source-fandom-escort-civilians
type: source
source_kind: wiki
raw: raw/wiki/escort-civilians.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [quest, fuel-reward, store]
---

# Fandom — "Escort civilians"

## Summary
The community wiki page for `QUEST_ESCORT`. Retrieved via the MediaWiki API at revision
74735. A short page — it transcludes the shared "Escort Civilian Ship" destination template
rather than spelling out `QUEST_ESCORT_ARRIVE` — but it pins the id and quantifies the
down-payment.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'QUEST_ESCORT' in the datafiles."*
- Quotes all three intro variants, matching `textList QUEST_ESCORT_TEXT`.
- Down-payment: **1–3 fuel**, which is how it renders `autoReward level="LOW">fuel_only`.
  That numeric range does not appear in the XML.
- `unique=false`, `LRSmap=ship` — the ship is visible on long-range scanners.
- Notes the event *"is similar to Civilian FTL haywire escort in terms of quest beacon
  rewards"* — i.e. the two share the destination event list.

## Events Covered
- [[event-escort-civilians]] — the offer, the down-payment, and the shared destination

## Other Pages Touched
- [[event-escort-civilians-ftl-haywire]], [[event-rebel-fight]],
  [[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]],
  [[sector-rock-homeworlds]]

## Reliability Notes
`medium`. No game version stated, so `game_version: unknown`. The page does not distinguish
the AE-only fourth destination outcome (the reactor upgrade), which the XML marks
`<!--DLC!-->` — so its implicit destination odds are AE odds without saying so.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** sector coverage — omits [[sector-federation-space]] despite
> `QUESTS min=1 max=1` in `STANDARD_SPACE` ([[source-sector-data-xml]]). Recorded on
> [[event-escort-civilians]]; game files trusted.

The page's silence on the AE-only reactor-upgrade destination entry is noted on
[[event-escort-civilians]] under rule 10, with vanilla and AE odds given separately.

## Links
- Source URL: https://ftl.fandom.com/wiki/Escort_civilians
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
