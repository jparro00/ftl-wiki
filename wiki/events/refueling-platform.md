---
id: event-refueling-platform
type: event
event_name: FUELING_STATION
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: any
hostile: false
blue_options: [[[item-doors]]]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [fuel, filler, unique, blue-option, boarding-risk, hull-damage, fire, fuel-loss, pirate, ae]
---

# Refueling platform — `FUELING_STATION`

## Summary
A fuel vendor that is a coin flip between an honest station and a pirate trap. Docking
loads one of two sub-pools with equal weight: the "normal" pool offers fuel for scrap, for
free, or from a station that might explode; the "pirate" pool is an ambush both times, one
of which a level-2 Door System converts into free fuel. Ignoring the platform is not
entirely safe either — one entry in three stages a pirate fight anyway. The single best
fuel event in the Advanced Edition neutral pool, and the one most likely to cost you an
engine room.

## Trigger & Where It Appears
- **Advanced Edition content.** The event lives in the `DLC!!!` block of `newEvents.xml`,
  and every list entry that loads it is annotated `<!--DLC-->` ([[source-newevents]]).
- Lists it belongs to:
  - `NEUTRAL` and `NEUTRAL_EXIT` in `newEvents.xml` ([[source-newevents]])
  - `OVERRIDE_NEUTRAL` and `OVERRIDE_NEUTRAL_EXIT` in `dlcEventsOverwrite.xml`, which
    replace those two lists when the DLC is enabled ([[source-dlceventsoverwrite]])
  - `NEUTRAL_ENGI`, the Engi-specific neutral list ([[source-events-engi]])
- `sector_data.xml` allocates `NEUTRAL_ENGI` in the Engi Controlled Sector (4–6) and Engi
  Homeworlds (5–7), and names `NEUTRAL` explicitly only in Slug Home Nebula and Slug
  Controlled Nebula (1–2 each) ([[source-sector-data-xml]]).
- `NEUTRAL` / `OVERRIDE_NEUTRAL` is additionally the **hardcoded fill-in list** — its XML
  comment reads *"This event list is hardcoded to fill out a sector if it ran out of all
  other calls for that sector"* — so the event can appear in any sector with unallocated
  beacons. [[source-fandom-refueling-platform]] lists the Abandoned Sector for exactly
  this reason: that sector allocates only `STORE` (2–4) and nothing else, so the rest of
  its beacons fall through to the filler list.
- The `*_EXIT` memberships put it on exit beacons too.
- Beacon: ordinary/filler; no ship staged, so it starts non-hostile.
- `unique="true"` — at most once per run.

## Text
> A small platform orbits near this beacon - it looks like a fueling station of some sort,
> and it is cheerily broadcasting reasonable prices in a spectrum of frequencies and
> languages.

