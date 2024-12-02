passes = []
with open("Day5IN.txt") as f:
	passes = f.readlines()
line = []
char = []
seatlist = []
rowstr=""
colstr=""
for line in passes:
	for char in line:
		if(char == 'F'):
			rowstr = rowstr + "0"
		if(char == 'B'):
			rowstr = rowstr + "1"
		if(char == 'L'):
			colstr += '0'
		if(char == 'R'):
			colstr += '1'
	row = int(rowstr, 2)
	col = int(colstr, 2)
	currseat = (row * 8) + col
	seatlist.append(currseat)
	rowstr = ""
	colstr = ""
seatlist.sort()
for i in range(0, len(seatlist)-1):
	if (seatlist[i] != seatlist[i+1]-1):
		print(seatlist[i]+1)