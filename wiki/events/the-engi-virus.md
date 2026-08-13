---
id: event-the-engi-virus
type: event
event_name: ENGI_VIRUS
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]]
beacon_type: any
hostile: true
blue_options: [hacking lvl 1, hacking lvl 2, hacking lvl 3, engi crew, lanius crew]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, dlc, blue-option, crew-risk, crew-reward, augment-reward, hull-repair, reactor-upgrade, system-malfunction, clone-bay-failure]
---

# The Engi virus — `ENGI_VIRUS`

## Summary
The densest blue-option event in Engi space: **five** separate gates (Hacking at three
levels, Engi crew, Lanius crew), each with a different payout, over a base case that is
just a fight you did not ask for. Every blue option awards the Drone Reactor Booster
augmentation; the Hacking-2 and Hacking-3 options add hull repairs and a free reactor bar
on top. The Engi-crew option is the outlier — it kills your Engi permanently, then may give
them back maxed out.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]
- Beacon: ordinary — no `<distressBeacon/>` or `<store/>` tag ([[source-events-xml]], per
  `raw/gamedata/events_engi.xml`)
- Event list: `NEUTRAL_ENGI`, allocated `min=4 max=6` in Engi Controlled Sector and
  `min=5 max=7` in Engi Homeworlds ([[source-sector-data-xml]])
- Marked in the file as DLC-added content
- `unique="true"`. A developer comment beside the definition reads *"Right now you can get
  this more than once in a game. Dunno how good that is"* — a note that predates the
  `unique` flag now on the event ([[source-events-xml]]).

## Text
> The Engi are awaiting you at the beacon, with their weapons on-line! They explain a
> computer virus that is wanted for hostile acts against the Engi (multiple counts of binary
> scrambling, nano-dissolution, and variable interference) is aboard your vessel.

(`event_ENGI_VIRUS_text`, per [[source-text-events-xml]])

The event's only top-level choice is an unlabelled `continue`, leading to:

> They insist they must destroy your ship to prevent the virus from escaping!

## Choices & Outcomes

All seven choices below sit on that second screen.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Hold on! Let us try to purge the system code! | — | *"Wiping your engine core and shields proves useless…"* → **Shields and Engines are halved** (`<status type="divide" … amount="2"/>` on each), then fight `ENGI_VIRUS_SHIP`. | 100% |
| 2 | Attack the Engi vessel! | — | *"The Engi be damned, no one threatens your ship."* → fight `ENGI_VIRUS_SHIP` at full strength. | 100% |
| 3 | **(Hacking System)** Isolate and quarantine the virus. | `req="hacking" lvl="1"` | Virus ejected and destroyed; the Engi jump away → `LOW` `standard` **and** `<augment name="DRONE_SPEED"/>` — **Drone Reactor Booster**. No fight. | 100% |
| 4 | **(Improved Hacking)** Reprogram the virus. | `req="hacking" lvl="2"` | *"the virus 'sees the light'…"* → `<damage amount="-15"/>` (**15 hull repairs**) and `<upgrade amount="1" system="reactor"/>` (**+1 reactor**), then **Drone Reactor Booster**. No fight. | 100% |
| 5 | **(Advanced Hacking)** Reprogram the virus. | `req="hacking" lvl="3"` | As #4 but `<damage amount="-30"/>` — **30 hull repairs** — plus +1 reactor and **Drone Reactor Booster**. No fight. | 100% |
| 6 | **(Lanius Crew)** Your Lanius crewmember gestures frantically. | `req="anaerobic"` | *"the Lanius… proceeds to... digest the terminal."* → `<autoReward level="MEDIUM">scrap_only</autoReward>` and **Drone Reactor Booster**. No fight. | 100% |
| 7 | **(Engi Crew)** Have your Engi crewmember negotiate with the Engi ship. | `req="engi"` | *"your Engi crewmember suddenly dissolves into nanites"* → **you lose an Engi crewmember**, `<clone>false</clone>` — a Clone Bay **cannot** revive them — then fight `ENGI_VIRUS_SHIP_ALT`. | 100% |

### The fights

- **`ENGI_VIRUS_SHIP`** (choices 1–2): on destroyed *or* dead crew →
  `<autoReward level="MEDIUM">standard</autoReward>`, plus
  `<status type="clear" … system="engines"/>` and the same for `shields` — which **restores
  the halved systems** from choice 1 ([[source-events-xml]]).
