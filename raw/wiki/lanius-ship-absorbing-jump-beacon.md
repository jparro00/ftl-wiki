<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Lanius ship absorbing jump beacon
URL: https://ftl.fandom.com/wiki/Lanius_ship_absorbing_jump_beacon
Categories: Random_Events, Unique_Events, Trading_Events
Revision: 74232
Retrieved: 2026-08-09

---
{{Locations|Abandoned Sector|LRSmap=ship|unique=true}}


''You detect a damaged vessel docked with the jump beacon. It appears the Lanius are absorbing metal from the beacon, risking destroying it and becoming stranded.''
# Ask if they require assistance.
#*''After a long message the translator only able to spurt out "critical... must... metal..." You can only surmise they must be desperate for scrap.''
#*#Give them 30 scrap. &nbsp;[ {{Transaction|30|subtract_scrap}} ]
#*#* ''You release the material of the airlock and the Lanius quickly collect it and start melting it down. They are grateful for your assistance and send over a ship augmentation.''
#*#** You receive an <span style="color:limegreen">augmentation</span>.
#*# Leave.
#*#* {{DuplicateEvent|3}} ''You prepare to jump as soon as possible. You don't want to be around if they disable this beacon.''
#*#** Nothing happens.
#*#* ''You make preparations to jump but are surprised when the Lanius ship pulls away from the beacon towards you. It appears to be fully operational!''
#*#** Fight a [[Lanius Ships|Lanius ship]] ([[Rewards#Default_rewards:_Lanius|default Lanius rewards]]). <ref name="Enemy ship (LANIUS_SHIP)">{{SurrenderEscape(alt)|escape+surrender|LANIUS_SHIP|dlcEvents_anaerobic.xml|80|20-40|2-4|80|30-40|3-4}}</ref>
#* ''You begin to message the ship but it quickly powers on its weapons defensively. It appears to be fully functional and looking for a fight!''
#** Fight a [[Lanius Ships|Lanius ship]] ([[Rewards#Default_rewards:_Lanius|default Lanius rewards]]). <ref name="Enemy ship (LANIUS_SHIP)" />
# Send them 30 scrap. &nbsp;[ {{Transaction|30|subtract_scrap}} ]
#* ''You release the material out of the airlock and the Lanius quickly collect it and start melting it down. They are grateful for your assistance and send over a ship augmentation.''
#** You receive an <span style="color:limegreen">augmentation</span>.
#* ''You release the scrap out of the airlock and they greedily collect it. Shortly afterwards their impulse engines flicker on and they power up their weapons. It appears you haven't sated their lust for metal.''
#** Fight a [[Lanius Ships|Lanius ship]] ([[Rewards#Default_rewards:_Lanius|default Lanius rewards]]). <ref name="Enemy ship (LANIUS_SHIP)" /> &nbsp;<span style="color:grey">(spent 30 scrap won't be refunded)</span>
# Leave.
#* {{DuplicateEvent|3}} ''You prepare to jump as soon as possible. You don't want to be around if they disable this beacon.''
#** Nothing happens.
#* ''You make preparations to jump but are surprised when the Lanius ship pulls away from the beacon towards you. It appears to be fully operational!''
#** Fight a [[Lanius Ships|Lanius ship]] ([[Rewards#Default_rewards:_Lanius|default Lanius rewards]]). <ref name="Enemy ship (LANIUS_SHIP)" />
# {{Blue Option|Lanius Crew|Ask if they require assistance.}}
#* ''After a time you are told they were damaged and unable to repair their ship due to a lack of metal. They offer to exchange a piece of their ship's equipment for some scrap or other useful materials.
#*# Give them 30 scrap. &nbsp;[ {{Transaction|30|subtract_scrap}} ]
#*#* ''You release the material out of the airlock and the Lanius quickly collect it and start melting it down. They are grateful for your assistance and send over a ship augmentation.''
#*#** You receive an <span style="color:limegreen">augmentation</span>.
#*# Give them 6 missiles. &nbsp;[ {{Transaction|6|subtract_missiles}} ]
#*#* ''You release the material out of the airlock and the Lanius quickly collect it and start melting it down. They are grateful for your assistance and send over a ship augmentation.''
#*#** You receive an <span style="color:limegreen">augmentation</span>.
#*# Give them 6 drone parts. &nbsp;[ {{Transaction|6|subtract_drones}} ]
#*#* ''You release the material out of the airlock and the Lanius quickly collect it and start melting it down. They are grateful for your assistance and send over a ship augmentation.''
#*#** You receive an <span style="color:limegreen">augmentation</span>.
#*# Decline.
#*#* Nothing happens.
# {{Blue Option|Hull Repair Drone|Send a drone to help.|shortreq=Hull Repair Drone}}
#* ''As soon as the drone gets close, a Lanius in a type of spacewalk maneuvering unit grabs it and immediately starts breaking it down for metal. You prepare for a fight but they appear quite grateful for the act. They start to use the metal to repair key portions of their ship. From what you can understand from the translator it appears one of their crew wishes to join you.''
#** You receive a <span style="color:limegreen">Lanius crewmember</span>.

==Notes==
This event is called "LANIUS_BEACON_EATER" in the datafiles.
===Reference notes===
<references/>
[[Category:Advanced Edition Content Events]]
[[Category:Fights with Default Rewards (Lanius)]]
[[Category:Augmentation reward opportunity]]
[[Category:Crew reward opportunity]]
[[Category:Trading Events]]
[[Category:Scrap loss risk]]
