from stanfordkarel import *

def main():
	while front_is_clear():
		drop_the_bomb()
		ascend()
		move()
	drop_the_bomb()
	ascend()

def drop_the_bomb():
	turn_right()
	move()
	put_beeper()
	turn_left()

def ascend():
	turn_left()
	move()
	turn_right()

def turn_right():
	for i in range(3):
		turn_left()
