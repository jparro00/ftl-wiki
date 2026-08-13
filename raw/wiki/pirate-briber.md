<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Pirate briber
URL: https://ftl.fandom.com/wiki/Pirate_briber
Categories: Random_Events, Unique_Events, Filler_Events
Revision: 73759
Retrieved: 2026-08-09

---
{{Locations|Abandoned Sector|Civilian Sector|Engi Controlled Sector|Engi Homeworlds|Pirate Controlled Sector|Slug Controlled Nebula|Slug Home Nebula|Uncharted Nebula|Zoltan Controlled Sector|Zoltan Homeworlds|alsooccur=exitandfiller|LRSmap=ship|unique=true}}


The intro text for this event varies, and could be any of the following:
* ''You come across a pirate in hot pursuit of an unidentified ship. You quickly receive a transmission from the pirate: "Stay out of this fight and we'll make it worth your while."''
* ''An unidentified ship is badly damaged and still being assaulted by a space pirate. The victim begins a distress message until the pirate cuts in and offers to split the bounty if you sit tight.''
* ''A missile shoots across your bow when the jump completes. Your scans quickly reveal a ship with pirate markings pursuing an unknown vessel. The pirate hails you: "Damn it, we weren't expecting company. Stay out of this and you could profit."''

----

# Accept their bribe.
#* ''"Good choice, son. We've both come out of this richer."''
#** You receive low [[Rewards#Standard|scrap with resources]].
# Try to be a hero. Attack the pirate.
#* ''The pirate ship stops its pursuit and locks weapons onto your ship.''
#** Fight the [[Enemy Ships|Pirate ship]].
#*** {{Winning|surrender=true|"Fine! Our previous offer was not generous enough, let's improve it."}} &nbsp;<!-- ship name="PIRATE_BRIBER" (events_ships.xml) --><span style="color:grey">(has 70% chance to surrender at 30-40% hull)</span>
#***# Accept the more generous bribe and leave.
#***#* You receive {{Tooltip|high|fuel: 3-6 ; missiles: 4-8 ; drone parts: 1-2}} [[Rewards#Stuff|resources with some scrap]].
#***# Reject the offer and continue your assault.
#***#* Continue the fight.
#*** {{Winning|escape=true|You've proved a sufficient match for the pirates; they are powering up their FTL and trying to get away.}} &nbsp;<!-- ship name="PIRATE_BRIBER" (events_ships.xml) --><span style="color:grey">(has 60% chance to try to escape at 30-40% hull)</span>
#**** {{Winning|gotaway=true|The pirate has abandoned pursuit of both you and its former prey. You attempt to hail the damaged ship.}}
#***** [[#The pirate is gone|'''The pirate is gone''']].
#*** {{Winning|destroyed=true|The pirate explodes, leaving behind a substantial collection of useful scrap material. You go to examine the ship you just saved.}}
#**** You receive a random amount of [[Rewards#Scrap_only|scrap]].
#***** [[#The pirate is gone|'''The pirate is gone''']].
#*** {{Winning|deadCrew=true|The pirates are all dead, leaving the ship dead in space. You scrounge what you can from their ship before contacting its former prey.}}
#**** You receive medium [[Rewards#Standard|scrap with resources]].
#***** [[#The pirate is gone|'''The pirate is gone''']].

==The pirate is gone==
* ''"Thank you for the aid! I'm an arms dealer that usually only works with rebels, but considering the circumstances I'll make an exception."''
** A <span style="color:limegreen">store</span> opens.
* ''"Thank the heavens you showed up! We don't have much to offer as a reward, but our engineer should be proficient enough to patch your ship up a bit after that nasty fight."''
** Your ship receives <span style="color:limegreen">15 repairs</span>.
* ''Upon closer inspection, you realize the ship under attack was a Rebel scout! It's too damaged to put up much of a fight.''
*# Destroy the ship and salvage it
*#* ''You strip the ship of anything useful and leave its crew to hope help arrives.''
*#** You receive low [[Rewards#Standard|scrap with resources]].
*# Use the leverage you gained by saving their lives to convince them to delay the pursuing fleet.
*#* ''Hopefully that will buy you more time to get to the next sector.''
*#** Rebel Fleet is <span style="color:limegreen">delayed</span> for <span style="color:limegreen">1</span> turn. &nbsp;[no effect in The Last Stand sector]
* ''You were too late. A hull breach deprived the crew of oxygen during your fight with the pirate. You salvage what you can.''
** You receive medium [[Rewards#Scrap_only|scrap]].
* ''The pirate's victim quickly jumps away before you have a chance to speak to them.''
** Nothing happens.

==Trivia==
This event is called "PIRATE_BRIBER" in the datafiles.
[[Category:Store Opening chance]]
[[Category:Hull Repair chance]]
[[Category:Rebel Fleet delay chance]]
[[Category:Events with Stuff rewards]]
[[Category:Pirate ship fights]]
