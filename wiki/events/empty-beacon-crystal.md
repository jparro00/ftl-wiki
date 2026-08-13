---
id: event-empty-beacon-crystal
type: event
event_name: NOTHING_CRYSTAL
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [empty, flavor, no-choices]
---

# Empty beacon (Crystal) — `NOTHING_CRYSTAL`

## Summary
The sector's do-nothing beacon: flavour text about Crystalline society and then nothing.
Its only mechanical value is that it burns a jump safely — which in
[[sector-hidden-crystal-worlds]], where 6–10 of the beacons are forced fights, is not
worthless.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Allocation: `NOTHING_CRYSTAL` is placed exactly **twice** per sector (`min=2 max=2`)
  ([[source-sector-data-xml]])
- Beacon: shows **no ship** on Long-Range Scanners
  ([[source-fandom-empty-beacon-crystal]])

## Text
The text **varies** — `<text load="NOTHING_CRYSTAL"/>` draws from a 12-slot text list
built from 7 distinct strings, with `text_NOTHING_CRYSTAL_2` through `_6` each appearing
twice and `_1`/`_7` (near-identical wordings of the same scene) once each
([[source-events-xml]]). The distinct variants ([[source-text-events-xml]]):

> As soon as you arrive, all of the ships docked at a nearby station scatter and jump
> while the station itself uses some form of cloak technology to disappear. They mustn't
> like outsiders here...

> No ships are in range, so you take the time to scan the area. It seems like every planet
> you've seen so far shows signs of highly developed habitation without overpopulation.
> They must have a very structured and well regulated society.

> There appears to be no one living near this node, a rare sight in this highly developed
> sector.

> You arrive near a civilian settlement. It looks like their homes, ships and stations all
> rely heavily on an intriguing crystalline material. You wonder how they are able to
> create so much of this substance, as yet undiscovered in the rest of the galaxy.

> A few merchant ships pass nearby but they are either ignoring your hails or their
> computer isn't designed to work through the same frequencies...

> A number of civilian ships seem to be evacuating a small colony. One ship messages you
> before jumping away, "Damn you aliens! This is why we closed that Long-range Beacon in
> the first place!"

(The seventh string, `text_NOTHING_CRYSTAL_7`, differs from `_1` only by "jump away"
vs "jump".)

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _none — the event has no choice nodes and no effects_ | — | Nothing happens | 100% |

## Blue Options
- None.

## Rewards & Risks
- Neither. No `autoReward`, no `item_modify`, no `ship`, no `damage`.

## Strategy Notes
- Two guaranteed safe beacons per sector. Worth knowing when you are counting jumps
  against the Rebel fleet, since they cost you a jump and give nothing back.
  *(Opinion — no source states it.)*

## Related
- [[sector-hidden-crystal-worlds]]
- [[event-store-crystal]] — the other reliably non-hostile beacon type here
- [[concept-empty-beacons]]

## Open Questions
- [ ] Whether the duplicated entries in the text list are deliberate weighting or a
      copy-paste artefact (the same doubled-block pattern appears in `STORE_CRYSTAL` and
      `CRYSTAL_FIGHT`).

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-empty-beacon-crystal]] (per raw/wiki/empty-beacon-crystal.md)
