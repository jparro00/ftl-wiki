---
id: event-slaver-hostile
type: event
event_name: PIRATE_SLAVER
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]]]
beacon_type: hostile
hostile: false
blue_options: [engines lvl 6]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [pirate, slaver, crew-loss-risk, blue-option, clone-bay-failed-revival, crew-reward-chance]
---

# Slaver (hostile) — `PIRATE_SLAVER`

## Summary
A well-armed slaver demands one of your crew as the price of passage. Hand a crew member
over — permanently, the Clone Bay will not bring them back — or fight the ship, which is
tougher than a standard pirate but pays a `HIGH` `standard` reward and can hand you *back*
a crew member if you board it. Level 6 Engines opens a third line: run, which works 2/3 of
the time.

## Trigger & Where It Appears
- Sectors: [[sector-civilian-sector]], [[sector-federation-space]],
  [[sector-pirate-controlled-sector]]
- Event lists: `HOSTILE_PIRATE` ([[source-events-pirate]]), `HOSTILE_CIVILIAN`
  ([[source-newevents]]), and under Advanced Edition `OVERRIDE_HOSTILE2`,
  `OVERRIDE_HOSTILE_PIRATE` ([[source-dlceventsoverwrite]]). `HOSTILE_CIVILIAN` is what
  puts it in [[sector-federation-space]], which [[source-fandom-slaver-hostile]] omits.
- `unique="false"` — explicitly, so it can repeat within a sector
  ([[source-events-pirate]]; [[source-fandom-slaver-hostile]] agrees)
- The ship is loaded `<ship load="PIRATE_SLAVER" hostile="false"/>`, so combat is optional
- Long-range scanners show a ship ([[source-fandom-slaver-hostile]], `LRSmap=ship`)

## Text
> An especially well-armed pirate ship approaches you. "Hand over one of your crew-members
> and the rest of you can go free unharmed."

(`event_PIRATE_SLAVER_text`, per [[source-text-events-xml]])

> ⚠️ **CONTRADICTION (wording):** [[source-fandom-slaver-hostile]] renders this as *"Hand
> over one of your crew and the rest can go unharmed."* The game files say *"one of your
> crew-members and the rest of you can go free unharmed."* Trusting the game files
> (`high` vs `medium`); likely a paraphrase or pre-AE wording.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Draw straws and send a crew-member over to the slavers. | — | *"The chosen crew-member leaves without complaint, knowing you had no choice."* → `<removeCrew>` with `<clone>false</clone>`: **lose one crew member, permanently**. | 100% |
| 2 | We will never surrender one of our crew to slavers! | — | `<ship hostile="true"/>` — fight the `PIRATE_SLAVER` ship (below). No outcome text. | 100% |
| 3 | **(Engines)** Attempt to out-run the slaver ship. | `req="engines" lvl="6"` | Loads `PIRATE_SLAVER_RUN` — 2/3 get away, 1/3 fight anyway (below). | see below |

### Choice 1 and the Clone Bay
`<removeCrew><clone>false</clone></removeCrew>` explicitly blocks revival, with its own
message: *"You briefly consider cloning a replacement, but decide to respect the Federation
laws regarding simultaneous duplicates."* ([[source-events-pirate]],
[[source-text-events-xml]]). A Clone Bay does **not** protect you here.

### Choice 3 — `PIRATE_SLAVER_RUN`
Three entries. Two of them get you away clean, one drops you into the fight. Under
**uniform selection across list entries** that is **2/3 escape, 1/3 fight** — derived from
the list membership, not stated as a percentage anywhere ([[source-events-pirate]]):

| Result | Entries | Share |
|---|---|---|
| *"You divert all available power to your engines and flee… able to stay out of range long enough to charge the FTL drive."* / *"You fire up the engines and try to escape. Their slower ship is unable to keep pace…"* → get away, nothing lost | 2 | 2/3 |
| *"You quickly fire up your engines and make a break for it. However, it seems to be in vain. They catch up to you effortlessly and power up their weapons."* → `<ship hostile="true"/>`, fight | 1 | 1/3 |

[[source-fandom-slaver-hostile]] marks the two escape texts with a "duplicate event"
notice, which is the same observation.

### The `PIRATE_SLAVER` ship
`<ship name="PIRATE_SLAVER" auto_blueprint="SHIPS_PIRATE">`, tagged
`<!-- NEEDS ELITE TAG -->` ([[source-events-ships]]):

