f = open("invictus.txt")
for line in f:
	line = line.strip() # or strip("\n"), rstrip(), lstrip().
	# processing line
f.close()

with open("invictus.txt") as f: # reading mode. No writing.
	for line in f:
		line = line.strip() # or strip("\n"), rstrip(), lstrip().
	# processing line

with open("invictus.txt", "w") as f: # writing and editing mode. No reading.
	for line in f:
		line = line.strip() # or strip("\n"), rstrip(), lstrip().
	# processing line

with open("invictus.txt", "w") as f: # writing and editing mode. No reading.
	f.write("hello")
	f.write("\n")
	f.write("there")
	# processing line