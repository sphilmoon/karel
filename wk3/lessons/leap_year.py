def main():
    user_input = int(input("Please type a year: "))
    if user_input % 4 == 0 or user_input % 100 == 0 or user_input % 400 == 0:
        print("That's a leap year!")
    else:
        print("Not a leap year.")

if __name__ == "__main__":
    main()