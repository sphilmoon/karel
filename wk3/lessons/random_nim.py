import random

NUM_EXPERIMENTS = 10000
N_STONES = 20

def main():
	n_player1_wins = 0
	for i in range(NUM_EXPERIMENTS):
		winner = simulate_random_nimm()
		if winner == 1:
			n_player1_wins += 1
	print(n_player1_wins)

def simulate_random_nimm():
	player = 1
	stones = N_STONES # redefining the constant, cuz constant can't be changed.

	while stones > 0:
		take = random.randint(1, 2)
		stones -= take
		if player == 1:
			player == 2
		else:
			player == 1

	return player # giving the winner information. 

if __name__ == "__main__":
    main()