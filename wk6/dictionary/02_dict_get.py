ages = {"Chris" : 33, "Julie" : 22, "Mehran" : 50}

#1 for x in ages.keys():
# 	print(str(x) + " -> " + str(ages[x]))

#2 for x in ages:
	# print(str(x) + " -> " + str(ages[x]))

# make_list = list(ages.keys()) # listing keys
# print(make_list)

#4 for x in ages.values():
# 	print(x)

# make_list = list(ages.values()) # listing values
# print(make_list)

# ages.pop("Mehran")
# print(ages)

del ages["Mehran"] # same a pop function
print(ages)

# ages.clear()
# print(ages)

print(len(ages)) # printing the number of pairs in the list