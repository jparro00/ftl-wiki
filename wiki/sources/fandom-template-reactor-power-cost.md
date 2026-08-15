---
id: source-fandom-template-reactor-power-cost
type: source
source_kind: wiki
raw: raw/wiki/template-reactor-power-cost.md
game_version: unknown
date: 2023-11-01
ingested: 2026-08-14
reliability: medium
tags: [reactor, power, scrap, cost-curve, template]
---

# Fandom — "Template:Reactor power cost"

## Summary
A MediaWiki **template**, not an article: the reactor upgrade cost table, transcluded into
[[source-fandom-ship]] at the `{{Reactor power cost}}` marker. Captured separately because the
table is not present in the Ship page's own wikitext — reading only that page yields the
surrounding prose and an empty transclusion.

Twelve lines of wikitext holding the single most-requested number about the reactor.

## Key Takeaways

**The cost curve, banded by the bar being purchased:**

| Bar bought | Cost each |
|---|---|
| 1–5 | 30 scrap |
| 6–10 | 20 scrap |
| 11–15 | 25 scrap |
| 16–20 | 30 scrap |
| 21–25 | 35 scrap |

- **The curve is non-monotonic.** Bars 6–10 at 20 scrap are the cheapest in the game, below the
  opening band's 30. Cost only rises from bar 11 onward.
- The table's own header tooltip specifies these are *"purchase cost in ship upgrade menu"* —
  i.e. store/upgrade-menu prices, not event grants.
- Five bands of five bars each, ending at 25, corroborating the ceiling stated in
  [[source-fandom-ship]].

## Events Covered
None — a bare data table.

## Other Pages Touched
- [[concept-power-and-reactor]], [[item-reactor]]

## Reliability Notes
`medium`, inherited from Fandom, but **arithmetically corroborated**: the totals implied by this
table reproduce the independent 490-scrap figure in [[source-fandom-ship]] exactly, under the
bar-being-bought reading. Two pages edited three years apart agreeing to the scrap is meaningful
evidence.

`game_version: unknown` — a bare table with no version context. Last edited 2023-11-01, well
into the AE era, but it states nothing about which edition it describes and the reactor is not
known to have changed between them.

Stable content: unedited since 2023 while the Ship page that transcludes it was edited in 2026.

## Contradictions Flagged
None internally. It **contradicts the prose** of the page that transcludes it — see
[[source-fandom-ship]], where the "costs always increase" claim is recorded against this table.
The table is trusted.

## Links
- Source URL: https://ftl.fandom.com/wiki/Template:Reactor_power_cost (revision 68667)
- [[source-fandom-ship]] — the page that transcludes it
