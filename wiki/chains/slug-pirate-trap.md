---
id: chain-slug-pirate-trap
type: chain
trigger_event: [[[event-slug-comm-tapping]]]
steps: [[[event-slug-comm-tapping]], [[event-quest-slug-pirate-trap2]]]
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
reward: "high scrap for trusting the Slugs; med/high standard for finishing the pirate; low/med for going it alone"
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
tags: [quest, slug, nebula, greed, surrender-branch, double-cross]
---

# The Slug pirate raid

## Summary
You eavesdrop on two Slug ships planning to rob a pirate, follow them to the scene, and are
invited to join a heist already in progress. The chain is built entirely around one question —
**do you trust a Slug?** — and the answer, unusually for Slug space, is *yes*.

Trusting them pays `HIGH scrap_only`, the best outcome available. Cutting them out pays the
worst. The event is named `PIRATE_TRAP` in the files, which reads as a warning about the Slugs
and turns out to describe the pirate instead.

## How It Starts
- Trigger: [[event-slug-comm-tapping]] (`QUEST_SLUG_PIRATE_TRAP`) ([[source-events-slug]]).
  *"You arrive to the sight of two Slug ships in communication range. They don't see you."*
- **Tap their comm frequency** → *"you overhear their conversation and learn they're planning
  to raid an infamous and likely wealthy pirate ship in the area. The pair jump off and you
  note down their target co-ordinates."* → `<quest event="QUEST_SLUG_PIRATE_TRAP2"/>`
- **Ignore them** → nothing.

## Steps

1. **[[event-slug-comm-tapping]]** — tap the comms, take the coordinates.
2. **[[event-quest-slug-pirate-trap2]]** — the raid, in a nebula
   (`<environment type="nebula"/>`, so sensors are down — see [[concept-nebula-mechanics]]).
   One Slug ship is already fighting the pirate; the other is heading for the cache. A forced
   continue: the first Slug ship **bursts into flames**, and the survivors hail you —
   *"We sssugest you distract the pirate vesssel while we retrieve the valuables. Fifty fifty
   sssplit."* Two choices ([[source-events-slug]]):

   | Choice | Ship you fight |
   |---|---|
   | **Engage the pirate** — take the deal | `QUEST_SLUG_PIRATE_TRAP1` |
   | **Head for the cache** — cut them out | `QUEST_SLUG_PIRATE_TRAP2`; the Slug captain hails *"Foolish alienss, no eye for profit"* and jumps away |

3. **The two hulls pay very differently** ([[source-events-ships]]). Both are
   `auto_blueprint="SHIPS_PIRATE"`; only the deal branch has a surrender:

   | | `destroyed` | `deadCrew` | surrender |
   |---|---|---|---|
   | **Took the deal** (`TRAP1`) | `MED standard` | `HIGH standard` | **yes** — see below |
   | **Cut them out** (`TRAP2`) | `LOW standard` | `MED standard` | none |

4. **The surrender branch is the real payoff, and it is a second choice.**
   `<surrender chance="0" min="3" max="4">` — a **guaranteed** offer at 30–40% hull, since
   `chance` is the probability the ship keeps fighting ([[concept-surrender-offers]]). It
   fires as *"you notice the Slug ship has secured the loot and is preparing to jump away!"*

   | Choice | Outcome |
   |---|---|
   | Continue fighting the pirate | *"you wonder whether what the pirate is carrying will be as valuable as what the Slugs snuck off with"* — resolve as `destroyed`/`deadCrew` above |
   | **Let the pirate escape and go after the Slugman ship** | *"Ah, of courssse, we would never leave without providing the agreed upon ssspoils."* → **`autoReward HIGH scrap_only`**, pirate goes non-hostile |

## Requirements
- None. No gates anywhere.
- Fuel for the extra jump.

## Reward
`HIGH scrap_only` for chasing the Slugs at the surrender prompt is the best result. Boarding
the pirate for `HIGH standard` is comparable and gives items rather than pure scrap. Cutting
the Slugs out caps at `MED standard` and loses the cache regardless — *"it's lost in the
clouds"* in both of that hull's branches.

## Failure Modes
- **Cutting the Slugs out is strictly worse.** You never reach the cache, you lose the
  surrender branch entirely, and both outcomes drop a full tier.
- **Killing the pirate too fast on the deal branch** skips the surrender prompt and its
  `HIGH scrap_only`.
- Fighting in a nebula means no sensors for the duration.
- The standard quest-marker losses — see [[concept-quest-beacon-placement]].

## Strategy Notes
- *Opinion:* take the deal, bring the pirate to 30–40% hull, then **let it escape and chase
  the Slugs**. This is one of the few events where the game rewards keeping a bargain with a
  Slug, and it rewards it well.
- If you board rather than shoot, `HIGH standard` on `deadCrew` is a fine alternative — items
  plus scrap instead of scrap alone.
- Note the Slug ship that catches fire is not something you did; it happens in the narration
  before you choose.

## Related
- [[concept-surrender-offers]] — why `chance="0"` here is a guaranteed offer
- [[concept-nebula-mechanics]] — the beacon's environment
- [[entity-slugs]] — and the rare case of them dealing straight
- [[entity-pirates]]
- [[chain-secret-word-abadoth]] — the other Slug-nebula quest line

## Open Questions
- [ ] What was in the cache — no branch ever reveals it.
- [ ] Whether the burning Slug ship is recoverable or purely narrative.
- [ ] Whether `QUEST_SLUG_PIRATE_TRAP1`'s "continue fighting" branch still lets the Slugs pay
      out later; the file shows no second offer.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
