# this is a week2 group assignment.

# these are the constants:
MARS_GRAVITY = 0.378

def main():
	earth_weight = float(input("Enter your Earth weight: "))
	mars_weight = MARS_GRAVITY * earth_weight
	print("The equivalent weight on Mars is ", str(mars_weight))

if __name__ == "__main__":
    main()