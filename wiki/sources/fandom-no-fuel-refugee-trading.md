---
id: source-fandom-no-fuel-refugee-trading
type: source
source_kind: wiki
raw: raw/wiki/no-fuel-refugee-trading.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [out-of-fuel, refugee, advanced-edition]
---

# Fandom — "No fuel: refugee trading"

## Summary
Community wiki page covering the **whole `NO_FUEL_REFUGEE` event list** rather than a single
event, retrieved at revision 73281. It is therefore the joint source for two events that
have no page of their own: `NO_FUEL_REFUGEE_DAMAGED` and `NO_FUEL_REFUGEE_PIRATE`, plus the
list's unnamed inline first entry.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'NO_FUEL_REFUGEE' in the datafiles."* —
  a list id, not an event id, which is why the join is to the list rather than to one page.
- Marks it `{{Locations|outoffuel=distresson}}`, matching the XML (the list is one entry in
  `NO_FUEL_DISTRESS`).
- Presents all three list members as branches of one page:
  1. the inline "split its remaining fuel" event → `LOW` fuel_only (read as 1–3 fuel);
  2. `NO_FUEL_REFUGEE_DAMAGED` — the scrap-for-fuel trade with the Engi blue option;
  3. `NO_FUEL_REFUGEE_PIRATE` — the missiles-for-fuel trade with the pirate twist.
- Resolves the trades: 10 scrap → 3 fuel base, 10 scrap → 6 fuel with Engi or after a
  successful refusal, 1 missile → 5–7 fuel.
- **Flags the duplicated reject entry** with `{{DuplicateEvent|2}}`, independently confirming
  the doubled weight on the pirate-ambush outcome that is derivable from the XML.
- Reads the attack-the-refugees reward as medium (2–4 fuel + scrap).

## Events Covered
- [[event-no-fuel-refugee-damaged]]
- [[event-no-fuel-refugee-pirate]]

## Other Pages Touched
- [[event-no-fuel-friendly-refugee]] — a *different* event with near-identical prose; do not
  conflate the two.

## Reliability Notes
`medium`, `game_version: unknown`. It does not state that the whole list is Advanced Edition
content; that comes from the `<!-- DLC - below -->` annotation in
[[source-events-fuel]].

## Contradictions Flagged
None mechanical. Note the page's transcription of the damaged-refugee intro uses *"it's
hull looks damaged"* where the file has *"its hull looks damaged"*.

## Links
- Source URL: https://ftl.fandom.com/wiki/No_fuel:_refugee_trading
- [[source-events-fuel]], [[source-text-events-xml]], [[source-events-ships]]
