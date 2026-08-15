---
id: event-zoltan-trade-hub
type: event
event_name: ZOLTAN_TRADE_HUB
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: quest
hostile: false
blue_options: [teleporter, zoltan crew]
chain: [[[chain-zoltan-primitives]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [blue-option, store-chance, quest-marker, boarding-risk, scrap-cost, unique, zoltan]
---

# Zoltan trade hub — `ZOLTAN_TRADE_HUB`

## Summary
A Zoltan trading station you need papers to enter. Getting in is the whole event: a
Teleporter or a Zoltan crew member walks you in for free (or 10 scrap); without either,
talking your way in is a coin flip between getting in and getting boarded. Once inside,
it is another coin flip between **a store opening** and **a quest marker for
[[event-zoltan-quest-primitives]]** — the developer comment on the event calls it
*"a 50/50 chance of quest start"*.

## Trigger & Where It Appears
- Event list: `QUESTS_ZOLTAN` in `events_zoltan.xml`, an un-annotated base entry
  ([[source-events-zoltan]]).
- `QUESTS_ZOLTAN` is allocated at `min=0 max=1` in both `ZOLTAN_SECTOR`
  ([[sector-zoltan-controlled-sector]]) and `ZOLTAN_HOME`
  ([[sector-zoltan-homeworlds]]) ([[source-sector-data-xml]]) — so a Zoltan sector
  contains **at most one** quest beacon, and it is a five-way draw with
  `ZOLTAN_QUEST_PRIMITIVES`, `FEDERATION_PLANET_SIGNAL`, `QUEST_MANTIS_INVASION_START`
  and `QUEST_CREWDEAD_START`.
- `unique="true"` — at most once per run.
- Beacon: **quest beacon**, no ship on Long-Ranged Scanners
  ([[source-fandom-zoltan-trade-hub]]).

### Odds of drawing it
`QUESTS_ZOLTAN` has five distinct members, none duplicated. **Assuming uniform selection
across list entries** ([[concept-event-list-weighting]]), a Zoltan quest beacon is this
event **1/5** of the time — and a sector may allocate zero quest beacons at all.

## Text
> You come to a Zoltan trade and supply hub - everything the weary traveler needs,
> provided they have the right documentation.

(`event_ZOLTAN_TRADE_HUB_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Try to talk your way in. | — (`hidden="true"`) | Loads `ZOLTAN_TRADE_HUB_TALK` — two entries, below. | — |
| 2 | **(Teleporter)** Beam directly to the civilian deck. | `req="teleporter" lvl="1"` | *"You re-materialize in a dark corner of the main concourse and are able to conduct your investigations in peace."* → continue → `ZOLTAN_TRADE_HUB_SUCCESS`. | 100% |
| 3 | **(Zoltan Crew)** Present his official documentation and pay the entry fee. | `req="energy"` | *"They scan ID that declares your crewmember an official citizen, collect their fee, and let you pass."* → **−10 scrap** (fixed), then continue → `ZOLTAN_TRADE_HUB_SUCCESS`. | 100% |
| 4 | Leave. | — (`hidden="true"`) | *"You don't have the papers - well, the neuro-laced identity bracelets - to get in, so best not to try."* → nothing. | 100% |

### `ZOLTAN_TRADE_HUB_TALK` — two entries, no repeats (1/2 each)
**Assuming uniform selection across list entries** ([[concept-event-list-weighting]]):

| Odds | Text | Effect |
|---|---|---|
| 1/2 | *They don't see many of your species in these parts, and you stick out like a Casvagarian Sea Slug in a Plutonian Shrimp Stew. You make it back to the ship with a gang of Zoltan guards in tow!* | `<ship load="ZOLTAN_SHIP" hostile="true"/>` **and** `<boarders min="2" max="4" class="energy"/>` — a Zoltan fight *with* 2–4 Zoltan boarders already aboard. |
| 1/2 | *You pose as traders and succeed in bypassing airlock security - however, it's only a matter of time before someone realizes your ID cards are counterfeit!* | Continue → `ZOLTAN_TRADE_HUB_SUCCESS`. |

### `ZOLTAN_TRADE_HUB_SUCCESS` — two entries, no repeats (1/2 each)
Reached identically by all three successful routes:

| Odds | Text | Effect |
|---|---|---|
| 1/2 | *You head into a ship supply store. It is a well-equipped, self-service affair. An order is dialled into a terminal, scrap is deposited, and the item is dispatched from a nearby chute.* | `<store/>` — **a store opens**. |
| 1/2 | *You head into the cantina for gossip. Topics of conversation in the cantina range from crop distribution microbes to the joys of Slug pleasure cruises.* | Continue → *"You overhear one group discussing a newly discovered planet yet to have first contact, and note down its location."* → `<quest event="ZOLTAN_QUEST_PRIMITIVES"/>` — **a quest marker is added to your map**. |

This is the 50/50 the developer comment refers to
([[source-events-zoltan]], inline comment on the event).

### The `ZOLTAN_SHIP`
`auto_blueprint="SHIPS_ZOLTAN"`, `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` — default
rewards, and **no `<surrender>` and no `<escape>` block at all**
([[source-events-ships]]). Fandom notes the same absence
([[source-fandom-zoltan-trade-hub]]). The fight runs to a finish.

> ⚠️ **CONTRADICTION (wording, minor):** Fandom writes *"An order is **dialed** into a
> terminal"*; the game string uses the British *"dialled"*
> ([[source-fandom-zoltan-trade-hub]] vs [[source-text-events-xml]]). Trusting the game
> files.

## Blue Options
- **Teleporter** (`req="teleporter" lvl="1"`) — walks you straight into
  `ZOLTAN_TRADE_HUB_SUCCESS` for **free**, skipping the boarding risk entirely. Any level
  of Teleporter satisfies it.
- **Zoltan crew member** (`req="energy"`) — same result for a flat **10 scrap**. Note this
  choice is **not** `hidden="true"`, unlike the other three, and carries no `blue="false"`,
  so it renders as a normal blue option.

Both bypass the 1/2 chance of a fight-plus-boarders. Neither improves the store-vs-quest
split inside.

## Rewards & Risks
- **Best case:** a free store opening in a sector where stores are otherwise fixed at two
  ([[event-store-zoltan]]) — or a quest marker leading to
  [[event-zoltan-quest-primitives]].
- **Cost:** 10 scrap on the Zoltan-crew route, nothing on the other three.
- **Risk (talk route only):** 1/2 chance of a Zoltan hull fight **with 2–4 Zoltan boarders
  already on your ship**. Zoltan boarders damage systems on death, and the ship has a
  Super Shield and cannot be made to surrender or flee. This is the single worst branch
  and it is a coin flip.
- Leaving is free.

## Strategy Notes
- *Opinion:* with a Teleporter or any Zoltan aboard this is a strongly positive event —
  take it. Without either, "Try to talk your way in" is a genuine gamble: a free store or
  quest marker against a boarding fight you cannot end early.
- The quest-marker branch also costs a jump and advances the Rebel fleet, so it is not
  free value; the store branch is.
- Fandom notes the quest event can also be encountered standalone as
  [[event-zoltan-quest-primitives]], so drawing the store half here does not lock you out
  of that content permanently ([[source-fandom-zoltan-trade-hub]]).

## Related
- [[chain-zoltan-primitives]] — the full quest line this belongs to
- [[event-zoltan-quest-primitives]] — where the quest-marker branch leads
- [[event-store-zoltan]] — the sector's guaranteed store beacons; this event is a possible
  third
- [[event-zoltan-ship-asks-to-dock]], [[event-zoltan-wise-man]] — the other Zoltan events
  that can turn hostile without warning
- [[concept-event-list-weighting]] — basis for the 1/2 and 1/5 figures
- [[concept-sector-event-allocation]] — how `QUESTS_ZOLTAN` reaches the map

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Does the Zoltan-crew route require the Zoltan to be alive at the time?
- [ ] Do the 2–4 Zoltan boarders arrive before or after the enemy ship's shields come up?

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-zoltan-trade-hub]] (per raw/wiki/zoltan-trade-hub.md)
