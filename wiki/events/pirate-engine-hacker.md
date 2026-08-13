---
id: event-pirate-engine-hacker
type: event
event_name: PIRATE_NO_ESCAPE
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-pirate-controlled-sector]]]
beacon_type: hostile
hostile: true
blue_options: [hacking system]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [pirate, unavoidable-fight, system-debuff, blue-option, fuel-reward, unique]
---

# Pirate engine hacker — `PIRATE_NO_ESCAPE`

## Summary
A pirate remotely hacks your **Engines down to level 1** and then attacks. You cannot flee
and you cannot dodge — the debuff lasts for the whole fight. The enemy ship has no
surrender and no escape branch, so it is a fight to the finish, and it pays in fuel. With
a Hacking system installed you can trade the engine lockdown for having your **Hacking
offline** instead, which is strictly better.

## Trigger & Where It Appears
- Sectors: [[sector-civilian-sector]], [[sector-engi-controlled-sector]],
  [[sector-engi-homeworlds]], [[sector-federation-space]],
  [[sector-pirate-controlled-sector]]
- Event lists: `HOSTILE_PIRATE` ([[source-events-pirate]]), `HOSTILE_CIVILIAN`
  ([[source-newevents]]), `HOSTILE_ENGI` ([[source-events-engi]]), and under Advanced
  Edition `OVERRIDE_HOSTILE2`, `OVERRIDE_HOSTILE_ENGI`, `OVERRIDE_HOSTILE_PIRATE`
  ([[source-dlceventsoverwrite]]). `HOSTILE_CIVILIAN` is what puts it in
  [[sector-federation-space]], which [[source-fandom-pirate-engine-hacker]] omits.
- `unique="true"` — once per run ([[source-events-pirate]];
  [[source-fandom-pirate-engine-hacker]] agrees)
- Long-range scanners show a ship ([[source-fandom-pirate-engine-hacker]], `LRSmap=ship`)

## Text
> Once you arrive, your screen lights up with warnings. A nearby pirate seems to have
> advanced hacking tools and they have tried to shut down your engines. Your crew manages
> to keep them barely operational and you move into attack.

(`event_PIRATE_NO_ESCAPE_text`, per [[source-text-events-xml]])

> ⚠️ **CONTRADICTION (wording):** [[source-fandom-pirate-engine-hacker]] transcribes
> *"…they have tried to shut down **our** engines. Your crew manages to keep them
> operational…"* — "our" for "your", and without the word "barely". The game files say
> "your engines" and "barely operational". Trusting the game files (`high` vs `medium`);
> most likely the Fandom text is pre-AE wording, but nothing here confirms that.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Continue… (hidden) | — | `<status type="limit" target="player" system="engines" amount="1"/>` — your **Engines are capped at level 1** for the fight. | 100% |
| 2 | **(Hacking System)** Counter the remote hacking. | `req="hacking"` | *"Your Hacking System automatically counters the digital assault and you move in to fight the ship."* → `<status type="limit" target="player" system="hacking" amount="0"/>` — your **Hacking is capped at 0**, i.e. offline, but Engines are untouched. | 100% |

Both choices are `hidden="true"`; the hostile ship is already loaded by the event body
([[source-events-pirate]]).

### The `PIRATE_NO_ESCAPE` ship
`<ship name="PIRATE_NO_ESCAPE" auto_blueprint="SHIPS_PIRATE">` — **no `<surrender>` and no
`<escape>` element at all** ([[source-events-ships]]). It fights until one side is gone.

| Branch | Result |
|---|---|
| Destroyed | *"With the pirate ship destroyed, your ship's system is restored to full functionality. You salvage what you can from the debris."* → `autoReward level="RANDOM"` `fuel`, plus `<status type="clear" …>` on both `engines` and `hacking` |
| Crew killed | *"With the pirate ship disabled, your engines come online again. You salvage what you can from their ship."* → `autoReward level="MED"` `fuel`, plus the same two `clear` statuses |

The `clear` statuses are what lift the debuff, which is why it persists for the entire
fight and not just the first jump ([[source-events-ships]]).

## Blue Options
- **Hacking system** (`req="hacking"`) — swaps the debuff. Instead of Engines limited to
  1 (no evasion, no FTL charge advantage) you lose the use of your Hacking system for the
  fight. If you own Hacking you almost certainly want this: engine level drives evasion,
  and this fight has no escape route to make FTL charge matter.
- **Version note:** this choice is marked `<!-- CHANGED - added -->` in
  `raw/gamedata/events_pirate.xml` ([[source-events-pirate]]), and the Hacking system is
  Advanced Edition content — so in **vanilla** this event has only choice 1 and the engine
  lockdown is unavoidable.

## Rewards & Risks
- **Reward:** fuel-flavoured — `RANDOM` `fuel` on destruction, `MED` `fuel` (Fandom reads
  the MED band as 2–4 fuel, [[source-fandom-pirate-engine-hacker]]) on a crew kill. This
  is one of the few reliable fuel sources in the pirate pool.
- **Risk:** a no-surrender, no-escape fight with your evasion gutted. Every enemy shot has
  its full hit chance. If you are already low on hull this is a genuinely dangerous beacon
  and there is no way to decline it.

## Strategy Notes
- *(Opinion, from [[source-fandom-pirate-engine-hacker]]:)* level-1 Engines are still
  *powered*, so a crew member stationed there keeps training the Engines skill — the
  lockdown caps the system, it does not disable it.
- With Hacking, take choice 2 without thinking about it. Losing an offensive system you
  might not have needed beats losing all your evasion.
- Worth entering with your weapons charged: there is no surrender offer to end this early.

## Related
- [[event-pirate-fight]] — the ordinary pirate fight, with surrender and escape branches
- [[event-pirate-toll]] — a pirate encounter you *can* buy out of
- [[item-hacking]] — the system that unlocks choice 2
- [[entity-pirates]]
- [[sector-pirate-controlled-sector]], [[sector-civilian-sector]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-federation-space]]

## Open Questions
- [ ] Exact fuel amounts behind `RANDOM` and `MED` `fuel` `autoReward` levels — Fandom's
      "2-4 fuel" for MED is a community reading, not a file value.
- [ ] Does the Engines cap also block manual evasion bonuses from Piloting/cloaking? The
      `status` tag only names the `engines` system.

## Sources
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — `HOSTILE_CIVILIAN`)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml — `HOSTILE_ENGI`)
- [[source-fandom-pirate-engine-hacker]] (per raw/wiki/pirate-engine-hacker.md)
