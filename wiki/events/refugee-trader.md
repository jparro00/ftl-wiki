---
id: event-refugee-trader
type: event
event_name: REFUGEE_TRADER
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-federation-space]], [[sector-zoltan-controlled-sector]], [[sector-pirate-controlled-sector]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [trading, refugee, no-risk, advanced-edition, shared-sub-event]
---

# Refugee trader — `REFUGEE_TRADER`

## Summary
The good half of every refugee encounter. Eight different parent events funnel into this
one node: a refugee ship short on supplies offers a barter — fuel, missiles or drone parts
for one of the others. There is no ambush, no fight and no cost beyond the trade itself.
It is the single most-reused trade sub-event in the Advanced Edition content.

## Trigger & Where It Appears
- **Not in any sector event list of its own.** It is a shared sub-event, reached from four
  hail pools, each fed by two parent events ([[source-newevents]]):

| Hail pool | Entries | `REFUGEE_TRADER` share | Parent events |
|---|---|---|---|
| `REFUGEE_HAIL_LIST` | 8 | **4/8** | [[event-refugee]] (`REFUGEE_NO_DISTRESS`), [[event-refugee-distress]] |
| `REFUGEE_HAIL_LIST_ZOLTAN` | 2 | **1/2** | [[event-refugee-zoltan]], [[event-refugee-distress-zoltan]] |
| `REFUGEE_HAIL_LIST_PIRATE` | 2 | **1/2** | [[event-refugee-pirate]], [[event-refugee-distress-pirate]] |
| `REFUGEE_HAIL_LIST_SLUG` | 2 | **1/2** | [[event-refugee-slug]], [[event-refugee-distress-slug]] |

  Shares assume uniform selection across list entries ([[concept-event-list-weighting]]).
  Every non-trader entry in those pools is an ambush fight, so these numbers are also the
  odds of *not* being ambushed after hailing a refugee.
- Sectors are inherited from the parents; the list above is their union. The event itself
  has no allocation ([[concept-sector-event-allocation]]).
- **Version: `ae`.** The definition sits in `newEvents.xml`, a base file with no DLC marker
  of its own — but **every** list entry that reaches its parents is `<!--DLC-->`-wrapped
  (`newEvents.xml` lines 112, 141, 218; `events_engi.xml` line 92;
  `dlcEventsOverwrite.xml` lines 153, 176). There is no vanilla path into the refugee
  family, so the event is Advanced Edition content despite its file
  ([[source-newevents]], [[source-events-engi]], [[source-dlceventsoverwrite]]).
- No Fandom page joins this id; the community wiki folds the trade into each refugee page.

## Text
> The vessel is relieved to hear from you! They are running low on supplies. They suggest a
> trade.

(`event_REFUGEE_TRADER_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Trade with them. | — | Loads `TRADER_LIST` (defined in `events.xml`) — four entries, no repeats, **1/4 each** assuming uniform selection. See table below. | — |
| 2 | Politely decline. | — | Empty `<event/>` — nothing happens. | 100% |

### `TRADER_LIST` — the four barters

| Odds | You gain | You pay |
|---|---|---|
| 1/4 | 5–10 fuel | 1–2 drone parts |
| 1/4 | 4–5 missiles | 1–2 fuel |
| 1/4 | 2–3 drone parts | 2–3 missiles |
| 1/4 | 4–10 fuel | 2–4 missiles |

All four entries are **pure `<item_modify>` blocks with no `<text>` element at all**
([[source-events-xml]]). The game surfaces the specific offer in the trade UI before you
commit, so the roll is visible rather than blind — which is why there is no prose to quote.

## Blue Options
None. Neither choice carries a `req`.

## Rewards & Risks
- **No risk.** No branch damages you, costs crew, or starts a fight. The worst outcome is a
  trade you did not want, and the offer is shown before you accept.
- The trades are resource swaps, never scrap. Two of four pay fuel, which makes this a
  quiet fuel-stabiliser across long AE runs.
- The cost is upstream: reaching this node at all means having hailed a refugee, which in
  `REFUGEE_HAIL_LIST` carries a 4/8 ambush risk.

## Strategy Notes
- *Opinion:* trade whenever fuel is the offer. Missiles and drone parts are dead weight on
  ships that do not use them, and 5–10 fuel is a meaningful buffer.
- Decline the missiles-for-fuel trade if you are running a missile weapon — 1–2 fuel is
  rarely worth 2–4 missiles late in a run.
- Because the offer is visible before acceptance, there is never a reason to skip choice 1
  outright; open it and then decide.

## Related
- [[event-refugee]], [[event-refugee-distress]] — the widest-reaching parents
- [[event-refugee-zoltan]], [[event-refugee-distress-zoltan]],
  [[event-refugee-pirate]], [[event-refugee-distress-pirate]],
  [[event-refugee-slug]], [[event-refugee-distress-slug]] — the species-specific parents
- [[event-refugee-comms-down]] — the refugee variant with no hail option
- [[concept-event-list-weighting]] — basis for the 1/4 and 4/8 figures
- [[concept-sector-event-allocation]] — why `sectors` is inherited, not allocated

## Open Questions
- [ ] Whether `TRADER_LIST` selection is genuinely uniform.
- [ ] Whether the trade UI lets you back out after seeing the offer, or only before.

## Sources
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
