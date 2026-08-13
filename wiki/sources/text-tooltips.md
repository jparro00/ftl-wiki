---
id: source-text-tooltips
type: source
source_kind: gamedata
raw: raw/gamedata/text_tooltips.xml
game_version: ae
ingested: 2026-08-09
reliability: high
tags: [partial-ingest]
---

# text_tooltips.xml

## Summary
The in-game hover tooltips: system descriptions, UI controls, and — most usefully for this
wiki — the **beacon hazard tooltips** that state what a nebula, plasma storm, pulsar,
asteroid field, sun or anti-ship battery actually does to you.

64 `<text>` entries, 7 KB.

## Key Takeaways
- Extracted from the user's installed 1.6.x Advanced Edition build; see
  `raw/gamedata/_PROVENANCE.md`.
- **This file is where several mechanics are stated in the game's own words** and nowhere
  else in `raw/gamedata/`:
  - `tooltip_nebula` — *"You're inside a nebula. Your sensors will not function, but the
    Rebel fleet will advance more slowly towards you."*
  - `tooltip_storm` — *"This section of the nebula is experiencing a **plasma storm**. Your
    main reactor can only function at half capacity."*
  - `tooltip_pulsar` — *"…Periodic waves of electromagnetic energy will disrupt your systems."*
  - `tooltip_sun` — *"…Solar flares will light the ship on fire. Shields will reduce the effect."*
  - `tooltip_asteroids` — *"…Periodically asteroids will strike your ship."*
  - `tooltip_PDS_FLEET` / `_PLAYER` / `_ENEMY` / `_ALL` — who an anti-ship battery targets.
- It is the counterpart to [[source-text-misc]]'s star-map strings: `text_misc.xml` says what
  a beacon looks like from the map, this file says what it does once you are in it.
- Reliability `high`: the game's own data, outranking the community wiki wherever the two
  disagree.

## Events Covered
None directly — this file contains no event prose. It is cited by concept pages for the
mechanics behind environment tags.

## Other Pages Touched
- [[concept-nebula-mechanics]]
- [[concept-rebel-fleet-advance]]

## Contradictions Flagged
- `tooltip_storm` calls the hazard a **plasma storm**, while `text_misc.xml`'s star-map
  string for the same beacon is `map_ion_loc`, *"This section of the nebula is experiencing
  an **ion storm**."* Same environment (`<environment type="storm"/>`), two names, both
  first-party. Recorded on [[concept-nebula-mechanics]].

## Links
- [[source-text-misc]] — the star-map and notification strings
- [[source-text-blueprints]] — system and augment descriptions
