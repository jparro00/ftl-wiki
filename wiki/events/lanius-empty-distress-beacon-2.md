---
id: event-lanius-empty-distress-beacon-2
type: event
event_name: LANIUS_DISTRESS_TOOLATE
sectors: [[[sector-abandoned-sector]]]
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [lanius, distress, empty, no-choice, unique, advanced-edition]
---

# Lanius empty distress beacon 2 — `LANIUS_DISTRESS_TOOLATE`

## Summary
The second of the Abandoned Sector's two "nothing happens" distress beacons. The signal
dies as you arrive and a scavenger fleet is picking over a battlefield nearby; the game
decides for you that you don't provoke them. No choices, no ship, no reward.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `DISTRESS_BEACON_LANIUS`, allocated `min=1 max=2` per sector
  ([[source-sector-data-xml]]); twelve members → **1/12** *assuming uniform selection
  across list entries* ([[source-dlcevents-anaerobic]]).
- Carries `<distressBeacon/>`; `unique="true"`.
- Long-range scanners show **no** ship
  ([[source-fandom-lanius-empty-distress-beacon-2]]).

> **AE-only.** As with its sibling, Fandom omits the AE category, but the source file and
> the sector are both Advanced Edition.

## Text
> When you get to the beacon you quickly try to locate the source of the distress call. As
> you are looking, the signal blinks out. It is then that you notice the small fleet of
> scavenger ships absorbing debris from a large battle nearby. You can't help but wonder
> where the distress signal came from, but you decide not to risk pressuring the fleet.

(`event_LANIUS_DISTRESS_TOOLATE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none)_ | — | Nothing happens. | 100% |

Note the scavenger fleet is narrative only — the event defines no `<ship>`, so there is
nothing to fight and no option to try ([[source-dlcevents-anaerobic]]).

## Blue Options
None. Notably there is no Lanius-crew option to hail the fleet, unlike most other Lanius
encounters.

## Rewards & Risks
Neither.

## Strategy Notes
- Nothing to play around.

## Related
- [[event-lanius-empty-distress-beacon-1]] — the other empty distress result
- [[event-lanius-fight-distress]] — the version of "you're too late" that does fight you
- [[sector-abandoned-sector]]

## Open Questions
- [ ] Whether an unused Lanius-crew branch for this event exists anywhere (none found in
      `dlcEvents_anaerobic.xml`).

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-lanius-empty-distress-beacon-2]] (per raw/wiki/lanius-empty-distress-beacon-2.md)
