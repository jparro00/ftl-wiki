---
id: event-mantis-named-thief-defeat
type: event
event_name: MANTIS_NAMED_THIEF_DEFEAT
sectors: [[[sector-mantis-homeworlds]]]
beacon_type: hostile
hostile: false
blue_options: [teleporter, "sensors level 3", "medbay level 2", "clonebay level 2"]
chain: [[[chain-mantis-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [aftermath, ship-unlock, crew-reward, augment-reward, blue-option, unique, mantis]
---

# KazaaakplethKilik defeated — `MANTIS_NAMED_THIEF_DEFEAT`

## Summary
The aftermath event that decides the [[chain-mantis-cruiser-unlock]]. It fires **only when
you kill the crew** of KazaaakplethKilik's ship — not when you destroy the hull — and it is
where the Mantis Cruiser is won or lost. Four nested layers of blue options separate
"loot the wreck" from "recruit the legendary thief, take his augment, and unlock a ship".

## Trigger & Where It Appears
- **Not in any sector event list.** It is loaded from a ship block: the
  `MANTIS_NAMED_THIEF` hull declares `<deadCrew load="MANTIS_NAMED_THIEF_DEFEAT"/>`
  ([[source-events-ships]]).
- The parent encounter is [[event-legendary-thief-kazaaakplethkilik]]
  (`MANTIS_NAMED_THIEF`), a `unique` event in [[sector-mantis-homeworlds]].
- **Destroying the ship does not reach here.** `MANTIS_NAMED_THIEF`'s `<destroyed>` block
  pays `MED standard` and ends the encounter — *"KazaaakplethKilik fights to the last…"*.
  Only `deadCrew` loads this event. Killing the crew therefore requires boarding, a
  bio-beam, fire/asphyxiation, or an anti-personnel drone.
- The hull has **no surrender and no escape block** at all, so there is no third path
  ([[source-events-ships]]).
- Fandom documents this whole tree inside its *Legendary thief KazaaakplethKilik* page
  ([[source-fandom-legendary-thief-kazaaakplethkilik]]).

## Text
> No more life signs are detected aboard their ship. You appear to have won.

(`event_MANTIS_NAMED_THIEF_DEFEAT_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Move in to strip their ship. | — | *"It seems almost a waste for such a fierce foe to die in such an anticlimactic fashion."* → `HIGH standard`. **Chain ends here.** | 100% |
| 2 | **(Teleporter)** Quickly teleport additional crew and check for survivors. | `req="teleporter"` | *"You find KazaaakplethKilik slumped in a corner dying."* → opens the survivor sub-tree below. | 100% |
| 3 | **(Sensors)** Quickly scan their ship for survivors. | `req="sensors" lvl="3"` | *"You detect KazaaakplethKilik slumped in a corner dying."* → the **same** sub-tree, with the wording changed from teleporting to docking. | 100% |

### The survivor sub-tree (identical under choices 2 and 3)

| # | Choice | Requirement | Outcome(s) |
|---|--------|-------------|-----------|
| a | Put him out of his misery. / Let him die. | — | *"Thus ends the life of the famed captain…"* → `HIGH standard`. Chain ends. |
| b | Listen to what he has to say. / Dock and try to speak with him. | — | *"In his dying moments he gives up the location of his secret stash."* → `HIGH standard` **+ quest marker** `MANTIS_NAMED_THIEF_STASH`. Chain ends, but you keep the stash. |
| c | **(Adv. Medbay)** Quickly teleport / dock and take him back to the medbay. | `req="medbay" lvl="2"` | *"Your haste has paid off…"* → **Accept** → the full payoff, below. |
| d | **(Adv. Clonebay)** Quickly configure the Clonebay to save him. | `req="clonebay" lvl="2"` | *"…he is quickly reconstructed on board your ship."* → **Accept** → the identical payoff. |

### The full payoff (choices c and d, after "Accept.")
> KazaaakplethKilik joins your crew, offers the coordinates for a nearby stash of stolen
> military goods and transmits the coordinates for a custom cruiser he has been working on.
> You forward it to the Federation, sure they can make good use of it.

All in one event body ([[source-events-mantis]]):
- `<unlockShip id="2"/>` — **the Mantis Cruiser**
- `<crewMember amount="1" class="mantis" all_skills="2" id="name_Kazaaak"/>` — a Mantis
  crew member named Kazaaak, at skill level 2 in every skill
- `<augment name="CREW_STIMS"/>` — **Mantis Pheromones** (`aug_CREW_STIMS_title`, +25%
  crew movement speed; [[source-text-blueprints]])
- `<autoReward level="HIGH">scrap_only</autoReward>`
- `<quest event="MANTIS_NAMED_THIEF_STASH"/>` — the stash beacon as well

There is only one choice under c/d ("Accept."), and a developer note in the XML asks
*"Add other options?"* — none were added.

## Blue Options
- **Teleporter** (`req="teleporter"`) — the primary gate. Any teleporter level works.
- **Sensors level 3** (`req="sensors" lvl="3"`) — a full alternative to the teleporter,
  reaching the identical sub-tree. Level 3 sensors are expensive; this is one of the few
  events that pays for them.
- **Medbay level 2** or **Clonebay level 2** — the second gate, and the only way to the
  ship unlock. Either satisfies it, with identical rewards.
- Net requirement for the unlock: (teleporter **or** sensors 3) **and** (medbay 2 **or**
  clonebay 2). Fandom notes you can jump away, buy or upgrade the missing system, and
  return ([[source-fandom-legendary-thief-kazaaakplethkilik]]).

## Rewards & Risks
- Best case: Mantis Cruiser unlock + Kazaaak (skill-2 Mantis) + Mantis Pheromones +
  `HIGH scrap_only` + a stash quest marker.
- Middle case: `HIGH standard` + the stash quest marker.
- Worst case (choice 1 or 'a'): `HIGH standard` and nothing else.
- **The real risk is upstream**, not here: destroying the hull instead of killing the crew
  skips this event entirely and pays only `MED standard`.

## Strategy Notes
- *Opinion:* if you are hunting the Mantis Cruiser, check your systems **before** engaging.
  A boarding party is the natural way to reach `deadCrew`, and it also satisfies the
  teleporter gate — so a teleporter plus a level-2 medbay is the cheapest complete kit.
- If you lack the second gate entirely, take sub-choice 'b': the stash marker is free and
  pays a weapon with high scrap.
- Clonebay 2 counts, so Clonebay ships are not locked out of the unlock.

## Related
- [[event-legendary-thief-kazaaakplethkilik]] — the parent encounter
- [[event-mantis-named-thief-stash]] — the quest marker two of these branches award
- [[chain-mantis-cruiser-unlock]] — the chain this resolves
- [[sector-mantis-homeworlds]] — where the parent appears
- [[entity-mantis]] — the faction
- [[item-mantis-pheromones]] — the augment awarded (`CREW_STIMS`)

## Open Questions
- [ ] Does the `sensors lvl 3` path require *powered* level 3, or just installed?
- [ ] Exact scrap values behind `HIGH standard` and `HIGH scrap_only` here.
- [ ] Does killing the crew with fire/asphyxiation (no teleporter) still allow the sensors
      path to the unlock? The data says yes; unconfirmed in play.

## Sources
- [[source-events-mantis]] (per raw/gamedata/events_mantis.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-fandom-legendary-thief-kazaaakplethkilik]] (per raw/wiki/legendary-thief-kazaaakplethkilik.md)
