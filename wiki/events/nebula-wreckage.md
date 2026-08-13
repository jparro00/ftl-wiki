---
id: event-nebula-wreckage
type: event
event_name: NEBULA_BATTLEFIELD
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: false
blue_options: [slug crew, medbay lvl 2, clonebay]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, blue-option, crew-reward, quest-marker, hull-damage-risk, fire-risk, dlc]
---

# Nebula wreckage — `NEBULA_BATTLEFIELD`

## Summary
A non-hostile unique nebula beacon in Slug space. Poking through the debris can cost you
hull and start a fire, but it can also turn up a dying survivor — who is worth either a
free crew member (with an upgraded Medbay or a Clone Bay) or a quest marker leading to
[[event-secret-word-abadoth]]. A Slug crew member skips the search entirely and goes
straight to the survivor.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — via the
  `NEBULA_NEUTRAL_SLUG` event list (`min 3 / max 5` beacons per sector)
  ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: nebula (`<environment type="nebula"/>`), non-hostile, `unique="true"`
- Marked `<!--DLC - Below-->` in the event list — Advanced Edition content
  ([[source-events-slug]])

> ⚠️ **CONTRADICTION:** where the event can appear.
> - Game files: `NEBULA_BATTLEFIELD` is listed **only** in `NEBULA_NEUTRAL_SLUG`, and
>   that list is drawn on only by `SLUG_SECTOR` and `SLUG_HOME`
>   ([[source-events-slug]], [[source-sector-data-xml]]).
> - Fandom: "Slug Controlled Nebula | **Uncharted Nebula**", and does **not** list Slug
>   Home Nebula ([[source-fandom-nebula-wreckage]]).
>
> Trusting the game files (`high` vs `medium`): the event is available in both Slug
> sectors and not in [[sector-uncharted-nebula]]. Not resolvable as an AE-vs-vanilla
> difference — the event is AE-only to begin with.

## Text
> This nebula looks like it's recently seen two ships exchange fire... with
> mutually-assured destructive results. Wreckage drifts by your screens and tumbles into
> the depths of the nebula to be lost to sight. It's hard to determine who the combatants
> were without closer investigation.

(`event_NEBULA_BATTLEFIELD_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | **(Slug Crew)** Ask your Slug crew to scan for survivors. | `req="slug"` | "…your crewman is able to pick up the faint thoughts of a life form in the debris." → sub-choice: **Assist the survivor** (see below) or **Leave the battlefield** (nothing). | 100% |
| 2 | Investigate the battlefield. | — | Rolls `BATTLEFIELD_INVESTIGAGE` [sic], a 5-entry list — see below. | see below |
| 3 | Leave the battlefield before other ships arrive. | — | Nothing happens. | 100% |

### `BATTLEFIELD_INVESTIGAGE` (choice 2)

Five entries, one drawn at random. Entry 2's text is repeated three times, so three of the
five slots are the same "nothing happens" result. ([[source-events-slug]])

| Entry | Text | Effect |
|---|---|---|
| 1 | "…your ship is pummeled by drifting wreckage — unable to detect anything of interest…" | `<damage amount="4"/>` **and** `<damage amount="1" system="room" effect="fire"/>` — hull damage plus a fire in a random room |
| 2, 3, 4 | "The wreckage is drifting faster than it first appeared. You barely avoid being pummeled…" | Nothing |
| 5 | "You spot a life form floating within the wreckage." | Sub-choice: **Assist the survivor** or **Leave the battlefield** (nothing) |

Fandom reads the two damage tags as **5 hull damage total** plus 1 fire damage to a random
room ([[source-fandom-nebula-wreckage]]); the game files state them as separate `4` and `1`
tags ([[source-events-slug]]). Same numbers, different bookkeeping.

### `BATTLEFIELD_SURVIVOR` — "Assist the survivor"

> Your bring the survivor aboard, but discover their wounds are severe. They won't live
> much longer.

(`event_BATTLEFIELD_SURVIVOR_text` — the "Your bring" typo is in the game files;
[[source-text-events-xml]]. Fandom silently corrects it to "You bring".)

| # | Choice | Requirement | Outcome |
|---|--------|-------------|---------|
| 1 | Make them comfortable for their final moments. | — | The survivor croaks out coordinates and the word "ABADOTH", then dies. `<quest event="SECRET_WORD_ABADOTH"/>` — a quest marker is added to your map → [[event-secret-word-abadoth]] |
| 2 | **(Advanced Medbay)** Get them into the medbay! | `req="medbay" lvl="2"` | They recover and join you — `<crewMember amount="1"/>`, species not specified in the data |
| 3 | **(Clonebay)** Try to clone them before it's too late. | `req="clonebay"` | The clone joins you — `<crewMember amount="1"/>` |

## Blue Options
- **Slug crew member** (`req="slug"`) — skips the `BATTLEFIELD_INVESTIGAGE` roll entirely,
  so you reach the survivor with no chance of hull damage or fire.
- **Medbay level 2+** (`req="medbay" lvl="2"`) — turns the dying survivor into a free
  crew member instead of a quest marker.
- **Clone Bay** (`req="clonebay"`) — same payoff, no level requirement.

## Rewards & Risks
- Best case: a **free crew member** (Medbay 2+ or Clone Bay). The crew member's species is
  not specified in the event data ([[source-events-slug]]).
- Otherwise: a quest marker to [[event-secret-word-abadoth]], which pays medium
  scrap-with-resources if you guess (or know) the password, and a
  [[entity-zoltan-ships|Zoltan ship]] fight if you don't.
- Risk is confined to choice 2: one entry in five costs hull and sets a fire.

## Strategy Notes
- With a Slug aboard, this is a strictly free event — take choice 1 every time.
- Without one, choice 2 is a 1-in-5 chance of hull damage plus fire for a 1-in-5 chance of
  reaching the survivor: three of five entries do nothing at all. *(Opinion, derived from
  the entry weighting in [[source-events-slug]]; the game does not state per-entry odds.)*
- If you have an upgraded Medbay or a Clone Bay, the survivor is a free crew member and the
  ABADOTH quest never fires — the crew is the better prize.

## Related
- [[event-secret-word-abadoth]] — the quest marker this event can create
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]
- [[entity-slugs]], [[entity-zoltan]]
- [[event-battlefield-survivor]] — the `BATTLEFIELD_SURVIVOR` sub-event, on its own page

## Open Questions
- [ ] Per-entry odds inside `BATTLEFIELD_INVESTIGAGE` (assumed uniform over five entries).
- [ ] Which species the `<crewMember amount="1"/>` reward produces.
- [ ] Whether Fandom's "Uncharted Nebula" listing reflects a build we don't have.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-nebula-wreckage]] (per raw/wiki/nebula-wreckage.md)
