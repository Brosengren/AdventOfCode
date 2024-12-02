def readFile(filename):
	with open(filename) as f:
		return [x for x in f]

input = readFile("Day02INtest.txt")
Oplay = []
Mplay = []

print(input)
for line in input:
    Oplay.append(line[0])
    Mplay.append(line[2])
print(Oplay)
print(Mplay)