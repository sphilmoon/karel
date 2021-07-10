SENTINEL = 0

def main():
	total = 0
	user_input = float(input("Enter a value: "))
	total += user_input
	print("Running total is", total)

	while user_input != SENTINEL:
		user_input = float(input("Enter a value: "))
		total += user_input
		print("Running total is", total)

if __name__ == "__main__":
    main()