---
id: concept-augmentations
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
related_events: []
tags: [mechanics, items, augments, rarity, blue-options]
---

# Augmentations

## Definition & Context

Augments are passive equipment: no power, no crew, no room. They occupy augment slots and
change how the ship works for the whole run.

In the event data they appear as **`<augment name="X"/>` — 30 uses** ([[source-events-xml]] and
siblings), plus **8 `autoReward` records with the `augment` tier** (4 `HIGH`, 4 `LOW`). That is
38 opportunities across the whole event corpus, making an augment one of the rarer things an
event can hand you — rarer than a weapon (37 `<weapon>` uses plus 37 weapon-tier rewards).

## What events actually award

Of the 30 named awards ([[source-events-xml]]):

| Augment | Uses | Note |
|---|---|---|
| `RANDOM` | **10** | a sentinel, not a blueprint — the game rolls |
| `DRONE_SPEED` | 4 | Drone Reactor Booster |
| `CREW_STIMS` | 4 | [[item-mantis-pheromones]] — *the id does not match the name* |
| `DLC_AUGMENTS` | 2 | a blueprint **list**, AE-only |
| `NANO_MEDBAY` | 2 | [[item-nano-med-bot-dispersal]] |
| `STASIS_POD` | 2 | [[item-damaged-stasis-pod]] — the Crystal route key |
| `SLUG_GEL` | 2 | [[item-slug-repair-gel]] |
| `CRYSTAL_SHARDS`, `SYSTEM_CASING`, `ROCK_ARMOR`, `ENERGY_SHIELD` | 1 each | the starting augments of four player ships |

**A third of all named augment awards are `RANDOM`.** That is why so many event pages here say
"a random augment" — the specific item genuinely is not in the data.

## The id/name traps

Augment ids and display names diverge often enough to be a standing hazard when grepping:

- `CREW_STIMS` → **Mantis Pheromones**
- `NANO_MEDBAY` → **Nano Med-bot Dispersal**
- `ENERGY_SHIELD` → **Zoltan Shield**
- `SYSTEM_CASING` → **Titanium System Casing**

The card pipeline resolves these through `blueprints.xml` → `text_blueprints.xml`, which is why
cards show *"Rock Plating"* rather than `ROCK_ARMOR`. That resolution was a **bug fix**: awarded
items originally rendered as raw ids while *gates* on the same row resolved correctly. See the
2026-08-10 cold-start entry in `log.md`.

## Rarity, and the `0` that is not a rarity

Augments carry a `<rarity>` in `blueprints.xml`. Rarity runs **1 (commonest) → 5 (rarest)**, and
**`0` is a separate exclusion flag** meaning *never generated in stores or random rolls* — see
[[concept-blueprint-rarity]].

This matters directly: [[item-rock-plating]] and [[item-mantis-pheromones]] are both rarity 0.
They cannot be bought. The **only** way to get them is the event or chain that awards them —
which is why [[chain-rock-cruiser-unlock]] is the sole route to Rock Plating.

## Augments as gates

Augments do not only get awarded; they unlock choices. `req="ADV_SCANNERS"`,
`req="FTL_JUMPER"`, `req="STASIS_POD"` and others gate blue options — see
[[concept-blue-options]]. Two worked examples:

- [[item-long-ranged-scanners]] converts [[chain-hidden-federation-base]]'s empty destination
  into a weapon reward.
- [[item-ftl-jumper]] lets [[chain-escort-civilians]] skip its entire quest for a `HIGH
  standard` payout.

## Implications For Play

- **Rarity-0 augments are chain rewards, full stop.** Do not wait for a store.
- **An augment that gates events is worth more than its combat stats suggest** — the events it
  unlocks are the return, and this is the clearest case in the game of an item paying in
  content rather than in numbers.
- **`RANDOM` awards are a real gamble**, and one of the few places the wiki cannot tell you
  what you will get.

## Where It Applies
Every item page with `item_kind: augment`, and the events that award or require them.

## Related
- [[concept-blueprint-rarity]] — the 1–5 scale and the `0` exclusion flag
- [[concept-blue-options]] — augments as gates
- [[concept-autoreward-tiers]] — the `augment` reward tier
- [[item-rock-plating]], [[item-mantis-pheromones]], [[item-damaged-stasis-pod]],
  [[item-long-ranged-scanners]], [[item-ftl-jumper]]

## Open Questions
- [ ] What pool `<augment name="RANDOM"/>` draws from, and whether rarity-0 items are excluded
      from it (they should be, by the meaning of `0`, but nothing states it).
- [ ] What `DLC_AUGMENTS` contains — it is a `blueprintList`, not a single augment.
- [ ] How many augment slots a ship has, and whether any event can exceed them.
- [ ] Whether the augment-overwrite bug Fandom reports on [[chain-slug-cruiser-unlock]] — a
      `standard` reward roll overwriting a guaranteed augment — is present in this 1.6.x build.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
