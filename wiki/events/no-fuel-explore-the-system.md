---
id: event-no-fuel-explore-the-system
type: event
event_name: FUEL_EXPLORE
sectors: []
beacon_type: any
hostile: unknown
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [out-of-fuel, trading, asteroid-field, auto-ship, hull-damage-risk, derived-odds]
---

# No fuel: explore the system — `FUEL_EXPLORE`

## Summary
Stranded with no fuel, you can burn impulse power to poke around the system. It is the
only out-of-fuel event that offers a **guaranteed opt-out** ("Stay near the beacon" does
nothing at all), and the only one whose exploration branch can sell you fuel in
1 / 2 / 5-unit increments — which matters when you are down to your last few scrap.

## Trigger & Where It Appears
- **Not a sector event.** Drawn from the out-of-fuel wait pools. `FUEL_EXPLORE` is a member
  of **both** `NO_FUEL` (distress off) and `NO_FUEL_DISTRESS` (distress on)
  ([[source-events-fuel]]); Fandom marks it `outoffuel=distressboth`
  ([[source-fandom-no-fuel-explore-the-system]]).
- Prerequisites: 0 fuel, and you choose to wait at the beacon.

**Derived odds.** 1/11 (~9.1%) per wait with the beacon off, 1/12 (~8.3%) with it on
(AE list lengths). Vanilla, without the `<!-- DLC -->` refugee entries: 1/10 and 1/11.
*Assumes uniform selection across list entries* ([[source-events-fuel]]).

## Text
> Although your lack of fuel cells prevents your ship from jumping, you can still use your
> impulse engines. Will you spend some time exploring the nearby system?

(`event_FUEL_EXPLORE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Explore the nearby area. | — | Loads `FUEL_EXPLORE_LIST` (4 entries) — see below. | — |
| 2 | Stay near the beacon. | — | Empty `<event/>` — nothing happens. | 100% |

### Choice 1 — `FUEL_EXPLORE_LIST` (4 entries, 1/4 each)

| Outcome | Result | Odds |
|---|---|---|
| **Asteroid field.** "You happen across a small asteroid field near the beacon." | *Approach the asteroid field to scan it* → loads `ASTEROID_EXPLORE_RESULTS` (see below). *Avoid the risk* → nothing. | 1/4 |
| **Outpost.** "You find a small outpost for local travelers… their stock of fuel cells is small and their price high" | Four fixed trades: 20 scrap → 5 fuel; 10 scrap → 2 fuel; 5 scrap → 1 fuel; or don't trade. | 1/4 |
| "No ships respond to your hails and you find nothing of interest." | Nothing happens. | 1/4 |
| "You wander within scanning range of a small Rebel automated scout!" | Hostile `REBEL_AUTO_FUEL` — an auto-ship on an 80s escape timer. Destroyed → `autoReward level="MED"` **fuel**. No `deadCrew` block (it has no crew). | 1/4 |

### `ASTEROID_EXPLORE_RESULTS` (defined in `events.xml`, 6 entries, 1/6 each)

| Outcome | Result | Odds |
|---|---|---|
| A brief exploration yields nothing of interest. | Nothing. | 1/6 |
| Useful asteroid compositions. | `autoReward level="HIGH"` **fuel_only**. | 1/6 |
| Wrecked ship with functional missiles. | `autoReward level="MED"` **missiles**. | 1/6 |
| Abandoned mining site. | `autoReward level="MED"` **droneparts**. | 1/6 |
| The field bites back. | 3 hull damage, **+1 damage to a random system (AE only — the tag carries `<!--DLC-->`)**, and 1 damage with fire to a random room. | 1/6 |
| A pirate ship hiding behind an asteroid attacks. | Hostile `PIRATE` in an asteroid-field environment (default rewards). | 1/6 |

All 1/N figures are derived from `<eventList>` entry counts and **assume uniform selection
across list entries** ([[source-events-fuel]], [[source-events-xml]]).

> ⚠️ **CONTRADICTION:** hull damage on the bad asteroid outcome.
> - Game files: `<damage amount="3"/>` plus a `<!--DLC-->`-gated `<damage amount="1"
>   system="random"/>` and `<damage amount="1" system="room" effect="fire"/>`
>   ([[source-events-xml]], per raw/gamedata/events.xml).
> - Fandom: *"Your ship takes **5 hull** damage, 1 damage to a random system, 1 damage with
>   fire to a random room"* ([[source-fandom-no-fuel-explore-the-system]]).
>
> Trusting the game files (`high` vs `medium`) for the base 3; the discrepancy is most
> likely Fandom summing the three `<damage>` tags, since each system/room hit also costs
> hull. Not resolved here.

## Blue Options
None on this event. (The equivalent asteroid scenario in the *Large asteroid field* event
additionally offers a Scrap Recovery Arm option; this one does not —
[[source-fandom-no-fuel-explore-the-system]].)

## Rewards & Risks
- Best case: `HIGH` fuel_only from the asteroid scan, or an outright fuel purchase.
- The 5-scrap-for-1-fuel trade is the cheapest guaranteed unstick in the whole out-of-fuel
  pool — one fuel is all you need to jump.
- Risks: 1/4 of the explore branch is an auto-ship fight; inside the asteroid branch,
  1/6 is hull+system+fire damage and 1/6 is a pirate fight *in an asteroid field*.
- "Stay near the beacon" is a genuine zero-risk out.

## Strategy Notes
- *Opinion:* if you have scrap, explore — the outpost branch alone (1/4) can end the
  crisis for 5 scrap, and two more of the four branches are harmless or profitable.
- If you are already hull-critical, the asteroid sub-branch is the one to decline
  ("Avoid the risk" is free), while still taking the explore choice itself.

## Related
- [[event-no-fuel-prepare-to-dock]] — the other event in both out-of-fuel pools
- [[event-no-fuel-wait-fail-distress-off]] / [[event-no-fuel-wait-fail-distress-on]]
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Exact scrap/fuel values behind `autoReward` `MED` / `HIGH` fuel tiers.
- [ ] Whether the 5-hull figure on Fandom is a real vanilla value or a summed estimate.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml — `ASTEROID_EXPLORE_RESULTS`)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-fandom-no-fuel-explore-the-system]] (per raw/wiki/no-fuel-explore-the-system.md)
