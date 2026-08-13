---
id: event-lanius-trader
type: event
event_name: LANIUS_TRADER
sectors: [[[sector-abandoned-sector]]]
beacon_type: any
hostile: false
blue_options: [lanius crew]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [lanius, item-event, trading, blue-option, unique, no-risk, advanced-edition]
---

# Lanius trader — `LANIUS_TRADER`

## Summary
A resource-for-scrap trade: the Lanius want fuel, missiles or drone parts and pay scrap for
them. The game rolls *which* resource and *how much* before showing you the offer, so the
only real decision is accept or decline. A Lanius crew member unlocks a second, **rerolled**
offer drawn from a better-paying table. No fight, no risk.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] (`LANIUS_SECTOR`) only.
- List: `ITEM_LANIUS`, allocated `min="2" max="4"` beacons per sector
  ([[source-sector-data-xml]]). Five members, none duplicated → **1/5** of any item beacon
  *assuming uniform selection across list entries* ([[source-dlcevents-anaerobic]]).
- `unique="true"` — at most once per run.
- Long-range scanners show **no ship** ([[source-fandom-lanius-trader]]).

> **AE-only.** AE data file, AE sector, no `OVERRIDE_ITEM_LANIUS` in
> `dlcEventsOverwrite.xml` ([[source-dlceventsoverwrite]]).

## Text
`[varies: textList LANIUS_TRADER_TEXT]` — three entries, none duplicated → **1/3 each**
*assuming uniform selection across list entries*. The first carries
`planet="PLANET_POPULATED"`, i.e. it is drawn with a populated-planet backdrop
([[source-dlcevents-anaerobic]]). All three, per [[source-text-events-xml]]:

> Aided by a modified translator, a nearby Lanius scavenger ship messages you, saying,
> "Metal sufficient. Request exchange." It appears there are some Lanius who wish sociable
> interaction with other races.

> A small Lanius craft approaches. You prepare for a fight but they do not seem to be
> carrying any weapons. After a brief moment they message you, although your translator
> struggles with the unfamiliar dialect. It appears they wish to trade.

> You arrive to find a large Lanius vessel laden with recently collected metal. They are
> apparently offering to trade for supplies they are lacking.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Agree to the exchange. | — | Loads `LANIUS_TRADER_LIST` — see below. | 100% |
| 2 | Decline. | — | "They leave without a word." Nothing happens. | 100% |
| 3 | **(Lanius Crew)** Ask for an alternative trade. | `req="anaerobic"` | "After a short discussion you do not understand, the trader comes back with a second proposal." → a fresh accept/decline pair drawing on `LANIUS_TRADER_LIST2`. | 100% |

### `LANIUS_TRADER_LIST` (choice 1)
Three entries, all sharing the flavour string *"After the exchange is complete they leave
without a word."* and differing only in payload → **1/3 each** *assuming uniform selection
across list entries* ([[source-dlcevents-anaerobic]]):

| Trade | You lose | You gain |
|---|---|---|
| Fuel | 3–7 fuel | 15–30 scrap |
| Missiles | 3–7 missiles | 20–40 scrap |
| Drone parts | 3–7 drone parts | 20–40 scrap |

### `LANIUS_TRADER_LIST2` (choice 3 → accept)
Same three-way split, better rates:

| Trade | You lose | You gain |
|---|---|---|
| Fuel | 3–7 fuel | 20–35 scrap |
| Missiles | 3–7 missiles | 25–50 scrap |
| Drone parts | 3–7 drone parts | 25–50 scrap |

Declining after the blue option is still available and still costs nothing.

Fandom notes that **the actual trade offer is displayed before you commit**
([[source-fandom-lanius-trader]]) — the game files do not state this, but they do resolve
the `item_modify` amounts within the loaded event, which is consistent with it.

## Blue Options
- **Lanius crew member** (`req="anaerobic"`) — a **reroll**, not a strict upgrade of the
  offer on the table. Fandom is explicit: *"Using the Lanius blue option will make a new,
  different roll for a resource and its amount and for the scrap reward amount… However, a
  less beneficial outcome (in all regards) is also possible."*
  ([[source-fandom-lanius-trader]]). The XML supports this: choice 3 loads a *different
  list*, so both the resource and the amounts are drawn afresh
  ([[source-dlcevents-anaerobic]]).

## Rewards & Risks
- Best case: 25–50 scrap for 3 drone parts or 3 missiles via the blue option.
- Worst case if you accept badly: 7 fuel for 20 scrap — a real loss if you are low on fuel,
  since fuel cannot be bought back reliably outside stores.
- No fight, no hull risk, no scrap cost. Declining is always free.
- The scrap range is drawn independently of the resource amount, so a 7-missile / 20-scrap
  result is possible.

## Strategy Notes
- *Opinion, derived from the ranges above:* the missile and drone-part trades are the good
  ones; the fuel trade is the trap. Fuel is the resource most likely to end a run.
- With Lanius crew, take the reroll only when the first offer is one you would decline —
  the second offer replaces the first and can be worse.
- Ranges are wide (15–50 scrap). Judge the specific offer, not the category.

## Related
- [[event-lanius-trader-with-translator]] — same trade tables, no blue option, but sells a
  Lanius crew member instead
- [[event-lanius-craftsmen]] — the other `ITEM_LANIUS` trading beacon, scrap → equipment
- [[event-lanius-with-federation-science-craft]] — the free-items member of the same list
- [[sector-abandoned-sector]], [[entity-lanius]], [[concept-blue-options]]

## Open Questions
- [ ] Whether the resource type and the scrap amount are rolled together or independently —
      the file gives them as separate `<item>` ranges inside one `item_modify`.
- [ ] Whether declining after the blue option preserves the original offer (the XML
      structure suggests not — the first proposal is gone).

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-lanius-trader]] (per raw/wiki/lanius-trader.md)
