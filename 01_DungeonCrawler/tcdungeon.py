#!/usr/bin/python

from random import randint  # import randint for use in randomizing positons
import tcinput  # import our custom i/o methods for keyboard input

dungeon_rows = 5  # number of rows in the dungeon
dungeon_cols = 5  # number of rows in the dungeon
num_monsters = 2  # number of monsters in the dungeon
num_pits = 2      # number of pits in the dungeon
player_lives = 3  # number of lives the player has remaining

found_treasure = False  # indicates if the treasure has been found
quit = False  # indicates if the user has pressed quit

start_r = 0 # starting position row
start_c = int(dungeon_cols / 2) # starting position column

player_r = start_r # player's current position row, initialized to the starting row
player_c = start_c # player's current position column, initialized to the starting column

dungeon = [] # list to hold the dungeon data
dungeon_map = [] # list to hold the player's map of the explored dungeon

# to represent the dungeon chamber states we will use the following definitions:
#   0: open chamber
#   1: starting position
#   2: treasure
#   3: monster chamber
#   4: pit chamber

# initialize dungeon to all zeros
for r in range(dungeon_rows):
	dungeon.append([])  # append an empty list for this row
	dungeon_map.append([])
	for c in range(dungeon_cols):
		dungeon[r].append(0)  # append a 0 for each column in the current row
		dungeon_map[r].append('?') # initialize all the cells to '?' on the map

dungeon[start_r][start_c] = 1  # set the start position
dungeon_map[start_r][start_c] = '.'  # mark the chamber as visited on the map

# randomly generate the treasure's position
t_row = start_r
t_col = start_c
while dungeon[t_row][t_col] != 0:
	t_row = randint(0, dungeon_rows - 1)
	t_col = randint(0, dungeon_cols - 1)
dungeon[t_row][t_col] = 2

# randomly place monsters
for m in range (num_monsters):
	m_row = randint(0, dungeon_rows - 1)
	m_col = randint(0, dungeon_cols - 1)
	while dungeon[m_row][m_col] != 0:
		m_row = randint(0, dungeon_rows - 1)
		m_col = randint(0, dungeon_cols - 1)
	dungeon[m_row][m_col] = 3

# randomly place pits
for p in range (num_pits):
	p_row = randint(0, dungeon_rows - 1)
	p_col = randint(0, dungeon_cols - 1)
	while dungeon[p_row][p_col] != 0:
		p_row = randint(0, dungeon_rows - 1)
		p_col = randint(0, dungeon_cols - 1)
	dungeon[p_row][p_col] = 4

# print the greeting
print('You have entered a cave in search of treasure. You hear a strage roar from somewhere deep within but you are brave. Good luck!')
print('You stand in an empty chamber')

# main game loop
# loop while player has lives left, has not quit, and the treasure has not been found
while player_lives > 0 and not found_treasure and not quit:
	key = tcinput.getkey()  # wait for a key press from the user
	if key == 'w' or key == 'W':
		if player_r < dungeon_rows - 1:  # the user pressed the w key so move north if there is room
			player_r += 1
			print('You move north')
		else:
			print('You run into a wall and cannot move north (also, ouch)')
	elif key == 's' or key == 'S':
		if player_r > 0:  # the user pressed the s key so move south if there is room
			player_r -= 1
			print('You move south')
		else:
			print('You run into a wall and cannot move south (also, ouch)')
	elif key == 'd' or key == 'D':
		if player_c < dungeon_cols - 1:  # the user pressed the d key so move east if there is room
			player_c += 1
			print('You move east')
		else:
			print('You run into a wall and cannot move east (also, ouch)')
	elif key == 'a' or key == 'A':
		if player_c > 0:  # the user pressed the a key so move west if there is room
			player_c -= 1
			print('You move west')
		else:
			print('You run into a wall and cannot move west (also, ouch)')	
	elif key == 'p' or key == 'P':
		for r in range(dungeon_rows - 1, -1, -1):  # the user pressed the p key so print out the map
			for c in range(0, dungeon_cols):
				if r == player_r and c == player_c:
					print('X'),
				else:
					print(dungeon_map[r][c]),
			print('')
	elif key == 'q' or key == 'Q':
		print('Goodbye')  # the user pressed q so print a goodbye message and set the quit variable to True
		quit = True

	cell = dungeon[player_r][player_c]  # get the value of the current cell

	if cell == 2:
		# the treasure has been reached so print a message and set found_treasure to True
		print('You found the treasure! Yay!')
		found_treasure = True
		dungeon_map[player_r][player_c] = 'T'  # mark the treasure's location on the map
	elif cell == 3:
		# a monster was encountered so print a message and decrement player_lives
		print('You encountered a fearsome beast and were devoured...bummer')
		player_lives -= 1
		dungeon_map[player_r][player_c] = 'M'  # mark the monster's location on the map
		if player_lives > 0:
			# the player still has lives so reset the player to the start position and print a message
			player_r = start_r
			player_c = start_c
			print('Lives remaining:'),
			print(player_lives)
			print('You awaken in the mouth of the cave where you started. You stand in an empty chamber')
	elif cell == 4:
		# a pit was encountered so print a message and decrement player_lives
		print ('You fell into a bottomless abyss...oops')
		player_lives -= 1
		dungeon_map[player_r][player_c] = 'P'  # mark the pit's location on the map
		if player_lives > 0:
			# the player still has lives so reset the player to the start position and print a message
			player_r = start_r
			player_c = start_c
			print('Lives remaining:'),
			print(player_lives)
			print('You awaken in the mouth of the cave where you started. You stand in an empty chamber')
	else:
		# the cell is empty so print a message
		print('You stand in an empty chamber')
		dungeon_map[player_r][player_c] = '.'  # mark the chamber as visited on the map

if player_lives == 0:
	# if the game loop exited because the player ran out of lives print a message
	print('Another fallen hero, another failed quest. Goodbye.')