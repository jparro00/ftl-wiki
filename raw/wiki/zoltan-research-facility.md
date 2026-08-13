<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Zoltan research facility
URL: https://ftl.fandom.com/wiki/Zoltan_research_facility
Categories: Random_Events, Ship_Unlocking_Events
Revision: 74726
Retrieved: 2026-08-09

---
{{Locations|Engi Controlled Sector|Engi Homeworlds|Zoltan Controlled Sector|Zoltan Homeworlds|LRSmap=noship|unique=false}}


This event is the '''2nd''' step in the process of unlocking the [[The Crystal Cruiser|Crystal Cruiser]] and the [[Ancestry]] achievement while using the [[The Rock Cruiser|Rock Cruiser]].
----


''You arrive at a Zoltan research facility. They say they are researching genetic distortion due to stasis sleep and prolonged FTL travel. They ask if your crew has the time to undergo a few scans.''
# Participate in their study.
#* {{DuplicateEvent|2}} ''Your crew calmly lines up for the Zoltans to take their readings. After a short time, the process is done. They contact you, "Thank you for your participation in our study. Please accept these small cakes made from stiff dough as well as some scrap."''
#** You receive low [[Rewards#Scrap_only|scrap]].
#* ''As soon as you dock, pirates burst on board and a hostile ship appears on the radar. You hear the Zoltans yell in the distance, "We're being held hostage!"''
#**  <span style="color:red">2 boarders</span> beam aboard your ship, and you fight a [[Enemy Ships|Pirate ship]].
#*** {{Winning|destroyed=true|You take out the ship and contact the research station.}}
#**** You receive medium [[Rewards#Standard|scrap with resources]].
#***** ''"Thank you for rescuing us! They held us hostage to ambush unsuspecting passersby. Please, take this."''
#****** You receive a <span style="color:limegreen">drone schematic</span> with {{Tooltip|low|fuel: 1-3 ; missiles: 1-2 ; drone parts: 1}} [[Rewards#Stuff|resources and scrap]].<ref name=":0">The "resources and scrap" component will never give a bonus weapon, drone schematic or augmentation, due to its interaction with a guaranteed weapon/drone schematic reward.
</ref>
#*** {{Winning|deadCrew=true|You disable the ship and contact the research station.}}
#**** You receive high [[Rewards#Standard|scrap with resources]].
#***** ''"Thank you for rescuing us! They held us hostage to ambush unsuspecting passersby. Please, take this."''
#****** You receive a <span style="color:limegreen">drone schematic</span> with {{Tooltip|low|fuel: 1-3 ; missiles: 1-2 ; drone parts: 1}} [[Rewards#Stuff|resources and scrap]].<ref name=":0" />
# Decline.
#* ''"Alright. Fly safe." You prepare to leave.''
#** Nothing happens.
# {{Blue Option|Advanced Medbay|Give them your medical records.|level=3|shortreq=Medbay}}
#* ''"Thank you! We didn't expect to receive such a significant amount of data regarding your crew's health during FTL travel. Please, accept this for your trouble."''
#** You receive a <span style="color:limegreen">drone schematic</span> with {{Tooltip|low|fuel: 1-3 ; missiles: 1-2 ; drone parts: 1}} [[Rewards#Stuff|resources and scrap]].<ref name=":0" />
# {{Blue Option|Damaged Stasis Pod|Ask if they can fix this.}}
#* ''"Interesting. I've never seen a cryogenic system like this. It appears to still be functioning..." They hook it up to their system and run a number of tests on it.''
#** ''"Amazing! It has the ability to reconstruct the body if it was damaged during transit. Watch." They reactivate the pod and you watch as the hunks of crystal inside reform to build a humanoid structure. The pod slides open and the re-formed alien steps out.''
#*** ''It speaks slowly, "Greetings. I appear to be in your debt. My people isolated themselves a long time ago, but perhaps it's time to re-establish a connection. There's a hidden wormhole near the Rock home-worlds. Perhaps you can take me there so I can properly repay you?"''
#**** You receive a <span style="color:limegreen">Crystal crewmember</span> named Ruwen and a [[Ancient Device|quest marker]] will appear in the [[Rock Homeworlds]] (as long as Ruwen stays alive).

==Trivia==
This event is called "ZOLTAN_CREW_STUDY" in the datafiles.
* This event can occur multiple times per game:
** at one beacon per Zoltan sector; <!-- guaranteed for Zoltan sectors by <event name="ZOLTAN_CREW_STUDY" min="1" max="1"/> line in "sector_data.xml" -->
** at one or two beacons per Engi sector. <!-- occurred twice in a regular Engi sector -->
* Any Engi sector potentially allows to [[Dense asteroid field distress call|receive]] and open a [[Augmentations#Damaged_Stasis_Pod|Damaged Stasis Pod]] within the same sector.
* The Pirate ship ("PIRATE_ZOLTAN_CREW_STUDY")  doesn't surrender, nor tries to escape.

=== Reference notes ===
[[Category:Ship_Unlocking_Events]]
[[Category:Events with Quest Markers]]
[[Category:Crew reward opportunity]]
[[Category:Drone Schematics reward opportunity]]
[[Category:Boarding risk]]
[[Category:Events with Stuff rewards]]
