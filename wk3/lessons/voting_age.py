P = 16
S = 25
M = 48

def main():
	user_age = int(input("How old are you? "))
	if user_age >= P and user_age < S and user_age < M:
		print("You can vote in P where the voting age is", P)
		print("You cannot vote in S where the voting age is", S)
		print("You cannot vote in M where the voting age is", M)
	elif user_age >= S and user_age >= P and user_age < M:
		print("You can vote in S where the voting age is", S)
		print("You can vote in P where the voting age is", P)
		print("You cannot vote in M where the voting age is", M)
	elif user_age >= S and user_age >= P and user_age >= M:
		print("You can vote in S where the voting age is", S)
		print("You can vote in P where the voting age is", P)
		print("You can vote in M where the voting age is", M)

if __name__ == "__main__":
    main()