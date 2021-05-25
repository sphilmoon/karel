from stanfordkarel import *

'''
Karel always needs to face east to meet 
the post-conditions match the pre-conditions.
'''

def main():
	for i in range(8):
		if not front_is_clear():
			jump_hurdle()
		else:
			move()

def jump_hurdle():
	ascend_hurdle()
	move()
	descend_hurdle()

def ascend_hurdle():
	turn_left()
	while right_is_blocked():
		move()
	turn_right()

def descend_hurdle():
	turn_right()
	move_to_wall()
	turn_left()

def move_to_wall():
	while front_is_clear():
		move()

def turn_right():
	for i in range(3):
		turn_left()

# running the karel GUI
if __name__ == "__main__":
    run_karel_program()