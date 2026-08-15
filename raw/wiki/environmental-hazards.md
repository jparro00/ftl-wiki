<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-15. Source layer: do not edit. -->
Title: Environmental Hazards
URL: https://ftl.fandom.com/wiki/Environmental_Hazards
Categories: Mechanics
Revision: 74893
Retrieved: 2026-08-15

---
{| class="table" align="right" style="margin-left: 15px;"
| align="center" |[[File:LRS_hazard_beacon_with_ship.png]]<br /><span style="font-size: smaller;">A {{tooltip|beacon|(revealed by the Long-Ranged Scanners augmentation or beacon map reveal reward)}} with<br />environmental hazard</span>
|}

Some [[beacon]]s have '''environmental hazards''', which have certain effects on the ships staying at the beacon.

Solar flares, asteroid fields, pulsars, and enemy ASBs will impose permanent <span style="color: red;">'''IN DANGER'''</span> status while staying at the beacon: it prevents opening the ship menu to perform ship and reactor upgrades, access the cargo bay to swap weapons and drone schematics, and crew management.

A beacon with an environmental hazard and no hostile ship, upon revisiting, will not have the hazard anymore (except for, a regular nebular environment or if the beacon is overtaken by the Rebels).

==Class-M Red Giant Star==
:''For red giant events, see [[:Category:Red Giant Events|Red Giant Events]].''

[[File:Planet_sun1_300px.png|65px]] ''Beacon coordinates appear to be very close to a nearby sun.''

[[File:Solar_Flare_danger.png]] ''<!--You're too close to a star. -->Solar flares will light the ship on fire. Shields will reduce the effect.''

Solar flares periodically light fires on your ship and any enemy ship, with a chance to also damage hull and systems in the affected rooms. The solar flare triggers randomly every 28-34 seconds, with a warning 5 seconds beforehand.

The effect is reduced when you have shields up, including a Zoltan Shield. Having additional layers of shield makes no difference.

With shields up, a flare will start 1 or 2 fires. When shields are down, it will start 3-6 fires. These fires are placed in random rooms, with either 1 or 2 of the total fires randomly allocated to each room.

Each room where fires are started has a chance to take 1 hull (and system) damage, depending on how many fires were started in that room: 33% chance from one fire, and 66% chance from two.

With shields down, the maximum possible hull damage is 6, but the chance of this happening is about 1 in 93,000.

{{Solar Flare effects}}

