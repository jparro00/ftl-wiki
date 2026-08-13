---
id: source-fandom-single-life-form-on-moon
type: source
source_kind: wiki
raw: raw/wiki/single-life-form-on-moon.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [crew-reward, crew-loss-risk, blue-option]
---

# Fandom — "Single life form on moon"

## Summary
The community wiki page for the event the game files call `STRANDED_BEACON`. Retrieved via
the MediaWiki API at revision 73862. It transcribes the whole nested tree — both `STRANDED`
branches, all six `STRANDED_CHARLIES` variants, all four `MADMAN` outcomes and the Slug
check — and resolves several `autoReward` tags into concrete effects.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'STRANDED_BEACON' in the
  datafiles."* This is the join key.
- Lists **eight** sectors in its `{{Locations}}` template (Abandoned, Civilian, Pirate,
  Rock Controlled, Rock Homeworlds, Uncharted Nebula, Zoltan Controlled, Zoltan
  Homeworlds) — Federation Space is missing; see Contradictions.
- Notes that the *"Take him home to his family"* sub-event (`FAMILY_RETURN`) is shared with
  [[event-small-asteroid-belt-distress-beacon]]'s Teleporter blue option — a cross-event
  link the XML shows only as a shared `load=` target.
- Records the Clone Bay interaction on `MADMAN` outcome 1 as a nested blue-ish outcome
  rather than an automatic effect; the XML expresses it as `<removeCrew><clone>true</clone>`.
- Trivia: the event is a reference to the Star Trek episode "Charlie X" — which explains
  why every crew reward here is named Charlie.
- Categorised: `Random_Events`, `Unique_Events`, plus crew-loss / hull-damage /
  system-damage / crew-reward / hull-repair categories.

## Events Covered
- [[event-single-life-form-on-moon]]

## Other Pages Touched
- [[event-small-asteroid-belt-distress-beacon]], [[entity-slugs]]

## Reliability Notes
`medium`. No game version stated, so `game_version` is `unknown` — although the page
documents the AE-only Advanced Medbay and Improved Clonebay branches without marking them
as such, which is itself a reason not to read it as vanilla.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** [[sector-federation-space]] is missing from the page's
> `{{Locations}}` template.
> Fandom lists eight sectors. The game files put the event in the generic `DISTRESS_BEACON`
> pool ([[source-newevents]]), which `STANDARD_SPACE` allocates at
> `min="1" max="2"` ([[source-sector-data-xml]]) — so it can appear in
> Federation Space. Recorded on [[event-single-life-form-on-moon]]. Game files trusted
> (`high` vs `medium`); this looks like a Fandom convention/omission, not a version
> difference — no DLC marker is involved.

> ⚠️ **CONTRADICTION:** hull damage on `MADMAN` outcome 3.
> Fandom: *"Your ship takes 5 hull damage, 1 damage to a random system."*
> Game files: `<damage amount="4"/>` plus a DLC-marked
> `<damage amount="1" system="random"/>` ([[source-events-xml]]).
> Recorded on [[event-single-life-form-on-moon]]. They reconcile if a system-targeted
> `<damage>` entry also costs 1 hull, but no source here states that rule. Game files
> trusted on the literal values.

## Links
- Source URL: https://ftl.fandom.com/wiki/Single_life_form_on_moon
- [[source-events-xml]], [[source-text-events-xml]], [[source-newevents]],
  [[source-sector-data-xml]]
</content>
