from stanfordkarel import *

def main():
	go_to_beeper()
	pick_beeper()
	move()
	turn_left()
	go_home()
	put_beeper()
	go_back()

def go_to_beeper():
	move()
	move()

def go_home():
	move()
	move()

def go_back():
	turn_around()
	move_to_wall()
	turn_right()
	move_to_wall()
	turn_around()

def turn_around():
	turn_left()
	turn_left()

def move_to_wall():
	while front_is_clear():
		move()

def turn_right():
	for i in range(3):
		turn_left()
	
