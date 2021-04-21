from stanfordkarel import *

def main():
	drop_beeper_20()
	move()
	drop_beeper_21()
	move()

def drop_beeper_20():
	for i in range(20):
		put_beeper()

def drop_beeper_21():
	for i in range(21):
		put_beeper()