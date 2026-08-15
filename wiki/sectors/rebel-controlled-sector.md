---
id: sector-rebel-controlled-sector
type: sector
sector_id: REBEL_SECTOR
sector_class: hostile
faction: [[[entity-rebels]]]
min_sector: 0
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 19
tags: [rebel-fleet, pursuit, hostile]
---

# Rebel Controlled Sector

## Summary
Rebel-held space. Repeatable, and available from the first sector onward
(`minSector="0"`), which makes it one of the few hostile sectors a run can meet early.
Fandom groups it with the **hostile** sectors (per [[source-fandom-sectors]]).

Its allocation table is close to the pirate sector's, but the interesting thing about the
pool is the pursuit: of the 49 distinct events the sector can produce, **seven carry a
`modifyPursuit` effect and only one of them can move the clock in your favour**
(per [[source-events-rebel]], [[source-sector-data-xml]]; see
[[concept-rebel-fleet-advance]]).

> **Correction, 2026-08-15.** An earlier version of this page said the pool is "structurally
> identical to the pirate sector's, swapped to `_REBEL` lists". That is at best partial.
> Eight of the nine entries do swap `_PIRATE` → `_REBEL`, but **line 2 is the shared `ITEMS`
> list — the same list in both sectors, and in fourteen sector definitions in all — not a
> swapped one**. One swapped line also differs in more than its name: `QUESTS_REBEL`
> allocates 0–2 where `QUESTS_PIRATE` allocates 0–1. The two sectors also carry different
> track lists (`wasteland` here, `void` there).
> (per [[source-sector-data-xml]], per raw/gamedata/sector_data.xml)

## Character & Hazards
- **6–8 hostile beacons** and a boarding beacon allocated 1–1, so a boarding is guaranteed
  as long as the map has not filled before line 5 (per [[source-sector-data-xml]]).
- **Environments in the pool**: nebula on eight events, plasma/ion storm on three, one
  asteroid field, one red giant, and — via the Advanced Edition override list only — one
  pulsar. All from `<environment>` tags on the events themselves; see
  [[concept-hazards]] and [[concept-nebula-mechanics]].
- **Being caught by the fleet** replaces whatever was at the beacon, event *and*
  environmental hazard alike, with a Rebel Elite Fighter. Killing it yields **1 fuel and no
  scrap** — the armada prevents salvage — or **4 fuel if you were out of fuel**. An
  Anti-Ship Battery is present, firing a shield-piercing 3-hull shot that always breaches,
  **except at a nebula beacon**, where the fleet's arrival instead forces an ion storm.
  Nebula *exit* beacons never gain the storm, and ASBs never occur at exit beacons on Easy.
  (per [[source-fandom-rebel-fleet]], [[source-fandom-environmental-hazards]];
  [[concept-anti-ship-battery]])

## Event Pool

The table is a **filling queue, not a shopping list**: lines are filled in definition order,
each rolling its own min–max inclusive, and generation stops the moment the beacons run out
(per [[source-fandom-sectors]]). Every `NEBULA_*` line is processed first regardless of file
order, because the cloud graphics have to be drawn before events are assigned.

| Fill order | Event list | min | max | Notes |
|---|---|---|---|---|
| 1st (out of order) | `NEBULA_REBEL` | 0 | 5 | drawn before everything else; also defined as a single event elsewhere, so the name is ambiguous |
| 2 | `STORE_REBEL` | 1 | 2 | |
| 3 | `ITEMS` | 1 | 2 | **shared list, not Rebel-specific** |
| 4 | `HOSTILE_REBEL` | 6 | 8 | at most 9 beacons can precede it, so it always fills |
| 5 | `BOARDERS_REBEL` | 1 | 1 | |
| 6 | `DISTRESS_BEACON_REBEL` | 1 | 2 | |
| 7 | `NOTHING_REBEL` | 1 | 2 | |
| 8 | `QUESTS_REBEL` | 0 | 2 | |
| 9 | `NEUTRAL_REBEL` | 5 | 6 | **can be cut entirely** — see below |

Start beacon: `START_BEACON_REBEL` (not part of the allocation; see [[concept-start-beacons]]).
The exit beacon is not in the table either — it draws from the shared `EXIT_LIST`, and an exit
that falls inside a cloud is always empty (per [[source-fandom-sectors]]).

File order and min/max here match the Fandom sector list line for line, which is worth noting
because that page warns its own ordering "does **not** completely reflect the actual order of
events in the game files". For `REBEL_SECTOR` it happens to.
(per [[source-fandom-sectors]], [[source-sector-data-xml]])

## Map Generation Here

