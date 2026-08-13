---
id: event-no-fuel-drifting-debris
type: event
event_name: FUEL_OFF_ROCK_WRECK
sectors: []
beacon_type: any
hostile: false
blue_options: [[[item-lifeform-scanner]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [out-of-fuel, rock, crew-risk, scrap-loss-risk, map-reveal, blue-option, derived-odds]
---

# No fuel: drifting debris — `FUEL_OFF_ROCK_WRECK`

## Summary
A gutted Rock frigate drifts past while you are stranded. Boarding it is the only
out-of-fuel event that can **cost you a crew member**, and the Clone Bay explicitly does
not save them. The Advanced Edition **Lifeform Scanner** blue option removes that risk
entirely for a guaranteed `MED` fuel payout.

## Trigger & Where It Appears
- **Not a sector event.** Member of the `NO_FUEL` list — the distress-beacon-**off**
  out-of-fuel pool ([[source-events-fuel]]). Fandom marks it `outoffuel=distressoff`
  ([[source-fandom-no-fuel-drifting-debris]]).
- The developer comment above it says these Rock events "should eventually be tied to the
  rock sector"; they never were — it fires anywhere ([[source-events-fuel]]).
- Prerequisites: 0 fuel, distress beacon off, and you choose to wait.

**Derived odds.** 1/11 (~9.1%) per wait in AE; 1/10 (10%) in vanilla. *Assumes uniform
selection across list entries.*

## Text
> As you await either salvation or death, your attention is drawn to a sea of debris
> drifting past the starboard view port. The chunks gliding by grow bigger in size until
> the stern of a Rock frigate, gutted in some distant war, comes into view.

(`event_FUEL_OFF_ROCK_WRECK_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Send an away team. | — | "Perhaps there's some viable fuel left on board; a small away team boards the vessel." → *Report!* → loads `FUEL_OFF_ROCK_WRECK_LIST` (4 entries) — see below. | — |
| 2 | Let it drift by. | — | "The Rock don't take kindly to aliens picking through their belongings…" Nothing happens. | 100% |
| 3 | **(Life Scanner)** Run additional scans. | `req="LIFE_SCANNER"` — **AE only**, the tag carries `<!--DLC-->` | "The ship appears to be entirely lifeless. Your crew is able to find some usable fuel cells after a brief search." → `autoReward level="MED"` **fuel_only**. | 100% |

### Choice 1 — `FUEL_OFF_ROCK_WRECK_LIST` (4 entries, 1/4 each)

| Outcome | Result | Odds |
|---|---|---|
| "…a stash of ammunition and scrap - but all the fuel on board is long gone." | `autoReward level="MED"` **missiles** (missiles + scrap, no fuel). | 1/4 |
| "…the main computer… still partially operational… Your map has been updated." | `<reveal_map/>` — sector map revealed — plus `autoReward level="MED"` **fuel_only**. | 1/4 |
| "…the ship's emergency fuel cell just happened to drift by!" | `autoReward level="MED"` **fuel_only**. | 1/4 |
| "…a Rockman can be heard - he's the lone survivor… He demands you pay a scrap ransom in return for your crew-member's life!" | *Pay* → **−25–40 scrap**, crew returned. *Refuse* → **`removeCrew` with `<clone>false</clone>` — you lose a crew member permanently; a Clone Bay does not revive them** ("Before preparing to jump you check the Clone Bay but there is no sign of activity"). | 1/4 |

The 1/4 figures are derived from the four `<event>` entries and **assume uniform selection
across list entries** ([[source-events-fuel]]).

## Blue Options
- **[[item-lifeform-scanner]]** (`req="LIFE_SCANNER"`) — **Advanced Edition only.** The
  `<choice>` tag is annotated `<!--DLC-->` in the base file, so the vanilla version of this
  event has only two choices ([[source-events-fuel]], rule: DLC-wrapped tags are AE
  content). It replaces the 1/4 crew-hostage risk with a guaranteed `MED` fuel payout.

## Rewards & Risks
- 3 of 4 away-team outcomes pay `MED` rewards; one of those also reveals the sector map.
- The fourth costs either 25–40 scrap or a crew member — permanently, Clone Bay included.
- No combat anywhere in this event.

## Strategy Notes
- *Opinion:* with the Lifeform Scanner, always take choice 3 — same `MED` fuel as the good
  away-team outcomes, zero downside.
- Without it, boarding is a 75/25 gamble. When stranded with no fuel you generally need the
  fuel badly enough to take it; if you are short-crewed or the scrap ransom would bankrupt
  you, letting it drift by is a defensible pass.
- Losing a crew member here is unusually punishing because it is Clone-Bay-proof, which is
  not true of most crew-loss events.

## Related
- [[event-no-fuel-engi-ship-repair]] — the other faction-flavoured distress-off draw
- [[event-no-fuel-friendly-refugee]]
- [[entity-rock-men]]
- [[concept-out-of-fuel]]
- [[event-fuel-off-rock-curious]] (`FUEL_OFF_ROCK_CURIOUS`) — the unlisted sibling directly below it in `events_fuel.xml`

## Open Questions
- [ ] Exact scrap/fuel values behind `autoReward level="MED"` for `fuel_only` vs `missiles`.
- [ ] Which crew member is chosen by `removeCrew` (random, or a fixed slot).

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-fandom-no-fuel-drifting-debris]] (per raw/wiki/no-fuel-drifting-debris.md)
