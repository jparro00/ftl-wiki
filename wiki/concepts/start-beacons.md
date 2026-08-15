---
id: concept-start-beacons
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
related_events: []
tags: [mechanics, structural, sector-entry, no-choice, worldbuilding]
---

# Start beacons — the sector-entry events

## Definition & Context

Every sector begins on a **start beacon**: the arrival event that fires once, automatically,
when you jump into a new sector. There are **eleven**, one per sector flavour
([[source-events-xml]] and siblings):

`START_BEACON` · `START_BEACON_CRYSTAL` · `START_BEACON_ENGI` · `START_BEACON_LANIUS` ·
`START_BEACON_MANTIS` · `START_BEACON_NEBULA` · `START_BEACON_PIRATE` · `START_BEACON_REBEL` ·
`START_BEACON_ROCK` · `START_BEACON_SLUG` · `START_BEACON_ZOLTAN`

They are **structural events, not encounters**: no choices, no rewards, no ship. Their
`beacon_type` in this wiki is `empty` or `quest`, never a hazard or a fight.

## What they are for

Two jobs, and the second is why one of them matters enormously:

1. **Orientation.** The generic [[event-start-beacon]] states the game's core loop in the
   game's own words — explore the sector, then run for the exit before the Rebel fleet
   arrives. The faction-flavoured versions set the tone for where you have landed.

2. **A guaranteed hook.** Because a start beacon is the one event you are *certain* to see in a
   sector, it is the natural place to hang something that must not be missed.

## The exception that proves the rule

**[[event-start-beacon-crystal]]** is not flavour. It is the hinge between steps 3 and 4 of
[[chain-crystal-cruiser-unlock]]: arriving in [[sector-hidden-crystal-worlds]] plants
`<quest event="CRYSTAL_UNLOCK"/>`, which is why the Crystal Cruiser is guaranteed once you
reach the sector at all. Its `beacon_type` is `quest`, alone among the eleven.

This is the design pattern worth naming: **the game uses the one beacon you cannot avoid to
guarantee a quest it does not want you to miss.** Compare [[event-last-stand-start]], the
scripted arrival in [[sector-the-last-stand]] where Admiral Tully briefs the war plan — the
same mechanism used for narrative rather than for a marker.

## Where It Applies

| Start beacon | Sector | Notable |
|---|---|---|
| [[event-start-beacon]] | generic / [[sector-federation-space]] | states the core loop |
| [[event-start-beacon-crystal]] | [[sector-hidden-crystal-worlds]] | **plants the Crystal Cruiser marker** |
| [[event-start-beacon-nebula]] | [[sector-uncharted-nebula]] | six strings, pure flavour |
| [[event-start-beacon-lanius]] | [[sector-abandoned-sector]] | AE-only |
| [[event-start-beacon-pirate]] | [[sector-pirate-controlled-sector]] | |
| [[event-last-stand-start]] | [[sector-the-last-stand]] | scripted briefing, not a `START_BEACON_*` id |

plus the Engi, Mantis, Rebel, Rock, Slug and Zoltan variants.

## Implications For Play
- Nothing to decide at one — but **arriving in the Crystal sector is itself the reward**, and
  the start beacon is what delivers it.
- The flavour text is the game's only statement of what a sector *is*, which makes these the
  natural citation for sector pages.

## Related
- [[concept-empty-beacons]] — the other structurally-required no-choice event family
- [[chain-crystal-cruiser-unlock]] — the chain the Crystal start beacon carries
- [[concept-quest-beacon-placement]] — why a guaranteed hook matters
- [[concept-sector-event-allocation]] — how the rest of a sector's beacons are filled
- [[event-start-beacon]], [[event-start-beacon-crystal]]

## Open Questions
- [ ] Whether the start beacon occupies a beacon slot in the sector's allocation, or sits
      outside the count.
- [ ] Whether any start beacon other than the Crystal one carries a mechanical payload in
      some sector configuration.
- [ ] `START_BEACON_DEMO` / `START_GAME` variants — whether they are reachable at all; both are
      currently tagged as dev/demo content.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-crystal]] (per raw/gamedata/events_crystal.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
