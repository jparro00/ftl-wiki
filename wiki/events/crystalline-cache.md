---
id: event-crystalline-cache
type: event
event_name: CRYSTAL_CACHE
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: any
hostile: false
blue_options: [[[item-breach-missiles]], crystal crew, [[item-teleporter]] lvl 2, [[item-engines]] lvl 7]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, weapon-reward, crew-risk, boarding-risk, fuel-risk, blue-option]
---

# Crystalline cache — `CRYSTAL_CACHE`

## Summary
A sealed weapons cache inside an asteroid. Getting in is the first puzzle (three routes,
two of them blue); what is inside is the second, and one of the three interiors is a
singularity trap that costs you a crew member unless you have a second blue option ready.
The payoff on the good branches is a **Crystal weapon** plus low resources.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Pool: one of **6** entries in the `ITEMS_CRYSTAL` event list, allocated exactly twice
  per sector (`min=2 max=2`) ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="true"` — at most once per run
- Beacon: shows **no ship** on Long-Range Scanners
  ([[source-fandom-crystalline-cache]])

## Text
> Odd radar pings from a huge, orbiting asteroid here reveal a Crystalline cache of some
> kind. A deep crater has been sealed over with a thick layer of crystal to keep whatever's
> inside safe - it'd take some serious firepower to break though.

(`event_CRYSTAL_CACHE_text`, per [[source-text-events-xml]]. Fandom transcribes the last
word as "through"; the file says "though" — a typo in the shipped string, not a
disagreement about content.)

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attempt to break through with the weapons you have. | — | Loads `CRYSTAL_CACHE_BREAK` — see below. | — |
| 2 | **(Breach Missiles)** Use a Breach Missile. | `req="MISSILES_BREACH"` | −1 missile, barrier shattered → **Investigate the cache**. | 100% |
| 3 | **(Crystal crewmember)** Have your Crystalline Being recalibrate your weapons. | `req="crystal"` | Barrier gives way at no cost → **Investigate the cache**. | 100% |

### Sub-event: `CRYSTAL_CACHE_BREAK` (choice 1)
Three list entries, two of which are the same failure text
([[source-events-xml]]):

| Entry | Result |
|---|---|
| 1, 2 | *"You fire everything you have, but the crystal barrier remains strong."* → **nothing happens**. |
| 3 | *"…a lucky shot strikes an existing fracture…"* → **Investigate the cache**. |

The file weights it 2 failures to 1 success; neither source states this as a percentage.

### Sub-event: `CRYSTAL_CACHE_LIST` ("Investigate the cache")
All three entry routes converge here. Three entries ([[source-events-xml]],
[[source-fandom-crystalline-cache]]):

| Entry | Result |
|---|---|
| 1 | Forgotten weapons cache → `weapon name="WEAPONS_CRYSTAL"` (**a Crystal weapon**) + `autoReward level="LOW"` **stuff**. |
| 2 | The owners show up → same **Crystal weapon** + LOW stuff, **and** `boarders min="2" max="3" class="crystal"` teleport aboard. |
| 3 | **Singularity booby trap** — a branch of its own, below. |

#### Entry 3: the singularity trap
> You send a crewmember down to check out the cache. The comm goes dead, and shortly
> thereafter massive gravity readings are detected on the asteroid. You must have triggered
> some kind of singularity booby trap!

| # | Choice | Requirement | Outcome(s) |
|---|--------|-------------|-----------|
| 1 | Pull out now! | — | `removeCrew` with `<clone>true</clone>` → **lose the crew member**, but a Clone Bay revives them. |
| 2 | Detonate your entire fuel reserves to escape with your crew and the cargo. | — | `item_modify steal="true"` `fuel −100` → **all your fuel**, plus `weapon name="RANDOM"` + LOW stuff. |
| 3 | **(Improved Teleporter)** Beam your crewmember back on board. | `req="teleporter" lvl="2"` | Crew saved. **Nothing else gained.** |
| 4 | **(Advanced Engines)** Rescue your crewmember and the cargo. | `req="engines" lvl="7"` | Crew saved **and** `weapon name="RANDOM"` + LOW stuff. |

Fandom quantifies the LOW "stuff" reward as fuel 1–3, missiles 1–2, drone parts 1, plus
scrap ([[source-fandom-crystalline-cache]]).

## Blue Options
- **Breach Missiles** (`req="MISSILES_BREACH"`) — costs 1 missile, skips the 2-in-3 chance
  of failing to open the cache at all.
- **Crystal crew member** (`req="crystal"`) — opens the cache for free. Strictly better
  than the Breach Missile route.
- **Improved Teleporter, level 2+** (`req="teleporter" lvl="2"`) — inside the singularity
  branch: saves the crew member at no cost, but forfeits the cargo.
- **Advanced Engines, level 7+** (`req="engines" lvl="7"`) — the best node in the event:
  crew **and** cargo, no cost.

## Rewards & Risks
- **Rewards:** a Crystal weapon (`WEAPONS_CRYSTAL`) or a `RANDOM` weapon, plus low
  resources with scrap.
- **Risks:** 2–3 Crystal boarders (entry 2); a permanently lost crew member (entry 3,
  choice 1, without a Clone Bay); or your entire fuel reserve (entry 3, choice 2).
- Fandom flags two engine quirks worth knowing
  ([[source-fandom-crystalline-cache]]):
  - The "resources and scrap" component **never** yields a bonus weapon, drone schematic
    or augment here, because the guaranteed `<weapon>` grant blocks those auto-reward
    categories in the same block.
  - The fuel-detonation option is **bugged**: no fuel is actually lost if the reward roll
    includes fuel.

## Strategy Notes
- With Crystal crew this is a free weapon at 1/3 odds of hitting the trap branch; without
  any blue option it is a coin-flip on even getting inside, then a 1/3 chance of a crew
  loss. *(Odds of the entry list are from the file's list weighting; the "coin-flip"
  characterisation is the 2-in-3 failure rate, [[source-events-xml]].)*
- If you have neither blue option and no Clone Bay, the honest read is that choice 1 is a
  gamble with a real crew member on the table. *(Opinion.)*

## Related
- [[sector-hidden-crystal-worlds]]
- [[item-breach-missiles]] — unlocks choice 2
- [[entity-crystal-men]] — the boarders on entry 2
- [[event-boarders-crystal]] — the same 2–3 Crystal boarders as a standalone event
- [[event-crystal-scrap-collector]] — the other `ITEMS_CRYSTAL` Crystal-specific entry
- [[concept-blue-options]]

## Open Questions
- [ ] The contents of the `WEAPONS_CRYSTAL` weapon list (blueprints.xml not yet ingested).
- [ ] Whether the sector `rarityList` (which zeroes almost every non-Crystal weapon)
      affects the `RANDOM` weapon grants in the singularity branch.
- [ ] Confirm the fuel-loss bug in the current build.

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-crystalline-cache]] (per raw/wiki/crystalline-cache.md)
