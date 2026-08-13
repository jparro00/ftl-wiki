---
id: source-fandom-pirate-engine-hacker
type: source
source_kind: wiki
raw: raw/wiki/pirate-engine-hacker.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [pirate, system-debuff, blue-option, fuel-reward]
---

# Fandom — "Pirate engine hacker"

## Summary
Community wiki page for `PIRATE_NO_ESCAPE`, retrieved via the MediaWiki API at revision
74290. Documents the engine lockdown, the Hacking blue option, and the fuel-flavoured
rewards.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'PIRATE_NO_ESCAPE' in the datafiles."*
- Locations: Civilian Sector, Engi Controlled Sector, Engi Homeworlds, Pirate Controlled
  Sector; `LRSmap=ship`, `unique=true` — matching `unique="true"` in the files.
- Confirms the two outcomes of choice 1 and choice 2: **Engines limited to level 1** vs
  **Hacking offline**, which matches the two `<status type="limit">` tags exactly.
- **Confirms the ship neither surrenders nor escapes** — matching
  `<ship name="PIRATE_NO_ESCAPE">`, which has no `<surrender>` or `<escape>` element.
- Two claims not in the game files:
  - reads the `MED` `fuel` reward as **2–4 fuel** (tooltip, no source given);
  - *"Level 1 Engines system is not affected by the enemy hack, hence the crew skill can
    be trained."*

## Events Covered
- [[event-pirate-engine-hacker]]

## Other Pages Touched
- [[item-hacking]], [[entity-pirates]], [[sector-pirate-controlled-sector]]

## Reliability Notes
`medium`. No version stated. Its intro text is a slightly different wording from the
shipped `text_events.xml` string — possibly pre-AE.

## Contradictions Flagged
- **Intro text wording.** Fandom: *"they have tried to shut down **our** engines. Your crew
  manages to keep them operational."* Game files: *"…**your** engines. Your crew manages to
  keep them **barely** operational."* Recorded on [[event-pirate-engine-hacker]]; game
  files trusted.
- Sector list omits [[sector-federation-space]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Pirate_engine_hacker
- [[source-events-pirate]], [[source-events-ships]], [[source-text-events-xml]]
