# Index

The catalog of everything in the wiki. **Read this first on every query** to locate
relevant pages, then open those pages. Regenerated on every ingest.

Row format: `[[slug]] — one-line description | key field | Updated: YYYY-MM-DD`

Nothing generated lives in `wiki/`. The machine-readable decision trees behind event cards
are at `cards/trees/<slug>.tree.json` and the built cards at `cards/card-<slug>.html`, kept
out of this layer so wiki searches never scan machine output — see
[[concept-event-tree-grammar]] and `tools/EVENT-CARD.md`.

## Events

395 event pages, covering every reachable encounter in the game data.
Grouped by sector; events reaching several sectors are listed under **Cross-sector**.

### Abandoned Sector

- [[event-boarders-humans-abandoned]] — The Abandoned Sector's boarding event, and the whole of its boarding pool. Desperate humans whose engines the… | `LANIUS_PIRATE_BOARDERS` · any · ae | Updated: 2026-08-09
- [[event-empty-beacon-lanius]] — The Abandoned Sector's nothing-happens beacon. It prints one of six worldbuilding vignettes about what the… | `NOTHING_LANIUS` · empty · ae | Updated: 2026-08-09
- [[event-free-scrap-with-resources-lanius]] — The Abandoned Sector's free lunch: a battered Lanius ship flees at the sight of you, leaving a field of… | `LANIUS_FREE_STUFF` · any · ae | Updated: 2026-08-09
- [[event-lanius-craftsmen]] — A shop in event form. Lanius craftsmen docked with a merchant will melt your scrap into a specific category… | `LANIUS_RESEARCHER_CRAFT` · any · ae | Updated: 2026-08-09
- [[event-lanius-empty-distress-beacon-1]] — A distress beacon that resolves to nothing at all: a plastic satellite looping a message from settlers who… | `LANIUS_DISTRESS_EMPTY` · distress · ae | Updated: 2026-08-09
- [[event-lanius-empty-distress-beacon-2]] — The second of the Abandoned Sector's two "nothing happens" distress beacons. The signal dies as you arrive… | `LANIUS_DISTRESS_TOOLATE` · distress · ae | Updated: 2026-08-09
- [[event-lanius-fight]] — The baseline hostile encounter of the abandoned sector: you arrive, a Lanius warship is already coming for… | `LANIUS_FIGHT` · hostile · ae | Updated: 2026-08-09
- [[event-lanius-fight-distress]] — The Abandoned Sector's "answering a distress call gets you shot" event. Whatever was calling for help has… | `LANIUS_DISTRESS_TRAP` · distress · ae | Updated: 2026-08-09
- [[event-lanius-fight-in-asteroid-field]] — A LANIUSSHIP fight with an asteroid field on top. No choices, no avoid, no blue option — the only thing that… | `LANIUS_FIGHT_ASTEROID` · hostile · ae | Updated: 2026-08-09
- [[event-lanius-fight-near-pulsar]] — A LANIUSSHIP fight inside a pulsar's EM pulses. No choices. Identical to lanius fight except for <environment… | `LANIUS_FIGHT_PULSAR` · hostile · ae | Updated: 2026-08-09
- [[event-lanius-fight-with-friendly-asb-support]] — The one encounter where the planetary Anti-Ship Battery is shooting at your enemy instead of at you:… | `LANIUS_NOBOARDERS_PDS` · hostile · ae | Updated: 2026-08-09
- [[event-lanius-lone-ship]] — A civilian screams that the "metal monsters" are about to melt their ship — but the event text itself tells… | `LANIUS_SCARED_CIVILIAN` · any · ae | Updated: 2026-08-09
- [[event-lanius-powered-down-ship]] — A hibernating Lanius vessel, undamaged and unpowered. Poking it wakes it up; investigating carefully opens a… | `LANIUS_DORMANT_EVENT` · any · ae | Updated: 2026-08-09
- [[event-lanius-ship-absorbing-automated-scout]] — A Lanius ship is eating a Rebel automated scout. Scare it off and the half-digested scout is yours to strip —… | `LANIUS_AUTO_REBEL` · any · ae | Updated: 2026-08-09
- [[event-lanius-ship-absorbing-jump-beacon]] — A damaged Lanius ship is eating the jump beacon it is docked to. Every route through this event is a… | `LANIUS_BEACON_EATER` · any · ae | Updated: 2026-08-09
- [[event-lanius-ship-absorbing-rebel-base]] — A swarm of Lanius ships is dismantling a forward Rebel base. You can try to point them at the Rebel fleet — a… | `LANIUS_GROUP_AUTO` · any · ae | Updated: 2026-08-09
- [[event-lanius-ship-attacking-civilian]] — The optional-fight version of the Lanius-versus-civilians encounter: a Lanius ship is tearing into a civilian… | `LANIUS_CIVILIAN` · any · ae | Updated: 2026-08-09
- [[event-lanius-ship-attacking-civilian-distress]] — A distress beacon where a civilian ship is being shot apart by a rogue Lanius vessel. You can fight, walk… | `LANIUS_DISTRESS_FIGHT` · distress · ae | Updated: 2026-08-09
- [[event-lanius-ship-attacking-mantis]] — A Mantis ship is being mined for parts and its distress beacon is failing. You can save the Mantis or let… | `LANIUS_MANTIS_DISTRESS` · distress · ae | Updated: 2026-08-09
- [[event-lanius-ship-attacking-rock]] — A distress beacon in the abandoned sector: Lanius are stripping a Rockman ship with its crew still aboard.… | `LANIUS_ROCK_DISTRESS` · distress · ae | Updated: 2026-08-09
- [[event-lanius-ship-attacking-slug]] — The Slug version of the Lanius rescue-or-abandon distress beacon, mechanically identical to lanius ship… | `LANIUS_SLUG_DISTRESS` · distress · ae | Updated: 2026-08-09
- [[event-lanius-ship-in-rich-debris-field]] — A Lanius vessel is harvesting a rich debris field and you want a share. Greed without piloting skill starts a… | `LANIUS_HARVESTER` · hostile · ae | Updated: 2026-08-09
- [[event-lanius-ship-salvager]] — A lone Lanius ship is picking over wreckage and has not noticed you, or does not care. You can jump it,… | `LANIUS_SOLO_SALVAGE` · any · ae | Updated: 2026-08-09
- [[event-lanius-surrender]] — The surrender offer made by the standard Lanius hull, and the most generous offer rate in the game:… | `LANIUS_SURRENDER` · hostile · ae | Updated: 2026-08-09
- [[event-lanius-trader]] — A resource-for-scrap trade: the Lanius want fuel, missiles or drone parts and pay scrap for them. The game… | `LANIUS_TRADER` · any · ae | Updated: 2026-08-09
- [[event-lanius-trader-with-translator]] — The near-twin of lanius trader — same resource-for-scrap tables, same "accept or decline" shape — with one… | `LANIUS_TRADER_TRANSLATOR` · any · ae | Updated: 2026-08-09
- [[event-lanius-with-federation-science-craft]] — A pure-upside item beacon in the abandoned sector: Federation xenolinguists studying the Lanius will hand you… | `LANIUS_RESEARCHER_CONTACT` · any · ae | Updated: 2026-08-09
- [[event-pirate-fight-lanius]] — An ordinary pirate fight wearing Abandoned Sector clothes. Mechanically it is three lines — a text list and… | `LANIUS_PIRATE_FIGHT` · hostile · ae | Updated: 2026-08-09
- [[event-pirate-ship-attacking-civilian-lanius]] — The Abandoned Sector's re-skin of the classic pirate-attacking-civilian encounter: same two choices, same… | `LANIUS_PIRATE_CIVILIAN` · any · ae | Updated: 2026-08-09
- [[event-rebel-fight-lanius]] — A standard Rebel fight with Abandoned Sector flavour text. The enemy is the generic REBEL ship definition;… | `LANIUS_REBEL_FIGHT` · hostile · ae | Updated: 2026-08-09
- [[event-refueling-platform-garbled-broadcast]] — A refuelling platform is broadcasting nonsense. Hail it and it turns out to be a Lanius ship in disguise;… | `LANIUS_FUELING_STATION` · any · ae | Updated: 2026-08-09
- [[event-start-beacon-lanius]] — The beacon you arrive on when you jump into an Abandoned Sector. A structural event, not an encounter: it… | `START_BEACON_LANIUS` · empty · ae | Updated: 2026-08-09
- [[event-store-lanius]] — The Abandoned Sector's store beacon. It opens a store and nothing else; the six flavour variants exist to… | `STORE_LANIUS` · store · ae | Updated: 2026-08-09

### Engi Homeworlds

- [[event-engi-fleet-discussion]] — The first step of stealth cruiser unlock and a guaranteed beacon in the engi homeworlds. Without an Engi… | `ENGI_UNLOCK_1` · any · both · **ship-unlock** | Updated: 2026-08-09

### Federation Space

- [[event-boarders-asteroid-ghost]] — Fully authored, atmospheric, and — as far as sectordata.xml goes — unreachable. A field of wrecks disgorges… | `BOARDERS_ASTEROID_GHOST` · any · both · **unreachable** | Updated: 2026-08-09
- [[event-ghost-ship]] — A fully authored multi-branch salvage encounter — a derelict with no life signs, a deep tree of boarding… | `GHOST_SHIP` · ae · **unreachable** · **cut-content** | Updated: 2026-08-09
- [[event-start-beacon]] — The generic sector-entry text: the reminder to explore and then run for the exit before the Rebel fleet… | `START_BEACON` · any · both | Updated: 2026-08-09

### Hidden Crystal Worlds

- [[event-auto-ship-fight-crystal]] — The one Rebel automated ship in hidden crystal worlds. It is a plain forced fight with no choices and no… | `CRYSTAL_AUTO` · hostile · both | Updated: 2026-08-09
- [[event-boarders-crystal]] — The hidden crystal worlds boarding event. No choices, no enemy ship — 2–3 Crystalline boarders simply… | `BOARDERS_CRYSTAL` · any · both | Updated: 2026-08-09
- [[event-crystal-chat]] — A curious Crystalline civilian wants to interview you. Humouring them is a three-way gamble — supplies, hull… | `CRYSTAL_CHATTY` · any · both | Updated: 2026-08-09
- [[event-crystal-fight]] — The backbone of hidden crystal worlds's hostile pool: a forced fight against a generic Crystal warship. It… | `CRYSTAL_FIGHT` · hostile · both | Updated: 2026-08-09
- [[event-crystal-fight-choice]] — A bait event. It looks like rebel ship attacking crystal ship — a Rebel firing on a Crystalline vessel, and… | `CRYSTAL_REBEL_CRYSTAL2` · any · both | Updated: 2026-08-09
- [[event-crystal-fight-with-surrender-offer-hull-repairs]] — A forced fight against a convoy escort that, once beaten down, offers a truce worth 8 hull repairs plus fuel… | `CRYSTAL_CONVOY` · hostile · both | Updated: 2026-08-09
- [[event-crystal-fight-with-surrender-offer-human-crew]] — A forced fight against a Crystalline slaver hauling human captives. Its surrender branch hands you a free… | `CRYSTAL_HUNTER` · hostile · both | Updated: 2026-08-09
- [[event-crystal-scrap-collector]] — A collector of alien junk offers to trade. Pay 35 scrap and you choose your payment: either a Crystal crew… | `CRYSTAL_SCRAP_EXCITED` · any · both | Updated: 2026-08-09
- [[event-crystal-ship-attacking-federation-loyalists]] — A Crystalline border guard is running down a Federation ship. Intervening is an optional fight with a… | `CRYSTAL_FED` · any · both | Updated: 2026-08-09
- [[event-crystal-unlock]] — The payoff. Step 4 of 4 of crystal cruiser unlock and the end of the Crystal route: you find your Crystalline… | `CRYSTAL_UNLOCK` · quest · both · **ship-unlock** | Updated: 2026-08-09
- [[event-crystalline-cache]] — A sealed weapons cache inside an asteroid. Getting in is the first puzzle (three routes, two of them blue);… | `CRYSTAL_CACHE` · any · both | Updated: 2026-08-09
- [[event-crystalline-men-buried]] — The sector's longest branch and its nastiest trade. A Crystalline ship asks you to lend a crew member to a… | `CRYSTAL_HELP_DIG` · any · both | Updated: 2026-08-09
- [[event-crystalline-research-facility]] — Crystalline scientists want to study your crew's physiology. Volunteering a crew member is a 1-in-3 chance of… | `CRYSTAL_HUMAN_TESTS` · any · both | Updated: 2026-08-09
- [[event-crystalline-ship-messaging-about-rebels]] — The Crystals will pay you high scrap for your flight plan so they can hand it to the Rebels and get the fleet… | `CRYSTAL_REQUEST` · any · both | Updated: 2026-08-09
- [[event-empty-beacon-crystal]] — The sector's do-nothing beacon: flavour text about Crystalline society and then nothing. Its only mechanical… | `NOTHING_CRYSTAL` · empty · both | Updated: 2026-08-09
- [[event-federation-deserters]] — A Federation warship that ran from the fleet and hid in the Crystal sector. Paying them off reveals the… | `CRYSTAL_FED_DESERTER` · any · both | Updated: 2026-08-09
- [[event-mantis-ship-attacking-crystal]] — A Mantis raider is picking on Crystalline civilians. Intervene and you fight a Mantis ship for standard… | `CRYSTAL_MANTIS_CRYSTAL` · any · both | Updated: 2026-08-09
- [[event-pirate-ship-attacking-crystal]] — A pirate that followed you through the reopened Long-Range Beacon is about to hit a Crystalline transport.… | `CRYSTAL_PIRATE_CRYSTAL` · any · both | Updated: 2026-08-09
- [[event-rebel-fight-crystal]] — A standard Rebel pursuit fight, reskinned for hidden crystal worlds. No choices, generic REBEL ship, default… | `CRYSTAL_REBEL` · hostile · both | Updated: 2026-08-09
- [[event-rebel-ship-attacking-crystal-ship]] — A three-way: a Rebel and a Crystalline ship are already shooting at each other. You can help the Crystals… | `CRYSTAL_REBEL_CRYSTAL` · any · both | Updated: 2026-08-09
- [[event-start-beacon-crystal]] — The arrival beacon of hidden crystal worlds and the hinge between steps 3 and 4 of crystal cruiser unlock. It… | `START_BEACON_CRYSTAL` · quest · both | Updated: 2026-08-09
- [[event-store-crystal]] — The hidden crystal worlds store beacon. Mechanically an ordinary store, but strategically the most… | `STORE_CRYSTAL` · store · both | Updated: 2026-08-09

### Mantis Homeworlds

- [[event-legendary-thief-kazaaakplethkilik]] — The mantis cruiser unlock beacon, and a guaranteed one: sectordata.xml allocates MANTISNAMEDTHIEF at min=1… | `MANTIS_NAMED_THIEF` · hostile · both · **ship-unlock** | Updated: 2026-08-09
- [[event-mantis-named-thief-defeat]] — The aftermath event that decides the mantis cruiser unlock. It fires only when you kill the crew of… | `MANTIS_NAMED_THIEF_DEFEAT` · hostile · both · **ship-unlock** | Updated: 2026-08-09
- [[event-mantis-named-thief-stash]] — The payoff beacon of mantis cruiser unlock: a hidden weapon cache you can open with codes taken from the… | `MANTIS_NAMED_THIEF_STASH` · quest · both | Updated: 2026-08-09

### Pirate Controlled Sector

- [[event-destroyed-cargo-ship]] — Free-floating cargo from a wrecked freighter. Taking it aboard is a coin-flip: half the pool is scrap, half… | `FLOATING_CARGO` · any · both | Updated: 2026-08-09
- [[event-empty-beacon-pirate]] — The Pirate sectors' filler beacon. Nothing happens: no choices, no ship, no reward. Three of its four flavour… | `NOTHING_PIRATE` · empty · both | Updated: 2026-08-09
- [[event-refugee-distress-pirate]] — The pirate-sector cut of refugee distress. Identical prose and identical choices, but the hail pool is… | `REFUGEE_DISTRESS_PIRATE` · distress · both | Updated: 2026-08-09
- [[event-refugee-pirate]] — The pirate-sector, no-distress cut of the refugee encounter: your sensors spot a drifting refugee ship that… | `REFUGEE_NO_DISTRESS_PIRATE` · any · both | Updated: 2026-08-09
- [[event-start-beacon-pirate]] — The beacon you arrive on when you jump into a pirate controlled sector. It is a structural event, not an… | `START_BEACON_PIRATE` · empty · both | Updated: 2026-08-09
- [[event-store-pirate]] — The Pirate-flavoured store beacon. It opens a store and nothing else; the four flavour variants exist to… | `STORE_PIRATE` · store · both | Updated: 2026-08-09

### Rebel Stronghold

- [[event-rebel-shipyard]] — The miniboss. A guaranteed beacon in rebel stronghold where you can fight a second, unfinished Rebel Flagship… | `FLAGSHIP_CONSTRUCTION` · any · both · **ship-unlock** | Updated: 2026-08-09

### Rock Homeworlds

- [[event-ancient-device]] — A guaranteed beacon in the rock homeworlds and the third step of crystal cruiser unlock. Without a Crystal… | `ROCK_CRYSTAL_BEACON` · any · both · **ship-unlock** | Updated: 2026-08-09
- [[event-rock-unlock1]] — The opening beacon of the Rock Cruiser unlock quest. A Rock war vessel challenges you to prove the Federation… | `ROCK_UNLOCK1` · quest · both · **ship-unlock** | Updated: 2026-08-09
- [[event-rock-unlock2]] — The trial by fire. The Rock war vessel from rock unlock1 challenges you to a duel beside an M-class star, and… | `ROCK_UNLOCK2` · quest · both · **ship-unlock** | Updated: 2026-08-09

### Slug Home Nebula

- [[event-slug-home-nebula-surrender]] — A guaranteed beacon in slug home nebula that is deliberately disguised as an ordinary slug fight in nebula —… | `NEBULA_SLUG_FIGHT_UNLOCK` · nebula · both · **ship-unlock** | Updated: 2026-08-09
- [[event-slug-unlock-1]] — The payoff beacon of the Slug Cruiser chain. A prototype cruiser is being towed away on a mobile construction… | `SLUG_UNLOCK_1` · quest · both · **ship-unlock** | Updated: 2026-08-09
- [[event-slug-unlock-surrender]] — The hidden surrender that starts the Slug Cruiser unlock. It looks exactly like an ordinary slug surrender —… | `SLUG_UNLOCK_SURRENDER` · nebula · both · **ship-unlock** | Updated: 2026-08-09

### The Last Stand

- [[event-boss-automated]] — The one-line event that fires when you wipe out the Rebel Flagship's crew instead of its hull: an onboard AI… | `BOSS_AUTOMATED` · quest · both | Updated: 2026-08-09
- [[event-boss-destroyed]] — The win condition's event: the Flagship blows up and the Federation is saved. Two lines of prose, a… | `BOSS_DESTROYED` · quest · both | Updated: 2026-08-09
- [[event-boss-escaped]] — Fires when the Flagship breaks off and jumps rather than dying — the transition between one phase and the… | `BOSS_ESCAPED` · quest · both | Updated: 2026-08-09
- [[event-boss-text-1]] — The event that announces the first Flagship engagement. Like its two siblings it is a bare <text tag — it… | `BOSS_TEXT_1` · quest · both | Updated: 2026-08-09
- [[event-boss-text-2]] — The announcement for the Flagship's second engagement, in which it has dumped power into its drone bay. A… | `BOSS_TEXT_2` · quest · both | Updated: 2026-08-09
- [[event-boss-text-3]] — The announcement for the final Flagship engagement — the one where it starts teleporting boarders and firing… | `BOSS_TEXT_3` · quest · both | Updated: 2026-08-09
- [[event-empty-beacon-last-stand]] — The safe draw in the last stand: a beacon the Rebel fleet has not reached yet, still held by Federation… | `BOSS_FLEETS_FED` · empty · both | Updated: 2026-08-09
- [[event-federation-base]] — The arrival text at the Federation Base beacon in the last stand — the beacon you are defending, and where… | `FEDERATION_BASE` · quest · both | Updated: 2026-08-09
- [[event-fight-in-last-stand]] — The plain hostile beacon of the last stand. No choices: you arrive, a Rebel scout or an automated ship is… | `BOSS_SCOUT` · hostile · both | Updated: 2026-08-09
- [[event-last-stand-start]] — The scripted arrival event of the last stand: you dock at a Federation outpost, brief Admiral Tully's war… | `LAST_STAND_START` · quest · both | Updated: 2026-08-09
- [[event-rebel-fight-among-federation-and-rebel-fleets]] — A beacon in the middle of the two fleets grinding against each other in the last stand. Mechanically… | `BOSS_FLEETS_BOTH_FIGHT` · hostile · both | Updated: 2026-08-09
- [[event-rebel-fight-among-rebel-fleet]] — The beacon behind the Rebel advance line in the last stand. A Rebel fighter peels off the fleet and attacks;… | `BOSS_FLEETS_REBEL` · hostile · both | Updated: 2026-08-09
- [[event-rebel-ship-attacking-civilians-in-last-stand]] — The only beacon in the last stand that offers a real decision: a Rebel scout is tearing into Federation… | `BOSS_SCOUT_RESCUE` · any · both | Updated: 2026-08-09
- [[event-repair-station-in-last-stand]] — The Federation's parting gift: three guaranteed beacons in the last stand that fully repair your ship and… | `BOSS_REPAIR_STATION` · any · both | Updated: 2026-08-09

