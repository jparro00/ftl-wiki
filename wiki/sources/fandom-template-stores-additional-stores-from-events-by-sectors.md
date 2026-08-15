---
id: source-fandom-template-stores-additional-stores-from-events-by-sectors
type: source
source_kind: wiki
raw: raw/wiki/template-stores-additional-stores-from-events-by-sectors.md
game_version: unknown
date: 2026-08-15
ingested: 2026-08-15
reliability: medium
tags: [sector, store, economy, routing]
---

# Fandom — Template: "Stores: additional stores from events, by sectors"

## Summary
The companion table to [[source-fandom-template-stores-number-of-stores-by-sectors]],
retrieved at revision 73435. It maps which store-spawning **events** can occur in which
sector — the stores that never show in the `sector_data.xml` `STORE` counts because they
arrive as event outcomes.

## Key Takeaways
- Two tiers are distinguished: **"store opening opportunity"** events (a store is offered)
  and **"store opening chance"** events (a store may result).
- Opportunity events: [[event-large-trade-station]] — available in every listed sector, and
  it can also occur as an *exit beacon* event in any sector; [[event-lone-lanius-ship]] —
  Abandoned only.
- Chance events by sector: [[event-escort-civilians]] (Civilian, Zoltan, Rock, Slug —
  and it can occur more than once per sector); [[event-escort-civilians]] FTL-haywire variant
  (Civilian, Pirate, Rebel, Rock, Slug, Uncharted); [[event-pirate-briber]] — **every**
  sector, as a filler or exit event, including Hidden Crystal Worlds and The Last Stand;
  [[event-settlement-mercenary-work]] (Civilian, Engi, Pirate, Rock);
  [[event-slug-drink]] and [[event-slug-transport-with-military-escort]] (Slug Nebulas only);
  [[event-zoltan-trade-hub]] (Zoltan only).
- Footnote: Hidden Crystal Worlds and The Last Stand have **no sector-specific** store-opening
  events — [[event-pirate-briber]] is the only route to an extra store there.
- Routing consequence: the store-poor sectors by guaranteed count (Pirate, Rebel, Mantis) are
  not equally poor in practice. Pirate is the best supplied of the three; Mantis is the worst.

> ⚠️ **CONTRADICTION:** this summary originally read *"Mantis carries none at all beyond the
> universal [[event-pirate-briber]]"*, and assigned the FTL-haywire escort row to
> "Civilian, Pirate, Rebel, Rock, Slug, Uncharted". Both are misreadings of the table above,
> caught while writing [[sector-mantis-controlled-sector]] and [[sector-mantis-homeworlds]].
>
> - The raw table marks **Mantis**, not Slug, on the FTL-haywire escort row, and marks
>   [[event-pirate-briber]] **grey** (filler/exit only) in the Mantis column.
> - The game files agree with the table, not the summary: `ESCORT_BEACON` is a member of
>   `DISTRESS_BEACON_MANTIS` and does open a store, while `PIRATE_BRIBER` appears in **none**
>   of either Mantis sector's lists.
>
> Corrected reading, betting on the game files: Mantis sectors carry **one** in-pool
> store-opening event, not zero — and it sits behind a *distress* marker rather than a store
> marker, which is the routing detail that actually matters. Pirate carries four
> ([[event-pirate-briber]], [[event-settlement-mercenary-work]], [[event-escort-civilians]]
> and its FTL-haywire variant), plus [[event-large-trade-station]] under AE.
>
> The store-poor conclusion survives either way; the mechanism stated for it did not.

## Events Covered
- [[event-large-trade-station]], [[event-lone-lanius-ship]], [[event-escort-civilians]],
  [[event-pirate-briber]], [[event-settlement-mercenary-work]], [[event-slug-drink]],
  [[event-slug-transport-with-military-escort]], [[event-zoltan-trade-hub]]

## Other Pages Touched
- Every page in `wiki/sectors/`, [[source-fandom-stores-and-resources]]

## Reliability Notes
`medium`. This is a hand-maintained cross-reference, not a transcription of a single file —
verifying it means checking each event's presence in each sector's event lists across
`events*.xml`. Not done in this pass; treat individual cells as claims to confirm.

## Contradictions Flagged
- **This page's own summary vs. the table it summarises** — see the flagged block under Key
  Takeaways. Two cells were misread (the Mantis column on the FTL-haywire escort row, and
  [[event-pirate-briber]]'s grey filler-only marking). Resolved against `raw/gamedata/`.
- **[[event-large-trade-station]] is version-sensitive.** The table lists it as an ordinary
  entry for several sectors, but `STORE_REBELSIDE` exists only in `OVERRIDE_ITEMS`, never in
  the base `ITEMS` list. With Advanced Edition content off it cannot come from the items line
  at all; with it on, it rides on the unresolved `OVERRIDE_` substitution question in
  [[concept-sector-event-allocation]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Template:Stores:_additional_stores_from_events,_by_sectors
- [[source-fandom-stores-and-resources]],
  [[source-fandom-template-stores-number-of-stores-by-sectors]], [[source-sector-data-xml]]
