from pathlib import Path
filename = Path(__file__).parent.__str__() + "/Day03IN.txt"
with open(filename) as f:
    raw_input = [x for x in f]


import re
mul_list = []
for line in raw_input:
    mul_list += re.findall("mul\(\d*,\d*\)|don't\(\)|do\(\)", line)

total = 0
doing = True
for mul in mul_list:
    print(mul)
    if doing:
        if mul == "don't()":
            doing = False
        elif mul != "do()":
            nums = re.findall("\d*", mul)
            nums = list(map(int, [x for x in nums if x]))
            total += nums[0] * nums[1]
    if not doing:
        if mul == "do()":
            doing = True

print(total)