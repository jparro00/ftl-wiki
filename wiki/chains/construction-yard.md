---
id: chain-construction-yard
type: chain
trigger_event: [[[event-space-station-under-construction]]]
steps: [[[event-space-station-under-construction]]]
sectors: [[[sector-civilian-sector]], [[sector-federation-space]]]
reward: "1 of 3 destinations: a PDS fight for med/high scrap, an abandoned-station gamble, or a fuel-for-scrap trade"
version: ae
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
tags: [quest, lanius, blue-option, sell-a-crewmember, pds, fuel-cost]
---

# The construction yard

## Summary
A half-built space station has lost contact with its supply ship and asks you to find out why.
Ordinary enough — but the opening beacon carries **the strangest blue option in the game**:
with a Lanius crew member aboard, you can solve their problem on the spot, and they will then
offer to **buy your crewmate**. You are asked to consult the crew member first, and the file
carries a line for what happens if you have a Clone Bay: *"Your clonebay obviously does not
revive your crewmember since they did not die."*

The quest proper is a 3-entry destination table, one of which is a Rebel station fight
conducted **under Anti-Ship Battery fire**.

## How It Starts
- Trigger: [[event-space-station-under-construction]] (`QUEST_CONSTRUCTIONYARD`)
  ([[source-newevents]]). *"We recently lost contact with a cargo ship that was set to deliver
  more construction materials. Could you help us figure out what happened to them?"*
- Three routes:

  | Choice | Requirement | Result |
  |---|---|---|
  | Offer your help | — | supplies, then `<quest event="QUEST_CONSTRUCTIONYARD_LIST"/>` |
  | Decline | — | *"I understand." Transmission has been cut.* |
  | **(Lanius Crew) Offer to have your crewmember help** | Lanius crew | the station's parts problem is solved on the spot — **and the quest never happens** |

## The Lanius branch — selling a crew member

Your Lanius converts base metal sheets into the specialised parts the yard needs, and the
foreman asks to buy them: *"This robot thing could save us a ton of time. Could I buy it off
you?"* ([[source-newevents]])

| Choice | Outcome |
|---|---|
| **Ask your crew if they agree** | *"Once your Lanius crewmember understands the situation it appears to like the idea of assisting with construction in deep space. Much less dangerous."* — you **lose the Lanius**, they offer goods in exchange |
| **Our crew is not for sale** | *"In terms of payment, here's some of the scrap metal we don't need now that we've got necessary parts."* |

This is one of very few events where a crew member leaves willingly and permanently, and the
only one that stops to note the Clone Bay does not apply. See [[entity-lanius]].

## Steps

1. **[[event-space-station-under-construction]]** — offer help, take the marker and supplies.
2. **The marked beacon** resolves `QUEST_CONSTRUCTIONYARD_LIST`, 3 entries — **33% each** per
   [[concept-event-list-weighting]] ([[source-newevents]]):

   | # | What you find | Choices |
   |---|---|---|
   | 1 | The cargo ship held at a **Rebel station**, forced to *"donate their supplies for the war effort"* | **Attack** → hostile `QUEST_CONSTRUCTIONYARD_SHIP` **plus `<environment type="PDS" target="player"/>`** — an Anti-Ship Battery firing at you throughout · or **Leave** |
   | 2 | The cargo ship docked at an **empty, abandoned station** | **Examine** → hands off to `EMPTY_STATION2_LIST`, the same six-outcome table as [[event-abandoned-station]] · or **stay at the beacon** |
   | 3 | The cargo ship **adrift, out of fuel** | Give **4 fuel** → `MED scrap_only` · give **1 fuel** → nothing but *"better than nothing"* · give none → *"I see…"* |

3. **The fight on entry 1** (`auto_blueprint="SHIPS_REBEL"`) pays `MED standard` on
   `destroyed` and `HIGH standard` on `deadCrew`, and both branches then offer a *"Contact the
   cargo ship"* follow-up worth a further `MED scrap_only` ([[source-newevents]]).

## Requirements
- Nothing to start or finish.
- A **Lanius crew member** for the alternative opening — which is a different reward, not a
  better version of the same one.
- **4 fuel** to take the best branch of destination 3.

## Reward
Highly variable, and one third of the table is a straight loss of fuel for `MED scrap_only`.
Destination 1 is the best on paper — `HIGH standard` plus `MED scrap_only` if you board — but
it is fought under continuous PDS fire.

## Failure Modes
- **Entry 1 under the Anti-Ship Battery.** `target="player"` means the battery shoots only at
  you; a slow kill is punished throughout.
- **Entry 2 is the [[event-abandoned-station]] table**, which contains genuinely bad outcomes
  as well as good ones.
- **Entry 3 at low fuel** — giving 4 fuel for `MED scrap_only` is a poor trade if you are
  short, and giving 1 pays literally nothing.
- The standard quest-marker losses — see [[concept-quest-beacon-placement]].

## Strategy Notes
- *Opinion:* this is the weakest of the civilian quests. One outcome in three is good, one is a
  coin-flip table, and one asks you for fuel.
- With a Lanius aboard, taking the blue option and **refusing the sale** is the cleanest play:
  you get paid, you keep the crew member, and you skip a mediocre destination table entirely.
- Selling the Lanius is defensible only if you are over-crewed and short of supplies. The
  goods offered are not enumerated in the file.

## Related
- [[entity-lanius]] — the crew member the yard wants to buy
- [[event-abandoned-station]] — shares `EMPTY_STATION2_LIST` with destination 2
- [[concept-quest-beacon-placement]], [[concept-event-list-weighting]]
- [[entity-rebels]]
- [[concept-hazards]] — the `PDS` environment on destination 1

## Open Questions
- [ ] What goods the yard hands over for the Lanius — the file states an exchange but the
      payload is not enumerated here.
- [ ] Whether the Lanius branch is available with any Lanius crew member or only a specific one.
- [ ] Whether entry 2's `EMPTY_STATION2_LIST` draw is identical to
      [[event-abandoned-station]]'s, or a subset.

## Sources
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
