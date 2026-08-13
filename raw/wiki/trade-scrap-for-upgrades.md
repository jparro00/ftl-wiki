<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Trade scrap for upgrades
URL: https://ftl.fandom.com/wiki/Trade_scrap_for_upgrades
Categories: Random_Events, Unique_Events, Trading_Events
Revision: 73902
Retrieved: 2026-08-09

---
{{Locations|Civilian Sector|Engi Controlled Sector|Engi Homeworlds|Mantis Controlled Sector|Mantis Homeworlds|Pirate Controlled Sector|Rebel Controlled Sector|Rebel Stronghold|Rock Controlled Sector|Rock Homeworlds|Slug Controlled Nebula|Slug Home Nebula|Uncharted Nebula|alsooccur=exit|LRSmap=noship|unique=true}}


The event intro text for this varies, and can be any of the following:
*''You pick up an automated message from a nearby space station. There appears to be a local shipwright that can perform emergency work on military ships.''
*''There are a number of privately owned ship construction platforms in the area. You find one that has a slot open for some immediate work.''
*''You receive a message from a small refugee convoy, "Hail. We'd like to help you on your mission but don't have much to offer. If you have extra metal perhaps we could work on your ship?"''
*''You are immediately hailed by a mobile docking platform upon arrival, "Welcome to Uncle Joe's Fix-it Shop! Need a tune-up? We got you covered!"''
*#Inquire about their specialty.
*#*''They offer to upgrade your Oxygen system in exchange for some scrap.''
*#*# Decline.
*#*#* ''You thank them but prepare to move on.''
*#*#** Nothing happens.
*#*# Agree to the exchange. &nbsp;<span style="color:grey;">[ the actual trade offer is shown prior to making the choice ]</span>
*#*#* ''You let their team on board and after a short time they finish their work.''
*#*#** ([[Oxygen]] level 1) You lose {{Transaction|15-20|subtract_scrap}} and your '''Oxygen''' system is upgraded to level '''2'''.
*#*#** ([[Oxygen]] level 2) You lose {{Transaction|25-40|subtract_scrap}} and your '''Oxygen''' system is upgraded to level '''3'''.
*#*''They offer to upgrade your Piloting subsystem in exchange for some scrap.''
*#*# Decline.
*#*#* ''You thank them but prepare to move on.''
*#*#** Nothing happens.
*#*# Agree to the exchange. &nbsp;<span style="color:grey;">[ the actual trade offer is shown prior to making the choice ]</span>
*#*#* ''You let their team on board and after a short time they finish their work.''
*#*#** ([[Piloting]] level 1) You lose {{Transaction|8-15|subtract_scrap}} and your '''Piloting''' is upgraded to level '''2'''.
*#*#** ([[Piloting]] level 2) You lose {{Transaction|25-40|subtract_scrap}} and your '''Piloting''' is upgraded to level '''3'''.
*#*''They offer to upgrade your Door subsystem in exchange for some scrap.''
*#*# Decline.
*#*#* ''You thank them but prepare to move on.''
*#*#** Nothing happens.
*#*# Agree to the exchange. &nbsp;<span style="color:grey;">[ the actual trade offer is shown prior to making the choice ]</span>
*#*#* ''You let their team on board and after a short time they finish their work.''
*#*#** ([[Door System]] level 1) You lose {{Transaction|8-15|subtract_scrap}} and your '''Door System''' is upgraded to level '''2'''.
*#*#** ([[Door System]] level 2) You lose {{Transaction|25-40|subtract_scrap}} and your '''Door System''' is upgraded to level '''3'''.
*#*''They offer to upgrade your Sensors subsystem in exchange for some scrap.''
*#*# Decline.
*#*#* ''You thank them but prepare to move on.''
*#*#** Nothing happens.
*#*# Agree to the exchange. &nbsp;<span style="color:grey;">[ the actual trade offer is shown prior to making the choice ]</span>
*#*#* ''You let their team on board and after a short time they finish their work.''
*#*#** ([[Sensors]] level 1) You lose {{Transaction|10-20|subtract_scrap}} and your '''Sensors''' are upgraded to level '''2'''.
*#*#** ([[Sensors]] level 2) You lose {{Transaction|35-45|subtract_scrap}} and your '''Sensors''' are upgraded to level '''3'''.
*#*''They offer to upgrade your reactor in exchange for some scrap.''
*#*# Agree to the exchange. &nbsp;<span style="color:grey;">[ the actual trade offer is shown prior to making the choice ]</span>
*#*#* ''You let their team on board and after a short time they finish their work.''
*#*#** You lose {{Transaction|15-25|subtract_scrap}} and your ship <span style="color:limegreen">reactor</span> is upgraded.
*#*# Decline.
*#*#* ''You thank them but prepare to move on.''
*#*#** Nothing happens.

==Trivia==
This event is called "TRADER_UPGRADES" in the datafiles.
*It is impossible to upgrade:
**a (sub)system beyond its maximum level
**a subsystem that is not currently installed (e.g. Sensors, Door System)
**the reactor beyond 25 power bars
*In the files, the "agree" choices come before the "decline" choices. However, outcomes which upgrade (sub)systems use "max_group" to select the right level of (sub)system, and since choices with max_group are moved below choices without it, it causes those "agree" choices to come after the "decline" choices. This is why the choice order for the reactor outcome is different from the rest. This is also why blue options tend to be at the bottom of lists.
[[Category:Trading Events]]
[[Category:System Upgrade chance]]
[[Category:Reactor Upgrade chance]]
