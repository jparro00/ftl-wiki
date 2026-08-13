---
id: source-fandom-intelligent-ponies
type: source
source_kind: wiki
raw: raw/wiki/intelligent-ponies.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [slug, crew-reward, crew-loss-risk, clone-bay, blue-option]
---

# Fandom — "Intelligent ponies"

## Summary
The community wiki page for the event the game files call `DONOR_PONY`. Retrieved via the
MediaWiki API at revision 74078. Documents the full three-level choice tree, including the
Slug blue option that turns the event into a guaranteed Engi crew member.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'DONOR_PONY' in the
  datafiles."* This is the join key.
- Sector availability: Slug Controlled Nebula, Slug Home Nebula, plus
  `alsooccur=exitandfiller`. `LRSmap=noship`.
- Renders the blue option as **Slugman Crew**, matching `req="slug"`.
- Spells out the Clone Bay interaction on the "sell them" branch: `<clone>true</clone>`
  means the trampled crew member **is** revived — the opposite of the Clone Bay outcome in
  [[event-plagued-station]].
- Categorised `Random_Events`, `Unique_Events`, `Filler_Events`, `Donor Events`,
  `Crew loss risk`, `Clone Bay revival`, `Crew reward opportunity`.

## Events Covered
- [[event-intelligent-ponies]]

## Other Pages Touched
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[entity-slugs]],
  [[entity-engi]], [[item-clone-bay]]

## Reliability Notes
`medium`. No game version stated. Gives no odds for either two-member outcome pool, which
matches the files.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** one word in the peaceful-contact success text.
> Fandom: *"Eventually, **the creatures** guide you to an old Engi ship's crash site."*
> Game files: *"Eventually, **they** guide you to an old Engi ship's crash site."*
> ([[source-text-events-xml]], `event_DONOR_PONY_PEACE_1_text`).
> Recorded on [[event-intelligent-ponies]]. Cosmetic; game files trusted.

## Links
- Source URL: https://ftl.fandom.com/wiki/Intelligent_ponies
- [[source-events-xml]], [[source-text-events-xml]]
