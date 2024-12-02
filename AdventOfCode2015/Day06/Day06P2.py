def read_integers(filename):
	with open(filename) as f:
		return [x for x in f]

input = read_integers("Day06IN.txt")
# print(input)

import re

width = 1000
height = 1000
lights = [[0 for x in range(width)] for y in range(height)]

for line in input:
    numbers = re.findall(r'\d+',line)
    numbers = [int(x) for x in numbers]
    # print(numbers)

    for x in range(numbers[0], numbers[2]+1):
        for y in range(numbers[1], numbers[3]+1):
            if line.startswith("turn on"):
                lights[x][y] += 1
            elif line.startswith("turn off"):
                lights[x][y] -= 1
                if lights[x][y] < 0:
                    lights[x][y] = 0
            elif line.startswith("toggle"):
                lights[x][y] += 2

lit = 0
for x in range(width):
    for y in range(height):
        lit += lights[x][y]
print(lit)
