---
id: event-legendary-thief-kazaaakplethkilik
type: event
event_name: MANTIS_NAMED_THIEF
sectors: [[[sector-mantis-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: [[[item-teleporter]], [[item-sensors]], [[item-medbay]], [[item-clone-bay]], mantis crew]
chain: [[[chain-mantis-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [ship-unlock, unique, guaranteed, blue-option, quest-marker, crew-reward, augment-reward, mantis]
---

# Legendary thief KazaaakplethKilik — `MANTIS_NAMED_THIEF`

## Summary
The [[chain-mantis-cruiser-unlock]] beacon, and a guaranteed one: `sector_data.xml`
allocates `MANTIS_NAMED_THIEF` at `min=1 max=1` in [[sector-mantis-homeworlds]]
([[source-sector-data-xml]]). You fight a heavily armoured Mantis ship, and **how** you
win decides everything — destroy the hull and you get medium scrap and nothing else;
kill the crew and you open a branching aftermath that can yield the Mantis Cruiser
unlock, the [[item-mantis-pheromones]] augment, a fully-trained Mantis crew member, high
scrap, and a quest marker to a weapon cache. The full payout needs a
[[item-teleporter]] **or** level-3 [[item-sensors]], *plus* a level-2 [[item-medbay]] or
level-2 [[item-clone-bay]].

## Trigger & Where It Appears
- Sector: [[sector-mantis-homeworlds]] **only** — `<event name="MANTIS_NAMED_THIEF" min="1" max="1"/>`
  in the `MANTIS_HOME` sector description ([[source-sector-data-xml]]). It is guaranteed
  once per Mantis Homeworlds sector.
- Not in `MANTIS_SECTOR` (the ordinary Mantis Controlled Sector) — only the homeworlds.
- `unique="true"`, with an in-file developer note reading
  `NOTE - make globally unique` ([[source-events-xml]]).
- Long-range scanners show a ship ([[source-fandom-legendary-thief-kazaaakplethkilik]]).
- **You can come back.** Fandom notes that if you reach the beacon without the systems the
  blue options need, you may jump away, buy or upgrade them, and return to finish the
  quest ([[source-fandom-legendary-thief-kazaaakplethkilik]]). This is not stated in the
  game files.

## Text
> You cross paths with a Mantis ship that looks to have had dozens of layers of
> armor-plating added over what must have been a hundred year career. Its captain is
> legendary thief KazaaakplethKilik. Your crew look frightened.

(`event_MANTIS_NAMED_THIEF_text`, per [[source-text-events-xml]])

## Choices & Outcomes

Both choices lead to the same fight. The Mantis-crew option is pure flavour.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | **(Mantis crewmember)** Attempt to hail him. | `req="mantis"` | *"Your Mantis crew-member steps forward. He and KazaaakplethKilik perform a weird kind of alien haka. You, meanwhile, charge the battle systems."* → ship turns hostile. | 100% |
| 2 | Prepare to fight. | — | Ship turns hostile, no extra text. | 100% |

### The fight
`<ship name="MANTIS_NAMED_THIEF" auto_blueprint="SHIPS_MANTIS">`, carrying an in-file
note `NEEDS ELITE TAG - need an escape/surrender`. As shipped it has **no surrender and
no escape branch** ([[source-events-xml]], per `raw/gamedata/events_ships.xml`). Fandom
confirms: no surrender, no escape ([[source-fandom-legendary-thief-kazaaakplethkilik]]).
Fandom also states the crew is entirely Mantis; the ship definition specifies no `<crew>`
block, so that composition comes from the `SHIPS_MANTIS` auto-blueprint and is **not**
independently confirmed in the files read here.

Two ways to win, and they are **not** equivalent:

**(A) Destroy the ship** → `<destroyed>`:
> KazaaakplethKilik fights to the last, and you pick the scraps from the corpse of his
> ship. You sense, though, that his death has left a great mystery unresolved.

Payload: `autoReward level="MED"` `standard`. **Nothing else.** The chain ends here — no
unlock, no augment, no crew, no quest marker.

**(B) Kill the crew** → `<deadCrew load="MANTIS_NAMED_THIEF_DEFEAT"/>` → the aftermath
tree below. This is the only path to the ship unlock.

## Aftermath — `MANTIS_NAMED_THIEF_DEFEAT`

Loaded from the ship's `deadCrew` branch, so it is documented here rather than on its own
page. It is not reachable from any sector event list.

> No more life signs are detected aboard their ship. You appear to have won.

| # | Choice | Requirement | Outcome | Reward |
|---|--------|-------------|---------|--------|
| 1 | Move in to strip their ship. | — | *"It seems almost a waste for such a fierce foe to die in such an anticlimactic fashion. You shrug it off and take what you can."* | `autoReward level="HIGH"` `standard` — **ends the chain** |
| 2 | **(Teleporter)** Quickly teleport additional crew and check for survivors. | `req="teleporter"` | *"You find KazaaakplethKilik slumped in a corner dying."* → four sub-choices | see below |
| 3 | **(Sensors)** Quickly scan their ship for survivors. | `req="sensors" lvl="3"` | *"You detect KazaaakplethKilik slumped in a corner dying."* → the same four sub-choices | see below |

Choices 2 and 3 are functionally identical — different gates, identical sub-tree
([[source-events-xml]]):

| Sub-choice (teleporter wording / sensors wording) | Requirement | Reward |
|---|---|---|
| "Put him out of his misery." / "Let him die." | — | `autoReward level="HIGH"` `standard`. Chain ends. |
| "Listen to what he has to say." / "Dock and try to speak with him." | — | `autoReward level="HIGH"` `standard` **and** `<quest event="MANTIS_NAMED_THIEF_STASH"/>` — a quest marker is added to your map. Chain ends with the stash but **no ship unlock**. |
| **(Adv. Medbay)** "Quickly teleport him back to the medbay." / "Dock and quickly take him back to the medbay." | `req="medbay" lvl="2"` | → *Save the thief* (below) |
| **(Adv. Clonebay)** "Quickly configure the Clonebay to save him." | `req="clonebay" lvl="2"` | → *Save the thief* (below) |

### Save the thief — the full payout
Medbay version:
> Your haste has paid off and you are able to bring him back from the brink of death.
> When his senses return he says, "I never thought I would see this day, but... I am
> willing to devote myself and my ships to your cause."

Clonebay version:
> Your haste has paid off and you register him into the Clonebay's database. After he
> passes away he is quickly reconstructed on board your ship. When his senses return he
> says, "I never thought I would see this day, but... I am willing to devote myself and
> my ships to your cause."

One further choice, **Accept**:
> KazaaakplethKilik joins your crew, offers the coordinates for a nearby stash of stolen
> military goods and transmits the coordinates for a custom cruiser he has been working
> on. You forward it to the Federation, sure they can make good use of it.

Payload, verbatim from the file ([[source-events-xml]]):
- `<augment name="CREW_STIMS"/>` — the [[item-mantis-pheromones]] augment
  (`aug_CREW_STIMS_title` = "Mantis Pheromones", `aug_CREW_STIMS_desc` = "Your crew's
  movement speed is increased by 25 percent." — [[source-text-blueprints]], per
  `raw/gamedata/text_blueprints.xml`)
- `<autoReward level="HIGH">scrap_only</autoReward>` — **scrap only**, not scrap-with-resources
- `<crewMember amount="1" class="mantis" all_skills="2" id="name_Kazaaak"/>` — a Mantis
  crew member named **Kazaaak** (`name_Kazaaak` = "Kazaaak", [[source-text-events-xml]])
  with every skill at level 2
- `<quest event="MANTIS_NAMED_THIEF_STASH"/>` — quest marker → [[event-mantis-named-thief-stash]]
- `<unlockShip id="2"/>` — the ship unlock

> **Note on the unlock:** the game file says only `unlockShip id="2"`. Fandom identifies
> that as the [[entity-mantis-cruiser]] (Layout A)
> ([[source-fandom-legendary-thief-kazaaakplethkilik]]). Corroborating but not proof: the
> `PLAYER_SHIP_MANTIS` blueprint carries `<aug name="CREW_STIMS"/>` — the same augment
> this event awards ([[source-blueprints]], per `raw/gamedata/blueprints.xml`). The
> id→ship mapping itself is not stated anywhere in the extracted files.
>
> Fandom additionally claims the Mantis Cruiser can be unlocked by winning the game with
> the Zoltan Cruiser. `achievements.xml` contains no unlock-condition entry supporting
> this, so it is recorded as **Fandom-only, unverified**.

> ⚠️ **CONTRADICTION (minor):** "maxed in all skills".
> - Fandom: *"Mantis crewmember named Kazaaak maxed in all skills"*
>   ([[source-fandom-legendary-thief-kazaaakplethkilik]])
> - Game files: `all_skills="2"` ([[source-events-xml]])
>
> These are probably the same statement — level 2 appears to be the top skill tier — but
> the files say "2", not "max". Recorded as the raw value; whether 2 is the cap is an
> open question, not something to assert.

## Blue Options
- **Mantis crew member** (`req="mantis"`, on the parent event) — unlocks a flavour hail
  before the fight. **No mechanical benefit.** Both choices set `<ship hostile="true"/>`
  and nothing else.
- **[[item-teleporter]]** (`req="teleporter"`, aftermath) — opens the survivor branch.
  No level requirement, just the system.
- **[[item-sensors]]** at level 3 (`req="sensors" lvl="3"`, aftermath) — the alternative
  gate to the identical survivor branch.
- **[[item-medbay]]** at level 2 (`req="medbay" lvl="2"`) — inside the survivor branch,
  the path to the ship unlock.
- **[[item-clone-bay]]** at level 2 (`req="clonebay" lvl="2"`) — identical alternative to
  the Medbay path.

The unlock therefore needs **two** gates satisfied at once: (teleporter OR sensors 3) AND
(medbay 2 OR clonebay 2).

## Rewards & Risks
Best-to-worst, by path:

| Path | Reward |
|---|---|
| Kill crew → teleporter/sensors → medbay/clonebay → Accept | Ship unlock, [[item-mantis-pheromones]], Kazaaak (all skills 2), HIGH `scrap_only`, quest marker to [[event-mantis-named-thief-stash]] |
| Kill crew → teleporter/sensors → "listen"/"speak" | HIGH `standard` + quest marker |
| Kill crew → strip the ship, or "put him out of his misery"/"let him die" | HIGH `standard` |
| Destroy the ship | MED `standard`, chain over |

Risks:
- **No surrender, no escape branch on the enemy ship.** Once committed, you fight it out.
- The ship is described in-fiction as heavily armoured and is the sector's set-piece
  encounter.
- Destroying it by accident — e.g. with a strong weapon loadout and no boarding party —
  silently forfeits the entire unlock. This is the single most expensive mistake available
  at this beacon.

## Strategy Notes
- *(Opinion.)* Plan the win condition before you engage. The unlock requires killing
  crew, not hull, which in practice means boarders, a Fire Beam / anti-personnel approach,
  or venting — not a hull-race.
- *(Opinion.)* A [[item-teleporter]] does double duty here: it satisfies the aftermath
  gate **and** is the most reliable way to produce a dead-crew win in the first place.
  Level-3 [[item-sensors]] satisfies only the gate, not the win condition.
- Because the beacon is guaranteed in [[sector-mantis-homeworlds]], the systems can be
  bought for it deliberately — and Fandom confirms you may leave and come back
  ([[source-fandom-legendary-thief-kazaaakplethkilik]]).
- Note the full payout gives `scrap_only` at HIGH, whereas the lesser branches give
  `standard` at HIGH. `standard` includes fuel/missiles/drone parts; `scrap_only` does not
  — so the "best" branch is not strictly dominant on resources, only on everything else.

## Related
- [[chain-mantis-cruiser-unlock]] — this beacon plus its quest-marker follow-up
- [[event-mantis-named-thief-stash]] — the quest marker, `MANTIS_NAMED_THIEF_STASH`
- [[entity-mantis-cruiser]] — the ship this unlocks
- [[item-mantis-pheromones]] — the `CREW_STIMS` augment awarded
- [[item-teleporter]], [[item-sensors]], [[item-medbay]], [[item-clone-bay]]
- [[event-mantis-fight]] — the ordinary Mantis fight, a different ship definition
- [[sector-mantis-homeworlds]]
- [[event-mantis-named-thief-defeat]] — the `MANTIS_NAMED_THIEF_DEFEAT` aftermath, written up in full on its own page

## Open Questions
- [ ] Confirm `unlockShip id="2"` is the Mantis Cruiser — the mapping is not in the files.
- [ ] Is skill level 2 the cap (i.e. is Fandom's "maxed" exact)?
- [ ] Does the Zoltan-Cruiser-victory unlock path exist? Not in `achievements.xml`.
- [ ] Crew composition of the `MANTIS_NAMED_THIEF` ship — the `SHIPS_MANTIS` auto-blueprint
      has not been read.
- [ ] Numeric values behind HIGH `standard` vs HIGH `scrap_only`.
- [ ] Fandom's "jump away, upgrade, come back" claim is untested against the files.

## Sources
- [[source-events-xml]] (per raw/gamedata/events_mantis.xml, raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-fandom-legendary-thief-kazaaakplethkilik]] (per raw/wiki/legendary-thief-kazaaakplethkilik.md)
