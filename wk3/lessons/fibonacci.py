
'''
constant = 0

def main():
    for i in range(10000):
        i += constant
        print(i)
		'''

MAX = 10000

def main():
	current_numb = 0
	next_numb = 1
	while current_numb <= MAX:
		print(current_numb)
		rule = current_numb + next_numb
		current_numb =next_numb
		next_numb = rule

if __name__ == "__main__":
    main()

