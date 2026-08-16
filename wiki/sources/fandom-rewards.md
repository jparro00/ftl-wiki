---
id: source-fandom-rewards
type: source
source_kind: wiki
raw: raw/wiki/rewards.md
game_version: both
date: 2026-08-14
ingested: 2026-08-16
reliability: medium
tags: [mechanics, rewards, economy, scrap, autoreward, surrender, resolves-open-question]
---

# Fandom — "Rewards"

## Summary
The mechanics page for how events pay out, retrieved at revision 74729. It is the source that
**puts numbers behind `autoReward`** — the wiki's largest standing unknown ([[concept-autoreward-tiers]],
[[concept-scrap-economy]]) — via two transcluded tables captured separately as
[[source-fandom-template-scrap-rewards-normal]] and [[source-fandom-template-resources-rewards]].
It also documents the bonus-item roll, the precedence rules between an `autoReward` and a
guaranteed item reward, and the Lanius variant of the default fight rewards.

## Key Takeaways

- **Scrap scales; resources do not.** Scrap payout is a function of *sector number × tier ×
  difficulty*. Resource payouts (fuel / missiles / drone parts) are flat — the same in sector 1
  and sector 8, on Easy and on Hard.
- **The tier list matches the game files exactly.** Every tier Fandom describes is a tier that
  appears in `raw/gamedata/*.xml`, and the three it calls *unused* (`missiles_only`,
  `droneparts_only`, `item`) appear **zero** times in the event files. See the corroboration
  note below.
- **The bonus-item roll.** `standard` carries **~3%** and `stuff` **~6%** chance of an extra
  weapon, augment or drone schematic on top of the stated payout. This is the first quantified
  probability the wiki holds for either tier.
- **`stuff` is the surrender tier**, "most often used in non-scripted ship surrenders" — and
  ships in the default-reward categories offer **random tier**. If the 6% bonus lands, the
  scrap half of a `stuff` reward is upgraded from low to match the resources tier.
- **Precedence between rewards.** A guaranteed weapon or drone-schematic reward declared
  outside the `autoReward` **suppresses** the bonus roll and **overwrites** the `weapon` /
  `augment` / `drone` tiers; a guaranteed *augment* reward is instead **overwritten by** the
  bonus or by the `augment` tier. So weapons/drones win over the auto-reward and augments lose
  to it.
- **Lanius fights pay differently.** Against Lanius ships in Abandoned sectors: destroying the
  ship can pay **high scrap (1 in 4)**; killing the crew yields **no weapon** but can yield a
  **drone schematic (1 in 8)**, and the fuel chance drops to **1 in 8** from **2 in 9**.
- **Slug surrenders hide their offer.** Most Slug ships do not show the reward before you
  accept, unlike every other surrender — and once revealed it cannot be rejected.
- **`item_modify` is the exact-value mechanism**, `<item_modify><item type="…" min="…"
  max="…"/></item_modify>`, used for costs as well as gains — and **an `autoReward` can
  overwrite an `item_modify`** that awards the same resource, "which causes some bugs".

## Corroboration found in the game files

Fandom's tier list is independently confirmed by a **developer comment in `events.xml`**
(around line 97, in the scratch block above the `*_TEST` events) that documents the tag's
schema in the authors' own words:

```
<autoReward level=<LOW/MED/HIGH/RANDOM>> tag </autoreward>
where tag is
standard  - which is scrap + 2 resources (possible a weapon)
stuff     - less scrap, mostly resources (intended for surrenders)
fuel / missiles / droneparts  - scrap + that resource
fuel_only / missiles_only / droneparts_only - self explanatory
weapon / augment / drone
item - scrap + that thing
```

Two things fall out of it, neither previously recorded here:

1. **It matches Fandom line for line** — including "intended for surrenders" for `stuff`, which
   Fandom reached from behaviour rather than from this comment.
2. **`scrap_only` and `scrap` are in neither list**, yet `scrap_only` is the *second most used
   tier in the game* (92 uses). The developer comment is plainly older than the shipped data.
   See the contradiction below.

## Events Covered
- None specifically. By reference: every event carrying an `<autoReward>`, and the
  `Fights with Default Rewards` / `Fights with Default Rewards (Lanius)` /
  `Events with Stuff rewards` / `Ship surrender Events` categories.
- Named in the text: [[event-pirate-briber]] (worked example of the `stuff` bonus roll).

## Other Pages Touched
- [[concept-autoreward-tiers]] — rewritten around this source
- [[concept-scrap-economy]] — largest open question closed
- [[concept-surrender-offers]] — the reward half of a surrender
- [[concept-blueprint-rarity]] — what the bonus roll can hand you

## Reliability Notes
`medium` by convention. The scrap and resource tables are sourced by Fandom to
**"Calculated FTL"** (Steam guide 2127539536), a third-party datamining/derivation effort this
repo does **not** hold — so these numbers inherit that guide's uncertainty and cannot be
checked against `raw/`. The tier *names and semantics*, by contrast, check out against the
event files exactly, which raises confidence in the page as a whole.

## Contradictions Flagged

> ⚠️ **Two tiers the schema comment does not know about.** The `events.xml` developer comment
> lists 11 tiers and **`scrap_only` is not among them** — yet it is used **92** times, second
> only to `standard`. Fandom *does* document "Scrap only" as live. Reading: the comment is a
> stale design note, and Fandom is right. The 3 uses of bare **`scrap`** remain unexplained by
> either list and stay flagged as a probable typo for `scrap_only`
> ([[concept-autoreward-tiers]]).

> ⚠️ **Difficulty is a reward axis this wiki cannot see.** Fandom states the scrap amount
> depends on game difficulty, and transcludes three tables (Easy / Normal / Hard). Only the
> **Normal** table is held in `raw/`. Every scrap figure in this wiki is therefore
> Normal-difficulty-only and must be labelled as such.

**Not a contradiction:** Fandom's claim that resource rewards do not vary by sector or
difficulty agrees with [[source-fandom-stores-and-resources]], which says the same.

## Gaps in the capture
`rewards.md` transcludes six templates; only two were retrieved. Missing:
`{{Scrap rewards (Easy)}}`, `{{Scrap rewards (Hard)}}`, `{{Default rewards (generic)}}`,
`{{Default rewards (Lanius)}}`, `{{Slug surrender rewards}}`, `{{Events with equivalent
rewards}}`. The default-rewards and Slug-surrender tables are the substantive losses — the
prose here summarises them but gives no per-outcome odds beyond the fractions quoted above.

`rewards.md` and both captured templates are also **absent from `raw/wiki/_manifest.csv`**,
which lists 311 rows and does not include them. Noted, not corrected: `raw/` is the user's.

## Links
- Source URL: https://ftl.fandom.com/wiki/Rewards
- Cited by Fandom: https://steamcommunity.com/sharedfiles/filedetails/?id=2127539536
  ("Calculated FTL")
- [[source-fandom-template-scrap-rewards-normal]],
  [[source-fandom-template-resources-rewards]],
  [[source-fandom-stores-and-resources]], [[source-events-xml]], [[source-events-ships]]
