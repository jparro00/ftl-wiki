---
id: concept-sector-event-allocation
type: concept
version: both
first_seen: 2026-08-09
last_updated: 2026-08-16
sources: 6
related_events: []
tags: [mechanics, methodology, unresolved, ae-delta]
---

# How events get allocated to beacons — and what "unreachable" can mean

## Definition & Context
Two different allocation systems exist in the game data, and they do not agree. Which one
the engine reads determines whether a set of shipped events is reachable at all.

## System 1 — `sector_data.xml`, per sector *type*
Each `<sectorDescription>` lists the event lists it draws on with beacon counts:

```xml
<event name="HOSTILE_ROCK" min="6" max="8"/>
```

This is comprehensive: it covers all 19 playable sectors and is the basis of every
sector page in this wiki. ([[source-sector-data-xml]])

## System 2 — `<eventCounts>` in `newEvents.xml`, per map *depth*
A parallel scheme indexed by depth, not sector type:

```xml
<eventCounts sector="0"> ... <event name="HOSTILE2" .../> ... </eventCounts>
```

Four blocks exist, `sector="0"` through `sector="3"`, one headed *"PLANNING FOR the 3rd
Sector"*. ([[source-newevents]])

## What is established

- `HOSTILE2` and `NEUTRAL2` are allocated by **zero** `sectorDescription`s. They appear
  **only** in `eventCounts` blocks.
- `HOSTILE_BOARDING` is allocated `min=0 max=0` in Federation Space and commented out in
  the Civilian Sector — dead under System 1 — but is allocated 1–2 by `eventCounts`.
- `dlcEventsOverwrite.xml` defines `OVERRIDE_HOSTILE2`, so Advanced Edition maintains a
  replacement for a list that System 1 never allocates.

## The correction: absence from `sector_data.xml` is NOT proof of unreachability

Two `OVERRIDE_` lists have **zero** `sectorDescription` allocations yet are plainly
functional:

| List | Allocated by sector_data | Reached how |
|---|---|---|
| `NEUTRAL_EXIT` | 0 | the exit beacon — engine-called by name |
| `FEDERATION_BASE_ASSIST` | 0 | the Federation base — engine-called by name |
| `NEUTRAL` | 2 (both Slug nebulas) | *also* the leftover-beacon fallback, "hardcoded" per the file's own comment — see below |

So the engine resolves some list names directly, outside either allocation table. A list
with no sector allocation may still be live.

> **Rule for this wiki:** do not tag an event `unreachable` solely because its list has no
> `sector_data.xml` allocation. That justifies `sectors: []` and an open question — nothing
> stronger. `unreachable` requires positive evidence: a commented-out sole reference, or no
> reference anywhere in `raw/gamedata/`.

## RESOLVED 2026-08-15 — `OVERRIDE_X` does replace `X` in sector allocation

Settled by direct in-game observation, not by a data file. FTL Hyperspace logs sector
generation, and a Civilian Sector generation printed an `ITEMS` allocation:

```
-- Generating Events --
Sector: CIVILIAN_SECTOR
Getting Event: ITEMS   x2
...
Creating event: STORE_REBELSIDE
```

`STORE_REBELSIDE` is **not** a member of `<eventList name="ITEMS">`
(`raw/gamedata/newEvents.xml:185`). It exists only in `<eventList name="OVERRIDE_ITEMS">`
(`raw/gamedata/dlcEventsOverwrite.xml:119`). An `ITEMS` allocation produced it, so under
Advanced Edition the sector allocator resolves the name `ITEMS` to `OVERRIDE_ITEMS`.

What this settles, and what it does not:

- **Settled:** `OVERRIDE_X` substitutes for `X` in `sectorDescription` allocation. The AE
  deltas `extract-sector.py` records as `override.applies: "unconfirmed"` are live content.
- **Not settled:** whether the substitution also applies where the engine resolves a list
  name directly (the exit beacon, the Federation base, the leftover-beacon fallback) rather
  than through a sector allocation. The same evidence does not reach those call sites —
  though for the fallback there is separate file evidence, below.

The nine lists this changes, and their deltas, are tabulated in [[concept-ae-vs-vanilla]].
Note `OVERRIDE_HOSTILE1` also *removes* `AUTO_BAIT` — the only removal among them, so
substitution is not purely additive.

