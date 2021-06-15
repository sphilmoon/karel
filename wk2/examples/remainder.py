def main():
    numerator = float(input("Please enter an integer to be dived: "))
    denominator = float(input("Please enter an integer to dived by: "))
    division_int = numerator // denominator
    mode = numerator % denominator
    print("The result of this division is",
          int(division_int), "with a remainder of", int(mode))

if __name__ == "__main__":
    main()