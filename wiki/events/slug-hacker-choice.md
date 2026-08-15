---
id: event-slug-hacker-choice
type: event
event_name: NEBULA_SLUG_CHOOSE_DEATH
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: true
blue_options: [hacking system]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [unique, combat, nebula, system-malfunction, blue-option, scrap-cost]
---

# Slug hacker (choice) — `NEBULA_SLUG_CHOOSE_DEATH`

## Summary
A Slug hacker lets you pick which of your systems he cripples before he attacks. Every
answer starts a fight with one of your systems halved; you can buy him off for 35 scrap
instead, or — with a Hacking system of your own — deny the hack entirely and fight on even
terms. The reward tier depends on which system you sacrificed.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — via the
  `NEBULA_NEUTRAL_SLUG` event list (`min 3 / max 5` per sector)
  ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: nebula (`<environment type="nebula"/>`), `unique="true"`
- Listed as *neutral*, but four of its five choices lead straight to combat.

## Text
> You are immediately hailed by a dangerous looking ship guarding a station. "I'm feeling
> generouss today. I shall allow you to choose your own death. Which do you like leasst:
> shields, oxygen, or weaponsss?"

(`event_NEBULA_SLUG_CHOOSE_DEATH_text`, per [[source-text-events-xml]])

> ⚠️ **CONTRADICTION:** intro wording.
> - Game files: "…hailed by a dangerous looking ship **guarding a station**."
>   ([[source-text-events-xml]])
> - Fandom: "…hailed by a dangerous looking ship." — the station clause is absent
>   ([[source-fandom-slug-hacker-choice]]).
>
> Also on choice 2's outcome: game files read "Your life support **is sabatoged**" [sic];
> Fandom reads "Your life support **shuts off**". Trusting the game files (`high` vs
> `medium`); most likely Fandom transcribes pre-AE wording.

## Choices & Outcomes

All five choices are `hidden="true"` — you see them only after arriving.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Shields. | — | "Very good then!" → `<ship load="JELLY_STATUS_SHIELDS" hostile="true"/>` + `<status type="divide" target="player" system="shields" amount="2"/>` — your Shields halved for the fight. Destroyed: `MED standard`; crew killed: `HIGH standard`. Shields restored after. | 100% |
| 2 | Oxygen. | — | `<ship load="JELLY_STATUS_OXYGEN" hostile="true"/>` + Oxygen halved. Destroyed **and** crew killed: `MED standard`. Oxygen restored after. | 100% |
| 3 | Weapons. | — | `<ship load="JELLY_STATUS_WEAPONS" hostile="true"/>` + Weapon Control halved. Destroyed and crew killed: `HIGH standard`. Weapons restored after. | 100% |
| 4 | Offer 35 scrap to leave you alone. | — | `<item type="scrap" min="-35" max="-35"/>` — pay 35 scrap, no fight. | 100% |
| 5 | **(Hacking System)** Counter any hack attempt. | `req="hacking"` | "…Wait. Why isn't this working?" → `<ship load="JELLY_STATUS_HACKING" hostile="true"/>` + `<status type="limit" target="player" system="hacking" amount="0"/>` — your **Hacking** is offline instead, everything else intact. Destroyed and crew killed: `HIGH standard`. | 100% |

Reward levels are read from the ship definitions in [[source-events-ships]]; `LOW` / `MED` /
`HIGH` are the game's own words.

Fandom adds three behavioural notes ([[source-fandom-slug-hacker-choice]]):
- The **Shields** option can be chosen even with no Shields system installed.
- The **Oxygen** hack does not fully disable an upgraded Oxygen system — it behaves like the
  Oxygen 2+ blue option in [[event-slug-hacker-oxygen]].
- The **Weapons** hack does not affect [[item-artillery-beam]] or [[item-flak-artillery]].

## Blue Options
- **Hacking system** (`req="hacking"`) — the best line in the event. Your Hacking is zeroed
  for the fight (which you were not going to use against a ship this weak anyway), your
  combat systems stay whole, and the reward is the top `HIGH standard` tier.

## Rewards & Risks
- `HIGH standard` from choices 3 and 5, and from choice 1 on a crew-kill.
- `MED standard` from choice 2, and from choice 1 on a hull-kill.
- Choice 4 costs 35 scrap and yields nothing — it buys safety only.
- The halved system is restored by the winning ship's `status type="clear"` block, so the
  handicap does not persist past the fight ([[source-events-ships]]).

## Strategy Notes
- With Hacking installed, choice 5 dominates: no combat handicap and the highest reward
  tier. *(Opinion, from comparing the reward levels in [[source-events-ships]].)*
- Without it, **Weapons** pays the same `HIGH` tier as the hacking option — but halved
  Weapon Control against an armed Slug ship is the most dangerous handicap of the three.
  **Shields** on a crew-kill also reaches `HIGH`.
- Choice 4 is the only zero-risk exit and is priced at 35 scrap.

## Related
- [[event-slug-hacker-doors]], [[event-slug-hacker-oxygen]], [[event-slug-hacker-medical]] —
  the rest of the Slug remote-hacking family
- [[item-hacking]] — the system that unlocks the blue option
- [[entity-slugs]]

## Open Questions
- [ ] Whether the five choices are all always offered regardless of installed systems
      (Fandom says Shields is, at least).

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-slug-hacker-choice]] (per raw/wiki/slug-hacker-choice.md)
