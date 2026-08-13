---
id: entity-pirates
type: entity
entity_kind: faction
hostility: hostile
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [faction, reskin, mixed-crew, slavers, ambush]
---

# Pirates

## Summary
Pirates are **not a species and have no ships of their own**. Mechanically they are a
relabelling layer: thirteen other factions' hulls, re-imaged with pirate art, renamed
"Pirate ⟨whatever⟩", and crewed by a random draw from six species. That single fact explains
most of how pirate encounters feel — a "Pirate Interceptor" fights exactly like a
[[entity-slugs]] Slug Interceptor, right down to its Slug Repair Gel.

They are also the game's most *situational* faction: they have one sector of their own, but
pirate events (tolls, ambushes, slavers, fake distress calls, salesmen) appear throughout the
map.

## Traits / Stats

### The reskin system
`autoBlueprints.xml` defines `SHIPS_PIRATE` as a list of `_P`-suffixed blueprints, each of
which lives in `dlcPirateBlueprints.xml` and is a copy of a faction hull with three changes:
a pirate `img`/`layout`, a "Pirate …" class name, and `crewCount class="random"` in place of
the species class ([[source-autoblueprints]], [[source-dlcpirateblueprints]],
[[source-text-blueprints]]).

| Pirate blueprint | Copied from | Pirate class name |
|---|---|---|
| `JELLY_BUTTON_P` | [[entity-slugs]] Slug Interceptor | Pirate Interceptor |
| `JELLY_CROISSANT_P` | Slug Light-Cruiser | Pirate Light-Cruiser |
| `JELLY_TRUFFLE_P` | Slug Assault | Pirate Assault |
| `REBEL_FAT_P` | [[entity-rebels]] Rebel Rigger | Pirate Rigger |
| `REBEL_SKINNY_P` | Rebel Fighter | Pirate Fighter |
| `ROCK_SCOUT_P` | [[entity-rock-men]] Rock Scout | Pirate Scout |
| `ROCK_FIGHT_P` | Rock Fighter | Pirate Fighter |
| `MANTIS_SCOUT_P` | [[entity-mantis]] Mantis Scout | Pirate Scout |
| `MANTIS_FIGHTER_P` | Mantis Fighter | Pirate Fighter |
| `MANTIS_BOMBER_P` | Mantis Bomber | Pirate Bomber |
| `FED_SCOUT_P` | [[entity-federation]] Federation Scout | Pirate Scout |
| `FED_BOMBER_P` | Federation Bomber | Pirate Bomber |
| `ZOLTAN_FIGHTER_P` | [[entity-zoltan]] Energy Fighter | Pirate Fighter |

Each also has a `_P_DLC` variant carrying that faction's Advanced Edition changes (clonebays,
hacking, mind control) — e.g. `REBEL_FAT_P_DLC` is *Pirate Disruptor* with a clonebay and
hacking ([[source-dlcpirateblueprints]], [[source-text-blueprints]]).

**Pirate ships keep the donor faction's augment.** `ROCK_*_P` still carry `ROCK_ARMOR`,
`JELLY_*_P` still carry `SLUG_GEL`, `ZOLTAN_FIGHTER_P` still carries `ENERGY_SHIELD`. Read
the pirate ship's *hull name in the class string* to know what you are actually facing.

### Pirate crew — `class="random"`
Random pirate crew are drawn from `CREW_RANDOM` ([[source-autoblueprints]]):

> `mantis` · `rock` · `engi` · `energy` (Zoltan) · `human` · `slug`

**Excluded: `crystal` and `anaerobic`.** You will never meet a Crystal or Lanius pirate, and
there are no `CRYSTAL_*_P` or `ANAEROBIC_*_P` blueprints
([[source-dlcpirateblueprints]]). See [[entity-crystal-men]], [[entity-lanius]].

Consequences worth carrying into a fight: a pirate crew can be six 150-HP fire-immune
Rockmen, or six 70-HP Zoltan, or any mix. You cannot predict boarding strength from the hull.

> ⚠️ **Data oddities in `SHIPS_PIRATE`** ([[source-autoblueprints]]):
> - A commented-out `P_REPLACE` version of the list sits directly above the live one. It
>   uses the **un-reskinned** hulls and additionally lists `ANAEROBIC_BOMBER` and
>   `ANAEROBIC_SCOUT`. The live list has neither.
> - `ZOLTAN_BOMBER_P` is fully defined but is **not** in the live `SHIPS_PIRATE` — it is
>   reachable only via `SHIPS_ZOLTAN_PIRATE`.
> - Separate per-faction pirate lists also exist: `SHIPS_ROCK_PIRATE`,
>   `SHIPS_ZOLTAN_PIRATE`, each with its own commented-out `P_REPLACE` predecessor.

## Where They Appear
- [[sector-pirate-controlled-sector]] (`PIRATE_SECTOR`, `minSector` 0) — every list is the
  `_PIRATE` variant: `STORE_PIRATE`, `HOSTILE_PIRATE`, `BOARDERS_PIRATE`,
  `DISTRESS_BEACON_PIRATE`, `NEBULA_PIRATE`, `NOTHING_PIRATE`, `QUESTS_PIRATE`,
  `NEUTRAL_PIRATE` ([[source-sector-data-xml]]).
