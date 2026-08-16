---
id: concept-autoreward-tiers
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-16
sources: 8
related_events: []
tags: [mechanics, rewards, schema, data-bugs, resolves-open-question]
---

# `autoReward` — the reward matrix, and what it is worth

## Definition & Context

`<autoReward level="MED">standard</autoReward>` is how almost every event in FTL pays out.
It is **the single most common effect tag in the game — 555 uses** across the event files
([[source-events-xml]] and siblings) — and it is a *matrix*, not a number: a **level** crossed
with a **tier**.

The event files carry the matrix and no magnitudes at all. Until 2026-08-16 that made
`MED standard` unquantifiable here, and it was the wiki's largest single unknown.
**[[source-fandom-rewards]] and its two tables close it** — see *The numbers*, below. The
caveats are real and stated there, but "medium scrap" now has a range attached.

## The two axes

**Level** — how much (227 `MED`, 145 `HIGH`, 138 `LOW`, 32 `RANDOM`, plus 13 misspelled):

| Level | Uses | Meaning |
|---|---|---|
| `MED` | 227 | the default payout |
| `HIGH` | 145 | typically a crew-kill or a completed quest |
| `LOW` | 138 | a consolation, or a small favour |
| `RANDOM` | 32 | the game rolls the level too |

**Tier** — what kind of thing (11 distinct values):

| Tier | Uses | What it pays |
|---|---|---|
| `standard` | 290 | scrap + 2 random resources, + a bonus-item roll |
| `scrap_only` | 92 | scrap and nothing else |
| `stuff` | 52 | resources-weighted, low scrap, + a bigger bonus-item roll |
| `weapon` | 37 | a random weapon + scrap |
| `fuel` | 32 | fuel + scrap |
| `drone` | 17 | a random drone schematic + scrap |
| `fuel_only` | 13 | fuel and nothing else |
| `augment` | 8 | a random augment + scrap |
| `missiles` | 6 | missiles + scrap |
| `droneparts` | 5 | drone parts + scrap |
| `scrap` | 3 | see the bugs below |

The most common single combination is `MED standard` (131), then `HIGH standard` (85) and
`LOW standard` (56).

> **Method note.** An earlier revision of this page counted **551** total, 287 `standard`,
> 141 `HIGH`, 91 `scrap_only`. A recount on 2026-08-16 over all 17 event files containing the
> tag gives **555 / 290 / 145 / 92**; the four extra tags are all `HIGH` (three `standard`, one
> `scrap_only`). What the earlier scan dropped was not traced — no single file accounts for
> exactly four. The 556th `<autoReward` string in `raw/gamedata/` is the developer comment
> quoted below, not a tag.

## The developers' own schema

A comment in `events.xml` (in the scratch block above the `*_TEST` events, ~line 97) documents
the tag in the authors' words:

```
<autoReward level=<LOW/MED/HIGH/RANDOM>> tag </autoreward>
where tag is
standard  - which is scrap + 2 resources (possible a weapon)
stuff     - less scrap, mostly resources (intended for surrenders)
fuel / missiles / droneparts  - scrap + that resource
fuel_only / missiles_only / droneparts_only - self explanatory
weapon / augment / drone
item - scrap + that thing
```

This matters twice over. It **confirms Fandom's tier semantics from inside the game files** —
including "intended for surrenders" for `stuff`, which Fandom derived from usage. And the three
tiers it lists that Fandom calls unused — `missiles_only`, `droneparts_only`, `item` — appear
**zero times** in the shipped events, so both lists agree on what is dead.

## The numbers

**Scrap scales with sector depth; resources do not.** That asymmetry is the headline.

### Scrap, by sector and level — Normal difficulty

| Sector | `LOW` | `MED` | `HIGH` |
|---|---|---|---|
| 1 | 7–10 | 12–19 | 19–23 |
| 2 | 10–14 | 16–27 | 27–32 |
| 3 | 13–18 | 21–35 | 35–41 |
| 4 | 16–23 | 26–42 | 42–51 |
| 5 | 19–27 | 31–50 | 50–60 |
| 6 | 22–31 | 36–58 | 58–69 |
| 7 | 25–35 | 40–66 | 66–79 |
| 8 | 28–39 | 45–74 | 74–88 |

