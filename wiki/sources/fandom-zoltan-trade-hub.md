---
id: source-fandom-zoltan-trade-hub
type: source
source_kind: wiki
raw: raw/wiki/zoltan-trade-hub.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [zoltan, quest-marker, blue-option, store-chance]
---

# Fandom — "Zoltan trade hub"

## Summary
The community wiki page for `ZOLTAN_TRADE_HUB`. Retrieved via the MediaWiki API at
revision 73918. Ingested here as a **supporting source only** — the event it primarily
documents is not part of this batch. It was used to establish the second route into
[[event-zoltan-quest-primitives]].

## Key Takeaways
- **Names both in-game ids**: *"This event is called 'ZOLTAN_TRADE_HUB' in the
  datafiles… The quest marker event is called 'ZOLTAN_QUEST_PRIMITIVES'."*
- Confirms `ZOLTAN_QUEST_PRIMITIVES` can be reached **either** as a standalone quest
  beacon **or** as a marker planted by the trade hub's cantina branch, and transcludes
  the primitives page wholesale to show the outcomes are identical.
- Notes the primitives quest marker shows **no ship** on Long-Ranged Scanners.
- Documents two blue options on the trade hub itself — **Teleporter** (`req="teleporter"
  lvl="1"`) and **Zoltan Crew** (`req="energy"`, costs 10 scrap) — for
  [[event-zoltan-trade-hub]] when that page is written.
- The game file comments the event `<!-- This is a 50/50 chance of quest start-->`,
  matching Fandom's two-entry `ZOLTAN_TRADE_HUB_SUCCESS` (store, or cantina + quest).
- Categorised `Events with Quest Markers`, `Store Opening chance`, `Boarding risk`,
  `Rebel Fleet advancement risk`, `Weapon reward chance`, `Scrap use Events`.

## Events Covered
- [[event-zoltan-quest-primitives]] — supporting citation for its second entry route
- [[event-zoltan-trade-hub]] — **not yet written**; this page is its primary source when
  it is

## Other Pages Touched
- [[item-teleporter]], [[entity-zoltan]]

## Reliability Notes
`medium`. States no game version. Used here only for the trade-hub → primitives link,
which the game files independently confirm via
`<quest event="ZOLTAN_QUEST_PRIMITIVES"/>` in `ZOLTAN_TRADE_HUB_SUCCESS`
([[source-events-zoltan]]).

## Contradictions Flagged
None observed within the portion used.

## Links
- Source URL: https://ftl.fandom.com/wiki/Zoltan_trade_hub
- [[source-fandom-zoltan-quest-primitives]], [[source-events-zoltan]]
