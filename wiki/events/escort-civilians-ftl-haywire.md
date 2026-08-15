---
id: event-escort-civilians-ftl-haywire
type: event
event_name: ESCORT_BEACON
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-uncharted-nebula]]]
beacon_type: distress
hostile: false
blue_options: [[[item-ftl-jumper]]]
chain: [[[chain-escort-civilians]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [distress, unique, quest-marker, blue-option, augment, escort, scrap-reward]
---

# Escort civilians FTL haywire — `ESCORT_BEACON`

## Summary
A distress beacon where a civilian ship asks you to lead it to a repair depot. Accepting
pays a token amount of scrap now and plants a quest marker that pays properly on arrival;
declining costs nothing. With the **Advanced FTL Navigation** augment you skip the escort
entirely and take the high reward on the spot — the augment converts a two-jump commitment
into a one-screen payout.

## Trigger & Where It Appears
- Sectors: [[sector-civilian-sector]], [[sector-federation-space]],
  [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]],
  [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]],
  [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]],
  [[sector-rock-homeworlds]], [[sector-uncharted-nebula]]
- Beacon: **distress** — the event carries `<distressBeacon/>` and is pooled in
  `DISTRESS_BEACON` plus its Mantis, Pirate, Rebel and Rock variants
  ([[source-events-xml]], [[source-newevents]]).
- A non-hostile `CIVILIAN_SHIP` is present at the beacon, so Long-Range Scanners show a
  ship ([[source-events-ships]], [[source-fandom-escort-civilians-ftl-haywire]]).
- `unique="true"` — at most once per run.

## Text
> Once you arrive at the location of the distress call a civilian ship hails you, "Thanks
> for responding to our beacon. Our FTL navigation has gone haywire and we can't plot a
> course to the nearest depot to get it fixed. Could you lead us there?"

(`event_ESCORT_BEACON_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Lead them to their destination. | — | *"Take this bit of scrap as a down-payment. We'll use your jump signatures to follow you. You're really helping us out here."* → `autoReward level="LOW"` type `scrap_only`, **plus** `<quest event="QUEST_ESCORT_ARRIVE"/>` — a quest marker is added to your map. | 100% |
| 2 | Decline. | — | *"Alright... If you're not going that way I guess it can't be helped. We'll just wait for the next ship to come."* → nothing. | 100% |
| 3 | **(Advanced FTL Navigation)** Have your navigation software calculate and upload route instructions to their ship. | `req="FTL_JUMPER"` | *"We're receiving your transmission... Wow, I didn't know that chain-jumping was possible with this class of ship. We'll get back in a single jump! Thank you so much, please accept this."* → `autoReward level="HIGH"` type `standard`. **High scrap with resources, immediately, no escort.** | 100% |

### The destination — `QUEST_ESCORT_ARRIVE`

Choice 1 marks a beacon; arriving there fires the `QUEST_ESCORT_ARRIVE` event list. That
list is **shared with `QUEST_ESCORT`** ([[event-escort-civilians]]) — the two escort
events lead to the same four destinations ([[source-events-xml]]). Fandom notes the same
similarity ([[source-fandom-escort-civilians-ftl-haywire]]).

Four members in Advanced Edition, three in vanilla — the fourth is flagged `<!--DLC!-->`.
**Assuming uniform selection across list entries: 1/4 each in AE, 1/3 each in vanilla.**

| Odds (AE / vanilla) | Outcome |
|---|---|
| 1/4 · 1/3 | *"You escort the ship to the requested beacon. Much to your dismay you are ambushed by a Rebel ship. You walked right into their trap!"* → `<ship load="REBEL" hostile="true"/>` — a normal Rebel fight with default rewards. |
| 1/4 · 1/3 | *"Shortly after you arrive, the ship you were escorting jumps nearby. They thank you for your help and offer you a reward."* → `autoReward level="HIGH"` type `standard`. |
| 1/4 · 1/3 | *"…Let my friends patch up some of your hull and show you their wares."* → `<damage amount="-5"/>` (**+5 hull repaired**) and `<store/>` — **a store opens at the beacon.** |
| 1/4 · — | **AE only.** *"Thank you. Perhaps as payment our engineer can try to optimize your ship's reactor output?"* → `<upgrade amount="1" system="reactor"/>`. |

> Version note: the fourth member carries an explicit `<!--DLC!-->` marker inside
> `events.xml`, so the vanilla destination pool is three entries, not four
> ([[source-events-xml]]). This shifts the ambush odds from 1/3 in vanilla to 1/4 in
> Advanced Edition.

The `REBEL` ship at the ambush: `<surrender chance="0.5" min="2" max="3">` and
`<escape chance="0.5" min="3" max="4">`, both loading the shared `PIRATE_SURRENDER` /
`PIRATE_ESCAPE` blocks, with `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` rewards
([[source-events-ships]]). Per [[concept-surrender-offers]], `chance="0.5"` means a **50%
surrender chance** — `chance` is the probability the ship keeps fighting.

## Blue Options
- **[[item-ftl-jumper]] — "Advanced FTL Navigation"** (`req="FTL_JUMPER"`). It replaces a
  low `scrap_only` payout plus a two-jump escort commitment with an immediate
  `autoReward level="HIGH"` of type `standard` — the best single payout in the event, with
  no ambush risk and no beacon spent. The augment's display name is only recoverable from
  Fandom; the id `FTL_JUMPER` does not say it
  ([[source-fandom-escort-civilians-ftl-haywire]]).

## Rewards & Risks
- Choice 1: low scrap now; then one of high scrap / a store + 5 hull repair / a reactor
  upgrade (AE) / a Rebel ambush.
- Choice 3: high scrap with resources, immediately.
- Risk: only on the escort. The ambush is a standard Rebel ship with default rewards, so
  even the bad branch is not a loss unless the fight goes wrong — but it costs a jump and
  fleet advance to get there.

## Strategy Notes
- The blue option is the whole event if you have the augment. High-tier `standard` on the
  spot beats the expected value of the escort, and costs no beacons. *Opinion*, from the
  reward tiers.
- Without it, the escort is a reasonable take: three of four AE destinations are pure gain,
  and the store outcome is often the best of them if you are carrying scrap.
- The quest marker consumes a beacon you were probably visiting anyway, but it does drag
  the Rebel fleet forward one step.

## Related
- [[chain-escort-civilians]] — the full quest line this belongs to
- [[event-escort-civilians]] — `QUEST_ESCORT`, which shares the exact same
  `QUEST_ESCORT_ARRIVE` destination list
- [[item-ftl-jumper]] — the blue-option gate
- [[entity-rebels]] — the ambush ship
- [[concept-quest-beacon-placement]], [[concept-surrender-offers]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] The actual distribution across `QUEST_ESCORT_ARRIVE` — the 1/4 and 1/3 figures assume
      uniform selection across list entries.
- [ ] What "low `scrap_only`" and "high `standard`" pay in absolute scrap; no source states
      it.
- [ ] Whether the destination beacon can be one you have already visited.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-fandom-escort-civilians-ftl-haywire]] (per raw/wiki/escort-civilians-ftl-haywire.md)
