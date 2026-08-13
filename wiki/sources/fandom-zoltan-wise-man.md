---
id: source-fandom-zoltan-wise-man
type: source
source_kind: wiki
raw: raw/wiki/zoltan-wise-man.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [zoltan, scrap-reward, cut-content]
---

# Fandom — "Zoltan wise man"

## Summary
The community wiki page for `ZOLTAN_RIFT_FIGHT`. Retrieved via the MediaWiki API at
revision 73919. Supplies the ship-reward tiers and independently confirms the
commented-out fourth option in the game source.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'ZOLTAN_RIFT_FIGHT' in the
  datafiles."*
- **Supplies what the game files do not:** the ship reward tiers — `low` scrap with
  resources for destroying the hull, `medium` for killing the crew — before the separate
  `ZOLTAN_RIFT_SUCCESS` payout.
- Confirms all three opponents converge on the **same** post-fight structure, so the
  choice of enemy does not change the reward.
- Confirms the Mantis option's ship has a **crew entirely composed of Mantis**.
- **Independently corroborates the cut content:** *"In the datafiles there is a fourth
  option to battle a crystal ship, but the option wasn't finished and is commented out."*
  The game file shows the unfinished `<ship load= ?!?!` and a developer note.
- Locations template: both Zoltan sectors, `unique=true`, Long-Ranged Scanners `noship`.

## Events Covered
- [[event-zoltan-wise-man]]

## Other Pages Touched
- [[entity-mantis]], [[entity-slugs]], [[entity-rock-men]],
  [[concept-cut-content]]

## Reliability Notes
`medium`. States no game version. Gives no loadout information for the three rift ships,
which is the main open question on the event page.

## Contradictions Flagged
None. The page's quoted texts match `text_events.xml` where they overlap, including the
`ZOLTAN_RIFT_SUCCESS` implosion text.

## Links
- Source URL: https://ftl.fandom.com/wiki/Zoltan_wise_man
- [[source-events-zoltan]], [[source-text-events-xml]]
