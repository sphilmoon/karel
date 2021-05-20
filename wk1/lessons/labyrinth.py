from karel.stanfordkarel import *

'''
def main():
    one_route()

def one_route():
    while front_is_clear():
        move_to_wall()
        if front_is_blocked():
            turn_left()
            if front_is_blocked():
                turn_around()
            else:
                move_to_wall()
        else:
            move_to_wall()
    while front_is_blocked():
        turn_left()
        move_to_wall()

def move_to_wall():
    while front_is_clear():
        move()

def turn_around():
    turn_left()
    turn_left()
'''

def main():
    while front_is_clear():
        move_to_wall()
        find_direction()

def move_to_wall():
    while front_is_clear():
        move()

def find_direction():
    if left_is_clear():
        turn_left()
    elif right_is_clear():
        turn_right()
    #else:
        #turn_right() THIS ALSO WORKS.
    
def turn_right():
    for i in range(3):
        turn_left()