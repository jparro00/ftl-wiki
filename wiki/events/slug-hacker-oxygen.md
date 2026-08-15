---
id: event-slug-hacker-oxygen
type: event
event_name: NEBULA_SLUG_OXYGEN
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: true
blue_options: [oxygen lvl 2, hacking system]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [unique, combat, nebula, system-malfunction, fire-risk, blue-option, crew-risk]
---

# Slug hacker (oxygen) — `NEBULA_SLUG_OXYGEN`

## Summary
Your Oxygen system is hacked to zero and the Slug attacks with a fire weapon. Suffocation
plus fire, with no way to vent. Two blue options soften it: an upgraded Oxygen system keeps
life support barely running, and a Hacking system restores it outright. Notable as **the
only event in the game with a blue option for an upgraded Oxygen system**
([[source-fandom-slug-hacker-oxygen]]).

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — via the
  `NEBULA_HOSTILE_SLUG` event list (`min 5 / max 7` per sector)
  ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: nebula (`<environment type="nebula"/>`), `unique="true"`
- The oxygen shutdown and the enemy ship are applied by the **event body**, before any
  choice: `<status type="limit" target="player" system="oxygen" amount="0"/>` and
  `<ship load="JELLY_STATUS_OXYGEN_FIRE" hostile="true"/>` ([[source-events-slug]])
- Dev note in source: `<!-- NEEDS CODE TO GIVE FIRE WEAPONS-->`

## Text
> The Slugs here use a tactic you hoped you'd never see: they use a remote hacking
> satellite to sabotage your oxygen production system and then charge fire-weapons -
> you're going to suffocate!

(`event_NEBULA_SLUG_OXYGEN_text`, per [[source-text-events-xml]])

> ⚠️ **CONTRADICTION:** intro wording.
> - Game files: "…**they use a remote hacking satellite to** sabotage your oxygen
>   production system…" ([[source-text-events-xml]])
> - Fandom: "…**They** sabotage your oxygen production system…" — no hacking satellite, and
>   "The slugs" is lower-cased ([[source-fandom-slug-hacker-oxygen]]).
>
> Trusting the game files (`high` vs `medium`). Likely a version difference: the Hacking
> system is an Advanced Edition addition, and this event's hacking-related choice is marked
> `<!-- CHANGED - added -->` in the source — so Fandom's text plausibly predates AE.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | *Continue…* | — | Nothing further — you fight with **Oxygen offline** (set by the event body). | 100% |
| 2 | **(Improved Oxygen)** Try to squeeze some extra power to the system. | `req="oxygen" lvl="2"` | "…able to counter their hacking enough to keep the life support barely functional." → `<status type="divide" target="player" system="oxygen" amount="2"/>` — Oxygen **halved** instead of offline. | 100% |
| 3 | **(Hacking System)** Counter the remote hacking. | `req="hacking"` | `<status type="limit" target="player" system="hacking" amount="0"/>` + `<status type="clear" target="player" system="oxygen" amount="100"/>` — **Oxygen fully restored**, your Hacking offline instead. | 100% |

All three are `hidden="true"`. Choice 3 is marked `<!-- CHANGED - added -->`
([[source-events-slug]]).

### The enemy — `JELLY_STATUS_OXYGEN_FIRE`

`auto_blueprint="SHIPS_JELLY"`, no surrender or escape block, and a forced fire weapon
([[source-events-ships]]):

```
<weaponOverride count="1">
    <name>BEAM_FIRE</name>
    <name>BOMB_FIRE</name>
</weaponOverride>
```

Both `destroyed` and `deadCrew` give `<autoReward level="MED">standard</autoReward>` and
clear the `oxygen` and `hacking` statuses.

## Blue Options
- **Oxygen level 2+** (`req="oxygen" lvl="2"`) — halves rather than kills life support.
  Note the divide is applied *on top of* the event body's `limit … amount="0"`, so the
  practical effect is "barely functional" rather than "half speed".
- **Hacking system** (`req="hacking"`) — restores Oxygen completely. Strictly better than
  choice 2.

## Rewards & Risks
- `MED standard` on a win, whichever choice you take — the blue options change the danger,
  not the payout ([[source-events-ships]]).
- Risk: suffocation across the whole ship while fighting a fire-weapon ship in a nebula.
  Crew loss is a real outcome if the fight drags.

## Strategy Notes
- Hacking > Oxygen 2 > nothing. With Hacking you are fighting an ordinary fire-weapon Slug
  ship. *(Opinion, from the status effects in [[source-events-slug]].)*
- With neither, close the doors of the room you are fighting in, keep crew in the O2 room's
  pocket of air, and prioritise killing the fire weapon over the hull.
- Fandom notes the upgraded-Oxygen blue option also appears in the "Dangerous-looking ship"
  event ([[source-fandom-slug-hacker-oxygen]]) — its "only event" claim refers to the
  *blue option*, and it contradicts itself in the same note. Treat the "only event" line
  with caution.

## Related
- [[event-slug-hacker-choice]] — its Oxygen branch behaves like this event's blue option
- [[event-slug-hacker-doors]], [[event-slug-hacker-medical]]
- [[item-hacking]], [[item-oxygen-system]]
- [[entity-slugs]]

## Open Questions
- [ ] Exact stacking behaviour of `limit amount="0"` followed by `divide amount="2"`.
- [ ] Whether Fandom's pre-AE text is confirmed as a vanilla string.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-slug-hacker-oxygen]] (per raw/wiki/slug-hacker-oxygen.md)
