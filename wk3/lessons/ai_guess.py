def main():
	print("Think of a number between 0 and 100")
	min_value = 0
	max_value = 100

	while True:
		que = min_value + (max_value - min_value) // 2 # guessing from value 50.
		if check_is_answer(que):
			break # the right answer.
		if check_is_greater(que):
			min_value = que + 1
		else:
			max_value = que - 1

	print("Your number was " + str(que) + "!")

def check_is_answer(value):
	return ask_true_false("Is your number " + str(value) + "?")

def check_is_greater(value):
	return ask_true_false("Is your number greater than " + str(value) + "?")

def ask_true_false(prompt):
	response = input(prompt + " ( Y / N ) ")
	return response == "y" or response == "Y"

if __name__ == "__main__":
    main()