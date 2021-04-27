from stanfordkarel import *

# pre-condition: karel is always facing the EAST. 

def main():
    while front_is_clear():
        build_column()
        go_to_next_column()
    build_column()
    turn_around()
    move_to_wall()
    turn_left()

def build_column():
    turn_left()
    while front_is_clear():
        safe_put()
        move()
    safe_put()

def safe_put():
    if no_beepers_present():
        put_beeper()

def go_to_next_column():
    turn_around()
    move_to_wall()
    turn_left()
    for i in range(4):
        move()

def turn_around():
    turn_left()
    turn_left()

def move_to_wall():
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()