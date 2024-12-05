from pathlib import Path
filename = Path(__file__).parent.__str__() + "/Day05IN.txt"
with open(filename) as f:
    raw_input = [x.strip() for x in f]

split_index = raw_input.index('')
raw_rules = raw_input[:split_index]
raw_updates = raw_input[split_index+1:]

rules = [list(map(int, x.split('|'))) for x in raw_rules]
updates = [list(map(int, x.split(','))) for x in raw_updates]

count = 0

for update in updates:
    # for page in update:
    add_this = False
    good = False
    while(not good):
        good=True
        for x,y in rules:
            if x in update and y in update:
                prev = update[:update.index(y)]
                if x not in prev:
                    good = False
                    add_this = True
                    update.pop(update.index(x))
                    update.insert(update.index(y), x)
                    break
    if add_this:
        count += update[int(len(update)/2)]

print(count)
