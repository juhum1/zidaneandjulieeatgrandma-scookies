## Compilation Steps
python3 game.py

## Sources
https://github.com/smlbiobot/cr-assets-png/blob/master/assets/sc/building_tower_tex.png

# Proposal
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
Pygame has built in music playing we can use

# Game Instructions

## Objective

The game is very tower-defense esque, running until the player runs out of health. The player places towers down with currency they gain
from killing enemies. Each tower has its own health

## Mechanics
To start the game, press Start😀! Then, with an initial $500, place towers by clicking them and then clicking the tile you wish to place them on. You cannot fill a tile with an existing tower or current enemy. In order to get past this, use the remove tool to click on a tower and remove it. 
You will get some percentage of currency back (not the entire amount).

Each tower has its own health and can be destroyed by enemies.
Enemies spawn in waves, making their way towards the bottom. If they reach it, you lose health.

## Gameplay

Each tower and enemy has its own unique stats. Here are them all listed

| Name             | Health | Damage | Range | Attack Speed | Price | Special |
|------------------|--------|--------|--------|----------------|--------|---------|
| **Classic**       | 150    | 40     | 2      | 1 attack/sec   | $100   |  starter tower |
| **Fast**          | 100    | 40     | 2      | 3 attacks/sec  | $150   | High fire rate  |
| **Heavy**         | 300    | 100    | 3      | 0.5 attacks/sec| $150   | Tanky and hard-hitting |
| **Princess**      | 75     | 300    | 6      | 0.2 attacks/sec| $250   | High range and damge |
| **Slowing**       | 150    | 100    | 3      | 0.5 attacks/sec| $200   | Intended for slow effects|
| **Bomb**          | 150    | 75     | 2      | 0.8 attacks/sec| $200   | Hits 3 enemies in a row|

| Name               | Health | Damage | Attack Range | Attack Speed | Currency | Special |
|--------------------|--------|--------|----------------|----------------|----------|---------|
| **Goblin**          | 80     | 40     |  1              | 1              | $10       | Quick and basic |
| **Skeleton**        | 20     | 50     |  1              | 1              | $5        | Very weak, often summoned |
| **Witch**           | 150    | 70     |  3              | 1              | $10       | Spawns a Skeleton on death |
| **Bat**             | 10     | 50     |  1              | 0.5            | $2        | Fast attack speed|
| **Bandit**          | 160    | 30     |  1              | 1              | $8        | Teleports after taking damage |
| **Necromancer**     | 100    | 20     |  4              | 1.5            | $15       | Spawns **2 Skeletons** on death  |
| **Slime**           | 40     | 25     |  1              | 1              | $3        | Splits into **2 Slimelets** on death |
| **Slimelet**        | 10     | 10     |  1              | 1              | $1        | Very weak, often summoned |
| **Fire Imp**        | 50     | 35     | 2              | 0.8            | $12       | Destroys tower **in front** on death |