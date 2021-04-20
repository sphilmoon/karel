from stanfordkarel import *

# karel will sweep every beep on the map like Wall-E.
# start with decomposition.
# karel is ALWAYS facing east to meet pre- and post- conditions.
# I am using a 'comb strategy'.
# test your code as you progress.

def main():
	while left_is_clear(): # no cage line on the left of karel.
		clear_row()
		next_row()
	clear_row() # cleaning the last row right below the cage line.

def clear_row():
	while front_is_clear() # no cage line in front of karel.
		safe_pick()
		move()
	safe_pick() # the last column is blocked, so pick the beeper out of the while loop.

def safe_pick():
	if beepers_present():
		pick_beeper()

def next_row():
	turn_around()
	move_to_wall()
	turn_right()
	move()
	turn_right()

def move_to_wall():
	while front_is_clear():
		move()

def turn_around():
	turn_left()
	turn_left()

def turn_right():
	for i in range(3):
		turn_left()



