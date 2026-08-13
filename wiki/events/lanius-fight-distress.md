---
id: event-lanius-fight-distress
type: event
event_name: LANIUS_DISTRESS_TRAP
sectors: [[[sector-abandoned-sector]]]
beacon_type: distress
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [lanius, combat, distress, no-choice, unique, advanced-edition]
---

# Lanius fight distress — `LANIUS_DISTRESS_TRAP`

## Summary
The Abandoned Sector's "answering a distress call gets you shot" event. Whatever was
calling for help has already been eaten; the Lanius that ate it now wants your hull. No
choices — the fight starts on arrival.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `DISTRESS_BEACON_LANIUS`, allocated `min=1 max=2` beacons per sector
  ([[source-sector-data-xml]]). That list has twelve members, none duplicated, so **1/12**
  per distress beacon *assuming uniform selection across list entries*
  ([[source-dlcevents-anaerobic]]).
- Carries `<distressBeacon/>`, so the beacon is flagged as a distress signal on the map
  before you jump.
- `unique="true"` — at most once per sector.
- Long-range scanners show a ship ([[source-fandom-lanius-fight-distress]]).

> **AE-only** — Advanced Edition file, Advanced Edition sector.

## Text
> You are too late - whatever once was emitting the distress signal from this system drew
> a Lanius ship as well as your own. Having consumed the original target, the Lanius turn
> their attention to your vessel.

(`event_LANIUS_DISTRESS_TRAP_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none)_ | — | Immediate combat with `LANIUS_SHIP`; **default Lanius rewards**. | 100% |

Reward tables (including the surrender option and the 1/8 free crew member on dead crew):
[[event-lanius-fight]].

## Blue Options
None.

## Rewards & Risks
- Reward: default Lanius rewards ([[event-lanius-fight]]).
- Risk: this is one of twelve things a distress beacon in this sector can be, and three of
  the twelve are Lanius fights of some kind. Answering distress calls here is not free.

## Strategy Notes
- File this under the general Abandoned Sector rule: distress beacons in this sector are
  more likely to be a fight than a gift. If your hull is thin, the distress beacon is not
  the safe detour it is in a Civilian sector.

## Related
- [[event-lanius-ship-attacking-civilian-distress]],
  [[event-lanius-empty-distress-beacon-1]], [[event-lanius-empty-distress-beacon-2]],
  [[event-lanius-ship-attacking-mantis]] — the other Lanius distress beacons
- [[event-lanius-fight]] — the same ship, and the reward tables
- [[entity-lanius]], [[sector-abandoned-sector]]
- [[event-lanius-surrender]] — the `LANIUS_SURRENDER` aftermath this hull loads

## Open Questions
- [ ] Numeric values behind default Lanius rewards.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-lanius-fight-distress]] (per raw/wiki/lanius-fight-distress.md)
