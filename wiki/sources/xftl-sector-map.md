---
id: source-xftl-sector-map
type: source
source_kind: research
raw: raw/modding/2026-08-15-xftl-sector-map.txt
game_version: unknown
date: 2026-08-15
ingested: 2026-08-15
reliability: medium
tags: [sector, map-generation, beacon, quest-marker, rebel-fleet, sector-choice, engine-internals, reverse-engineering, external-research]
---

# xftl — reverse-engineered sector map and beacon map generation

## Summary
A technical document from **xftl** (znixian), a reverse-engineering effort against the
compiled FTL binary, linked twice from the Fandom `Sectors` page as its citation for beacon
counts and sector colour odds. It names the actual engine methods — `StarMap::GenerateSectorMap`,
`AddSectorColumn`, `GenerateMap`, `PopulateGrid`, `ConnectLocations`, `AddQuest`,
`TurnIntoFleetLocation` — and describes each. **This is the only source in the repo that
describes the sector graph and the beacon layout algorithm at all**, and it answers questions
`sector_data.xml` structurally cannot.

## Key Takeaways

### Sector graph — how sector choice works
- `GenerateSectorMap` fixes the first and last sectors and calls `AddSectorColumn` **six
  times** for the middle.
- Each column holds a random **2–4 sectors**, re-rolled so it never matches the previous
  column's count. **The first column always has exactly two** — "presumably to avoid giving
  the player more than two options."
- Linking depends on the count transition: 4→2 links new-1 to old-1/2 and new-2 to old-3/4;
  2→4 links new-1/2 to old-1 and new-3/4 to old-2; all other transitions walk each new sector
  to its index-peer in the previous column, chaining as it goes, so that no neighbour links
  overlap.
- **Sector type roll**: 20% nebula; otherwise an independent 60% friendly / 40% hostile —
  i.e. **48% friendly, 32% hostile, 20% nebula**, in `StarMap::GetRandomSectorChoice`. A
  fourth value (>2) exists in `RenderSectorMap` and draws a grey dot; the author speculates
  it relates to the Crystal homeworlds or is cut content.

### Beacon map — layout, then allocation
- `GenerateMap` calls `PopulateGrid` once per cell of a **6×4 grid** (the author cites a
  Subset Games tweet showing the same grid).
- **20% chance a cell holds no beacon**, with a guard: if at least one empty cell already
  exists and empties are at least 20% of the cells placed so far, the cell is filled anyway.
  So the beacon count is bounded, not fixed.
- Each cell is a **110×110px area**; the beacon sits randomly inside it with a 10px margin.
  Y is clamped to ≤415, and in the two top-right cells to ≥30 (to clear the "next sector"
  button).
- A beacon then connects to **all beacons in adjacent cells within 165px** (`ConnectLocations`).
- **Layout happens first, allocation second** — `PopulateGrid` places and connects beacons
  with no reference to events; events are assigned afterwards.
- **Exit beacon placement**: random Y, X randomly in the **two right-most columns** (zero-indexed
  {4,5}), with the constraint that the start→exit distance is **at least five jumps**. The game
  retries up to **16 times** and then gives up on the constraint.
