def read_integers(filename):
    with open(filename) as f:
        return [x.replace('\n','') for x in f]

input = read_integers("Day08IN.txt")
# print(input)

chars = 0
disp = 0

for line in input:
    line_count = len(line)
    chars += line_count
    disp += line_count
    disp += line.count('"')
    disp += line.count('\\')
    disp += 2
    

diff = disp-chars
print(diff)