Beacons are placed before any events are assigned: a **6×4 grid**, each cell 80% likely to hold
a beacon, so **at most 24** (per [[source-fandom-sectors]], [[source-xftl-sector-map]]). This
sector's allocation totals **16 at minimum and 30 at maximum**, which produces two mutually
exclusive regimes:

- **High rolls — the table overruns the map.** Summing the maxima of lines 1–8 gives exactly
  24. So on a maximal roll the map is full before `NEUTRAL_REBEL` is reached and the sector's
  entire neutral pool is discarded. That pool holds `AUTO_DEFENSE_RADAR`, the **only** event in
  the sector whose tree contains a negative `modifyPursuit`.
- **Low rolls — the map outruns the table.** With a minimum of 16 allocated against a map that
  Fandom describes as holding 19–24 beacons, a quiet roll leaves beacons unassigned at the end
  of the definition. Those are filled from the shared `NEUTRAL` fallback list
  (`OVERRIDE_NEUTRAL` under Advanced Edition), which is **not** this sector's `NEUTRAL_REBEL`.
  (per [[source-fandom-sectors]], [[source-newevents]], [[source-dlceventsoverwrite]];
  [[concept-sector-event-allocation]])

> ⚠️ **CONTRADICTION — how many beacons a map actually has.** [[source-fandom-sectors]] states
> flatly that sectors contain "between 19 and 24 beacons". [[source-xftl-sector-map]] describes
> the mechanism — 24 cells, 20% chance each is left empty, with a guard that fills a cell anyway
> once empties reach 20% of cells placed so far — which **bounds** the empty count near five but
> states no hard floor. The two are consistent in practice and neither is a game file; the 24
> ceiling is the number this wiki relies on, and the 19 floor is recorded as Fandom's claim
> rather than as a derived fact. Both retained.

## `NEUTRAL_REBEL` Is Not the `NEUTRAL` Fallback

