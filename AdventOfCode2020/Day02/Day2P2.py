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
	if(((line[2][int(line[0][0])-1] == line[1][0]) or (line[2][int(line[0][1])-1] == line[1][0])) and (line[2][int(line[0][0])-1] != line[2][int(line[0][1])-1])):
		valid += 1
print(valid)