> ⚠️ **Evidence not yet in `raw/`.** This rests on `FTL_HS.log` from a live 2026-08-15
> session, which is an observation the user's game produced rather than a file dropped into
> the source layer. Reliability is that of a single observed run for the *negative* claim
> (what the lists do elsewhere) but effectively decisive for the *positive* one: an event
> appeared that only one list contains.

## The leftover-beacon fallback — and it *is* in the files (2026-08-16)

A run out of allocations before it runs out of beacons fills the rest from the `NEUTRAL`
list. [[source-fandom-sectors]] (per `raw/wiki/sectors.md`, "Fallback events") states the
rule and says `OVERRIDE_NEUTRAL` replaces it under Advanced Edition.

That is not the only evidence. Subset's own comment sits on the list definition, in both
editions' copies:

```xml
<eventList name="NEUTRAL">           <!-- newEvents.xml -->
<eventList name="OVERRIDE_NEUTRAL">  <!-- dlcEventsOverwrite.xml:139 -->
<!-- This event list is hardcoded to fill out a sector if it ran out of all other calls for that sector -->
```

So the mechanic is attested by the game files, at higher reliability than the community
wiki, and "hardcoded" is consistent with the engine resolving the name directly rather
than through `sector_data.xml`. Two consequences for this page:

- The fallback earns its row in the table above, alongside `NEUTRAL_EXIT` and
  `FEDERATION_BASE_ASSIST` — a third list the engine reaches by name. Unlike those two,
  `NEUTRAL` *is* also allocated conventionally, by the two Slug nebulas (`min 1 max 2`).
- The comment appearing on **both** the base and the `OVERRIDE_` copy is evidence — not
  proof — that the AE substitution is real at this call site. Against it: the identical
  comment is copy-pasted onto `OVERRIDE_NEUTRAL_EXIT`, where it is simply wrong (that is
  the exit list, not the fill-out list), so the comment is not carefully placed.

### The AE delta is one event

| List | Members | Delta |
|---|---|---|
| `NEUTRAL` → `OVERRIDE_NEUTRAL` | 19 → 20 | **+`EMPTY_STATION2`** |
| `NEUTRAL_EXIT` → `OVERRIDE_NEUTRAL_EXIT` | 17 → 18 | **+`EMPTY_STATION2`** |

Nothing is removed or reordered — unlike `OVERRIDE_HOSTILE1`, which drops `AUTO_BAIT`.
`EMPTY_STATION2` ([[event-abandoned-station]], `newEvents.xml:1081`, `unique="true"`) is
referenced by **no other list anywhere** in `raw/gamedata/`, so it is AE-only content
reachable only as filler — which is why it is the deciding observation for the open
question below. That event's page has recorded the "hardcoded" comment since 2026-08-09;
this page had simply not absorbed it.

The delta is small because the base `NEUTRAL` list already carries eight events the file
itself tags as DLC — `REFUGEE_NO_DISTRESS`, `WRECKAGE_EVENT`, `FUELING_STATION`,
`PIRATE_SALESMAN`, `TERRAFORMING_SCAN`, `REBEL_CHECKPOINT`, `REBEL_HELPERS`, `ROGUE_REBEL`,
each commented `<!--DLC - down below-->` or `<!--DLC matt - down below-->`. AE content is
therefore **not** confined to the `OVERRIDE_` branch.

> ⚠️ **What "vanilla" can mean here.** This repo holds one copy of the game data, from an
> Advanced Edition install. The non-`OVERRIDE_` branch is the DLC-off branch *of AE-era
> files*, not the 1.03.3 shipped `newEvents.xml`, which we do not have. Whether those eight
> DLC-tagged entries were present pre-AE cannot be checked from `raw/`.

Two other filler mechanisms are distinct from this one and easy to confuse with it:
non-nebula beacons swallowed by cloud graphics are reassigned from the default `NEBULA`
list ([[concept-nebula-mechanics]]), and the exit beacon draws from `EXIT_LIST`, outside the
sector table entirely.

## What is NOT established

**Whether `eventCounts` is live or legacy.** The wiki cannot settle it:

- *For legacy:* `sector_data.xml` is complete and covers every playable sector; the
  "PLANNING FOR" header reads like a design note; `HOSTILE2`/`NEUTRAL2` are defined as
  single `<event>`s that nothing else references.