### Uncharted Nebula

- [[event-mantis-fight-choice-in-nebula]] — A Mantis ship lets you go. You can accept that, or shoot first. Two choices, no blue options, no requirements… | `NEBULA_MANTIS_CHOICE` · nebula · both | Updated: 2026-08-09
- [[event-rock-ship-in-plasma-storm]] — A lost Rock transport insults you and tells you to leave. With a Rock crew member you can escort them out for… | `NEBULA_ROCK_RACIST` · nebula · both | Updated: 2026-08-09
- [[event-start-beacon-nebula]] — The arrival text for uncharted nebula. Pure flavour: six strings, no choices, no mechanics. It fires once, on… | `START_BEACON_NEBULA` · any · both | Updated: 2026-08-09
- [[event-store-in-nebula-uncharted]] — The guaranteed store beacon of uncharted nebula. Five flavour texts, <environment type="nebula"/, and a bare… | `NEBULA_STORE` · store · both | Updated: 2026-08-09

### Zoltan Homeworlds

- [[event-unarmed-zoltan-transport]] — Step 1 of the zoltan cruiser unlock and a guaranteed beacon in the zoltan homeworlds. Hearing the peace envoy… | `ZOLTAN_PEACE_QUEST` · quest · both · **ship-unlock** | Updated: 2026-08-09
- [[event-zoltan-peace-quest2]] — Step 2 and the payoff of zoltan cruiser unlock. What looks like a Rebel ambush is a Zoltan test: exactly one… | `ZOLTAN_PEACE_QUEST2` · quest · both · **ship-unlock** | Updated: 2026-08-09

### Cross-sector

