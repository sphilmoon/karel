from stanfordkarel import *

def main():
    beeper_stairs()
    descend()
    reverse_zigzag()
    descend()
    put_beeper()
    turn_around()
    move_to_wall()
    turn_around()
    wipe_beepers()
    descend()
    turn_around()
    go_to_beeper()

def beeper_stairs():
    while front_is_clear():
        put_beeper()
        move()
        put_beeper()
        turn_left()
        move()
        turn_right()
    put_beeper()

def descend():
    turn_right()
    move_to_wall()
    turn_left()

def move_to_wall():
    while front_is_clear():
        move()

def reverse_zigzag():
    while no_beepers_present():
        turn_left()
        move()
        turn_left()
        move()
        turn_left()
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

def wipe_beepers():
    while front_is_clear():
        pick_beeper()
        move()
        pick_beeper()
        turn_left()
        move()
        turn_right()
    pick_beeper()

def go_to_beeper():
    while no_beepers_present():
        move()