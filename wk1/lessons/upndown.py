from stanfordkarel import *

def main():
    ascend()
    descend()

def ascend():
    while left_is_clear():
        turn_left()
        move()
        turn_right()
        move()

def turn_right():
    for i in range(3):
        turn_left()

def descend():
    while front_is_clear():
        move()
        turn_right()
        move()
        turn_left()