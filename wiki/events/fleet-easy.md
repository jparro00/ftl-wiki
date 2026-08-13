---
id: event-fleet-easy
type: event
event_name: FLEET_EASY
sectors: []
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [rebel-fleet, structural, engine-event, orphan, no-choice, combat, pds]
---

# Rebel fleet takeover — `FLEET_EASY`

## Summary
What happens when you sit at a beacon the Rebel fleet has just claimed: an elite Rebel
scout engages you while the cruisers behind it shell your position with a planetary-defence
barrage. There are no choices and the reward for killing the scout is a single unit of
fuel — this is a survival encounter, not a farm.

## Trigger & Where It Appears
**Not in any sector event list.** `FLEET_EASY` is a structural event the engine calls by
name when the Rebel fleet overtakes the beacon you are on. Its sibling `FLEET_EASY_BEACON`
is named in the *Fleet Progression* section of the summary comment at the top of
`events.xml`; `FLEET_EASY` itself is not listed there but sits in the same block and
carries the same `<fleet>rebel</fleet>` marker ([[source-events-xml]]).

The `<fleet>rebel</fleet>` element is the tell: it marks the beacon as fleet-held. Every
working member of this family carries it — [[event-fleet-easy-nebula]] is the one that
does not, and it is unreachable.

**No Fandom page joins it**; the slug comes from the in-game id.

### The `_DLC` twin

`FLEET_EASY_DLC` is byte-for-byte the same event with a different id and a *separate but
textually identical* string ([[source-text-events-xml]]). The engine presumably selects
between them by edition. See [[event-fleet-easy-dlc]] — this page covers the base id.

## Text
> The Rebel fleet has found you, and a nearby scout turns to engage. The cruisers in the
> distance are firing on you!

(`event_FLEET_EASY_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | Immediate combat with `LONG_FLEET`, inside `<environment type="PDS" target="player"/>` — an anti-ship battery firing **on you** for the duration. | 100% |

The `LONG_FLEET` ship, on the `SHIPS_REBEL_ELITE` blueprint pool and flagged
`<!-- NEEDS ELITE BLUEPRINT -->` ([[source-events-ships]]):

| Ship result | Outcome |
|---|---|
| Destroyed | `<item_modify><item type="fuel" min="1" max="1"/></item_modify>` — **+1 fuel and nothing else.** No scrap, no `autoReward`. |
| Dead crew | The identical +1 fuel. |
| Surrender | None defined. |
| Escape | None defined. |

That reward shape is the point: an elite Rebel warship that pays one unit of fuel is meant
to be fled, not fought.

## Blue Options
None.

## Rewards & Risks
- **Reward:** +1 fuel if you kill it. That is the entire payout.
- **Risk:** an elite Rebel ship *plus* a hostile PDS barrage hitting your hull on a timer
  regardless of the fight. You cannot out-trade this encounter; you can only leave.

## Strategy Notes
- Jump. The event exists to punish loitering at a beacon the fleet has reached — the
  reward structure makes no other reading available. *Opinion*, from the ship block.
- Practical consequence: never plan to sit still on a beacon the fleet is one step from.

## Related
- [[event-fleet-easy-dlc]] — the Advanced Edition-id twin, identical content
- [[event-fleet-easy-beacon]], [[event-fleet-easy-beacon-dlc]] — the same situation at the
  sector's **exit** beacon
- [[event-fleet-hard]] — the harder variant, no PDS but framed as unwinnable
- [[event-fleet-easy-nebula]] — the nebula version, shipped but unreachable
- [[event-finish-beacon]] — the exit beacon when the fleet has *not* claimed it
- [[concept-rebel-fleet-advance]], [[concept-rebel-fleet-advance]]
- [[event-fleet-easy-again]] — the commented-out `FLEET_EASY_AGAIN` repeat takeover

## Open Questions
- [ ] How the engine chooses between `FLEET_EASY` and `FLEET_EASY_DLC`; nothing in
      `raw/gamedata/` states the selection rule.
- [ ] What distinguishes `FLEET_EASY` from `FLEET_HARD` in engine terms — hull threshold,
      sector number, or fleet distance? Their prose implies "engage" vs "flee", but no
      source states the condition.
- [ ] Whether the commented-out `FLEET_EASY_AGAIN` (*"Another ship approaches, the
      reinforcements seem endless!"*) was ever live ([[source-events-xml]]).

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — the `LONG_FLEET` block)
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml — the unreachable nebula
  sibling)
