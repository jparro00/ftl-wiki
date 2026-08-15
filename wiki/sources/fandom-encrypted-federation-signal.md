---
id: source-fandom-encrypted-federation-signal
type: source
source_kind: wiki
raw: raw/wiki/encrypted-federation-signal.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [quest-marker, boarding-risk, federation, stuff-reward]
---

# Fandom — "Encrypted federation signal"

## Summary
The community wiki page for the event the game files call `FEDERATION_PLANET_SIGNAL`.
Retrieved via the MediaWiki API at revision 74043. Lists all five outcomes of the
away-party branch and, uniquely, puts numbers on the `stuff` reward tier.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'FEDERATION_PLANET_SIGNAL'
  in the datafiles."* This is the join key.
- **Quantifies `autoReward level="MED"` of type `stuff`** in a tooltip:
  *fuel 2–4; missiles 2–4; drone parts 1*. The game files give only the level name, so
  this is the only numeric source for that payout.
- Confirms the Rebel-ambush outcome is a normal `REBEL` ship with **default rewards**, plus
  2–3 human boarders, and reproduces the ship's surrender/escape parameters
  (50 / 30–40 / 3–4 and 50 / 20–30 / 2–3) — read via [[concept-surrender-offers]].
- Confirms sector availability across ten sectors and `LRSmap=noship`, `unique=true`.
- Transcludes `{{Hidden federation base}}` for the first quest destination, so the
  retrieved markup does not contain the `HIDDEN_FEDERATION_BASE_LIST` outcomes.
- Categorised `Random_Events`, `Unique_Events`, `Fights with Default Rewards`,
  `Boarding risk`, `Events with Quest Markers`, `Events with Stuff rewards`.

## Events Covered
- [[event-encrypted-federation-signal]]

## Other Pages Touched
- [[entity-rebels]], [[entity-federation]], [[concept-quest-beacon-placement]],
  [[concept-surrender-offers]]

## Reliability Notes
`medium`. No game version stated. The `stuff` tier numbers are unattributed on the wiki
side, but they are the only figures available and are not contradicted by the files.

## Contradictions Flagged
None material. Fandom writes the second choice as *"It could be a trap, let's move on."*;
the files have *"It could be a trap. Let's move on."* Fandom also lower-cases *"federation
outpost"* where the files capitalise it.

## Links
- Source URL: https://ftl.fandom.com/wiki/Encrypted_federation_signal
- [[source-events-xml]], [[source-text-events-xml]], [[source-events-ships]]