([[source-fandom-template-scrap-rewards-normal]]) — `MED` and `HIGH` are **contiguous in every
row**: the top of `MED` is exactly the floor of `HIGH`. `LOW` sits below a gap. And `MED` is the
*widest* band, not the middling one — at sector 8 it spans 30 points against `HIGH`'s 15.

### Resources, flat everywhere

| Resource | `LOW` | `MED` | `HIGH` |
|---|---|---|---|
| Fuel | 1–3 | 2–4 | 3–6 |
| Missiles | 1–2 | 2–4 | 4–8 |
| Drone parts | 1 | 1 | 1–2 |

([[source-fandom-template-resources-rewards]]) — identical in sector 1 and sector 8, on every
difficulty. Note `droneparts` is barely tiered at all: `LOW` and `MED` are both a flat 1.

### The bonus-item roll

- `standard` — **~3%** chance of an extra weapon, augment or drone schematic on top.
- `stuff` — **~6%**, and a successful roll also **upgrades the scrap half** from low to match
  the resources tier.

These are the first quantified probabilities this wiki holds for either tier.

## Precedence — which reward wins

When an event declares a guaranteed item reward *alongside* an `autoReward`
([[source-fandom-rewards]]):

| Guaranteed reward outside the `autoReward` | Effect |
|---|---|
| weapon or drone schematic | **suppresses** the bonus roll; **overwrites** the `weapon` / `augment` / `drone` tiers |
| augmentation | **overwritten by** the bonus roll, and by the `augment` tier |

So weapons and drone schematics beat the auto-reward, and augments lose to it. A `standard`
reward on an event that already guarantees a weapon never rolls its 3% bonus at all.

An `<item_modify>` block — the exact-value mechanism, used for costs as much as gains — can be
**overwritten by an `autoReward`** that happens to award the same resource. Fandom notes this
"causes some bugs"; no specific event is named.

## Reading an event page

- **A tier change is a bigger deal than a level change.** `LOW weapon` hands you an item;
  `HIGH scrap_only` hands you 74–88 scrap in sector 8. Still not comparable, but the scrap side
  now has a figure.
- **`deadCrew` usually pays one level above `destroyed`.** This is the mechanical reason
  boarding is rewarded across the whole event pool — see [[chain-rock-bride]],
  [[chain-zoltan-primitives]] and [[chain-construction-yard]] for three worked examples in a
  row. On midpoints that is worth roughly **+36%** scrap at every depth — about +5.5 scrap in
  sector 1, +21.5 in sector 8. The `LOW` → `MED` step is much larger, about **+80%**.
- **Resource-tier rewards decay in value.** Resources are flat while scrap quadruples by
  sector 8, so the same `HIGH fuel` beacon is a real payday in sector 1 and near-noise in
  sector 8.
- **`RANDOM` means the level is rolled**, so an event with `RANDOM stuff` has variance the page
  still cannot quantify — the draw's distribution is unknown.

## Lanius fights pay differently

Most Lanius fights in Abandoned sectors use a variant of the default fight rewards
([[source-fandom-rewards]]):

- **Destroying the ship** — a high scrap reward becomes possible, **1 in 4**.
- **Killing the crew** — **no weapon** reward; a drone schematic instead, **1 in 8**.
- **Fuel** — **1 in 8**, down from **2 in 9**.

Ships in the default-reward categories offer **random-tier** `stuff` on surrender.

## Shipped data bugs in this tag

Recorded rather than silently corrected, per §4:

> ⚠️ **Level spellings that break the schema.** The schema uses `LOW`/`MED`/`HIGH`/`RANDOM`,
> but the files also contain **`MEDIUM` (6 uses)** and **lowercase `low` (7 uses)**. Whether
> the engine falls through to a default on these is not established here. `MEDIUM` was already
> recorded in `overview.md`'s known-bugs list; the lowercase `low` variants were found by the
> 2026-08-13 lint census.