- **Everywhere else**, via pirate events embedded in other sectors' pools — the Rock sector
  has its own `SHIPS_ROCK_PIRATE` encounters, the Zoltan sector its own, and generic pirate
  ambush/toll/slaver events appear in civilian and Federation space.

## Events Involving Them

**Pirate-sector furniture**
- [[event-start-beacon-pirate]] · [[event-empty-beacon-pirate]] · [[event-store-pirate]]

**Ambushes and straight fights**
- [[event-pirate-fight]] · [[event-pirate-fight-in-nebula]] ·
  [[event-pirate-fight-choice-in-nebula]] · [[event-pirate-fight-in-asteroid-field]] ·
  [[event-pirate-fight-near-sun]] · [[event-pirate-fight-near-pulsar]] ·
  [[event-pirate-ships-in-plasma-storm]]
- Faction-flavoured variants: [[event-pirate-fight-engi]] · [[event-pirate-fight-lanius]] ·
  [[event-pirate-fight-slug]] · [[event-pirate-fight-zoltan]]
- Rock-sector pirates: [[event-rock-pirates-fight]] ·
  [[event-rock-pirates-fight-in-asteroid-field]] · [[event-rock-pirates-fight-near-sun]]

**Traps and shakedowns — the pirate signature**
- [[event-pirate-toll]] · [[event-pirate-briber]] · [[event-pirate-engine-hacker]] ·
  [[event-pirate-smuggler]] · [[event-pirate-ship-distress-trap]] ·
  [[event-refugee-distress-pirate]] · [[event-refugee-pirate]] · [[event-abandoned-station]]
- [[event-boarders-humans-pirate]] · [[event-boarders-humans-near-sun]] ·
  [[event-boarders-humans-jammed-sensors]] · [[event-boarders-asteroid]] ·
  [[event-capture-the-ship]] · [[event-quest-crewdead]]

**Slavers**
- [[event-slaver-friendly]] · [[event-slaver-hostile]]

**Pirates as merchants**
- [[event-pirate-ship-selling-drones]] · [[event-pirate-ship-selling-weapon]] ·
  [[event-dock-bomb-salesman]] · [[event-dock-drone-salesman]] ·
  [[event-merchant-investigate]] · [[event-the-mercenary]] ·
  [[event-settlement-mercenary-work]] · [[event-remote-settlement]]

**Pirates preying on others**
- [[event-pirate-ship-attacking-civilian]] · [[event-pirate-ship-attacking-civilian-distress]] ·
  [[event-pirate-ship-attacking-civilian-lanius]] · [[event-pirate-ship-attacking-crystal]] ·
  [[event-destroyed-cargo-ship]] · [[event-refueling-platform]] · [[event-crushed-pirate]] ·
  [[event-pirate-surrender-civilan]] · [[event-refugee]] · [[event-refugee-distress]] ·
  [[event-refugee-slug]] · [[event-refugee-distress-slug]] · [[event-slug-comm-tapping]] ·
  [[event-no-fuel-refugee-pirate]]

### Blue options gated on Pirates
None. There is no `req="pirate"` — you can never be one.

## How To Fight / Deal With Them
- **Read the class name.** "Pirate Interceptor" = Slug hull with `SLUG_GEL` (breach weapons
  wasted). "Pirate Scout" is ambiguous — it maps to three different donor hulls (Rock,
  Mantis, Federation) with different augments and weapon pools. The visible name does not
  fully disambiguate; the augment behaviour will.
- **Assume mixed crew.** `CREW_RANDOM` means the boarding party you kill on one pirate ship
  tells you nothing about the next. Fire is a coin-flip: Rockmen are immune, everyone else
  is not.
- Mantis-hull pirates carry teleporters (two of the three with them powered at spawn) — the
  same boarding threat as [[entity-mantis]] proper.
- Zoltan-hull pirates arrive behind a **Zoltan super shield**.
- No pirate hull is Crystal or Lanius, so you will never face crystal weapons or an
  oxygen-draining boarding party from a pirate.

## Related
- [[entity-slugs]], [[entity-rock-men]], [[entity-mantis]], [[entity-zoltan]],
  [[entity-rebels]], [[entity-federation]] — the six donor factions
- [[entity-crystal-men]], [[entity-lanius]] — explicitly excluded from the pirate system
- [[sector-pirate-controlled-sector]]

> **Naming note.** Event pages also link pirates as `entity-pirate` and
> `entity-pirate-ships`; both resolve conceptually to this page.

## Open Questions
- [ ] Whether `ZOLTAN_BOMBER_P`'s absence from the live `SHIPS_PIRATE` list is intentional.
- [ ] Whether `class="random"` rolls once per ship or per crew member.
- [ ] Whether the pirate reskin system exists in vanilla at all — the `_P` blueprints live in
      `dlcPirateBlueprints.xml`, but `autoBlueprints.xml`'s commented-out `P_REPLACE` blocks
      suggest the pre-reskin behaviour was to use the donor hulls unchanged. This page is
      tagged `version: both` on the strength of the live list; the vanilla presentation is
      unconfirmed.

## Sources
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-dlcpirateblueprints]] (per raw/gamedata/dlcPirateBlueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
