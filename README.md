## Compilation Steps
python3 game.py

## Tower Defense Simulator

### Who are you working with? (you may work in teams of up to 2)
Zidane Karim and Julie Hum

### What are the exact requirements for your project? e.g. What is the input and the output of the entire project? If it’s a game, what does the game do?
The game is a tower defense simulator. In multiples waves, "enemies" will come down from the top of the terminal and the player will set "upgrades"/defenses each round/wave, in between spawns of enemies. 


Input:

* Player actions: placing towers, upgrading them, and starting waves.

Output:

* GUI-based visual representation of the game.

* Display of player stats (health, money, wave).

### Be very specific as to what you want to build for your final project.
A GUI-based game where the player defends against multiple waves of incoming enemies by strategically placing towers. The goal is to prevent enemies from reaching the bottom of the terminal. As they do, player health decreases and the player loses if they get to 0 health, or wins if they reach a certain wave. 

Towers have different stats, and as the game goes on enemies will spawn faster and faster.

### How will your project will use C/Python?
We will use Python's Pygame library to create a GUI based game, using point and click features.

### How will your project will use C/Python structs/classes along with its features?
There will be abstract base classes for the Enemies and Towers and we will design inherited classes to represent different enemies. We could also implement sprites to represent each entity. 

### What other other technologies/languages, if any, are you using as part of the project? (e.g. android studio, CSS/javascript for UIs, openGL for graphics, etc.)
Pygame has buiilt in music playing we can use
