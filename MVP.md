# **Score Keeper**

## A brief introduction
Trap shooting is one of the most popular shotgun based shooting sports. Originally based around practicing shooting pigeons people quickly moved on to clay targets. Each round of the game consists of 25 targets, shot in sets of 5 targets, from 5 points 16 yards from the 'house' (generally a cement enclosure with an automatic target thrower inside). The maximum score is 25 out of 25 targets and as people progress they gravitate towards a cumulative score over 4 rounds. There are other variations including doubles (two targets every time, for a total of 50) and Handicap, which is shot up to 27 yards from the house.

### Product Overview
The core focus of this app is to keep track of scores and information about trap shooting. It will allow a player to easily log scores and relavent details (eg. shells, weather, location) to look for trends that show over time. 

### Specific Functionality

**Main Page:**
  * index of players
  * Longest streak
  * last score submitted
  * advanced goals:
    * map with nearby locations
    * user login
    * tailor front page data to the logged in user

**Player page:**
  * Time-sorted list of rounds
  * Place to add shotgun/shell/location data to your profile
  * Basic statistics:
    * hit %
    * average score
    * best score
    * longest streak
    * total shots

**Round Page:**
  * 5x5 grid of target pictures, clickable to set hit/miss, hit by default
  * Ability to just input a score using integers EG. 23 or 4, 5, 3, 5, 5 without specific orders (would take away the ability to run some statistics vs the stats, but allow greater user flexibility)
  * Drop downs/menus/etc for relavent details
   * Shells
   * Gun
   * Location
   * Weather
   * External conditions/excuses (wind, lighting, busy day, etc)
   * save/autosave functionality?

**Group page:**
 * Ability to score 5 rounds simultaneously (the max amount of people in a squad)

## Data Model
The app will need to store a handful of very spefic things:
 * The 'player'/user
   * Name
   * Location
   * Shotgun make/model
 * details about a specific round:
   * date/time
   * location
   * a score, represented by an integer or 25 booleans
   * type of shells used (TBD how specific this will get)
   * shotgun used

## Technical Components
In order to keep the front end simple, fast, and easy the pages will all be done in JS using basic HTML elements and images. For example the score input will take either a 5x5 grid of clay targets that are by default set to 'hit' (Eg an image like: [broken clay.jpg](http://mickleyhall.com/wp-content/uploads/2015/05/clay-pigeon-shooting.jpg)).

The data will be passed back to the python 'back-end' via json to be massaged into various metrics that can then be presented on the main page or player page. 

One of the major moving parts in this is having unique ID's for players to tie rounds to. The ideal way to accomplish this would be an account based system. Per David's suggestions earlier in the course this may represent a lot of work and take away a lot of time from the core functionalities of the program. However, in an ideal world I'd like to tie this to google accounts using something like [Firebase](https://firebase.google.com/docs/auth/). The alternative is just using peoples full names as the ID. 


## Schedule

1. Write out all basic classes and data transformations in python -- Fairly straight forward.
2. Write out the basic outline of the HTML/CSS/JS for the site and get the layout roughed up to find any challenges I haven't considered.
3. Write the JS for to take in scores communicate with the 'backend' (One of the harder parts, may become more clear when we've dealt with django)
4. Set up a structure for the database and the unique ID's to tie to users.


## Further Work

*  potentially an account system (EG. google logins)
*  a page/section of the 'site' made for tournaments/events.
  For example Portland Gun Club hosts day long events with things like special targets, classes (beginner, intermediate, expert). There would be a database of entrants, a page to display the scores (seperated by class), flags for special targets, etc. 
* the ability to store pictures in the 'player'/user section. The person, guns, shotgun shell boxes, etc.
* The ability to store custom data about 'handloads', what poweder, wad, shot, hulls, etc.
* a page to compare a player to player(s) or statistics based on the 'nouns'
