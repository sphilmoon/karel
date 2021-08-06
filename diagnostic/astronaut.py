def main():
    checking_height()

def checking_height():
    user_input = float(input("Enter your height in meters: "))

    if user_input >= 1.6 and user_input <= 1.9:
        print("Correct height to be an astronaut")
    if user_input < 1.6:
        print("Below minimum astronaut height")
    if user_input > 1.9:
        print("Above maximum astronaut height")

if __name__ == "__main__":
    main()