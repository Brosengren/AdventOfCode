def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]
		
		
expenses = read_integers("Day1IN.txt")
for x in expenses:
	for y in expenses:
		if(x + y == 2020):
			print(x * y)
			