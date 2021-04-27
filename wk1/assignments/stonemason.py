from stanfordkarel import *

# pre-condition: karel is always facing the EAST. 

def main():
    while front_is_clear():
        clear_column()
        next_column()
    clear_column() #  

def clear_column():
    turn_left()
    while front_is_clear():
        safe_pick()
        move()
    safe_pick() # pick up the last beeper next to the cage line. 

def safe_pick():
    if beepers_present():
        pick_beeper()

def next_column():
    turn_around()
    move_to_wall()
    turn_left()
    move()

def turn_around():
    turn_left()
    turn_left()

def move_to_wall():
    while front_is_clear():
        move()