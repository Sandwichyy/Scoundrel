# Scoundrel (Pygame Implementation)

## Overview

This project is a recreation of the solo dungeon-crawler card game **Scoundrel**, implemented in **Python using Pygame**. The goal of the project was to build a playable digital version of the game while preserving the core mechanics and decision-making of the original tabletop experience.

Scoundrel is a **single-player roguelike card game** where the player explores a dungeon represented by a deck of cards. Each room presents a set of cards that may contain **monsters, weapons, or health potions**, and the player must decide how to survive using limited resources.

Our implementation focuses on recreating the gameplay loop of the original game while providing an interactive graphical interface through Pygame.

---

## Team Members

- **Abdulmateen Shaikh**
- **Samuel Xu**
- **Obadiah Smolenski**
- **Mohammed Sadaf**

---

## How the Game Works

At the start of the game:

- The dungeon deck is created from a standard 52-card deck with **red face cards and red Aces removed**.
- The player begins with **20 health**.
- The dungeon is explored in rooms, each of which consists of a hand of **four cards at a time**.

Depending on their suit, the cards in each room can be one of the following:

### Monsters (♠ Spades, ♣ Clubs)
- Monsters deal damage based on their card value.
- The player may fight them using their current weapon, or hand-to-hand.
- If the weapon is weaker than the monster, the player takes the difference as damage.

### Weapons (♦ Diamonds)
- Weapons allow the player to fight monsters more effectively.
- Equipping a new weapon replaces the old one.

### Health Potions (♥ Hearts)
- Potions restore health based on the card value.

And if things get really dicey, you can always...
### RUN!!!
- Put the current room at the bottom of the dungeon and go to the next room, but NOT SO FAST...
- You are NOT allowed to run away from back-to-back rooms.

The player must carefully decide **which cards to play, fight, discard, or flee from** in order to survive the dungeon.

If the player’s health reaches **0**, the game ends.

If the dungeon deck is cleared, the player **wins**.

---

## Rule Reference

For further detail on how the game is played, the original rules for Scoundrel can be found here:

**Official Rules:**  
http://www.stfj.net/art/2011/Scoundrel.pdf

---

## Difference From the Original Game

One of the most fun aspects of Scoundrel is the sheer number of variations that exist, ranging from small balance tweaks to entire redesigns implementing Jokers, merchants, inventories, and much more. Whether you're a purist or a fanatic for house rules, there's truly something for everyone!

Our implementation stays almost entirely true to classic Scoundrel, except it contains **one small balance change**:

> **Multiple health potions can be used in a single turn.**

In the original game, potion usage is limited to one per turn. In our version, allowing multiple potions per turn helps:

- Reduce the impact of **extremely unlucky card draws**
- Prevent unwinnable situations caused by **low-roll RNG**
- Improve the overall **balance and playability** of the digital version

This change keeps the core strategy intact while making the gameplay experience less punishing and awkward.

---

## Technologies Used

- **Python**
- **Pygame**
- **pygame-cards** (card rendering and interaction)

---

## Project Goal

The goal of this project was to:

- Recreate the mechanics of a tabletop card game digitally
- Implement interactive card handling using Pygame
- Design a playable UI with health tracking, card movement, and combat logic
- Demonstrate collaborative development in a hackathon setting

---

## Running the Game

1. Install Python.
2. Install required dependencies:
   `pip install pygame'
   'pip install pygame_cards'
3. Run the main game file:
   --> Scoundrel.py

## Acknowledgment

Scoundrel was originally designed by **Zach Gage and Kurt Bieg**.  
This project is a fan recreation created for educational and hackathon purposes.
