def main():
    sequence_length = 1
    intro()
    user_input = float(input("Enter num: "))
	
    while user_input >= user_input:
        user_input = float(input("Enter num: "))
        sequence_length += 1
    else:
        print("Thanks for playing!")
    print("Sequence length:", sequence_length)

def intro():
    print("Enter a sequence of non-decreasing numbers.")

def user_input():
    user_input = float(input("Enter num: "))

if __name__ == "__main__":
    main()