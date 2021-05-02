from karel.stanfordkarel import *

def main():
    while front_is_clear():
        move_to_beeper()
        while beepers_present():
            pick_beeper()
        check_wall()
        while front_is_blocked():
            turn_right()
            move()

def move_to_beeper():
    while no_beepers_present():
        move()

def check_wall():
    if left_is_blocked():
        turn_right()
    elif left_is_clear():
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()
