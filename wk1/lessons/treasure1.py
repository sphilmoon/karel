from karel.stanfordkarel import *

def main():
    find_treasure()

def find_treasure():
    while no_beepers_present(): # keep searching.
        move()
        while beepers_present(): # collect treasures then turn left!
            pick_beeper()
            turn_left()