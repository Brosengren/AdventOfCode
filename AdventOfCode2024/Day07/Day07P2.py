from pathlib import Path
filename = Path(__file__).parent.__str__() + "/Day07IN.txt"
with open(filename) as f:
    raw_input = [x.split() for x in f]

def operate(total=0, index=0) -> bool:
    global answer
    global elements

    if index == len(elements):
        return total == answer

    tot = total + elements[index]
    if operate(tot, index +1):
        return True
    
    tot = total * elements[index]
    if operate(tot, index+1):
        return True

    tot = int(str(total)+str(elements[index]))
    if operate(tot, index+1):
        return True
    
    if operate(tot, index+1):
        return True
    
    return False

line_num = 1
tot_lines = len(raw_input)
count = 0
count_total = 0
for line in raw_input:
    answer = int(line[0].removesuffix(':'))
    elements = list(map(int, line[1:]))
    print(line_num, end='')
    print('/', end='')
    print(tot_lines, end=" -- ")
    print(line)
    line_num += 1

    if operate():
        count += 1
        count_total += answer

print(count)
print(count_total)
