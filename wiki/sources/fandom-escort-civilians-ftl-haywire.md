---
id: source-fandom-escort-civilians-ftl-haywire
type: source
source_kind: wiki
raw: raw/wiki/escort-civilians-ftl-haywire.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [distress, quest-marker, blue-option, augment]
---

# Fandom — "Escort civilians FTL haywire"

## Summary
The community wiki page for the event the game files call `ESCORT_BEACON`. Retrieved via
the MediaWiki API at revision 74056. Short page — three choices — but it supplies the
quest-destination content via a transcluded template.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'ESCORT_BEACON' in the
  datafiles."* This is the join key.
- Confirms it is a **distress beacon** (`distress=true`) with a ship present at the beacon
  (`LRSmap=ship`), and `unique=true`.
- Renders the blue option as **Advanced FTL Navigation**, matching `req="FTL_JUMPER"` —
  the augment id in the files is not obviously that augment's display name, so this page
  is the join for it.
- States that choice 1 grants low **scrap only** plus a quest marker, and that the blue
  option grants **high scrap with resources**. Both match the files' `autoReward` payload
  types (`scrap_only` / `standard`).
- Notes the event *"is similar to Escort nearby ship in terms of quest beacon
  rewards"* — Fandom's "Escort nearby ship" is [[event-escort-civilians]] (`QUEST_ESCORT`),
  and the two share the `QUEST_ESCORT_ARRIVE` destination list in the files.
- The destination content is transcluded (`{{Escort Civilian Ship}}`), so the retrieved
  markup does **not** contain the destination outcomes; those come from
  [[source-events-xml]] here.
- Categorised `Random_Events`, `Unique_Events`, `Events with Quest Markers`.

## Events Covered
- [[event-escort-civilians-ftl-haywire]]

## Other Pages Touched
- [[item-ftl-jumper]], [[event-escort-civilians]], [[concept-quest-beacon-placement]]

## Reliability Notes
`medium`. No game version stated. The unexpanded template means this page is *less*
complete than the game files for the destination half of the event.

## Contradictions Flagged
None. Wording matches the files verbatim.

## Links
- Source URL: https://ftl.fandom.com/wiki/Escort_civilians_FTL_haywire
- [[source-events-xml]], [[source-text-events-xml]]
