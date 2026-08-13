---
id: event-rebel-ship-supplying-civilians
type: event
event_name: REBEL_HELPERS
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [rebel, filler, drone-reward, hull-damage-risk, advanced-edition]
---

# Rebel ship supplying civilians — `REBEL_HELPERS`

## Summary
A Rebel ship running humanitarian supplies to civilian colonies. The event's whole point is
that the Rebels are, for once, the ones helping — and the game offers you the option of
robbing the colonists either instead of or after killing their supplier. There is no reward
for leaving them alone; the only payouts come from taking the supplies.

## Trigger & Where It Appears
- Event lists: `NEUTRAL` and `NEUTRAL_EXIT` in `newEvents.xml`, tagged
  `<!--DLC matt - down below-->` ([[source-newevents]]), plus `OVERRIDE_NEUTRAL` and
  `OVERRIDE_NEUTRAL_EXIT` ([[source-dlceventsoverwrite]]).
- Universal filler / exit pools, so it can appear in any sector that falls back on generic
  neutrals. Fandom scopes it to the two Slug sectors as an exit-and-filler event
  ([[source-fandom-rebel-ship-supplying-civilians]]).
- Not `unique`.
- Beacon: ordinary; no distress flag, no environment.

## Text
`[varies: textList REBEL_HELPERS_TEXT]` — five variants
([[source-newevents]], [[source-text-events-xml]]), all describing Rebels distributing
supplies to civilians in need. One sample:

> Because of the war, thousands of colonists have had their supply lines disrupted and have
> found themselves in dire straits. It seems in this system, the Rebels are sympathetic and
> are distributing what little supplies they can spare.

Fandom lists all five and they match `text_REBEL_HELPERS_TEXT_1` … `_5`
([[source-fandom-rebel-ship-supplying-civilians]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the Rebels. | — | `<ship load="REBEL_HELPERS_SHIP" hostile="true"/>` — see below. | 100% |
| 2 | Wait and steal the supplies from the civilians. *(hidden)* | — | Loads `REBEL_HELPERS_SUPPLIES` — the steal pool, below. | — |
| 3 | Leave them be. | — | `<event/>` — nothing happens. | 100% |

### `REBEL_HELPERS_SHIP`
`auto_blueprint="SHIPS_REBEL"`. **No `<surrender>` and no `<escape>` branch**, so the fight
runs to a conclusion — Fandom notes the same ([[source-fandom-rebel-ship-supplying-civilians]]).

- `destroyed` — *"With the Rebel ship destroyed, you take the time to collect what little
  scrap remains. They had already made their delivery to the civilians."* →
  `autoReward level="LOW"` `standard`.
- `deadCrew` — *"With the Rebel crew dead, you strip their ship for equipment. They had
  already made their delivery to the civilians."* → `autoReward level="MED"` `standard`.

Either ending then offers two hidden choices:
- **"Steal the civilian supplies."** → `REBEL_HELPERS_SUPPLIES` (same pool as choice 2).
- **"Leave the civilians alone."** → `REBEL_HELPER_NO_SUPPLIES`, whose text is itself a
  four-variant list and which has **no mechanical effect** — all four variants are the
  colonists telling you what you have cost them. Sample:

  > Before your FTL drive charges, you receive a hail: "My son was on that ship. He only
  > helped the Rebels because they cared enough to help us. Without him to find us
  > supplies, we'll likely be forgotten and die out here."

### `REBEL_HELPERS_SUPPLIES` — the steal pool
Four distinct entries. **Assuming uniform selection across list entries**, each is 1/4:

| # | Text | Effect |
|---|------|--------|
| 1 | *"…mostly equipment meant for automated farming, but you can make use of it. … 'This is why the Rebels will always have support!'"* | `autoReward level="LOW"` **`droneparts`** |
| 2 | *"…you crack it open and discover nothing more than vaccinations for a local plague."* | Nothing. |
| 3 | *"You make the colonists teleport the supplies to your ship. It's nothing more than building construction supplies. Oh well, scrap is scrap."* | `autoReward level="LOW"` `scrap_only` |
| 4 | *"The colonists willingly give up their supplies. But as you make to jump away, an explosion rocks your ship. The cargo was booby trapped!"* | `<damage amount="2" system="room" effect="random"/>` |

([[source-newevents]], [[source-text-events-xml]]) Derived from list contents, not a stated
percentage.

> ⚠️ **CONTRADICTION:** the booby-trap damage.
> - Game files: a single `<damage amount="2" system="room" effect="random"/>` — 2 damage to
>   one random room, with a random fire/breach effect ([[source-newevents]]).
> - Fandom: *"Your ship takes 2 hull damage, 2 damage with a random effect to a random
>   room"* ([[source-fandom-rebel-ship-supplying-civilians]]).
>
> Trusting the game files for what is written. As with
> [[event-pirate-ship-selling-drones]], Fandom's extra "hull damage" line is most likely
> its rendering of system damage also costing hull, not a second XML entry.

Fandom also reads the `LOW` `droneparts` reward as exactly **1 drone part**
([[source-fandom-rebel-ship-supplying-civilians]]); the game files only say `LOW`.

## Blue Options
None — no `req`-gated choices anywhere in the tree.

## Rewards & Risks
- Stealing without fighting (choice 2) is free: 3/4 of the outcomes are neutral-to-good,
  1/4 costs you 2 room damage plus a fire or breach.
- Fighting first adds `LOW` (destroyed) or `MED` (dead crew) `standard` on top, at the cost
  of a no-surrender, no-escape Rebel fight.
- Leaving them be pays nothing at all.

## Strategy Notes
- *(Opinion, from the tree shape.)* Choice 2 is the efficient line if you do not want a
  fight — it reaches the same reward pool as the post-combat steal without any combat.
- If you do fight, always take "Steal the civilian supplies" afterwards: the alternative
  branch is pure flavour with no effect.
- Killing the crew rather than destroying the ship upgrades the reward from `LOW` to `MED`,
  so boarding parties are worth more here than usual.

## Related
- [[event-rebel-checkpoint]] — the other Rebels-and-civilians filler event from the same
  DLC batch
- [[event-rebel-fight-chance]] — the third of the batch
- [[entity-rebels]]

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Exact drone-part count behind `autoReward level="LOW"` `droneparts` (Fandom says 1).
- [ ] Whether the booby trap also costs hull, per the contradiction above.
- [ ] The full sector reach of `NEUTRAL` / `NEUTRAL_EXIT` placement.

## Sources
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-fandom-rebel-ship-supplying-civilians]] (per `raw/wiki/rebel-ship-supplying-civilians.md`)
