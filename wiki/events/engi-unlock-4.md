---
id: event-engi-unlock-4
type: event
event_name: ENGI_UNLOCK_4
sectors: []
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-stealth-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [orphan, chain, ship-unlock, augment-reward, hull-repair, payoff]
---

# Engi unlock — Project X-ME56 — `ENGI_UNLOCK_4`

## Summary
The payoff of [[chain-stealth-cruiser-unlock]]. The Engi explain that the stolen technology
is an advanced stealth cruiser, ask for the Federation fleet's coordinates, and pay you for
them: **the Stealth Cruiser unlock**, the Titanium System Casing augmentation, `HIGH` scrap
with resources, and 20 hull repairs. No fight, no risk, no way to lose it once you are here.

## Trigger & Where It Appears
- **Not in any sector event list.** It is the continuation of [[event-engi-unlock-3]] —
  loaded directly by that fight's `<destroyed load="ENGI_UNLOCK_4"/>`, or via a continue
  choice on its `deadCrew` block ([[source-events-xml]], per `raw/gamedata/events_ships.xml`).
- Beacon: **quest** — same beacon as step 3, immediately after the fight.

## Text
> The Engi emerge victorious from their battles with only minor losses. They message you,
> "Project X-ME56 commissioned by Federation military research division. Advanced stealth
> cruiser. Project finished during rebellion. Unable to reconnect with Federation military
> command."

(`event_ENGI_UNLOCK_4_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Ask about the Mantis ships. | — | *"Likely ploy by Rebels to avoid breaking non-aggression pact with Engi. 97.56 percent likely. Your mission to assist last Federation fleet, correct? Coordinates?"* | 100% |
| 1a | Transmit coordinates of Federation command. | — | *"Satisfactory. Delivery of tech will assist in Federation cause…"* → `<damage amount="-20"/>` (**20 hull repairs**), `<autoReward level="HIGH">standard</autoReward>`, `<augment name="SYSTEM_CASING"/>` (**Titanium System Casing**), and `<unlockShip id="1"/>` — the **Stealth Cruiser**. | 100% |

There is no branch that declines. ([[source-events-xml]], per `raw/gamedata/events_engi.xml`)

## Blue Options
None.

## Rewards & Risks
- **[[ship-stealth-cruiser]]** unlocked (`<unlockShip id="1"/>`). Fandom identifies this as
  the Stealth Cruiser Layout A, and notes the ship can alternatively be unlocked by winning
  the game with the Rock Cruiser ([[source-fandom-engi-fleet-discussion]]).
- **[[item-titanium-system-casing]]** (`SYSTEM_CASING`).
- `HIGH` scrap with resources.
- 20 hull repairs.
- No risk — the event contains no ship, no crew effect, and no losing branch.

> ⚠️ **CONTRADICTION:** the reward prose.
> - Game files: *"Their crews deliver **an advanced augmentation** for installation but
>   you're more pleased to hear that the Federation will have an improved arsenal."*
>   (`event_ENGI_UNLOCK_4_c1_c1_text`, per [[source-text-events-xml]])
> - Fandom: *"Their crews deliver **a weapon** for installation…"*
>   ([[source-fandom-engi-fleet-discussion]])
>
> The mechanical payload is not in dispute — both sources agree it is the Titanium System
> Casing augmentation, high scrap and 20 repairs — so "a weapon" reads as stale text that
> was corrected to match the actual reward. Trusting the game files (`high` vs `medium`).
> Plausibly a vanilla→AE text fix, but not confirmed as one.

> ⚠️ **BUG (Fandom-only):** Fandom reports that if the `HIGH` scrap-with-resources roll
> happens to award an augmentation, it **overwrites** the guaranteed Titanium System Casing
> ([[source-fandom-engi-fleet-discussion]]). The game files order the lines as
> `autoReward` then `augment`, which is consistent with the claim but does not establish it.
> Recorded at `medium` reliability.

## Strategy Notes
- Nothing to decide — take the single choice. The value of this page is knowing what you are
  playing for three steps earlier: an unlock, an augment, `HIGH` scrap and 20 repairs is a
  large return for a chain whose only real risk is over-killing the scout at
  [[event-engi-unlock-2real]]. *(Opinion.)*
- If you are carrying a full augment slot set, be aware of the overwrite bug above before
  arriving. *(Opinion, contingent on an unverified Fandom claim.)*

## Related
- [[chain-stealth-cruiser-unlock]] — this is step 4 of 4
- [[event-engi-unlock-3]] — the fight immediately before this
- [[event-engi-fleet-discussion]] — where the chain starts
- [[ship-stealth-cruiser]], [[item-titanium-system-casing]]
- [[entity-engi]]

## Open Questions
- [ ] Is the augment-overwrite bug reproducible?
- [ ] Is "a weapon" vs "an advanced augmentation" a vanilla/AE change or a wiki error?
- [ ] Does `<unlockShip id="1"/>` unlock Layout A only, as Fandom states?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`, `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-engi-fleet-discussion]] (per `raw/wiki/engi-fleet-discussion.md`)
