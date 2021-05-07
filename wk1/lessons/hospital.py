from stanfordkarel import *

def main():
	check_beeper()

def check_beeper():
    while front_is_clear():
        if front_is_clear():
            move()
        if beepers_present():
            pick_beeper()
            build_hospital()

# pre-condition: we are on the cell where it has a beeper.
# post-conditions: 2*3 beeper columns
def build_hospital():
    turn_left()
    place_row()
    turn_right()
    move()
    turn_right()
    place_row()
    turn_left()

# putting three beepers in a row.
def place_row():
    for i in range(2):
        put_beeper()
        move()
    put_beeper()

def turn_right():
    for i in range(3):
        turn_left()