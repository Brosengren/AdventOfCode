def read_integers(filename):
	with open(filename) as f:
		return [int(x) for x in f]


depths = read_integers("Day01IN.txt")

count = 0

for i in range(1, len(depths)):
	if depths[i] > depths[i-1]:
		count += 1

print(count)