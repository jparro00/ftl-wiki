---
id: event-lanius-craftsmen
type: event
event_name: LANIUS_RESEARCHER_CRAFT
sectors: [[[sector-abandoned-sector]]]
beacon_type: any
hostile: false
blue_options: [lanius crew]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [lanius, item-event, trading, blue-option, unique, no-risk, advanced-edition]
---

# Lanius craftsmen — `LANIUS_RESEARCHER_CRAFT`

## Summary
A shop in event form. Lanius craftsmen docked with a merchant will melt your scrap into a
specific *category* of Advanced-Edition-only equipment: 45 scrap for an augment, 50 for a
weapon, 40 for a drone schematic. You choose the category, the game chooses the item. A
Lanius crew member knocks **10 scrap off every price**. No fight, no risk — the only cost
is scrap you choose to spend.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] (`LANIUS_SECTOR`) only.
- List: `ITEM_LANIUS`, allocated `min="2" max="4"` beacons per sector
  ([[source-sector-data-xml]]). Five members, none duplicated → **1/5** of any item beacon
  *assuming uniform selection across list entries* ([[source-dlcevents-anaerobic]]).
- `unique="true"` — at most once per run.
- Long-range scanners show **no ship** ([[source-fandom-lanius-craftsmen]]).

> **AE-only.** An Advanced Edition data file, an AE sector, and the reward pools are the
> `DLC_*` blueprint lists — this event cannot exist in vanilla. `dlcEventsOverwrite.xml`
> defines no `OVERRIDE_ITEM_LANIUS` ([[source-dlceventsoverwrite]]).

## Text
> A merchant ship is docked with a Lanius transport. You message them to see if they need
> any help. It turns out they have been studying the Lanius's ability to reshape metal.

(`event_LANIUS_RESEARCHER_CRAFT_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Inquire about the process. | — | Explanation, then the crafting menu below. | 100% |
| 2 | Leave them to their research. | — | "…your mission has a much higher priority at the moment." Nothing happens. | 100% |

### Choice 1 → the crafting menu
Reached after the flavour line *"They respond, 'We haven't the foggiest idea how it works.
They appear to meld part of their bodies into the metal and reshape it…'"*
([[source-text-events-xml]]).

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1a | Give 45 scrap to craft an augmentation. | — | −45 scrap, `<augment name="DLC_AUGMENTS"/>` | 100% |
| 1b | Give 50 scrap to craft a weapon. | — | −50 scrap, `<weapon name="DLC_WEAPONS"/>` | 100% |
| 1c | Give 40 scrap to craft a drone schematic. | — | −40 scrap, `<drone name="DLC_DRONES"/>` | 100% |
| 1d | Decline their offer. | — | Nothing happens. | 100% |
| 1e | **(Lanius Crew)** Offer to help in the process. | `req="anaerobic"` | Reopens the same menu 10 scrap cheaper — see below. | 100% |

### Choice 1e → the discounted menu

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1e-i | Give 35 scrap to craft an augmentation. | — | −35 scrap, `DLC_AUGMENTS` augment | 100% |
| 1e-ii | Give 40 scrap to craft a weapon. | — | −40 scrap, `DLC_WEAPONS` weapon | 100% |
| 1e-iii | Give 30 scrap to craft a drone schematic. | — | −30 scrap, `DLC_DRONES` drone | 100% |
| 1e-iv | Decline their offer. | — | Nothing happens. | 100% |

All prices are exact, not ranges: `<item type="scrap" min="-45" max="-45"/>` and so on
([[source-dlcevents-anaerobic]]). Fandom independently describes the blue option as a flat
"10 scrap discount", which matches the file exactly ([[source-fandom-lanius-craftsmen]]).

## Blue Options
- **Lanius crew member** (`req="anaerobic"`) — a flat −10 scrap on all three prices. Note
  it is **nested one level down**: it does not appear on the opening screen, only after you
  pick "Inquire about the process." If you take "Leave them to their research" you never
  see it ([[source-dlcevents-anaerobic]]).

## Rewards & Risks
- The item pools are the Advanced Edition blueprint lists ([[source-dlcblueprints]], per
  `raw/gamedata/dlcBlueprints.xml`) — `DLC_AUGMENTS` is an 11-entry list (`O2_MASKS`,
  `EXPLOSIVE_REPLICATOR`, `FIRE_EXTINGUISHERS`, `FLEET_DISTRACTION`, `TELEPORT_HEAL`,
  `BATTERY_BOOSTER`, `DEFENSE_SCRAMBLER`, `BACKUP_DNA`, `LIFE_SCANNER`, `ZOLTAN_BYPASS`,
  `HACKING_STUN`), with `DLC_WEAPONS` and `DLC_DRONES` defined alongside it.
- You pick the *category*, never the item. Nothing in the event lets you see or reject what
  you get.
- Risk: only the scrap. There is no `<ship>` tag anywhere in the event.
- You can only craft **one** item — taking a purchase resolves the event.

## Strategy Notes
- *Opinion, derived from the price table:* the drone schematic at 40 (30 with Lanius crew)
  is the cheapest way in, but only pays off with a Drone Control system already installed —
  otherwise it is a scrap-to-sell-value conversion.
- Buying blind from a fixed-price menu is a worse deal than a store, where you see the
  item first. The case for this event is that Abandoned sectors guarantee only 2 stores
  ([[source-sector-data-xml]]) and the `DLC_AUGMENTS` pool contains several augments you
  would otherwise rarely see.
- The blue-option discount is worth roughly 20–25% of the price, and it is the only
  mechanical difference — the item pools are identical either way.

## Related
- [[event-lanius-with-federation-science-craft]] — the other Lanius-scientist beacon, and
  the one that gives items away free
- [[event-lanius-trader]], [[event-lanius-trader-with-translator]] — the resource-for-scrap
  trades in the same `ITEM_LANIUS` list
- [[sector-abandoned-sector]], [[entity-lanius]]
- [[concept-blue-options]]

## Open Questions
- [ ] Full membership of `DLC_WEAPONS` and `DLC_DRONES` (only `DLC_AUGMENTS` is
      transcribed above).
- [ ] Whether the draw from each `DLC_*` list is uniform or rarity-weighted — the
      `<blueprintList>` entries carry no rarity attributes, but blueprint rarity is defined
      elsewhere.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-lanius-craftsmen]] (per raw/wiki/lanius-craftsmen.md)
