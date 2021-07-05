import random

def main():
	stones = 20
	player = 1 

	print("There are", stones, "stones left.")

	while stones > 0:
		user_input = int(input("Player " + str(player) + " remove 1 or 2 stones: "))

		while user_input != 2 and user_input != 1:
			user_input = int(input("Please enter 1 or 2: "))
		print("")

		stones -= user_input
		player = which_player(player)

		if stones == 0:
			break
		else:
			print("There are", stones, "stones left.")

	# whoever break the while loop loses.
	# so player will always either 1+1 or 2-1.
	print("Player " + str(player) + " wins! GAME OVER.")

def which_player(player):
	if player == 1:
		player += 1
	elif player == 2:
		player -= 1
	return player

if __name__ == '__main__':
	main()