For more details on how the solar flare fires spawn and work, see [https://gitlab.com/znixian/xftl/-/blob/master/doc/solar-flares reverse-engineered data on solar flares].

==Asteroid Field==
:''For asteroid field events, see [[:Category:Asteroid Field Events|Asteroid Field Events]].''

[[File:Low_asteroid_1.png|65px]] &nbsp;''Asteroid field detected in this location.''&emsp;[[File:Asteroid_danger.png]] ''<!--You're in an asteroid field. -->Periodically asteroids will strike your ship.''

Asteroids will periodically fly towards your ship. Unless dodged, they will either knock down a single shield layer or deal 1 point of hull and system damage to a random room on the ship. They have a small chance to cause a fire or a breach. They have the same effect on enemy ships.

The interval between each asteroid is random, but scales according to '''your ship's''' shield system level: asteroids will come more frequently if your shields are highly upgraded. This potentially makes ion-heavy enemy weapons extremely dangerous in an asteroid field, since the asteroid frequency will not decrease when your shields are down. Nevertheless, shield upgrades generally make your ship much safer in asteroid fields.

Defense drones can shoot down asteroids, but will often fail to hit them before the asteroid takes down a shield layer.

Your crew can gain skill in shields and evasion from asteroids. Skill can only be gained while you are in combat with an enemy ship, even though the asteroids keep coming after the battle.

==Pulsar==
:''For pulsar events, see [[:Category:Pulsar Events|Pulsar Events]].''

[[File:Pulsar_white.png|65px]] ''A pulsar is flooding this area with dangerous electromagnetic forces.''&emsp;[[File:Pulsar_danger.png]] ''<!--You're close to a pulsar. -->Periodic waves of electromagnetic energy will disrupt your systems.''

You can encounter a pulsar only if you play with [[Advanced Edition]] content on.

An ion pulse will occur every 11--18 seconds, with a warning 5 seconds beforehand. The ion pulse will randomly ionise 2 systems on your ship, and 2 systems on the enemy ship. The amount of ion damage depends on the amount of power in the system. The formula is: ion damage = 1 + 0.5(system power), rounded down.

{{Pulsar ion damage}}

Subsystems will take ion damage according to their system level, including the temporary upgrade level from crew manning them. For example, level 3 doors will take 3 ion damage when crew are manning them.

If shields are powered, one of the two random systems ionized will always be shields. If shields are unpowered, they can still be ionised randomly as can any other system, but will only take 1 ion damage. Therefore it may be tactically useful to unpower your shields just before the pulse hits, reducing their downtime. Alternatively, a single Zoltan can be positioned in the shields room to force the system to be ionized (albeit minimally) by the pulse, so that only 1 other (totally random) system or sub-system gets ionized instead of 2 random systems when the shields are completely depowered - this can help reduce the chances of other, more vital to the situation, systems to be ionized, e.g. weapons or cloaking.

[[Zoltan_shield|Zoltan Shield]] completely absorbs the ion pulse, taking 3 or 4 ion damage and protecting all systems. A single layer of Zoltan Shield is enough to block a pulse, making the [[Drone_Control#Shield_Overcharger|Shield Overcharger]] drone very effective. However, a Zoltan Shield will '''not''' protect a ship that lacks a shield system (the ion pulse will ignore the Zoltan Shield); this is likely a bug.

[[Augmentations#Reverse_Ion_Field|Reverse Ion Field]] augmentation acts against the entire pulse: two or zero systems will be ionised, never 1. Zoltan Shields will not take damage if the pulse is resisted. Two or more stacks of the augmentation grant complete immunity from all sources of ion damage, including that from a pulsar, and also protect a Zoltan Shield.

[[Crew_Members#Zoltan|Zoltan]]s don't protect systems or subsystems from ion damage. However, they can supply their zoltan power to an ionized system (but not to a subsystem), and this power cannot be removed by anything, except for by moving Zoltans out of the room.

Tips on Pulsars: [https://www.youtube.com/watch?v=FcfjeR9GIhQ video (1)].

==Nebula==
:''For nebula events, see [[:Category:Nebula Events|Nebula Events]].''

[[File:Low storm 1.png|65px]] ''You're inside a nebula. Your sensors will not function, but the Rebel fleet will advance more slowly towards you.'' [[File:Danger_nebula.png]]<!-- Nebula beacon description: ''"The nebula here will make fleet pursuit slower but will disrupt your sensors."'' -->

Nebulas disable your [[Sensors]]. [[Crew_Members#Slug|Slugs']] telepathic abilities or [[Augmentations#Lifeform Scanner|Lifeform Scanner]] will allow you to see enemy crew regardless.

The speed that the Rebels chase you is reduced while inside a nebula, by 50% in most sectors and by 20% inside [[Sector#Nebulae Sectors|nebula sectors]]. Nebulas do not count as environmental hazards for the purpose of the [[Ship_Achievements/Tactical_Approach|Tactical Approach]] achievement.

==Plasma/ion Storm==
:''For plasma/ion storm events, see [[:Category:Plasma Storm Events|Plasma Storm Events]].''

[[File:Low storm 2.png|65px]] ''This section of the nebula is experiencing a plasma storm. Your main reactor can only function at half capacity.''[[File:Danger_storm.png]]<!-- Plasma/ion Storm beacon description: ''"This section of the nebula is experiencing an ion storm."'' -->

Some nebula beacons contain ion storms (also called plasma storms), which make your reactor run at half-efficiency (rounded up). Zoltan power is not affected, nor is power from the [[Backup Battery]]. You will need to use your remaining power efficiently.

Power will be removed automatically from systems as you arrive, potentially causing you to lose shields and take damage from an enemy drone. You can prevent this by leaving enough spare power in the reactor before you jump.

Enemy ships' reactors are also halved, which can make the battle easier. They can re-allocate power when systems are ionised or damaged, potentially doubling their shields or deploying a new weapon or drone mid-battle. If the current enemy power usage is favourable to you, consider attacking only rooms that do not use power (such as piloting).

When the Rebel fleet overtakes a nebula beacon, it will '''always''' have an ion storm, even if it didn't have one beforehand. However, overtaken nebula exit beacons cannot have ion storms.

==Anti-Ship Battery (ASB)==
:''For events with hostile ASBs, see [[:Category:Anti-Ship Battery hazard risk|Anti-Ship Battery hazard risk events]].''
:''For events with friendly ASBs, see [[:Category:Anti-Ship Battery support|Anti-Ship Battery support events]].''

''Planet-side anti-ship batteries are detected in this system.''<!-- @to-do: add cropped image of rebel battleships --> [[File:ASB_danger.png]] ''The Fleet's Anti-Ship Batteries are targeting you.''

ASBs periodically fire a shield-piercing 3-damage shot at your ship, hitting a random room, and always causing a hull breach. These shots can be evaded but cannot be shot down. ASB shots bypass [[Zoltan shield|Zoltan Shields]]: the Zoltan shield takes no damage, but the ship will take hull and system damage.

Although many shots will be animated firing at you during this hazard, most are harmless and purely for cosmetic effect. You receive a warning 15--20 seconds after the battle starts, and the "real" ASB shot appears 5--10 seconds later. This cycle continues indefinitely until you escape. The real ASB projectile appears following the fake ASB projectile that comes after the target lock-on signal; if the fake ASB shot appeared after the signal or simultaneously, another fake ASB shot will appear prior to the real one. The gap between the fake and the real shot can be long (few seconds) or very short (a fraction of a second), and may change with each ASB cycle.

If you are overtaken by the [[Rebel Fleet]], an ASB will always be present, with two exceptions: they don't appear if you are at a [[Environmental Hazards#Nebula|nebula beacon]], or at the [[Beacon#Exit|exit beacon]] while playing on easy mode. However, if you are out of fuel and '''waiting''' at a nebula beacon when the Fleet overtakes it, the nebula environment will be removed, and you will face an ASB as well as the Rebel Elite. If you have 0 fuel after a jump to the nebula beacon overtaken by Rebel Fleet, as expected, there will be no ASB: the beacon will have a Plasma Storm, or it will be a regular nebula environment in case of an exit beacon - and the enemy ship will start to run away with 90 seconds escape timer.<!-- @todo: test if the Rebel Elite drops 4 fuel when it is destroyed, just like when you destroy it in a fight during the WAITING instance. -->

There are some [[:Category:Anti-Ship Battery hazard risk|events with hostile ASBs]], as well as few [[:Category:Anti-Ship Battery support|events with friendly ASBs]] (which target the enemy ship).

ASBs are not considered an Environmental Hazard for the Stealth Cruiser achievement [[Tactical Approach]].

==Environmental hazard events (table)==
{{Environmental hazard events}}

==See also==
* [https://gitlab.com/znixian/xftl/-/blob/master/doc/asteroids Reverse-engineered data on asteroids]
* [https://gitlab.com/znixian/xftl/-/blob/master/doc/solar-flares Reverse-engineered data on solar flares]
[[Category:Mechanics]]
