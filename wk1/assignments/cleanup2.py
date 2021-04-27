from stanfordkarel import *

def main():
	cleanup_karel()

def cleanup_karel():
	while front_is_clear():
		move()
		safe_pick()

def safe_pick():
	if beepers_present():
		pick_beeper()