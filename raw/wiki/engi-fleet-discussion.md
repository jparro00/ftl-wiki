<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Engi fleet discussion
URL: https://ftl.fandom.com/wiki/Engi_fleet_discussion
Categories: Random_Events, Unique_Events, Ship_Unlocking_Events
Revision: 74722
Retrieved: 2026-08-09

---
{{Locations|Engi Homeworlds|LRSmap=noship|unique=true}}


This is the [[The_Stealth_Cruiser#Layout_A|Stealth Cruiser]] ship unlocking event. <span style="color:grey">(the ship can also be unlocked by winning the game with the Rock Cruiser)</span>
----
__TOC__

''You arrive near a small fleet of civilian Engi ships. A simple decryption and translation of their comm frequency tells you that they are having a frantic discussion about something obviously troubling them.''
# Message them and ask if you can help.
#* ''Slightly shocked at your question, their leader quickly responds, "Declined offer with apologetic gratitude. Topic of discussion private matter, no concern of Federation."''
#** Nothing happens.
# Ignore it and move on.
#* ''You can't help but wonder what they were discussing as you prepare to jump.''
#** Nothing happens.
# {{Blue Option|Engi Crew|Have your Engi crewmember contact them.}}
#* ''Your crew member syncs with the comm unit to communicate with them directly. You offer your help and a summary of the ship's mission. They respond, "Our goals have analogous elements. However, not all available for disclosure, discretion necessary."''
#** Offer your help.
#*** ''"Secret technologies stolen by Mantis. Implicit connection to Rebels. Implicit. Tracked Mantis to hidden Rebel base, uploading coordinates."''
#**** A [[Engi Fleet Discussion#First Quest Marker (Real)|'''quest marker''']] is added to your map.
#***** ''"However, tracked second ship to different base. Would calculate probability but data insufficient. Cannot risk obvious Rebel-Engi conflict. Also, need time to acquire military ships. Assist in finding technology?"''
#****** A [[Engi Fleet Discussion#Second Quest Marker (Fake)|'''second quest marker''']] is added to your map.
#******* Agree.


==First Quest Marker (Real)==
:{{Long-Ranged Scanners info|shipdetected=ship}}
''You arrive at one of the Rebel bases that the Engi told you about. It appears abandoned except for one scout ship. Perhaps you could extract information from them.''
* Fight the [[Enemy Ships#Rebel_Ships|Rebel Ship]]. <ref name="Enemy ship (REBEL_ENGI_UNLOCK_2REAL)">{{SurrenderEscape(alt)|escape+surrender*|REBEL_ENGI_UNLOCK_2REAL|events_ships.xml|immediately starts to escape (40 seconds timer); surrenders at {{tooltip|50%|actual in-game value may be 5 hull + additional hull adjusted by sector progression}} hull}}</ref>
** {{Winning|escape=true|As soon as they see you they power up their engines to jump away. Stop them!}}
*** {{Winning|gotaway=true|With the ship gone, you search through the abandoned base for any signs of their destination but find none.}}
**** Nothing happens. [unlock quest is failed]
** {{Winning|surrender=true|"Stop!  This isn't worth dying for..."}}
*** Demand information on the stolen technology.
****''"Of course, that's why you're here. Yes, they passed by here but I had nothing to do with it, I don't know what they were carrying. I'll transmit coordinates. Now just let us go..."''
***** A [[#Final Quest Marker|'''final quest marker''']] is added to your map.
****** Let them go.
******* You prepare an FTL message containing the coordinates to send to the Engies and get ready to jump.
******** Nothing else happens.
** {{Winning|deadCrew=true|Once their crew is dead you scan the log for information regarding the envoy. You're in luck! It seems ships matching the thieves' description passed through here not too long ago. You strip the ship and prepare to pursue them.}}
*** You receive high [[Rewards#Standard|scrap with resources]] and a [[#Final Quest Marker|'''final quest marker''']] is added to your map.


==Second Quest Marker (Fake)==
:{{Long-Ranged Scanners info|shipdetected=ship}}
''You arrive at one of the Rebel bases that the Engi told you about. It appears abandoned except for one scout ship. Perhaps you could extract information from them.''
* Fight the [[Enemy Ships#Rebel_Ships|Rebel Ship]]. <ref name="Enemy ship (REBEL_ENGI_UNLOCK_2FAKE)">{{SurrenderEscape(alt)|escape+surrender*|REBEL_ENGI_UNLOCK_2FAKE|events_ships.xml|immediately starts to escape (40 seconds timer); surrenders at {{tooltip|40%|actual in-game value may be 4 hull + additional hull adjusted by sector progression}} hull}}</ref>
** {{Winning|escape=true|As soon as they see you, they power up their engines to jump away.  Stop them!}}
*** {{Winning|gotaway=true|With the ship gone you search through the abandoned base for any signs of their destination but find none.}}
**** Nothing happens.
** {{Winning|surrender=true|"Stop! I don't want to die here."}}
*** Demand information on the stolen technology.
**** ''"Ah, so that's what you're after. Too bad, you followed the wrong ship. The envoy that passed through here was a fake, to trick fools like you. Now let us go!"''
****# Let them go.
****#* The ship turns neutral.
****# Ignore him and attack.
****#* ''"No, wait..." You cut the transmission and continue the assault.''
****#** Continue the fight.
** {{Winning|destroyed=true|You take what you can from the debris.}}<br />{{Winning|deadCrew=true|A quick search of their communication logs shows that the tech you were searching for never passed through this base... It must have been a decoy! You strip what you can and prepare to jump.}}
*** You receive medium [[Rewards#Standard|scrap with resources]].


==Final Quest Marker==
:{{Long-Ranged Scanners info|shipdetected=ship}}
''You have finally caught up with the ships you've been hunting. A hangar-sized cargo ship is being escorted by a number of Mantis ships. As you reconsider the assault, a squadron of Engi ships with pirate emblems jump in and assist you. You prepare to fight the Mantis but scans indicate they are manned by Rebels!''
* Fight the [[Enemy Ships#Mantis_Ships|Mantis Ship]] controlled by Humans. <ref name="Enemy ship (MANTIS_ENGI_UNLOCK_3)">{{SurrenderEscape(alt)|no|MANTIS_ENGI_UNLOCK_3|events_ships.xml}}</ref>
** {{Winning|destroyed=true}}
*** [[#Victory|'''Victory''']].
** {{Winning|deadCrew=true|You strip what you can and contact the Engi ships.}}
*** You receive medium [[Rewards#Standard|scrap with resources]].
**** [[#Victory|'''Victory''']].

===<h2><span style=font-size:smaller;>Victory</span></h2>===
''The Engi emerge victorious from their battles with only minor losses. They message you, "Project X-ME56 commissioned by Federation military research division. Advanced stealth cruiser. Project finished during rebellion. Unable to reconnect with Federation military command."''
* Ask about the Mantis ships.
** ''"Likely ploy by Rebels to avoid breaking non-aggression pact with Engi. 97.56 percent likely. Your mission to assist last Federation fleet, correct? Coordinates?"''
*** Transmit coordinates of Federation command.
**** ''"Satisfactory. Delivery of tech will assist in Federation cause. Gratitude alone insufficient. Commencing ship repair and compensation." Their crews deliver a weapon for installation but you're more pleased to hear that the Federation will have an improved arsenal.''
***** You unlock the [[Stealth Cruiser]]; you receive <span style="color:limegreen">Titanium System Casing</span> [[Augmentations#Titanium_System_Casing|augmentation]], high [[Rewards#Standard|scrap with resources]] and your ship receives <span style="color:limegreen">20 repairs</span>.<ref>Bugged: if the "scrap with resources" component gives an augmentation, it will overwrite the guaranteed augmentation.</ref>

==Notes==
This event is called "ENGI_UNLOCK_1" in the datafiles.
* Both the fake and the real quest marker beacons can be visited in no particular order.
* The [[#First Quest Marker (Real)|real quest]] can be distinguished by the '''''missing'' comma''' in the introductory text preceding the fight ("As soon as they see you").
** If the intro text was skipped and the ship escaped, it is possible to determine if the [[#First Quest Marker (Real)|real quest]] was failed: it '''''has''''' a '''comma''' in the "With the ship gone" text.
===Reference notes===
<references/>
[[Category:Ship Unlocking Events]]
[[Category:Events with Quest Markers]]
[[Category:Ship escape Events]]
[[Category:Ship surrender Events]]
[[Category:Augmentation reward opportunity]]
[[Category:Hull Repair opportunity]]
