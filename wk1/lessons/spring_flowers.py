from stanfordkarel import *

def main():
	move_to_wall()
	climb()
	bloom()
	descend()
	move_to_wall()
	climb()
	bloom()
	descend()
	move_to_wall()

def bloom():
	if no_beepers_present():
		put_beeper()
		move()
		put_beeper()
		turn_right()
		move()
		put_beeper()
		turn_right()
		move()
		put_beeper()

def turn_right():
	for i in range(3):
		turn_left()

def move_to_wall():
	while front_is_clear():
		move()

def climb():
	turn_left()
	while right_is_blocked():
		move()

def descend():
	move_to_wall()
	turn_left()