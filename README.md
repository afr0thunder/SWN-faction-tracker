# STARS WITHOUT NUMBER - Sector and Faction Tracker

"Stars Without Number" is a science-themed space RPG set in the future history of the human race designed by Kevin Crawford. 

You can find more information at: https://www.swnrpg.com/

## Purpose
The purpose of this project is twofold. Firstly, I am building my programming skillset, and this will be my first major software project. I want to develop a useful tool that will expand by abilities and give me a solid project to add to my portfolio. Second, due to the popularity of the faction system used in SWN, I am building a visual tracker that can both generate a random sector (including all stars, planets, and other features) and random factions to fill that sector, plus the ability to save and load this information. Future features will include editing and manually creating sector and faction elements, faction turn simulation, multiple sector generation/tracking, and incorporation of additional SWN generation resources (such as lifeforms, starships, etc.).

## Current Build
I am early in the process, but the interface displays two screens: a grid screen showing the sector on the left and a summary screen with a toolbar on the right. The grid screen generates the sector and can generate objects in each grid space; currently, it generates a circle representing the local solar system in each "occupied" space. More visual information will be rendered once more information is generated for each system. The grid can be navigated using the keyboard arrow keys or the mouse.

The right-hand screen consists of a series of tabs that display detailed information about stars, planets, factions, etc. The current build only displays the selected grid space coordinates. A toolbar at the bottom is where a random sector can be generated and files saved and loaded. Only the system generator and exit button have functionality here.

## Next Steps
The next steps:
* add save and load capabilities
* display information in the tab window
* editing capability in the tab window for each element
* scrolling for large sets of information that extend past the interface.
