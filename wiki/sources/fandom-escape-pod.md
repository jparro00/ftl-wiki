---
id: source-fandom-escape-pod
type: source
source_kind: wiki
raw: raw/wiki/escape-pod.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [mantis, crew-reward-chance, crew-loss-risk, contradiction]
---

# Fandom — "Escape pod"

## Summary
The community wiki page for `MANTIS_CREW`. Retrieved via the MediaWiki API at revision
74053. Fully enumerates the three-outcome gamble behind "Pry it open", including the
Clone Bay revival branch.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'MANTIS_CREW' in the datafiles."*
- Locations: Mantis Controlled Sector, Mantis Homeworlds; `unique=true`, `LRSmap=noship`.
- Enumerates all three `MANTIS_CREW_LIST` outcomes and states the crew-loss branch
  explicitly: *"1 mantis boarder beams aboard your ship and you lose a crewmember."*
- Documents the **Clone Bay revival** as a nested outcome, matching the
  `<removeCrew><clone>true</clone></removeCrew>` structure in the game files. Fandom
  presents it as a blue-option-styled branch; in the files it is an automatic flag, not a
  player choice.
- Claims outcome (b) gives a **Mantis crewmember** — this is the contradiction below.
- Categorised `Boarding risk`, `Crew loss risk`, `Clone Bay revival`,
  `Crew reward chance`.
- Gives **no odds** for the three-way split, matching the files' silence.

## Events Covered
- [[event-escape-pod]]

## Other Pages Touched
- [[item-clone-bay]], [[entity-mantis]], [[sector-mantis-controlled-sector]],
  [[sector-mantis-homeworlds]]

## Reliability Notes
`medium`. Version unstated. On the Mantis-crewmember question it may actually be the
*better* source, because it describes observed behaviour where the game file carries only
a stale developer comment — see below.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** does `MANTIS_CREW_LIST` entry 2 give a Mantis or a Human?
> - Fandom: *"You receive a Mantis crewmember."*
> - Game files: `<crewMember amount="1" class="mantis"/>` with the inline developer
>   comment `NOTE - Doesnt work yet -gives human` ([[source-events-xml]]).
>
> Unresolved — the comment is undated and may predate a fix. Recorded on
> [[event-escape-pod]]. Needs an observed run to settle, not another file.

## Links
- Source URL: https://ftl.fandom.com/wiki/Escape_pod
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
