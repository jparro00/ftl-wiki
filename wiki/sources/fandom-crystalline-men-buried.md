---
id: source-fandom-crystalline-men-buried
type: source
source_kind: wiki
raw: raw/wiki/crystalline-men-buried.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [crystal-sector, crew-risk, weapon-reward, fleet-advance]
---

# Fandom — "Crystalline men buried"

## Summary
The community wiki page for `CRYSTAL_HELP_DIG`. Retrieved via the MediaWiki API at revision
74724. The deepest branch map in this batch, plus the clearest statement anywhere in the
ingested sources of FTL's auto-reward suppression rule.

## Key Takeaways
- Names the in-game id: *"This event is called 'CRYSTAL_HELP_DIG' in the datafiles"*.
- Quantifies the two abandon-your-crew payouts: **2–4 fuel** (cycle 1, `autoReward MED
  fuel`) and **3–6 fuel** (cycle 2, `autoReward HIGH fuel`).
- Records that the **Clone Bay has no effect** on either crew loss — matching
  `<clone>false</clone>` in both `removeCrew` nodes. This is the inverse of
  [[event-crystalline-cache]] and [[event-crystalline-research-facility]].
- Names the wait-twice reward as the **Heavy Crystal Mark II** (`CRYSTAL_HEAVY_2`).
- **Engine note:** *"In the files, the outcome after waiting 2 times includes an
  augmentation with high scrap. However, the free weapon prevents them from being
  awarded."* It then states the general rule: a `<weapon>` or `<drone>` grant blocks
  "weapon", "drone" and "augment" auto-rewards in the same event block, which is also why
  "standard" and "stuff" rewards never include bonuses alongside a free weapon.
- Describes `modifyPursuit amount="1"` as *"Rebel Fleet pursuit is doubled for 1 jump"*.
- Location: Hidden Crystal Worlds, `unique=true`, **ship** on Long-Range Scanners.

## Events Covered
- [[event-crystalline-men-buried]]

## Other Pages Touched
- [[sector-hidden-crystal-worlds]], [[entity-crystal-men]],
  [[item-heavy-crystal-mark-ii]], [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. No game version stated. Its branch structure matches the game file node for node.
The auto-reward suppression rule is the page's own reverse-engineering — plausible,
internally consistent, and repeated on [[source-fandom-crystalline-cache]], but not
confirmed by any game file in `raw/`.

## Contradictions Flagged
None outright. The `autoReward HIGH augment` present in the file but reportedly never
awarded is recorded on [[event-crystalline-men-buried]] as a data-file quirk rather than a
source disagreement, since the page and the file agree on what the file *says*.

## Links
- Source URL: https://ftl.fandom.com/wiki/Crystalline_men_buried
- [[source-events-xml]], [[source-text-events-xml]]
