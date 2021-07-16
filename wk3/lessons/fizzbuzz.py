"""
Prints the Fizz Buzz sequence up to a given number.
"""

def main():
    # Fill me out!
	numb_fizz = 0 # divisible by 3
	numb_buzz = 0 # divisible by 5
	numb_fizzbuzz = 0 # divisilbe by both 3 and 5
	user_input = int(input("Number to count to: "))

	for i in range(1, user_input+1):
		if i % 3 == 0 and i % 5 == 0:
			print("fizzbuzz")
			numb_fizzbuzz += 1
		elif i % 3 == 0:
			print("fizz")
			numb_fizz += 1
		elif i % 5 == 0:
			print("buzz")
			numb_buzz += 1
		else: 
			print(str(i))

	print("")
	print("Number of fizz:", numb_fizz)
	print("Number of buzz:", numb_buzz)
	print("Number of fizzbuzz:", numb_fizzbuzz)

if __name__ == '__main__':
    main()