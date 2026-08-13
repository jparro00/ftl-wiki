---
id: sector-the-last-stand
type: sector
sector_id: FINAL
sector_class: special
faction: [[[entity-rebels]]]
min_sector: 7
unique: true
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [endgame, flagship]
---

# The Last Stand

## Summary
The final sector. Its pool is entirely boss-specific — no ordinary event lists appear
at all.

## Character & Hazards
`unique="true"`, `minSector="7"`. Every list is a `BOSS_*` list except a single store.
3 guaranteed repair stations, 6 guaranteed hostile beacons.
(per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max | Resolves to |
|---|---|---|---|
| `STORE` | 1 | 1 | a store beacon |
| `BOSS_REPAIR_STATION` | 3 | 3 | [[event-repair-station-in-last-stand]] |
| `BOSS_HOSTILE` | 6 | 6 | [[event-fight-in-last-stand]] (3× duplicated → always this event) |
| `BOSS_NEUTRAL` | 7 | 10 | 1/5 each: [[event-rebel-fight-among-rebel-fleet]], [[event-rebel-fight-among-federation-and-rebel-fleets]], [[event-empty-beacon-last-stand]], [[event-rebel-ship-attacking-civilians-in-last-stand]] |

Start beacon: `BOSS_NEUTRAL`. Entry to the sector is [[event-last-stand-start]] (+10 fuel,
+10 hull).

Every allocation here is fixed except `BOSS_NEUTRAL` — the only sector in the game with
almost no randomness in its beacon mix. `BOSS_HOSTILE` lists `BOSS_SCOUT` three times, so
every hostile beacon here is the same encounter.

## Chains That Run Through It
- The Flagship fight, in three phases: [[event-boss-text-1]] → [[event-boss-text-2]] →
  [[event-boss-text-3]], ending in [[event-boss-destroyed]] or [[event-boss-escaped]].
  See also [[event-federation-base]] and [[event-boss-automated]].
  _A `[[chain-the-flagship]]` page is still to be written._

## Factions & Ships
- [[entity-rebels]] — the Flagship
- [[entity-flagship]]

## Version Differences
The endgame is where Advanced Edition diverges most sharply. Per the `_DLC` blueprints in
`bosses.xml` ([[source-bosses]]):
- **Phase 1** gains **Hacking** (power 3) in AE.
- **Phase 3** gains **Mind Control** (power 3); max power rises 31 → 32.
- **Phase 2** is unchanged.
- All `_EASY_DLC` variants **lose the vanilla Easy-mode shield discount** (6 → 8 shield
  power), so Easy difficulty is harder in AE than in vanilla.

`dlcEventsOverwrite.xml` does not touch any `BOSS_*` list — the event pools themselves are
identical across editions; only the Flagship's loadout changes.

## Strategy Notes
- _None sourced yet._

## Open Questions
- [ ] `blueprints.xml` defines unsuffixed `BOSS_1`/`BOSS_2`/`BOSS_3` carrying systems the
      `bosses.xml` difficulty variants lack (teleporter, sensors, drones). No file states
      which set the game actually loads.
- [ ] `BOSS_WARNING_NODE` is allocated by no `sectorDescription` — its link to the
      fleet-advance warning marker is only implied by an XML comment.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
