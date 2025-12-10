def read_input(filename):
	with open(filename) as f:
		return [x for x in f]

inputs = read_input("Day01IN.txt")

dial = 50
count = 0

for line in inputs:
    line = line.strip()
    move = 0
    if line[0] == 'L':
        move = -int(line[1:])
    else:
        move = int(line[1:])
    dial += move
    dial = dial % 100
    if dial == 0:
        count += 1
print(count)
