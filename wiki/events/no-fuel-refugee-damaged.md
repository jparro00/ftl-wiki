---
id: event-no-fuel-refugee-damaged
type: event
event_name: NO_FUEL_REFUGEE_DAMAGED
sectors: []
beacon_type: distress
hostile: false
blue_options: [engi crew]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [out-of-fuel, distress-beacon, refugee, trading, blue-option, advanced-edition, derived-odds]
---

# No fuel: damaged refugee — `NO_FUEL_REFUGEE_DAMAGED`

## Summary
A refugee ship with a wrecked hull answers your distress call and wants scrap for its
spare fuel. The stated deal is poor (3 fuel for 10 scrap); an **Engi crew member** doubles
the fuel for the same price — and so, half the time, does simply refusing. There is also an
option to shoot them, which pays more than any trade and costs nothing but the choice.

## Trigger & Where It Appears
- **Not a sector event, and not directly in a pool.** It is a member of the
  `NO_FUEL_REFUGEE` event list, which is itself one entry in `NO_FUEL_DISTRESS` — the
  distress-beacon-**on** out-of-fuel pool ([[source-events-fuel]]).
- Prerequisites: 0 fuel, distress beacon on, and you choose to wait.

**Version: `ae`.** The `NO_FUEL_REFUGEE` entry in `NO_FUEL_DISTRESS` is annotated
`<!-- DLC - below -->` and the whole refugee block sits under the file's
`DLC!!! / Events added with the DLC` header ([[source-events-fuel]]). Not present in
vanilla.

**Derived odds.** `NO_FUEL_REFUGEE` is 1 of 12 entries in the AE `NO_FUEL_DISTRESS` list,
and this event is 1 of its 3 members → **1/36 (~2.8%)** per wait. *Assumes uniform selection
across list entries.* The list's own developer comment confirms the intent: *"I made this
one compile all 3 so they're less likely than the normal events"*
([[source-events-fuel]]).

The other two members of `NO_FUEL_REFUGEE` are [[event-no-fuel-refugee-pirate]] and an
inline event (no id of its own) that simply grants `autoReward level="LOW"` fuel_only.

## Text
> A refugee ship fleeing the Rebel advance enters the system, having picked up your distress
> beacon. While it doesn't have much fuel to spare, its hull looks damaged - it is in bad
> need of scrap and is willing to trade fuel for it.

(`event_NO_FUEL_REFUGEE_DAMAGED_text`, per [[source-text-events-xml]])

No `<ship>` tag until you choose to attack.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Trade some scrap for fuel. | — | "The refugees thank you for the parts…" **−10 scrap, +3 fuel.** | 100% |
| 2 | **(Engi Crew)** Negotiate a better trade. | `req="engi"` | "…they admit that their need for repairs is greater than their fuel surplus and offer a better trade." → *Accept it* → **−10 scrap, +6 fuel**. *Refuse it* → nothing. | 100% |
| 3 | Refuse their offer. | — | Loads `NO_FUEL_REFUGEE_REFUSE` (2 entries) — see below. | — |
| 4 | The helpless refugees make easy targets. Attack them. | — | "Panicked, the refugees immediately surrender as your weapons power up." → `autoReward level="MED"` **fuel** (fuel + scrap). **No combat actually occurs** — there is no `<ship>` tag, only the reward. | 100% |

### Choice 3 — `NO_FUEL_REFUGEE_REFUSE` (2 entries, 1/2 each)

| Outcome | Result | Odds |
|---|---|---|
| "The refugee ship cuts communications and jumps from the system without another word…" | Nothing happens. | 1/2 |
| "The refugees become desperate at your refusal… Almost begging, they offer a better trade than before." | *Accept it* → **−10 scrap, +6 fuel** (identical to the Engi blue option). *Refuse their offer again* → the cold-shoulder text again, nothing happens. | 1/2 |

The 1/2 split is derived from the two `<event>` entries in the `<eventList>` and **assumes
uniform selection across list entries** ([[source-events-fuel]]).

## Blue Options
- **Engi crew member** (`req="engi"`) — turns the 3-fuel-for-10-scrap deal into
  6-fuel-for-10-scrap, guaranteed, with an option to walk away for free after seeing it.
  Exactly the same terms that refusing reaches at 1/2 odds.

## Rewards & Risks
- Best guaranteed outcome without a blue option: **attack** — `autoReward level="MED"` fuel
  *and* scrap, at no cost, with no fight.
- Best trade: 6 fuel for 10 scrap (Engi, or 1/2 of refusing).
- Worst outcome: nothing, from the 1/2 cold-shoulder branch or from declining a better
  offer.
- **No combat, no boarding, no theft anywhere in this event** — the attack option resolves
  as an instant surrender.

## Strategy Notes
- *Opinion:* mechanically, choice 4 dominates: `MED` fuel + scrap beats 6 fuel for 10 scrap,
  it is guaranteed, and nothing shoots back. The cost is entirely narrative.
- *Opinion:* if you would rather not shoot refugees, the Engi option is the clean line and
  refusing is the gamble — half the time you get the Engi deal anyway, half the time you get
  nothing.
- Note choice 1 is the *worst* option on the board and the only one presented as the
  default.

## Related
- [[event-no-fuel-refugee-pirate]] — the sibling refugee event in the same list
- [[event-no-fuel-friendly-refugee]] — the distress-off refugee, free and unconditional
- [[entity-engi]]
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Exact fuel/scrap values behind `autoReward level="MED"` fuel.
- [ ] Whether the Fandom page's coverage under the list title *"No fuel: refugee trading"*
      implies any behaviour not visible in the XML.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-fandom-no-fuel-refugee-trading]] (per raw/wiki/no-fuel-refugee-trading.md — the
  Fandom page covers the whole `NO_FUEL_REFUGEE` list, including this event)
