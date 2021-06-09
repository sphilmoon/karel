dog_conversion = 7.18

def main():
    human = float(input("Enter an age in human years: "))
    conversion = human * dog_conversion
    print("That's", conversion, "in dog years!")

if __name__ == "__main__":
    main()