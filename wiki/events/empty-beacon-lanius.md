---
id: event-empty-beacon-lanius
type: event
event_name: NOTHING_LANIUS
sectors: [[[sector-abandoned-sector]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [lanius, empty, flavor-only, no-choice, repeatable, advanced-edition]
---

# Empty beacon (Lanius) — `NOTHING_LANIUS`

## Summary
The Abandoned Sector's nothing-happens beacon. It prints one of six worldbuilding
vignettes about what the Lanius have already done to the region and ends. No choices, no
ship, no resources. Its only function beyond flavour is that it consumes a beacon slot —
1 to 2 of them per sector are reserved for it.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] (`LANIUS_SECTOR`) only.
- Allocation: `<event name="NOTHING_LANIUS" min="1" max="2"/>` — not drawn from a list, but
  allocated directly by the sector definition ([[source-sector-data-xml]], per
  `raw/gamedata/sector_data.xml`).
- No `unique` attribute → it repeats freely ([[source-dlcevents-anaerobic]];
  [[source-fandom-empty-beacon-lanius]] renders `unique=false`, `LRSmap=noship`).

> **AE-only, with a second-pass marker.** The whole of `dlcEvents_anaerobic.xml` is
> Advanced Edition content and `LANIUS_SECTOR` is an AE sector, so there is no vanilla form
> of this event. The `textList` does carry a `<!--DLC2-->` comment on its sixth entry
> ([[source-dlcevents-anaerobic]]) — but since the file itself only exists in AE, that
> marker denotes a **later AE content pass**, not a vanilla/AE boundary. Recorded here
> because rule-of-thumb "`<!--DLC-->` means AE" does not apply cleanly inside an AE-only
> file. `dlcEventsOverwrite.xml` defines no `OVERRIDE_NOTHING_LANIUS`
> ([[source-dlceventsoverwrite]]).

## Text
`[varies: textList NOTHING_LANIUS]` — **8** `<text>` entries drawing on **6** distinct
strings. `text_NOTHING_LANIUS_1` and `_2` each appear **twice**; `_3`, `_4`, `_5`, `_6`
appear once ([[source-dlcevents-anaerobic]]). So, *assuming uniform selection across list
entries*:

| String | Gist | Share |
|---|---|---|
| `_1` | A skirmish site with no debris left — "sucked dry by the Lanius" | **2/8** |
| `_2` | No ships or settlements; you cannot tell if the area was ever inhabited | **2/8** |
| `_3` | Refugees whose FTL drives the Lanius hacked, then left alone | 1/8 |
| `_4` | A Lanius ship firing on its own companion over salvage rights | 1/8 |
| `_5` | A settlement that drove off a Lanius fleet with ASB warning shots | 1/8 |
| `_6` | A human ship fleeing a "Humanitis" purity cult (`<!--DLC2-->`) | 1/8 |

The trailing `_1` / `_2` repeats sit after the `_6` line and match the "NEEDS MORE" padding
pattern used elsewhere in the AE event files — i.e. they read as filler to keep list length
up rather than as intentional weighting. All six strings are transcribed verbatim on
[[source-fandom-empty-beacon-lanius]] and live at `text_NOTHING_LANIUS_1` … `_6` in
`raw/gamedata/text_events.xml` ([[source-text-events-xml]]).

Representative:

> You pass a civilian ship that warns of the nearby Lanius. "One of them attacked a civilian
> transport and started to melt their fracking hull. But then the weirdest thing happened...
> another metal ship actually fired on its companion until it backed off." Apparently there
> are disagreements among the Lanius about what should be salvaged.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices; continue)_ | — | Nothing happens. | 100% |

The `<event name="NOTHING_LANIUS">` element contains a single `<text load=…/>` child and
nothing else ([[source-dlcevents-anaerobic]]).

## Rewards & Risks
None of either. This beacon cannot give or cost you anything.

## Strategy Notes
- Mechanically identical to every other faction's empty beacon: it costs a jump and one
  tick of Rebel fleet advance, nothing more.
- The 1–2 guaranteed empty beacons are a small mercy in a sector that also guarantees 5–6
  hostile plus 1–2 hazard-hostile beacons ([[source-sector-data-xml]]).
- Note the `_6` variant is a piece of continuity with the Humanitis cult events elsewhere
  in the AE files, not a hint that anything happens here.

## Related
- [[event-start-beacon-lanius]] — the sector's other no-op beacon
- [[event-store-lanius]] — the sector's guaranteed store
- [[event-empty-beacon-rock]], [[event-empty-beacon-slug]], [[event-empty-beacon-engi]] —
  the same slot in other sectors
- [[sector-abandoned-sector]], [[entity-lanius]]

## Open Questions
- [ ] Whether the doubled `_1` / `_2` entries are intentional weighting or list padding —
      the file gives no comment either way.
- [ ] What the `<!--DLC2-->` marker denotes precisely across the AE files (a second content
      pass is the reading here, but no source states it).

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-empty-beacon-lanius]] (per raw/wiki/empty-beacon-lanius.md)
