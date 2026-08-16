---
id: source-fandom-template-resources-rewards
type: source
source_kind: wiki
raw: raw/wiki/template-resources-rewards.md
game_version: both
date: 2026-08-14
ingested: 2026-08-16
reliability: medium
tags: [mechanics, rewards, economy, fuel, missiles, drone-parts, autoreward]
---

# Fandom — Template: "Resources rewards"

## Summary
The table transcluded into [[source-fandom-rewards]], retrieved at revision 72607. What the
`LOW` / `MED` / `HIGH` levels are worth in fuel, missiles and drone parts. Unlike scrap, these
do **not** scale with sector or difficulty, so this one small table is the whole answer.

## Key Takeaways

| Resource | `LOW` | `MED` | `HIGH` |
|---|---|---|---|
| Fuel | 1–3 | 2–4 | 3–6 |
| Missiles | 1–2 | 2–4 | 4–8 |
| Drone parts | 1 | 1 | 1–2 |

- **Flat across the whole run.** A `HIGH` fuel reward is 3–6 in sector 1 and 3–6 in sector 8,
  on every difficulty. Scrap is the only reward axis that scales
  ([[source-fandom-template-scrap-rewards-normal]]).
- **Drone parts are barely tiered at all** — `LOW` and `MED` are both a flat 1, and `HIGH`
  reaches 2. The level attribute is nearly meaningless on the `droneparts` tier.
- **Missiles have the widest spread**, 1–2 up to 4–8 — a factor of four across levels, against
  fuel's two.
- These figures are the *resource* half of a reward. `standard` and `stuff` pay **2 random
  resources** drawn from these three, plus scrap; the `fuel` / `missiles` / `droneparts` tiers
  pay one named resource plus scrap; `fuel_only` pays this and nothing else
  ([[concept-autoreward-tiers]]).

**Consequence worth stating plainly:** because resources are flat and scrap quadruples by
sector 8, a resource-tier reward is a large payout early and a rounding error late. The same
`HIGH fuel` event is worth taking in sector 1 and worth skipping in sector 8.

## Events Covered
- None. Applies to every `<autoReward>` with a resource component.

## Other Pages Touched
- [[concept-autoreward-tiers]], [[concept-scrap-economy]], [[concept-fuel]],
  [[source-fandom-rewards]]

## Reliability Notes
`medium`. Sourced by Fandom to the third-party "Calculated FTL" Steam guide (2127539536), not
held here. **Independently corroborated on the no-scaling claim** by
[[source-fandom-stores-and-resources]], which states separately that resource rewards do not
vary by sector number or difficulty — two Fandom pages, but the agreement is not circular
within a single article.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Template:Resources_rewards
- [[source-fandom-rewards]], [[source-fandom-template-scrap-rewards-normal]]