The two share a name and nothing else. `NEUTRAL_REBEL` is line 9 of this sector's definition;
`NEUTRAL` is the hard-coded list the engine uses to fill beacons left over after *any* sector's
definition is exhausted (the game file's own comment says so).

| | `NEUTRAL_REBEL` | shared `NEUTRAL` / `OVERRIDE_NEUTRAL` |
|---|---|---|
| Where it comes from | `raw/gamedata/events_rebel.xml` | `raw/gamedata/newEvents.xml` / `dlcEventsOverwrite.xml` |
| Size | 8 events | 19 events (20 under AE — `EMPTY_STATION2` is added) |
| When it fills | line 9, only if beacons remain | only if the whole definition is exhausted and beacons remain |

Three events sit in both — `REBEL_TRANSPORT`, `BROKEN_REBEL_DRONE` and `AUTO_DEFENSE_ITEM` — so
those can still appear on a map that never reaches line 9. The other five
(`AUTO_CIVILIAN`, `SQUAT_REFUEL_STATION`, `AUTO_DEFENSE_MAP`, `AUTO_DEFENSE_RADAR`,
`ALISON_DEFECTOR`) are line 9 or nothing.

Conversely, the fallback brings in events this sector's own pool does not contain at all,
including `MERCENARY` (hire the mercenary: **2 turns of fleet delay** for 10–25 scrap),
`PIRATE_BRIBER`, `REBEL_CHECKPOINT`, `REBEL_HELPERS` and `ROGUE_REBEL`.
(per [[source-newevents]], [[source-dlceventsoverwrite]], [[source-fandom-the-mercenary]])

> ⚠️ **CONTRADICTION — is the Mercenary reachable here?** [[source-fandom-the-mercenary]] lists
> the event's locations as Civilian, Pirate, Rock, Rock Homeworlds and both Slug nebulas —
> Rebel Controlled is **not** among them. But the same page tags the event `alsooccur=filler`,
> `MERCENARY` is a member of the shared `NEUTRAL`/`OVERRIDE_NEUTRAL` fallback in the game files,
> and [[source-fandom-sectors]] says the fallback fills leftover beacons in any sector. The
> game files plus the fallback rule are the better bet: it can occur here, as a filler. The
> per-event "Locations" lists appear to enumerate *allocation-list membership only* and to omit
> fallback reachability. Both claims retained.

## Beacon Markers

What the map draws before you jump is set by `<distressBeacon/>` and `<store/>` on the event,
not by which allocation line placed it, and the two sets routinely disagree
(per [[source-fandom-sectors]], [[source-fandom-beacons]]).

- **Distress-marked here** (5): `CIVILIAN_ASTEROIDS_BEACON`, `DISTRESS_STATION_FIRE`,
  `ESCORT_BEACON`, `FRIENDLY_BEACON`, `TRAP_BEACON`.
- **Allocated but unmarked** (1): `REBEL_VS_FEDERATION` sits in `DISTRESS_BEACON_REBEL` but
  carries no distress tag, so it never shows the marker. Fandom describes this class as a
  mistake in the data.
- **Marked from outside the distress line**: *none*. This sector is the clean case — unlike the
  Engi sectors, which Fandom uses as its worked example of a sector showing more distress
  beacons than its distress count, nothing here leaks a distress marker in from another list.
  Checked against the shared fallback list too: none of its 19–20 members carries the tag.

Distress and store markers are only visible on beacons **adjacent** to you — one jump — so this
is a next-jump signal, not a sector plan. Quest markers, once planted, are visible from any
distance. (per [[source-fandom-beacons]])

## Stores

**1–2 guaranteed**, which matches the Fandom store table for the Rebel sector exactly
(per [[source-fandom-template-stores-number-of-stores-by-sectors]], [[source-sector-data-xml]]).
The line is filled second, so nothing can squeeze it out. Additional stores can come from:

- `ESCORT_BEACON` (Escort civilians FTL haywire) — carries a `<store/>` outcome and is in this
  sector's distress list;
- `STORE_REBELSIDE` (Large trade station) — present only in the AE `OVERRIDE_ITEMS` list, so
  whether it reaches this sector depends on the unresolved override question
  ([[concept-sector-event-allocation]]);
- `PIRATE_BRIBER` — via the shared fallback list, which is why Fandom marks it for this sector
  as filler/exit-beacon rather than as a sector event.

(per [[source-fandom-template-stores-additional-stores-from-events-by-sectors]],
[[source-fandom-stores-and-resources]], [[source-dlcevents]])

## The Fleet Clock

The baseline is one step of advance per jump. `modifyPursuit` is **signed and its name is
misleading**: negative delays the fleet, positive advances it. Seven events in this pool carry
one (per [[source-events-rebel]]; see [[concept-rebel-fleet-advance]]):

| Event | Effect | Where |
|---|---|---|
| `AUTO_WARNING` | +1 if the scout escapes | `HOSTILE_REBEL` |
| `SQUAT_WARNING` | +1 if the scout escapes | `HOSTILE_REBEL` |
| `NEBULA_AUTO_WARNING` | +1 if the scout escapes | `NEBULA_REBEL` |
| `NEBULA_REBEL_UNDETECTED` | +1 if it spots you and lives | `NEBULA_REBEL` |
| `CIVILIAN_ASTEROIDS_BEACON` | +1 | `DISTRESS_BEACON_REBEL` |
| `ALISON_DEFECTOR` | +1 | `NEUTRAL_REBEL` |
| `AUTO_DEFENSE_RADAR` | **−1** on the Hacking branch, or −1 / map reveal / nothing / +1 on the four-way plain roll | `NEUTRAL_REBEL` |

Fandom describes the escape case as **doubling** that turn's advance, which is the same thing
as `+1` on a baseline of one step (per [[source-fandom-auto-ship-warning]],
[[source-fandom-rebel-ship-warning]], [[source-fandom-rebel-fleet]]).

Modifiers that are not events in this pool but still apply here:

- **A nebula beacon in a non-nebula sector halves that turn's advance.** Rebel Controlled is not
  a nebula sector, so the uncontested 50% figure is what applies — the 1/5-versus-20% dispute
  recorded on [[source-fandom-rebel-fleet]] and [[source-xftl-sector-map]] concerns nebula
  *sectors* and does not bite here. `NEBULA_REBEL` rolls 0–5 and is placed before everything
  else, so the sector's structural brake is decided before any event is assigned.
- **Distraction Buoys** postpone the start-of-sector advance by 1 turn.
- **`REBEL_TRANSPORT` is the exception that looks like a rule.** It is a Rebel ship that flees
  and charges FTL exactly like the two scouts, but its escape does **not** advance the fleet —
  stated explicitly on both the event page and the Rebel Fleet page, and confirmed by the
  absence of any `modifyPursuit` in its tree.
  (per [[source-fandom-rebel-transport-ship]], [[source-fandom-rebel-fleet]],
  [[source-events-rebel]])

Net effect: the clock in this sector is close to one-way. Six of the seven pool events can only
push it forward; the one that can pull it back sits in the single line the map is most likely to
discard.

## Chains That Run Through It

- **Hidden Federation base** — three separate entry points here plant
  `HIDDEN_FEDERATION_BASE_LIST`: `CIVILIAN_ASTEROIDS_BEACON` and `REBEL_VS_FEDERATION` from the
  distress line, `FEDERATION_PLANET_SIGNAL` from the quest line (which can also plant
  `FEDERATION_BASE_ASSIST` directly). _Chain page not yet created._
- **The Rebel defector** — `ALISON_DEFECTOR` plants `ALISON_DEFECTOR_QUEST`.
  (see [[event-rebel-defector]])
- **The merchant's request** — `MERCHANT_REQUEST` plants one of `MERCHANT_DELIVER`,
  `MERCHANT_INVESTIGATE`, `MERCHANT_INVESTIGATE_DELIVER`.
- **Escort** — `ESCORT_BEACON` plants `QUEST_ESCORT_ARRIVE`.

Whether any of these markers actually lands is a separate question: a quest beacon must be
unvisited, outside a nebula, not the exit, not already a store/quest/distress beacon, not
overtaken by the fleet, and fewer jumps from you than the fleet is from it — otherwise the quest
is pushed to the next sector, or dropped outright from sector 7 on. In a sector whose defining
problem is the fleet's position, that last clause is the one that bites.
(per [[source-xftl-sector-map]], [[source-fandom-beacons]]; see
[[concept-quest-beacon-placement]])

## Factions & Ships
- [[entity-rebels]] — dominant faction. No alien ever serves on a Rebel ship, and the human
  supremacism shows up in the pool: every boarding party in this sector is human
  (`BOARDERS_SUN`, `BOARDERS_REBEL_SHIP`, `NEBULA_REBEL_BOARDING`, `FEDERATION_PLANET_SIGNAL`,
  `MERCHANT_REQUEST`, `ALISON_DEFECTOR`), and the one crew class the sector names as a reward is
  human. `ALISON_DEFECTOR` is the game's clearest hint that the Rebellion has members who find
  it repellent. (per [[source-fandom-the-rebellion]], [[source-events-rebel]])

## Strategy Notes
- The two scouts, `AUTO_WARNING` and `SQUAT_WARNING`, are the only fights in the sector where
  the *speed* of the kill is worth more than the safety of it: they charge FTL from the start
  and escaping costs you a jump of pursuit.
- `AUTO_DEFENSE_RADAR` behind Hacking is the only reliable −1 in the pool, and it costs a drone
  part. The plain approach is a 1-in-4 chance at the same result and a 1-in-4 chance at the
  opposite one.
- Routing through cloud beacons is the only brake that does not depend on a roll going your way,
  at the price of blind sensors while you are inside.
- Fandom's own guidance on fighting the Elite Fighter — disable its weapons and wait out the FTL
  charge rather than kill it — is *opinion*, offered without data. (per
  [[source-fandom-rebel-fleet]])

## Related
- [[sector-rebel-stronghold]] — the unique, sector-5-plus version of this sector
- [[sector-pirate-controlled-sector]] — the near-twin table
- [[concept-rebel-fleet-advance]], [[concept-sector-event-allocation]],
  [[concept-quest-beacon-placement]], [[concept-nebula-mechanics]],
  [[concept-anti-ship-battery]], [[concept-stores]]

## Open Questions
- [x] ~~Which events populate each list.~~ Answered — all nine lines are extracted into
  `sectors/data/rebel-controlled-sector.sector.json` (49 distinct events).
- [ ] Does the engine substitute `OVERRIDE_ITEMS` for `ITEMS` and `OVERRIDE_HOSTILE_REBEL` for
  `HOSTILE_REBEL` under Advanced Edition? Unresolved repo-wide
  ([[concept-sector-event-allocation]]). It decides whether `STORE_REBELSIDE` and `REBEL_PULSAR`
  belong to this sector at all.
- [ ] Is `unique="true"` scoped per sector or per run? 34 of the 49 events here are marked
  unique, so the answer materially changes the pool's shape ([[concept-event-uniqueness]]).
- [ ] What is the actual floor on beacons per map? Fandom says 19; no game file states one.
- [ ] Does the shared `NEUTRAL` fallback draw with the same "same event can repeat without
  limit unless unique" rule as an allocation list? No source in the repo says.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-events-rebel]] (per raw/gamedata/events_rebel.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlcevents]] (per raw/gamedata/dlcEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-sectors]] (per raw/wiki/sectors.md)
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md)
- [[source-fandom-the-rebellion]] (per raw/wiki/the-rebellion.md)
- [[source-fandom-beacons]] (per raw/wiki/beacons.md)
- [[source-fandom-environmental-hazards]] (per raw/wiki/environmental-hazards.md)
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md)
- [[source-fandom-template-stores-number-of-stores-by-sectors]] (per raw/wiki/template-stores-number-of-stores-by-sectors.md)
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]] (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md)
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt)
- [[source-fandom-the-mercenary]] (per raw/wiki/the-mercenary.md)
- [[source-fandom-rebel-transport-ship]] (per raw/wiki/rebel-transport-ship.md)
- [[source-fandom-auto-ship-warning]] (per raw/wiki/auto-ship-warning.md)
- [[source-fandom-rebel-ship-warning]] (per raw/wiki/rebel-ship-warning.md)
