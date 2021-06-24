"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

MIN_RANDOM = 10
MAX_RANDOM = 99

def main():
    streaks = 0

    while True:
        streaks += 1

        num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        num2 = random.randint(MIN_RANDOM, MAX_RANDOM)

        print("What is", str(num1), "+", str(num2), "?")
        user_answer = int(input(""))
        answer_statment = print("Your answer:", int(user_answer))
        
        if user_answer == num1 + num2:
            print("correct!", "You've gotten", streaks, "in a row.")
            if streaks == 3:
                print("Congratulations! You mastered addition!")
                break
        elif user_answer != num1 + num2:
            streaks = 0
            print("Incorrect.")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()