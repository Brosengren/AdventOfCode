with open("Day3IN.txt") as f:
	slope = f.read().splitlines()
count = 0
x = 0
length = len(slope[0])
for y in range(1, len(slope)):
	x = (x + 3) % length
	# print(slope[y][x])
	if (slope[y][x] == '#'):
		count += 1
print(count)
