---
id: event-trade-resources-in-nebula
type: event
event_name: NEBULA_TRADER
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: nebula
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [nebula, trading, resources, no-risk, unique]
---

# Trade resources in nebula — `NEBULA_TRADER`

## Summary
A barter stall in a nebula. Two choices — trade or ignore — and the trade is a swap of one
resource for another with no scrap involved and no risk of any kind. Crucially, the game
shows you the actual offer before you commit, which turns what looks like a gamble into a
plain yes/no.

## Trigger & Where It Appears
- Beacon: nebula (`<environment type="nebula"/>`). No ship present.
- `unique="true"` — once per run.
- Lists: `NEBULA` ([[source-newevents]]), `NEBULA_PIRATE` ([[source-events-pirate]]) and
  `NEBULA_REBEL` ([[source-events-rebel]]) — reaching Federation Space and Civilian via
  `NEBULA`, Pirate space via `NEBULA_PIRATE`, both Rebel sectors via `NEBULA_REBEL`, and
  the Zoltan sectors and [[sector-uncharted-nebula]] through the nested `NEBULA_REBEL`
  entry in their pools ([[source-sector-data-xml]]).
- Long-range scanners show no ship ([[source-fandom-trade-resources-in-nebula]]).

## Text
> It's hard to see why, but this beacon is apparently a tourist destination. One of the
> ships at the small station is offering a deal.

(`event_NEBULA_TRADER_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Trade. | — | Loads `TRADER_LIST` — one of four fixed swaps, table below. | unknown (4-entry list) |
| 2 | Ignore. | — | Empty `<event/>` — nothing happens. | 100% |

### `TRADER_LIST` — the four offers
Defined in `raw/gamedata/events.xml` and shared with other trader events
([[source-events-xml]]). Each entry is a pure `item_modify`, with no text of its own:

| You give | You get |
|---|---|
| 1–2 drone parts | 5–10 fuel |
| 1–2 fuel | 4–5 missiles |
| 2–3 missiles | 2–3 drone parts |
| 2–4 missiles | 4–10 fuel |

[[source-fandom-trade-resources-in-nebula]] reproduces all four exactly, and adds the fact
the XML cannot express: **the actual trade offer is shown before you choose.** So the roll
happens first and you decide with full information — choice 1 is never a blind commitment.

## Blue Options
None.

## Rewards & Risks
- No scrap changes hands, no hull damage, no combat, no fleet advance. The only cost is the
  resource you give up.
- Three of the four offers are fuel-positive or missile-positive; the drone-parts-for-fuel
  swap is the one that can hurt a drone-heavy build.
- Because you see the offer first, the worst realistic case is that you decline and get
  nothing — identical to choice 2.

## Strategy Notes
- Effectively a free look at a resource conversion. Take choice 1 to see the offer; there
  is no downside to looking, since the outcome is displayed and the deal is only applied if
  you accept.
- Fuel is the resource this event most often hands out (two of four offers), which pairs
  well with nebula sectors, where fuel pressure is highest.
- Two of the four offers spend missiles, which is close to free for a laser/beam ship and
  expensive for a missile-based one — the same offer is worth wildly different amounts
  depending on loadout. *(Opinion; no source ranks the offers.)*

## Related
- [[event-pirate-ship-selling-weapon]] — the nebula's other trade, with real downside risk
- [[event-store-in-nebula-uncharted]] — the sector's actual store
- [[sector-uncharted-nebula]], [[concept-scrap-economy]]

## Open Questions
- [ ] Weights inside `TRADER_LIST` (4 entries, none stated).
- [ ] Whether the offer is re-rollable, or a single fixed draw per visit.
- [ ] Whether the trade is blocked when you lack the resource being asked for.

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-trade-resources-in-nebula]] (per raw/wiki/trade-resources-in-nebula.md)