- **The Last Stand** reuses this logic for the Federation Base: X from {2,3} on easy/normal and
  {3,4} on hard; path length 4 jumps on easy/normal, 5–6 on hard (with a note that the code's
  constants are exclusive, so "normal must be between 3–5 jumps, but both min and max are
  exclusive"). The Flagship then spawns in one of the two right-most columns, with the
  flagship→base path required to be 4–6 jumps inclusive of both endpoints.

### Quest markers — `StarMap::AddQuest`
The candidate filter, in full. A beacon is eligible only if it:
- has **not been visited**;
- is **not a nebula beacon**;
- is **not the exit beacon**;
- has **not been overtaken by the Rebel fleet**;
- does **not already have a quest**;
- is **not a store**;
- is **not a distress beacon**;
- is **not the player's current beacon**;
- and has a **path** from the player.

Then: "unless the 'force' argument is set, the number of jumps away from the player must be
**less than the number of jumps until this quest is overtaken by the rebels**." `force` is true
for quests carried over from a previous sector. If no beacon qualifies, the quest is **delayed
to the next sector — except in sector 7 or later, where it is not delayed** (i.e. dropped).

### Rebel fleet — the pursuit is a moving circle
- Internally the "danger zone": a **circle of radius 767**, centre Y random in 50–300, centre X
  starting at **−959**.
- X advances **64px per jump from a normal beacon, 51px from a nebula beacon in a nebula sector,
  and 32px from a nebula beacon in a normal sector.**
- Overtaking swaps the beacon's event via `TurnIntoFleetLocation` to one of `FLEET_EASY`,
  `FLEET_EASY_DLC`, `FLEET_EASY_NEBULA`, `FLEET_EASY_BEACON` (exit on easy) or
  `FLEET_EASY_BEACON_DLC` (exit on normal/hard — "not tied to AE!").
- "There is no separate nebula exit beacon event. Instead, the nebula effect is applied to
  `FLEET_EASY_BEACON[_DLC]`, overwriting the ASB/PDS hazard."

## Events Covered
- `FLEET_EASY`, `FLEET_EASY_DLC`, `FLEET_EASY_NEBULA`, `FLEET_EASY_BEACON`,
  `FLEET_EASY_BEACON_DLC` — named as the fleet-overtake replacements.

## Other Pages Touched
- [[concept-quest-beacon-placement]], [[concept-sector-event-allocation]],
  [[concept-rebel-fleet-advance]], [[concept-start-beacons]], [[sector-the-last-stand]],
  every page in `wiki/sectors/`

## Reliability Notes
`medium`, and the ceiling for this kind of claim. It is read out of the compiled binary, so it
outranks the community wiki on mechanism — but it is one person's disassembly notes, undated,
unversioned (no upstream revision id: GitLab raw URLs on `master` return none), against an
unstated build, and hedged in places by the author himself ("seems to involve", "at least in
the build I'm looking at", "annoying to read due to inlining"). Not a game file; do not promote
to `high`.

## Contradictions Flagged
> ⚠️ **CONTRADICTION — nebula pursuit reduction.** This source gives the advance in pixels per
> jump: **64 normal, 32 nebula-beacon-in-normal-sector, 51 nebula-beacon-in-nebula-sector**.
> That is a **50% reduction** and a **~20% reduction (51/64 ≈ 0.797)** respectively — which
> **resolves the wording clash** between [[source-fandom-rebel-fleet]] ("by 1/5 of regular
> beacon advance rate", read as reduce-*to*-20%) and [[source-fandom-environmental-hazards]] /
> [[source-fandom-sectors]] ("by 20%", reduce-*by*-20%). The Environmental Hazards phrasing is
> the correct one. Recording all three; the Rebel Fleet page's phrasing should be treated as
> misleading, not deleted.

> ⚠️ **CONTRADICTION — quest marker exclusions.** [[source-fandom-beacons]] says a quest marker
> overwrites any event "unless it is a store, exit, or another quest marker", and that markers
> "cannot appear in nebula area". `AddQuest` gives a longer and different filter: it also
> excludes **visited** beacons, **fleet-overtaken** beacons, **distress** beacons and the
> **player's current** beacon, and the nebula exclusion is **per beacon**, not per area. Fandom
> carries `@to-do: test and verify` comments on exactly this claim. The engine list should be
> preferred; [[concept-quest-beacon-placement]] currently cites only the Fandom version.

> ⚠️ **CONTRADICTION — "not many jumps left".** [[concept-quest-beacon-placement]] lists the
> threshold as an open question with no source. `AddQuest` defines it exactly: the candidate
> must be **fewer jumps away than the number of jumps before the Rebels take it.**

> ⚠️ **PARTIAL CONTRADICTION — sector-7 cancellation.** [[source-fandom-beacons]] and
> [[source-fandom-random-events]] say a quest triggered in sector 7 is cancelled because sector 8
> allows no quests. `AddQuest` says the *delay* does not happen "in sector 7 or later", which is
> the same outcome by a different mechanism — the quest is not cancelled by a sector-8 rule, it
> simply is never carried forward.

## Links
- Source URL: https://gitlab.com/znixian/xftl/-/blob/master/doc/sector-map
- [[source-fandom-sectors]], [[source-fandom-beacons]], [[source-fandom-rebel-fleet]],
  [[source-fandom-environmental-hazards]], [[source-sector-data-xml]],
  [[source-xftl-oxygen-mechanics]], [[source-xftl-stores]]
