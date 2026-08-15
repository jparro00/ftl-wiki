---
id: source-fandom-stores-and-resources
type: source
source_kind: wiki
raw: raw/wiki/stores-and-resources.md
game_version: both
date: 2026-08-15
ingested: 2026-08-15
reliability: medium
tags: [sector, store, economy, fuel, rarity, routing]
---

# Fandom — "Stores and resources"

## Summary
The store and resource mechanics page, retrieved at revision 74856. It supplies the
per-sector store economy (via two transcluded tables, captured separately as
[[source-fandom-template-stores-number-of-stores-by-sectors]] and
[[source-fandom-template-stores-additional-stores-from-events-by-sectors]]), the rules that
decide what a store stocks, and the out-of-fuel mechanics that govern waiting at a beacon.

## Key Takeaways
- **Store contents**: unlimited hull repairs, limited fuel/missiles/drone parts, and 2–4
  *slots* of systems / weapons / drones / augments / crew, each slot holding 3 random
  entries. Never duplicate weapons, drones or augments; crew **can** duplicate.
- **Hull repair price scales with sector number**; resource prices are fixed. Fuel is
  3 scrap in a store, 2 scrap at a refuelling-station event.
- **System-slot rules**: if you have fewer than 11 systems+subsystems there is a **50%
  chance the first slot is forced to be systems**. Stores never sell a system you own;
  Shields and a medical system are **guaranteed** if you lack them; a drone system is
  guaranteed if the store also sells drones.
- **Rarity 1–5 governs store stock and event-reward eligibility per sector**; rarity 0 means
  unobtainable randomly. "Every sector has a table of loot which then gets weighted by its
  rarity" — this is the `<rarityList>` block in `sector_data.xml`. Crystal weapons and crew
  exist only in Hidden Crystal Worlds (one Zoltan event excepted); **Lanius crew only in
  Abandoned sectors**.
- **Resource rewards do not scale** with sector number or difficulty — unlike scrap.
- **Fuel and waiting**: 16 fuel at start, 1 per jump including backtracking. With 0 fuel the
  map offers **Wait**, which advances the Rebels exactly as a jump would — and is slowed by
  a nebula exactly as a jump would be. Turning the distress beacon on before waiting raises
  the chance of a ship arriving (hostile or friendly) and therefore of getting fuel.
- **Out-of-fuel combat**: every enemy starts charging FTL and leaves after ~90s. An
  anti-stalemate rule ends the fight with **+2 fuel** if the enemy is below roughly 30–50%
  hull and takes no further damage for 60s.
- **Store bugs worth routing around**: reloading at an event-generated store deletes it;
  leaving the store UI with boarders aboard deletes it; reloading at any store re-rolls crew
  skills and forces Drone Control to come with a Defence Drone Mk 1. With **AE content off**
  there is a bug that very often leaves item slots empty.

## Events Covered
- By reference: the trading-event, resource-reward, resource-loss, out-of-fuel
  (distress on/off) categories; [[event-large-trade-station]], [[event-pirate-briber]],
  [[event-escort-civilians]], [[event-zoltan-trade-hub]], [[event-slug-drink]],
  [[event-settlement-mercenary-work]], [[event-lone-lanius-ship]].

## Other Pages Touched
- Every page in `wiki/sectors/`, [[concept-scrap-economy]], [[item-fuel]],
  [[entity-lanius]]

## Reliability Notes
`medium`. The system-slot 50% rule is sourced to a message-wall thread with Mike Hopley,
and the page links reverse-engineered store data at xftl. The out-of-fuel anti-stalemate
hull threshold is explicitly hedged ("likely below 50%, closer to 30–40%") and carries an
open `@todo` on the page — do not treat it as a number.

## Contradictions Flagged
None against `sector_data.xml`. The guaranteed-store counts in the transcluded table match
the `STORE*` lines of every sector definition (see
[[source-fandom-template-stores-number-of-stores-by-sectors]]).

## Links
- Source URL: https://ftl.fandom.com/wiki/Stores_and_resources
- [[source-fandom-sectors]], [[source-fandom-beacons]], [[source-fandom-scrap]],
  [[source-sector-data-xml]]
