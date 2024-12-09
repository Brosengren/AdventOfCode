from pathlib import Path
filename = Path(__file__).parent.__str__() + "/Day08IN.txt"
with open(filename) as f:
    raw_input = [x.split()[0] for x in f]

# print(raw_input)
import re

# create antinode array
antinodes = [[0] * len(raw_input[0]) for col in range(len(raw_input))]

# get all different signals
letter_list = []
for line in raw_input:
    for letter in line:
        if letter == '.':
            continue
        if not letter_list.__contains__(letter):
            letter_list.append(letter)

print(letter_list)

for letter in letter_list:
    # get locations of each letter
    letter_locations = []
    for i, line in enumerate(raw_input):
        cols = [m.start() for m in re.finditer(letter, line)]
        if cols:
            for each in cols:
                letter_locations.append([i,each])

    print(letter_locations)
    for i, node1 in enumerate(letter_locations):
        for j, node2 in enumerate(letter_locations):
            if j == i:
                continue
            dif1 = node1[0] + (node1[0] - node2[0])
            dif2 = node1[1] + (node1[1] - node2[1])
            try:
                if dif1 < 0 or dif2 < 0:
                    continue
                print("["+str(dif1)+"]["+str(dif2)+"]",end=' ')
                antinodes[dif1][dif2] = 1
                print("+")
            except:
                print("x")



for x in antinodes:
    print(x)

count = 0
for row in antinodes:
    for col in row:
        count += col

print(count)
