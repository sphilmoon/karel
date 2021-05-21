from stanfordkarel import *

def main():
	five_beepers()

def five_beepers():
	for i in range(4):
		if front_is_clear():
			put_beeper()
			move()
	put_beeper()