import random

N_GAMES = 3

def main():
	print_welcome()
	total_score = 0

	for i in range(N_GAMES):
	# 1. Define the moves.
		ai_move = get_ai_move()
		human_move = get_human_move()

		winner = get_winner(ai_move, human_move)
		total_score = update_score(winner, total_score)

		print("The AI move was", ai_move)
		print("The winner was", winner)
		print("")
	print("Total score is", total_score)

def update_score(winner, total_score):
	if winner == "AI":
		total_score -= 1
	
	if winner == "human":
		total_score += 1
	
	if winner == "tie":
		total_score += 0
	return total_score

def get_ai_move():
    value = random.randint(1, 3)
    if value == 1:
        return "rock"
    if value == 2:
        return "paper"
    else:
        return "scissors"

def get_human_move():
	'''
    human_move = input("Enter your move: ")
    while human_move != "paper":
        human_move = input("type valid move: ")
	'''

	while True:
		human_move = input("Enter your move: ")

		if is_valid_move(human_move):
			return human_move
		else:
			print("invalid move.")
			print("")

def is_valid_move(move): # use boolean function. 
    if move == "rock":
        return True
    if move == "paper":
        return True
    if move == "scissors":
        return True
    return False    

def get_winner(ai_move2, human_move2): # using parameters with the same name.

	if ai_move2 == human_move2: 
		return "tie"
	if ai_move2 == "rock":
		if human_move2 == "scissors":
			return "AI"
		if human_move2 == "paper":
			return "human"
	if ai_move2 == "paper":
		if human_move2 == "rock":
			return "AI"
		if human_move2 == "scissors":
			return "human"
	if ai_move2 == "scissors":
		if human_move2 == "rock":
			return "human"
		if human_move2 == "paper":
			return "AI"

def print_welcome():
	print("Let's play Rock, Paper, Scissors.")

if __name__ == '__main__':
    main()