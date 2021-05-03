from stanfordkarel import *

# pre-condition: karel is always facing the EAST. 

def main():
    while front_is_clear():
        put_beeper()
        ramp_up()
    put_beeper()

def ramp_up():
    move()
    move()
    turn_left()
    move()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()