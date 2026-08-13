---
id: event-auto-ship-carrying-shield-virus
type: event
event_name: AUTO_HACKER
sectors: [[[sector-civilian-sector]], [[sector-federation-space]]]
beacon_type: hostile
hostile: true
blue_options: [[[item-hacking]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [rebel, auto-ship, unique, system-malfunction, blue-option, ae-addition, contradiction]
---

# Auto-ship carrying shield virus — `AUTO_HACKER`

## Summary
A forced auto-ship fight that starts with your Shields already crippled: a satellite-borne
virus halves your shield system before the first shot. Advanced Edition added a Hacking
blue option that counters the virus — but in the game files that option also **swaps the
enemy ship for a Slug ship** and takes your Hacking system offline instead, which is not
what the community wiki describes.

## Trigger & Where It Appears
- Sectors: [[sector-civilian-sector]], [[sector-federation-space]].
- Beacon: hostile — a hostile ship is loaded on arrival.
- Event lists: `HOSTILE1` ([[source-newevents]]) and `OVERRIDE_HOSTILE1`
  ([[source-dlceventsoverwrite]]). It also appears commented out in `HOSTILE_CIVILIAN`
  ([[source-newevents]], line 84).
- `unique="true"` — at most once per run.
- Long-range scanners show a ship ([[source-fandom-auto-ship-carrying-shield-virus]]).

> ⚠️ **CONTRADICTION (reach):** [[source-fandom-auto-ship-carrying-shield-virus]] lists
> **Civilian Sector only**. The event sits in the generic `HOSTILE1` /
> `OVERRIDE_HOSTILE1` pools, which are also drawn on by
> [[sector-federation-space]] ([[source-newevents]], [[source-dlceventsoverwrite]]).
> Trusting the game files — the Fandom location box is narrower than the lists imply.

## Text
> Your arrival is greeted by numerous computer alerts. The nearby automated Rebel scout has
> used a local satellite to deploy a virus to disrupt your Shields System. Hopefully it
> won't cause further problems before you can destroy it.

(`event_AUTO_HACKER_text`, per [[source-text-events-xml]])

> ⚠️ **CONTRADICTION (wording):** Fandom transcribes this as *"…has **deployed a virus and
> disrupted your shield system**."* — no satellite, past tense
> ([[source-fandom-auto-ship-carrying-shield-virus]]). The game file says *"has **used a
> local satellite to deploy a virus to disrupt your Shields System**"*
> ([[source-text-events-xml]]). Trusting the game files (`high` vs `medium`). The event's
> Hacking choice carries a `<!-- CHANGED - added -->` dev comment in
> `events_rebel.xml`, confirming the event was edited for AE — so the wiki is plausibly
> transcribing pre-AE text, but nothing in the sources read here confirms that.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | *Continue…* | — | `<status type="divide" target="player" system="shields" amount="2"/>` — **your Shields are halved** — then fight `REBEL_AUTO_HACKSHIELDS`. | 100% |
| 2 | **(Hacking System)** Counter the remote hacking. | `req="hacking"`, `hidden="true"` | *"Your hacking system automatically counters the digital assault and you move in to fight the ship."* Shields untouched; `<status type="limit" target="player" system="hacking" amount="0"/>` — **Hacking is limited to 0** — and the enemy becomes `<ship load="JELLY" hostile="true"/>`. | 100% |

The event loads `<ship load="REBEL_AUTO_HACKSHIELDS" hostile="true"/>` at the top level;
choice 2's inner event overrides it with `JELLY` ([[source-events-rebel]]).

### The `REBEL_AUTO_HACKSHIELDS` ship (choice 1)
`auto_blueprint="SHIPS_AUTO"`. Both `destroyed` and `deadCrew` give
([[source-events-ships]]):

> The ship explodes, leaving behind a collection of useful scrap material.

→ `autoReward level="MED"` `standard`, plus
`<status type="clear" target="player" system="shields" amount="100"/>` and
`<status type="clear" target="player" system="hacking" amount="100"/>` — i.e. **winning
lifts the shield debuff**. No surrender, no escape branch.

### The `JELLY` ship (choice 2)
> ⚠️ **CONTRADICTION (enemy identity):** the AE Hacking branch loads `JELLY`, which is
> `auto_blueprint="SHIPS_JELLY"` — a **Slug ship**, with a 50% surrender chance
> (`SLUG_SURRENDER`), a 50% escape chance (`PIRATE_ESCAPE`), and `DESTROYED_DEFAULT` /
> `DEAD_CREW_DEFAULT` endings ([[source-events-ships]]).
> [[source-fandom-auto-ship-carrying-shield-virus]] instead says you *"Fight an Auto-ship
> with your Hacking offline"* and gives the same
> *"The ship explodes, leaving behind a collection of useful scrap material"* /
> `MED` `standard` result as choice 1.
>
> Trusting the game files (`high` vs `medium`): the XML plainly reads
> `<ship load="JELLY" hostile="true"/>`. This looks like a **dev slip** — a Rebel scout in a
> Civilian sector should not turn into a crewed Slug cruiser — but it is what ships.
> Note the consequence: because `JELLY` has no `status type="clear"` on its endings, the
> Hacking limit imposed by choice 2 may not be lifted on victory the way choice 1's shield
> debuff is. Untested here.

## Blue Options
- **[[item-hacking]]** (`req="hacking"`, `hidden="true"`) — an **AE addition**, marked
  `<!-- CHANGED - added -->` in the file ([[source-events-rebel]]). It trades the halved
  Shields for a disabled Hacking system: strictly better if your Hacking is not part of
  your kill plan, and it also skips the auto-ship for a ship that can surrender. The
  requirement is the *system*, not a specific level.

## Rewards & Risks
- Reward: `MED` `standard` on either path.
- Risk (choice 1): **Shields halved, rounding down against you**
  ([[source-fandom-auto-ship-carrying-shield-virus]]) for the duration of the fight — a
  4-layer shield becomes 2. Against an AE auto-ship this is the difference between
  trivial and dangerous.
- Risk (choice 2): Hacking offline, plus an enemy that can escape with 50% probability.

## Strategy Notes
- *(Opinion.)* Take the blue option if you have Hacking and are not relying on it to win
  fights; losing Hacking for one encounter is cheaper than losing half your shields.
- The debuff is cleared by destroying `REBEL_AUTO_HACKSHIELDS` — so on choice 1 there is
  no lingering cost, only in-fight danger.

## Related
- [[event-auto-ship-fight]] — the plain version of the same auto-ship fight
- [[item-hacking]] — the system that gates choice 2
- [[item-shields]]
- [[concept-rebel-fleet-advance]], [[entity-slugs]]
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Is the `JELLY` enemy on choice 2 intentional or a copy-paste bug? Nothing in the file
      comments on it.
- [ ] Does `status type="limit" system="hacking" amount="0"` persist after the fight when
      the enemy is `JELLY` (which has no `status clear`)?
- [ ] Is the Fandom text a vanilla transcription, i.e. was the intro rewritten for AE?

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-fandom-auto-ship-carrying-shield-virus]] (per `raw/wiki/auto-ship-carrying-shield-virus.md`)