- *For live:* Advanced Edition still ships an `OVERRIDE_HOSTILE2`, which is effort spent on
  a list that would otherwise be dead; and `NEUTRAL_EXIT` proves zero-allocation lists can
  function.

## Consequences if it is live
- `HOSTILE_BOARDING` events become reachable at depths 0–3, and
  [[event-boarders-asteroid]]'s `unreachable` tag is wrong.
- [[event-rebel-pds]] becomes reachable, and its empty `sectors:` is wrong.
- Depth-based allocation would coexist with type-based allocation, and no sector page
  currently reflects that.

## A third meaning of "unreachable": the bug

Allocation is not the only way shipped content fails to appear. [[source-fandom-random-events]]
states, in the note under its distress category, that *"some other events were meant to occur
at a distress beacon, but they won't due to coding errors"* — and that the community wiki
therefore leaves them out of the category. It names none of them, and gives no mechanism.

That adds a third case to this page's subject, alongside allocated-to-nothing (`HOSTILE2`,
`NEUTRAL2`) and allocated-with-`min=0 max=0` ([[sector-federation-space]]): **allocated
correctly, but broken in the engine.** Nothing in `raw/gamedata/` can show it, since the
defect is in code the files do not contain. It is also a reason not to treat "no Fandom page
exists" as evidence an event is fictional — the same source says events that do not appear in
unmodified FTL are deliberately given no article.

The same page notes that events unreachable in the unmodified game *"do not have individual
article pages and are not part of any category"*, which is why `HOSTILE2` and `NEUTRAL2`
members have no community coverage to check this wiki's reading against.

> ⚠️ Unverified from the data side. Recorded because it changes what an absence means, not
> because it can be confirmed here.

## Where It Applies
Every event whose only list membership is `HOSTILE1`, `HOSTILE2`, `NEUTRAL2` or
`HOSTILE_BOARDING`; and the `sectors:` field of every event page.

## Related
- [[concept-event-tree-grammar]] — the node grammar every event is built from
- [[concept-event-list-weighting]] — list weighting, once allocation has selected a list
- [[sector-federation-space]] — where `HOSTILE_BOARDING` is `min=0 max=0`
- [[sector-vestigial-definitions]] — the other case of dead-looking structure in the data
- [[concept-modding-and-the-append-convention]] — the same allocation step written forwards,
  by a mod author adding a sector
- [[concept-quest-beacon-placement]] — allocation's blind spot: quest beacons are placed by a
  different rule, and can be discarded
- [[concept-event-uniqueness]] — how much of a sector's pool a single beacon consumes

## Open Questions
- [ ] **Does the engine read `<eventCounts>`?** Needs the binary or an in-game
      observation — no data file answers it.
- [ ] Do boarding events occur in Federation Space in practice? A single observed
      `BOARDERS_*` event there would prove `eventCounts` live and settle this page.
- [x] ~~Does `OVERRIDE_X` replace `X`~~ — resolved above **for sector allocation**.
      Still open for names the engine resolves directly, outside either allocation table.
- [ ] **Does `OVERRIDE_NEUTRAL` substitute at the fallback call site?** Narrowed, not
      closed: the "hardcoded to fill out a sector" comment sits on both copies, which is
      suggestive, and [[source-fandom-sectors]] asserts the substitution outright — but the
      same comment is mis-copied onto `OVERRIDE_NEUTRAL_EXIT`. Decidable in play: a single
      observed `EMPTY_STATION2` would settle it, since that event is in no other list.
- [ ] Whether the pre-AE `NEUTRAL` list differed from the one shipped in the AE files. Not
      answerable from `raw/` — it would need a 1.03.3 copy of `newEvents.xml`.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml) — the
  `OVERRIDE_NEUTRAL` definition and the "hardcoded to fill out a sector" comment
- [[source-fandom-sectors]] (per raw/wiki/sectors.md) — the "Fallback events" rule, and the
  `NEBULA` / `EXIT_LIST` filler mechanisms it is distinct from
- [[source-fandom-random-events]] (per raw/wiki/random-events.md) — bugged distress events,
  and the exclusion of unreachable content from the community wiki
- [[source-modding-research]] (per raw/modding/2026-08-12-ftl-modding-research.md) — the
  `sectorDescription` allocation step from the mod author's side
