---
id: item-healing-burst
type: item
item_kind: weapon
rarity: 3
unlocks_blue: [[[event-rebel-ship-attacking-federation-loyalists]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [weapon, bomb, crew]
---

# Healing Burst

## Summary
The `BOMB_HEAL` weapon — *"Self-teleporting healing unit that instantly heals all friendly crew
in the room. Can target your own ship."* ([[source-text-blueprints]]).

## Stats
- Blueprint `BOMB_HEAL` (`<weaponBlueprint>`), `<type>BOMB</type>`, [[source-blueprints]].
- `persDamage` **-10** — i.e. it heals 10. Hull damage 0, `sysDamage` 0.
- Power **1**, cooldown **18**, 1 shot, consumes **1 missile** per shot.
- Cost **40** scrap, `bp` 4, `rarity` 3.

## How To Get It
- **[[event-distress-engi-rebel-result]]** — the `DISTRESS_ENGI_REBEL_LIST1` pool awards `<weapon name="BOMB_HEAL"/>` ([[source-events-engi]]).
- **[[event-zoltan-great-eye]]** — the `NEBULA_ZOLTAN_EYE_LIST` pool awards it ([[source-events-zoltan]]).
- **Stores**, and as `autoReward` `weapon` payouts. Generic reward pools (`RANDOM`, `WEAPONS_*` lists) name no specific blueprint, so most events cannot be attributed to one weapon.

## Blue Options It Unlocks
- [[event-rebel-ship-attacking-federation-loyalists]] — `REBEL_VS_FEDERATION_SAVED_LIST`, tagged `<!--DLC!-->` — keep the survivors alive; the AE-only route to a free engineer plus the hidden-base quest marker

## Strategy Notes
- At 1 power it is the cheapest weapon slot in the file to keep filled, and the only one
  that heals.
- Its single blue option is explicitly Advanced-Edition-only: the `<choice req="BOMB_HEAL">`
  in `events.xml` carries a `<!--DLC!-->` marker, so in vanilla that beacon has no healing
  route. ([[source-events-xml]])
- The AE `BOMB_HEAL_SYSTEM` (Repair Burst) is a different blueprint in
  [[source-dlcblueprints]] and satisfies no `req`.

## Related
- [[item-medbay]] / [[item-clone-bay]] — what it substitutes for mid-fight
- [[item-engi-med-bot-dispersal]] — passive healing outside the Medbay
- [[item-teleporter]] — boarding parties are the usual reason to carry it

## Open Questions
- [ ] Whether vanilla replaces the removed `BOMB_HEAL` choice at `REBEL_VS_FEDERATION_SAVED_LIST` with anything.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
