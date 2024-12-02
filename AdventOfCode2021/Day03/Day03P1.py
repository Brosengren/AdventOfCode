def read_file(filename):
	with open(filename) as f:
		return f.readlines()


input = read_file("Day03IN.txt")
report = [x.strip('\n') for x in input]
countlist = [0 for x in range(len(report[0]))]
gamma = list(countlist)
epslion = list(countlist)
for row in report:
    for col in range(len(row)):
        if row[col] == '1':
            countlist[col] += 1
        else:
            countlist[col] -= 1
print(countlist)

for x in range(len(countlist)):
    if countlist[x] > 0:
        gamma[x] = 1
        epslion[x] = 0
    else:
        gamma[x] = 0
        epslion[x] = 1

print(gamma)
print(epslion)
a = int("".join(str(i) for i in gamma),2)
print(a)
b = int("".join(str(i) for i in epslion),2)
print(b)

print(a*b)