---
id: event-auto-bait
type: event
event_name: AUTO_BAIT
sectors: []
beacon_type: unknown
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [rebel, auto-ship, unique, unreachable, cut-content, fleet-advance-risk, no-fandom-page]
---

# Auto-bait (unreachable) — `AUTO_BAIT`

## Summary
A fully authored auto-ship encounter that **is not reachable in the shipped game**. It
inverts [[event-auto-ship-warning]]: the scout is rigged so that *destroying* it summons
the fleet, and the intended play is to leave it alone. Its only reference in any event
list is commented out, and it has no Fandom page — so it is documented here as shipped
content, not as something you can encounter.

## Trigger & Where It Appears
- **Not in any live event list.** The single reference is in the `HOSTILE1` list in
  `raw/gamedata/newEvents.xml`, disabled:

  ```xml
  <event load="AUTO_WARNING"/>
  <!--<event load="AUTO_BAIT"/>-->
  <event load="AUTO_ASTEROID"/>
  ```

  ([[source-newevents]], line 69). The AE replacement list `OVERRIDE_HOSTILE1` in
  `raw/gamedata/dlcEventsOverwrite.xml` does not include it at all
  ([[source-dlceventsoverwrite]]) — so it is dead in both vanilla and Advanced Edition.
- Nothing else in `raw/gamedata/` loads it: the event id appears only in its own
  definition and in the `events_rebel.xml` header comment, which still lists it as a
  hostile event ([[source-events-rebel]]).
- `unique="true"`.
- Sectors: **none**. If the list entry were re-enabled it would inherit `HOSTILE1`'s reach
  (the generic hostile pool used by [[sector-civilian-sector]] and
  [[sector-federation-space]]), but that is a hypothetical, not a fact about the game.

## Text
Shares the `REBEL_AUTO` text list with [[event-auto-ship-fight]] and
[[event-auto-ship-warning]] — **nine variants**, none of them hinting at the trap
([[source-events-rebel]], [[source-text-events-xml]]). The warning arrives only in the
ship's escape text, below.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements)* | — | Combat with `<ship load="REBEL_AUTO_BAIT" hostile="true"/>`. **Destroying it** → `autoReward level="LOW"` `standard` **and** `modifyPursuit amount="1"`. **Letting it escape** → `modifyPursuit amount="1"`. | 100% |

### The `REBEL_AUTO_BAIT` ship
`auto_blueprint="SHIPS_AUTO"`, `<escape timer="2000" min="3" max="4">`
([[source-events-ships]]). The 2000-unit timer is enormous compared to the 40 used by
`REBEL_AUTO_WARNING` — in effect the ship will sit there indefinitely, which is what makes
"leave it alone" a real option.

- **Escape branch text** (the trap warning, delivered once the fight starts):
  > Careful! Sensors indicate that this automated ship is rigged to inform the fleet of
  > your location if destroyed! It is better to avoid risk and leave it alone, otherwise
  > the fleet will find you faster within this Sector.
- **`destroyed`** — *"As the ship breaks apart, you detect the pulse of a Long-Range
  message. It must have informed the fleet of your position."* → `autoReward level="LOW"`
  `standard` **plus** `<modifyPursuit amount="1"/>`.
- **`gotaway`** — *"The scout jumps away. It will certainly have informed the fleet of your
  position. You must get to the next Sector as soon as possible!"* →
  `<modifyPursuit amount="1"/>`.
- No surrender branch, and no crew, so no `deadCrew` payout.

Note that **both** endings advance the fleet. The file provides no branch where you jump
away without paying the pursuit cost — the beacon has no `<choice>` to flee. Whether the
player could simply leave the beacon without engaging is not stated in the files read here.

## Blue Options
None.

## Rewards & Risks
- Reward: `LOW` `standard` at best — the same reduced payout as
  [[event-auto-ship-warning]].
- Risk: fleet advance either way, per the ship definition.

## Strategy Notes
Not applicable — the event cannot occur. Recorded so the content is not silently lost.

## Related
- [[event-auto-ship-warning]] — the shipped, reachable version of the same idea
- [[event-auto-ship-fight]] — shares the same nine intro texts
- [[concept-rebel-fleet-advance]]
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Was `AUTO_BAIT` disabled because the "destroying it hurts you" twist was unreadable
      given it shares intro text with two other events? No dev note states a reason.
- [ ] Whether the beacon could be left without triggering combat at all.
- [ ] Whether any mod-facing tooling still exposes it.

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
