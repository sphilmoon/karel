# this is a week2 group assignment.
# 8 ball will answer your questions. 

import random

def main():
	question1 = input("What's your question: ")
	while question1 != '': # if q1 is not empty, then:
		randome_answer()
		question1 = input("What's your question: ")
	else: # if q1 is empty, then:
		print("No more questions.")

def randome_answer(): 
	answer_number = random.randint(1, 6)

	if answer_number == 1:
		print("Give me a hard question!")
	if answer_number == 2:
		print("Ask Google!")
	if answer_number == 3:
		print("Absolutely!")
	if answer_number == 4:
		print("I need a moment...")
	if answer_number == 5:
		print("Probably not")
	if answer_number == 6:
		print("It's a secret.")

if __name__ == "__main__":
    main()