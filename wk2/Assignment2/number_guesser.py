import random

MIN_RANDOM = 1
MAX_RANDOM = 100

def main():
	num_guesses = 0

	lower_limit = MIN_RANDOM
	higher_limit = MAX_RANDOM

	while True:
		num_guesses += 1
		
		guess = random.randint(lower_limit, higher_limit)
		user_input = input("Is your number", guess, "?")

		if user_input == "higher":
			lower_limit = guess + 1
		if user_input == "lower":
			higher_limit = guess -1
		if user_input == "correct":
			break

	print("I win! It took me", num_guesses, "guesses.")

if __name__ == '__main__':
	main()
