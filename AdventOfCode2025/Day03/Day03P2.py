def read_input(filename):
    with open(filename) as f:
        return [x.strip() for x in f]

inputs = read_input("Day03IN.txt")

jolts = 0

for bank in inputs:
    dlen = 12
    digits = ['0'] * dlen
    dpos = 0
    for num in range(dlen):
        for pos in range(dpos, len(bank)-dlen+num+1):
            if bank[pos]>digits[num]:
                digits[num] = bank[pos]
                dpos = pos + 1
    print(f"Bank: {bank} -> Digits: {digits}")
    jolts += int("".join(digits))

print(f"Total jolts: {jolts}")
