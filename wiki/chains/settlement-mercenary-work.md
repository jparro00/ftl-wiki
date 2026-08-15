---
id: chain-settlement-mercenary-work
type: chain
trigger_event: [[[event-settlement-mercenary-work]], [[event-store-rescue]]]
steps: [[[event-settlement-mercenary-work]], [[event-store-rescue]], [[event-quest-store-rescue]]]
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]]]
reward: "a store plus 5 hull and med scrap; or a med weapon for sparing the pirates"
version: ae
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
tags: [quest, mercenary, two-triggers, store, surrender, mercy-reward]
---

# Settlement mercenary work

## Summary
Two jobs offered by the same kind of civilian settlement, feeding one shared destination. Both
are mercenary contracts, and both **pay more for restraint than for killing**: the store-rescue
branch ends in a store opening, and the pirate branch pays a `MED weapon` only if you accept
the pirates' surrender and let them live.

Killing the pirates instead drops the reward to `LOW standard` and the prose says so plainly:
*"With all of the would-be pirates dead, you think it best not to return to the settlement."*

## How It Starts

Two triggers, both planting `<quest event="QUEST_STORE_RESCUE"/>` or opening the pirate job
([[source-events-xml]]):

| Trigger | What is offered |
|---|---|
| [[event-settlement-mercenary-work]] (`MERCENARY_WORK`) | Loads `MERCENARY_WORK_LIST`, a **2-entry** list — 50/50 between the store-rescue contract and the pirate-discipline contract |
| [[event-store-rescue]] (`STORE_RESCUE`, `unique="true"`) | A distress shuttle: *"a small shuttle is asking anyone who'll listen for help protecting their family from a Rebel ship"* → the same `QUEST_STORE_RESCUE` marker |

## Steps

### Job A — rescue the space dock

Reached from either trigger.

1. **Accept** → `<quest event="QUEST_STORE_RESCUE"/>`. The settlement version notes the dock is
   *"technically… illegal within their laws"*, which is why the Rebels are there.
2. **[[event-quest-store-rescue]]** — *"you detect a Rebel scout assaulting a compound on a
   nearby desolate moon."* Two choices:
   - **Engage the Rebel** → a hostile `SQUAT_STORE_RESCUE` (`auto_blueprint="SHIPS_REBEL"`).
   - **Avoid a fight** → *"After a time the ship powers down its weapons and jumps away. No
     life-signs are detected on the moon."* The dock is destroyed and you get nothing.
3. **Winning** — `destroyed` and `deadCrew` pay **identically** ([[source-events-ships]]):
   `autoReward MED scrap_only`, `<damage amount="-5"/>` (5 hull repaired), and `<store/>` — **a
   store opens at the beacon**.

### Job B — discipline the pirates

Reached only from [[event-settlement-mercenary-work]].

1. **Accept** → *"We'll pay you well as long as you don't kill them all"* → an immediate
   hostile `SQUAT_PIRATE_MERCENARY` (`auto_blueprint="SHIPS_PIRATE"`), no marker and no jump.
2. **The ship carries a `<surrender>` with no `chance` attribute** at `min="3" max="4"` hull
   ([[source-events-ships]]) — one of the four such blocks in the game, whose default is
   undocumented. See [[concept-surrender-offers]]. On surrender:

   | Choice | Outcome |
   |---|---|
   | Let them live and return to the settlement | ship goes non-hostile → `autoReward MED weapon` |
   | *"Forget your promise, they die!"* | nothing at all — an empty `<event/>` |

3. **Destroying them or killing the crew** pays `autoReward LOW standard`, both branches
   sharing one text.

## Requirements
- None. No gates anywhere in either job.
- Fuel for one extra jump on job A; job B fights at the beacon you are already on.

## Reward
- **Job A:** `MED scrap_only`, 5 hull repaired, and a **store** — see [[concept-stores]] for
  why an extra store is worth more than its scrap value.
- **Job B, sparing them:** `MED weapon`.
- **Job B, killing them:** `LOW standard` — the worst outcome available, and worse than the
  surrender branch by a full tier plus an item.

## Failure Modes
- **Avoiding the fight at job A** destroys the dock and pays nothing. The choice is presented
  neutrally, but there is no hidden benefit to walking away.
- **Killing the pirates in job B**, whether by hull damage or boarding, forfeits the weapon.
  The danger is real: `SHIPS_PIRATE` is a fragile hull and the surrender window is 30–40%.
- **Refusing the surrender after it fires** is worse still — the *"they die!"* branch resolves
  to a literally empty event, so you get neither the weapon nor the `LOW standard`.
- The standard quest-marker losses on job A — see [[concept-quest-beacon-placement]].

## Strategy Notes
- *Opinion:* both jobs are worth taking, and both reward the patient play. On job B, stop
  shooting once the pirate is low and wait for the offer.
- Job B's *"kill them anyway"* branch is the only choice in this chain that is strictly
  dominated — it pays nothing where every other route pays something.
- Job A's store is the real prize in a sector that rolled no store of its own.

## Related
- [[concept-surrender-offers]] — the `<surrender>` with no `chance` attribute
- [[concept-stores]] — why an event-granted store matters
- [[chain-mantis-war-camp]], [[chain-merchant-s-request]] — the other civilian-contract quests
- [[concept-quest-beacon-placement]]
- [[entity-rebels]], [[entity-pirates]]

## Open Questions
- [ ] The default `chance` on a `<surrender>` block that omits it — four ships are affected,
      and this is one of them.
- [ ] Whether `MERCENARY_WORK_LIST`'s two entries are truly 50/50, per
      [[concept-event-list-weighting]].
- [ ] Why the chain is `ae` on its triggers while the destination event is `both`.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
