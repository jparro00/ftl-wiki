---
id: concept-autoreward-tiers
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
related_events: []
tags: [mechanics, rewards, schema, data-bugs, unknown-magnitudes]
---

# `autoReward` — the reward matrix, and what it does not tell you

## Definition & Context

`<autoReward level="MED">standard</autoReward>` is how almost every event in FTL pays out.
It is **the single most common effect tag in the game — 551 uses** across the event files
([[source-events-xml]] and siblings) — and it is a *matrix*, not a number: a **level** crossed
with a **tier**.

The crucial fact for this wiki: **the numeric scrap behind each pair is not in the event
files.** `MED standard` says "a medium-sized standard reward" and nothing more. That is why
event pages here say "medium scrap" rather than a figure, and why almost every odds and reward
question ends in `unknown`.

## The two axes

**Level** — how much (227 `MED`, 141 `HIGH`, 138 `LOW`, 32 `RANDOM`):

| Level | Uses | Meaning |
|---|---|---|
| `MED` | 227 | the default payout |
| `HIGH` | 141 | typically a crew-kill or a completed quest |
| `LOW` | 138 | a consolation, or a small favour |
| `RANDOM` | 32 | the game rolls the level too |

**Tier** — what kind of thing (11 distinct values):

| Tier | Uses | What it pays |
|---|---|---|
| `standard` | 287 | scrap plus a mix of resources |
| `scrap_only` | 91 | scrap and nothing else |
| `stuff` | 52 | resources with some scrap |
| `weapon` | 37 | a weapon |
| `fuel` | 32 | fuel-weighted |
| `drone` | 17 | a drone schematic |
| `fuel_only` | 13 | fuel and nothing else |
| `augment` | 8 | an augment |
| `missiles` | 6 | missiles |
| `droneparts` | 5 | drone parts |
| `scrap` | 3 | see the bugs below |

The most common single combination is `MED standard` (131), then `HIGH standard` (82) and
`LOW standard` (56).

## Why this matters for reading an event page

- **A tier change is a bigger deal than a level change.** `LOW weapon` hands you an item;
  `HIGH scrap_only` hands you scrap. They are not comparable, and no page here converts
  between them.
- **`deadCrew` usually pays one level above `destroyed`.** This is the mechanical reason
  boarding is rewarded across the whole event pool — see [[chain-rock-bride]],
  [[chain-zoltan-primitives]] and [[chain-construction-yard]] for three worked examples in a
  row.
- **`RANDOM` means the level is rolled**, so an event with `RANDOM stuff` has variance the
  page cannot quantify.

## Shipped data bugs in this tag

Recorded rather than silently corrected, per §4:

> ⚠️ **Level spellings that break the schema.** The schema uses `LOW`/`MED`/`HIGH`/`RANDOM`,
> but the files also contain **`MEDIUM` (6 uses)** and **lowercase `low` (7 uses)**. Whether
> the engine falls through to a default on these is not established here. `MEDIUM` was already
> recorded in `overview.md`'s known-bugs list; the lowercase `low` variants were found by the
> 2026-08-13 lint census and are new.

> ⚠️ **`scrap` vs `scrap_only`.** Three uses of the tier `scrap` sit alongside 91 uses of
> `scrap_only`. It is not in the documented tier list and may be a typo for `scrap_only`.

**A fallback that was plausible but wrong.** The card pipeline originally mapped only 7 of the
11 tiers and fell through to the `standard` template, so `MED missiles` rendered as *"medium
scrap"* — a wrong statement with no way to notice. It now prints the raw tier name for
anything unmapped. See `tools/EVENT-CARD.md` and the 2026-08-10 tooling entries in `log.md`.
The general rule that came out of it: **a fallback that produces a plausible-but-wrong value
is worse than a visible gap.**

## Where It Applies
Effectively every event page in this wiki. The events most defined by it are the pure-reward
beacons — [[event-free-scrap-with-resources]], [[event-free-weapon]],
[[event-free-drone-schematic]] — which are an `autoReward` and nothing else.

## Related
- [[concept-scrap-economy]] — what the scrap is for
- [[concept-event-tree-grammar]] — where `autoReward` sits in the grammar
- [[concept-event-list-weighting]] — the other place magnitudes are implicit
- [[concept-blueprint-rarity]] — how `weapon`/`drone`/`augment` tiers pick an item

## Open Questions
- [ ] **The numbers.** What `LOW`/`MED`/`HIGH` resolve to in scrap, and whether they scale with
      sector depth. This is the largest single unknown in the wiki.
- [ ] Whether `RANDOM` draws uniformly across the three levels.
- [ ] Whether the engine treats `MEDIUM` and `low` as valid, or silently defaults them.
- [ ] Whether the `weapon`/`drone`/`augment` tiers respect `<rarityList>` sector overrides.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
