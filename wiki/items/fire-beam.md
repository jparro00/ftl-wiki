---
id: item-fire-beam
type: item
item_kind: weapon
rarity: 3
unlocks_blue: [[[event-remote-settlement]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [weapon, beam, fire]
---

# Fire Beam

## Summary
The `BEAM_FIRE` weapon — *"This terrifying beam does no physical damage but ignites fires."*
([[source-text-blueprints]]). The file carries a developer note wondering whether to call it
*"Induction beam?"*.

## Stats
- Blueprint `BEAM_FIRE` (`<weaponBlueprint>`), `<type>BEAM</type>`, [[source-blueprints]].
- Hull damage **0**, `fireChance` **8**, `breachChance` 0, `sp` 0.
- Power **2**, cooldown **20**, beam `length` 140.
- Cost **50** scrap (`<!--was 70-->`), `bp` 6, `rarity` 3.

## How To Get It
- **Stores**, and as `autoReward` `weapon` payouts. Generic reward pools (`RANDOM`, `WEAPONS_*` lists) name no specific blueprint, so most events cannot be attributed to one weapon.
- No event in `raw/gamedata/` awards `BEAM_FIRE` by name.

## Blue Options It Unlocks
- [[event-remote-settlement]] — `PIRATE_STATION_CROPS` — the same choice list also takes [[item-fire-bomb]]

## Strategy Notes
- `sp` 0 and 0 damage: against a shielded ship it does literally nothing, which is the
  weapon's whole risk.
- `fireChance` 8 versus [[item-fire-bomb]]'s 10, but the beam sweeps multiple rooms per shot
  and costs no missiles.

## Related
- [[item-fire-bomb]] — shares its only blue option
- [[item-anti-bio-beam]] — the other 0-damage beam
- [[item-beam-weapons]] — the `WEAPONS_BEAM_DAMAGE` category, which excludes this weapon

## Open Questions
- [ ] Whether `fireChance` 8 vs 10 is a meaningful difference — the units are undefined.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
