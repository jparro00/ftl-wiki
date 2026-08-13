---
id: source-fandom-ancient-device
type: source
source_kind: wiki
raw: raw/wiki/ancient-device.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [crystal-route]
---

# Fandom — "Ancient device"

## Summary
The community wiki page for the event the game files call `ROCK_CRYSTAL_BEACON`.
Retrieved via the MediaWiki API at revision 74020. It carries everything the game files
don't: the full chain context, sector-availability rules, reward values, and strategy.

## Key Takeaways
- **Names the in-game id explicitly** in its Notes section: *"This event is called
  'ROCK_CRYSTAL_BEACON' in the datafiles"*, and *"The quest marker event in the Hidden
  Crystal Worlds is called 'CRYSTAL_UNLOCK'"*. This is the join key between the two
  source layers, and it is not derivable from the page title.
- Lays out all four steps of [[chain-crystal-cruiser-unlock]] and the sector types each
  step requires — information that exists nowhere in the game files in that assembled form.
- Any Crystal crew satisfies the blue option; only Ruwen converts the beacon into a
  marked quest beacon.
- Rewards for completing the chain: the ship, [[item-crystal-vengeance]], 2–4 fuel and
  scrap, 10 hull repairs.
- Crystal-sector enemy strength scales to the Rock Homeworlds' sector number; you cannot
  choose your next sector on exit.
- Categorised as `Random_Events`, `Unique_Events`, `Ship_Unlocking_Events`.

## Events Covered
- [[event-ancient-device]]

## Other Pages Touched
- [[chain-crystal-cruiser-unlock]], [[item-crystal-vengeance]],
  [[sector-hidden-crystal-worlds]], [[sector-rock-homeworlds]]

## Reliability Notes
`medium`. The page states no game version, so `game_version` is `unknown` — not `ae`.
Where it disagrees with the extracted 1.6.x files, the files win.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** choice-3 outcome text.
> Fandom: *"the abandoned link to **my home worlds**"*.
> Game files: *"the abandoned link to **the Crystal home worlds**"*
> ([[source-text-events-xml]]).
> Recorded on [[event-ancient-device]]. Game files trusted; possibly pre-AE wording.

## Links
- Source URL: https://ftl.fandom.com/wiki/Ancient_device
- [[source-events-xml]], [[source-text-events-xml]]
