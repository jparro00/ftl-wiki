---
id: event-slug-distress-piloting
type: event
event_name: SLUG_DISTRESS_PILOTING
sectors: []
beacon_type: unknown
hostile: false
blue_options: [pilot lvl 2, hacking system]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unreachable, orphan, blue-option, crew-reward, system-malfunction, combat]
---

# Slug allegiance demand — `SLUG_DISTRESS_PILOTING`

## Summary
A fully authored, fully polished Slug event — engines hacked, an ultimatum to swear
allegiance to the Slug Empire, four choices including two blue options and a free crew
member on one branch — that **is not reachable in this build**. It appears in no event list
and in no sector allocation.

## Trigger & Where It Appears
**None.** `SLUG_DISTRESS_PILOTING` is defined in `raw/gamedata/events_slug.xml` but:

- it is not loaded by any `<eventList>` in that file — including `DISTRESS_BEACON_SLUG`,
  where its name and shape suggest it belongs;
- it is referenced by no other file in `raw/gamedata/`;
- it appears in no `<sectorDescription>` in `sector_data.xml`;
- it is not even mentioned in the file's own header summary of distress events, which lists
  only `SLUG_DISTRESS_ROCK`, `SLUG_DISTRESS_QUESTION` and `SLUG_DISTRESS_MANTIS`.

([[source-events-slug]], [[source-sector-data-xml]])

The definition carries the dev note `<!-- changed to engines-->` — it was reworked from a
Piloting-system event into an Engines event at some point, and the choice labels still say
"(Improved Piloting)" while the mechanics operate on `engines`. It has **no Fandom page**,
which is consistent with it never appearing in play.

Tagged `unreachable`. Not tagged `cut-content`: no dev note says it was pulled, and it is
still `unique="true"` and fully wired internally.

## Text
> The distress signal originates from a tampered jump beacon. A Slug vessel jumps in and
> announces he has hacked your engines system. "Of course if you, as one of the few
> remaining ships in the Federation, swear allegiance to the Slug Empire you will be free
> to go."

(`event_SLUG_DISTRESS_PILOTING_text`, per [[source-text-events-xml]])

## Choices & Outcomes

Applied by the event body before any choice ([[source-events-slug]]):
`<status type="limit" target="player" system="engines" amount="1"/>` — Engines capped at
level 1 — and `<ship load="JELLY_STATUS_ENGINES" hostile="false"/>`. Note the event has an
`<environment type="nebula"/>` tag but **no** `<distressBeacon/>` tag, despite the intro
text describing a distress signal.

All four choices are `hidden="true"`.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Swear allegiance. | — | Rolls `SLUG_DISTRESS_PILOTING_SWEAR` — 2 entries, below. No fight. | see below |
| 2 | Never! | — | "The Slug is unimpressed by your bravado and moves in to attack. Get the shields up, you're a sitting duck with malfunctioning thrusters!" → `<ship hostile="true"/>` — **Engines stay capped at 1**. | 100% |
| 3 | **(Improved Piloting)** Override his control. | `req="pilot" lvl="2"` | "You quickly re-wire through a secondary control module." → `<ship hostile="true"/>` + `<status type="clear" target="player" system="engines" amount="100"/>` — Engines restored. | 100% |
| 4 | **(Hacking System)** Counter the remote hacking. | `req="hacking"` | `<ship hostile="true"/>` + Engines restored + `<status type="limit" target="player" system="hacking" amount="0"/>` — your Hacking offline instead. | 100% |

Choice 4 is marked `<!-- CHANGED - added -->` — an Advanced Edition addition
([[source-events-slug]]).

### `SLUG_DISTRESS_PILOTING_SWEAR` (choice 1)

| Entry | Text | Effect |
|---|---|---|
| 1 | "'Wow, I didn't think you'd go through with it...' … Strangely enough, they simply let you pass." | `<status type="clear" … system="engines" amount="100"/>` — Engines restored, nothing else |
| 2 | "'…let me introduce you to your new Slug Empire Overseer.' A bored-looking Slug teleports over." | `<crewMember amount="1" class="slug"/>` + Engines restored — **a free Slug crew member** |

Swearing allegiance has no recorded penalty anywhere in the data: no scrap cost, no flag,
no later consequence.

### The enemy — `JELLY_STATUS_ENGINES`

`SHIPS_JELLY`; `destroyed` `MED standard`, `deadCrew` `HIGH standard`, both clearing the
`engines` and `hacking` statuses. No surrender or escape block ([[source-events-ships]]).
The same ship is used by [[event-slug-repair-station]]'s EMP branch, which *is* reachable.

## Blue Options
- **Piloting level 2+** (`req="pilot" lvl="2"`) — label says Piloting, effect operates on
  Engines; a leftover from the `<!-- changed to engines-->` rework.
- **Hacking system** (`req="hacking"`) — restores Engines at the cost of your own Hacking.

## Rewards & Risks
Academic, since the event cannot occur:
- Choice 1 is free and half the time hands you a Slug crew member.
- Choices 2–4 fight a `JELLY_STATUS_ENGINES` for `MED`/`HIGH standard`; only choice 2
  fights with crippled Engines.

## Strategy Notes
Not applicable — you will not see this beacon. Listed here so the wiki does not silently
drop shipped content, and so a future build (or a mod) that re-enables it has a page.

## Related
- [[event-slug-repair-station]] — the reachable event that uses the same
  `JELLY_STATUS_ENGINES` ship and the same Engines handicap
- [[event-slug-hacker-choice]], [[event-slug-hacker-doors]], [[event-slug-hacker-oxygen]],
  [[event-slug-hacker-medical]] — the reachable Slug remote-hacking family
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — where it would have
  appeared

## Open Questions
- [ ] Was it intentionally removed from `DISTRESS_BEACON_SLUG`, or dropped by accident? It
      sits directly beside `SLUG_DISTRESS_TRICK` in the file, which *is* listed.
- [ ] Does any later FTL build or the AE hotfixes re-add it to a list?

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
