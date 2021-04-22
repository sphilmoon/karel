from stanfordkarel import *

def main():
	a_collect_all_beepers()
	b_drop_all_beepers()
	c_return_home()

def a_collect_all_beepers():
	while front_is_clear():
		collect_one_tower()
		move()
	collect_one_tower()

def collect_one_tower():
	turn_left()
	collect_line_of_beepers()
	turn_around()
	move_to_wall()
	turn_left()

def collect_line_of_beepers():
	while beepers_present():
		pick_beeper()
	if front_is_clear():
		move()

def turn_around():
	turn_left()
	turn_left()

def move_to_wall():
	while front_is_clear():
		move()

def b_drop_all_beepers():
	while beepers_in_bag():
		put_beeper()

def c_return_home():
	turn_around()
	move_to_wall()
	turn_around()

# running the karel GUI
if __name__ == "__main__":
    run_karel_program()
