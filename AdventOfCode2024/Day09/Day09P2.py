from pathlib import Path
filename = Path(__file__).parent.__str__() + "/Day09IN.txt"
with open(filename) as f:
    raw_input = [x.strip() for x in f][0]

id = 0
empty = False
output = []
for block in raw_input:
    block = int(block)
    while block > 0:
        if not empty:
            output.append(str(id))
        else:
            output.append('')
        block -= 1
    if not empty:
        id += 1
    empty = not empty

empty_index = 0
last_num_index = -1
def next_empty():
    global empty_index
    while output[empty_index] != '':
        empty_index += 1
        if empty_index == len(output):
            return False
    return True

def remove_empty_endings():
    global last_num_index
    while output[-1] == '':
        output.pop(-1)

while(next_empty()):
    remove_empty_endings()
    output[empty_index] = output.pop(-1)
    remove_empty_endings()

output = list(map(int, output))
count = 0
for i, num in enumerate(output):
    count += i * num

print(count)
