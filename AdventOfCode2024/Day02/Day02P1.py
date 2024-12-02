from pathlib import Path
filename = Path(__file__).parent.__str__() + "/Day02IN.txt"
with open(filename) as f:
    raw_input = [x for x in f]

input = []
for line in raw_input:
    input.append(line.split())

def is_ascending_safe(report):
    prev = -1
    for i in report:
        i = int(i)
        if prev == -1:
            prev = i
            continue
        diff = i - prev
        if diff < 1 or diff > 3:
            return False
        prev = i
    return True

def is_descending_safe(report):
    prev = -1
    for i in report:
        i = int(i)
        if prev == -1:
            prev = i
            continue
        diff = prev - i
        if diff < 1 or diff > 3:
            return False
        prev = i
    return True


safe_count = 0
for report in input:
    if is_ascending_safe(report) or is_descending_safe(report):
        safe_count += 1

print(safe_count)
        