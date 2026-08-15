---
id: chain-secret-word-abadoth
type: chain
trigger_event: [[[event-battlefield-survivor]]]
steps: [[[event-battlefield-survivor]], [[event-secret-word-abadoth]]]
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
reward: "autoReward MED standard — for remembering one word"
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
tags: [quest, password, memory-puzzle, zoltan, slug, engi, fourth-wall]
---

# ABADOTH — the secret word

## Summary
The only puzzle in FTL that tests **the player**, not the ship. A dying crewman gives you a
word and some coordinates. Several jumps later a cloaked Zoltan ship decloaks and demands to
know why you are there, and the game presents you with a menu of near-identical options:

> Say ANODYNE. · Say ABADOTH. · Say ABATODH.

Nothing in the interface tells you which is right. If you were not paying attention at the
first beacon — or did not write it down — it is a one-in-three guess, and two of the three
answers start a fight with a Zoltan warship.

The word is **ABADOTH**.

## How It Starts
- Trigger: [[event-battlefield-survivor]] (`BATTLEFIELD_SURVIVOR`), itself reached from the
  battlefield-wreckage investigation in Slug nebula space ([[source-events-slug]]).
- The survivor you pull out of the wreckage dies, but not before giving you a word and a set
  of coordinates → `<quest event="SECRET_WORD_ABADOTH"/>`.
- The other choice lets him die without asking, and plants nothing.

## Steps

1. **[[event-battlefield-survivor]]** — attempt to save the dying crewman; take the
   coordinates. **This is where the word is spoken.**
2. **[[event-secret-word-abadoth]]** (`SECRET_WORD_ABADOTH`) — *"There doesn't seem to be
   anything here — no planets, no vessels, and no clue as to what he meant by sending you
   here."* Two ways to proceed ([[source-events-slug]]):

   | Choice | Requirement | Cost |
   |---|---|---|
   | **(Slug Crew) Ask your Slug crewmember to scan for life forms** | `req="slug"` | **free** |
   | Do a full system scan | — | `<modifyPursuit amount="1"/>` — **the Rebel fleet advances 1 jump** |

   Both lead to the same place. A Slug crew member's innate life-form sensing (see
   [[entity-slugs]]) is what saves you the fleet advance — see
   [[concept-rebel-fleet-advance]] for why a positive `modifyPursuit` is a cost, not a gain.

3. **`SECRET_WORD_ABADOTH_CONCLUSION`** — *"A Zoltan ship decloaks and demands your reason for
   being here!"* Five choices:

   | Choice | Requirement | Outcome |
   |---|---|---|
   | Explain about finding the dead crewman | — | *"must have been the wrong word to use"* → hostile `ZOLTAN_SHIP` |
   | **(Engi Crew) Say ABADOTH** | `req="engi"` | *"Your Engi crewman easily recalls the phrase… from its memory banks."* → `autoReward MED standard` |
   | Say ANODYNE | — | **fight** |
   | **Say ABADOTH** | — | *"the ship's captain solemnly thanks you… he offers several upgrades"* → `autoReward MED standard` |
   | Say ABATODH | — | **fight** |

## The Engi option is the joke

`req="engi"` produces the *same* reward as simply picking the right word — the Engi crewman
"easily recalls the phrase from its memory banks" because it is a machine and you are not. It
is a blue option that exists to compensate for the player's memory, and it is the only gate in
the game of that kind.

## Requirements
- **Nothing mechanical.** Remembering one word is the entire requirement.
- A **Slug** crew member avoids the fleet advance; an **Engi** crew member removes the guess.
- Fuel for the extra jump.

## Reward
`autoReward MED standard` — modest for a two-beacon quest, and deliberately so. What you are
buying is the absence of a fight with a Zoltan warship, which at `ZOLTAN_SHIP`'s shield
strength is worth more than the scrap.

## Failure Modes
- **Guessing wrong: a 2-in-3 chance of a fight** if you did not note the word, against a
  Zoltan hull with a super-shield ([[entity-zoltan]]).
- **Explaining honestly also starts the fight** — candour is modelled as the wrong answer.
- **No Slug crew** means paying a Rebel fleet advance just to find the ship.
- The standard quest-marker losses — see [[concept-quest-beacon-placement]].

## Strategy Notes
- *Opinion:* the word is **ABADOTH**. `ABATODH` is a transposition trap and `ANODYNE` is a
  plausible-sounding decoy; both lead to combat.
- With an Engi aboard, take the Engi option — it is identical in payout and immune to
  misreading the two similar spellings under time pressure.
- With a Slug aboard, use the Slug scan first: one jump of Rebel fleet advance is a real cost
  in a long run.

## Related
- [[event-battlefield-wreckage]], [[event-nebula-wreckage]] — the wreckage events that lead to
  the dying survivor
- [[entity-slugs]] — the life-form scan
- [[entity-engi]] — the memory banks
- [[entity-zoltan]] — who is waiting at the coordinates
- [[concept-rebel-fleet-advance]] — why the full system scan costs you
- [[chain-slug-pirate-trap]] — the other Slug-nebula quest line

## Open Questions
- [ ] Whether the Zoltan ship here differs from a generic `ZOLTAN_SHIP` draw.
- [ ] What the Zoltan are guarding at the coordinates — never stated in any branch.
- [ ] Whether the correct word changes between runs; the file hard-codes ABADOTH, so
      presumably not, but no source confirms the player-facing text is identical every time.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
