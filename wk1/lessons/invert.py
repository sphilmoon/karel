from stanfordkarel import *

def main():
	while front_is_clear():
		if beepers_present():
			pick_beeper()
			move()
		else:
			put_beeper()
			move()
	if beepers_present():
		pick_beeper()
	else:
		put_beeper()