(`event_FUELING_STATION_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Dock with the refueling platform. | — | Loads `eventList FUELING_STATION_LIST`, a two-member list of *other lists*: `FUELING_STATION_NORMAL_LIST` and `FUELING_STATION_PIRATE_LIST`. | 1/2 each pool |
| 2 | Ignore the refueling platform. | — | Loads `eventList FUELING_STATION_IGNORE` (3 entries): one stages a `PIRATE` fight, two are empty. | 1/3 fight, 2/3 nothing |

All fractions on this page **assume uniform selection across list entries**; no source
states a percentage. They are derived from list membership only ([[source-newevents]]).

### Ignoring — `FUELING_STATION_IGNORE`
| # | Prose | Effect |
|---|-------|--------|
| 1 | *"As you prepare to leave the system, a Pirate ship suddenly appears on scanners - it looks like it was attempting to use the platform as bait!"* | `ship load="PIRATE" hostile="true"`, default rewards. |
| 2–3 | *(no text, no effect)* | Nothing happens. |

Fandom marks the nothing outcome `{{DuplicateEvent|2}}`, independently observing the two
empty entries ([[source-fandom-refueling-platform]]).

### Docking, honest pool — `FUELING_STATION_NORMAL_LIST` (3 entries)

**N1 — *"The platform makes an offer."***

| Choice | Outcome |
|--------|---------|
| Accept it. | −5 to −10 scrap, **+5 fuel**. |
| Reject it. | Nothing. |

**N2 — *"The automated platform seems to be damaged. You can likely steal as much fuel as remains."***

| Choice | Outcome |
|--------|---------|
| Steal it. *(hidden)* | *"If you take the fuel at least it won't fall into the hands of the Rebels…"* → **+3 to +5 fuel**, free. |
| War doesn't justify abandoning one's values. You leave it alone. | Nothing. |

**N3 — *"The platform seems to be malfunctioning and could ignite at any moment."***

| Choice | Outcome |
|--------|---------|
| Quickly dock and refuel. *(hidden)* | Loads `FUELING_STATION_BLOW` (2 entries): (a) *"You're able to safely refuel and get clear before the station explodes."* → **+5 fuel**; (b) *"Just as you hook up to refuel, the station ignites and explodes…"* → **−3 fuel** (`item_modify steal="true"`) and `damage amount="3" system="engines" effect="fire"`. **1/2 each.** |
| Give the station a wide berth and carry on. | Nothing. |

### Docking, pirate pool — `FUELING_STATION_PIRATE_LIST` (2 entries)

**P1 — *"You dock and signal the fuel station's staff to begin refueling."*** Both options
are `hidden="true"`; without Doors 2 only the first is offered.

| Choice | Requirement | Outcome |
|--------|-------------|---------|
| Wait for them to finish. | — | *"…there is an explosion from your engine room! …pirates from the station swarm aboard your vessel!"* → `damage amount="3" system="engines"` and `boarders min="2" max="4" class="random"`. |
| **(Blast Doors)** Seal your blast doors, one can never be too careful when docked. | `req="doors" lvl="2"` | *"Pirates hidden on the station are confounded by your security locks…"* → **+5 fuel**, no damage, no boarders. |

**P2 — *"The refueling station welcomes you into one of its berths… you detect a Pirate
Ship closing fast!"*** → `ship load="PIRATE" hostile="true"` **and**
`damage amount="3" system="engines"`. No choice; you start the fight already damaged.

## Blue Options
- **[[item-doors]] level 2** (`req="doors" lvl="2"`) — the single best blue option in the
  event. On outcome P1 it converts *3 engine damage plus 2–4 boarders* into *+5 fuel with
  no cost*. That is a full swing from the worst survivable outcome to the best one, on
  1/4 of all docks (1/2 pirate pool × 1/2 of that pool).

## Rewards & Risks
- **Fuel:** +5 (paid, N1), +3 to +5 (free, N2), +5 (gamble, N3a), +5 (blue option, P1).
  Fuel is the whole point of the event.
- **Fuel loss:** −3 on N3b.
- **Scrap cost:** only on N1 (−5 to −10), and only if you accept.
- **Damage:** every hostile branch attacks the **engines** specifically —
  `damage amount="3" system="engines"` on P1-wait and P2, and the same with
  `effect="fire"` on N3b. Losing engines is losing your ability to run.
- **Boarders:** 2–4, `class="random"` (any species), on P1-wait.
- **Fights:** `PIRATE` on P2 and on the ignore branch. Per `events_ships.xml` that ship has
  `surrender chance="0.5" min="3" max="4"` and `escape chance="0.5" min="2" max="4"`, with
  default destroyed/deadCrew rewards ([[source-events-ships]]).

> ⚠️ **CONTRADICTION:** the hull-damage figures.
> - Game files: a single tag per branch — `<damage amount="3" system="engines"/>`, and on
>   N3b `<damage amount="3" system="engines" effect="fire"/>`. No separate hull damage is
>   written ([[source-newevents]]).
> - Fandom: *"Your ship takes 3 hull damage, 3 damage with fires to engines, and lose 3
>   fuel"* — i.e. it reads the same tag as dealing hull damage **and** system damage, plus
>   1–2 fires ([[source-fandom-refueling-platform]]).
>
> This is almost certainly engine behaviour rather than a disagreement about the data:
> FTL's `damage` tag with a `system` attribute does both, and the fires come from
> `effect="fire"`. But **no file in `raw/gamedata/` states it**, so the wiki's figure is an
> interpretation, not a datamined value. Trusting the game files for *what is written* and
> Fandom for *what a player sees*; both are recorded rather than resolved.

> ⚠️ **CONTRADICTION:** minor wording. Game files: *"losing **you** precious fuel and
> damaging your ship"* ([[source-text-events-xml]]). Fandom: *"losing **your** precious
> fuel"* ([[source-fandom-refueling-platform]]). The game files contain the typo; the wiki
> silently corrected it. Trusting the game files as the literal in-game string.

## Strategy Notes
- Docking is the right call whenever you are short on fuel: three of the five docking
  scenarios hand you fuel, and one of the two bad ones is neutralised by Doors 2.
- With **Doors level 2** the event is close to strictly positive — the only remaining
  unavoidable punishment is P2, at 1/4 of docks.
- Ignoring is *not* free: 1/3 of ignores stage a pirate fight anyway, and you get no fuel
  for it. If you were going to risk the fight regardless, dock.
- The damage always lands on engines. If your engines are already down or your evasion is
  carrying the run, the calculus shifts toward ignoring. (Opinion, reasoned from the
  outcome table; no source ranks this event.)

## Related
- [[event-refueling-platform-garbled-broadcast]] — `LANIUS_FUELING_STATION`, the Lanius
  sector's near-identical rework of this beacon
- [[event-abandoned-station]] — the other AE filler station event in the same file
- [[event-confused-mantis]] — same file, same Engi neutral list
- [[item-doors]], [[entity-pirates]]
- [[concept-blue-options]]
- [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]

## Open Questions
- [ ] Whether `eventList` selection is uniform (every fraction here depends on it).
- [ ] Whether the engine `damage` tags also deal hull damage, and how many fires
      `effect="fire"` starts — Fandom says 3 hull and 1–2 fires; no game file says so.
- [ ] The `FUELING_STATION_BLOW` reference is written `<event name="FUELING_STATION_BLOW"/>`
      inside the choice rather than `load=`, while the target is an `<eventList>` of the
      same name. Fandom documents both list outcomes as reachable, so it evidently
      resolves — but the attribute is inconsistent with every other reference in the file.
- [ ] Numeric scrap value of the `PIRATE` default rewards.

## Sources
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-refueling-platform]] (per raw/wiki/refueling-platform.md)
