---
id: event-store-zoltan
type: event
event_name: STORE_ZOLTAN
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: store
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [store, varies-text, guaranteed, repeatable]
---

# Store (Zoltan) — `STORE_ZOLTAN`

## Summary
The Zoltan sectors' store beacon. Purely a store opening with flavour text — no choices,
no cost, no risk. Notable for its allocation: **exactly two per sector, guaranteed**.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: **store**, no ship on Long-Ranged Scanners
  ([[source-fandom-store-zoltan]]).
- Allocated **directly by the sector**, not through an event list:
  `<event name="STORE_ZOLTAN" min="2" max="2"/>` in both `ZOLTAN_SECTOR` and
  `ZOLTAN_HOME` ([[source-sector-data-xml]]). Because `min` equals `max`, **every Zoltan
  sector contains exactly two stores.**
- **Not** `unique="true"` — which is what allows the same event to fill both slots.

## Text
`[varies: textList STORE_ZOLTAN]` — drawn from a three-entry text list
(`text_STORE_ZOLTAN_1` … `_3`) with no repeated entries
([[source-events-zoltan]], per raw/gamedata/events_zoltan.xml).

The three variants ([[source-text-events-xml]]):

1. *The Zoltan are fascinated by other species, and have set up something of an alien knick-knack shop here. Why not take a look?*
2. *A human ship hails: "My friends! Please, there is nothing I don't have, and there is nothing worth wanting that I can't get. Why not take a look around my shop?"*
3. *A Mantis crew here has hunkered down in the abdomen of a long-dead space-whale - the only way, presumably, for them to operate their black-market trade without detection. Worth a look?*

Fandom's three bullets match the three game strings exactly and in order
([[source-fandom-store-zoltan]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `<store/>` — **a store opens**. Nothing else. | 100% |

The flavour text has **no mechanical effect**: the Mantis black-market variant and the
Zoltan knick-knack variant open the same store with the same generated stock
([[source-events-zoltan]]).

## Blue Options
None.

## Rewards & Risks
- **Reward:** access to a store — repairs, fuel, missiles, drone parts, and whatever
  weapons/drones/augments/crew the stock roll produced.
- **Risk:** none.

## Strategy Notes
- *Opinion:* the guaranteed **two stores** is the main reason to like Zoltan sectors
  strategically, and it partly offsets how hard the sector's Super Shield fights are on
  an under-equipped ship. Two guaranteed repair-and-restock points per sector is a strong
  floor.
- Because the store count is fixed at exactly two (not a range), route planning can
  count on it — but neither source here states what stock the stores carry, so the
  *quality* of those two stops is unknown in advance.

## Related
- [[event-empty-beacon-zoltan]], [[event-start-beacon-zoltan]] — the other structural,
  textList-driven Zoltan events
- [[event-zoltan-trade-hub]] — the other way to open a store in a Zoltan sector, via an
  event branch rather than a store beacon
- [[concept-stores]] — how store stock is generated

## Open Questions
- [ ] Does `STORE_ZOLTAN` roll any special or Zoltan-themed stock, or is it the generic
      store table? Nothing in the event suggests special stock.
- [ ] Are the three text variants equally likely?

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-store-zoltan]] (per raw/wiki/store-zoltan.md)
