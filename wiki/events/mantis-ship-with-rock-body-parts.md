---
id: event-mantis-ship-with-rock-body-parts
type: event
event_name: ROCK_MANTIS_HUNTER
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: any
hostile: false
blue_options: [[[item-rock-plating]], [[item-rock-crew]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [rock, mantis, blue-option, default-rewards, unique, avoidable-fight]
---

# Mantis ship with Rock body parts — `ROCK_MANTIS_HUNTER`

## Summary
A Mantis ship decorated with the remains of Rockmen it has killed. It is **not hostile on
arrival** and you can simply leave. Both blue options here are traps of a sort: the Rock
Plating option genuinely helps (it disables the enemy's engines before the fight), while
the Rock Crew option starts the same fight for nothing but a line of dialogue.

## Trigger & Where It Appears
- Sectors: [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- Event list: `NEUTRAL_ROCK`, allocated `min="7" max="8"` per Rock sector
  ([[source-sector-data-xml]])
- Beacon: ship present but **non-hostile** — `<ship load="MANTIS_FIGHT" hostile="false"/>`
  ([[source-events-rock]]); [[source-fandom-mantis-ship-with-rock-body-parts]] marks
  `LRSmap=ship`
- `unique="true"` — at most once per sector ([[source-events-rock]])

## Text
> A Mantis ship here is adorned with Rock body parts! It would be a gorier display if they
> had internal organs, but the message is clear enough: this is a hunter of a very
> specialized kind.

(`event_ROCK_MANTIS_HUNTER_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack! | — | *"No species deserves a Mantis hunter on their back…"* → `<ship hostile="true"/>`. Fight `MANTIS_FIGHT`, default rewards. | 100% |
| 2 | Ignore them. | — | *"The Mantis take no interest in your ship - they're lying in wait for the next Rock ship to venture through. You're able to spin up the engines and jump at your leisure."* Nothing happens. | 100% |
| 3 | **(Rock Ship)** Ram the bastards. | `req="ROCK_ARMOR"` | You ram them; your armoured hull is undamaged. `<ship hostile="true"/>` **plus** `<status type="limit" target="enemy" system="engines" amount="0"/>` — the enemy's Engines are capped at 0 power. | 100% |
| 4 | **(Rock Crew)** Put your Rock crewmember on the comm. | `req="rock"` | An exchange of insults (*"Cave-dwelling pebble-man!"*) → `<ship hostile="true"/>`. Identical fight to choice 1, **no mechanical benefit**. | 100% |

### The enemy ship — `MANTIS_FIGHT`
- `auto_blueprint="SHIPS_MANTIS"`, crew 80% Mantis / 20% Engi
  ([[source-events-ships]])
- `destroyed` / `deadCrew` both load the generic `DESTROYED_DEFAULT` /
  `DEAD_CREW_DEFAULT` — hence "default rewards"
- **No `<surrender>` and no `<escape>`** — the fight goes to the end.
  [[source-fandom-mantis-ship-with-rock-body-parts]] agrees (`|no|` in its template).

## Blue Options
- **Rock Plating augment** (`req="ROCK_ARMOR"`) — despite the in-game label reading
  *"(Rock Ship)"*, the gate is the **augment**, not the hull.
  [[source-fandom-mantis-ship-with-rock-body-parts]] spells this out: *"Requires Rock
  Plating"*. Any ship carrying `ROCK_ARMOR` qualifies; it is not exclusive to the Rock
  Cruiser, which merely starts with it — `PLAYER_SHIP_ROCK` lists `<aug name="ROCK_ARMOR"/>`
  in `raw/gamedata/blueprints.xml` ([[source-blueprints]]). The payoff is real: `status type="limit" … system="engines"
  amount="0"` caps the enemy's engine power at zero, so their evasion is gone for the
  fight.
- **Rock crew member** (`req="rock"`) — cosmetic. It produces different prose and the
  exact same hostile `MANTIS_FIGHT` with no status effect and no altered reward
  ([[source-events-rock]]).

> ⚠️ **CONTRADICTION (label vs. gate):** the choice text says *"(Rock Ship)"* but
> `req="ROCK_ARMOR"` names an augment ([[source-events-rock]], per
> `raw/gamedata/events_rock.xml`). [[source-fandom-mantis-ship-with-rock-body-parts]]
> resolves it in the augment's favour and the game files support that reading — a `req`
> attribute matches augments, systems and crew classes, never a ship id. Trusting the
> augment reading; the label is simply loose writing by the developers.

## Rewards & Risks
- Every fighting branch gives **default rewards** for a Mantis ship
  ([[source-fandom-mantis-ship-with-rock-body-parts]]). There is **no** reward difference
  between choices 1, 3 and 4.
- Choice 2 costs and gives nothing.
- Risk: a full-strength `SHIPS_MANTIS` with a mostly-Mantis crew and no surrender option.
  Boarding it is dangerous; it will board you.

## Strategy Notes
- **Choice 3 if you have Rock Plating, otherwise choice 1 or 2 on the merits of the fight.**
  Never choice 4 — it is choice 1 with extra steps.
- [[source-fandom-mantis-ship-with-rock-body-parts]] notes that *"even if you're in a Rock
  Cruiser when using the 'Ignore them' option, the Mantis take no interest in your ship"* —
  the hunter's stated interest in Rockmen is flavour only and does not force the fight.

## Related
- [[event-mantis-ships-battle-for-rock-freighter]] — the other Mantis beacon in Rock space
- [[event-rock-atheists]] — where you can pick up the Rock crew member this event asks for
- [[item-rock-plating]], [[item-rock-crew]]
- [[entity-mantis]], [[entity-rock-men]], [[entity-rock-cruiser]]

## Open Questions
- [ ] Does `status type="limit" amount="0"` on engines persist for the whole fight, or can
      the enemy repair out of it?
- [ ] Exact values behind "default rewards" for `SHIPS_MANTIS`.

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-fandom-mantis-ship-with-rock-body-parts]] (per raw/wiki/mantis-ship-with-rock-body-parts.md)
