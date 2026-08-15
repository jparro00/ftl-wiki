---
id: event-auto-ship-near-storage-station-in-nebula
type: event
event_name: NEBULA_AUTO_DEFENSE_ITEM
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: nebula
hostile: false
blue_options: [[[item-cloaking]], [[item-hacking]]]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [nebula, rebel, auto-ship, blue-option, cloaking, hacking, unique, loot]
---

# Auto-ship near storage station in nebula — `NEBULA_AUTO_DEFENSE_ITEM`

## Summary
A guarded Rebel storage station. Six choices — the widest blue-option spread of any event
in `events_nebula.xml` — all funnelling into the same four-entry loot table. The quiet
punchline is that **fighting is not the worst option**: killing the ship pays medium scrap
*and* opens the station, while the stealth routes only open the station.

## Trigger & Where It Appears
- Beacon: nebula (`<environment type="nebula"/>`).
- `unique="true"` — once per run.
- Lists: `NEBULA`, `NEBULA_NEUTRAL`, `NEBULA_NEUTRAL_SLUG`, `NEBULA_REBEL`
  ([[source-newevents]], [[source-events-nebula]], [[source-events-slug]],
  [[source-events-rebel]]). `NEBULA_NEUTRAL` is allocated 7–8 per
  [[sector-uncharted-nebula]] and `NEBULA_NEUTRAL_SLUG` 3–5 per Slug sector
  ([[source-sector-data-xml]]).
- Arrives non-hostile: `<ship load="REBEL_AUTO_ITEM" hostile="false"/>`. Long-range
  scanners show a ship ([[source-fandom-auto-ship-near-storage-station-in-nebula]]).

## Text
> An advance Rebel automated ship remains stationed near a small Rebel space-station.
> However, without functioning sensors it is impossible to tell what is inside.

(`event_NEBULA_AUTO_DEFENSE_ITEM_text`, per [[source-text-events-xml]]. "An advance" is
the game's own wording; Fandom marks it `[sic]`.)

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the automated ship to get to the station. | — | Fight `REBEL_AUTO_ITEM`. On destruction: *"You salvage what you can from the broken ship."* → `autoReward level="MED"` / `scrap_only`, then a hidden **"Investigate the station"** choice → `DEFENSE_ITEM_LIST`. | 100% |
| 2 | Avoid provoking the ship. | — | Empty `<event/>` — nothing happens. | 100% |
| 3 | **(Cloaking)** Attempt to stealthily access the space station. | `req="cloaking" lvl="1"` (`max_group="0"`) | `NEBULA_AUTO_DEFENSE_ITEM_CLOAK`, two entries: **(a)** *"You successfully sneak by the ship…"* → `DEFENSE_ITEM_LIST`; **(b)** *"You try to sneak past the automated ship but it quickly turns and attacks!"* → fight. | unknown (2-entry list) |
| 4 | **(Improved Cloaking)** Use your stealth to access the space station. | `req="cloaking" lvl="2"` (`max_group="0"`) | *"You successfully sneak by the ship and access the station undetected."* → `DEFENSE_ITEM_LIST`. No fight risk. | 100% |
| 5 | **(Hacking)** Try to hack the station to prevent an alert. | `req="hacking" lvl="1"` (`max_group="1"`, `hidden="false"`) | `NEBULA_AUTO_DEFENSE_ITEM_HACK`, two entries, **both costing −1 drone part**: **(a)** success → `DEFENSE_ITEM_LIST`; **(b)** *"…the automated ship notices and turns to attack!"* → fight. | unknown (2-entry list) |
| 6 | **(Improved Hacking)** Hack the station to prevent an alert. | `req="hacking" lvl="2"` (`max_group="1"`, `hidden="false"`) | −1 drone part, *"…accessing the station completely undetected."* → `DEFENSE_ITEM_LIST`. No fight risk. | 100% |

### The station loot — `DEFENSE_ITEM_LIST`
Defined in `raw/gamedata/events_rebel.xml` and shared with several other Rebel-station
events ([[source-events-rebel]]). Four entries:

| Outcome | Payload |
|---------|---------|
| *"The station was either abandoned or stripped clean…"* | nothing |
| *"…designed to outfit Rebel ships with Drone Systems. You find a functioning Schematic."* | `autoReward level="LOW">drone` |
| *"…a storage site for military grade weapons."* | `autoReward level="LOW">weapon` |
| *"…a storage site for various resources. You salvage everything possible."* | `autoReward level="MED">stuff` |

The XML states no weights, so a 1-in-4 read is an assumption, not a source.

## Blue Options
- **[[item-cloaking]] level 1** (`req="cloaking" lvl="1"`) — a gamble: half the branch
  sneaks you in free, half turns into the fight you were trying to avoid.
- **[[item-cloaking]] level 2** (`lvl="2"`) — the same access, guaranteed, still free.
- **[[item-hacking]] level 1** (`req="hacking" lvl="1"`) — **costs 1 drone part either
  way**, because the `item_modify` sits inside both branches of the sub-list, not on the
  choice. Strictly worse than level-1 Cloaking: same coin-flip, plus a resource cost.
- **[[item-hacking]] level 2** — guaranteed access for 1 drone part.

Choices 3–4 share `max_group="0"` and choices 5–6 share `max_group="1"`, which is how the
file keeps the level-1 and level-2 variants of each system from both appearing at once.
The Hacking options are `hidden="false"` (their cost is shown up front); the Cloaking ones
are `hidden="true"`. Both Hacking choices are AE-only — the XML marks them `<!--DLC-->`
([[source-events-nebula]]).

## Rewards & Risks
- Best expected haul: **choice 1**, because it is the only route that pays
  `MED` / `scrap_only` for the kill *on top of* the station roll — provided you can win the
  fight cleanly.
- Choices 4 and 6 are the safe routes; 6 costs a drone part, 4 costs nothing.
- Risk: choices 3 and 5 can drop you into the fight anyway, and 5 has already spent the
  drone part when it does.
- The station roll can come up empty regardless of how you got in.

## Strategy Notes
- With Cloaking level 2 this is a free loot roll. With Cloaking level 1 only, taking the
  fight is often the better play if your guns can handle an auto-ship, since the fight
  route pays extra scrap and the sneak route pays none.
- Level-1 Hacking is the trap option here — it is dominated by level-1 Cloaking and costs a
  drone part on both outcomes. *(Opinion, derived from the XML above; no source states it.)*
- Fandom notes this is the more blue-option-rich twin of the non-nebula
  `Auto-ship near storage station` event
  ([[source-fandom-auto-ship-near-storage-station-in-nebula]]).

## Related
- [[event-auto-ship-fight-in-nebula]] — the same auto-ship with no choices
- [[event-auto-ship-warning-in-nebula]]
- [[item-cloaking]], [[item-hacking]], [[concept-rebel-fleet-advance]]
- [[sector-uncharted-nebula]], [[sector-slug-home-nebula]]

## Open Questions
- [ ] Weights inside `DEFENSE_ITEM_LIST` and inside both two-entry sub-lists.
- [ ] Numeric values behind `LOW`/`MED` for the `drone` / `weapon` / `stuff` payload types.
- [ ] Whether the "Investigate the station" choice after the fight can be declined (it is
      `hidden="true"` with `text id="continue"`, suggesting it is the only continuation).

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-rebel]] (per raw/gamedata/events_rebel.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-auto-ship-near-storage-station-in-nebula]] (per raw/wiki/auto-ship-near-storage-station-in-nebula.md)
