---
id: item-anti-bio-beam
type: item
item_kind: weapon
rarity: 5
unlocks_blue: [[[event-giant-alien-spiders]], [[event-capture-the-ship]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [weapon, beam, anti-crew]
---

# Anti-Bio Beam

## Summary
The `BEAM_BIO` weapon — *"This terrifying beam does no physical damage but rips through organic
material, dealing heavy damage to crewmembers."* Tooltip: *"2 power beam weapon that greatly
damages enemy crew."* ([[source-text-blueprints]]).

## Stats
- Blueprint `BEAM_BIO` (`<weaponBlueprint>`), `<type>BEAM</type>`, [[source-blueprints]].
- Hull damage: **0**. Crew damage (`persDamage`): **4**.
- Power **2**, cooldown **16**, beam `length` 140, `speed` 13.
- Cost **50** scrap, `bp` 6, **`rarity` 5** — the maximum rarity value in the weapon data,
  shared with only `BEAM_3` (Glaive Beam) and `LASER_CHAINGUN_2` (Chain Vulcan).
- `fireChance` 0, `breachChance` 0, `sp` (shield piercing) 0.

## How To Get It
- **[[event-slug-unlock-surrender]]** — `SLUG_UNLOCK_SURRENDER` awards `<weapon name="BEAM_BIO"/>` ([[source-events-slug]]). The only named grant in the event data.
- **Stores**, and as `autoReward` `weapon` payouts. Generic reward pools (`RANDOM`, `WEAPONS_*` lists) name no specific blueprint, so most events cannot be attributed to one weapon.

## Blue Options It Unlocks
- [[event-giant-alien-spiders]] — `DISTRESS_INFESTATION` — the classic use: clear the infestation from orbit
- [[event-capture-the-ship]] — the `QUEST_CREWDEAD_START_2` sub-event

## Strategy Notes
- `sp` 0 means it does not pierce shields, so both of its blue options are the real
  argument for carrying it — it is an anti-crew tool, not a shield-breaker.
- `rarity` 5 puts it in the three-weapon top tier alongside the Glaive Beam and the Chain
  Vulcan; do not plan a run around finding one.
- Both gates are "there are hostile lifeforms in there" beacons, alongside
  [[item-anti-personnel-drone]] and [[item-boarding-drone]] on the same lists.

## Related
- [[item-anti-personnel-drone]] / [[item-boarding-drone]] — share the `DISTRESS_INFESTATION` choice list
- [[item-fire-beam]] — the other 0-damage beam
- [[item-beam-weapons]] — the `WEAPONS_BEAM_DAMAGE` category, which **excludes** this weapon

## Open Questions
- [ ] Why `BEAM_BIO` is excluded from the `WEAPONS_BEAM_DAMAGE` event list (see [[item-beam-weapons]]) — presumably because it deals no hull damage, but no source says so.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
