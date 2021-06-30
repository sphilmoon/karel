"""
File: nimm.py
-------------------------
Add your comments here.
"""

def main():
    stones = 20

    while stones > 0:
        player = 0

        print("There are", stones, "stones left.")
        
        if player == 0:
            user_input = int(input("Player 1, would you like to remove 1 or 2 stones? "))
            while user_input != 2 and user_input != 1:
                user_input = int(input("Please enter 1 or 2: "))
            
            stones -= user_input
            player += 1
            print("")

        if player == 1:
            user_input = int(input("Player 2, would you like to remove 1 or 2 stones? "))
            while user_input != 2 and user_input != 1:
                user_input = int(input("Please enter 1 or 2: "))

            stones -= user_input
            player -= 1
            print("")

    if player % 2 == 0:
        print("Player 2 wins! GAME OVER.")
    else:
        print("Player 1 wins! GAME OVER.")

        # elif user_input != 2 or user_input != 1:
        #     print("Please remove either '1' or '2' stones.")
        #     print("")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
