---
id: concept-quest-beacon-placement
type: concept
version: unknown
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 2
related_events: []
tags: [mechanics, quests, routing, sector-8]
---

# Where a quest beacon lands — and when the quest is silently thrown away

## Definition & Context
Accepting a quest does not place the destination where you are. The game has to *put the
marker somewhere*, and where it puts it depends on how much of the current sector you have
left. Late enough in a run, the answer is "nowhere" — and the quest you just accepted is
discarded without telling you.

## The rule

Per [[source-fandom-random-events]] (per `raw/wiki/random-events.md`):

1. **Normally**, the quest beacon is placed in the **current sector**.
2. **If you don't have many jumps left**, the game **pushes the quest into the next sector**
   instead.
3. **If that happens in sector 7, the quest is cancelled** — *"because quests are not allowed
   in sector 8."*

The source states the rule qualitatively. It does not define "not many jumps left" as a
number, and no file in `raw/gamedata/` exposes the threshold.

## What the data corroborates

The sector-8 half checks out from the other side. The `FINAL` `<sectorDescription>` in
`raw/gamedata/sector_data.xml` — `minSector="7"`, i.e. the eighth and last sector — allocates
exactly four event lists ([[source-sector-data-xml]]):

```xml
<startEvent>BOSS_NEUTRAL</startEvent>
<event name="STORE"                min="1"  max="1"/>
<event name="BOSS_REPAIR_STATION"  min="3"  max="3"/>
<event name="BOSS_HOSTILE"         min="6"  max="6"/>
<event name="BOSS_NEUTRAL"         min="7"  max="10"/>
```

None of those lists carries a `<quest>` tag. Every `<quest event="…"/>` in the game data —
`CRYSTAL_UNLOCK`, `ROCK_UNLOCK2`, `ENGI_UNLOCK_3`, `MANTIS_NAMED_THIEF_STASH`,
`HIDDEN_FEDERATION_BASE_LIST`, `MERCHANT_DELIVER`, `QUEST_ESCORT_ARRIVE` and the rest — sits
in an event allocated to some other sector type. So the Last Stand has no quest surface at
all, which is what a hard "no quests in sector 8" rule would look like from the data side.
This corroborates the claim without independently proving the *cancellation* behaviour, which
is engine logic and is not in the files.

## Implications For Play

- **A quest accepted deep into sector 7 can be worth nothing.** The push-to-next-sector
  fallback has nowhere to land, and the quest is dropped. There is no in-game warning.
- **Take quest-bearing events early in a sector**, not on your way to the exit — the earlier
  you are, the more likely the beacon lands in the sector you are actually still flying
  through.
- **Ship-unlock quests are the expensive case.** [[chain-crystal-cruiser-unlock]],
  [[chain-rock-cruiser-unlock]] and the other unlock chains span multiple beacons; a step
  pushed into the next sector costs jumps you may not have against
  [[concept-rebel-fleet-advance]], and a step pushed out of sector 7 is the chain ending
  silently.
- It also means a quest marker appearing in the *next* sector is normal behaviour, not a bug.

## Where It Applies
- Every event containing a `<quest event="…"/>` tag — the unlock chains
  ([[chain-crystal-cruiser-unlock]], [[chain-rock-cruiser-unlock]],
  [[chain-mantis-cruiser-unlock]], [[chain-slug-cruiser-unlock]],
  [[chain-zoltan-cruiser-unlock]], [[chain-stealth-cruiser-unlock]]) and the standalone
  quest-givers such as [[event-merchant-s-request]] and [[event-escort-civilians]].
- [[sector-the-last-stand]] — the sector where the fallback has nowhere to go.

## Related
- [[concept-sector-event-allocation]] — how beacons get their events in the first place
- [[concept-rebel-fleet-advance]] — why "how many jumps left" is a live constraint
- [[concept-event-uniqueness]] — the other per-sector scoping rule

## Open Questions
- [ ] What counts as *"not many jumps left"* — no source gives a number.
- [ ] Does the push-to-next-sector fallback apply to every quest, or only to those whose
      destination type exists in the next sector?
- [ ] Is the cancellation silent in-game, or is the sector-7 message shown in
      `raw/wiki/random-events.md`'s screenshot caption (*"Message given when a quest is
      triggered late in sector 7"*) the warning? The image is not in `raw/`, so its text is
      unknown.

## Sources
- [[source-fandom-random-events]] (per raw/wiki/random-events.md)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
