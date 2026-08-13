<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Space station under construction
URL: https://ftl.fandom.com/wiki/Space_station_under_construction
Categories: Random_Events, Unique_Events, Trading_Events
Revision: 74321
Retrieved: 2026-08-09

---
{{Locations|Civilian Sector|LRSmap=noship|unique=true}}

__TOC__
''You come across a space station under construction. You receive a message from their command tower, "Greetings. We recently lost contact with a cargo ship that was set to deliver more construction materials. Could you help us figure out what happened to them?"''
#Offer your help.
#*''"Great. Thanks for your help. I've marked their last known coordinates and sent over some supplies to help you get there."''
#**You receive {{Transaction|2-4|add_fuel}} {{Transaction|0-4|add_missiles}} {{Transaction|0-2|add_drones}}, and a [[#Quest Marker|'''quest marker''']] is added to your map.
#Decline.
#*''"I understand." Transmission has been cut.''
#**Nothing happens.
#{{Blue Option|Lanius Crew|Offer to have your crewmember help.}}
#*''"Interesting. So this metal man can help us make some of these unique parts out of scrap? That would be a huge help." Your crewmember checks over the blueprints and quickly converts some of their base metal sheets into the specialized parts.''
#**''"Amazing! This robot thing could save us a ton of time. Could I buy it off you?"''
#**#Ask your crew if they agree.
#**#*''Once your Lanius crewmember understands the situation, it appears to like the idea of assisting with construction in deep space. Much less dangerous. They offer you some goods in exchange.''
#**#**You <span style="color:red">lose</span> a <span style="color:red">Lanius crewmember</span>, and receive an <span style="color:limegreen">augmentation</span> with high <span style="color:#70b8ff">scrap</span>.
#**#***<span style="color:#70b8ff">(Clone Bay)</span> [<span style="color:red">no effect</span>] &nbsp;''Your clonebay obviously does not revive your crewmember since they did not die.''
#**#Our crew is not for sale.
#**#*"''A pity. In terms of payment, here's some of the scrap metal we don't need, now that we've got the necessary parts.''"
#**#**You receive medium [[Rewards#Scrap only|scrap]].


==Quest Marker==
One of the following subevents occurs:
* [[#Cargo ship docked to a Rebel station|'''The cargo ship is docked to a Rebel station''']]
* [[#Cargo ship docked to an empty space station|'''The cargo ship is docked to an empty space station''']]
* [[#Cargo ship floating near the beacon|'''The cargo ship is floating near the beacon''']]<br /><br />

==='''Cargo ship docked to a Rebel station'''===
''You find the missing cargo ship docked to a Rebel station. You send a short-band message to them and discover they are being held against their will and forced to 'donate to their supplies for the war effort.'''
#Attack the Rebels to help them escape.
#*''You move in to attack the Rebel ship that is threatening them and scanners detect weapon locks from a nearby Anti-Ship Battery. It's about to get hectic!''
#**Fight a [[Rebel Ships|Rebel ship]] while a planet-side[[File:Danger_pds.png|35px|bottom]]<span style="color:red">Anti-Ship Battery</span> periodically fires on your ship. <ref name="Enemy ship (QUEST_CONSTRUCTIONYARD_SHIP)">{{SurrenderEscape(alt)|no|QUEST_CONSTRUCTIONYARD_SHIP|newEvents.xml}}</ref>
#***{{Winning|destroyed=true|You quickly salvage what you can from the ship.}}
#****You receive medium [[Rewards#Standard|scrap with resources]].
#*****Contact the cargo ship.
#******''Amidst the blasts from the Anti-Ship Battery, the cargo ship escaped from the station. They jettisoned some scrap towards your ship before jumping away.''
#*******You receive medium [[Rewards#Scrap only|scrap]].
#***{{Winning|deadCrew=true|You quickly salvage what you can from the ship.}}
#****You receive high [[Rewards#Standard|scrap with resources]].
#*****Contact the cargo ship.
#******''Amidst the blasts from the Anti-Ship Battery, the cargo ship escaped from the station. They jettisoned some scrap towards your ship before jumping away.''
#*******You receive medium [[Rewards#Scrap only|scrap]].
#Leave.
#*''You apologize but it's not worth the risk to attack a Rebel station.''
#**Nothing happens.<br /><br />

==='''Cargo ship docked to an empty space station'''===
''You find the missing cargo ship docked to an empty space station. However their hold appears to be empty and there are no obvious signs that anyone is inside the ship or station. Everything looks abandoned.''
{{:Abandoned station}}<br /><br />

==='''Cargo ship floating near the beacon'''===
''You find the missing cargo ship floating near the beacon. "Thank heavens! We've been drifting here after using the last of our fuel to escape a pirate raid."''
#Give them the requested 4 fuel. &nbsp;[ {{Transaction|4|subtract_fuel}} ]
#*''"Great, thank you. Here's some scrap metal for your troubles. Be careful out there."''
#**You receive medium [[Rewards#Scrap only|scrap]].
#Give them 1 fuel. &nbsp;[ {{Transaction|1|subtract_fuel}} ]
#*''"Well, I suppose that's better than nothing. Thank you. Hopefully we can find a station at the next Beacon."''
#**Nothing else happens.
#Do not give them any.
#*''"I see..."''
#**Nothing happens.

==Notes==
This event is called "QUEST_CONSTRUCTIONYARD" in the datafiles. 
* [[#Cargo ship docked to an empty space station|The cargo ship is docked to an empty space station]] subevent can also be found as [[Abandoned station]] standalone event with different intro texts.
===Reference notes===
<references/>
[[Category:Advanced Edition Content Events]]
[[Category:Events with Quest Markers]]
[[Category:Trading Events]]
[[Category:Anti-Ship Battery hazard risk]]
[[Category:Boarding risk]]
[[Category:Augmentation reward opportunity]]
[[Category:Crew reward chance]]
[[Category:Clone Bay failed revival]]
[[Category:Fuel reward]]
[[Category:Missiles reward chance]]
[[Category:Drone Parts reward chance]]
[[Category:Pirate ship fights]]
