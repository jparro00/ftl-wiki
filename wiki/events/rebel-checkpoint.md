---
id: event-rebel-checkpoint
type: event
event_name: REBEL_CHECKPOINT
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [rebel, filler, scrap-cost, advanced-edition]
---

# Rebel checkpoint — `REBEL_CHECKPOINT`

## Summary
A Rebel inspection post holding up civilian traffic. You can pick a fight, buy the
civilians' freedom for 10–15 scrap, or slip past. Paying is not simply charity — it opens a
hidden follow-up where the freed civilians may repay you, or may turn out to be Federation
loyalists and get you into the fight you were avoiding.

## Trigger & Where It Appears
- Event lists: `NEUTRAL` and `NEUTRAL_EXIT` in `newEvents.xml`, both tagged
  `<!--DLC matt - down below-->` ([[source-newevents]]), plus the Advanced Edition
  replacements `OVERRIDE_NEUTRAL` and `OVERRIDE_NEUTRAL_EXIT`
  ([[source-dlceventsoverwrite]]).
- These are the universal filler and exit pools, so the event can surface in any sector
  that falls back to generic neutrals. Fandom scopes it to the two Slug sectors and marks
  it exit-and-filler ([[source-fandom-rebel-checkpoint]]).
- Not `unique` — it can recur.
- Beacon: ordinary; no distress flag, no environment.

## Text
`[varies: textList REBEL_CHECKPOINT_TEXT]` — four variants
([[source-newevents]], [[source-text-events-xml]]). All four establish the same situation:
a Rebel checkpoint inspecting civilians for Federation ties, and *"The Rebels haven't
noticed you yet."* One sample:

> A rather large fleet of civilian ships are held up at this Beacon. It appears to be a
> Rebel checkpoint; everyone is being inspected for possible ties to the Federation. No one
> has noticed you yet.

Fandom lists all four and they match the `text_REBEL_CHECKPOINT_TEXT_1` … `_4` strings
([[source-fandom-rebel-checkpoint]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Fend for yourself, attack and escape. | — | `<ship load="REBEL" hostile="true"/>` — standard Rebel fight, default rewards. | 100% |
| 2 | Bribe the Rebels to release the civilian ships. | — | −10 to −15 scrap, then a `[varies: textList REBEL_BRIBE_TEXT]` result, then a hidden follow-up choice (below). | 100% |
| 3 | `[varies: textList GENERIC_HIDE_TEXT]` — "Fly behind a moon and stay hidden." / "Shut down all non-vital systems and stay hidden." / "Stay quiet and hope they don't notice you." / "Stay out of their way and charge your FTL drive." | — | `<event/>` — nothing happens. | 100% |

Choice 3's *label itself* is drawn from a text list, so the wording of the third option
changes between encounters while the effect never does ([[source-newevents]], line 1997).

### After bribing
The four `REBEL_BRIBE_TEXT` variants all describe the Rebels taking the scrap and letting
the civilians go. A hidden choice then appears — **"Contact the civilian ships."** — which
loads `REBEL_BRIBE_RESULT`. Four distinct entries; **assuming uniform selection across list
entries**, each is 1/4:

| # | Text | Effect |
|---|------|--------|
| 1 | *"The civilians are grateful. However, none of them seem eager to be mistaken as Federation loyalists so they quickly jump away."* | Nothing. |
| 2 | *"Some of the civilians pool together their excess scrap to try to repay you for your help."* | `autoReward level="LOW"` `scrap_only` |
| 3 | *"One of the civilian ships quietly teleports over a crate of Federation military supplies."* | `autoReward level="LOW"` `standard` |
| 4 | *"One of the civilian ships contacts you and reveals they are Federation loyalists. An eavesdropping Rebel swoops in, destroys the ship, and turns to attack you!"* | `<ship load="REBEL" hostile="true"/>` |

([[source-newevents]], [[source-text-events-xml]]) Derived from list contents, not a stated
percentage.

The scrap loss is applied **before** the follow-up choice, so bribing costs 10–15 scrap
whatever happens next — and 1/4 of the time you pay it and get the fight anyway.

### The `REBEL` ship
`auto_blueprint="SHIPS_REBEL"`, 50% surrender chance (`min=2 max=3`), 50% escape chance
(`min=3 max=4`), `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` — default rewards
([[source-events-ships]]).

## Blue Options
None. There are no `req`-gated choices on this event at any depth.

## Rewards & Risks
- Hiding is a guaranteed clean skip.
- Bribing is −10/−15 scrap for a 1/4 chance of `LOW` `scrap_only`, a 1/4 chance of `LOW`
  `standard`, a 1/4 chance of nothing, and a 1/4 chance of a Rebel fight on top.
- Attacking is a plain Rebel fight with default rewards and no scrap outlay.

## Strategy Notes
- *(Opinion, from the payout structure.)* Bribing is a losing proposition in scrap terms:
  you always pay 10–15 and only half the branches pay anything back, at `LOW` level. If you
  want the fight, choice 1 gives it to you without the bribe.
- Hiding is the correct default on a damaged ship — this is one of the cleanest free skips
  in the filler pool.

## Related
- [[event-rebel-ship-supplying-civilians]] — the other "Rebels and civilians" filler event
  added alongside this one
- [[event-rebel-fight-chance]] — the third of the same DLC batch of Rebel filler events
- [[entity-rebels]]

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Exact scrap values behind `autoReward level="LOW"`.
- [ ] The full sector reach of `NEUTRAL` / `NEUTRAL_EXIT` placement, versus Fandom's
      Slug-only scoping.

## Sources
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-fandom-rebel-checkpoint]] (per `raw/wiki/rebel-checkpoint.md`)
