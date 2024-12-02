def read_integers(filename):
	with open(filename) as f:
		return [x for x in f]

input = read_integers("Day05IN.txt")
print(input)
nice = 0
for line in input:
    vowel = line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u')
    if vowel < 3:
        continue

    double=False
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            double=True
            break
    if not double:
        continue 

    stuff=line.count('ab') + line.count('cd') + line.count('pq') + line.count('xy')
    if stuff:
        continue
    
    nice += 1

print(nice)