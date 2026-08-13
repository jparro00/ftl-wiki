---
id: event-federation-deserters
type: event
event_name: CRYSTAL_FED_DESERTER
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, map-reveal, scrap-cost, combat-optional, federation]
---

# Federation deserters — `CRYSTAL_FED_DESERTER`

## Summary
A Federation warship that ran from the fleet and hid in the Crystal sector. Paying them
off reveals the sector map — genuinely valuable in a sector you cannot navigate by
reputation — and the Fandom page notes this is **the only event in the game where you can
attack a non-pirate Federation ship**.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Pool: one of **10** entries in the `NEUTRAL_CRYSTAL` event list, allocated exactly **12**
  times per sector (`min=12 max=12`) ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="true"` — at most once per run
- Beacon: shows a **ship** on Long-Range Scanners — the Federation ship is present from
  the start as `<ship load="FED_SHIP" hostile="false"/>`
  ([[source-events-xml]], [[source-fandom-federation-deserters]])

## Text
> For a moment you assume it's a glitch, but no... you've found a Federation military ship!
> They hail you and, after some probing, reveal that they deserted the Federation fleet
> before stumbling into this sector while seeking refuge.

(`event_CRYSTAL_FED_DESERTER_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Offer supplies. | — | `item_modify`: fuel **−3 to −1**, scrap **−25 to −15**; then `reveal_map` → **the current sector map is revealed**. | 100% |
| 2 | Attack the traitors. | — | `ship hostile="true"` → fight the `FED_SHIP` already present, **default rewards**. No surrender, no escape branch on `FED_SHIP`. | 100% |
| 3 | Leave them be. | — | *"You send them a friendly warning regarding the armada of Rebel ships pursuing you…"* Nothing happens. | 100% |

Choice 1 is the only **non-hidden** choice in the event (`hidden="false"`), meaning its
cost is shown up front; choices 2 and 3 are `hidden="true"`
([[source-events-xml]]). Fandom renders the cost as 15–25 scrap and 1–3 fuel
([[source-fandom-federation-deserters]]) — the same range the file states.

## Blue Options
- None.

## Rewards & Risks
- **Choice 1:** costs 15–25 scrap and 1–3 fuel; gains a full sector map reveal. In
  [[sector-hidden-crystal-worlds]] that means seeing where the 6–10 hostile beacons and
  2–3 stores are before committing jumps ([[source-sector-data-xml]]).
- **Choice 2:** default `FED_SHIP` rewards for a kill, and no way for them to surrender or
  flee.
- **Choice 3:** free, nothing gained.

## Strategy Notes
- The map reveal is worth more here than in most sectors, because you cannot choose your
  exit sector afterwards and the hostile density is the highest in the game
  ([[source-fandom-ancient-device]], [[source-sector-data-xml]]). *(Opinion, built on
  those two sourced facts.)*
- Note the fuel cost. This sector has no dedicated refuelling allocation beyond
  `ITEMS_CRYSTAL`, so paying 1–3 fuel on top of scrap is a real charge if you arrived low.

## Related
- [[sector-hidden-crystal-worlds]]
- [[event-crystal-ship-attacking-federation-loyalists]] — the other Federation encounter
  here, where you rescue rather than shoot them
- [[entity-federation]]
- [[concept-map-reveal]]

## Open Questions
- [ ] What "default rewards" resolves to for `FED_SHIP` (`auto_blueprint="SHIPS_FED"`,
      `events_ships.xml` not yet fully ingested).
- [ ] Whether attacking them has any downstream consequence (no source suggests one).

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml, raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-federation-deserters]] (per raw/wiki/federation-deserters.md)
