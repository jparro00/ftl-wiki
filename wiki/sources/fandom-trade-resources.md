---
id: source-fandom-trade-resources
type: source
source_kind: wiki
raw: raw/wiki/trade-resources.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [trading]
---

# Fandom — "Trade resources"

## Summary
The community wiki page for the event the game files call `TRADER_CIV`. Retrieved via the
MediaWiki API at revision 73900. A short page: the six intro texts, the four trade offers,
and one behavioural note the XML does not express.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'TRADER_CIV' in the
  datafiles."* This is the join key.
- All four `TRADER_LIST` offers match the XML `<item_modify>` ranges exactly (1–2 drones →
  5–10 fuel; 1–2 fuel → 4–5 missiles; 2–3 missiles → 2–3 drone parts; 2–4 missiles → 4–10
  fuel). No disagreement anywhere.
- **The one thing only this source has:** an inline note that *"the actual trade offer is
  shown prior to making the choice"*. The XML gives no hint of this, and it changes the
  event from a blind gamble into an informed decision.
- Lists **fifteen** sectors and adds `alsooccur=exit` — the event can land on the exit
  beacon. The fifteen omit Federation Space; see Contradictions.
- Marks the event `unique=false`, matching the absence of `unique="true"` in the XML.
- Categorised: `Random_Events`, `Trading_Events`.

## Events Covered
- [[event-trade-resources]]

## Other Pages Touched
- [[event-trade-resources-in-nebula]]

## Reliability Notes
`medium`. No game version stated, so `game_version` is `unknown`. Nothing on the page is
edition-specific, and `TRADER_CIV` carries no DLC markers, so the risk of version drift
here is low.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** [[sector-federation-space]] is missing from the page's
> `{{Locations}}` template.
> Fandom lists fifteen sectors. The game files put the event in the generic `ITEMS`
> pool ([[source-newevents]]), which `STANDARD_SPACE` allocates at
> `min="1" max="1"` ([[source-sector-data-xml]]) — so it can appear in
> Federation Space. Recorded on [[event-trade-resources]]. Game files trusted
> (`high` vs `medium`); this looks like a Fandom convention/omission, not a version
> difference — no DLC marker is involved.

## Links
- Source URL: https://ftl.fandom.com/wiki/Trade_resources
- [[source-events-xml]], [[source-text-events-xml]], [[source-newevents]],
  [[source-sector-data-xml]]
</content>
