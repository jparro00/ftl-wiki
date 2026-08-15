---
id: event-slug-hacker-medical
type: event
event_name: NEBULA_SLUG_MEDBAY
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: true
blue_options: [medbay lvl 2, hacking system]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [unique, combat, nebula, boarding, system-malfunction, blue-option, crew-risk]
---

# Slug hacker (medical) — `NEBULA_SLUG_MEDBAY`

## Summary
Two Slug boarders teleport aboard while your Medbay **and** Clone Bay are hacked offline —
a boarding fight with no healing and no revival. An upgraded Medbay gets it half-working;
a Hacking system leaves it fully intact. The best-paying of the Slug hacker events: `HIGH
standard` either way.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — via the
  `NEBULA_HOSTILE_SLUG` event list (`min 5 / max 7` per sector)
  ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: nebula (`<environment type="nebula"/>`), `unique="true"`
- The ship and the boarders are applied by the **event body**, before any choice:
  `<ship load="JELLY_STATUS_MEDBAY" hostile="true"/>` and
  `<boarders min="2" max="2" class="slug"/>` — always exactly two Slug boarders
  ([[source-events-slug]])

## Text
> A Slug ship hails you: "We've detected some worrying radiation coming from your medical
> unit, perhaps you should take a look?" As he signs off, your system shuts off and their
> crew teleports aboard from a nearby station. They don't look like engineers.

(`event_NEBULA_SLUG_MEDBAY_text`, per [[source-text-events-xml]])

> ⚠️ **CONTRADICTION:** intro wording.
> - Game files: "…your **system** shuts off…" ([[source-text-events-xml]])
> - Fandom: "…your **medical bay** shuts off…" ([[source-fandom-slug-hacker-medical]])
>
> Minor, and Fandom's version is clearer, but the files are the authority (`high` vs
> `medium`). Not established as an AE-vs-vanilla difference.

## Choices & Outcomes

All three choices are `hidden="true"`.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | *Continue…* | — | `<status type="limit" target="player" system="medbay" amount="0"/>` and the same for `clonebay` — fight the Slug ship and 2 boarders with **Medbay and Clone Bay offline**. | 100% |
| 2 | **(Improved Medbay)** Try to squeeze some extra power to the system. | `req="medbay" lvl="2"` | "Its lights flicker back on…" → `<status type="divide" target="player" system="medbay" amount="2"/>` — Medbay **halved** instead of dead. | 100% |
| 3 | **(Hacking System)** Counter the remote hacking. | `req="hacking"` | `<status type="limit" target="player" system="hacking" amount="0"/>` — Medbay untouched, your **Hacking** offline instead. | 100% |

Choice 3 is marked `<!-- CHANGED - added -->` — an Advanced Edition addition
([[source-events-slug]]).

### The enemy — `JELLY_STATUS_MEDBAY`

`auto_blueprint="SHIPS_JELLY"`. Both `destroyed` and `deadCrew` give
`<autoReward level="HIGH">standard</autoReward>` and clear the `medbay`, `clonebay` and
`hacking` statuses. **No surrender or escape block** — Fandom flags this explicitly
([[source-events-ships]], [[source-fandom-slug-hacker-medical]]).

## Blue Options
- **Medbay level 2+** (`req="medbay" lvl="2"`) — halved healing beats no healing when two
  boarders are already aboard.
- **Hacking system** (`req="hacking"`) — full Medbay/Clone Bay, no downside that matters in
  this fight. The best line.

Note the Clone Bay is only protected by choice 3: choice 2's `divide` targets `medbay`
only, and a player running a Clone Bay instead of a Medbay does not qualify for choice 2 at
all ([[source-events-slug]]).

## Rewards & Risks
- `HIGH standard` on either a hull kill or a crew kill — the top tier, and unconditional.
- Risk: two Slug boarders with no healing and no cloning. Losing crew here is permanent.
- The ship cannot flee or surrender, so the fight resolves one way or the other.

## Strategy Notes
- The reward does not change with the choice, so take whichever blue option you have —
  they are pure risk reduction. *(Opinion, from the identical reward levels in
  [[source-events-ships]].)*
- Without either, fight the boarders in a room you can control and accept the damage;
  vent-and-suffocate is the standard answer when the Medbay is unavailable.

## Related
- [[event-slug-hacker-choice]], [[event-slug-hacker-doors]], [[event-slug-hacker-oxygen]]
- [[item-hacking]], [[item-medbay]], [[item-clone-bay]]
- [[entity-slugs]]

## Open Questions
- [ ] Whether choice 2 is offered to a Clone Bay ship at all.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-slug-hacker-medical]] (per raw/wiki/slug-hacker-medical.md)
