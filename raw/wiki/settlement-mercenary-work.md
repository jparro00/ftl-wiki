<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Settlement mercenary work
URL: https://ftl.fandom.com/wiki/Settlement_mercenary_work
Categories: Random_Events, Unique_Events
Revision: 74665
Retrieved: 2026-08-09

---
{{Locations|Civilian Sector|Engi Controlled Sector|Engi Homeworlds|Pirate Controlled Sector|Rock Controlled Sector|Rock Homeworlds|LRSmap=noship|unique=true}}


''You are immediately contacted by a settlement, "Hello, travelers. Your ship seems to be outfitted for combat...care to take up a bit of mercenary work?"''
#Listen to their offer.
#*''"Some of our friends have taken to piracy in the recent chaos of the war. We'd like you to "convince" them of their poor decision by severely damaging the ship. We'll pay you well as long as you don't kill them all."''
#*#Accept.
#*#*''"Just be sure not to blow them up!" they say nervously as they direct you to a nearby moon. You find the pirate ship docked there. They immediately respond to your appearance with, "Your money or your life!" They must be new to this.''
#*#**Fight a [[Enemy Ships|Pirate ship]].
#*#***{{Winning|surrender=true|They hail your ship saying, "You win! We're not cut out for this!"}} &nbsp;<!-- ship name="SQUAT_PIRATE_MERCENARY" (events_ships.xml) --><span style="color:grey">(surrenders at 30-40% hull)</span>
#*#***#Let them live and then return to the settlement.
#*#***#*''With the pirates dissuaded from their career path, you return to the settlement. "Thank you, they returned to us before you did. I don't think we'll need this anymore."''
#*#***#**You receive a <span style="color:limegreen">weapon</span> with medium <span style="color:#70b8ff">scrap</span>.
#*#***#Forget your promise, they die!
#*#***#*The fight continues.
#*#***{{Winning|destroyed/deadCrew=true|With all of the would-be pirates dead, you think it best not to return to the settlement... You prepare to jump.}}
#*#****You receive low [[Rewards#Standard|scrap with resources]].
#**Decline.
#***''"Fine. I don't know what we'll do about them though..." You prepare to jump away from this sector.''
#****Nothing happens.
#*''"A space dock is under assault from the Rebels. Although the dock is... technically... illegal within their laws, it's very important for our trade. We'll pay you in fuel and scrap if you promise to save them."''
#*#Agree to rescue the store.
#*#*''They transmit the space dock's coordinates.'' 
#*#** A [[#Quest marker|'''quest marker''']] is added to your map.
#*#Decline.
#*#*''They regretfully accept your decision.''
#*#**Nothing happens.
#Decline.
#*Nothing happens.


==Quest marker==
:{{Long-Ranged Scanners info|shipdetected=noship}}

''Once you arrive at the beacon you detect a Rebel scout assaulting a compound on a nearby desolate moon.''
# Engage the Rebel and rescue the space dock.
#* {{Winning|destroyed/deadCrew=true|The outpost hails you, "Thank you! I don't know what we did to anger the Rebels, but they were ready to kill us. I'll show you our goods and patch up your hull."}}
#** You receive medium [[Rewards#Scrap_only|scrap]], your ship receives <span style="color:limegreen">5 repairs</span> and a <span style="color:limegreen">store</span> opens.
# Avoid a fight.
#* ''After a time the ship powers down its weapons and jumps away. No life-signs are detected on the moon.''
#** Nothing happens.

==Trivia==
This event is called "MERCENARY_WORK_START" in the datafiles.
* The "SQUAT_STORE_RESCUE" ship assaulting the space dock doesn't surrender, nor tries to escape.
* The "SQUAT_PIRATE_MERCENARY" ship from the settlement never runs away.
[[Category:Events with Quest Markers]]
[[Category:Hull Repair chance]]
[[Category:Store Opening chance]]
[[Category:Ship surrender Events]]
[[Category:Weapon reward chance]]
[[Category:Pirate ship fights]]