- [[event-abandoned-station]] — A filler beacon with an abandoned station you may examine. Six equally-likely outcomes: three are harmless… | `EMPTY_STATION2` · any · ae — the entire `NEUTRAL`→`OVERRIDE_NEUTRAL` delta | Updated: 2026-08-16
- [[event-asteroid-belt-distress]] — A civilian miner is being torn apart by an asteroid belt with its shields down. It is one of the most… | `CIVILIAN_ASTEROIDS_BEACON` · distress · both | Updated: 2026-08-09
- [[event-asteroid-mining-colony]] — A pure trade: hand over missiles, get something back. Five missiles buys one of scrap, hull repairs, or a… | `HELP_MINERS` · any · ae | Updated: 2026-08-09
- [[event-auto-ship-attacking-civilian]] — An optional auto-ship fight with a rescue attached: intervene, kill the automated scout, and you get a roll… | `AUTO_CIVILIAN` · hostile · both | Updated: 2026-08-09
- [[event-auto-ship-attacking-outpost]] — An optional auto-ship fight where the reward is paid twice: a LOW payout for the kill, then a grateful… | `AUTO_REFUEL_STATION` · hostile · both | Updated: 2026-08-09
- [[event-auto-ship-carrying-shield-virus]] — A forced auto-ship fight that starts with your Shields already crippled: a satellite-borne virus halves your… | `AUTO_HACKER` · hostile · both | Updated: 2026-08-09
- [[event-auto-ship-fight]] — The unmanned counterpart to rebel fight: a Rebel automated scout engages on arrival, no choices. Mechanically… | `REBEL_AUTO` · hostile · both | Updated: 2026-08-09
- [[event-auto-ship-fight-in-asteroid-field]] — auto ship fight with rocks. A crewless Rebel scout engages on arrival inside an asteroid field; there are no… | `AUTO_ASTEROID` · hostile · both | Updated: 2026-08-09
- [[event-auto-ship-fight-in-nebula]] — The nebula's baseline forced fight against a Rebel drone. Three elements of XML — a text list, <ship… | `NEBULA_AUTO` · nebula · both | Updated: 2026-08-09
- [[event-auto-ship-fight-in-plasma-storm]] — The same Rebel drone as auto ship fight in nebula, but in a plasma storm and with three ways out. It is the… | `STORM_AUTO` · nebula · both | Updated: 2026-08-09
- [[event-auto-ship-fight-near-sun]] — The sun-hazard twin of auto ship fight in asteroid field, and the more dangerous of the two: a crewless Rebel… | `AUTO_SUN` · hostile · both | Updated: 2026-08-09
- [[event-auto-ship-near-radar-station]] — The most branching event in eventsrebel.xml, and the only one that can delay the Rebel fleet. A dormant… | `AUTO_DEFENSE_RADAR` · hostile · both | Updated: 2026-08-09
- [[event-auto-ship-near-sensor-station]] — A map-reveal beacon guarded by an auto-ship. Fight it for scrap and the map, or use one of two blue options… | `AUTO_DEFENSE_MAP` · hostile · both | Updated: 2026-08-09
- [[event-auto-ship-near-storage-station]] — An optional auto-ship fight guarding a military storage cache. Winning — or sneaking past with Cloaking —… | `AUTO_DEFENSE_ITEM` · hostile · both | Updated: 2026-08-09
- [[event-auto-ship-near-storage-station-in-nebula]] — A guarded Rebel storage station. Six choices — the widest blue-option spread of any event in eventsnebula.xml… | `NEBULA_AUTO_DEFENSE_ITEM` · nebula · ae | Updated: 2026-08-09
- [[event-auto-ship-warning]] — An auto-ship fight on a clock. Identical intro text to auto ship fight, but the enemy is running its FTL… | `AUTO_WARNING` · hostile · both | Updated: 2026-08-09
- [[event-auto-ship-warning-in-nebula]] — A timed kill. A Rebel drone is already charging its FTL when you arrive; you have 40 seconds to destroy it or… | `NEBULA_AUTO_WARNING` · nebula · both | Updated: 2026-08-09
- [[event-battlefield-survivor]] — The dying survivor pulled out of the nebula wreckage debris. With no medical systems you can only make their… | `BATTLEFIELD_SURVIVOR` · nebula · both | Updated: 2026-08-09
- [[event-battlefield-wreckage]] — The aftermath of a ship battle, and one of the few events in the game that pays off Sensors — a subsystem… | `WRECKAGE_EVENT` · any · ae | Updated: 2026-08-09
- [[event-boarders-humans-in-nebula]] — The nebula's ambush. No ship on the map, no choices, no reward — 2 to 4 human boarders simply appear inside… | `NEBULA_BOARDING` · nebula · both | Updated: 2026-08-09
- [[event-boarders-humans-in-plasma-storm]] — Salvage interrupted by a boarding party. Unlike its nebula twin boarders humans in nebula, this one pays —… | `STORM_BOARDING` · nebula · ae | Updated: 2026-08-09
- [[event-boarders-humans-jammed-sensors]] — boarders humans pirate with a twist: the same 3–5 human boarders, but a station jams your Sensors for the… | `BOARDERS_HACKING` · any · both | Updated: 2026-08-09
- [[event-boarders-humans-near-sun]] — Desperate pirates whose own ship is dying next to a star decide to take yours. 2–4 human boarders beam aboard… | `BOARDERS_SUN` · any · both | Updated: 2026-08-09
- [[event-boarders-humans-pirate]] — The plainest boarding event in the game and the archetype the others are variations on: 3–5 human boarders… | `BOARDERS` · any · both | Updated: 2026-08-09
- [[event-boarders-mantis]] — A no-choice ambush: you arrive, and 2–4 Mantis boarders are already on your ship. There is nothing to click… | `MANTIS_BOARDERS` · hostile · both | Updated: 2026-08-09
- [[event-boarders-rebels-in-nebula]] — Three to four human boarders teleport onto your ship from a nearby station, and there is no enemy ship at all… | `NEBULA_REBEL_BOARDING` · nebula · both | Updated: 2026-08-09
- [[event-boarders-rockmen-near-sun]] — The purest boarding beacon in Rock space: no enemy ship at all, just 2–3 Rockmen in your corridors while a… | `ROCK_BOARDERS_SUN` · hostile · both | Updated: 2026-08-09
- [[event-capture-the-ship]] — A quest start that is gated entirely behind crew-killing equipment. Without a Teleporter, Anti-Bio Beam or… | `QUEST_CREWDEAD_START` · quest · ae | Updated: 2026-08-09
- [[event-confused-mantis]] — An Engi ship asks you to talk down a Mantis who believes he is human. Send an untrained away team and you are… | `CONFUSED_MANTIS` · any · both | Updated: 2026-08-09
- [[event-crew-hiring-station]] — A mercenary hiring post. Two crew are on offer at independently rolled prices; you may take one or walk away.… | `TAVERN_HIRE` · any · both | Updated: 2026-08-09
- [[event-crushed-pirate]] — A pirate ship is pinned between two asteroids, having mined the belt without the gear for it. Every branch… | `DISTRESS_TRAPPED_MINER` · distress · both | Updated: 2026-08-09
- [[event-deactivated-auto-ship]] — A dormant Rebel auto-ship you can loot safely for LOW scrap, or gamble with for scrap and a map reveal at the… | `BROKEN_REBEL_DRONE` · any · both | Updated: 2026-08-09
- [[event-dense-asteroid-field-distress]] — Step 1 of crystal cruiser unlock — the beacon that can hand you the Damaged Stasis Pod. Searching is a… | `ASTEROID_DERELICT_SHIP` · distress · both · **ship-unlock** | Updated: 2026-08-09
- [[event-disabled-rock-ship]] — A salvage-or-walk-away beacon. Strip a derelict Rock transport for scrap at a 50% risk of a Rock patrol… | `ROCK_LOOTING` · any · both | Updated: 2026-08-09
- [[event-distress-engi-rebel-result]] — The trading half of the Engi distress ambush. Having beaten the Rebel fighter, you can pay the surviving Engi… | `DISTRESS_ENGI_REBEL_RESULT` · distress · both | Updated: 2026-08-09
- [[event-donor-mantis-chase2]] — The quest-marker half of the mantis ship collectors chase. The Mantis captain who ran from you has bought a… | `DONOR_MANTIS_CHASE2` · quest · both | Updated: 2026-08-09
- [[event-empty-beacon-civilian]] — The baseline empty beacon: you arrive, a line of scenery text plays, nothing happens, and you jump on. It is… | `NOTHING` · empty · both | Updated: 2026-08-09
- [[event-empty-beacon-engi]] — The Engi empty beacon: ten flavour texts, no choices, no effects. Its only mechanical role is to occupy… | `NOTHING_ENGI` · empty · both | Updated: 2026-08-09
- [[event-empty-beacon-mantis]] — The Mantis-flavoured empty beacon. One line of prose from a six-string list, no choices, no payload of any… | `NOTHING_MANTIS` · empty · both | Updated: 2026-08-09
- [[event-empty-beacon-rebel]] — The Rebel sector's empty beacon: five lines of flavour text and nothing else. Structurally required — every… | `NOTHING_REBEL` · empty · both | Updated: 2026-08-09
- [[event-empty-beacon-rock]] — The Rock sectors' filler beacon. Nothing happens: no choices, no ship, no reward. It exists so that a Rock… | `NOTHING_ROCK` · empty · both | Updated: 2026-08-09
- [[event-empty-beacon-slug]] — The Slug sectors' empty beacon outside the clouds. No choices, no effects; five flavour texts, all of which… | `NOTHING_SLUG` · empty · both | Updated: 2026-08-09
- [[event-empty-beacon-zoltan]] — The Zoltan sectors' "nothing happens" beacon. Mechanically inert, but its seven flavour strings are the… | `NOTHING_ZOLTAN` · empty · both | Updated: 2026-08-09
- [[event-empty-nebula-beacon]] — Nothing happens, nine different ways. NEBULAEMPTY is the nebula pool's filler: a text list, an environment… | `NEBULA_EMPTY` · nebula · both | Updated: 2026-08-09
- [[event-empty-nebula-beacon-slug]] — The Slug sectors' "nothing here" nebula beacon. No choices, no effects — six flavour texts and a jump onward.… | `NEBULA_NOTHING_SLUG` · empty · both | Updated: 2026-08-09
- [[event-encrypted-federation-signal]] — A quest-pool event that is a straight one-in-five gamble: send an away party and you get one of five results,… | `FEDERATION_PLANET_SIGNAL` · quest · both | Updated: 2026-08-09
- [[event-engi-cache]] — A clean two-way trade with no downside branch: spend 2 missiles to push the Rebel fleet back 2 jumps, or take… | `ENGI_FLEET_DELAY` · any · both | Updated: 2026-08-09
- [[event-engi-distress-rebel-fight]] — A distress beacon that is really an ambush: there is no choice, you simply fight a Rebel fighter. Winning… | `DISTRESS_ENGI_REBEL` · distress · both | Updated: 2026-08-09
- [[event-engi-fight]] — A mistaken-identity fight: an Engi escort blames you for a destroyed Zoltan cruiser and refuses all hails. No… | `ZOLTAN_ENGI` · hostile · ae | Updated: 2026-08-09
- [[event-engi-research-station]] — A unique distress beacon in Engi space with a real crew-loss risk attached to a real crew-gain reward.… | `DISTRESS_ENGI_REACTOR` · distress · both | Updated: 2026-08-09
- [[event-engi-ship-attacked-by-mantis-ship]] — The richest reward tree in Engi space, and the only event there that can hand you a quest marker. Answering… | `ENGI_STATION_DISTRESS` · any · both | Updated: 2026-08-09
- [[event-engi-smashed-ships]] — Two Engi ships are stuck together and it looks like a rescue. Helping starts a fight that pays nothing at all… | `ENGI_SEX` · any · both | Updated: 2026-08-09
- [[event-engi-surrender]] — An Engi ship surrenders its cargo before you have done anything. Taking the loot is a guaranteed payout;… | `ENGI_SURRENDER` · any · both | Updated: 2026-08-09
- [[event-escape-pod]] — A pure gamble with no cost to decline. Jettison the pod and nothing happens; pry it open and you draw one of… | `MANTIS_CREW` · any · both | Updated: 2026-08-09
- [[event-escort-civilians]] — A lightly-armed civilian ship asks for an escort. Accepting pays a small fuel down-payment immediately and… | `QUEST_ESCORT` · quest · both | Updated: 2026-08-09
- [[event-escort-civilians-ftl-haywire]] — A distress beacon where a civilian ship asks you to lead it to a repair depot. Accepting pays a token amount… | `ESCORT_BEACON` · distress · both | Updated: 2026-08-09
- [[event-fire-on-research-station]] — A laboratory fire is about to take a research station with it. Two unaided branches each roll a coin: help… | `DISTRESS_STATION_FIRE` · distress · both | Updated: 2026-08-09
- [[event-free-drone-schematic]] — A pure gift beacon: you arrive, you are handed a drone schematic and a little scrap, and that is the whole… | `FIND_DRONE` · any · both | Updated: 2026-08-09
- [[event-free-scrap-with-resources]] — The plainest event in the game: arrive, take a medium payout of scrap with resources, leave. No choices, no… | `FREE_ITEMS` · any · both | Updated: 2026-08-09
- [[event-free-scrap-with-resources-engi]] — Pure free loot. No choices, no risk, no fight — you arrive, the Engi hand you supplies, you leave. The only… | `ENGI_GIFT` · any · both | Updated: 2026-08-09
- [[event-free-scrap-with-resources-zoltan]] — An abandoned Zoltan freighter with nobody aboard. No choices, no cost, no catch — a RANDOM… | `ZOLTAN_DISTRESS_SHELL` · distress · both | Updated: 2026-08-09
- [[event-free-weapon]] — A pure gift beacon that hands you a weapon and a little scrap. No choices, no ship, no risk. Structurally… | `FIND_WEAPON` · any · both | Updated: 2026-08-09
- [[event-friendly-ship-out-of-fuel]] — A stranded civilian ship asks for fuel. Give 2–4 fuel and you get a gift from a four-outcome pool: high scrap… | `FRIENDLY_BEACON` · distress · both | Updated: 2026-08-09
- [[event-giant-alien-spiders]] — The most notorious event in FTL. Sending your crew to fight the spiders is a coin flip between losing a… | `DISTRESS_INFESTATION` · distress · both | Updated: 2026-08-09
- [[event-improve-reactor-for-supplies]] — A refugee convoy that will add a reactor bar in exchange for missiles, drone parts and/or fuel — no scrap… | `TRADER_UPGRADES_EXCHANGE` · any · ae | Updated: 2026-08-09
- [[event-intelligent-ponies]] — A three-level choice tree on a planet full of small six-legged horses. The peaceful route is a coin flip for… | `DONOR_PONY` · any · both | Updated: 2026-08-09
- [[event-large-asteroid-field]] — The game's most widely-distributed filler event: it sits in nearly every neutral pool, in both hardcoded… | `ASTEROID_EXPLORE` · any · both | Updated: 2026-08-09
- [[event-large-trade-station]] — A store you have to work for. The Rebels broadcast a warning not to trade with you, and searching for a… | `STORE_REBELSIDE` · store · ae | Updated: 2026-08-09
- [[event-malfunctioning-defense-system]] — A station's automated gun has gone rogue. The unaided answer — shoot it — is a coin flip between a small… | `DISTRESS_SATELLITE_DEFENSE` · distress · both · **cut-content** | Updated: 2026-08-09
- [[event-mantis-fight]] — The baseline hostile Mantis encounter: you arrive, a Mantis ship is already shooting, there are no choices.… | `MANTIS_FIGHT` · hostile · ae | Updated: 2026-08-09
- [[event-mantis-fight-choice]] — You spot a Mantis warship before it spots you. Attack, try to hide, or — with cloaking — cloak. Hiding is a… | `MANTIS_FIGHT_CHOICE` · any · both | Updated: 2026-08-09
- [[event-mantis-fight-engi]] — A forced Mantis fight, flavoured for Engi space. No choices — the event exists to put a generic Mantis ship… | `ENGI_MANTIS_FIGHT` · hostile · ae | Updated: 2026-08-09
- [[event-mantis-fight-in-nebula]] — A forced Mantis fight at a nebula beacon. Five flavour texts wrapped around <ship load="MANTISFIGHT"… | `NEBULA_MANTIS_FIGHT` · nebula · both | Updated: 2026-08-09
- [[event-mantis-fight-in-nebula-slug]] — A Mantis raider hunting Slugs on their own turf. No choices — you fight a standard Mantis ship at default… | `NEBULA_SLUG_MANTIS` · nebula · both | Updated: 2026-08-09
- [[event-mantis-fight-near-sun]] — mantis fight with a star hazard bolted on. Identical enemy (ship load="MANTISFIGHT"), identical lack of… | `MANTIS_SUN_FIGHT` · hostile · ae | Updated: 2026-08-09
- [[event-mantis-fight-slug]] — A Mantis raider hunting in Slug space. No choices, no escape route — the event body is a line of text and a… | `SLUG_MANTIS` · hostile · both | Updated: 2026-08-09
- [[event-mantis-fight-zoltan]] — A straight Mantis ambush in Zoltan space. No choices, default rewards, no boarders. The Mantis presence in a… | `ZOLTAN_MANTIS` · hostile · ae | Updated: 2026-08-09
- [[event-mantis-fugitive]] — A Mantis deserter teleports aboard while the Engi warship that was hunting him offers you a bounty. There is… | `ALISON_MANTIS_CREW` · hostile · both | Updated: 2026-08-09
- [[event-mantis-outcasts]] — A Mantis boarding action inside Zoltan space: 2–3 Mantis boarders land while a Mantis scout engages. Fewer… | `ZOLTAN_BOARDERS_MANTIS` · hostile · both | Updated: 2026-08-09
- [[event-mantis-ship-attacking-civilian]] — A Mantis warship is running down a civilian. You can intervene or jump on. Intervening is a fully optional… | `MANTIS_CIVILIAN` · any · both | Updated: 2026-08-09
- [[event-mantis-ship-attacking-slug-ship]] — A Mantis raider has a Slug ship cornered and the Slugs are begging for help. You can save them, finish them,… | `SLUG_DISTRESS_MANTIS` · distress · both | Updated: 2026-08-09
- [[event-mantis-ship-collectors]] — A no-choice Mantis ambush that turns into a two-part chase. The first ship always tries to run at low hull;… | `DONOR_MANTIS_CHASE` · hostile · both | Updated: 2026-08-09
- [[event-mantis-ship-with-rock-body-parts]] — A Mantis ship decorated with the remains of Rockmen it has killed. It is not hostile on arrival and you can… | `ROCK_MANTIS_HUNTER` · any · both | Updated: 2026-08-09
- [[event-mantis-ships-battle-for-rock-freighter]] — Two Mantis ships are fighting over a crippled Rock freighter. You can wait and take on the winner, walk away,… | `ROCK_MANTIS_FREIGHTER` · any · both | Updated: 2026-08-09
- [[event-mantis-war-camp]] — A settlement asks you to scout a Mantis war camp. Unusually for a quest start, accepting pays immediately… | `QUEST_MANTIS_INVASION_START` · quest · ae | Updated: 2026-08-09
- [[event-merchant-s-request]] — A quest-start beacon that branches into one of two errands: a delivery job (you are handed 5 drone parts and… | `MERCHANT_REQUEST` · quest · ae | Updated: 2026-08-09
- [[event-nebula-lost-ship]] — A free-crew event with a fight attached to the free option. Federation survivors vanish into the clouds;… | `NEBULA_LOST_SHIP` · nebula · both | Updated: 2026-08-09
- [[event-nebula-wreckage]] — A non-hostile unique nebula beacon in Slug space. Poking through the debris can cost you hull and start a… | `NEBULA_BATTLEFIELD` · nebula · ae | Updated: 2026-08-09
- [[event-pirate-briber]] — A pirate is running down another ship and offers you scrap to look the other way. Take the bribe for a small… | `PIRATE_BRIBER` · any · ae | Updated: 2026-08-09
- [[event-pirate-engine-hacker]] — A pirate remotely hacks your Engines down to level 1 and then attacks. You cannot flee and you cannot dodge —… | `PIRATE_NO_ESCAPE` · hostile · ae | Updated: 2026-08-09
- [[event-pirate-fight]] — The plain pirate ambush: you jump in, a pirate ship is hostile, there is no choice and no way out but… | `PIRATE` · hostile · ae | Updated: 2026-08-09
- [[event-pirate-fight-choice-in-nebula]] — A stranded pirate ship deep in Slug space. It sits in the NEBULAHOSTILESLUG list but the fight is optional —… | `NEBULA_SLUG_PIRATE` · nebula · both | Updated: 2026-08-09
- [[event-pirate-fight-engi]] — A forced pirate fight with a single fixed intro text and default rewards. The plainest event in the Engi… | `ENGI_PIRATE_FIGHT` · hostile · ae | Updated: 2026-08-09
- [[event-pirate-fight-in-asteroid-field]] — pirate fight with an asteroid field running. Same PIRATE ship, same default rewards, but incoming asteroids… | `PIRATE_ASTEROID` · hostile · ae · **cut-content** | Updated: 2026-08-09
- [[event-pirate-fight-in-nebula]] — A complete, fully authored pirate ambush — five flavour texts, a PIRATE ship, default rewards — that almost… | `NEBULA_PIRATE` · nebula · both · **unreachable** | Updated: 2026-08-09
- [[event-pirate-fight-near-pulsar]] — An ordinary pirate ambush with a pulsar on the board. Three lines of XML — a text list, a PIRATE ship, and… | `PIRATE_PULSAR` · hostile · ae | Updated: 2026-08-09
- [[event-pirate-fight-near-sun]] — pirate fight run inside a solar flare hazard. Same PIRATE ship and the same default rewards, but the star… | `PIRATE_SUN` · hostile · ae | Updated: 2026-08-09
- [[event-pirate-fight-slug]] — Pirates working the edges of Slug territory. A plain forced fight with three flavour variants — but against… | `SLUG_PIRATE` · hostile · both | Updated: 2026-08-09
- [[event-pirate-fight-zoltan]] — Filler combat: a pirate ship in Zoltan space, no choices, default rewards. Its only distinguishing feature is… | `ZOLTAN_PIRATE` · hostile · ae | Updated: 2026-08-09
- [[event-pirate-ship-attacking-civilian]] — A pirate is running down a civilian ship. Intervene and you fight a pirate that cannot surrender and cannot… | `PIRATE_CIVILIAN` · any · ae | Updated: 2026-08-09
- [[event-pirate-ship-attacking-civilian-distress]] — A distress-list encounter where a pirate is chasing a civilian. Killing the pirate opens the shared… | `PIRATE_CIVILIAN_BEACON` · distress · both | Updated: 2026-08-09
- [[event-pirate-ship-distress-trap]] — The distress-beacon tax. A distress signal that is simply bait: you arrive, a pirate opens fire, and there… | `TRAP_BEACON` · distress · both | Updated: 2026-08-09
- [[event-pirate-ship-selling-drones]] — A pirate advertising a shop. It is a genuine shop — a drone-parts, drone-schematic and Drone Control upgrade… | `PIRATE_SALESMAN` · any · ae | Updated: 2026-08-09
- [[event-pirate-ship-selling-weapon]] — A black-market weapon for 45 scrap, sight unseen — and a coin-flip chance the seller simply takes your scrap… | `NEBULA_WEAPONS_TRADER` · nebula · ae | Updated: 2026-08-09
- [[event-pirate-ships-in-plasma-storm]] — Two pirate ships, one carrying fuel and one carrying ammunition — you pick which to raid, or skip both.… | `STORM_ZOLTAN_SUPPLY_CHOICE` · nebula · both | Updated: 2026-08-09
- [[event-pirate-smuggler]] — A smuggler tries to slip past you. You can shake him down with a big enough gun deck, rob him outright, or… | `NEBULA_PIRATE_SMUGGLE` · nebula · both | Updated: 2026-08-09
- [[event-pirate-toll]] — A pirate ship is sitting at the beacon and wants a toll. Pay 15–25 scrap and nothing happens; refuse and it… | `PIRATE_CHOICE` · hostile · ae | Updated: 2026-08-09
- [[event-plagued-station]] — A gamble at an abandoned station: board it for a one-in-three shot at a free Human crew member, a… | `DONOR_PLAGUE` · any · both | Updated: 2026-08-09
- [[event-plasma-storm-incapacitated-ships]] — A ship graveyard in a plasma storm, and the richest loot table in eventsnebula.xml. Searching by hand is a… | `STORM_ITEMS` · nebula · both | Updated: 2026-08-09
- [[event-quest-slug-pirate-trap2]] — The quest-marker payoff of slug comm tapping. You arrive mid-raid and choose which pirate to fight: help the… | `QUEST_SLUG_PIRATE_TRAP2` · quest · both | Updated: 2026-08-09
- [[event-rebel-checkpoint]] — A Rebel inspection post holding up civilian traffic. You can pick a fight, buy the civilians' freedom for… | `REBEL_CHECKPOINT` · any · ae | Updated: 2026-08-09
- [[event-rebel-defector]] — A Rebel ship engages and a lone Rebel soldier teleports aboard begging to defect. The fight with the rebel… | `ALISON_DEFECTOR` · hostile · both | Updated: 2026-08-09
- [[event-rebel-fight]] — The baseline Rebel encounter and one of the most widely-reachable events in the game: you arrive, a Rebel… | `REBEL` · hostile · both | Updated: 2026-08-09
- [[event-rebel-fight-chance]] — An optional Rebel hunt. Searching blind is a gamble — you may not find him, and one branch costs you… | `ROGUE_REBEL` · any · ae | Updated: 2026-08-09
- [[event-rebel-fight-chance-in-nebula]] — You have the drop on a Rebel scout. Chasing it blind is a three-way roll that can cost you fleet position;… | `NEBULA_REBEL_CHASE` · nebula · ae | Updated: 2026-08-09
- [[event-rebel-fight-choice-in-nebula]] — A Rebel picket is waiting for you and hasn't seen you yet. Attack, hide, or cloak. Hiding is a three-way roll… | `NEBULA_REBEL_UNDETECTED` · nebula · both | Updated: 2026-08-09
- [[event-rebel-fight-engi]] — A forced Rebel fight with a single fixed intro text and default rewards. Its only flavour contribution is… | `ENGI_REBEL_FIGHT` · hostile · ae | Updated: 2026-08-09
- [[event-rebel-fight-in-nebula]] — Seven flavour texts and a Rebel ship — and the single most structurally important dead event in the nebula… | `NEBULA_REBEL` · nebula · both · **unreachable** | Updated: 2026-08-09
- [[event-rebel-fight-in-plasma-storm]] — Three elements of XML: text, a Rebel ship, a plasma storm. No choices, no blue options, no escape. It is the… | `STORM_REBEL` · nebula · both | Updated: 2026-08-09
- [[event-rebel-fight-near-pulsar]] — The Rebel twin of pirate fight near pulsar and structurally identical to it: a text list, a REBEL ship,… | `REBEL_PULSAR` · hostile · ae | Updated: 2026-08-09
- [[event-rebel-fight-slug]] — The Rebellion pushing into Slug nebula space. A forced fight with three flavour variants against the standard… | `SLUG_REBEL` · hostile · both | Updated: 2026-08-09
- [[event-rebel-fight-with-boarders]] — A Rebel ship fight with 2–3 human boarders already on your deck when the event resolves. One of only two… | `BOARDERS_REBEL_SHIP` · hostile · both | Updated: 2026-08-09
- [[event-rebel-ship-attacking-federation-loyalists]] — A Rebel scout is killing a Federation transport. Saving it opens a three-outcome rescue table that can hand… | `REBEL_VS_FEDERATION` · distress · both | Updated: 2026-08-09
- [[event-rebel-ship-attacking-refueling-outpost]] — The crewed twin of auto ship attacking outpost: intervene against a Rebel scout threatening a fuel depot, and… | `SQUAT_REFUEL_STATION` · hostile · both | Updated: 2026-08-09
- [[event-rebel-ship-supplying-civilians]] — A Rebel ship running humanitarian supplies to civilian colonies. The event's whole point is that the Rebels… | `REBEL_HELPERS` · any · ae | Updated: 2026-08-09
- [[event-rebel-ship-warning]] — The crewed twin of auto ship warning: a Rebel forward scout that is already charging its FTL when you arrive.… | `SQUAT_WARNING` · hostile · both | Updated: 2026-08-09
- [[event-rebel-transport-ship]] — A fleeing Rebel cargo hauler with the richest random loot table in eventsrebel.xml: eleven possible outcomes… | `REBEL_TRANSPORT` · hostile · both | Updated: 2026-08-09
- [[event-refueling-platform]] — A fuel vendor that is a coin flip between an honest station and a pirate trap. Docking loads one of two… | `FUELING_STATION` · any · ae | Updated: 2026-08-09
- [[event-refueling-station]] — A flat-rate fuel vendor: 2 scrap per fuel, in lots of 1, 3 or 6. No ship, no risk, no blue options — the only… | `REFUEL_STATION` · store · ae | Updated: 2026-08-09
- [[event-refugee]] — The same drifting refugee ship as refugee distress, but found by your sensors instead of by its beacon — no… | `REFUGEE_NO_DISTRESS` · any · ae | Updated: 2026-08-09
- [[event-refugee-comms-down]] — The grim member of the refugee family. Same drifting ship, same dead beacon, but the comms are out — so there… | `REFUGEE_GHOST` · distress · both | Updated: 2026-08-09
- [[event-refugee-distress]] — A stranded refugee ship broadcasting a distress beacon. Hailing it is a coin flip: half the time it is an… | `REFUGEE_DISTRESS` · distress · both | Updated: 2026-08-09
- [[event-refugee-distress-slug]] — The Slug-sector cut of refugee distress. Same prose, same two choices, but the hail pool is two entries… | `REFUGEE_DISTRESS_SLUG` · distress · both | Updated: 2026-08-09
- [[event-refugee-distress-zoltan]] — The Zoltan-sector cut of refugee distress. Same prose, same two choices, two-entry hail pool: a trade, or a… | `REFUGEE_DISTRESS_ZOLTAN` · distress · both | Updated: 2026-08-09
- [[event-refugee-slug]] — The Slug-nebula, no-distress cut of the refugee encounter, and the only member of the refugee family that… | `REFUGEE_NO_DISTRESS_SLUG` · nebula · both | Updated: 2026-08-09
- [[event-refugee-trader]] — The good half of every refugee encounter. Eight different parent events funnel into this one node: a refugee… | `REFUGEE_TRADER` · any · both | Updated: 2026-08-09
- [[event-refugee-zoltan]] — The Zoltan-sector, no-distress cut of the refugee encounter. Two-entry hail pool: barter, or a Zoltan warship… | `REFUGEE_NO_DISTRESS_ZOLTAN` · any · both | Updated: 2026-08-09
- [[event-remote-settlement]] — A pirate is shaking down a farming settlement. You can fight the pirate for a modest, multi-stage reward —… | `PIRATE_STATION_CROPS` · any · both | Updated: 2026-08-09
- [[event-repair-station]] — A flat-rate hull repair vendor: 2 scrap per hull point, in lots of 5, 10 or 20. No ship, no risk, no blue… | `REPAIR_STATION` · store · ae | Updated: 2026-08-09
- [[event-research-station-with-no-response]] — A silent research station that turns out to be full of people driven violently insane by an alien neurotoxin.… | `STATION_SICK` · distress · both | Updated: 2026-08-09
- [[event-rock-and-slug-standoff]] — A Slug crew upgraded a Rock ship's reactor and the Rock captain will not pay. Intervening is the only route… | `ROCK_SLUG_ARGUMENT` · any · ae | Updated: 2026-08-09
- [[event-rock-atheists]] — One of the few reliable sources of a free Rockman crew member. A Rock dissident ship wants out of Rock… | `ROCK_ATHIEST` · hostile · both | Updated: 2026-08-09
- [[event-rock-bride]] — A two-beacon quest: accept a Rock bride as cargo, then decide at Numa V whether to deliver her or keep her.… | `ROCK_QUEST_MARRIAGE_START` · quest · both | Updated: 2026-08-09
- [[event-rock-fight]] — The baseline Rock combat encounter and the single most-reused Rock event in the game. It is an unavoidable… | `ROCK_SHIP` · hostile · both | Updated: 2026-08-09
- [[event-rock-fight-in-asteroid-field]] — rock fight with an asteroid field bolted on. Same enemy (ROCKSHIP), same lack of choices, but <environment… | `ROCK_FIGHT_ASTEROID` · hostile · both | Updated: 2026-08-09
- [[event-rock-fight-in-nebula]] — Rock refugees hiding from the Zoltan border police open fire rather than let you leave with their position.… | `NEBULA_ZOLTAN_ROCK` · nebula · both | Updated: 2026-08-09
- [[event-rock-fight-with-boarders]] — The nastiest of the plain Rock beacons: you fight a Rock ship and 1–3 Rockmen teleport aboard on arrival,… | `ROCK_BOARDERS_SHIP` · hostile · both | Updated: 2026-08-09
- [[event-rock-fight-with-boarders-in-asteroid-field]] — A Rock ship fight, plus 1–2 Rockman boarders on arrival, plus an asteroid field. Three pressures at once and… | `ROCK_BOARDERS_ASTEROID` · hostile · both | Updated: 2026-08-09
- [[event-rock-live-mine]] — A drilling mine latches onto your hull and you have to get it off. Without a blue option this is one of the… | `ROCK_STARSHIP_MINE` · any · both | Updated: 2026-08-09
- [[event-rock-pirates-fight]] — An unavoidable fight against a Rock pirate ship. Mechanically identical in structure to rock fight — no… | `ROCK_PIRATE` · hostile · both | Updated: 2026-08-09
- [[event-rock-pirates-fight-in-asteroid-field]] — rock pirates fight with <environment type="asteroid"/ attached: an unavoidable fight against a ROCKPIRATE… | `ROCK_PIRATE_ASTEROID` · hostile · both | Updated: 2026-08-09
- [[event-rock-pirates-fight-near-sun]] — rock pirates fight with <environment type="sun"/: an unavoidable fight against a ROCKPIRATE ship next to a… | `ROCK_PIRATE_SUN` · hostile · both | Updated: 2026-08-09
- [[event-rock-quest-marriage]] — The second beacon of the Rock bride quest, and a clean moral fork with a clean mechanical one behind it. Hand… | `ROCK_QUEST_MARRIAGE` · quest · both | Updated: 2026-08-09
- [[event-sell-drone-parts-for-scrap]] — A flat-rate buyer for drone parts: 4 scrap per part, in lots of 3, 6 or 12. No ship, no risk, no blue… | `SELL_DRONES_STATION` · store · ae | Updated: 2026-08-09
- [[event-sell-missiles-for-scrap]] — A black-market buyer for missiles: 3 scrap per missile, in lots of 5, 10 or 15. The mechanical twin of sell… | `SELL_MISSILES_STATION` · store · ae | Updated: 2026-08-09
- [[event-settlement-mercenary-work]] — A quest-start beacon that offers you one of two different jobs, picked at random: rescue a space dock from a… | `MERCENARY_WORK_START` · quest · ae | Updated: 2026-08-09
- [[event-single-life-form-on-moon]] — The widest crew-reward event in the base game and the deepest nested tree in events.xml. A distress beacon… | `STRANDED_BEACON` · distress · both | Updated: 2026-08-09
- [[event-slaver-friendly]] — A slave trader offers to sell you a "laborer". Buying is the cheapest reliable crew member in the game —… | `FRIENDLY_SLAVER` · any · ae | Updated: 2026-08-09
- [[event-slaver-hostile]] — A well-armed slaver demands one of your crew as the price of passage. Hand a crew member over — permanently,… | `PIRATE_SLAVER` · hostile · ae | Updated: 2026-08-09
- [[event-slocknog]] — A marooned Slug named Slocknog offers to sell you his services for 55 scrap. Refuse and he immediately offers… | `SLUG_DISTRESS_RESCUE` · nebula · both | Updated: 2026-08-09
- [[event-slug-and-rock-standoff-in-nebula]] — A two-line nebula wrapper around rock and slug standoff. You detect ships running hot somewhere in the murk;… | `ROCK_SLUG_ARGUMENT_NEBULA` · nebula · both | Updated: 2026-08-09
- [[event-slug-comm-tapping]] — Two Slug ships plotting a raid on a wealthy pirate, unaware you are listening. Tapping the comms is entirely… | `QUEST_SLUG_PIRATE_TRAP` · nebula · both | Updated: 2026-08-09
- [[event-slug-drink]] — A Slug captain boards your ship uninvited with a flask and a toast. Drinking is a coin flip: 10 hull repaired… | `SLUG_DRINK` · nebula · both | Updated: 2026-08-09
- [[event-slug-fight]] — The plain Slug ambush outside the clouds: no choices, no environment, straight into a fight with a standard… | `SLUG_FIGHT` · hostile · both | Updated: 2026-08-09
- [[event-slug-fight-in-nebula]] — The bread-and-butter Slug nebula ambush. Five flavour texts, no choices, one Slug ship at default rewards.… | `NEBULA_SLUG_FIGHT` · nebula · both | Updated: 2026-08-09
- [[event-slug-fight-in-plasma-storm]] — A Slug ship ambushing you inside an ion storm. Mechanically it is the ordinary JELLY fight — 50% surrender,… | `STORM_SLUG_FIGHT` · hostile · both | Updated: 2026-08-09
- [[event-slug-hacker-choice]] — A Slug hacker lets you pick which of your systems he cripples before he attacks. Every answer starts a fight… | `NEBULA_SLUG_CHOOSE_DEATH` · nebula · both | Updated: 2026-08-09
- [[event-slug-hacker-doors]] — A forced fight in which your Door system is hacked offline and the enemy is guaranteed a fire weapon — the… | `NEBULA_SLUG_DOORS` · nebula · both | Updated: 2026-08-09
- [[event-slug-hacker-medical]] — Two Slug boarders teleport aboard while your Medbay and Clone Bay are hacked offline — a boarding fight with… | `NEBULA_SLUG_MEDBAY` · nebula · both | Updated: 2026-08-09
- [[event-slug-hacker-oxygen]] — Your Oxygen system is hacked to zero and the Slug attacks with a fire weapon. Suffocation plus fire, with no… | `NEBULA_SLUG_OXYGEN` · nebula · both | Updated: 2026-08-09
- [[event-slug-moons-question]] — A marooned Slug offers to join your crew if you can say how many moons orbit the planet you're standing off.… | `SLUG_DISTRESS_QUESTION` · distress · both | Updated: 2026-08-09
- [[event-slug-oxygen-malfunction]] — A Slug ship asks you to send crew over to fix its life support. Two thirds of the time it is an ambush that… | `SLUG_DISTRESS_TRICK` · nebula · both | Updated: 2026-08-09
- [[event-slug-repair-station]] — A Slug repair station offers to patch your hull. Accepting free repairs docks you to the station and then… | `NEBULA_SLUG_HULLFIX` · nebula · both | Updated: 2026-08-09
- [[event-slug-ship-boarding-rock-ship]] — Slugs are boarding a disabled Rock freighter. Intervening is a coin flip between a free bloodless win and a… | `SLUG_DISTRESS_ROCK` · distress · both | Updated: 2026-08-09
- [[event-slug-store-ship]] — A Slug merchant offers to show you his wares, then stalls you through three pages of legal disclaimers while… | `NEBULA_SLUG_FAKE_STORE` · nebula · both | Updated: 2026-08-09
- [[event-slug-surrender]] — The surrender offer made by the standard Slug hull. Accepting ends the fight and pays out one of three… | `SLUG_SURRENDER` · hostile · both | Updated: 2026-08-09
- [[event-space-station-under-construction]] — An Advanced Edition quest beacon: a half-built station has lost contact with its supply freighter and wants… | `QUEST_CONSTRUCTIONYARD` · quest · ae | Updated: 2026-08-09
- [[event-start-beacon-engi]] — The text you get on arriving in an Engi sector. It is the sector's <startEvent, not a random encounter —… | `START_BEACON_ENGI` · any · both | Updated: 2026-08-09
- [[event-start-beacon-mantis]] — The arrival beacon for both Mantis sector types — the text you see the moment you jump in, before anything… | `START_BEACON_MANTIS` · any · both | Updated: 2026-08-09
- [[event-start-beacon-rebel]] — The text you get on arriving in a Rebel sector. Five variants, all saying the same thing in different words:… | `START_BEACON_REBEL` · empty · both | Updated: 2026-08-09
- [[event-start-beacon-rock]] — The beacon you arrive on when you jump into a Rock sector. It is a structural event, not an encounter: it… | `START_BEACON_ROCK` · empty · both | Updated: 2026-08-09
- [[event-start-beacon-slug]] — The arrival beacon for both Slug sectors. Mechanically empty — it prints one of five scene-setting strings… | `START_BEACON_SLUG` · empty · both | Updated: 2026-08-09
- [[event-start-beacon-zoltan]] — The arrival beacon for both Zoltan sectors. Mechanically empty — it exists to print one of four scene-setting… | `START_BEACON_ZOLTAN` · empty · both | Updated: 2026-08-09
- [[event-store]] — The generic store beacon — the one used by sectors that have no faction-flavoured store event of their own.… | `STORE` · store · both | Updated: 2026-08-09
- [[event-store-engi]] — The Engi store beacon. Three flavour texts, then a store opens. Notable mainly for its allocation: two to… | `STORE_ENGI` · store · both | Updated: 2026-08-09
- [[event-store-in-nebula-slug]] — The Slug sectors' own store beacon, sited inside the clouds. No choices, no risk — the store just opens. It… | `NEBULA_STORE_SLUG` · store · both | Updated: 2026-08-09
- [[event-store-mantis]] — The Mantis-flavoured store beacon. Six flavour intros wrapped around a single <store/ tag — mechanically… | `STORE_MANTIS` · store · both | Updated: 2026-08-09
- [[event-store-rebel]] — The Rebel sector's store beacon. Three lines of flavour explaining why a Rebel-aligned station will trade… | `STORE_REBEL` · store · both | Updated: 2026-08-09
- [[event-store-rock]] — The Rock-flavoured store beacon. It opens a store and nothing else; the flavour text exists to explain why… | `STORE_ROCK` · store · both | Updated: 2026-08-09
- [[event-store-zoltan]] — The Zoltan sectors' store beacon. Purely a store opening with flavour text — no choices, no cost, no risk.… | `STORE_ZOLTAN` · store · both | Updated: 2026-08-09
- [[event-terraforming-scan]] — A Federation terraforming crew needs a planetary life-scan they can't power themselves. Helping is free and… | `TERRAFORMING_SCAN` · any · ae | Updated: 2026-08-09
- [[event-the-black-raven]] — A donor event: Captain Nights, a Slug pirate in a Slug Assault cruiser, challenges you to a duel in the best… | `DONOR_BLACK_RAVEN` · hostile · both | Updated: 2026-08-09
- [[event-the-engi-virus]] — The densest blue-option event in Engi space: five separate gates (Hacking at three levels, Engi crew, Lanius… | `ENGI_VIRUS` · any · ae | Updated: 2026-08-09
- [[event-the-mercenary]] — A pirate-marked ship sells you one of two services for scrap: two turns of Rebel fleet delay, or a full… | `MERCENARY` · any · ae | Updated: 2026-08-09
- [[event-trade-fuel-for-drone-parts]] — A flat trade at an item beacon: 2–4 fuel for 1–3 drone parts, take it or leave it. No risk, no branching, no… | `FUEL_FOR_DRONE` · any · both | Updated: 2026-08-09
- [[event-trade-resources]] — A pure resource-swap beacon: a trader offers one of four fixed exchanges, converting a surplus resource into… | `TRADER_CIV` · any · both | Updated: 2026-08-09
- [[event-trade-resources-in-nebula]] — A barter stall in a nebula. Two choices — trade or ignore — and the trade is a swap of one resource for… | `NEBULA_TRADER` · nebula · both | Updated: 2026-08-09
- [[event-trade-scrap-for-upgrades]] — A mobile shipwright who will sell you exactly one (sub)system upgrade for scrap. Which one is offered is… | `TRADER_UPGRADES` · any · ae | Updated: 2026-08-09
- [[event-unknown-disease-on-mining-colony]] — A quarantine riot on a human mining colony. Sending your own crew is a coin flip: half the time nothing… | `DISTRESS_STATION_DISEASE` · distress · both | Updated: 2026-08-09
- [[event-zoltan-border-police]] — An unavoidable boarding action: 3–4 Zoltan boarders appear aboard your ship at the same moment a Zoltan… | `ZOLTAN_BOARDERS` · hostile · both | Updated: 2026-08-09
- [[event-zoltan-fight]] — The baseline hostile encounter of Zoltan space: a Zoltan warship, no choices, default rewards. It is… | `ZOLTAN_FIGHT` · hostile · ae | Updated: 2026-08-09
- [[event-zoltan-fight-in-asteroid-field]] — zoltan fight with an asteroid field bolted on. No choices, default rewards, and the environment runs for the… | `ZOLTAN_ASTEROID` · hostile · ae | Updated: 2026-08-09
- [[event-zoltan-free-augment]] — A free augment with low scrap, no choices and no cost. One of the purest positive beacons in the game — the… | `ZOLTAN_FREE_AUGMENT` · any · both | Updated: 2026-08-09
- [[event-zoltan-free-map]] — A free reveal of the entire current sector map, with no choices and no cost. Functionally a one-shot long… | `ZOLTAN_FREE_MAP` · any · both | Updated: 2026-08-09
- [[event-zoltan-great-eye]] — A pure gamble in a Zoltan nebula. Looking into the "Great Eye" rolls one of four outcomes ranging from a free… | `NEBULA_ZOLTAN_EYE` · nebula · both | Updated: 2026-08-09
- [[event-zoltan-odd-moon]] — A completely safe exploration event — no branch leads to combat or damage. Checking it out rolls one of four… | `ZOLTAN_ODD_MOON` · any · both | Updated: 2026-08-09
- [[event-zoltan-quest-primitives]] — A pick-a-side fight over an uncontacted primitive world. Siding with the Zoltan (attack the Rebel) pays a… | `ZOLTAN_QUEST_PRIMITIVES` · quest · both | Updated: 2026-08-09
- [[event-zoltan-research-facility]] — Step 2 of crystal cruiser unlock. On its own it is a small trade-your-scans-for- scrap event with a 1-in-3… | `ZOLTAN_CREW_STUDY` · any · both · **ship-unlock** | Updated: 2026-08-09
- [[event-zoltan-retake-the-ship]] — A rescued Zoltan asks you to clear pirates off his ship without destroying it. The game rewards exactly that:… | `ZOLTAN_LIFERAFT` · any · both | Updated: 2026-08-09
- [[event-zoltan-rift-success]] — The payout event that fires after you win any of the three fights the mad Zoltan wise man summons at zoltan… | `ZOLTAN_RIFT_SUCCESS` · any · both | Updated: 2026-08-09
- [[event-zoltan-security-checkpoint]] — A neutral Zoltan checkpoint with two blue options that both pay the same reward. Without one of them,… | `ZOLTAN_CREW_SCAN` · any · both | Updated: 2026-08-09
- [[event-zoltan-ship-asks-to-dock]] — A Zoltan science ship asks to come alongside. Docking is a coin flip: half the time they hand you a medium… | `ZOLTAN_SCIENCE_DOCK` · any · both | Updated: 2026-08-09
- [[event-zoltan-ship-follows-mantis-ship]] — A distress beacon where the Zoltan explicitly ask you not to help. Both interference options lead to the same… | `ZOLTAN_DISTRESS_MANTIS` · distress · both | Updated: 2026-08-09
- [[event-zoltan-trade-hub]] — A Zoltan trading station you need papers to enter. Getting in is the whole event: a Teleporter or a Zoltan… | `ZOLTAN_TRADE_HUB` · quest · both | Updated: 2026-08-09
- [[event-zoltan-wise-man]] — A mad Zoltan opens a wormhole and lets you pick your opponent — Mantis, Slug, or Rock. There is no way out;… | `ZOLTAN_RIFT_FIGHT` · any · both · **cut-content** | Updated: 2026-08-09

### No sector allocation

_Reached by quest marker, fleet or boss logic, or unreachable — see [[concept-sector-event-allocation]]._

- [[event-auto-bait]] — A fully authored auto-ship encounter that is not reachable in the shipped game. It inverts auto ship warning:… | `AUTO_BAIT` · both · **unreachable** · **cut-content** | Updated: 2026-08-09
- [[event-boarders-asteroid]] — Fully authored but, as far as the sector data goes, unreachable. A pirate stronghold teleports 2–4 human… | `BOARDERS_ASTEROID` · both · **unreachable** | Updated: 2026-08-09
- [[event-boss-fleets-both]] — The peaceful half of the battle-background pair in the last stand: you arrive beside a raging fleet… | `BOSS_FLEETS_BOTH` · empty · both | Updated: 2026-08-09
- [[event-boss-stalemate]] — A single line of prose the engine appears to call when a fight ends without a winner and the enemy FTLs out.… | `BOSS_STALEMATE` · both | Updated: 2026-08-09
- [[event-crew-stuck]] — The line the game shows when your boarding party is on an enemy ship and your Teleporter is destroyed beyond… | `CREW_STUCK` · both | Updated: 2026-08-09
- [[event-derelict-treasure]] — A three-variant salvage beacon with a real risk/reward split and a strong Engi blue option: salvage blind for… | `DERELICT_TREASURE` · both · **unreachable** | Updated: 2026-08-09
- [[event-dock-bomb-salesman]] — A fully authored weapons shop — missiles, a cheap bomb launcher, an expensive missile launcher — that cannot… | `DOCK_BOMB_SALESMAN` · both · **unreachable** · **cut-content** | Updated: 2026-08-09
- [[event-dock-drone-salesman]] — The shop you actually get to after boarding the pirate salesman's ship: drone parts, a random drone… | `DOCK_DRONE_SALESMAN` · any · ae | Updated: 2026-08-09
- [[event-engi-monster]] — A finished, fully-written unique event that cannot be reached in normal play: its only reference in the event… | `ENGI_MONSTER` · both · **unreachable** · **cut-content** | Updated: 2026-08-09
- [[event-engi-refugees]] — A damaged Engi refugee freighter asks for help. Pay scrap and you get thanks; send an Engi crew member with… | `ENGI_REFUGEES` · both · **unreachable** | Updated: 2026-08-09
- [[event-engi-unlock-2fake]] — The decoy half of stealth cruiser unlock. Identical intro text to engi unlock 2real, identical setup, and no… | `ENGI_UNLOCK_2FAKE` · quest · both | Updated: 2026-08-09
- [[event-engi-unlock-2fake-surrender]] — The surrender dialogue at the decoy Rebel base. The scout admits the envoy you followed was a fake, and you… | `ENGI_UNLOCK_2FAKE_SURRENDER` · quest · both | Updated: 2026-08-09
- [[event-engi-unlock-2real]] — Step 2 of stealth cruiser unlock, and the step most likely to lose you the ship unlock. A Rebel scout that… | `ENGI_UNLOCK_2REAL` · quest · both | Updated: 2026-08-09
- [[event-engi-unlock-2real-surrender]] — The surrender dialogue at the real Rebel base in stealth cruiser unlock. Short and entirely positive: the… | `ENGI_UNLOCK_2REAL_SURRENDER` · quest · both | Updated: 2026-08-09
- [[event-engi-unlock-3]] — Step 3 of stealth cruiser unlock: you catch the stolen-technology convoy, an Engi pirate squadron jumps in to… | `ENGI_UNLOCK_3` · quest · both | Updated: 2026-08-09
- [[event-engi-unlock-4]] — The payoff of stealth cruiser unlock. The Engi explain that the stolen technology is an advanced stealth… | `ENGI_UNLOCK_4` · quest · both · **ship-unlock** | Updated: 2026-08-09
- [[event-finish-beacon]] — The event that fires when you arrive at a sector's exit beacon. It is a structural event — the engine calls… | `FINISH_BEACON` · exit · both | Updated: 2026-08-09
- [[event-finish-beacon-nebula]] — The exit-beacon event used when the sector's Long-Range Beacon sits inside a nebula. Unlike its non-nebula… | `FINISH_BEACON_NEBULA` · exit · both · **cut-content** | Updated: 2026-08-09
- [[event-fleet-easy]] — What happens when you sit at a beacon the Rebel fleet has just claimed: an elite Rebel scout engages you… | `FLEET_EASY` · hostile · both | Updated: 2026-08-09
- [[event-fleet-easy-again]] — The "you stayed too long again" event: a second Rebel scout jumping in on a beacon the fleet already owns.… | `FLEET_EASY_AGAIN` · hostile · both · **unreachable** · **cut-content** | Updated: 2026-08-09
- [[event-fleet-easy-beacon]] — You reach the sector's exit beacon and the Rebel fleet is already there. An elite Rebel scout engages and you… | `FLEET_EASY_BEACON` · exit · both | Updated: 2026-08-09
- [[event-fleet-easy-beacon-dlc]] — The Advanced Edition variant of fleet easy beacon. Same prose, same elite Rebel ship, same +1 fuel payout —… | `FLEET_EASY_BEACON_DLC` · exit · both | Updated: 2026-08-09
- [[event-fleet-easy-dlc]] — The Advanced Edition-suffixed duplicate of fleet easy. Its definition, its ship, its environment and even its… | `FLEET_EASY_DLC` · hostile · ae | Updated: 2026-08-09
- [[event-fleet-easy-nebula]] — The nebula version of the "the Rebel fleet has caught you" fight. Fully authored — its own prose string, an… | `FLEET_EASY_NEBULA` · both · **unreachable** | Updated: 2026-08-09
- [[event-fleet-hard]] — The harder framing of the fleet-takeover encounter: a Rebel scout engages and the prose tells you outright to… | `FLEET_HARD` · hostile · both | Updated: 2026-08-09
- [[event-free-augment]] — One line of text and a free random augment, with no choices and no risk. It is not reachable in normal play —… | `FREE_AUGMENT` · both · **unreachable** | Updated: 2026-08-09
- [[event-fuel-escape-asteroids]] — A one-line resolution event: you were stranded without fuel in an asteroid field and have now navigated clear… | `FUEL_ESCAPE_ASTEROIDS` · both | Updated: 2026-08-09
- [[event-fuel-escape-fleet]] — A one-line resolution event: your pilot is dodging fleet artillery while you work out what to do next. No… | `FUEL_ESCAPE_FLEET` · ae | Updated: 2026-08-09
- [[event-fuel-escape-pds]] — A one-line resolution event: you were stranded without fuel under a hostile planet's Anti-Ship Battery and… | `FUEL_ESCAPE_PDS` · ae | Updated: 2026-08-09
- [[event-fuel-escape-pulsar]] — A one-line resolution event: you were stranded without fuel at a pulsar and have now pulled clear of it. No… | `FUEL_ESCAPE_PULSAR` · ae | Updated: 2026-08-09
- [[event-fuel-escape-storm]] — A one-line resolution event: you were stranded without fuel in an ion storm and the storm has now passed. No… | `FUEL_ESCAPE_STORM` · both | Updated: 2026-08-09
- [[event-fuel-escape-sun]] — A one-line resolution event: you were stranded without fuel next to a star and have now drifted clear of it… | `FUEL_ESCAPE_SUN` · both | Updated: 2026-08-09
- [[event-fuel-fleet-distress]] — A fully authored duplicate of no fuel rebel fleet delay built for the distress-beacon-on pool — and then… | `FUEL_FLEET_DISTRESS` · both · **unreachable** | Updated: 2026-08-09
- [[event-fuel-off-rock-curious]] — A complete out-of-fuel encounter — prose, two choices, an outcome list, a bespoke enemy hull with its own… | `FUEL_OFF_ROCK_CURIOUS` · any · both · **unreachable** | Updated: 2026-08-09
- [[event-lanius-boarders]] — A finished boarding ambush — three Lanius board you out of a derelict husk, with no ship, no choices and no… | `LANIUS_BOARDERS` · ae · **unreachable** · **cut-content** | Updated: 2026-08-09
- [[event-lone-shuttle]] — A silent one-man shuttle drifts toward you. Shoot it down for a 1/3 chance at scrap and fuel from grateful… | `LONE_SHUTTLE` · both · **unreachable** | Updated: 2026-08-09
- [[event-mantis-capture-commando]] — A moral-choice prisoner event: you salvage an Engi wreck and find the lone survivor of the Mantis boarding… | `MANTIS_CAPTURE_COMMANDO` · ae | Updated: 2026-08-09
- [[event-mantis-gamble]] — A 50-scrap bet on a Mantis arena fight: pick blue or red, win 100 scrap or owe the house. The losing branch… | `MANTIS_GAMBLE` · both | Updated: 2026-08-09
- [[event-merchant-deliver]] — The delivery destination of merchant s request. You arrive carrying the 5 drone parts the merchant gave you… | `MERCHANT_DELIVER` · quest · both | Updated: 2026-08-09
- [[event-merchant-investigate]] — The investigation destination of merchant s request. You search for a missing freighter and find one of three… | `MERCHANT_INVESTIGATE` · quest · both | Updated: 2026-08-09
- [[event-merchant-investigate-deliver]] — The terminal payoff of the investigation branch of merchant s request. It is a pure reward beacon: no… | `MERCHANT_INVESTIGATE_DELIVER` · quest · both | Updated: 2026-08-09
- [[event-no-fuel-auto-ship-warning]] — The worst draw in the distress-on pool. A Rebel automated scout answers your beacon, identifies you, and… | `FUEL_ON_REBEL_WARNING` · distress · both | Updated: 2026-08-09
- [[event-no-fuel-automated-refueling-ship]] — The single best draw in the distress-on pool. An automated refueller answers your beacon and hands out free… | `FUEL_SELLER_DISTRESS` · distress · both | Updated: 2026-08-09
- [[event-no-fuel-drifting-debris]] — A gutted Rock frigate drifts past while you are stranded. Boarding it is the only out-of-fuel event that can… | `FUEL_OFF_ROCK_WRECK` · any · both | Updated: 2026-08-09
- [[event-no-fuel-engi-ship-repair]] — An Engi ship drifts past while you are stranded, discussing repairs. Hailing them is a four-way coin flip… | `FUEL_OFF_ENGI_DUBIOUS` · any · both | Updated: 2026-08-09
- [[event-no-fuel-explore-the-system]] — Stranded with no fuel, you can burn impulse power to poke around the system. It is the only out-of-fuel event… | `FUEL_EXPLORE` · any · both | Updated: 2026-08-09
- [[event-no-fuel-fleet]] — What happens when you run out of fuel and stall long enough for the Rebel fleet to reach your beacon. There… | `NO_FUEL_FLEET` · both | Updated: 2026-08-09
- [[event-no-fuel-fleet-dlc]] — The Advanced Edition version of no fuel fleet. Same predicament, same elite Rebel fuel carrier, same 2–4 fuel… | `NO_FUEL_FLEET_DLC` · ae | Updated: 2026-08-09
- [[event-no-fuel-friendly-refugee]] — Pure charity, and the only unconditional-gain draw in the distress-beacon-off out-of-fuel pool. A refugee… | `NO_FUEL_REFUGEE_FRIENDLY` · any · ae | Updated: 2026-08-09
- [[event-no-fuel-fuel-trader-distress-off]] — A merchant offers to barter fuel while you are stranded with your distress beacon off. Its one non-obvious… | `FUEL_TRADER` · any · both | Updated: 2026-08-09
- [[event-no-fuel-fuel-trader-distress-on]] — The distress-beacon-on twin of no fuel fuel trader distress off. Mechanically identical: same friendly… | `FUEL_TRADER_DISTRESS` · distress · both | Updated: 2026-08-09
- [[event-no-fuel-mantis-fight]] — One of two "your distress call was answered by the wrong people" draws. A Mantis ship answers your beacon and… | `FUEL_ON_MANTIS_ATTACK` · distress · both | Updated: 2026-08-09
- [[event-no-fuel-prepare-to-dock]] — One of the encounters that can fire when you sit at a beacon with zero fuel. A ship offers to dock and refuel… | `FUEL_APPROACH` · any · both | Updated: 2026-08-09
- [[event-no-fuel-rebel-fight]] — Your distress call is answered by a Rebel fighter that recognises you. No choices; the fight starts… | `FUEL_ON_REBEL_ATTACK` · distress · both | Updated: 2026-08-09
- [[event-no-fuel-rebel-fleet-delay]] — The best possible outcome of waiting at a beacon with no fuel and your distress beacon off: the Rebel fleet… | `FUEL_FLEET_DELAY` · any · both | Updated: 2026-08-09
- [[event-no-fuel-refugee-damaged]] — A refugee ship with a wrecked hull answers your distress call and wants scrap for its spare fuel. The stated… | `NO_FUEL_REFUGEE_DAMAGED` · distress · both | Updated: 2026-08-09
- [[event-no-fuel-refugee-pirate]] — A refugee ship answers your distress call wanting weapons, not scrap. The name gives away the twist: half of… | `NO_FUEL_REFUGEE_PIRATE` · distress · both | Updated: 2026-08-09
- [[event-no-fuel-slug-fuel-depot]] — A mobile Slug fuel depot with the worst prices in the game — 10 scrap per fuel unit, against the 3-per-unit… | `FUEL_ON_SLUG_OVERPRICED` · distress · both | Updated: 2026-08-09
- [[event-no-fuel-slug-fuel-trader]] — A chuckling Slug offers a fair-looking price on fuel. The price is fair — 15 scrap for 5 fuel — but half the… | `FUEL_ON_SLUG_CHUCKLE` · distress · both | Updated: 2026-08-09
- [[event-no-fuel-wait-fail-distress-off]] — The single most likely thing to happen when you wait at a beacon with no fuel and your distress beacon off:… | `FUEL_NOTHING` · any · both | Updated: 2026-08-09
- [[event-no-fuel-wait-fail-distress-on]] — The "no one came" draw for waiting at a beacon with no fuel and the distress beacon on. It is the heaviest… | `FUEL_NOTHING_DISTRESS` · distress · both | Updated: 2026-08-09
- [[event-pirate-escape]] — The generic "the enemy is charging its FTL" warning. Nine different hulls hand their <escape block to this… | `PIRATE_ESCAPE` · hostile · both | Updated: 2026-08-09
- [[event-pirate-surrender]] — The most widely reused surrender offer in the game. Six different enemy hulls — including the generic PIRATE… | `PIRATE_SURRENDER` · hostile · both | Updated: 2026-08-09
- [[event-pirate-surrender-civilan]] — A complete, authored surrender-aftermath event: the pirate harassing a civilian ship breaks off and jumps… | `PIRATE_SURRENDER_CIVILAN` · both · **unreachable** · **cut-content** | Updated: 2026-08-09
- [[event-quest-crewdead]] — The quest marker placed by capture the ship. A pirate ship you must take intact: kill the crew and you get… | `QUEST_CREWDEAD` · quest · both | Updated: 2026-08-09
- [[event-quest-mantis-invasion]] — The quest marker placed by mantis war camp. Two of the three routes end in a Mantis patrol fight; the third —… | `QUEST_MANTIS_INVASION` · quest · both | Updated: 2026-08-09
- [[event-quest-store]] — A one-line store event: you arrive at a hidden space dock that was expecting you, and a store opens. It is… | `QUEST_STORE` · store · both · **unreachable** · **cut-content** | Updated: 2026-08-09
- [[event-quest-store-rescue]] — The quest marker where you save an illegal space dock from a Rebel scout. Winning the fight is a triple… | `QUEST_STORE_RESCUE` · quest · both | Updated: 2026-08-09
- [[event-rebel-auto-pds]] — A complete, fully authored event that nothing in the shipped data ever loads. It is the auto-ship version of… | `REBEL_AUTO_PDS` · ae · **unreachable** | Updated: 2026-08-09
- [[event-rebel-pds]] — A Rebel forward base opens up on you with an Anti-Ship Battery while a patrol ship closes in. Unlike the… | `REBEL_PDS` · hostile · ae | Updated: 2026-08-09
- [[event-rock-nursery]] — A fully written, fully wired away-team event that is disabled in the shipped game. Its entry in the… | `ROCK_NURSERY` · both · **cut-content** | Updated: 2026-08-09
- [[event-rock-ship-surrender]] — The surrender offer made by the standard Rock hull (ROCKSHIP). It is the stingiest offer rate in the game —… | `ROCK_SHIP_SURRENDER` · hostile · both | Updated: 2026-08-09
- [[event-rock-unlock3]] — The payoff beacon of the Rock Cruiser chain. It unlocks ship 6 — the Rock Cruiser — and then, on a follow-up… | `ROCK_UNLOCK3` · quest · both · **ship-unlock** | Updated: 2026-08-09
- [[event-rock-zoltan-help]] — A finished moral-choice event that is disabled in the shipped game: a Zoltan ship fleeing a Rock settlement… | `ROCK_ZOLTAN_HELP` · both · **cut-content** | Updated: 2026-08-09
- [[event-secret-word-abadoth]] — The quest-marker payoff of nebula wreckage. A dying survivor gives you coordinates and one word; at the… | `SECRET_WORD_ABADOTH` · quest · both | Updated: 2026-08-09
- [[event-slug-distress-piloting]] — A fully authored, fully polished Slug event — engines hacked, an ultimatum to swear allegiance to the Slug… | `SLUG_DISTRESS_PILOTING` · both · **unreachable** | Updated: 2026-08-09
- [[event-stalemate-surrender]] — The bail-out an unresolvable fight gets: the enemy silently powers down its weapons, you scoop 2 fuel out of… | `STALEMATE_SURRENDER` · both | Updated: 2026-08-09
- [[event-start-demo]] — The opening briefing for FTL's demo build, which reframes the run as a Federation training simulation. It… | `START_DEMO` · both · **unreachable** | Updated: 2026-08-09
- [[event-start-game]] — The briefing you get when a run begins: carry the data, loot every sector, stay ahead of the fleet. It is a… | `START_GAME` · both | Updated: 2026-08-09
- [[event-store-rescue]] — A fully authored quest-giver: a shuttle begs you to save its family's space dock from a Rebel attacker, and… | `STORE_RESCUE` · quest · both · **unreachable** | Updated: 2026-08-09
- [[event-tutorial-enemy]] — The tutorial's practice fight, and the game's only self-referential event: its second choice is a blue option… | `TUTORIAL_ENEMY` · hostile | Updated: 2026-08-09
- [[event-tutorial-missile]] — The tutorial's hand-out: a free Artemis Missiles launcher, given so the player can get through the practice… | `TUTORIAL_MISSILE` | Updated: 2026-08-09
- [[event-tutorial-start]] — The opening beat of FTL's scripted tutorial: three screens of "welcome, here's the war, here's your job",… | `TUTORIAL_START` | Updated: 2026-08-09
- [[event-unlock-stealth]] — A shipped, fully-written one-line event announcing that you have found a hidden Federation research lab and… | `UNLOCK_STEALTH` · both · **unreachable** · **cut-content** · **ship-unlock** | Updated: 2026-08-09
- [[event-zoltan-surrender]] — A fully written Zoltan surrender offer — six flavour strings, two choices, a payout — that no ship in the… | `ZOLTAN_SURRENDER` · hostile · both · **unreachable** | Updated: 2026-08-09

## Chains

21 pages.

- [[chain-capture-the-ship]] — The only quest in the game that is invisible without the right equipment. You overhear merchants who need an enemy ship… | autoReward HIGH weapon — but only if you kill the crew without destroying the hull · ae | Updated: 2026-08-13
- [[chain-construction-yard]] — A half-built space station has lost contact with its supply ship and asks you to find out why. Ordinary enough — but… | 1 of 3 destinations: a PDS fight for med/high scrap, an abandoned-station gamble, or a fuel-for-scrap trade · ae | Updated: 2026-08-13
- [[chain-crystal-cruiser-unlock]] — The four-step quest line that unlocks the Crystal Cruiser and the Ancestry achievement. It is the most route-dependent… | Crystal Cruiser unlock + Crystal Vengeance augment · ae | Updated: 2026-08-09
- [[chain-escort-civilians]] — Two different beacons ask you to escort a civilian ship, and both resolve to the same destination list,… | 1 of 4: high scrap · a store plus 5 hull · +1 reactor bar (AE) · or a Rebel ambush · both | Updated: 2026-08-13
- [[chain-hidden-federation-base]] — The most widely-reachable quest in the game and the shortest: four different beacons, across six sector types, all… | 1 of 5: high drone reward · free crew · 35 hull repair · a gated scrap/weapon roll · an auto-ship fight · both | Updated: 2026-08-13
- [[chain-mantis-collectors-chase]] — A running grudge. A Mantis ship escapes you once; the quest marker lets you catch up with it — and find the crew… | a high weapon for sparing them; a random weapon + med scrap for killing them; high scrap if they escape · both | Updated: 2026-08-13
- [[chain-mantis-cruiser-unlock]] — A single set-piece fight in the mantis homeworlds whose aftermath is the real chain. Beat the legendary thief… | Mantis Cruiser unlock + Mantis Pheromones + the crew member Kazaaak + a weapon cache · both | Updated: 2026-08-09
- [[chain-mantis-war-camp]] — A settlement asks you to scout a Mantis war camp, pays you before you go, and then the destination turns out to be… | med scrap up front; then nothing, a fight, or (2 Fire Bombs) high stuff + a free Engi crew member · ae | Updated: 2026-08-13
- [[chain-merchant-s-request]] — One beacon that forks into two entirely different quests and never rejoins. A merchant broadcasting for a mercenary… | scrap, a drone reward, possible crew, or a random weapon — depending which of two jobs you draw · ae | Updated: 2026-08-13
- [[chain-rebel-defector]] — A Rebel offers to defect, join your crew, and lead you to a hoard of supplies. Accepting rolls a six-entry table, and… | a human crew member, then high stuff or low scrap at the stash — if the defector was genuine · both | Updated: 2026-08-13
- [[chain-rock-bride]] — A courier job with a person as the cargo, and the only quest in the game whose final choice is purely ethical: deliver… | a random augment + low scrap, OR Ariadne (a named Rock crew member) and a fight · both | Updated: 2026-08-13
- [[chain-rock-cruiser-unlock]] — Three events, two beacons, and one inverted win condition: the Rockmen challenge you to a duel beside a star and the… | Rock Cruiser unlock + Rock Plating augment + 29 hull repairs · both | Updated: 2026-08-13
- [[chain-secret-word-abadoth]] — The only puzzle in FTL that tests the player, not the ship. A dying crewman gives you a word and some coordinates.… | autoReward MED standard — for remembering one word · both | Updated: 2026-08-13
- [[chain-settlement-mercenary-work]] — Two jobs offered by the same kind of civilian settlement, feeding one shared destination. Both are mercenary contracts,… | a store plus 5 hull and med scrap; or a med weapon for sparing the pirates · ae | Updated: 2026-08-13
- [[chain-slug-cruiser-unlock]] — The only ship-unlock chain in the game with a hidden entry point. Its first beacon is deliberately disguised as an… | Slug Cruiser unlock + Slug Repair Gel + HIGH scrap (or the Anti-Bio Beam instead) · both | Updated: 2026-08-09
- [[chain-slug-pirate-trap]] — You eavesdrop on two Slug ships planning to rob a pirate, follow them to the scene, and are invited to join a heist… | high scrap for trusting the Slugs; med/high standard for finishing the pirate; low/med for going it alone · both | Updated: 2026-08-13
- [[chain-stealth-cruiser-unlock]] — Four beacons in the engi homeworlds that end with <unlockShip id="1"/ — the Stealth Cruiser — plus the Titanium System… | Stealth Cruiser unlock + Titanium System Casing + HIGH scrap + 20 hull · both | Updated: 2026-08-09
- [[chain-the-flagship]] — The endgame sequence: you reach the Federation Base in the last stand, the Rebel Flagship arrives to destroy it, and… | Victory — the Federation Victory achievements; no in-run payout · both | Updated: 2026-08-09
- [[chain-tutorial]] — Not a quest. The three TUTORIAL events are a scripted onboarding sequence the engine runs outside the beacon system… | — · both | Updated: 2026-08-13
- [[chain-zoltan-cruiser-unlock]] — The shortest ship-unlock chain in the game: two beacons, no fight, no equipment requirement, no crew requirement. A… | Zoltan Cruiser unlock + Zoltan Shield augment or the crew member Envoy · both | Updated: 2026-08-09
- [[chain-zoltan-primitives]] — A quest you are not offered but overhear. Visiting the cantina at a Zoltan trade hub, you catch gossip about a newly… | a weapon roll — low/med for defending the planet, low/random scrap for siding against it · both | Updated: 2026-08-13

## Sectors

20 pages.

- [[sector-abandoned-sector]] — The Lanius sector, added in Advanced Edition. Display name is "Abandoned Sector" but its | LANIUS_SECTOR · hostile | Updated: 2026-08-15
- [[sector-civilian-sector]] — The generic friendly sector, and the one that most clearly shows the gap between what a | CIVILIAN_SECTOR · civilian | Updated: 2026-08-15
- [[sector-engi-controlled-sector]] — Engi-flavoured sector with its own parallel set of event lists — every generic list is | ENGI_SECTOR · civilian | Updated: 2026-08-15
- [[sector-engi-homeworlds]] — The unique Engi home sector, and the only place the Stealth Cruiser quest can begin. Its pool | ENGI_HOME · civilian | Updated: 2026-08-15
- [[sector-federation-space]] — The sector every run begins in. Its event pool is the generic, faction-neutral one — | STANDARD_SPACE · special | Updated: 2026-08-15
- [[sector-hidden-crystal-worlds]] — The hidden sector at the end of the Crystal route. Not reachable by normal map routing — | CRYSTAL_HOME · special | Updated: 2026-08-15
- [[sector-mantis-controlled-sector]] — Mantis space: seven allocation lists, 37 distinct events, and the two structural absences | MANTIS_SECTOR · hostile | Updated: 2026-08-15
- [[sector-mantis-homeworlds]] — Unique Mantis home sector. mantis controlled sector's pool plus a guaranteed | MANTIS_HOME · hostile | Updated: 2026-08-15
- [[sector-pirate-controlled-sector]] — A repeatable hostile sector available from the first sector onward (minSector="0", | PIRATE_SECTOR · hostile | Updated: 2026-08-15
- [[sector-rebel-controlled-sector]] — Rebel-held space. Repeatable, and available from the first sector onward | REBEL_SECTOR · hostile | Updated: 2026-08-15
- [[sector-rebel-stronghold]] — The unique Rebel sector that houses the Flagship construction beacon. Its allocation table is | REBEL_SECTOR_MINIBOSS · hostile | Updated: 2026-08-15
- [[sector-rock-controlled-sector]] — Rock space: a repeatable red sector with two guaranteed stores, six to eight fights that | ROCK_SECTOR · hostile | Updated: 2026-08-15
- [[sector-rock-homeworlds]] — Unique Rock home sector, and the gateway to the Crystal route: it guarantees both the | ROCK_HOME · hostile | Updated: 2026-08-15
- [[sector-slug-controlled-nebula]] — Slug space, and a nebula sector throughout. The widest event pool in the game at 11 | SLUG_SECTOR · nebula | Updated: 2026-08-15
- [[sector-slug-home-nebula]] — Unique Slug home sector — the largest event pool in the game at 12 allocation lines. | SLUG_HOME · nebula | Updated: 2026-08-15
- [[sector-the-last-stand]] — The final sector. Its pool is entirely boss-specific — no ordinary event lists appear | FINAL · special | Updated: 2026-08-16
- [[sector-uncharted-nebula]] — The unfactioned nebula sector. Its pool is built from dedicated NEBULA_ lists rather | NEBULA_SECTOR · nebula | Updated: 2026-08-15
- [[sector-vestigial-definitions]] — Two <sectorDescription> entries in sector_data.xml that appear to be dead stubs. | DEEP_SPACE_SECTOR, ABANDONED_SECTOR | Updated: 2026-08-09
- [[sector-zoltan-controlled-sector]] — Zoltan space. Guarantees a ZOLTAN_CREW_STUDY beacon even in the non-home variant — | ZOLTAN_SECTOR · civilian | Updated: 2026-08-15
- [[sector-zoltan-homeworlds]] — Unique Zoltan home sector. zoltan controlled sector's allocation table plus a | ZOLTAN_HOME | Updated: 2026-08-15
## Entities

16 pages.

- [[entity-crystal-men]] — The ancestors of the rock men, sealed away in a hidden sector that most runs never see. Crystal crew are the game's… | species · varies | Updated: 2026-08-14
- [[entity-engi]] — A machine-or-machine-adjacent species allied to the Federation, and the wiki's best-covered "friendly" faction. Engi… | species · friendly | Updated: 2026-08-09
- [[entity-federation-cruiser]] — The player ship awarded by rebel shipyard, the miniboss beacon in rebel stronghold. In-game description: | ship · friendly | Updated: 2026-08-13
- [[entity-federation]] — The side you fly for. The Federation is the losing power in the war against rebels: your ship is a Federation cruiser… | faction · friendly | Updated: 2026-08-09
- [[entity-flagship]] — The endgame boss: one ship, fought in three phases at the Federation Base in the last stand, with a separate blueprint… | ship · hostile | Updated: 2026-08-09
- [[entity-lanius]] — Advanced Edition's added species: anaerobic metal scavengers who drain the oxygen out of any room they stand in. They… | species · varies | Updated: 2026-08-14
- [[entity-mantis-cruiser]] — The player ship awarded by mantis cruiser unlock. In-game description: | ship · friendly | Updated: 2026-08-13
- [[entity-mantis]] — The game's dedicated boarding faction. Mantis crew hit 1.5× as hard as anyone else and move faster; Mantis ships carry… | species · hostile | Updated: 2026-08-09
- [[entity-pirates]] — Pirates are not a species and have no ships of their own. Mechanically they are a relabelling layer: thirteen other… | faction · hostile | Updated: 2026-08-09
- [[entity-rebels]] — The run's antagonist and the only faction you can never make peace with. The Rebels are present in three distinct… | faction · hostile | Updated: 2026-08-09
- [[entity-rock-cruiser]] — The player ship awarded by rock cruiser unlock. In-game description: | ship · friendly | Updated: 2026-08-13
- [[entity-rock-men]] — A heavy, slow, fire-proof species from Vrachos IV. Rockmen crew have the highest max health in the game (150) and move… | species · varies | Updated: 2026-08-09
- [[entity-slugs]] — Telepathic con artists who live in nebulas. Slug crew see through walls without sensors — which matters enormously… | species · varies | Updated: 2026-08-09
- [[entity-stealth-cruiser]] — The player ship awarded by stealth cruiser unlock. In-game description: | ship · friendly | Updated: 2026-08-13
- [[entity-zoltan-cruiser]] — The player ship awarded by zoltan cruiser unlock. In-game description: | ship · friendly | Updated: 2026-08-13
- [[entity-zoltan]] — An energy-bodied species allied to the engi and, through them, to the Federation. Zoltan crew are walking power… | species · neutral | Updated: 2026-08-14

## Items

65 pages.

- [[item-adv-scanners]] — Alias page. ADVSCANNERS is the blueprint id; the in-game title is Long-Ranged Scanners (text blueprints).… | augment · 1 | Updated: 2026-08-09
- [[item-anti-bio-beam]] — The BEAMBIO weapon — "This terrifying beam does no physical damage but rips through organic material, dealing… | weapon · 5 | Updated: 2026-08-09
- [[item-anti-personnel-drone]] — The BATTLE drone — "Will seek out and attempt to destroy any intruders on-board your ship." (text blueprints). | drone · 2 | Updated: 2026-08-09
- [[item-artemis-missiles]] — The MISSILES2 weapon — "Standard missile launcher on most Federation ships." Tooltip: "Fires 1 missile; does… | weapon · 0 | Updated: 2026-08-09
- [[item-artillery-beam]] — The ARTILLERYFED weapon — "Powers a slow, high-powered beam that pierces all shields and does one damage per… | weapon · 0 | Updated: 2026-08-09
- [[item-backup-dna-bank]] — The BACKUPDNA augment, added in Advanced Edition — "Your crew is safe in clone storage even if the system is… | augment · 2 | Updated: 2026-08-09
- [[item-backup-battery]] — The battery system, added in Advanced Edition — "Provides a 30 second power boost to your Reactor." | system · 1 | Updated: 2026-08-14
- [[item-beam-drone]] — Alias page. The COMBATBEAM drone's in-game title is Anti-Ship Beam Drone I (text blueprints). Full write-up… | drone · 3 | Updated: 2026-08-09
- [[item-beam-weapons]] — Not a single item: WEAPONSBEAMDAMAGE is a <blueprintList annotated "for events". The name is precise — it is… | weapon | Updated: 2026-08-09
- [[item-boarding-drone]] — The BOARDER drone — "Breaches through the enemy hull and wreaks havoc. Awesome." (text blueprints; the… | drone · 4 | Updated: 2026-08-09
- [[item-breach-missiles]] — The MISSILESBREACH weapon — "These missiles are designed to cause maximum destruction to ship hull armor."… | weapon · 3 | Updated: 2026-08-09
- [[item-cloaking]] — The cloaking system — "Cloaks the ship, adding 60 to your evasion and preventing the enemy ship from locking… | system · 1 | Updated: 2026-08-09
- [[item-clone-bay]] — The clonebay system, added in Advanced Edition. "Automatically clones dead crew with skill penalty. Taking… | system · 1 | Updated: 2026-08-09
- [[item-combat-beam-drone]] — The COMBATBEAM drone — "Combat drone that repeatedly attacks with a small beam weapon." (text blueprints).… | drone · 3 | Updated: 2026-08-09
- [[item-combat-drone-mark-i]] — The COMBAT1 drone — "Powerful drone that continually attacks the enemy ship." (text blueprints). | drone · 2 | Updated: 2026-08-09
- [[item-crystal-burst-mark-ii]] — The CRYSTALBURST2 weapon — "Modified projectile weapon that fires 3 shield piercing crystals." Tooltip:… | weapon · 0 | Updated: 2026-08-09
- [[item-crystal-lockdown-bomb]] — The BOMBLOCK weapon — "Self-teleporting explosive that does no damage but creates a dense wall preventing… | weapon · 0 | Updated: 2026-08-09
- [[item-crystal-vengeance]] — An augment awarded on completion of crystal cruiser unlock. | augment | Updated: 2026-08-09
- [[item-damaged-stasis-pod]] — The STASISPOD augment — "This bizarre alien artifact appears to be barely operational. It has no practical… | augment · 0 | Updated: 2026-08-09
- [[item-defense-drone-mark-i]] — Alias page. "Defense Drone Mark I" is the in-game title of the DEFENSE1 drone (text blueprints). Full… | drone · 1 | Updated: 2026-08-09
- [[item-defense-drone]] — The DEFENSE1 drone — "Shoots down incoming missiles, asteroids, and flak debris." (text blueprints). Event… | drone · 1 | Updated: 2026-08-09
- [[item-distraction-buoys]] — The FLEETDISTRACTION augment, added in Advanced Edition — "Leaves a false signal at sector start to delay… | augment · 3 | Updated: 2026-08-09
- [[item-door-system]] — Alias page. "Door System" is the in-game display title of the doors subsystem (text blueprints). The full… | system · 1 | Updated: 2026-08-09
- [[item-doors]] — The doors subsystem, displayed as Door System — "Allows remote opening and closing of doors. Upgrades to… | system · 1 | Updated: 2026-08-14
- [[item-drone-control]] — The drones system, displayed as Drone Control — "Powers all of the ship's drones. Drones are automated robots… | system · 1 | Updated: 2026-08-09
- [[item-drone-parts]] — The drones <itemBlueprint — "Allows you to deploy drone schematics you've found. Each deployment costs one… | 3 | Updated: 2026-08-09
- [[item-drone-reactor-booster]] — The DRONESPEED augment — "Your shipboard drones have their movement speed increased by 25 percent." (text… | augment · 0 | Updated: 2026-08-09
- [[item-drones]] — Alias page. The blueprint id drones names two different things in blueprints: a <systemBlueprint (Drone… | system · 1 | Updated: 2026-08-09
- [[item-emergency-respirators]] — The O2MASKS augment, added in Advanced Edition — "Crew take half damage from low oxygen." (text blueprints). | augment · 2 | Updated: 2026-08-14
- [[item-engi-med-bot-dispersal]] — The NANOMEDBAY augment — "Engi nano med-bots heal the crew outside of the med-bay (at a reduced speed)."… | augment · 0 | Updated: 2026-08-09
- [[item-engines]] — The engines system — "Powers the FTL drive and allows the ship to dodge. Upgrading improves dodge chance and… | system · 1 | Updated: 2026-08-09
- [[item-fire-beam]] — The BEAMFIRE weapon — "This terrifying beam does no physical damage but ignites fires." (text blueprints).… | weapon · 3 | Updated: 2026-08-09
- [[item-fire-bomb]] — The BOMBFIRE weapon — "Self-teleporting explosive designed to damage crew-members and light fires. Can target… | weapon · 2 | Updated: 2026-08-09
- [[item-flak-artillery]] — The ARTILLERYFEDC weapon, added in Advanced Edition — "Powers a slow, high-powered flak gun that fires seven… | weapon · 0 | Updated: 2026-08-09
- [[item-ftl-jumper]] — The FTLJUMPER augment, titled Adv. FTL Navigation in game — "Allows the ship to jump to any previously… | augment · 3 | Updated: 2026-08-09
- [[item-hacking]] — The hacking system, added in Advanced Edition. "Targets a single system, locking its doors and granting the… | system · 1 | Updated: 2026-08-09
- [[item-halberd-beam]] — The BEAM2 weapon — "Slow but reliably powerful standard beam weapon." Tooltip: "Beam weapon, 2 damage per… | weapon · 2 | Updated: 2026-08-09
- [[item-healing-burst]] — The BOMBHEAL weapon — "Self-teleporting healing unit that instantly heals all friendly crew in the room. Can… | weapon · 3 | Updated: 2026-08-09
- [[item-heavy-crystal-mark-ii]] — The CRYSTALHEAVY2 weapon — "Modified projectile weapon that fires a shield piercing large crystal." Tooltip:… | weapon · 0 | Updated: 2026-08-09
- [[item-hull-repair-drone]] — The SHIPREPAIR drone, titled Hull Repair in game — "Automatically repairs 3-5 damage to your hull per drone… | drone · 4 | Updated: 2026-08-09
- [[item-ion-weapons]] — Not a single item: WEAPONSION is a <blueprintList annotated "for events" that asks "do you own any ion weapon?". | weapon | Updated: 2026-08-09
- [[item-lanius-crew]] — The anaerobic crew blueprint, added in Advanced Edition — "These anaerobic beings seem friendly enough."… | crew · 0 | Updated: 2026-08-14
- [[item-lifeform-scanner]] — The LIFESCANNER augment, added in Advanced Edition — "Detects the location of any life forms, even when… | augment · 3 | Updated: 2026-08-09
- [[item-long-ranged-scanners]] — The ADVSCANNERS augment — "Adds additional info about nearby Beacons on the star map." (text blueprints). Six… | augment · 1 | Updated: 2026-08-09
- [[item-mantis-pheromones]] — The CREWSTIMS augment — "Your crew's movement speed is increased by 25 percent." (text blueprints). | augment · 0 | Updated: 2026-08-09
- [[item-medbay]] — The medbay system — "Heals all crew-members within the Medbay room. Upgrading increases healing speed." (text… | system · 1 | Updated: 2026-08-14
- [[item-mind-control]] — The mind system, added in Advanced Edition. "Temporarily turn enemies into allies." (text blueprints). | system · 1 | Updated: 2026-08-09
- [[item-missile-weapon]] — Not a single item: WEAPONSMISSILES and WEAPONSMISSILESEVENTS are <blueprintList entries that events use to… | weapon | Updated: 2026-08-09
- [[item-nano-med-bot-dispersal]] — Alias page. NANOMEDBAY is the blueprint id; the in-game title is Engi Med-bot Dispersal (text blueprints).… | augment · 0 | Updated: 2026-08-09
- [[item-oxygen-system]] — The oxygen subsystem — "Refills the oxygen in the ship. Upgrading increases the rate of refill." (text blueprints). | system · 1 | Updated: 2026-08-14
- [[item-piloting]] — The pilot subsystem — "Allows the ship to make FTL jumps and dodge when piloted. Upgrading adds auto-pilot… | system · 1 | Updated: 2026-08-09
- [[item-reactor]] — The ship's power plant. Unlike every other system on this list the reactor has no <systemBlueprint entry in… | system | Updated: 2026-08-14
- [[item-repair-drone]] — The REPAIR drone — "Will seek out damaged systems and repair them automatically." (text blueprints). A… | drone · 1 | Updated: 2026-08-09
- [[item-rock-crew]] — The rock crew blueprint — "The 'Rockmen' of Vrachos IV are rarely seen and are known for their fortitude."… | crew · 3 | Updated: 2026-08-09
- [[item-rock-plating]] — The ROCKARMOR augment — "Superior hull armor provides a 15 percent chance to negate incoming hull damage (hit… | augment · 0 | Updated: 2026-08-14
- [[item-scrap-recovery-arm]] — The SCRAPCOLLECTOR augment — "Allows the ship to collect 10 percent more scrap from any source." (text… | augment · 1 | Updated: 2026-08-09
- [[item-sensors]] — The sensors subsystem — "Reveals the interior of your ship and gives information about enemy ships." (text… | system · 1 | Updated: 2026-08-09
- [[item-shields]] — The shields system — "Powers your shields. Each additional barrier can block one shot." (text blueprints). | system · 1 | Updated: 2026-08-09
- [[item-slug-crew]] — The slug crew blueprint — "These telepathic Slugs were shunned in the Galactic Federation for their constant… | crew · 0 | Updated: 2026-08-09
- [[item-slug-repair-gel]] — The SLUGGEL augment — "Slug ships excrete a thick gel that automatically repairs any hull breaches." (text… | augment · 0 | Updated: 2026-08-09
- [[item-teleporter]] — The teleporter system — "Allows you to send your crew-members to board enemy vessels." (text blueprints).… | system · 1 | Updated: 2026-08-09
- [[item-titanium-system-casing]] — The SYSTEMCASING augment — "All ship systems have additional plating that provides a 15 percent chance to… | augment · 0 | Updated: 2026-08-09
- [[item-weapon-control]] — Alias page. "Weapon Control" is the in-game display title of the weapons system (text blueprints). The full… | system · 1 | Updated: 2026-08-09
- [[item-weapons]] — The weapons system, displayed in game as Weapon Control — "Powers all of the ship's weapons. Upgrading lets… | system · 1 | Updated: 2026-08-09
- [[item-zoltan-shield]] — The ENERGYSHIELD augment — "An unexplained technology creates this nearly impenetrable shield. Only the… | augment · 0 | Updated: 2026-08-09

## Concepts

31 pages.

- [[concept-ae-vs-vanilla]] — Advanced Edition vs vanilla | both | Updated: 2026-08-13
- [[concept-anti-ship-battery]] — The Anti-Ship Battery — the `PDS` hazard | both | Updated: 2026-08-13
- [[concept-asteroid-fields]] — Asteroid fields | both | Updated: 2026-08-13
- [[concept-augmentations]] — Augmentations | both | Updated: 2026-08-13
- [[concept-autoreward-tiers]] — `autoReward` — the reward matrix, and what it is worth: scrap by sector, flat resources, the bonus roll, precedence | both | Updated: 2026-08-16
- [[concept-blue-options]] — Blue options — how `req=` gates work | both | Updated: 2026-08-09
- [[concept-blueprint-rarity]] — `rarity` on blueprints — what the files do and don't say | both | Updated: 2026-08-09
- [[concept-crew-loss-risk]] — Crew-loss risk | both | Updated: 2026-08-13
- [[concept-cut-content]] — Cut and unreachable content | both | Updated: 2026-08-13
- [[concept-empty-beacons]] — Empty beacons — the events where nothing happens | both | Updated: 2026-08-13
- [[concept-event-cards]] — Event cards — what they are and what they promise | both | Updated: 2026-08-12
- [[concept-event-list-weighting]] — Event list weighting — how odds are derived | both | Updated: 2026-08-13
- [[concept-event-tree-grammar]] — The event tree grammar — how every FTL event is shaped | both | Updated: 2026-08-13
- [[concept-event-uniqueness]] — `unique="true"` — once per sector, or once per run? | both | Updated: 2026-08-13
- [[concept-fuel]] — Fuel | both | Updated: 2026-08-13
- [[concept-hazards]] — Beacon hazards — the `<environment>` tag | both | Updated: 2026-08-13
- [[concept-map-reveal]] — Map reveal — `<reveal_map/>` | both | Updated: 2026-08-13
- [[concept-modding-and-the-append-convention]] — Modding FTL — the `.ftl` format, the append convention, and what it would take to ingest a mod | both | Updated: 2026-08-13
- [[concept-nebula-mechanics]] — Nebulae, sensors, and storms | both | Updated: 2026-08-14
- [[concept-out-of-fuel]] — Running out of fuel | both | Updated: 2026-08-09
- [[concept-oxygen-and-suffocation]] — Oxygen and suffocation — the rates (6.4 HP/sec, drain/refill/venting) | both | Updated: 2026-08-14
- [[concept-power-and-reactor]] — Power — the reactor, and the two things that aren't it (cost curve, 25-bar cap) | ae | Updated: 2026-08-14
- [[concept-quest-beacon-placement]] — Where a quest beacon lands — and when the quest is silently thrown away | unknown | Updated: 2026-08-13
- [[concept-rebel-fleet-advance]] — The Rebel fleet advance and `modifyPursuit` | both | Updated: 2026-08-09
- [[concept-scrap-economy]] — The scrap economy — precise about costs, tiered about rewards; scrap is the only axis that scales with depth | both | Updated: 2026-08-16
- [[concept-sector-event-allocation]] — How events get allocated to beacons — and what "unreachable" can mean; `OVERRIDE_X` substitution resolved for sector allocation; the leftover-beacon `NEUTRAL` fallback and its one-event AE delta | both | Updated: 2026-08-16
- [[concept-ship-unlocks]] — Ship unlocks | both | Updated: 2026-08-13
- [[concept-solar-flares]] — Solar flares — the `sun` hazard | both | Updated: 2026-08-13
- [[concept-start-beacons]] — Start beacons — the sector-entry events | both | Updated: 2026-08-13
- [[concept-stores]] — Stores — the `<store/>` tag, store beacons, and what they stock | both | Updated: 2026-08-13
- [[concept-surrender-offers]] — Surrender offers and the `chance` attribute; what a surrender pays, and why Slug offers are blind | both | Updated: 2026-08-16

## Sources

348 source pages: 33 game-data files (`reliability: high`), 309 Fandom pages
(308 `reliability: medium`, 1 `low`), 5 research syntheses (`reliability: medium`), and
1 piece of first-party vendor documentation filed as `source_kind: wiki` at
`reliability: high`.

### Game data

- [[source-achievements]] — raw/gamedata/achievements.xml | ae | Ingested: 2026-08-09
- [[source-autoblueprints]] — raw/gamedata/autoBlueprints.xml | ae | Ingested: 2026-08-09
- [[source-blueprints]] — raw/gamedata/blueprints.xml | ae | Ingested: 2026-08-09
- [[source-bosses]] — raw/gamedata/bosses.xml | ae | Ingested: 2026-08-09
- [[source-dlcblueprints]] — raw/gamedata/dlcBlueprints.xml | ae | Ingested: 2026-08-09
- [[source-dlcblueprintsoverwrite]] — raw/gamedata/dlcBlueprintsOverwrite.xml | ae | Ingested: 2026-08-09
- [[source-dlcevents]] — raw/gamedata/dlcEvents.xml | ae | Ingested: 2026-08-09
- [[source-dlcevents-anaerobic]] — raw/gamedata/dlcEvents_anaerobic.xml | ae | Ingested: 2026-08-09
- [[source-dlceventsoverwrite]] — raw/gamedata/dlcEventsOverwrite.xml | ae | Ingested: 2026-08-09
- [[source-dlcpirateblueprints]] — raw/gamedata/dlcPirateBlueprints.xml | ae | Ingested: 2026-08-09
- [[source-events-boss]] — raw/gamedata/events_boss.xml | ae | Ingested: 2026-08-09
- [[source-events-crystal]] — raw/gamedata/events_crystal.xml | ae | Ingested: 2026-08-09
- [[source-events-engi]] — raw/gamedata/events_engi.xml | ae | Ingested: 2026-08-09
- [[source-events-fuel]] — raw/gamedata/events_fuel.xml | ae | Ingested: 2026-08-09
- [[source-events-imagelist]] — raw/gamedata/events_imageList.xml | ae | Ingested: 2026-08-09
- [[source-events-mantis]] — raw/gamedata/events_mantis.xml | ae | Ingested: 2026-08-09
- [[source-events-nebula]] — raw/gamedata/events_nebula.xml | ae | Ingested: 2026-08-09
- [[source-events-pirate]] — raw/gamedata/events_pirate.xml | ae | Ingested: 2026-08-09
- [[source-events-rebel]] — raw/gamedata/events_rebel.xml | ae | Ingested: 2026-08-09
- [[source-events-rock]] — raw/gamedata/events_rock.xml | ae | Ingested: 2026-08-09
- [[source-events-ships]] — raw/gamedata/events_ships.xml | ae | Ingested: 2026-08-09
- [[source-events-slug]] — raw/gamedata/events_slug.xml | ae | Ingested: 2026-08-09
- [[source-events-xml]] — raw/gamedata/events.xml | ae | Ingested: 2026-08-09
- [[source-events-zoltan]] — raw/gamedata/events_zoltan.xml | ae | Ingested: 2026-08-09
- [[source-nameevents]] — raw/gamedata/nameEvents.xml | ae | Ingested: 2026-08-09
- [[source-newevents]] — raw/gamedata/newEvents.xml | ae | Ingested: 2026-08-09
- [[source-sector-data-xml]] — raw/gamedata/sector_data.xml | ae | Ingested: 2026-08-09
- [[source-text-achievements]] — raw/gamedata/text_achievements.xml | ae | Ingested: 2026-08-09
- [[source-text-blueprints]] — raw/gamedata/text_blueprints.xml | ae | Ingested: 2026-08-09
- [[source-text-events-xml]] — raw/gamedata/text_events.xml | ae | Ingested: 2026-08-09
- [[source-text-misc]] — raw/gamedata/text_misc.xml | ae | Ingested: 2026-08-09
- [[source-text-sectorname-xml]] — raw/gamedata/text_sectorname.xml | ae | Ingested: 2026-08-09
- [[source-text-tooltips]] — raw/gamedata/text_tooltips.xml | ae | Ingested: 2026-08-09

### Community wiki

One page per ingested Fandom page, all `game_version: unknown`. Listed in `raw/wiki/_manifest.csv` with revision ids.

- [[source-fandom-abandoned-station]] — raw/wiki/abandoned-station.md
- [[source-fandom-ancient-device]] — raw/wiki/ancient-device.md
- [[source-fandom-asteroid-belt-distress]] — raw/wiki/asteroid-belt-distress.md
- [[source-fandom-asteroid-mining-colony]] — raw/wiki/asteroid-mining-colony.md
- [[source-fandom-augmentations]] — raw/wiki/augmentations.md | rev 74810 | both | **what Long-Ranged Scanners does and does not tell you before a jump** | Ingested: 2026-08-15
- [[source-fandom-auto-ship-attacking-civilian]] — raw/wiki/auto-ship-attacking-civilian.md
- [[source-fandom-auto-ship-attacking-outpost]] — raw/wiki/auto-ship-attacking-outpost.md
- [[source-fandom-auto-ship-carrying-shield-virus]] — raw/wiki/auto-ship-carrying-shield-virus.md
- [[source-fandom-auto-ship-fight]] — raw/wiki/auto-ship-fight.md
- [[source-fandom-auto-ship-fight-crystal]] — raw/wiki/auto-ship-fight-crystal.md
- [[source-fandom-auto-ship-fight-in-asteroid-field]] — raw/wiki/auto-ship-fight-in-asteroid-field.md
- [[source-fandom-auto-ship-fight-in-nebula]] — raw/wiki/auto-ship-fight-in-nebula.md
- [[source-fandom-auto-ship-fight-in-plasma-storm]] — raw/wiki/auto-ship-fight-in-plasma-storm.md
- [[source-fandom-auto-ship-fight-near-sun]] — raw/wiki/auto-ship-fight-near-sun.md
- [[source-fandom-auto-ship-near-radar-station]] — raw/wiki/auto-ship-near-radar-station.md
- [[source-fandom-auto-ship-near-sensor-station]] — raw/wiki/auto-ship-near-sensor-station.md
- [[source-fandom-auto-ship-near-storage-station]] — raw/wiki/auto-ship-near-storage-station.md
- [[source-fandom-auto-ship-near-storage-station-in-nebula]] — raw/wiki/auto-ship-near-storage-station-in-nebula.md
- [[source-fandom-auto-ship-warning]] — raw/wiki/auto-ship-warning.md
- [[source-fandom-auto-ship-warning-in-nebula]] — raw/wiki/auto-ship-warning-in-nebula.md
- [[source-fandom-battlefield-wreckage]] — raw/wiki/battlefield-wreckage.md
- [[source-fandom-beacons]] — raw/wiki/beacons.md | rev 71696 | **beacon types, visibility, quest-marker placement rules** | Ingested: 2026-08-15
- [[source-fandom-boarders-crystal]] — raw/wiki/boarders-crystal.md
- [[source-fandom-boarders-humans-abandoned]] — raw/wiki/boarders-humans-abandoned.md
- [[source-fandom-boarders-humans-in-nebula]] — raw/wiki/boarders-humans-in-nebula.md
- [[source-fandom-boarders-humans-in-plasma-storm]] — raw/wiki/boarders-humans-in-plasma-storm.md
- [[source-fandom-boarders-humans-jammed-sensors]] — raw/wiki/boarders-humans-jammed-sensors.md
- [[source-fandom-boarders-humans-near-sun]] — raw/wiki/boarders-humans-near-sun.md
- [[source-fandom-boarders-humans-pirate]] — raw/wiki/boarders-humans-pirate.md
- [[source-fandom-boarders-mantis]] — raw/wiki/boarders-mantis.md
- [[source-fandom-boarders-rebels-in-nebula]] — raw/wiki/boarders-rebels-in-nebula.md
- [[source-fandom-boarders-rockmen-near-sun]] — raw/wiki/boarders-rockmen-near-sun.md
- [[source-fandom-capture-the-ship]] — raw/wiki/capture-the-ship.md
- [[source-fandom-confused-mantis]] — raw/wiki/confused-mantis.md
- [[source-fandom-crew-hiring-station]] — raw/wiki/crew-hiring-station.md
- [[source-fandom-crushed-pirate]] — raw/wiki/crushed-pirate.md
- [[source-fandom-crystal-chat]] — raw/wiki/crystal-chat.md
- [[source-fandom-crystal-fight]] — raw/wiki/crystal-fight.md
- [[source-fandom-crystal-fight-choice]] — raw/wiki/crystal-fight-choice.md
- [[source-fandom-crystal-fight-with-surrender-offer-hull-repairs]] — raw/wiki/crystal-fight-with-surrender-offer-hull-repairs.md
- [[source-fandom-crystal-fight-with-surrender-offer-human-crew]] — raw/wiki/crystal-fight-with-surrender-offer-human-crew.md
- [[source-fandom-crystal-scrap-collector]] — raw/wiki/crystal-scrap-collector.md
- [[source-fandom-crystal-ship-attacking-federation-loyalists]] — raw/wiki/crystal-ship-attacking-federation-loyalists.md
- [[source-fandom-crystalline-cache]] — raw/wiki/crystalline-cache.md
- [[source-fandom-crystalline-men-buried]] — raw/wiki/crystalline-men-buried.md
- [[source-fandom-crystalline-research-facility]] — raw/wiki/crystalline-research-facility.md
- [[source-fandom-crystalline-ship-messaging-about-rebels]] — raw/wiki/crystalline-ship-messaging-about-rebels.md
- [[source-fandom-deactivated-auto-ship]] — raw/wiki/deactivated-auto-ship.md
- [[source-fandom-dense-asteroid-field-distress]] — raw/wiki/dense-asteroid-field-distress.md
- [[source-fandom-destroyed-cargo-ship]] — raw/wiki/destroyed-cargo-ship.md
- [[source-fandom-disabled-rock-ship]] — raw/wiki/disabled-rock-ship.md
- [[source-fandom-empty-beacon-civilian]] — raw/wiki/empty-beacon-civilian.md
- [[source-fandom-empty-beacon-crystal]] — raw/wiki/empty-beacon-crystal.md
- [[source-fandom-empty-beacon-engi]] — raw/wiki/empty-beacon-engi.md
- [[source-fandom-empty-beacon-lanius]] — raw/wiki/empty-beacon-lanius.md
- [[source-fandom-empty-beacon-last-stand]] — raw/wiki/empty-beacon-last-stand.md
- [[source-fandom-empty-beacon-mantis]] — raw/wiki/empty-beacon-mantis.md
- [[source-fandom-empty-beacon-pirate]] — raw/wiki/empty-beacon-pirate.md
- [[source-fandom-empty-beacon-rebel]] — raw/wiki/empty-beacon-rebel.md
- [[source-fandom-empty-beacon-rock]] — raw/wiki/empty-beacon-rock.md
- [[source-fandom-empty-beacon-slug]] — raw/wiki/empty-beacon-slug.md
- [[source-fandom-empty-beacon-zoltan]] — raw/wiki/empty-beacon-zoltan.md
- [[source-fandom-empty-nebula-beacon]] — raw/wiki/empty-nebula-beacon.md
- [[source-fandom-empty-nebula-beacon-slug]] — raw/wiki/empty-nebula-beacon-slug.md
- [[source-fandom-encrypted-federation-signal]] — raw/wiki/encrypted-federation-signal.md
- [[source-fandom-engi-cache]] — raw/wiki/engi-cache.md
- [[source-fandom-engi-distress-rebel-fight]] — raw/wiki/engi-distress-rebel-fight.md
- [[source-fandom-engi-fight]] — raw/wiki/engi-fight.md
- [[source-fandom-engi-fleet-discussion]] — raw/wiki/engi-fleet-discussion.md
- [[source-fandom-engi-research-station]] — raw/wiki/engi-research-station.md
- [[source-fandom-engi-ship-attacked-by-mantis-ship]] — raw/wiki/engi-ship-attacked-by-mantis-ship.md
- [[source-fandom-engi-smashed-ships]] — raw/wiki/engi-smashed-ships.md
- [[source-fandom-engi-surrender]] — raw/wiki/engi-surrender.md
- [[source-fandom-environmental-hazards]] — raw/wiki/environmental-hazards.md | rev 74893 | **nebula/pulsar/ASB/asteroid/flare mechanics with timings** | Ingested: 2026-08-15
- [[source-fandom-escape-pod]] — raw/wiki/escape-pod.md
- [[source-fandom-escort-civilians]] — raw/wiki/escort-civilians.md
- [[source-fandom-escort-civilians-ftl-haywire]] — raw/wiki/escort-civilians-ftl-haywire.md
- [[source-fandom-federation-deserters]] — raw/wiki/federation-deserters.md
- [[source-fandom-fight-in-last-stand]] — raw/wiki/fight-in-last-stand.md
- [[source-fandom-fire-on-research-station]] — raw/wiki/fire-on-research-station.md
- [[source-fandom-free-drone-schematic]] — raw/wiki/free-drone-schematic.md
- [[source-fandom-free-scrap-with-resources]] — raw/wiki/free-scrap-with-resources.md
- [[source-fandom-free-scrap-with-resources-engi]] — raw/wiki/free-scrap-with-resources-engi.md
- [[source-fandom-free-scrap-with-resources-lanius]] — raw/wiki/free-scrap-with-resources-lanius.md
- [[source-fandom-free-scrap-with-resources-zoltan]] — raw/wiki/free-scrap-with-resources-zoltan.md
- [[source-fandom-free-weapon]] — raw/wiki/free-weapon.md
- [[source-fandom-friendly-ship-out-of-fuel]] — raw/wiki/friendly-ship-out-of-fuel.md
- [[source-fandom-ftl-advanced-edition]] — raw/wiki/ftl-advanced-edition.md | rev 74567 | ae | the version anchor: what AE changed, and what applies with AE content off | Ingested: 2026-08-15
- [[source-fandom-game-bugs]] — raw/wiki/game-bugs.md | rev 74618 | both | save-reload bugs; fixed vs event stores are different objects on the map | Ingested: 2026-08-15
- [[source-fandom-giant-alien-spiders]] — raw/wiki/giant-alien-spiders.md
- [[source-fandom-guides-and-tips]] — raw/wiki/guides-and-tips.md | rev 74605 | link directory; the wiki's only sector-routing guidance is 3 outbound links | Ingested: 2026-08-15
- [[source-fandom-improve-reactor-for-supplies]] — raw/wiki/improve-reactor-for-supplies.md
- [[source-fandom-intelligent-ponies]] — raw/wiki/intelligent-ponies.md
- [[source-fandom-lanius-craftsmen]] — raw/wiki/lanius-craftsmen.md
- [[source-fandom-lanius-empty-distress-beacon-1]] — raw/wiki/lanius-empty-distress-beacon-1.md
- [[source-fandom-lanius-empty-distress-beacon-2]] — raw/wiki/lanius-empty-distress-beacon-2.md
- [[source-fandom-lanius-fight]] — raw/wiki/lanius-fight.md
- [[source-fandom-lanius-fight-distress]] — raw/wiki/lanius-fight-distress.md
- [[source-fandom-lanius-fight-in-asteroid-field]] — raw/wiki/lanius-fight-in-asteroid-field.md
- [[source-fandom-lanius-fight-near-pulsar]] — raw/wiki/lanius-fight-near-pulsar.md
- [[source-fandom-lanius-fight-with-friendly-asb-support]] — raw/wiki/lanius-fight-with-friendly-asb-support.md
- [[source-fandom-lanius-lone-ship]] — raw/wiki/lanius-lone-ship.md
- [[source-fandom-lanius-powered-down-ship]] — raw/wiki/lanius-powered-down-ship.md
- [[source-fandom-lanius-ship-absorbing-automated-scout]] — raw/wiki/lanius-ship-absorbing-automated-scout.md
- [[source-fandom-lanius-ship-absorbing-jump-beacon]] — raw/wiki/lanius-ship-absorbing-jump-beacon.md
- [[source-fandom-lanius-ship-absorbing-rebel-base]] — raw/wiki/lanius-ship-absorbing-rebel-base.md
- [[source-fandom-lanius-ship-attacking-civilian]] — raw/wiki/lanius-ship-attacking-civilian.md
- [[source-fandom-lanius-ship-attacking-civilian-distress]] — raw/wiki/lanius-ship-attacking-civilian-distress.md
- [[source-fandom-lanius-ship-attacking-mantis]] — raw/wiki/lanius-ship-attacking-mantis.md
- [[source-fandom-lanius-ship-attacking-rock]] — raw/wiki/lanius-ship-attacking-rock.md
- [[source-fandom-lanius-ship-attacking-slug]] — raw/wiki/lanius-ship-attacking-slug.md
- [[source-fandom-lanius-ship-in-rich-debris-field]] — raw/wiki/lanius-ship-in-rich-debris-field.md
- [[source-fandom-lanius-ship-salvager]] — raw/wiki/lanius-ship-salvager.md
- [[source-fandom-lanius-trader]] — raw/wiki/lanius-trader.md
- [[source-fandom-lanius-trader-with-translator]] — raw/wiki/lanius-trader-with-translator.md
- [[source-fandom-lanius-with-federation-science-craft]] — raw/wiki/lanius-with-federation-science-craft.md
- [[source-fandom-large-asteroid-field]] — raw/wiki/large-asteroid-field.md
- [[source-fandom-large-trade-station]] — raw/wiki/large-trade-station.md
- [[source-fandom-legendary-thief-kazaaakplethkilik]] — raw/wiki/legendary-thief-kazaaakplethkilik.md
- [[source-fandom-malfunctioning-defense-system]] — raw/wiki/malfunctioning-defense-system.md
- [[source-fandom-mantis-fight]] — raw/wiki/mantis-fight.md
- [[source-fandom-mantis-fight-choice]] — raw/wiki/mantis-fight-choice.md
- [[source-fandom-mantis-fight-choice-in-nebula]] — raw/wiki/mantis-fight-choice-in-nebula.md
- [[source-fandom-mantis-fight-engi]] — raw/wiki/mantis-fight-engi.md
- [[source-fandom-mantis-fight-in-nebula]] — raw/wiki/mantis-fight-in-nebula.md
- [[source-fandom-mantis-fight-in-nebula-slug]] — raw/wiki/mantis-fight-in-nebula-slug.md
- [[source-fandom-mantis-fight-near-sun]] — raw/wiki/mantis-fight-near-sun.md
- [[source-fandom-mantis-fight-slug]] — raw/wiki/mantis-fight-slug.md
- [[source-fandom-mantis-fight-zoltan]] — raw/wiki/mantis-fight-zoltan.md
- [[source-fandom-mantis-fugitive]] — raw/wiki/mantis-fugitive.md
- [[source-fandom-mantis-outcasts]] — raw/wiki/mantis-outcasts.md
- [[source-fandom-mantis-ship-attacking-civilian]] — raw/wiki/mantis-ship-attacking-civilian.md
- [[source-fandom-mantis-ship-attacking-crystal]] — raw/wiki/mantis-ship-attacking-crystal.md
- [[source-fandom-mantis-ship-attacking-slug-ship]] — raw/wiki/mantis-ship-attacking-slug-ship.md
- [[source-fandom-mantis-ship-collectors]] — raw/wiki/mantis-ship-collectors.md
- [[source-fandom-mantis-ship-with-rock-body-parts]] — raw/wiki/mantis-ship-with-rock-body-parts.md
- [[source-fandom-mantis-ships-battle-for-rock-freighter]] — raw/wiki/mantis-ships-battle-for-rock-freighter.md
- [[source-fandom-mantis-war-camp]] — raw/wiki/mantis-war-camp.md
- [[source-fandom-merchant-s-request]] — raw/wiki/merchant-s-request.md
- [[source-fandom-nebula-lost-ship]] — raw/wiki/nebula-lost-ship.md
- [[source-fandom-nebula-wreckage]] — raw/wiki/nebula-wreckage.md
- [[source-fandom-no-fuel-auto-ship-warning]] — raw/wiki/no-fuel-auto-ship-warning.md
- [[source-fandom-no-fuel-automated-refueling-ship]] — raw/wiki/no-fuel-automated-refueling-ship.md
- [[source-fandom-no-fuel-drifting-debris]] — raw/wiki/no-fuel-drifting-debris.md
- [[source-fandom-no-fuel-engi-ship-repair]] — raw/wiki/no-fuel-engi-ship-repair.md
- [[source-fandom-no-fuel-explore-the-system]] — raw/wiki/no-fuel-explore-the-system.md
- [[source-fandom-no-fuel-friendly-refugee]] — raw/wiki/no-fuel-friendly-refugee.md
- [[source-fandom-no-fuel-fuel-trader-distress-off]] — raw/wiki/no-fuel-fuel-trader-distress-off.md
- [[source-fandom-no-fuel-fuel-trader-distress-on]] — raw/wiki/no-fuel-fuel-trader-distress-on.md
- [[source-fandom-no-fuel-mantis-fight]] — raw/wiki/no-fuel-mantis-fight.md
- [[source-fandom-no-fuel-prepare-to-dock]] — raw/wiki/no-fuel-prepare-to-dock.md
- [[source-fandom-no-fuel-rebel-fight]] — raw/wiki/no-fuel-rebel-fight.md
- [[source-fandom-no-fuel-rebel-fleet-delay]] — raw/wiki/no-fuel-rebel-fleet-delay.md
- [[source-fandom-no-fuel-refugee-trading]] — raw/wiki/no-fuel-refugee-trading.md
- [[source-fandom-no-fuel-slug-fuel-depot]] — raw/wiki/no-fuel-slug-fuel-depot.md
- [[source-fandom-no-fuel-slug-fuel-trader]] — raw/wiki/no-fuel-slug-fuel-trader.md
- [[source-fandom-no-fuel-wait-fail-distress-off]] — raw/wiki/no-fuel-wait-fail-distress-off.md
- [[source-fandom-no-fuel-wait-fail-distress-on]] — raw/wiki/no-fuel-wait-fail-distress-on.md
- [[source-fandom-oxygen]] — raw/wiki/oxygen.md | rev 74853 | **the only source with oxygen/suffocation rates** | Ingested: 2026-08-14
- [[source-fandom-pirate-briber]] — raw/wiki/pirate-briber.md
- [[source-fandom-pirate-engine-hacker]] — raw/wiki/pirate-engine-hacker.md
- [[source-fandom-pirate-fight]] — raw/wiki/pirate-fight.md
- [[source-fandom-pirate-fight-choice-in-nebula]] — raw/wiki/pirate-fight-choice-in-nebula.md
- [[source-fandom-pirate-fight-engi]] — raw/wiki/pirate-fight-engi.md
- [[source-fandom-pirate-fight-in-asteroid-field]] — raw/wiki/pirate-fight-in-asteroid-field.md
- [[source-fandom-pirate-fight-in-nebula]] — raw/wiki/pirate-fight-in-nebula.md
- [[source-fandom-pirate-fight-lanius]] — raw/wiki/pirate-fight-lanius.md
- [[source-fandom-pirate-fight-near-pulsar]] — raw/wiki/pirate-fight-near-pulsar.md
- [[source-fandom-pirate-fight-near-sun]] — raw/wiki/pirate-fight-near-sun.md
- [[source-fandom-pirate-fight-slug]] — raw/wiki/pirate-fight-slug.md
- [[source-fandom-pirate-fight-zoltan]] — raw/wiki/pirate-fight-zoltan.md
- [[source-fandom-pirate-ship-attacking-civilian]] — raw/wiki/pirate-ship-attacking-civilian.md
- [[source-fandom-pirate-ship-attacking-civilian-distress]] — raw/wiki/pirate-ship-attacking-civilian-distress.md
- [[source-fandom-pirate-ship-attacking-civilian-lanius]] — raw/wiki/pirate-ship-attacking-civilian-lanius.md
- [[source-fandom-pirate-ship-attacking-crystal]] — raw/wiki/pirate-ship-attacking-crystal.md
- [[source-fandom-pirate-ship-distress-trap]] — raw/wiki/pirate-ship-distress-trap.md
- [[source-fandom-pirate-ship-selling-drones]] — raw/wiki/pirate-ship-selling-drones.md
- [[source-fandom-pirate-ship-selling-weapon]] — raw/wiki/pirate-ship-selling-weapon.md
- [[source-fandom-pirate-ships-in-plasma-storm]] — raw/wiki/pirate-ships-in-plasma-storm.md
- [[source-fandom-pirate-smuggler]] — raw/wiki/pirate-smuggler.md
- [[source-fandom-pirate-toll]] — raw/wiki/pirate-toll.md
- [[source-fandom-plagued-station]] — raw/wiki/plagued-station.md
- [[source-fandom-plasma-storm-incapacitated-ships]] — raw/wiki/plasma-storm-incapacitated-ships.md
- [[source-fandom-random-events]] — raw/wiki/random-events.md — **the hub page**, not an event page: quest placement, `unique` scope, what LRS reports
- [[source-fandom-rarity]] — raw/wiki/rarity.md | a one-line redirect to Stores and resources#Items and crew rarity; there is no separate Fandom page on rarity | both | Ingested: 2026-08-16
- [[source-fandom-rebel-checkpoint]] — raw/wiki/rebel-checkpoint.md
- [[source-fandom-rebel-defector]] — raw/wiki/rebel-defector.md
- [[source-fandom-rebel-fight]] — raw/wiki/rebel-fight.md
- [[source-fandom-rebel-fight-among-federation-and-rebel-fleets]] — raw/wiki/rebel-fight-among-federation-and-rebel-fleets.md
- [[source-fandom-rebel-fight-among-rebel-fleet]] — raw/wiki/rebel-fight-among-rebel-fleet.md
- [[source-fandom-rebel-fight-chance]] — raw/wiki/rebel-fight-chance.md
- [[source-fandom-rebel-fight-chance-in-nebula]] — raw/wiki/rebel-fight-chance-in-nebula.md
- [[source-fandom-rebel-fight-choice-in-nebula]] — raw/wiki/rebel-fight-choice-in-nebula.md
- [[source-fandom-rebel-fight-crystal]] — raw/wiki/rebel-fight-crystal.md
- [[source-fandom-rebel-fleet]] — raw/wiki/rebel-fleet.md | rev 73264 | both | **every modifier to the fleet advance rate; what an overtaken beacon becomes** | Ingested: 2026-08-15
- [[source-fandom-rebel-fight-engi]] — raw/wiki/rebel-fight-engi.md
- [[source-fandom-rebel-fight-in-nebula]] — raw/wiki/rebel-fight-in-nebula.md
- [[source-fandom-rebel-fight-in-plasma-storm]] — raw/wiki/rebel-fight-in-plasma-storm.md
- [[source-fandom-rebel-fight-lanius]] — raw/wiki/rebel-fight-lanius.md
- [[source-fandom-rebel-fight-near-pulsar]] — raw/wiki/rebel-fight-near-pulsar.md
- [[source-fandom-rebel-fight-slug]] — raw/wiki/rebel-fight-slug.md
- [[source-fandom-rebel-fight-with-boarders]] — raw/wiki/rebel-fight-with-boarders.md
- [[source-fandom-rebel-ship-attacking-civilians-in-last-stand]] — raw/wiki/rebel-ship-attacking-civilians-in-last-stand.md
- [[source-fandom-rebel-ship-attacking-crystal-ship]] — raw/wiki/rebel-ship-attacking-crystal-ship.md
- [[source-fandom-rebel-ship-attacking-federation-loyalists]] — raw/wiki/rebel-ship-attacking-federation-loyalists.md
- [[source-fandom-rebel-ship-attacking-refueling-outpost]] — raw/wiki/rebel-ship-attacking-refueling-outpost.md
- [[source-fandom-rebel-ship-supplying-civilians]] — raw/wiki/rebel-ship-supplying-civilians.md
- [[source-fandom-rebel-ship-warning]] — raw/wiki/rebel-ship-warning.md
- [[source-fandom-rebel-shipyard]] — raw/wiki/rebel-shipyard.md
- [[source-fandom-rebel-transport-ship]] — raw/wiki/rebel-transport-ship.md
- [[source-fandom-refueling-platform]] — raw/wiki/refueling-platform.md
- [[source-fandom-refueling-platform-garbled-broadcast]] — raw/wiki/refueling-platform-garbled-broadcast.md
- [[source-fandom-refueling-station]] — raw/wiki/refueling-station.md
- [[source-fandom-refugee]] — raw/wiki/refugee.md
- [[source-fandom-refugee-comms-down]] — raw/wiki/refugee-comms-down.md
- [[source-fandom-refugee-distress]] — raw/wiki/refugee-distress.md
- [[source-fandom-refugee-distress-pirate]] — raw/wiki/refugee-distress-pirate.md
- [[source-fandom-refugee-distress-slug]] — raw/wiki/refugee-distress-slug.md
- [[source-fandom-refugee-distress-zoltan]] — raw/wiki/refugee-distress-zoltan.md
- [[source-fandom-refugee-pirate]] — raw/wiki/refugee-pirate.md
- [[source-fandom-refugee-slug]] — raw/wiki/refugee-slug.md
- [[source-fandom-refugee-zoltan]] — raw/wiki/refugee-zoltan.md
- [[source-fandom-remote-settlement]] — raw/wiki/remote-settlement.md
- [[source-fandom-repair-station]] — raw/wiki/repair-station.md
- [[source-fandom-repair-station-in-last-stand]] — raw/wiki/repair-station-in-last-stand.md
- [[source-fandom-research-station-with-no-response]] — raw/wiki/research-station-with-no-response.md
- [[source-fandom-rewards]] — raw/wiki/rewards.md | rev 74729 | both | **the numbers behind `autoReward`: scrap by sector, flat resources, the 3%/6% bonus-item roll, reward precedence, Lanius default rewards** | Ingested: 2026-08-16
- [[source-fandom-rock-and-slug-standoff]] — raw/wiki/rock-and-slug-standoff.md
- [[source-fandom-rock-atheists]] — raw/wiki/rock-atheists.md
- [[source-fandom-rock-bride]] — raw/wiki/rock-bride.md
- [[source-fandom-rock-fight]] — raw/wiki/rock-fight.md
- [[source-fandom-rock-fight-in-asteroid-field]] — raw/wiki/rock-fight-in-asteroid-field.md
- [[source-fandom-rock-fight-in-nebula]] — raw/wiki/rock-fight-in-nebula.md
- [[source-fandom-rock-fight-with-boarders]] — raw/wiki/rock-fight-with-boarders.md
- [[source-fandom-rock-fight-with-boarders-in-asteroid-field]] — raw/wiki/rock-fight-with-boarders-in-asteroid-field.md
- [[source-fandom-rock-live-mine]] — raw/wiki/rock-live-mine.md
- [[source-fandom-rock-pirates-fight]] — raw/wiki/rock-pirates-fight.md
- [[source-fandom-rock-pirates-fight-in-asteroid-field]] — raw/wiki/rock-pirates-fight-in-asteroid-field.md
- [[source-fandom-rock-pirates-fight-near-sun]] — raw/wiki/rock-pirates-fight-near-sun.md
- [[source-fandom-rock-ship-in-plasma-storm]] — raw/wiki/rock-ship-in-plasma-storm.md
- [[source-fandom-rock-war-vessel-encounter]] — raw/wiki/rock-war-vessel-encounter.md
- [[source-fandom-scrap]] — raw/wiki/scrap.md | rev 73343 | scrap scales with sector *number* × difficulty; sector *type* shifts profit via its event pool | Ingested: 2026-08-15
- [[source-fandom-sectors]] — raw/wiki/sectors.md | rev 74796 | both | **the sector hub — every per-sector Fandom title redirects here; carries the map-generation algorithm** | Ingested: 2026-08-15
- [[source-fandom-sell-drone-parts-for-scrap]] — raw/wiki/sell-drone-parts-for-scrap.md
- [[source-fandom-sell-missiles-for-scrap]] — raw/wiki/sell-missiles-for-scrap.md
- [[source-fandom-sensors]] — raw/wiki/sensors.md | rev 73457 | what a nebula costs you: Sensors are disabled inside one | Ingested: 2026-08-15
- [[source-fandom-settlement-mercenary-work]] — raw/wiki/settlement-mercenary-work.md
- [[source-fandom-single-life-form-on-moon]] — raw/wiki/single-life-form-on-moon.md
- [[source-fandom-slaver-friendly]] — raw/wiki/slaver-friendly.md
- [[source-fandom-slaver-hostile]] — raw/wiki/slaver-hostile.md
- [[source-fandom-slocknog]] — raw/wiki/slocknog.md
- [[source-fandom-slug-and-rock-standoff-in-nebula]] — raw/wiki/slug-and-rock-standoff-in-nebula.md
- [[source-fandom-slug-comm-tapping]] — raw/wiki/slug-comm-tapping.md
- [[source-fandom-slug-drink]] — raw/wiki/slug-drink.md
- [[source-fandom-slug-fight]] — raw/wiki/slug-fight.md
- [[source-fandom-slug-fight-in-nebula]] — raw/wiki/slug-fight-in-nebula.md
- [[source-fandom-ship]] — raw/wiki/ship.md | rev 74911 | **the only source with the reactor cost curve** | Ingested: 2026-08-14
- [[source-fandom-slug-fight-in-plasma-storm]] — raw/wiki/slug-fight-in-plasma-storm.md
- [[source-fandom-slug-hacker-choice]] — raw/wiki/slug-hacker-choice.md
- [[source-fandom-slug-hacker-doors]] — raw/wiki/slug-hacker-doors.md
- [[source-fandom-slug-hacker-medical]] — raw/wiki/slug-hacker-medical.md
- [[source-fandom-slug-hacker-oxygen]] — raw/wiki/slug-hacker-oxygen.md
- [[source-fandom-slug-home-nebula-surrender]] — raw/wiki/slug-home-nebula-surrender.md
- [[source-fandom-slug-moons-question]] — raw/wiki/slug-moons-question.md
- [[source-fandom-slug-oxygen-malfunction]] — raw/wiki/slug-oxygen-malfunction.md
- [[source-fandom-slug-repair-station]] — raw/wiki/slug-repair-station.md
- [[source-fandom-slug-ship-boarding-rock-ship]] — raw/wiki/slug-ship-boarding-rock-ship.md
- [[source-fandom-slug-store-ship]] — raw/wiki/slug-store-ship.md
- [[source-fandom-space-station-under-construction]] — raw/wiki/space-station-under-construction.md
- [[source-fandom-store]] — raw/wiki/store.md
- [[source-fandom-store-crystal]] — raw/wiki/store-crystal.md
- [[source-fandom-store-engi]] — raw/wiki/store-engi.md
- [[source-fandom-store-in-nebula-slug]] — raw/wiki/store-in-nebula-slug.md
- [[source-fandom-store-in-nebula-uncharted]] — raw/wiki/store-in-nebula-uncharted.md
- [[source-fandom-store-lanius]] — raw/wiki/store-lanius.md
- [[source-fandom-store-mantis]] — raw/wiki/store-mantis.md
- [[source-fandom-store-pirate]] — raw/wiki/store-pirate.md
- [[source-fandom-store-rebel]] — raw/wiki/store-rebel.md
- [[source-fandom-store-rock]] — raw/wiki/store-rock.md
- [[source-fandom-store-zoltan]] — raw/wiki/store-zoltan.md
- [[source-fandom-stores-and-resources]] — raw/wiki/stores-and-resources.md | rev 74856 | both | **store stocking rules, per-sector store economy, out-of-fuel / waiting mechanics** | Ingested: 2026-08-15
- [[source-fandom-terraforming-scan]] — raw/wiki/terraforming-scan.md
- [[source-fandom-template-reactor-power-cost]] — raw/wiki/template-reactor-power-cost.md | rev 68667 | a transcluded template, not an article | Ingested: 2026-08-14
- [[source-fandom-template-stores-number-of-stores-by-sectors]] — raw/wiki/template-stores-number-of-stores-by-sectors.md | rev 73433 | **guaranteed stores per sector, all 13 types; matches sector_data.xml exactly** | Ingested: 2026-08-15
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]] — raw/wiki/template-stores-additional-stores-from-events-by-sectors.md | rev 73435 | which store-spawning events reach which sector | Ingested: 2026-08-15
- [[source-fandom-template-distress-events-by-sectors]] — raw/wiki/template-distress-events-by-sectors.md | rev 74574 | **the 30 distress-marked events + what LRS shows at each; matches the 30 `<distressBeacon/>` tags exactly** | Ingested: 2026-08-15
- [[source-fandom-template-scrap-rewards-normal]] — raw/wiki/template-scrap-rewards-normal.md | rev 72605 | **`LOW`/`MED`/`HIGH` scrap by sector, Normal difficulty — the table that closes the wiki's largest open question** | both | Ingested: 2026-08-16
- [[source-fandom-template-resources-rewards]] — raw/wiki/template-resources-rewards.md | rev 72607 | **fuel / missiles / drone parts per level; flat across sector and difficulty** | both | Ingested: 2026-08-16
- [[source-fandom-the-black-raven]] — raw/wiki/the-black-raven.md
- [[source-fandom-the-engi-virus]] — raw/wiki/the-engi-virus.md
- [[source-fandom-the-mercenary]] — raw/wiki/the-mercenary.md
- [[source-fandom-the-rebellion]] — raw/wiki/the-rebellion.md | rev 68216 | lore only; factual content is the Rebel ship-type list | Ingested: 2026-08-15
- [[source-fandom-trade-fuel-for-drone-parts]] — raw/wiki/trade-fuel-for-drone-parts.md
- [[source-fandom-trade-resources]] — raw/wiki/trade-resources.md
- [[source-fandom-trade-resources-in-nebula]] — raw/wiki/trade-resources-in-nebula.md
- [[source-fandom-trade-scrap-for-upgrades]] — raw/wiki/trade-scrap-for-upgrades.md
- [[source-fandom-unarmed-zoltan-transport]] — raw/wiki/unarmed-zoltan-transport.md
- [[source-fandom-unknown-disease-on-mining-colony]] — raw/wiki/unknown-disease-on-mining-colony.md
- [[source-fandom-zoltan-border-police]] — raw/wiki/zoltan-border-police.md
- [[source-fandom-zoltan-fight]] — raw/wiki/zoltan-fight.md
- [[source-fandom-zoltan-fight-in-asteroid-field]] — raw/wiki/zoltan-fight-in-asteroid-field.md
- [[source-fandom-zoltan-free-augment]] — raw/wiki/zoltan-free-augment.md
- [[source-fandom-zoltan-free-map]] — raw/wiki/zoltan-free-map.md
- [[source-fandom-zoltan-great-eye]] — raw/wiki/zoltan-great-eye.md
- [[source-fandom-zoltan-odd-moon]] — raw/wiki/zoltan-odd-moon.md
- [[source-fandom-zoltan-quest-primitives]] — raw/wiki/zoltan-quest-primitives.md
- [[source-fandom-zoltan-research-facility]] — raw/wiki/zoltan-research-facility.md
- [[source-fandom-zoltan-retake-the-ship]] — raw/wiki/zoltan-retake-the-ship.md
- [[source-fandom-zoltan-security-checkpoint]] — raw/wiki/zoltan-security-checkpoint.md
- [[source-fandom-zoltan-ship-asks-to-dock]] — raw/wiki/zoltan-ship-asks-to-dock.md
- [[source-fandom-zoltan-ship-follows-mantis-ship]] — raw/wiki/zoltan-ship-follows-mantis-ship.md
- [[source-fandom-zoltan-trade-hub]] — raw/wiki/zoltan-trade-hub.md
- [[source-fandom-zoltan-wise-man]] — raw/wiki/zoltan-wise-man.md

### Research

Synthesised external research, written into `raw/` by instruction rather than captured from a
page. `source_kind: research` and the `raw/modding/` directory are extensions beyond
`CLAUDE.md` §1 / §2.7 — see the log entry for 2026-08-13.

- [[source-beacon-name-labels-mod-research]] — raw/modding/2026-08-15-beacon-name-labels-mod.md | **can a mod name every beacon on the map before it is revealed — yes, via Hyperspace Lua only** | both | Ingested: 2026-08-15
- [[source-modding-research]] — raw/modding/2026-08-12-ftl-modding-research.md | both | Ingested: 2026-08-13
- [[source-xftl-oxygen-mechanics]] — raw/modding/2026-08-14-xftl-oxygen-mechanics.txt | reverse-engineered engine constants for oxygen | unknown | Ingested: 2026-08-14
- [[source-xftl-sector-map]] — raw/modding/2026-08-15-xftl-sector-map.txt | **the sector graph, the 6×4 beacon grid, exit placement, `AddQuest`, and the fleet advance in px/jump** | unknown | Ingested: 2026-08-15
- [[source-xftl-stores]] — raw/modding/2026-08-15-xftl-stores.txt | store section generation, system selection, resource stock ranges | both | Ingested: 2026-08-15
- [[source-store-crew-selection-disassembly]] — raw/modding/2026-08-16-store-crew-selection-disassembly.md | the store crew-draw algorithm read out of FTLGame_orig.exe: weight = 6 − rarity, 0 excluded, 3 independent slots, rarityList overlays base | both | Ingested: 2026-08-16
- [[source-sector-column-linking-disassembly]] — raw/modding/2026-08-17-sector-column-linking-disassembly.md | StarMap::AddSectorColumn read out of FTLGame.exe: the exact link map for all six column transitions, and the proof that every unequal 2–4 pair occurs | both | Ingested: 2026-08-17
- [[source-ftl-dat-rarity-corpus-search]] — raw/modding/2026-08-16-ftl-dat-rarity-corpus-search.md | recorded negative: rarity is in only 3 data files in all of ftl.dat, all already held; the 164-entry uncopied diff; raw/gamedata verified not stale against a Hyperspace-modded install | both | Ingested: 2026-08-16

### Vendor documentation

Captured first-party documentation for the modding toolchain. Filed `source_kind: wiki` for
lack of a better value, but at `reliability: high` — see the page's own schema note.

- [[source-slipstream-readme-modders]] — raw/modding/slipstream-1.9.1-readme_modders.txt | both | Ingested: 2026-08-13
