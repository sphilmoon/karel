from stanfordkarel import *

def main():
	while front_is_clear():
		put_beeper()
		move()
	put_beeper()

# or

'''
def main():
	while front_is_clear():
		put_tens()
	put_tens()

def put_tens():
	for i in range(10):
		put_beeper()
		move()
'''

def main():
	five_beepers()

def five_beepers():
	for i in range(5):
		if front_is_clear():
			put_beeper()
			move()