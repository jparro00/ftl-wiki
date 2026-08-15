---
id: event-merchant-investigate
type: event
event_name: MERCHANT_INVESTIGATE
sectors: []
beacon_type: quest
hostile: false
blue_options: [[[item-teleporter]]]
chain: [[[chain-merchant-s-request]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [quest-destination, crew-reward, weapon-reward, blue-option, pirate-fight]
---

# Merchant's investigation — `MERCHANT_INVESTIGATE`

## Summary
The investigation destination of [[event-merchant-s-request]]. You search for a missing
freighter and find one of three things: **its wreck** (free `MED standard` plus cargo),
**its stranded crew** (a free crew member if you play nice), or **the ship still being
chased by a pirate** (an unavoidable fight). Every non-combat branch then lets you either
chase a second quest marker for a guaranteed drone schematic, or crack the cargo open now
for a gamble that includes a **free random weapon**.

## Trigger & Where It Appears
- **Not in any sector event list.** Reached only via `<quest event="MERCHANT_INVESTIGATE"/>`
  on the investigation branch of `MERCHANT_REQUEST_LIST` ([[source-events-xml]]) — its only
  reference in the game files.
- Sectors depend on where [[event-merchant-s-request]] placed the marker, so the
  frontmatter list is deliberately empty.
- [[source-fandom-merchant-s-request]] documents it as that page's "Merchant's
  Investigation" section, `LRSmap=noship`.

## Text
> You arrive at the last known location of the merchant's delivery. You begin to scan for
> the lost ship.

(`event_MERCHANT_INVESTIGATE_text`, per [[source-text-events-xml]])

A single hidden `continue` choice loads `eventList MERCHANT_INVESTIGATE_LIST`.

## Choices & Outcomes

### `eventList MERCHANT_INVESTIGATE_LIST` (3 entries)
Assuming uniform selection across `eventList` entries ([[concept-event-list-weighting]]),
each scenario is **1/3**.

**Entry 1 — the wreck** *(pays before you choose)*
> You find the remains of the ship. It seems to have severe external damage, but you cannot
> pinpoint a cause. The majority of its cargo seems intact. You manage to discern the
> ship's intended destination.

`autoReward level="MED"` `standard` fires on the entry itself, then:

| Choice | Requirement | Outcome |
|---|---|---|
| Take the cargo and head to its original destination in search of a reward. | — | `<quest event="MERCHANT_INVESTIGATE_DELIVER"/>` → see [[event-merchant-investigate-deliver]] |
| Take the cargo for yourself. | — | Loads `eventList MERCHANT_INVESTIGATE_CARGO_LIST`, below |

**Entry 2 — the stranded crew**
> You find a severely damaged ship floating among some debris. The crew hails you, "I can't
> believe that cheap bastard sent someone after us! I thought we would freeze to death. If
> you help us complete the delivery, we'll share the reward and join your crew."

| Choice | Requirement | Outcome |
|---|---|---|
| Promise to deliver the cargo and ask if any would be interested in joining your crew. | — | *"They upload the delivery destination once on board. One takes you up on your offer…"* → `<crewMember amount="1"/>` **and** `<quest event="MERCHANT_INVESTIGATE_DELIVER"/>` |
| Take the cargo but drop them off at a nearby station. | — | → `MERCHANT_INVESTIGATE_CARGO_LIST` |
| **(Teleporter)** Beam the cargo aboard and leave them to their fate. | `req="teleporter"` | → `MERCHANT_INVESTIGATE_CARGO_LIST` |

The crew member is only on the first branch. The Teleporter option and the "drop them off"
option are mechanically identical — both just route to the cargo list
([[source-events-xml]]).

**Entry 3 — the pirate chase**
> After a quick scan, you find a ship being chased by a pirate. This must be the missing
> delivery ship! You move in to rescue them.

`<ship load="JELLY_PIRATE_MERCHANT" hostile="true"/>` — **no choice, the fight is
unavoidable**. The ship definition has **no `<surrender>` and no `<escape>`**
([[source-events-ships]]): it neither gives up nor runs.

- `destroyed` / `deadCrew` → *"You contact the delivery ship, who are grateful for your
  assistance. They offer you a reward for saving them."* → `autoReward level="MED"`
  `standard`.

### `eventList MERCHANT_INVESTIGATE_CARGO_LIST` (3 entries — 1/3 each)

| Entry | Text | Effect |
|---|---|---|
| 1 | *"The cargo was some food and medical supplies, nothing that you need right now. You make a note of the delivery destination…"* | `<quest event="MERCHANT_INVESTIGATE_DELIVER"/>` — you end up with the marker anyway |
| 2 | *"You find a prototype weapon inside. You quickly install it on the ship."* | `<weapon name="RANDOM"/>` — a **free random weapon** |
| 3 | *"There were general military supplies in the cargo crates. You take what you can use."* | `autoReward level="HIGH"` `standard` |

## Blue Options
- **[[item-teleporter]]** (`req="teleporter"`, entry 2) — flavour only. It loads exactly the
  same `MERCHANT_INVESTIGATE_CARGO_LIST` as the non-blue "drop them off" choice, with no
  extra reward and no cost ([[source-events-xml]]). Worth recording precisely because it
  looks like it should do more.

## Rewards & Risks
- Entry 1 pays `MED standard` unconditionally — the safest of the three rolls.
- Entry 2's cooperative branch is a **free crew member**, the most valuable single outcome
  in this quest line.
- The cargo list is a 1/3 shot at a free random weapon, 1/3 at `HIGH standard`, 1/3 at
  just the follow-on marker.
- Entry 3 is a forced fight against a ship that will not surrender or flee. That is the
  whole risk of the errand.

## Strategy Notes
- On entry 2, taking the crew member also keeps the delivery marker, so the "nice" branch
  loses nothing relative to the cargo branches except the weapon gamble. A guaranteed crew
  member usually beats a 1/3 weapon. *(Opinion, derived from the tables; no source ranks
  them.)*
- On entry 1, cracking the cargo (1/3 weapon, 1/3 `HIGH standard`, 1/3 marker anyway) is a
  genuine gamble against the guaranteed `MED drone` schematic at
  [[event-merchant-investigate-deliver]].

## Related
- [[chain-merchant-s-request]] — the full quest line this belongs to
- [[event-merchant-s-request]] — the quest start
- [[event-merchant-investigate-deliver]] — the follow-on marker
- [[event-merchant-deliver]] — the other errand from the same start
- [[item-teleporter]], [[entity-pirates]]

## Open Questions
- [ ] Confirm `eventList` selection is uniform — every 1/3 above depends on it.
- [ ] Does `<weapon name="RANDOM"/>` draw from the full blueprint pool or a sector-scaled
      one?
- [ ] Is the Teleporter blue option's lack of any distinct reward intentional or an
      oversight?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-fandom-merchant-s-request]] (per raw/wiki/merchant-s-request.md)
