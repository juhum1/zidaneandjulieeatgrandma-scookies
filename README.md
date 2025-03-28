# zidaneandjulieeatgrandma-scookies
# Tower Defense Simulator

## Who are you working with? (you may work in teams of up to 2)
Zidane Karim and Julie Hum

## What are the exact requirements for your project? e.g. What is the input and the output of the entire project? If it’s a game, what does the game do?
The game is a tower defense simulator. In multiples waves, "enemies" will come down from the top of the terminal and the player will set "upgrades"/defenses each round/wave, in between spawns of enemies. 


Input:

* Player actions: placing towers, upgrading them, and starting waves.

Output:

* Terminal-based visual representation of the game.

* Display of player stats (health, money, wave).

## Be very specific as to what you want to build for your final project.
A terminal-based game where the player defends against multiple waves of incoming enemies by strategically placing towers. The goal is to prevent enemies from reaching the bottom of the terminal. As they do, player health decreases and the player loses if they get to 0 health, or wins if they reach a certain wave. 

Towers have different stats, and as the game goes on enemies will spawn faster and faster.

## How will your project will use C/Python?
We are going to try to incorporate the C library `ncurses` to implement terminal-based graphics. The bulk of the logic will come from collision detection and killing enemies with towers. The larger issue in this is the display, and implementing smooth displays of gameplay.

## How will your project will use C/Python structs/classes along with its features?
We would use structs to define towers and enemies. We would have to dynamically allocate memory when adding new enemies and towers to the map, which should also be stored in one large struct. 

## What other other technologies/languages, if any, are you using as part of the project? (e.g. android studio, CSS/javascript for UIs, openGL for graphics, etc.)
We could implement an external library (SLD2) to play music during the game. 
