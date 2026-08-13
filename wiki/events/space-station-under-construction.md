---
id: event-space-station-under-construction
type: event
event_name: QUEST_CONSTRUCTIONYARD
sectors: [[[sector-civilian-sector]], [[sector-federation-space]]]
beacon_type: quest
hostile: false
blue_options: [lanius crew]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [quest, unique, blue-option, lanius, crew-cost, augment-reward, advanced-edition, ae-only]
---

# Space station under construction — `QUEST_CONSTRUCTIONYARD`

## Summary
An Advanced Edition quest beacon: a half-built station has lost contact with its supply
freighter and wants you to find it. Accepting pays a supply advance up front and plants a
quest marker; the marker beacon resolves to one of three very different follow-ups, one of
which is an ASB-covered Rebel fight. There is also a Lanius blue option that skips the
quest entirely and offers to sell your crew member for an augment.

## Trigger & Where It Appears
- `unique="true"` — once per run.
- **Advanced Edition only.** The event's only list membership is `OVERRIDE_QUESTS` in
  `dlcEventsOverwrite.xml`, where it is appended to the vanilla quest pool and marked
  `<!--newEvents-->` ([[source-dlceventsoverwrite]], line 194). The vanilla `QUESTS` list in
  `newEvents.xml` does **not** contain it ([[source-newevents]], lines 221–228) — so in
  1.0 this beacon does not exist. The XML also carries a dev comment on the definition:
  `<!-- quest only meant for DLC cause of PDS -->` ([[source-newevents]], line 1358).
- The `QUESTS` slot that `OVERRIDE_QUESTS` fills is allocated by `sector_data.xml` in
  `STANDARD_SPACE` ([[sector-federation-space]], `min=1 max=1`) and `CIVILIAN_SECTOR`
  ([[sector-civilian-sector]], `min=0 max=2`) ([[source-sector-data-xml]]).
- Beacon: **quest** — accepting fires `<quest event="QUEST_CONSTRUCTIONYARD_LIST"/>`, which
  places a marker on the sector map.

> ⚠️ **CONTRADICTION:** sector scope.
> - Fandom scopes it to the Civilian Sector only
>   ([[source-fandom-space-station-under-construction]]).
> - `sector_data.xml` also allocates the `QUESTS` slot in `STANDARD_SPACE`
>   ([[source-sector-data-xml]]).
>
> Trusting the game files (`high` vs `medium`).

## Text
> You come across a space station under construction. You receive a message from their
> command tower, "Greetings. We recently lost contact with a cargo ship that was set to
> deliver more construction materials. Could you help us figure out what happened to them?"

