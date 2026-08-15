---
id: source-xftl-oxygen-mechanics
type: source
source_kind: research
raw: raw/modding/2026-08-14-xftl-oxygen-mechanics.txt
game_version: unknown
date: 2026-08-14
ingested: 2026-08-14
reliability: medium
tags: [oxygen, venting, breach, airlock, engine-internals, reverse-engineering, external-research]
---

# xftl — reverse-engineered oxygen mechanics

## Summary
A short technical document from **xftl** (znixian), a reverse-engineering / reimplementation
effort against the FTL binary. It describes the oxygen model by naming the actual engine
methods — `OxygenSystem::ComputeAirLoss`, `OxygenSystem::RedistributeOxygen`,
`OxygenSystem::ModifyRoomOxygen`, `ShipGraph::ConnectivityDFS` — and giving their constants.
It was found via the See-also on [[source-fandom-oxygen]] and fetched in the same pass.

This is the closest thing this repo holds to "the game files say so" for behaviour that is
**not in any XML**: it is a reading of compiled code, one step removed.

## Key Takeaways

- **Drain with Oxygen off: 1.2%/sec.** Refill is `1.2% × {1, 4, 7}` for levels 1/2/3 —
  *"NOT the 1,3,6 multipliers listed in the UI"*. Confirms [[source-fandom-oxygen]] on both.
- **`ComputeAirLoss` — the venting constants.** Open airlock door: **16%/sec each**. Hull
  breach: **8%/sec each**. Anaerobic crew (Lanius) are *"equivalent"* to a breach — the engine
  runs them through the same path, which upgrades Fandom's "same rate" claim from an
  observation to a structural fact.
- **Air loss is not confined to the breached room.** It propagates to every connected room at
  `0.75^distance`, distance measured by `ShipGraph::ConnectivityDFS` (breach room = 0). So an
  open door to a breach costs the neighbour 75% of the breach's drain.
- **Fires bypass this path entirely** — 0.96%/sec per fire, applied to their own room via
  `ModifyRoomOxygen`. Corroborates [[source-fandom-oxygen]]'s figure.
- **`RedistributeOxygen` — the spread model.** Rooms joined by open doors form a *chunk*; each
  room moves **8% of its difference from the chunk average, per second**. Critically,
  **distance within a chunk is irrelevant** — air spreads down a long corridor exactly as fast
  as between neighbours.
- **The asymmetry that drives all the tactics:** redistribution ignores distance, but breach
  loss decays with distance. Opening a door near a breach therefore costs more than it gains,
  while a long snaking path of open rooms *far* from the breach feeds it for free.
- **A measured example:** on the Kestrel with level-1 Oxygen, venting the teleporter room takes
  **3.5s through two airlocks versus 5.2s through one** — the only timed measurement in any
  source we hold.
- Explains a specific edge case: level-3 Oxygen sustains one Lanius room, but two such rooms
  with the connecting door open breaks, *"since they both vent each other's rooms"*.

## Events Covered
None — engine internals, no event content.

## Other Pages Touched
- [[concept-oxygen-and-suffocation]] — the page this source primarily created
- [[item-oxygen-system]], [[item-doors]], [[item-lanius-crew]]
- [[entity-lanius]]

## Reliability Notes
`medium`, and the reasoning matters. Per `CLAUDE.md` §2.7 a `research` source is *"never
`high`: it cites sources this repo does not hold"* — here the uncited source is the compiled
binary itself, which we cannot inspect to check the work. Weighed against that: it names
specific mangled-looking method symbols and gives self-consistent constants that independently
reproduce Fandom's derived table (1.2 × 4 = 4.8, 1.2 × 7 = 8.4). Fabricating that coincidence
would be more effort than measuring it.

**No upstream revision id.** GitLab raw URLs pinned to `master` return no version, so this
capture cannot be pinned the way a Fandom revision can. Re-fetch and diff to detect drift.

`game_version: unknown` — the doc never states which build was disassembled. The presence of
anaerobic crew means it is **at least** AE-era, but that is inference, not a statement.

## Contradictions Flagged
None against the game files — this source touches nothing that `raw/gamedata/` covers.

Against [[source-fandom-oxygen]] it **corrects one claim** (an airlock drains at 16%/sec, not
*"instantly"*) and **confirms** the drain rate, the refill multipliers, the UI's error, the
fire rate, and the breach/Lanius equivalence. The contradiction is recorded in full on
[[source-fandom-oxygen]] and [[concept-oxygen-and-suffocation]].

It is **silent on crew suffocation damage** — the 6.4 HP/sec figure gets no support here.

## Links
- Source URL: https://gitlab.com/znixian/xftl/-/blob/master/doc/oxygen
- Project root: https://gitlab.com/znixian/xftl
- [[source-fandom-oxygen]] — the page that cites it
- [[source-modding-research]] — the other `research` source in `raw/modding/`