- **`ENGI_VIRUS_SHIP_ALT`** (choice 7): on destroyed *or* dead crew →
  `MEDIUM` `standard`, then continue → `ENGI_VIRUS_REBORN`:
  > To your surprise your Engi crewmember reforms. It looks as if the virus reconstituted,
  > repurposed, and reprogrammed the Engi host and wants to travel with you... and it seems
  > to have learned a great deal from its time on your ship.

  → `<crewMember amount="1" class="engi" all_skills="2" id="name_Virus"/>` — an Engi named
  **Virus**, which Fandom reads as maxed in all skills
  ([[source-fandom-the-engi-virus]]).

## Blue Options
- **[[item-hacking]] level 1** (`req="hacking" lvl="1"`) — no fight, `LOW` scrap-with-resources
  and the augment.
- **[[item-hacking]] level 2** — no fight, 15 repairs, +1 reactor, the augment.
- **[[item-hacking]] level 3** — no fight, 30 repairs, +1 reactor, the augment.
- **Lanius crewmember** (`req="anaerobic"`) — no fight, `MEDIUM` scrap and the augment. Note
  the requirement string is `anaerobic`, not `lanius`.
- **Engi crewmember** (`req="engi"`) — the only blue option here that makes things *worse*:
  it kills the Engi and still starts a fight.

The three Hacking choices all carry `max_group="0"`; what that attribute does is not stated
by any source here ([[source-events-xml]]).

> ⚠️ **DANGER:** Fandom warns that taking choice 7 when the Engi is your **only**
> crewmember is a game over ([[source-fandom-the-engi-virus]]). The game files support the
> mechanism — `<removeCrew class="engi">` with `<clone>false</clone>` — but do not state the
> game-over consequence, so this rests on Fandom (`medium` reliability).

## Rewards & Risks
- **[[item-drone-reactor-booster]]** (`DRONE_SPEED`) from all four non-Engi blue options.
- Up to 30 hull repairs and a free reactor bar from Hacking 3 — among the largest
  no-cost swings any single event offers.
- **Risks:** choice 1 halves Shields and Engines *for the fight* (restored on victory);
  choice 7 permanently kills an Engi that a Clone Bay cannot bring back, and may or may not
  return them as "Virus" only after you win the follow-up fight; choices 1, 2 and 7 all end
  in combat.

> ⚠️ **CONTRADICTION (data vs. schema):** four `autoReward` lines in this event are written
> `level="MEDIUM"` — on `ENGI_VIRUS_SHIP` (×2), `ENGI_VIRUS_SHIP_ALT` (×2) and the Lanius
> branch — where the game's other events use `LOW` / `MED` / `HIGH` / `RANDOM`.
> - Game files: the literal string is `MEDIUM` ([[source-events-xml]], per
>   `raw/gamedata/events_engi.xml`).
> - Fandom: annotates each as a typo for `MED`, and states the game "treats non-standard
>   reward values as a `RANDOM` value" ([[source-fandom-the-engi-virus]]).
>
> The typo is verified; the fallback behaviour is Fandom's claim about the engine and is not
> stated in the files. Same pattern as [[event-engi-smashed-ships]].

## Strategy Notes
- With Hacking at any level, this is one of the best events in the game — a free augment and,
  from level 2, a large repair plus a reactor bar, with no fight. Hacking 3 is worth
  reaching before an Engi sector if you are close. *(Opinion.)*
- With a Lanius but no Hacking, choice 6 is a clean skip-the-fight-and-get-paid.
- The Engi-crew option is a trap dressed as a blue option: it costs you a crewmember, denies
  the Clone Bay, and still makes you fight. The compensation — a max-skill Engi named Virus —
  only arrives if you win, and only replaces what you lost. *(Opinion, though the outcome
  chain is explicit in the files.)*
- Without any gate, choice 2 is strictly better than choice 1: the same fight and the same
  reward, without halved Shields and Engines. *(Opinion, derived from the two branches.)*
- Fandom adds that using an Engi previously reborn as "Virus" makes no difference to the
  outcome ([[source-fandom-the-engi-virus]]) — sourced there to a single anonymous
  contributor, so treat as low confidence.

## Related
- [[event-engi-smashed-ships]] — the other DLC `NEUTRAL_ENGI` unique with an Engi-crew blue option
- [[item-drone-reactor-booster]] — the reward four of the five gates share
- [[item-hacking]], [[entity-lanius]], [[entity-engi]]
- [[concept-blue-options]]

## Open Questions
- [ ] What does `max_group="0"` do — are the three Hacking choices mutually exclusive?
- [ ] Does the engine really fall back to `RANDOM` on an unrecognised `autoReward` level?
- [ ] Does `all_skills="2"` mean fully maxed, or level 2 of a higher cap?
- [ ] Is the game-over-on-last-crewmember warning reproducible?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-the-engi-virus]] (per `raw/wiki/the-engi-virus.md`)