> ⚠️ **`scrap` vs `scrap_only`.** Three uses of the tier `scrap` sit alongside 92 uses of
> `scrap_only`. It appears in **neither** the developer comment nor Fandom's list, and remains
> a probable typo for `scrap_only`.

> ⚠️ **`scrap_only` is undocumented by the developers' own comment** — yet it is the second
> most used tier in the game (92). Fandom documents it as live. Reading: the comment is a stale
> design note that predates the tier. Recorded because it means the comment cannot be treated
> as a complete schema.

**A fallback that was plausible but wrong.** The card pipeline originally mapped only 7 of the
11 tiers and fell through to the `standard` template, so `MED missiles` rendered as *"medium
scrap"* — a wrong statement with no way to notice. It now prints the raw tier name for
anything unmapped. See `tools/EVENT-CARD.md` and the 2026-08-10 tooling entries in `log.md`.
The general rule that came out of it: **a fallback that produces a plausible-but-wrong value
is worse than a visible gap.**

## Confidence & limits

The tier *names and semantics* are confirmed twice over — the game files and the developer
comment. The **magnitudes are community-derived**: Fandom sources both tables to the
third-party "Calculated FTL" Steam guide, which this repo does not hold, and nothing in
`raw/gamedata/` can check them. Treat them as `medium` reliability, and note that the internal
structure (contiguous `MED`/`HIGH`, an exact `7 + 3(n−1)` floor on `LOW`) looks derived rather
than remembered.

> ⚠️ **Normal difficulty only.** Scrap payout depends on difficulty, and the increase per
> sector is **larger on lower difficulties**. Only the Normal table was captured; the Easy and
> Hard tables were not. Every scrap figure on this page and any page quoting it is
> Normal-only — a floor on Easy, a ceiling on Hard.

## Where It Applies
Effectively every event page in this wiki. The events most defined by it are the pure-reward
beacons — [[event-free-scrap-with-resources]], [[event-free-weapon]],
[[event-free-drone-schematic]] — which are an `autoReward` and nothing else.

## Related
- [[concept-scrap-economy]] — what the scrap is for, and the exact-value half of the economy
- [[concept-event-tree-grammar]] — where `autoReward` sits in the grammar
- [[concept-event-list-weighting]] — the other place magnitudes are implicit
- [[concept-blueprint-rarity]] — how `weapon`/`drone`/`augment` tiers pick an item
- [[concept-surrender-offers]] — `stuff` is the surrender tier

## Open Questions
- [x] **The numbers.** **Answered 2026-08-16** from [[source-fandom-rewards]] and its two
      tables — see *The numbers*. Community-derived and Normal-only; an in-game observation of
      any `MED standard` payout in a known sector would raise confidence cheaply.
- [x] **Whether the `weapon`/`drone`/`augment` tiers respect `<rarityList>` sector overrides.**
      **Yes** — rarity gates event-reward eligibility (0 = never), and `SetRarity` writes the
      sector's `rarityList` over the base values on entry. See [[concept-blueprint-rarity]].
- [ ] Whether `RANDOM` draws uniformly across the three levels.
- [ ] Whether the engine treats `MEDIUM` and `low` as valid, or silently defaults them.
- [ ] The Easy and Hard scrap tables — not captured, and the only remaining axis of the matrix
      this wiki cannot state.
- [ ] Which events the `autoReward`-overwrites-`item_modify` bug actually bites. Fandom asserts
      it happens and names none.

## Sources
- [[source-fandom-rewards]] (per raw/wiki/rewards.md)
- [[source-fandom-template-scrap-rewards-normal]] (per raw/wiki/template-scrap-rewards-normal.md)
- [[source-fandom-template-resources-rewards]] (per raw/wiki/template-resources-rewards.md)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md)
