<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-15. Source layer: do not edit. -->
Title: Stores and resources
URL: https://ftl.fandom.com/wiki/Stores_and_resources
Categories: Mechanics
Revision: 74856
Retrieved: 2026-08-15

---
Stores can be found at designated beacons or in [[Random Events|events]]. They offer goods and services in exchange for [[scrap]].
__TOC__
==<span style="font-size:larger;">'''Stores availability'''</span>==
===<h2>Guaranteed stores</h2>===
The number of guaranteed stores is determined by the sector type.
{{Stores: number of stores, by sectors}}

===<h2>Additional stores</h2>===
{{Stores: additional stores from events, by sectors}}

===<h2>Store bugs</h2>===
Reloading at an "event generated" store will make it vanish. If you have enemy boarders on your ship, leaving the store interface will also make the store disappear.

Reloading at any store will re-roll crew skills, and will force drone control to come with a Defence Drone Mark 1.

With [[FTL: Advanced Edition|Advanced Edition Content]] Off, there is a bug that very often causes item slots to be empty. It affects crew, augmentations, drones, systems, and weapons (e.g. a store might sell only two weapons or even one crew  - instead of a regular three).

Also note that a store with [[FTL: Advanced Edition|Advanced Edition Content]] On can have some empty systems slots when most or all of the systems are purchased/installed (i.e. with all 8 main systems installed it is possible to not be able to find Sensors or Backup Battery or a different medical unit in a store that sells systems - some sub-slots will be plainly empty). <!-- @to-do: specify the requirements or triggers for this bug -->

See [[game bugs]] for more information, including advice for avoiding these types of issue.


==<span style="font-size:larger;">'''Stores assortment'''</span>==
{| class="table" align="right" style="margin-left:3px;"
|{{Stores: hull repairs in stores}}
|-
| align="center" |{{Stores: resources in stores}}
|}

