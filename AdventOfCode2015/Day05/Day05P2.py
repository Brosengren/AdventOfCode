def read_integers(filename):
	with open(filename) as f:
		return [x for x in f]

input = read_integers("Day05IN.txt")

# print(input)
nice = 0
for line in input:
    line.replace('\n', "")
    print(line)
    repeat = False
    for i in range(len(line)-1):
        letters=line[i] + line[i+1]
        if line.count(letters)>1:
            repeat =True
            break
    if not repeat:
        continue 


    skip=False
    for i in range(len(line)-2):
        if line[i] == line[i+2]:
            skip=True
            break
    if not skip:
        continue 
    
    nice += 1

print(nice)