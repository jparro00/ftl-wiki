---
id: event-start-beacon-zoltan
type: event
event_name: START_BEACON_ZOLTAN
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [structural, start-beacon, varies-text, guaranteed, flavour]
---

# Start beacon (Zoltan) — `START_BEACON_ZOLTAN`

## Summary
The arrival beacon for both Zoltan sectors. Mechanically empty — it exists to print one
of four scene-setting strings when you jump in. Guaranteed exactly once per Zoltan
sector, since it is the sector's declared `<startEvent>`.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: the sector's entry beacon. It is **not** drawn from any event list — both
  `ZOLTAN_SECTOR` and `ZOLTAN_HOME` declare
  `<startEvent>START_BEACON_ZOLTAN</startEvent>` ([[source-sector-data-xml]]).
- Fires exactly once per Zoltan sector, on arrival, unconditionally.
- **No Fandom page joins this event** — the community wiki does not document start
  beacons separately. Everything here comes from the game files.

## Text
`[varies: textList START_BEACON_ZOLTAN]` — drawn from a four-entry text list
(`text_START_BEACON_ZOLTAN_1` … `_4`) with no repeated entries, so each is equally
likely ([[source-events-zoltan]], per raw/gamedata/events_zoltan.xml).

The four variants ([[source-text-events-xml]], per raw/gamedata/text_events.xml):

1. *You've entered Zoltan territory. This species is not renowned for giving anything for nothing, but you can always be assured a fair hearing.*
2. *The Zoltan patrol their borders but let you pass when you ID as Federation. Let's hope they won't be so courteous to the Rebels.*
3. *You arrive in Zoltan space. From what you have heard they anticipated the coming war and made preparations to hold their borders.*
4. *You're far from Federation home space here in Zoltan territory, and it's not clear whether the authorities will have any goodwill remaining. Still, you have to push forward.*

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | Nothing happens. The event body contains only a `<text load=...>` element — no reward, ship, store, or effect. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither. This beacon is free and inert.

## Strategy Notes
- Nothing to decide. The value of the page is confirming that **your first beacon in a
  Zoltan sector is always safe** — it can never be a fight, a store, or a distress
  beacon, because the sector hard-codes this event into the start slot.
- The same start event serves both Zoltan sectors, so the arrival text does not tell you
  which of the two you are in. Use the sector name for that
  ([[source-text-sectorname-xml]]).

## Related
- [[event-empty-beacon-zoltan]] — the other inert Zoltan beacon, but allocated 1–2 per
  sector rather than fixed at the entry point
- [[event-store-zoltan]] — the other directly-allocated structural Zoltan event
- [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]] — both declare this
  as their `<startEvent>`

## Open Questions
- [ ] Confirm textList selection is uniform across the four entries.
- [ ] Do the two Zoltan sectors weight the four variants differently? Nothing in
      `sector_data.xml` suggests so — both simply name the same `<startEvent>`.
- [ ] Were all four variants present in vanilla, or were any added in AE?

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
