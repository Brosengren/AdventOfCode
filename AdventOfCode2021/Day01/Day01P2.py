def read_integers(filename):
	with open(filename) as f:
		return [int(x) for x in f]


depths = read_integers("Day01IN.txt")

count = 0

for i in range(3, len(depths)):
	cur =  depths[i] +depths[i-1] +depths[i-2]
	prev = depths[i-1]+depths[i-2]+depths[i-3]
	if(cur > prev):
		count += 1

print(count)