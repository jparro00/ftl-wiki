<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: No fuel: explore the system
URL: https://ftl.fandom.com/wiki/No_fuel:_explore_the_system
Categories: Random_Events, Trading_Events
Revision: 73276
Retrieved: 2026-08-09

---
{{Locations|outoffuel=distressboth}}


''Although your lack of fuel cells prevents your ship from jumping, you can still use your impulse engines. Will you spend some time exploring the nearby system?''
# Explore the nearby area.
#* ''You find a small outpost for local travelers, but it seems few ships in this area employ FTL drives. Their stock of fuel cells is small and their price high, but beggars can't be choosers...''
#*# Trade 20 scrap for 5 fuel. &nbsp;[ {{Transaction|20|subtract_scrap}} ]
#*#* ''You gladly make the trade.''
#*#** You receive {{Transaction|5|add_fuel}}.
#*# Trade 10 scrap for 2 fuel. &nbsp;[ {{Transaction|10|subtract_scrap}} ]
#*#* ''This fuel won't last long, but you gladly make the trade.''
#*#** You receive {{Transaction|2|add_fuel}}.
#*# Trade 5 scrap for 1 fuel. &nbsp;[ {{Transaction|5|subtract_scrap}} ]
#*#* ''This fuel won't last long, but at least you can jump to another beacon.''
#*#** You receive {{Transaction|1|add_fuel}}.
#*# Don't make a trade.
#*#* Nothing happens.     
#* ''You happen across a small asteroid field near the beacon.''
#*# Approach the asteroid field to scan it.
#*#* ''Scans reveal a number of asteroids with useful compositions. You extract some fuel.''
#*#** You receive {{tooltip|high|3-6}} [[Rewards#Fuel_only|fuel]].
#*#* ''You discover the remains of ship embedded into an asteroid. It still has some functional missiles.''
#*#** You receive {{tooltip|medium|2-4 missiles}} [[Rewards#Missiles|missiles and scrap]].
#*#* ''You happen upon an abandoned mining site. A few mining drones were left behind and could be repurposed.''
#*#** You receive {{tooltip|medium|1 drone part}} [[Rewards#Drone_parts|drone parts and scrap]].
#*#* ''A pirate ship hiding behind one of the larger asteroids attacks you!''
#*#** Fight a [[Enemy Ships|Pirate ship]] ([[Rewards#Default_rewards|default rewards]]) in an[[File:Danger_asteroids.png|bottom|35px|astreroid field]]<span style="color:red">asteroid field</span>. <!-- Ship - PIRATE. Datafile - events_ships.xml -->{{SurrenderEscape|timer|90}}
#*#* ''The asteroid field proved more dangerous than expected. Some asteroids managed to get through your ship's defenses.''
#*#** Your ship takes <span style="color:red">5 hull</span> damage, 1 damage to a random <span style="color:red">system</span>, 1 damage with [[File:S_fire2.png|28px|bottom|1-2 fires|alt=fire]] to a random <span style="color:red">room</span>.
#*#* ''A brief exploration yields nothing of interest.''
#*#** Nothing happens.
#*# Avoid the risk.
#*#* Nothing happens.
#* ''You wander within scanning range of a small Rebel automated scout!''
#** Fight an [[AI-Controlled_Rebel_Ships|Auto-ship]] that is '''running away'''. <!-- Ship - REBEL_AUTO_FUEL. Datafile - events_ships.xml -->{{SurrenderEscape|timer|80}}
#*** {{Winning|gotaway=true|The ship jumps away without a word. You hope they didn't leave to get reinforcements.}}
#**** Nothing happens.
#*** {{Winning|destroyed=true|The ship explodes, leaving behind a collection of useful scrap material.}}
#**** You receive {{tooltip|medium|2-4 fuel}} [[Rewards#Fuel|fuel and scrap]].
#* ''No ships respond to your hails, and you find nothing of interest.''
#** Nothing happens.     
# Stay near the beacon.
#* Nothing happens.

==Trivia==
This event is called "FUEL_EXPLORE" in the datafiles.
* Asteroid field exploration scenario can also occur in the [[Large asteroid field]] event which additionally has [[Augmentations#Scrap_Recovery_Arm|Scrap Recovery Arm]] blue option.
[[Category:Trading Events]]
[[Category:Fire risk]]
[[Category:Hull damage risk]]
[[Category:System damage risk]]
[[Category:Asteroid Field risk]]
[[Category:Fights with Default Rewards]]
[[Category:Ship escape Events]]
[[Category:Auto-ship fights]]
[[Category:Pirate ship fights]]
