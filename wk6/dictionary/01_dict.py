# Monday's lectures
# Key-values
# Keys are immutable, unique (e.g. int, float, string, list)
# Values are mutable, and they persist after the change

def have_birthday(dict, name):
	print("You're one year older,", name + "!")
	dict[name] += 1

def main():
	ages = {"Chris" : 33, "Julie" : 22, "Mehran" : 50}
	print(ages)
	have_birthday(ages, "Chris")
	print(ages)
	have_birthday(ages, "Mehran")
	print(ages)

if __name__ == "__main__":
    main()