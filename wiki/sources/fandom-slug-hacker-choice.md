---
id: source-fandom-slug-hacker-choice
type: source
source_kind: wiki
raw: raw/wiki/slug-hacker-choice.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [slug, hacking, system-malfunction]
---

# Fandom — "Slug hacker (choice)"

## Summary
Community wiki page for `NEBULA_SLUG_CHOOSE_DEATH`, retrieved at revision 74291. Lays out
all five choices with their per-outcome reward tiers, and adds three behavioural notes that
are not derivable from the game files.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'NEBULA_SLUG_CHOOSE_DEATH' in the
  datafiles."*
- Reward tiers per branch match [[source-events-ships]]: Shields `MED`/`HIGH`, Oxygen
  `MED`/`MED`, Weapons `HIGH`/`HIGH`, Hacking `HIGH`/`HIGH`.
- Adds the "rounds down against you" note on all the halved-system tooltips.
- **Behavioural notes not in the files:**
  - The "Shields" option can be chosen even with no Shields system installed.
  - The "Oxygen" hack does not fully disable an upgraded Oxygen system — it behaves like the
    Oxygen 2+ blue option in [[event-slug-hacker-oxygen]].
  - The "Weapons" hack does not affect Artillery Beam or Flak Artillery.
- Quotes the winning texts for each ship's `destroyed` / `deadCrew` blocks, including a
  `[sic]` on a copy-paste error in the game's own hacking-branch text.

## Events Covered
- [[event-slug-hacker-choice]]

## Other Pages Touched
- [[event-slug-hacker-oxygen]], [[item-hacking]], [[item-artillery-beam]],
  [[item-flak-artillery]], [[entity-slugs]]

## Reliability Notes
`medium`. Its reward tiers check out exactly against the ship definitions, which raises
confidence in the behavioural notes too — but those remain unverified against the files
because the files cannot express them.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** two wording differences, recorded on [[event-slug-hacker-choice]]:
> the intro loses the clause "guarding a station", and choice 2's outcome reads "Your life
> support **shuts off**" where the files read "is sabatoged" [sic]. Game files trusted;
> likely pre-AE transcription.

## Links
- Source URL: https://ftl.fandom.com/wiki/Slug_hacker_(choice)
- [[source-events-slug]], [[source-events-ships]], [[source-text-events-xml]]
