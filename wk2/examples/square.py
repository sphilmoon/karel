import math

def main():
    user_input = float(input("Type a number to see its square: "))
    print(user_input, "squared is", math.pow(user_input, 2))

if __name__ == "__main__":
    main()