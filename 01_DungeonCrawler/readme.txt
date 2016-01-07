TechClimbers Workshop - Dungeon Crawler
=======================================

This is a sample implementation of a simple text-based dungeon crawler written
for a TechClimbers [ www.techclimbers.com ] workshop.


Getting Started
---------------

Run the tcdungeon python script to get started. Controls are as follows:

w - move north
s - move south
a - move west
d - move east
p - print a map of the known dungeon
q - quit

The goal is to find the treasure while avoiding the monsters and pits. The
dungeon is comprised of a grid of chambers and the player begins in the middle
of the southern most row. Upon encountering a monster or pit a life is lost and
the player is returned to the starting chamber. The player has 3 lives to find
the treasure.


Notes
-----

- The default dungeon is 5x5 and there are 2 monsters and 2 pits
- The dungeon_rows, dungeon_cols, num_monsters, num_pits variables can be
  altered to change these values