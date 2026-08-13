<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Remote settlement
URL: https://ftl.fandom.com/wiki/Remote_settlement
Categories: Random_Events, Unique_Events
Revision: 73835
Retrieved: 2026-08-09

---
{{Locations|Civilian Sector|LRSmap=ship|unique=true}}


''Scans show a remote settlement being blockaded by a pirate ship. The ship hastily messages you, "Stay out of this, or you'll be next!...Concentrate fire on..."''
# Attack the pirate.
#* ''"You asked for it!" They pull away from the planet and move in to engage.''
#** [[#Fight the pirate ship|'''Fight the pirate ship''']].
# Ignore them.
#* ''It's just not possible to save every civilian affected by this war. You prepare to jump.''
#** Nothing happens.
# {{Blue Option|Fire Beam|Show the pirate how to intimidate settlers: burn their crops!}}
#* ''The pirate watches as you start to light the meager crops on fire. In a few moments the settlement surrenders, offering tribute to leave them alone. The pirate seems impressed.''
#** You receive a <span style="color:limegreen">drone schematic</span> with high <span style="color:#70b8ff">scrap</span>.
# {{Blue Option|Fire Bomb|Show the pirate how to intimidate settlers: start fires in their crude dwellings.}} &nbsp;[ {{Transaction|1|subtract_missiles}} ]
#* ''The pirate watches as you teleport an incendiary explosive into their settlement. As the settlers scramble to put out the fires, their rudimentary planetary defenses power down. Forcing their surrender was almost laughably easy, but the pirate seems impressed with your tactics and agrees to share the settlement's 'tribute'.''
#** You receive a <span style="color:limegreen">drone schematic</span> with high <span style="color:#70b8ff">scrap</span>.

==Fight the pirate ship==
* {{Winning|escape=true|They look like they don't want to fight. They are trying to escape.}}&nbsp;<!-- ship name="PIRATE_STATION_CROPS" (events_ships.xml) --><span style="color:grey">(50% chance for escape attempt at 30-40% hull)</span>
** {{Winning|gotaway=true}}
*** You contact the station.
**** ''With the pirates gone you signal the station. "We appreciate what you've done, but there'll<!-- sic! --> just be another ship looking to profit from our isolation soon enough. Sorry we can't give you more."''
***** You receive {{Tooltip|low|fuel: 1-3 ; missiles: 1-2 ; drone parts: 1}} [[Rewards#Stuff|resources with scrap]].
* {{Winning|surrender=true|"Alright! We give up! We're terrible at this pirating thing anyway..."}} &nbsp;<!-- ship name="PIRATE_STATION_CROPS" (events_ships.xml) --><span style="color:grey">(50% chance for surrender offer at 20-40% hull)</span>
*# Let them go.
*#* You receive {{Tooltip|medium|fuel: 2-4 ; missiles: 2-4 ; drone parts: 1}} [[Rewards#Stuff|resources with some scrap]].
*# Piracy cannot be forgiven. Attack!
*#* The fight continues.
* {{Winning|destroyed/deadCrew=true|You pick through the remains and contact the settlement.}}
** You receive medium [[Rewards#Standard|scrap with resources]].
*** You contact the station.
**** ''With the pirates gone you signal the station. "We appreciate what you've done, but there'll<!-- sic! --> just be another ship looking to profit from our isolation soon enough. Sorry we can't give you more."''
***** You receive {{Tooltip|low|fuel: 1-3 ; missiles: 1-2 ; drone parts: 1}} [[Rewards#Stuff|resources and scrap]].

==Trivia==
This event is called "PIRATE_STATION_CROPS" in the datafiles.
[[Category:Drone Schematics reward opportunity]]
[[Category:Missiles use Events]]
[[Category:Events with Stuff rewards]]
[[Category:Pirate ship fights]]
