---
id: source-fandom-refueling-platform
type: source
source_kind: wiki
raw: raw/wiki/refueling-platform.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [fuel, filler, boarding-risk, blue-option, hull-damage, fire]
---

# Fandom — "Refueling platform"

## Summary
The community wiki page for `FUELING_STATION`. Retrieved via the MediaWiki API at
revision 74855. Transcribes both top-level branches and all five docking scenarios, and
supplies the hull-damage figures the game files leave implicit.

## Key Takeaways
- **Names the in-game id explicitly:** *"This event is called 'FUELING_STATION' in the
  datafiles."* (in a Trivia rather than Notes section).
- Locations template: Abandoned Sector, Engi Controlled Sector, Engi Homeworlds, Slug
  Controlled Nebula, Slug Home Nebula, `alsooccur=exitandfiller`, `unique=true`,
  Long-Range Scanners `noship`. The Abandoned Sector entry is not an explicit
  `sector_data.xml` allocation — that sector allocates only `STORE`, so the rest of its
  beacons fall through to the hardcoded neutral filler list that carries this event.
- **Supplies what the game files do not:** it reads each `<damage amount="3"
  system="engines"/>` as *3 hull damage plus 3 damage to engines*, and the `effect="fire"`
  variant as additionally starting 1–2 fires. The XML states only the single tag.
- Marks the Blast Doors option as **level 2+**, matching `req="doors" lvl="2"`.
- Uses `{{DuplicateEvent|2}}` on the "Ignore the platform" nothing-happens outcome —
  independently observing the two empty entries in `FUELING_STATION_IGNORE`.
- Gives `PIRATE` surrender/escape via template: surrender+escape, 50%/30–40/3–4 and
  50%/20–40/2–4.
- Categorised `Fuel reward chance`, `Fights with Default Rewards`, `Hull damage risk`,
  `Boarding risk`, `System damage risk`, `Fire risk`, `Fuel loss risk`.

## Events Covered
- [[event-refueling-platform]]

## Other Pages Touched
- [[entity-pirates]], [[item-doors]], [[sector-engi-controlled-sector]],
  [[sector-engi-homeworlds]], [[sector-slug-controlled-nebula]],
  [[sector-slug-home-nebula]]

## Reliability Notes
`medium`. States no game version; the event is Advanced Edition content per its position
in `newEvents.xml`. The hull-damage figures are engine behaviour the wiki infers, not
text any file states — treat them as the wiki's reading, not as datamined values.

## Contradictions Flagged
One transcription slip: the wiki renders the malfunctioning-station explosion as *"losing
your precious fuel"* where `text_events.xml` has *"losing you precious fuel"*. Recorded on
[[event-refueling-platform]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Refueling_platform
- [[source-newevents]], [[source-events-engi]], [[source-dlceventsoverwrite]],
  [[source-text-events-xml]], [[source-sector-data-xml]], [[source-events-ships]]
