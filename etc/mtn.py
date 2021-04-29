from stanfordkarel import *

# think about decomposition steps to solve the problems.

def main():
	ascende()
	put_beeper()
	descende()

# pre: karel is facing a step of the mountain.
# post: karel is on the top of the mountain.

def ascende():
	while front_is_blocked():
		step_up()

# pre: karel is facing a step of the mountain.
# post: karel is one step-up and still facing the mountain.

def step_up():
	turn_left()
	move()
	turn_right()	
	move()

# pre: karel is on the top of the mountain.
# post: karel is on the east side of the mountain.

def descende():
	while front_is_clear():
		step_down()

def step_down():
	move()
	turn_right()
	move()
	turn_left()

def turn_right():
	for i in range(3):
		turn_left()

# running the karel GUI
if __name__ == "__main__":
    run_karel_program()
