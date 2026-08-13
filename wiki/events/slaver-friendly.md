---
id: event-slaver-friendly
type: event
event_name: FRIENDLY_SLAVER
sectors: [[[sector-abandoned-sector]], [[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: any
hostile: false
blue_options: [teleporter lvl 2]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 10
tags: [pirate, slaver, crew-purchase, moral-choice, optional-fight, blue-option, unique]
---

# Slaver (friendly) — `FRIENDLY_SLAVER`

## Summary
A slave trader offers to sell you a "laborer". Buying is the cheapest reliable crew member
in the game — 25–45 scrap, with the species and skills shown before you commit. You can
also ignore him, attack him, or, with a Teleporter, board and free the slaves: 2/3 of the
time that gets you a crew member *and* the fight. Same ship as
[[event-slaver-hostile]], so beating it has its own crew-reward tree on top.

## Trigger & Where It Appears
- Sectors: [[sector-abandoned-sector]], [[sector-civilian-sector]],
  [[sector-federation-space]], [[sector-pirate-controlled-sector]],
  [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]],
  [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]],
  [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Event lists: `NEUTRAL_PIRATE` ([[source-events-pirate]]); `NEUTRAL`,
  `NEUTRAL_CIVILIAN`, `NEUTRAL_EXIT` ([[source-newevents]]); `NEUTRAL_ROCK`
  ([[source-events-rock]]); `NEUTRAL_ZOLTAN` ([[source-events-zoltan]]);
  `NEUTRAL_LANIUS` ([[source-dlcevents-anaerobic]]); plus the
  Advanced Edition replacements `OVERRIDE_NEUTRAL` and `OVERRIDE_NEUTRAL_EXIT`
  ([[source-dlceventsoverwrite]]) — which the file describes as filler lists used when a
  sector runs out of other calls
- `unique="true"` — once per run ([[source-events-pirate]];
  [[source-fandom-slaver-friendly]] agrees, and tags it a filler/exit event)
- The ship is loaded `<ship load="PIRATE_SLAVER" hostile="false"/>` before the text, so it
  is present but peaceful
- The event element carries a dev note: `<!-- add an event if you kill the crew? -->`
  ([[source-events-pirate]])

## Text
> You recognize the ship as a well-known slave trader. He hails you and offers you
> "laborers" for cheap.

(`event_FRIENDLY_SLAVER_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Buy one slave and free them to join your crew. | — | `<item type="scrap" min="-45" max="-25"/>` and `<crewMember amount="1"/>` — **pay 25–45 scrap, gain 1 crew member**. No outcome text of its own. | 100% |
| 2 | Attack the slaver scum. | — | `<ship hostile="true"/>` — fight the `PIRATE_SLAVER` ship (below). | 100% |
| 3 | Ignore the slaver and continue on your way. | — | Empty `<event/>` — nothing happens. | 100% |
| 4 | **(Teleporter)** Use your teleporter to attempt to board the ship and release some of the slaves. | `req="teleporter" lvl="2"` | Loads `FRIENDLY_SLAVER_TELEPORTER` — always ends in a fight, 2/3 with a free crew member first. | see below |

[[source-fandom-slaver-friendly]] adds a detail the game files do not state: **the crew
race and skills are shown before the trade**, so choice 1 is an informed purchase.

### Choice 4 — `FRIENDLY_SLAVER_TELEPORTER`
Three entries. Every one of them ends with `<ship hostile="true"/>`; two of them also give
`<crewMember amount="1"/>` first. Under **uniform selection across list entries** that is
**2/3 crew + fight, 1/3 fight only** — derived from list membership, not stated as a
percentage anywhere ([[source-events-pirate]]):

| Result | Entries | Share |
|---|---|---|
| *"You beam a small team into their holds… One of the captives seems fit for battle and you throw them a weapon…"* / *"…They are able to get to one person before being caught… You quickly beam the team and prisoner back."* → **+1 crew** and fight | 2 | 2/3 |
| *"…your estimations of the location of their prisoners was off… You beam them back to the ship and prepare for a fight."* → fight only | 1 | 1/3 |

### The `PIRATE_SLAVER` ship (choices 2 and 4)
Same ship as [[event-slaver-hostile]], tagged `<!-- NEEDS ELITE TAG -->`
([[source-events-ships]]):

| Branch | Trigger in the file | Result |
|---|---|---|
| Surrender | `chance="0.2" min="2" max="4"` | *"We surrender! Take one of our slaves as tribute…"* → Accept: **+1 crew member**, ship non-hostile. Refuse: fight continues. |
| Escape | `chance="0.5" min="2" max="4"` → `PIRATE_ESCAPE` | It spins up its FTL. |
| Destroyed | — | *"The slave ship is destroyed…"* → `autoReward level="HIGH"` `standard` |
| Crew killed | loads `DEAD_CREW_SLAVER` | 3-entry table, 2/3 of which pays a crew member; entry 1 lets you pick **Mantis**, **Rockman** or **Engi**. Documented in full on [[event-slaver-hostile]] ([[source-events-xml]]). |

This is what [[source-fandom-slaver-friendly]] means by "the Crew Teleporter blue option
does not prevent receiving another crew by accepting a surrender offer or killing enemy
crew" — the teleporter crew member and the ship's crew rewards stack.

## Blue Options
- **Teleporter, level 2** (`req="teleporter" lvl="2"`) — turns a purchase into a rescue.
  It converts the event into a guaranteed fight, but 2/3 of the time you take a crew
  member out of it for free, and the ensuing fight can pay a second one. Strictly a
  gain-crew line, not a safety line.

## Rewards & Risks
- **Choice 1:** the cheapest crew member in the pirate pool at 25–45 scrap, with the
  species known in advance. No combat risk at all.
- **Choice 2 / 4:** `HIGH` `standard` on a kill, or the `DEAD_CREW_SLAVER` crew table on a
  boarding action, or +1 crew from the surrender — with the teleporter crew member on top
  in 2/3 of choice-4 rolls. The theoretical ceiling is **three** crew members from one
  beacon (teleporter rescue + surrender tribute is impossible — accepting the surrender
  ends the fight — but teleporter rescue + `DEAD_CREW_SLAVER` entry 1 or 2 is not).
- **Risk:** an elite pirate with a low (0.2) surrender rate. Choices 2 and 4 are entirely
  optional fights; choice 3 is free.

## Strategy Notes
- *(Opinion.)* With a Teleporter, choice 4 is the best line on a ship that can win the
  fight — it is the only crew source in the pool that can pay twice.
- Without one, choice 1 vs choice 2 is a scrap-vs-risk question: 25–45 scrap for a known
  crew member is good value early, while the fight is worth more but needs a real weapons
  layout to beat an elite pirate.
- Because the event is `unique`, you get exactly one shot at it per run — and because it
  sits in the `NEUTRAL_EXIT` and filler lists, it can turn up in almost any non-hostile
  sector.

## Related
- [[event-slaver-hostile]] — the same ship demanding crew instead of selling it; full
  `DEAD_CREW_SLAVER` table
- [[event-pirate-briber]] — the other high-value neutral pirate beacon
- [[item-teleporter]] — unlocks choice 4
- [[entity-pirates]], [[entity-mantis]], [[entity-rock-men]], [[entity-engi]]
- [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]],
  [[sector-zoltan-controlled-sector]], [[sector-abandoned-sector]]
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Which species the purchased crew member can be, and how skills are rolled — the
      file is a bare `<crewMember amount="1"/>` with no `class`. Fandom only says the race
      and skills are displayed before the trade.
- [ ] Whether `chance="0.2"` is P(surrender) or P(keep fighting) — see the contradiction on
      [[event-pirate-fight]].
- [ ] The dev note *"add an event if you kill the crew?"* suggests a planned extra outcome
      that was never written. Nothing else in the file follows up on it.

## Sources
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — `NEUTRAL`, `NEUTRAL_CIVILIAN`,
  `NEUTRAL_EXIT`)
- [[source-events-rock]] / [[source-events-zoltan]] / [[source-dlcevents-anaerobic]]
  (per raw/gamedata/events_rock.xml, events_zoltan.xml, dlcEvents_anaerobic.xml — the
  `NEUTRAL_ROCK`, `NEUTRAL_ZOLTAN`, `NEUTRAL_LANIUS` lists)
- [[source-fandom-slaver-friendly]] (per raw/wiki/slaver-friendly.md)
