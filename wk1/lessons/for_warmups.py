from stanfordkarel import *

def main():
	place_10_beepers()
	move_5_times()
	backflip()
	frontflip() # karel cannot do frontflip.
	square()
	in_a_row()

def place_10_beepers():
	for i in range(10):
		put_beeper()

def move_5_times():
	for i in range(5):
		move()

def backflip():
	for i in range(4):
		turn_left()

def frontflip():
	for i in range(4):
		turn_right()

def turn_right():
	for i in range(3):
		turn_left()

def square():
	for i in range(4):
		put_beeper()
		move()
		turn_left()

def in_a_row():
	for i in range(3):
		put_beeper()
		move()
	put_beeper()