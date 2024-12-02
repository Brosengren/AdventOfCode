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
    disp_str = ""
    a= compile("disp_str="+line, 'test', 'exec')
    exec(a)
    disp += len(disp_str)

diff = chars-disp
print(diff)