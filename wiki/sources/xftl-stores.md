---
id: source-xftl-stores
type: source
source_kind: research
raw: raw/modding/2026-08-15-xftl-stores.txt
game_version: both
date: 2026-08-15
ingested: 2026-08-15
reliability: medium
tags: [store, economy, engine-internals, reverse-engineering, external-research]
---

# xftl — reverse-engineered store generation

## Summary
The companion xftl document to [[source-xftl-sector-map]], linked from the Fandom
`Stores and resources` page as its "See also". It describes `Store::OnInit` — how many
sections a store has, how they are chosen, how systems are selected, and the resource
stock ranges.

## Key Takeaways
- **Section count is random 2–4 inclusive.**
- **System sections are disabled** if you have 11 systems+subsystems **and are not playing
  AE**; under AE they are always enabled, because of the medbay/clonebay swap. With fewer
  than 11, there is a **50% chance the first section is systems**.
- **Section override**: if you have no drone system and the store has no systems section,
  any drones section is replaced — in preference order weapons, augments, crew, system.
- **System selection**: the candidate list excludes AE-only systems outside AE, excludes a
  drones system if the store has a drones section, and excludes a medical system unless you
  already own one. Guaranteed offers are **drones** (if the store sells drone blueprints and
  you lack the system), **shields** (if you lack them), and **medbay/clonebay** (if you have
  neither). The store sells `min(list length, 3)` systems — which is why a nearly-complete
  ship can be offered only two.
- **Augments can duplicate what you already own**, including non-stacking ones.
- **Resource stock ranges** — the numbers no Fandom page states: fuel **3–7**, missiles
  **2–6**, drone parts **2–4**.

## Events Covered
- None.

## Other Pages Touched
- [[concept-stores]], [[concept-scrap-economy]], all of `wiki/sectors/`

## Reliability Notes
`medium`, same caveats as [[source-xftl-sector-map]]: disassembly notes by one author, no
upstream revision id, unstated build, hedged in places ("The next bit is a bit weird", "It
appears the same goes for augments"). Read out of the binary, so it outranks the community
wiki on mechanism, but it is not a game file.

## Contradictions Flagged
None. It corroborates [[source-fandom-stores-and-resources]] on the 2–4 sections, the 50%
first-slot-systems rule and the three guaranteed systems, and adds the resource ranges and
the section-override rule that the Fandom page omits.

## Links
- Source URL: https://gitlab.com/znixian/xftl/-/blob/master/doc/stores
- [[source-fandom-stores-and-resources]], [[source-xftl-sector-map]],
  [[source-fandom-template-stores-number-of-stores-by-sectors]]
