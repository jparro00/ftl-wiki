---
id: source-fandom-auto-ship-carrying-shield-virus
type: source
source_kind: wiki
raw: raw/wiki/auto-ship-carrying-shield-virus.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, auto-ship, blue-option, system-malfunction, contradiction]
---

# Fandom — "Auto-ship carrying shield virus"

## Summary
The community wiki page for `AUTO_HACKER`. Retrieved via the MediaWiki API at revision
74288. Short, and it disagrees with the game files on two substantive points.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'AUTO_HACKER' in the datafiles."*
- Locations: **Civilian Sector only**. `LRSmap=ship`, `unique=true`. The event sits in
  `HOSTILE1` / `OVERRIDE_HOSTILE1`, which [[sector-federation-space]] also draws on.
- Transcribes the intro text as *"…has **deployed a virus and disrupted your shield
  system**."* — the current game file reads *"…has **used a local satellite to deploy a
  virus to disrupt your Shields System**."*
- Documents the debuff correctly and usefully: shields **halved, rounding down against
  you** — a gameplay detail the `<status type="divide" … amount="2"/>` tag does not spell
  out.
- Blue option: *"(Hacking System) Counter the remote hacking"*, after which you *"Fight an
  **Auto-ship** with your Hacking offline"* for medium scrap with resources. The game file
  instead loads `<ship load="JELLY" hostile="true"/>` — a **Slug ship** with surrender and
  escape branches.
- Categorised `Random_Events`, `Unique_Events`, `System malfunction hazard`,
  `Auto-ship fights`.

## Events Covered
- [[event-auto-ship-carrying-shield-virus]]

## Other Pages Touched
- [[item-hacking]], [[item-shields]], [[concept-rebel-fleet-advance]], [[entity-slugs]]

## Reliability Notes
`medium`. Version unstated, and this is a page where that matters: the event's Hacking
choice carries a `<!-- CHANGED - added -->` dev comment in `events_rebel.xml`, so the AE
edit is documented in the file but its consequences are not reflected here.

## Contradictions Flagged
- **Intro wording** — file mentions a local satellite; the wiki does not.
- **Enemy on the blue branch** — file says `JELLY` (Slug ship), the wiki says Auto-ship.
- **Sector reach** — Civilian Sector only vs the generic hostile pools.

All three recorded on [[event-auto-ship-carrying-shield-virus]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Auto-ship_carrying_shield_virus
- [[source-events-rebel]], [[source-events-ships]], [[source-text-events-xml]]