Stores sell:
* Unlimited hull repairs
* Limited quantities of all resources ([[Fuel|fuel]], [[Missiles|missiles]], and [[Drone parts|drone parts]])
* 2-4 slots of [[Systems|systems]], [[Weapons|weapons]], [[Drone_Control#Drone_Schematics|drone schematics]], [[Augmentations|augmentations]], and [[Crew Members|crewmembers]]

Hull repairs prices vary depending on sector progression: the cost of repairing 1 hull point of damage is determined by the sector number.

Fuel, missiles, and drone parts stock varies, but the price for each type of resource is fixed.

Each slot contains three random items (or crewmembers) of that type (for example, three random weapons). A store will never sell duplicate weapons, drone schematics, augmentations.

===<h2>Systems</h2>===
Stores may sell three random systems. Systems are installed on your ship in a predetermined location. If you buy a teleporter, it will always have two slots, not four.

Filling all your system slots will not prevent stores from selling systems, even though you can't buy them (except for medical systems, which replace your current one). If your ship has less than 11 systems+subsystems, there is a 50% chance the first store slot will be forced to be systems<!--for sources, see: https://ftl.fandom.com/wiki/Message_Wall:Mike_Hopley?threadId=4400000000000118913-->. When a store is selling systems, the selection is mostly random, but is governed by a few special rules:
*Stores cannot sell a system you already own
*Shields are '''guaranteed''' if you don't have them
*A medical system is '''guaranteed''' if you don't have one
*A drone system is guaranteed if the store also sells drones

{{Purchasable systems}}

===<h2>Items and crew rarity</h2>===
Rarity is a hidden attribute of [[weapons]], [[Drone_Control#Drone_Schematics|drone schematics]], [[augmentations]], and [[crew races]]. It is used to determine the likelihood of a specific item or a crew race to be found in stores and the possibility (without the likelihood tiers) for an item or a crew race to be received as an event reward in certain sector types.

Rarity normally goes from 1 to 5, 1 being common and 5 being rare.

If rarity is set to 0 on a specific item, then it cannot be randomly found in game. This usually happens in one of the following cases:
* An item only found with special requirements. (e.g. [[Augmentations#Damaged_Stasis_Pod|Damaged Stasis Pod]])
* An item only comes equipped on a particular ship. (e.g. [[Drone_Control#Shield_Overcharger_.2B|Shield Overcharger +]])
* An item only used by the AI. (e.g. [[Missiles_(Weapon)#Boss_Missile|Boss Missile]])
* An item only used for specific game mechanics. (e.g. crystal shard of [[Augmentations#Crystal_Vengeance|Crystal Vengeance]])

Every sector has a table of loot which then gets weighted by its rarity and selected accordingly, e.g.: [[Bomb_(Weapons)#Crystal_Lockdown_Bomb|Crystal Lockdown Bomb]] has different rarity values for certain sectors; other crystal weapons and crystal crewmembers cannot be acquired outside of Hidden Crystal Worlds (except for one particular [[Zoltan research facility|event]], regarding the crew); Lanius crewmembers are only encountered in Abandoned sectors.

===<h2>Weapons</h2>===
{{Purchasable weapons}}

===<h2>Drones</h2>===
{{Purchasable drones}}

===<h2>Augmentations</h2>===
{{Purchasable augmentations}}

===<h2>Crewmembers</h2>===
Stores may sell three random crew. Stores can sell duplicate crew (for example, a store could sell three Engi).

{{Crew races cost and rarity (sorting by race)}}


==<span style="font-size:larger;">'''Resources'''</span>==
Besides stores, resources can be exchanged for scrap and other goods in different [[:Category:Trading Events|trading events]], and are often awarded for defeating enemy ships, accepting surrenders or bribes. The amount of resources rewards does not vary by sector number or difficulty (see [https://mikehopley.github.io/ftl-scrap/easy#resources link]).

* [[:Category:Events with Resources use|Events with Resources use]]
* [[:Category:Resources Rewards|Events with Resources rewards]]
* [[:Category:Resources loss Events|Events with Resources loss risk]]

===<h2>[[File:Fuel.png]] Fuel</h2>===
''"Powers your FTL drive. One jump per fuel."''

Fuel cells are required to make FTL Jumps. Each jump between beacons costs 1 fuel, including backtracking to previously visited ones.

All ships start with 16 fuel. Fuel costs 3 [[File:Ftlgame-scrap.png]] from stores, or 2 [[File:Ftlgame-scrap.png]] from refuelling station events.
[[File:NO_FUEL.png|thumb|No Fuel!]]
If the player attempts to perform an FTL Jump with no fuel remaining, the Sector Map will spell out "NO FUEL" and will instead offer the option to Wait for one turn, with the Rebels advancing the same distance as they would after a regular FTL Jump. The Rebel advance will be slowed if you are in a nebula (just like a normal nebula jump).

A distress beacon can be activated before waiting. The distress beacon increases the chances of being found by a ship, either hostile or friendly, and therefore increases the chance of obtaining fuel.

When you are out of fuel, all enemy ships will start the fight charging their FTL drives, and will usually jump away after 90 seconds if not interrupted or stopped. There is also an additional anti-stalemate mechanism: when the enemy ship is below a certain hull threshold (likely below 50%, closer to 30-40%) and doesn't receive any more hull damage for 1 minute, the fight ends by granting you 2 fuel; the enemy boarder can sometimes postpone this trigger, but the trigger will work in 60 seconds after the end of the enemy boarder dying animation. (see [https://ftl.fandom.com/wiki/File:No_fuel_anti-stalemate.png screenshot]) <!-- @todo: provide more specific details, including the precise hull values. --- ?does hull damage caused by fires reset the 60 seconds timer? --- the example screenshot features a rock pirates rock scout ship in sector 3 on hard. --- based on multiple observations, it appears that the status of the enemy piloting system doesn't affect this mechanic - it doesn't matter whether the Piloting is fully functional or completely destroyed -->

* [[:Category:Out of Fuel Distress ON Events|Out-of-Fuel Events (Distress ON)]]
* [[:Category:Out of Fuel Distress OFF Events|Out-of-Fuel Events (Distress OFF)]]
* [[:Category:Fuel use Events|Fuel use Events]]
* [[:Category:Fuel Rewards|Fuel reward Events]]
* [[:Category:Fuel loss risk|Fuel loss risk Events]]

===<h2>[[File:Missiles.png]] Missiles</h2>===
"''Multipurpose ammo for any missile based weapon.''"

One missile ammunition is consumed when a [[Missiles (Weapon)|missile]] or [[Bomb (Weapon)|bomb]] is fired. You can reduce missile consumption with the [[Augmentations#Explosive_Replicator|Explosive Replicator]] augment, which provides a 50% chance of not consuming a missile.

* [[:Category:Missiles use Events|Missiles use Events]]
* [[:Category:Missiles Rewards|Missiles reward Events]]
* [[:Category:Missiles loss risk|Missiles loss risk Events]]

===<h2>[[File:DroneParts.png]] Drone parts</h2>===
"''Allows you to deploy drone schematics you've found. Each deployment costs one drone part.''"

Drone parts are consumed when deploying [[drones]] and by launching a [[hacking]] drone. Drone parts can be recovered from some external drone types after they have been deployed and weren't destroyed - with the [[Augmentations#Drone_Recovery_Arm|Drone Recovery Arm]] augment.

* [[:Category:Drone Parts use Events|Drone Parts use Events]]
* [[:Category:Drone Parts Rewards|Drone Parts reward Events]]
* [[:Category:Drone Parts loss risk|Drone Parts loss risk Events]]


==<span style="font-size:larger;">'''See also'''</span>==
* [https://gitlab.com/znixian/xftl/-/blob/master/doc/stores Reverse-engineered data on stores: store sections generation, filling out a store section, selecting systems]

[[Category:Mechanics]]
