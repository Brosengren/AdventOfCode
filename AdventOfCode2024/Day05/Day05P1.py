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
    good = True
    for a,b in rules:
        if a in update and b in update:
            prev = update[:update.index(b)]
            if a not in prev:
                    good = False
                    break
    if good:
        count += update[int(len(update)/2)]
print(count)