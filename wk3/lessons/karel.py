'''
Welcome to first person Karel. You're at row 1, column 1, facing East (facing column 3)
What would you like to do? You can move and turn left. Press enter to finish. move
You moved one step forward and now you're at row 1 column 2
What would you like to do? You can move and turn left. Press enter to finish. turn left
You turned left and are now facing North.
What would you like to do? You can move and turn left. Press enter to finish. turn left
You turned left and are now facing West.
What would you like to do? You can move and turn left. Press enter to finish. move
You moved one step forward and now you're at row 1 column 1.
What would you like to do? You can move and turn left. Press enter to finish. move
You can't move forward!
What would you like to do? You can move and turn left. Press enter to finish.
You've ended up at row 1 and column 1 facing West.
'''

MOVE = "move"
TURN_LEFT = "turn left"

N_COLS = 3  # notice these constants!
N_ROWS = 3

def main():
    print("Welcome to first person Karel. You're at row 1, column 1, facing East (facing column", N_COLS, ").")
    FACING = "East"
    user_input = str(input(
        "What would you like to do? You can 'move' or 'turn left'. Or press 'enter' to finish. "))
    current_cols = 1
    current_rows = 1

    while user_input != "":
        # moving 1 step right.
        if user_input == MOVE:
            if FACING == "East" and current_cols < N_COLS:
                current_cols += 1
                print("You moved one step forward and now you're at",
                current_rows, current_cols)
           # moving 1 step up.
            elif FACING == "North" and current_rows < N_ROWS:
                current_rows += 1
                print("You moved one step forward and now you're at",
                current_rows, current_cols)
            # moving 1 step left.
            elif FACING == "West" and current_cols > 1:
                current_cols -= 1
                print("You moved one step forward and now you're at",
                current_rows, current_cols)
            # moving 1 step below.
            elif FACING == "South" and current_rows > 1:
                current_rows -= 1
                print("You moved one step forward and now you're at",
                current_rows, current_cols)

        elif user_input == TURN_LEFT:
            if FACING == "East":
                FACING = "North"
            elif FACING == "North":
                FACING = "West"
            elif FACING == "West":
                FACING = "South"
            elif FACING == "South":
                FACING = "East"
            print("You turned left and now facing", FACING)
        user_input = str(input(
        "What would you like to do? You can 'move' or 'turn left'. Or press 'enter' to finish. "))
    
    # Final position. 
    print("You are at row", current_rows, "and column", current_cols, "facing", FACING)

if __name__ == "__main__":
    main()
