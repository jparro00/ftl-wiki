---
id: event-lanius-empty-distress-beacon-1
type: event
event_name: LANIUS_DISTRESS_EMPTY
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

# Lanius empty distress beacon 1 — `LANIUS_DISTRESS_EMPTY`

## Summary
A distress beacon that resolves to nothing at all: a plastic satellite looping a message
from settlers who already fled. Pure atmosphere — no choices, no ship, no reward, no risk.
Its only mechanical significance is that it occupies one of the twelve slots in the
Abandoned Sector's distress pool.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `DISTRESS_BEACON_LANIUS`, allocated `min=1 max=2` beacons per sector
  ([[source-sector-data-xml]]); twelve members, none duplicated → **1/12** *assuming
  uniform selection across list entries* ([[source-dlcevents-anaerobic]]).
- Carries `<distressBeacon/>`; `unique="true"`.
- Long-range scanners show **no** ship
  ([[source-fandom-lanius-empty-distress-beacon-1]]).

> **AE-only.** The event lives in `dlcEvents_anaerobic.xml` and only `LANIUS_SECTOR` loads
> that list. Fandom omits the "Advanced Edition Content Events" category on this page, but
> that is a tagging gap on their side, not evidence of vanilla availability.

## Text
> You arrive at the location of the distress signal prepared for a fight, but on first
> glance it's entirely empty. The signal is coming from a small plastic satellite orbiting
> a moon. A looping message describes how settlers have recently abandoned the area due to
> the Lanius threat. You fail to find any other signs of a settlement nearby.

(`event_LANIUS_DISTRESS_EMPTY_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event body is a text tag and a `<distressBeacon/>` tag)_ | — | Nothing happens. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither. The only cost is the jump and the fuel.

## Strategy Notes
- Nothing to play around. Worth knowing only as the reassuring outcome: two of the twelve
  Lanius distress results (this and [[event-lanius-empty-distress-beacon-2]]) are entirely
  empty, which is what makes the sector's distress beacons a gamble rather than a trap.

## Related
- [[event-lanius-empty-distress-beacon-2]] — the other empty result, near-identical role
- [[event-lanius-fight-distress]] — the ambush at the other end of the same pool
- [[sector-abandoned-sector]]

## Open Questions
- [ ] None outstanding — the event is fully specified by two XML tags.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-lanius-empty-distress-beacon-1]] (per raw/wiki/lanius-empty-distress-beacon-1.md)
