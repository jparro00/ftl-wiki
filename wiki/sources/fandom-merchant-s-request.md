---
id: source-fandom-merchant-s-request
type: source
source_kind: wiki
raw: raw/wiki/merchant-s-request.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [quest, trading, drone-schematic]
---

# Fandom — "Merchant's request"

## Summary
The community wiki page for `MERCHANT_REQUEST`. Retrieved via the MediaWiki API at revision
74272. The single most useful Fandom page in this batch: it assembles the whole quest line —
both errands, both destinations, the cargo sub-list and the final delivery — into one
document, with concrete scrap ranges the XML also carries.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'MERCHANT_REQUEST' in the datafiles."*
- Documents the up-front reward as **5 drone parts** on the delivery branch, and **nothing**
  on the investigation branch — matching the XML.
- Full delivery payout table, matching `MERCHANT_DELIVER_LIST` entry 2 exactly: 20–30 scrap
  for accepting, 40–55 via the bluff or Mind Control, 55–70 plus 2–5 fuel via Weapons 6, all
  costing 5 drone parts.
- Notes which trades are **previewed** before you commit: the paltry-payment and the
  post-bluff offers are shown; the Weapons 6 route is not.
- Documents the investigation's three scenarios, the three-entry cargo list (marker / free
  weapon / high scrap-with-resources), and the final `MED drone` schematic payout.
- Notes the "station doesn't respond" sub-event is the same content as the standalone
  *Small research station with no response*, but with a different intro and an extra
  Lifeform Scanner blue option that this copy lacks.
- `unique=true`, `LRSmap=noship`; the final delivery marker is `nolrs+noship`.

## Events Covered
- [[event-merchant-s-request]] — the quest start and both errands
- [[event-merchant-deliver]] — the delivery destination and its four price branches
- [[event-merchant-investigate]] — the investigation destination and the cargo list
- [[event-merchant-investigate-deliver]] — the final payout

## Other Pages Touched
- [[event-research-station-with-no-response]], [[item-mind-control]], [[item-weapons]], [[item-teleporter]],
  [[item-anti-personnel-drone]], [[entity-pirates]],
  [[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]],
  [[sector-rebel-stronghold]]

## Reliability Notes
`medium`. No game version stated, so `game_version: unknown`. Its numbers match the
extracted 1.6.x files everywhere they overlap; the one substantive divergence is prose, below.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** the merchant's delivery-offer wording.
> Fandom: *"**I'll pay you a bit of scrap now**, but they will surely tip you generously."*
> Game files: *"**We can't afford to pay another carrier**, but they will surely tip you
> generously."* ([[source-text-events-xml]]).
> Recorded on [[event-merchant-s-request]]. Game files trusted — the only up-front effect in
> the XML is `+5 drone parts`, so the wiki's wording would imply a payment that does not
> exist. Possibly pre-AE wording; not confirmed as a version difference.

> ⚠️ **CONTRADICTION:** sector coverage — omits [[sector-federation-space]] despite
> `QUESTS min=1 max=1` in `STANDARD_SPACE` ([[source-sector-data-xml]]). Recorded on
> [[event-merchant-s-request]]; game files trusted.

The page does not flag `MERCHANT_DELIVER_BLUFF_LIST` as Advanced Edition content, although
the XML marks it `<!--DLC!-->`. Recorded on [[event-merchant-deliver]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Merchant's_request
- [[source-events-xml]], [[source-text-events-xml]], [[source-events-ships]],
  [[source-sector-data-xml]]
