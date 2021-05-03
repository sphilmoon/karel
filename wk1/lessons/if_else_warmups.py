from stanfordkarel import *

def main():
	invert_spot()
	move_if_clear()
	conditional_run()
	turn_signal()

def invert_spot():
	if beepers_present():
		pick_beeper()
	else:
		put_beeper()

def move_if_clear():
	if front_is_clear():
		move()
		put_beeper()
	else:
		put_beeper()

def conditional_run():
	if beepers_present():
		turn_left()
	else:
		turn_right()

def turn_right():
	for i in range(3):
		turn_left()
		
def turn_signal():
	if front_is_blocked():
		put_beeper()
		turn_left()
		move()
	else:
		pass