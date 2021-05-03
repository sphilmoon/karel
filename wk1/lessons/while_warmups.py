from stanfordkarel import *

def main():
	move_to_wall()
	clean_spot()
	turn_to_wall()
	fill_bottom_row()

def move_to_wall():
	while front_is_clear():
		move()

def clean_spot():
	while beepers_present():
		pick_beeper()

def turn_to_wall():
	while front_is_clear():
		turn_left()

def fill_bottom_row():
	while front_is_clear():
		put_beeper()
		move()
	put_beeper()