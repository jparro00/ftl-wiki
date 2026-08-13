---
id: source-fandom-capture-the-ship
type: source
source_kind: wiki
raw: raw/wiki/capture-the-ship.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [quest, boarding, hull-damage-risk, weapon-reward]
---

# Fandom — "Capture the ship"

## Summary
The community wiki page for `QUEST_CREWDEAD_START`. Retrieved via the MediaWiki API at
revision 74023. Documents the three-way blue-option gate, the follow-up offer, and the quest
marker — and supplies the aggregate damage figure for the failure branch that the XML only
gives as separate tags.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'QUEST_CREWDEAD_START' in the
  datafiles."*
- Confirms that without a Teleporter, Anti-Bio Beam or Fire Bomb, both plain choices do
  nothing — the beacon is a dead end.
- Labels the Bio Beam requirement concretely as the **Anti-Bio Beam** weapon, which the
  opaque `req="BEAM_BIO"` token does not spell out.
- Quest marker is `shipdetected=ship` — long-range scanners show a ship there.
- Failure branch: *"Your ship takes 15 hull damage, 1 damage to a random system, 1 damage
  with 1–2 fires and a breach to a random room."*
- Notes: *"This event can deal the most damage to the player ship, at 15."*
- Success branch: a weapon with high scrap, matching `autoReward level="HIGH">weapon`.
- `unique=true`, `LRSmap=noship`.

## Events Covered
- [[event-capture-the-ship]] — the gate, the offer, and the quest marker
- [[event-quest-crewdead]] — the target ship and both outcomes

## Other Pages Touched
- [[item-teleporter]], [[item-anti-bio-beam]], [[item-fire-bomb]], [[entity-pirates]],
  [[sector-civilian-sector]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]],
  [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]

## Reliability Notes
`medium`. No game version stated, so `game_version: unknown`. Its damage total is the sum of
three separate XML tags, one of which is AE-only — see below.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** the failure branch's damage. Fandom reports **15 hull**; the game
> files carry `<damage amount="13"/>` plus `<damage amount="1" system="random"/>` (marked
> `<!--DLC-->`) plus `<damage amount="1" system="room" effect="all"/>`
> ([[source-events-xml]]). Reconcilable as 13 + 1 + 1 = 15 total, i.e. Fandom reports the
> aggregate. But under **vanilla**, without the DLC-marked tag, the total would be **14**.
> Recorded on [[event-quest-crewdead]]; game files trusted for tag-level detail, Fandom for
> the observed AE total.

> ⚠️ **CONTRADICTION:** sector coverage — omits [[sector-federation-space]] despite
> `QUESTS min=1 max=1` in `STANDARD_SPACE` ([[source-sector-data-xml]]). Recorded on
> [[event-capture-the-ship]]; game files trusted.

## Links
- Source URL: https://ftl.fandom.com/wiki/Capture_the_ship
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