(`event_QUEST_CONSTRUCTIONYARD_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Offer your help. *(hidden)* | — | *"Great. Thanks for your help. I've marked their last known coordinates and sent over some supplies to help you get there."* → **+0–4 missiles, +0–2 drone parts, +2–4 fuel**, and `<quest event="QUEST_CONSTRUCTIONYARD_LIST"/>` places a quest marker. | 100% |
| 2 | Decline. *(hidden)* | — | *"I understand." Transmission has been cut.* → nothing. | 100% |
| 3 | **(Lanius Crew)** Offer to have your crewmember help. *(hidden)* | `req="anaerobic"` | *"…So this metal man can help us make some of these unique parts out of scrap?"* → continue → *"Amazing! This robot thing could save us a ton of time. Could I buy it off you?"* → two sub-choices, below. **No quest marker is placed.** | 100% |

### The Lanius branch (choice 3)

| # | Choice | Outcome |
|---|--------|---------|
| 3a | Ask your crew if they agree. | *"Once your Lanius crewmember understands the situation it appears to like the idea of assisting with construction in deep space. Much less dangerous. They offer you some goods in exchange."* → `autoReward level="HIGH"` **`augment`**, and `<removeCrew class="anaerobic">` with `<clone>false</clone>` — **you lose the Lanius crew member permanently**. The Clone Bay text is explicit that it does *not* help: *"Your clonebay obviously does not revive your crewmember since they did not die."* |
| 3b | Our crew is not for sale. | *"A pity. In terms of payment, here's some of the scrap metal we don't need now that we've got necessary parts."* → `autoReward level="MED"` `scrap_only`. |

Note that taking choice 3 at all forecloses the quest — the branch never places the quest
marker, so the Lanius option and the cargo-ship hunt are mutually exclusive.

### `QUEST_CONSTRUCTIONYARD_LIST` — the quest beacon
Three distinct entries. **Assuming uniform selection across list entries**, each is 1/3
([[source-newevents]]):

**1 — Cargo ship docked to a Rebel station.**
> You find the missing cargo ship docked to a Rebel station. You send a short-band message
> to them and discover they are being held against their will and forced to 'donate their
> supplies for the war effort.'

- *Attack the Rebels to help them escape.* → fight `QUEST_CONSTRUCTIONYARD_SHIP`
  (`auto_blueprint="SHIPS_REBEL"`, **no surrender, no escape**) with
  `<environment type="PDS" target="player"/>` — a planet-side Anti-Ship Battery firing on
  you throughout. `destroyed` → `autoReward level="MED"` `standard`; `deadCrew` →
  `autoReward level="HIGH"` `standard`. Either then offers a hidden *"Contact the cargo
  ship."* → `autoReward level="MED"` `scrap_only`.
- *Leave.* → *"You apologize but it's not worth the risk to attack a Rebel station."* →
  nothing.

**2 — Cargo ship docked to an empty space station.**
> You find the missing cargo ship docked to an empty space station. However their hold
> appears to be empty and there are no obvious signs that anyone is inside the ship or
> station. Everything looks abandoned.

- *Move in to examine the station.* → loads `EMPTY_STATION2_LIST`, the shared
  [[event-abandoned-station]] outcome pool (six entries: nothing; `LOW` `scrap_only` ×2; a
  Clone Bay–gated branch that can give +1 crew or 1 boarder; 2 boarders plus a `PIRATE`
  fight; and 2–4 boarders under Anti-Ship Battery fire) ([[source-newevents]]).
- *Stay near the Beacon.* → nothing.

**3 — Cargo ship floating near the beacon.**
> You find the missing cargo ship floating near the beacon. "Thank heavens! We've been
> drifting here after using the last of our fuel to escape a pirate raid."

- *Give them the requested 4 fuel.* → **−4 fuel**, `autoReward level="MED"` `scrap_only`.
- *Give them 1 fuel.* → **−1 fuel**, nothing else.
- *Do not give them any.* → *"I see..."* → nothing.

## Blue Options
- **Lanius crew** (`req="anaerobic"`, `hidden="true"`) — the only gated choice on this
  event. It converts the quest into an immediate transaction: either sell the Lanius for
  `HIGH` `augment` (a permanent, un-cloneable crew loss) or refuse and take `MED`
  `scrap_only` for free. Taking it cancels the quest line.

## Rewards & Risks
- **Up front:** accepting pays 0–4 missiles, 0–2 drone parts and 2–4 fuel before you have
  done anything.
- **Quest beacon:** 1/3 a hard fight under Anti-Ship Battery fire (best payout,
  `HIGH` `standard` + `MED` `scrap_only` on a crew kill), 1/3 the abandoned-station pool
  (boarding risk, small scrap), 1/3 a fuel donation for `MED` `scrap_only`.
- **Lanius branch:** `HIGH` `augment` at the cost of a crew member no Clone Bay can
  recover, or `MED` `scrap_only` for nothing.
- The quest marker costs a jump to reach, as all quest beacons do.

## Strategy Notes
- *(Opinion.)* Accepting is close to free — the supply advance alone often covers the
  detour, and one of the three quest outcomes is a pure fuel-for-scrap trade.
- The Rebel-station fight is the only ASB-covered fight in this event; take it only with
  hull to spare, since the battery fires regardless of how the fight is going.
- The Lanius option is a real decision, not a bonus: a `HIGH` augment for a crew member is
  good value on a large crew and terrible on a small one. Refusing still pays `MED`
  `scrap_only`, so opening the branch costs nothing — but it does cancel the quest.
- Free `MED` `scrap_only` for refusing (3b) is strictly better than declining outright (2),
  so a Lanius crew makes choice 2 obsolete.

## Related
- [[event-abandoned-station]] — the `EMPTY_STATION2_LIST` pool reused by quest outcome 2
- [[entity-lanius]] — the blue-option requirement (`req="anaerobic"`)
- [[entity-rebels]] — the quest fight
- [[concept-anti-ship-battery]] — the PDS hazard on quest outcome 1
- [[item-clone-bay]] — explicitly does **not** save the traded Lanius

## Open Questions
- [ ] Whether event-list selection is truly uniform across the three quest beacons.
- [ ] Exact values behind `LOW` / `MED` / `HIGH` `standard`, `scrap_only` and `augment`.
- [ ] Whether the quest marker can spawn in the next sector as well as the current one —
      not stated in the files read here.

## Sources
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-space-station-under-construction]] (per `raw/wiki/space-station-under-construction.md`)
