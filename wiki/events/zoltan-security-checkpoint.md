---
id: event-zoltan-security-checkpoint
type: event
event_name: ZOLTAN_CREW_SCAN
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: any
hostile: false
blue_options: [slug crew, [[item-mind-control]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, blue-option, crew-risk, boarding-risk, fuel-reward, system-damage]
---

# Zoltan security checkpoint — `ZOLTAN_CREW_SCAN`

## Summary
A neutral Zoltan checkpoint with two blue options that both pay the same reward. Without
one of them, submitting is a coin-flip between "nothing happens" and a nasty forced
choice: give up a crew member permanently, or fight a Zoltan ship with boarders aboard
**and your Weapon Control halved**.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: ordinary; no environment hazard and no distress flag.
- Reached via the `NEUTRAL_ZOLTAN` event list, allocated `min=5 max=6` beacons in both
  Zoltan sectors ([[source-sector-data-xml]]).
- `unique="true"` — at most once per sector.

## Text
> You arrive at a Zoltan security checkpoint set up in a perimeter around the beacon.
> "Travelling vessel, you will submit to crew profiling to identify fugitives of the
> empire."

(`event_ZOLTAN_CREW_SCAN_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | You don't have time for this nonsense. Attack! | — | *"Expecting resistance, their Energy Shield is raised and ready for combat."* → fight `ZOLTAN_SHIP` ([[entity-zoltan]]), default rewards. | 100% |
| 2 | Submit to profiling. | — | Loads `ZOLTAN_CREW_SCAN_LIST` — two entries, see below. | unknown |
| 3 | **(Slug Crew)** Have your Slug talk them into letting you go. | `req="slug"` | *"…no words were exchanged, but the guards offer you some supplies and say the ship checks out."* → `autoReward level="MED"` `fuel_only`. | 100% |
| 4 | **(Mind Control)** Make the guards believe they have already checked your crew today. | `req="mind"` | *"Back so soon friend! …take these spare fuel canisters…"* → `autoReward level="MED"` `fuel_only`. | 100% |

### `ZOLTAN_CREW_SCAN_LIST` — the two results of choice 2

**Entry 1 — clean pass.**
> The Zoltan security staff board your ship and scan the crew's faces into a computer.
> After a few tense moments of uncertainty they allow your ship to pass.

Nothing happens.

**Entry 2 — a crew member is flagged.**
> …Suddenly alarms go off and the Zoltan leap on one of your crew! "This person is
> wanted on five charges of Utter Villainy! Surrender them to us!"

This opens a second, forced sub-choice:

| # | Sub-choice | Outcome |
|---|-----------|---------|
| 2a | Give up your crewmember. | `<removeCrew>` with `<clone>false</clone>` — **permanent crew loss, [[item-clone-bay]] cannot recover them** ("your crewmember was taken away unharmed so your Clone Bay was unable to retrieve them"). |
| 2b | Refuse and fight. | `<ship load="ZOLTAN_CREW_SCAN" hostile="true"/>` + `<boarders min="2" max="4" class="energy"/>` + `<status type="divide" target="player" system="weapons" amount="2"/>` — **2–4 Zoltan boarders, and your Weapon Control is halved** (rounds down against you). Destroy the ship → `low` scrap with resources; kill the crew → `medium` scrap with resources. |

Both list entries appear once; **the game files state no percentages**
([[source-events-zoltan]], per raw/gamedata/events_zoltan.xml). Reward tiers for 2b come
from [[source-fandom-zoltan-security-checkpoint]].

## Blue Options
- **Slug crew member** (`req="slug"`) — any [[entity-slugs]] crew satisfies it. Converts
  the whole event into a guaranteed `MED` fuel payout with no risk. Fandom glosses `MED`
  fuel as **2–4 fuel** ([[source-fandom-zoltan-security-checkpoint]]); the game file only
  says `MED`.
- **[[item-mind-control]]** (`req="mind"`) — the Mind Control *system*, not a crew type.
  Identical payout to the Slug option. If you have both, they are interchangeable here.

Note that neither blue option is gated on a level (`lvl` is unset), so Mind Control 1 is
enough ([[source-events-zoltan]]).

## Rewards & Risks
- **Rewards:** `MED` `fuel_only` via either blue option; default rewards from the
  choice-1 fight; `low`/`medium` scrap-with-resources from the 2b fight.
- **Risks:** permanent, non-cloneable crew loss (2a); a boarding fight at half weapon
  power (2b) — the halved Weapon Control is the real danger, since it can leave you
  unable to break the Zoltan Super Shield.

## Strategy Notes
- *Opinion:* with either blue option this is free fuel and should always be taken.
  Without one, choice 1 (attack immediately) is more predictable than choice 2 — you get
  a normal Zoltan fight at full weapon power instead of a coin-flip that can degenerate
  into the same fight at half weapon power plus boarders.
- Do not treat a Clone Bay as insurance: outcome 2a explicitly disables it.

> ⚠️ **CONTRADICTION:** two wording differences with Fandom.
> - Intro: game files *"**Travelling** vessel"*; Fandom *"**Traveling** vessel"*
>   ([[source-text-events-xml]] vs [[source-fandom-zoltan-security-checkpoint]]).
> - Clean-pass text: game files *"The Zoltan security staff board your ship and scan the
>   crew's faces into a computer. After a few tense moments of uncertainty they allow
>   your ship to pass."*; Fandom *"After a few moments of uncertainty, your crew is
>   allowed to pass."*
>
> Trusting the game files in both cases (`high` vs `medium`). The second looks like an
> abridged wiki paraphrase rather than a version difference, but that is unconfirmed.

## Related
- [[event-zoltan-trade-hub]] — the other Zoltan event that beams boarders aboard after a
  failed social approach
- [[entity-zoltan]] — the enemy in choices 1 and 2b
- [[entity-slugs]], [[item-mind-control]] — the two gates
- [[item-clone-bay]] — explicitly disabled by outcome 2a

## Open Questions
- [ ] Weighting between the two `ZOLTAN_CREW_SCAN_LIST` entries.
- [ ] Exact fuel range for `MED` `fuel_only` (Fandom says 2–4; game files say only `MED`).
- [ ] Is the flagged crew member chosen at random?
- [ ] Does `ZOLTAN_CREW_SCAN` (the ship) differ from `ZOLTAN_SHIP` in loadout? Fandom
      notes neither has surrender/escape values specified in `events_ships.xml`.

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-zoltan-security-checkpoint]] (per raw/wiki/zoltan-security-checkpoint.md)
