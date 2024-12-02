def hit_trees(slope, over, down):
	count = 0
	x = 0
	length = len(slope[0])
	for y in range(down, len(slope), down) :
		x = (x + over) % length
		# print(slope[y][x])
		if (slope[y][x] == '#'):
			count += 1
	print("{} over, {} down, {} trees".format(over, down, count))
	return count





with open("Day3IN.txt") as f:
	slope = f.read().splitlines()

m =		hit_trees(slope, 1, 1)
m = m * hit_trees(slope, 3, 1)
m = m * hit_trees(slope, 5, 1)
m = m * hit_trees(slope, 7, 1)
m = m * hit_trees(slope, 1, 2)
print(m)