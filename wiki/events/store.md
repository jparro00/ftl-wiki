---
id: event-store
type: event
event_name: STORE
sectors: [[[sector-federation-space]], [[sector-civilian-sector]], [[sector-uncharted-nebula]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-the-last-stand]]]
beacon_type: store
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [store, varies-text, guaranteed, repeatable, structural]
---

# Store — `STORE`

## Summary
The generic store beacon — the one used by sectors that have no faction-flavoured store
event of their own. No choices, no cost, no risk: it prints a line of flavour text and
opens a store. Its real interest is the allocation table, which is where the guaranteed
store count of half the sectors in the game is set.

## Trigger & Where It Appears
- Defined in `events.xml`, not `newEvents.xml` — the batch join map points at
  `newEvents.xml` because that file contains the legacy `<eventCounts>` blocks that also
  name `STORE`. The event body itself lives at `events.xml` under the "ITEMS!!! — Events
  that give items" heading ([[source-events-xml]]).
- Allocated **directly by the sector**, not through an event list
  ([[source-sector-data-xml]], and see [[concept-sector-event-allocation]]):

  | `sectorDescription` | Wiki sector | min | max |
  |---|---|---|---|
  | `STANDARD_SPACE` | [[sector-federation-space]] | 1 | 2 |
  | `CIVILIAN_SECTOR` | [[sector-civilian-sector]] | 2 | 3 |
  | `NEBULA_SECTOR` | [[sector-uncharted-nebula]] | 0 | 1 |
  | `SLUG_SECTOR` | [[sector-slug-controlled-nebula]] | 0 | 1 |
  | `SLUG_HOME` | [[sector-slug-home-nebula]] | 0 | 1 |
  | `FINAL` | [[sector-the-last-stand]] | 1 | 1 |

- **Not** `unique="true"`, which is what lets it fill more than one slot in a sector.
- Beacon: **store**, no ship on Long-Ranged Scanners ([[source-fandom-store]]).

### Two allocations that are not live sectors
`DEEP_SPACE_SECTOR` and `ABANDONED_SECTOR` also allocate `STORE` at `min=2 max=4`, but
both are stub definitions with no name list and no other events — see
[[sector-vestigial-definitions]] ([[source-sector-data-xml]]).

### Two allocations that are commented out
`ROCK_SECTOR` and `ROCK_HOME` each carry a **commented-out** `<event name="STORE"
min="2" max="4"/>` line. Those sectors use `STORE_ROCK` instead
([[source-sector-data-xml]]). Per [[concept-event-list-weighting]], commented-out entries
are excluded before counting, so the Rock sectors are not part of this event's reach.

## Text
`[varies: textList STORE_TEXT]` — five entries, no repeats
([[source-events-xml]], [[source-text-events-xml]]).

Three of the five are **conditioned on the beacon's planet art**, an attribute the parsed
preview drops:

| # | `planet=` | Text |
|---|---|---|
| 1 | — (any) | *A ship engineer has set up a small shop here.* |
| 2 | `NONE` | *You find yourself surrounded by a group of mysterious alien vessels. They hail you and apparently have some valuable technology for sale.* |
| 3 | `PLANET_POPULATED` | *A transmission from the nearby planet indicates an outpost below which offers supplies to travelers. You send down an away party to check it out.* |
| 4 | `PLANET_POPULATED` | *The space station here has a traveling merchant who shows you his wares.* |
| 5 | `NONE` | *There is only one other ship at this beacon, and it is showing heavy damage. You receive a message on your console: "Greetings, traveler. We were crippled by a band of pirates and are now forced to sell our remaining valuable equipment to acquire the necessary supplies to get home."* |

So the variants are **not** uniformly drawn: which subset is eligible depends on whether
the beacon rolled a populated planet or empty space.

> ⚠️ **CONTRADICTION (minor, wording):** Fandom renders variant 5 as *"Greetings traveler"*
> without the comma; the game string has *"Greetings, traveler."*
> ([[source-fandom-store]] vs [[source-text-events-xml]]). Trusting the game files —
> reliability `high` vs `medium`. Fandom also lists the five variants flat, without the
> `planet=` conditions.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `<store/>` — **a store opens**. Nothing else. | 100% |

## Blue Options
None.

## Rewards & Risks
- **Reward:** store access — repairs, fuel, missiles, drone parts, and whatever the stock
  roll produced.
- **Risk:** none. No ship, no environment, no cost to arrive.

## Strategy Notes
- The allocation table is the takeaway. [[sector-civilian-sector]] guarantees **at least
  two** of these, [[sector-federation-space]] and [[sector-the-last-stand]] at least one,
  and the three nebula sectors can roll **zero** — a Slug or Uncharted sector may contain
  no plain store at all. The Slug sectors compensate with `NEBULA_STORE_SLUG` at
  `min=2 max=2`; the Uncharted Nebula does not have an equivalent guarantee.
- *Opinion:* treat "0–1 stores" sectors as a reason to arrive already stocked, not as a
  reason to avoid them — the nebula sectors pay in other ways.

## Related
- [[event-store-zoltan]], [[event-store-engi]], [[event-store-mantis]],
  [[event-store-pirate]], [[event-store-rebel]], [[event-store-rock]],
  [[event-store-crystal]], [[event-store-lanius]] — the faction-flavoured equivalents
- [[event-store-in-nebula-slug]], [[event-store-in-nebula-uncharted]] — the nebula store
  beacons that top up the sectors where `STORE` can roll zero
- [[sector-vestigial-definitions]] — the two dead sector stubs that also allocate it
- [[concept-sector-event-allocation]] — how these numbers are read
- [[concept-stores]] — how store stock is generated

## Open Questions
- [ ] What determines a beacon's `planet=` value, and therefore which text subset is
      eligible?
- [ ] Does `STORE` roll generic stock, or is stock influenced by the sector it appears in?
- [ ] Were the Rock-sector `STORE` lines ever live, or commented out from the start?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-fandom-store]] (per raw/wiki/store.md)
