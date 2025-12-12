def read_input(filename):
    with open(filename) as f:
        return [x.strip() for x in f]

inputs = read_input("Day03IN.txt")

jolts = 0

for bank in inputs:
    first_digit = '0'
    first_loc = 0
    for pos in range(len(bank)-1):
        if bank[pos]>first_digit:
            first_digit = bank[pos]
            first_loc = pos
    second_digit = '0'
    second_loc = pos+1
    for pos in range(first_loc+1, len(bank)):
        if bank[pos]>second_digit:
            second_digit = bank[pos]
            second_loc = pos
    jolts += int(first_digit + second_digit)

print(f"Total jolts: {jolts}")
