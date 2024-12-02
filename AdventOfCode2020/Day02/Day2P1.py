def read_passcodes(filename):
	f = open(filename)
	lines = f.read().split('\n')
	# print(lines)
	lines2 = []
	for x in lines:
		lines2.append(x.split(' '))
	# print (lines2)
	lines3 = []
	for x in lines2:
		x[0] = x[0].split('-')
		x[1] = x[1].split(':')
		lines3.append(x)
	return lines3	




valid = 0
data = read_passcodes("Day2IN.txt")
for line in data:
	lcount = 0
	for letter in line[2]:
		if(letter == line[1][0]):
			lcount += 1

	if((int(line[0][0]) <= lcount) and (lcount <= int(line[0][1]))):
		valid += 1
print(valid)