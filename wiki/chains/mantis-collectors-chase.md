---
id: chain-mantis-collectors-chase
type: chain
trigger_event: [[[event-mantis-ship-collectors]]]
steps: [[[event-mantis-ship-collectors]], [[event-donor-mantis-chase2]]]
sectors: [[[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]]
reward: "a high weapon for sparing them; a random weapon + med scrap for killing them; high scrap if they escape"
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
tags: [quest, grudge, mantis, surrender, escape-timer, mercy-reward]
---

# The Mantis collector's chase

## Summary
A running grudge. A Mantis ship escapes you once; the quest marker lets you catch up with it —
and find the crew **transferring into a bigger ship**. *"Not YOU again! Do you know how much
these repairs are going to cost me? Time to take out the big guns."*

The second fight is against a `MANTIS_BOMBER`, and every one of its four resolutions pays
something. The best is the one that requires letting them go: `HIGH weapon` for accepting the
surrender, against `MED standard` plus a random weapon for finishing them off.

## How It Starts
- Trigger: [[event-mantis-ship-collectors]] (`DONOR_MANTIS`) — the Mantis collector encounter.
  The marker is planted on the branch where the ship gets away
  (`<quest event="DONOR_MANTIS_CHASE2"/>`, [[source-events-xml]]).
- The chase is therefore a **consolation prize for a failed fight** — you only get it because
  they escaped.

## Steps

1. **[[event-mantis-ship-collectors]]** — the first encounter; the Mantis escapes and you note
   where they went.
2. **[[event-donor-mantis-chase2]]** (`DONOR_MANTIS_CHASE2`) — the marked beacon. The ship is
   **already hostile on arrival**; the single "Continue…" choice is pure narration, not a
   decision. The enemy is `auto_blueprint="MANTIS_BOMBER"` — a heavier hull than the fighter
   you met the first time ([[source-events-ships]]).

3. **Four resolutions, all of which pay** ([[source-events-ships]]):

   | Resolution | Declaration | Payload |
   |---|---|---|
   | **Surrender** | `<surrender min="2" max="2">` — **no `chance` attribute** | see below |
   | **Escape / gotaway** | `<escape timer="12" min="6" max="6">` — a short 12-second timer | `autoReward HIGH standard` — *"At least you're able to scrap their abandoned fighter."* |
   | **Destroyed** | — | `<weapon name="RANDOM"/>` + `autoReward MED standard` |
   | **Dead crew** | — | (see the event page) |

4. **The surrender is a second choice**, at 20% hull:

   | Choice | Outcome |
   |---|---|
   | **Let them live** | *"But do you have any idea how much repairing TWO ships will set us back?…"* → **`autoReward HIGH weapon`**, ship goes non-hostile |
   | Finish them off | *"No! Hurry up, get us out of here! They're crazy!"* — the fight resumes |

## Requirements
- None. No gates anywhere.
- Fuel for the extra jump.

## Reward
Unusually generous for a quest with no requirements:

- **Sparing them: `HIGH weapon`** — the best outcome, and the only one that needs restraint.
- **Killing them: a random weapon plus `MED standard`** — still good, and the only branch that
  guarantees *a* weapon regardless of the surrender roll.
- **Letting them escape: `HIGH standard`** — even total failure pays a high-tier reward,
  because you salvage the fighter they abandoned.

## Failure Modes
- There is effectively **no failure branch** other than losing the fight yourself. Every
  resolution pays.
- The `<surrender>` block carries **no `chance` attribute** — one of the four such blocks in
  the game, whose default is undocumented. See [[concept-surrender-offers]]. Whether the offer
  is guaranteed is not derivable from the file.
- The 12-second escape timer is short: a slow kill can convert `HIGH weapon` into
  `HIGH standard`.
- The standard quest-marker losses — see [[concept-quest-beacon-placement]].

## Strategy Notes
- *Opinion:* bring them to 20% hull and **accept the surrender**. `HIGH weapon` beats a random
  weapon plus `MED standard` in expectation, and the fight ends immediately.
- Do not over-commit to a fast kill: with a 12-second escape timer and a 20% surrender
  threshold, burst damage risks skipping straight past the offer.
- Being beaten at the first encounter is what unlocks this — a rare case where losing an
  engagement leads somewhere better.

## Related
- [[concept-surrender-offers]] — the `<surrender>` with no `chance` attribute
- [[entity-mantis]]
- [[concept-quest-beacon-placement]]
- [[chain-mantis-cruiser-unlock]] — the other Mantis-space quest line

## Open Questions
- [ ] The default `chance` on a `<surrender>` block that omits it — this is one of the four
      affected ships.
- [ ] Whether `MANTIS_BOMBER` here is scaled to sector depth like an ordinary draw.
- [ ] Whether the marker can be planted more than once if the first encounter recurs.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