| Branch | Trigger in the file | Result |
|---|---|---|
| Surrender | `chance="0.2" min="2" max="4"` | *"We surrender! Take one of our slaves as tribute; if you destroy us they'll all die anyway!"* → **Accept**: **+1 crew member** and the ship goes non-hostile. **Refuse**: fight continues. |
| Escape | `chance="0.5" min="2" max="4"` → loads `PIRATE_ESCAPE` | *"The enemy ship appears to be powering up its FTL. It's trying to escape!"* |
| Destroyed | — | *"The slave ship is destroyed. They won't continue their evil trade, but many lives were probably lost on that ship."* → `autoReward level="HIGH"` `standard` |
| Crew killed | loads `DEAD_CREW_SLAVER` | The crew-reward table, below |

### `DEAD_CREW_SLAVER` — boarding the slaver
Three live entries (a fourth block is commented out in the file with the dev note
*"This causes a crash if you hit ACCEPT when there are too many crewmembers"*). Under
**uniform selection across list entries**, **1/3** each
([[source-events-xml]], per `raw/gamedata/events.xml`):

| # | Result | Share |
|---|---|---|
| 1 | *"You find a number of slaves in the cargo hold…"* → choose one to conscript: **Mantis**, **Rockman** or **Engi** — `<crewMember amount="1" class="…"/>` plus `autoReward level="MED"` `standard` in every case | 1/3 |
| 2 | *"…a slave falls out of a hidden compartment… offers to join your crew."* → **+1 crew member** (no class specified) and `autoReward level="HIGH"` `standard` | 1/3 |
| 3 | *"…no life signs. It appears the slaves died in the fight. You strip the ship…"* → `autoReward level="HIGH"` `standard`, no crew | 1/3 |

Two of the three entries hand you a crew member, and entry 1 lets you **pick the species**
— the only place in this batch where you choose what race joins you.

## Blue Options
- **Engines level 6** (`req="engines" lvl="6"`) — the escape option. Level 6 Engines is a
  steep investment, and it does not guarantee anything: 1/3 of the time you are dropped
  into the fight regardless. Its value is that it costs nothing when it works — no crew,
  no scrap, no hull.

## Rewards & Risks
- **Choice 1:** costs a crew member outright, gains nothing. Clone Bay does not help.
- **Choice 2:** `HIGH` `standard` for the kill, or the `DEAD_CREW_SLAVER` table (2/3 of
  which pays a crew member) for boarding it, or **+1 crew** if you accept the surrender.
  This is one of the better crew-acquisition beacons in the pirate pool.
- **Risk:** an elite-flavoured pirate with a 0.2 surrender rate — it will not tap out
  early the way an ordinary `PIRATE` does, and it has a 0.5 escape branch that can deny
  you the reward after you have already taken damage.

## Strategy Notes
- *(Opinion.)* Fighting is nearly always right. Handing over a crew member is a pure loss;
  the fight has three separate paths to *gaining* one, and pays `HIGH` `standard` on top.
- Board it if you can. `DEAD_CREW_SLAVER` beats the destruction reward, and entry 1 lets
  you pick a Mantis (boarding), a Rockman (fire immunity) or an Engi (repair speed) to
  suit your build.
- Choice 1 is only defensible if the fight would kill you and you have a genuinely
  expendable crew member — but note the removed crew member is chosen by the game, not by
  you.

## Related
- [[event-slaver-friendly]] — the same `PIRATE_SLAVER` ship, approached as a trade
- [[event-pirate-toll]] — the same "pay or fight" shape, priced in scrap
- [[event-pirate-fight]] — the standard pirate ship, for comparison
- [[item-clone-bay]] — explicitly blocked by this event's `removeCrew`
- [[entity-pirates]], [[entity-mantis]], [[entity-rock-men]], [[entity-engi]]
- [[sector-pirate-controlled-sector]], [[sector-civilian-sector]],
  [[sector-federation-space]]
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Which crew member `removeCrew` picks — the file gives no selection rule.
- [ ] Species of the `DEAD_CREW_SLAVER` entry-2 crew member (`<crewMember amount="1"/>`,
      no `class`).
- [ ] Exact scrap values behind `MED`/`HIGH` `standard`.
- [ ] Whether `chance="0.2"` is P(surrender) or P(keep fighting) — see the contradiction on
      [[event-pirate-fight]].

## Sources
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — `HOSTILE_CIVILIAN`)
- [[source-fandom-slaver-hostile]] (per raw/wiki/slaver-hostile.md)
