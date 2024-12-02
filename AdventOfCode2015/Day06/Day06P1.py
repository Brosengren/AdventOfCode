def read_integers(filename):
	with open(filename) as f:
		return [x for x in f]

input = read_integers("Day06IN.txt")
# print(input)

import re

width = 1000
height = 1000
lights = [[False for x in range(width)] for y in range(height)]
print(lights[888][1])


for line in input:
    numbers = re.findall(r'\d+',line)
    numbers = [int(x) for x in numbers]
    # print(numbers)

    for x in range(numbers[0], numbers[2]+1):
        for y in range(numbers[1], numbers[3]+1):
            if line.startswith("turn on"):
                lights[x][y] = True
            elif line.startswith("turn off"):
                lights[x][y] = False
            elif line.startswith("toggle"):
                lights[x][y] = not lights[x][y]

lit = 0
for x in range(width):
    for y in range(height):
        if lights[x][y]:
            lit += 1
print(lit)



