Final Report for COMP 388/488: https://docs.google.com/document/d/1IHxrWJRM8Q-Ep7kYrTry-WGRYwR7dCSz5FTPKEcIEMM/edit?usp=sharing

# 75 MM

A Game by Anthony Soto and Joe Conroy

# Codename: Tristram
COMP 388 Project

Language: Python and Pygame

**Game Idea:**
===============================

Roguelike, Dungeon Crawl, Action-Adventure

Wartime theme. Use of tanks, motorcycles, jeeps, half-tracks, etc., as player and enemy models.

Player traverses a series of gridded fields within a level. Fields will contain enemies that are randomly placed inside the field. Object is to advance through set of levels by defeating enemies (**temp idea - progressing through a WWII western campaign, using historic towns/battles as levels**).

**Inspiration from Games:**
===============================

**Binding of Isaac** - Roguelike/Dungeon Crawler gameplay with a focus on defeating smaller enemies by room, leading up to a larger boss to defeat. Includes multiple array of items that improve or hurt the stats of the player.

Example of gameplay: https://www.youtube.com/watch?v=oU8EEHy9vR0

**Nuclear Throne** - Roguelike/Shooter gameplay with fighting smaller enemies to progress levels.

Example of gameplay: https://www.youtube.com/watch?v=Yg7PdUlT4pw

**Real-World Inspiration**
===============================

European Theater of War in World War II

**Goals**
===============================

Opening context each time the game is booted, referring to the wartime period as well as the player's beginning location.

Incoming as an Allied Tank, the player is to defeat Axis forces (tanks/vehicles) as they progress. From Normandy to Berlin initially.

The gameplay is the main focus from a developer perspective. The historical context is to add to the setting, meaning the historical accuracy of each level will not be exact.

**Development Goals**
===============================
1.) Create smooth movement and functionality of both the player and computer-controlled enemies.
This involves:

- Creating the grid on which the characters will move, involving some sort of character collision or projectile collision aspect to indicate damage taken.

- Making the player controlled character able to look/face and fire projectiles in all cardinal directions.

- Designing a very basic stat system for the player that takes into account fire rate, movement speed, and projectile damage. Player stats will be changeable, while enemy stats can vary but will be final for each enemy.

- Creating a difference of movement speed between certain enemy models (e.g. tanks move slower than truck or bike vehicles). This means also outlining the design and function of different types of enemies (as of now, 3 different types in mind).

2.) Design a campaign that will be the main playable aspect of our game.
This involves:

- Determining how many levels and/or enemies the player will need to progress through in order to advance further. Also, including lose conditions (Game over screen? Level reset or campaign reset? How many lives?).

- Outlining the design of each level/section (location of enemies, player start point, blocking terrain, etc.)

- Figuring out the desired game length we would like to create.

3.) Creating an item system that can buff or debuff player stats.

- Designing the basic look of the items, making them pop out for the player when compared to the rest of the level.

- How will this affect the player model? Perhaps have different models for the player that change when specific items are picked up or when stats are boosted/decreased to a certain level.

- Implementing a system of randomness across which items appear where, giving a new way of playing each time the game is played.

These goals, if fulfilled correctly, will not be a main focus to the player as they will be focused more on the game objective and not the expected smoothness, functionality, and design of it.

**Selling Points**
===============================

- Simplicity of the story and gameplay is an alluring aspect of a game, making it easy to pick up and play without any intense levels of learning or understanding required.

- The stylistic design being military-themed and historically-based. War themed games have been popular over the last decade, and there are no rogue-like WWII games flooding the market.

- Much like The Binding of Isaac, the replayability of the game due to its randomness from level to level is a draw to players (rather than being a one playthrough type of game).

- The difficulty of enemies will present a challenge to the players to use their movements and aiming precisely to defeat them.

- The game's graphical demand is not high, making it easily playable and well optimized.
