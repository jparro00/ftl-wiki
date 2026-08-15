---
id: concept-scrap-economy
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
related_events: []
tags: [mechanics, economy, scrap, rewards, unknown-magnitudes]
---

# The scrap economy

## Definition & Context

Scrap is FTL's only currency: it buys systems, upgrades, weapons, drones, augments, crew and
repairs. Every event that pays you pays in scrap or in something you would otherwise buy with
scrap.

**The event files describe the economy in two incompatible ways**, and the difference is the
single most important thing to know when reading a page here:

| Form | Uses | Precision |
|---|---|---|
| `<autoReward level="MED">standard</autoReward>` | 551 | **a tier, not a number** — see [[concept-autoreward-tiers]] |
| `<item type="scrap" min="20" max="30"/>` | 116 | **an exact range** |

So roughly **five out of six scrap payments in the game are unquantified in the data.** When
an event page here says "medium scrap" rather than a figure, that is not laziness — the number
is genuinely not in the files.

## What the exact ranges tell us

Of the 116 explicit `<item type="scrap">` records ([[source-events-xml]] and siblings):

- **84 are losses and only 32 are gains.** Explicit scrap figures are used mostly for *costs* —
  the price of a bribe, a purchase, a toll — while rewards are left to the `autoReward` tiers.
- **The largest single explicit gain is 100 scrap.**
- Typical negotiated payments sit in the tens: [[chain-merchant-s-request]]'s delivery job pays
  20–30 for accepting the lowball, 40–55 with Mind Control, and 55–70 with Weapons 6.

That asymmetry is a design tell: **the game is precise about what it takes from you and vague
about what it gives you.**

## The other currencies

Scrap has three companions, all with exact ranges when they change
([[source-events-xml]]):

| Resource | `item_modify` uses | Skew |
|---|---|---|
| fuel | 73 | **59 gains, 14 losses** — the opposite of scrap |
| drone parts | 49 | mixed |
| missiles | 39 | mixed |

Fuel being mostly *given* is the counterweight to scrap being mostly *taken*: running dry is a
survival problem with its own event family ([[concept-out-of-fuel]]), so the game hands fuel
out freely and charges for everything else.

> ⚠️ **A shipped typo.** One record uses `<item type="missile">` (singular) where the schema
> uses `missiles`. Found by the 2026-08-13 lint census; whether the engine silently ignores it
> is not established here. Filed alongside the other known data bugs in `overview.md`.

## Implications For Play

- **Blue options are usually scrap.** The most consistent return on a system investment is not
  its combat value but the events it unlocks — [[chain-merchant-s-request]]'s Weapons 6 branch
  more than doubles the payout for pressing one button. See [[concept-blue-options]].
- **Crew kills pay better than hull kills.** `deadCrew` branches routinely sit one
  `autoReward` level above `destroyed` ones, which is a standing scrap argument for boarding —
  see [[concept-autoreward-tiers]].
- **Stores are where scrap becomes power**, so an event that opens one is worth more than its
  face value — see [[concept-stores]].

## Where It Applies
Every event with a reward, which is most of them. The events that are *purely* economic are
[[event-free-scrap-with-resources]], [[event-crew-hiring-station]],
[[event-improve-reactor-for-supplies]], [[event-asteroid-mining-colony]] and
[[event-lanius-craftsmen]].

## Related
- [[concept-autoreward-tiers]] — why most payments have no number
- [[concept-stores]] — where scrap is spent
- [[concept-out-of-fuel]] — the resource crisis scrap cannot directly solve
- [[concept-blue-options]] — the main lever on payout size
- [[concept-blueprint-rarity]] — what the `weapon`/`drone`/`augment` tiers can hand you

## Open Questions
- [ ] **What `LOW`/`MED`/`HIGH` are worth in scrap**, and whether they scale with sector depth.
      This is the wiki's largest single unknown and it blocks every quantitative comparison.
- [ ] Store prices — not held in the event files; they would come from `blueprints.xml` `<cost>`
      values, which this page does not survey.
- [ ] Whether the engine reads the singular `missile` type or drops the effect.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
