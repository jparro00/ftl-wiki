---
id: source-fandom-research-station-with-no-response
type: source
source_kind: wiki
raw: raw/wiki/research-station-with-no-response.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [boarding-risk, crew-loss-risk, blue-option]
---

# Fandom — "Research station with no response"

## Summary
The community wiki page for the event the game files call `STATION_SICK`. Retrieved via the
MediaWiki API at revision 74273. It transcribes the full outcome tree, including the two
Advanced-Edition-only Lifeform Scanner outcomes, and adds two things the XML does not
carry: the reuse of this event's lists inside Merchant's Delivery, and a bug note about the
Anti-Personnel Drone branch's drone-part cost.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'STATION_SICK' in the
  datafiles."* This is the join key.
- Records that the event also occurs as *"the station doesn't respond"* sub-event of
  [[event-merchant-s-request]]'s Merchant's Delivery scenario, and that the Lifeform Scanner
  blue option *"only appears if this event is found alone"* — consistent with the XML,
  where `MERCHANT_DELIVER_LIST` loads `STATION_SICK_LIST` and `STATION_SICK_DRONE_LIST` but
  not `STATION_SICK_SCANNER`.
- Carries an alternate intro text inside `<includeonly>` tags — *"You find the small
  research station and discover that it's putting out a distress signal. Strangely, there
  is no response to your hails."* — which is the wording used when the event is
  transcluded into the Merchant's request page, **not** a second in-game text. Only
  `event_STATION_SICK_text` exists in `text_events.xml`.
- Reward labels match the XML tags exactly (medium drone parts, medium `standard`, medium
  `scrap_only`), so the two layers agree on every payload.
- Its `{{Locations}}` template names **only** Pirate Controlled Sector, even though the
  event is also in the generic `HOSTILE_BOARDING` list. That turns out to be **correct**:
  `STANDARD_SPACE` allocates `<event name="HOSTILE_BOARDING" min="0" max="0"/>`
  ([[source-sector-data-xml]]), so Federation Space never places a beacon from that pool.
  A useful case where Fandom's location list is more accurate than raw list membership.
- Categorised: `Random_Events`, `Unique_Events`, plus crew-loss / boarding / crew-reward /
  drone-parts risk categories.

## Events Covered
- [[event-research-station-with-no-response]]

## Other Pages Touched
- [[event-merchant-s-request]], [[item-anti-personnel-drone]], [[item-lifeform-scanner]]

## Reliability Notes
`medium`. The page states no game version, so `game_version` is `unknown` — not `ae`, even
though it documents the AE-only Lifeform Scanner branch. Where it disagrees with the
extracted 1.6.x files, the files win.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** the Anti-Personnel Drone branch's drone-part cost.
> Fandom footnotes it as *"Bugged: no drone part is lost if the reward includes drone
> parts, though you still need at least 1 drone part to choose this blue option."*
> The game files apply `<item type="drones" min="-1" max="-1"/>` on **all three**
> `STATION_SICK_DRONE_LIST` members ([[source-events-xml]]).
> Recorded on [[event-research-station-with-no-response]]. Unresolved — this is an
> engine-behaviour claim the XML can neither confirm nor deny.

## Links
- Source URL: https://ftl.fandom.com/wiki/Research_station_with_no_response
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
</content>
