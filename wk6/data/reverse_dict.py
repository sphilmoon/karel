# This is an ultimate concept of CS106A aka Code In Place.
def main():	
	
	ages = {
		'Mehran': 51,
		'Gary': 70,
		'Chris': 33,
		'Brahm': 24,
		'Adele': 33,
		'Freya': 0.3,
		'Lionel': 33,
		'Rihanna': 33,
		'Stephen': 33,
		'Skrillex': 33
	}
	reversed_dict = reverse(ages)
	print(reversed_dict)

	# standard code to print out a dictionary
	print("")
	print('Reversed:')

	# for each key
	for key in reversed_dict:
	# print out the key, and its corresponding value.
		print(key, '->', reversed_dict[key])

def reverse(original):
# should create and return a new dictionary where the values of the original are now keys!

	# first, making an empty dictionary.
	reversed_dict_func = {}	
	
	# start with looping all the values in the original.
	for old_key in original:
		old_value = original[old_key]

		# reversed_dict_func[old_value] = old_key

		if old_value not in reversed_dict_func:
			reversed_dict_func[old_value] = [old_key]
		else:
			# Let's try appending the value to the list
			value_list = reversed_dict_func[old_value]
			value_list.append(old_key)

	return reversed_dict_func # must return, so I can use it in the main function.

if __name__ == '__main__':
	main()