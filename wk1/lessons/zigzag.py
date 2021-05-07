from karel.stanfordkarel import *

def main():
    while front_is_clear():
        zigzag()
    zigzag()

def zigzag():
    plus_45()
    minus_45()

def plus_45():
    while left_is_clear():
        put_beeper()
        move()
        turn_left()
        move()
        turn_right()
        #put_beeper()

def minus_45():
    while right_is_clear():
        put_beeper()
        move()
        turn_right()
        move()
        turn_left()
        #put_beeper()

def turn_right():
    for i in range(3):
        turn_left()