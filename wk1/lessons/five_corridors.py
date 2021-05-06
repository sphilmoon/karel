from stanfordkarel import *

def main():
	for i in range(4):
		check_row()
		top_row()
	check_row()
	turn_around()

def check_row():
	while front_is_clear():
		move()
	check_beeper()

def check_beeper():
	if beepers_present():
		first_column()
	else:
		put_beeper()
		first_column()

def first_column():
	turn_around()
	move_to_wall()

def turn_around():
	turn_left()
	turn_left()

def turn_right():
	for i in range(3):
		turn_left()

def move_to_wall():
	while front_is_clear():
		move()

def top_row():
	turn_right()
	move()
	turn_right()
