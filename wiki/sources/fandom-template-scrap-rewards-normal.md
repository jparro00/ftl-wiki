---
id: source-fandom-template-scrap-rewards-normal
type: source
source_kind: wiki
raw: raw/wiki/template-scrap-rewards-normal.md
game_version: both
date: 2026-08-14
ingested: 2026-08-16
reliability: medium
tags: [mechanics, rewards, economy, scrap, autoreward, resolves-open-question]
---

# Fandom — Template: "Scrap rewards (Normal)"

## Summary
The table transcluded into [[source-fandom-rewards]], retrieved at revision 72605. Eight rows —
one per sector — of scrap ranges for the `LOW` / `MED` / `HIGH` levels **on Normal difficulty**.
This is the single table that converts "medium scrap" into a number, and it closes the wiki's
longest-standing open question.

## Key Takeaways

| Sector | `LOW` | `MED` | `HIGH` |
|---|---|---|---|
| 1 | 7–10 | 12–19 | 19–23 |
| 2 | 10–14 | 16–27 | 27–32 |
| 3 | 13–18 | 21–35 | 35–41 |
| 4 | 16–23 | 26–42 | 42–51 |
| 5 | 19–27 | 31–50 | 50–60 |
| 6 | 22–31 | 36–58 | 58–69 |
| 7 | 25–35 | 40–66 | 66–79 |
| 8 | 28–39 | 45–74 | 74–88 |

Three structural facts read straight off it:

- **`MED` and `HIGH` are contiguous in all eight rows** — the top of `MED` is exactly the
  bottom of `HIGH` (19/19, 27/27, 35/35, 42/42, 50/50, 58/58, 66/66, 74/74). They are cuts of
  one distribution, not separate ones.
- **`LOW` and `MED` are not** — there is a gap at every sector (10 → 12, 14 → 16, …). `LOW` is
  a genuinely separate band.
- **`MED` is by far the widest band.** At sector 8 it spans 45–74 (30 points) against `LOW`'s
  12 and `HIGH`'s 15. "Medium scrap" is the least predictable payout in the game, not the
  middling one.

**Scaling.** `LOW`'s floor is exactly `7 + 3(n−1)` across all eight sectors. Every other column
is a near-linear ramp with rounding wobble, and every column lands close to **4× its sector-1
value by sector 8**. So the depth multiplier is roughly `1 + 3(n−1)/7`, applied to a fixed base
range — but the table is the authority, not the formula.

## Events Covered
- None. It applies to every event carrying an `<autoReward>` with a scrap component.

## Other Pages Touched
- [[concept-autoreward-tiers]], [[concept-scrap-economy]], [[source-fandom-rewards]]

## Reliability Notes
`medium`. Fandom sources these figures to the third-party "Calculated FTL" Steam guide
(2127539536), which this repo does not hold — the numbers cannot be checked against anything in
`raw/`, since the event files contain tier names and no magnitudes at all. The internal
structure (contiguous `MED`/`HIGH`, exact `7 + 3(n−1)` floor) is consistent enough to look
derived rather than remembered, which is the main reason to trust it.

## Contradictions Flagged
None — nothing in the wiki previously asserted a number to contradict.

> ⚠️ **Normal only.** The companion `{{Scrap rewards (Easy)}}` and `{{Scrap rewards (Hard)}}`
> tables were not captured. `rewards.md` states the increase per sector is **larger on lower
> difficulties**, so these figures are a floor on Easy and a ceiling on Hard — direction known,
> magnitude not. Label every derived scrap figure Normal-difficulty.

## Links
- Source URL: https://ftl.fandom.com/wiki/Template:Scrap_rewards_(Normal)
- [[source-fandom-rewards]], [[source-fandom-template-resources-rewards]]
