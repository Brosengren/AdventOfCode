def read_integers(filename):
	with open(filename) as f:
		return [x.replace('\n','') for x in f]

input = read_integers("Day07/Day07IN.txt")
# print(input)

import re

def parse_num(op:str):
    if op.isdigit():
          return int(op)
    else:
         return int(signals[op])

signals = {}
while input:
    for line in input:
        try:
            sides = line.split(" -> ")
            # print(sides)

            if sides[0].count("AND"):
                more = sides[0].split(' ')
                signals[sides[1]] = parse_num(more[0]) & parse_num(more[2])
                
            elif sides[0].count("OR"):
                more = sides[0].split(' ')
                signals[sides[1]] = parse_num(more[0]) | parse_num(more[2])

            elif sides[0].count("LSHIFT"):
                more = sides[0].split(' ')
                signals[sides[1]] = parse_num(more[0]) << int(more[2])

            elif sides[0].count("RSHIFT"):
                more = sides[0].split(' ')
                signals[sides[1]] = parse_num(more[0]) >> int(more[2])

            elif sides[0].count("NOT"):
                more = sides[0].split(' ')
                x = int(signals[more[1]])
                y = ~int(signals[more[1]]) & 0xFFFF
                # print(f"{x}  ::::  {y}")
                signals[sides[1]] = ~parse_num(more[1]) & 0xFFFF

            elif len(sides[0].split(" ")) == 1:
                if sides[0] == 'lx':
                    pass
                signals[sides[1]] = parse_num(sides[0])

            else:
                 pass

            input.pop(input.index(line))
        except:
            pass

print(signals['a'])
