<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Mantis war camp
URL: https://ftl.fandom.com/wiki/Mantis_war_camp
Categories: Random_Events, Unique_Events
Revision: 74270
Retrieved: 2026-08-09

---
{{Locations|Civilian Sector|Zoltan Controlled Sector|Zoltan Homeworlds|LRSmap=noship|unique=true}}


''You receive a request, "All of our military ships have been destroyed or damaged during the rebellion. However, there have been reports of a Mantis war camp only a few jumps from us. Can you help?"''
# Pledge to do what you can.
#* ''"Thank you! If you can just give us a count on their numbers perhaps we can get the Rebels to help."''
#** You receive medium [[Rewards#Scrap only|scrap]] and a [[#Quest Marker|'''quest marker''']] is added to your map.
# Apologize and decline.
#* Nothing happens.

==Quest Marker==
:{{Long-Ranged Scanners info|shipdetected=noship}}

''You find the Mantis encampment but there are far too many of them to count accurately. You send a long range message back to the settlement with your findings but unfortunately there's not much you can do. It would be suicide to attack directly.''
# Leave before they notice you.
#* ''As you try to leave, a patrol spots you. Wailing sirens begin to blare around the camp and the ship moves in to attack!''
#** Fight a [[Mantis Ships|Mantis ship]]. <ref name="Enemy ship (MANTIS_LANDING_PARTY)">{{SurrenderEscape(alt)|no|MANTIS_LANDING_PARTY|events.xml}}</ref>
#*** {{Winning|destroyed=true|With the patrol ship destroyed you hasten to leave. It won't be long before the other ships catch up.}}
#**** You receive medium [[Rewards#Standard|scrap with resources]].
#*** {{Winning|deadCrew=true|With the patrol ship taken care of you hasten to leave. It won't be long before the other ships catch up.}}
#**** You receive high [[Rewards#Standard|scrap with resources]].
#* ''They must have been focused on setting up camp since you got far enough away to attempt a jump without being noticed.''
#** Nothing happens.
# {{Blue Option|Missile Weapon|Bombard their key structures.}} &nbsp;[ {{Transaction|1|subtract_missiles}} ] &nbsp;-- bugged: Hull Missile doesn't count.
#* ''You fire at their fuel depot, but a shot from the surface rips the missile to shreds. They must have a planetary defense system set up already! You try to get away but a nearby patrol ship moves in to attack.''
#** Fight a [[Mantis Ships|Mantis ship]]. <ref name="Enemy ship (MANTIS_LANDING_PARTY)" />
#*** {{Winning|destroyed=true|With the patrol ship destroyed you hasten to leave. It won't be long before the other ships catch up.}}
#**** You receive medium [[Rewards#Standard|scrap with resources]].
#*** {{Winning|deadCrew=true|With the patrol ship taken care of you hasten to leave. It won't be long before the other ships catch up.}}
#**** You receive high [[Rewards#Standard|scrap with resources]].
# {{Blue Option|Fire Bomb|Teleport fire bombs into key structures.}} &nbsp;[ {{Transaction|2|subtract_missiles}} ]
#* ''It appears they have not set up a Teleporter disruption field yet. You deposit one bomb in a fuel depot and another in the barracks. Mantis comm channels fill with panicked chatter and you watch a number of structures go up in flames.''
#** ''With most of their ships and forces focused on the chaos, you slip undetected to a nearby depot. You find some useful resources and an Engi slave who gladly accepts your liberation.''
#*** You receive an <span style="color:limegreen">Engi crewmember</span> and high [[Rewards#Stuff|resources with some scrap]].

==Notes==
This event is called "QUEST_MANTIS_INVASION_START" in the datafiles.
===Reference notes===
<references/>
[[Category:Events with Quest Markers]]
[[Category:Missiles use Events]]
[[Category:Crew reward opportunity]]
