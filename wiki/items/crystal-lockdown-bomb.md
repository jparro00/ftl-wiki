---
id: item-crystal-lockdown-bomb
type: item
item_kind: weapon
rarity: 0
unlocks_blue: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [weapon, bomb, crystal]
---

# Crystal Lockdown Bomb

## Summary
The `BOMB_LOCK` weapon — *"Self-teleporting explosive that does no damage but creates a dense
wall preventing movement in or out of the room. Can target your own ship."*
([[source-text-blueprints]]). The weaponised form of the Crystal crew lockdown power.

## Stats
- Blueprint `BOMB_LOCK` (`<weaponBlueprint>`), `<type>BOMB</type>`, [[source-blueprints]].
- All damage fields **0**; `<lockdown>1</lockdown>` is the whole effect.
- Power **1**, cooldown **15**, 1 shot, consumes 1 missile.
- Cost **45** scrap (`<!--was 60-->`), `bp` 4, **`rarity` 0**.

## How To Get It
- **[[event-crystal-scrap-collector]]** — the `CRYSTAL_SCRAP_EXCITED_LIST` pool awards `<weapon name="BOMB_LOCK"/>` ([[source-events-crystal]]). The only named grant in the event data.
- `rarity` 0 — Crystal-set weapons are not ordinary store stock.

## Blue Options It Unlocks
- **None.** No `<choice req="BOMB_LOCK">` exists anywhere in `raw/gamedata/`.
  ([[source-events-xml]] and the other event files, searched exhaustively)

## Strategy Notes
- One power for a room-seal is the cheapest crowd control in the file; the cost is a missile
  per use and a weapon slot that does no damage.
- Pairs with [[item-teleporter]] boarding: seal the room your boarders are not in.

## Related
- [[item-crystal-burst-mark-ii]] / [[item-heavy-crystal-mark-ii]] — the rest of the Crystal weapon set
- [[event-crystal-scrap-collector]] — where it is awarded
- [[chain-crystal-cruiser-unlock]] — the route these weapons belong to

## Open Questions
- [ ] What `rarity` 0 means for store/reward generation — the blueprint files state the number but never define the scale.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-crystal]] (per raw/gamedata/events_crystal.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
