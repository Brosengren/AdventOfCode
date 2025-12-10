def read_input(filename):
	with open(filename) as f:
		return [x for x in f]

inputs = read_input("Day01IN.txt")

dial = 50
count = 0
start_at_0 = False

for line in inputs:
    dstr = ''
    line = line.strip()
    move = 0

    if dial == 0:
        start_at_0 = True
    else:
        start_at_0 = False

    if line[0] == 'L':
        move = -int(line[1:])
    else:
        move = int(line[1:])

    if move > 99:
        count += move // 100
        move = move % 100
    elif move < -99:
        count += (-move) // 100
        move = move % -100

    dial += move
    dstr = f"move {move} to dial {dial} "
    if dial < 1 or dial > 99:
        dial = dial % 100
        dstr += f" -> wrap to {dial}"
        if not start_at_0:
            count += 1
            dstr += f" counted is now {count}"
    # print(dstr)
print(count)
