---
id: source-fandom-no-fuel-fuel-trader-distress-off
type: source
source_kind: wiki
raw: raw/wiki/no-fuel-fuel-trader-distress-off.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [out-of-fuel, trading]
---

# Fandom — "No fuel: fuel trader (distress off)"

## Summary
Community wiki page for `FUEL_TRADER`, retrieved at revision 73259. It delegates the outcome
tree to two shared templates (`Fuel Trader High List`, `Fuel Trader Pt2`) rather than
inlining it, so the page itself is thin — the five intro variants and a pointer to the
shared tree.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'FUEL_TRADER' in the datafiles."*
- Marks it `{{Locations|outoffuel=distressoff}}`, matching the XML.
- Confirms the two events share one tree: the trade branches are templated identically to
  [[event-no-fuel-fuel-trader-distress-on]].
- **The actual trade offer is shown before you commit** — stated inline on the *Gladly
  trade* choice. This is not visible in the XML, where the values sit inside `item_modify`.
- Trivia: the "modified YT-1300" intro variant is a Star Wars reference (the Millennium
  Falcon).

## Events Covered
- [[event-no-fuel-fuel-trader-distress-off]]

## Other Pages Touched
- [[event-no-fuel-fuel-trader-distress-on]], [[event-no-fuel-prepare-to-dock]]

## Reliability Notes
`medium`, `game_version: unknown`. Because the outcome tables live in transcluded templates
that were not captured in this dump, the reward ranges on
[[event-no-fuel-fuel-trader-distress-off]] come from the game files rather than this page.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/No_fuel:_fuel_trader_(distress_off)
- [[source-events-fuel]], [[source-text-events-xml]]
