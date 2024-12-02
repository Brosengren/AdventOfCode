passes = []
with open("Day5IN.txt") as f:
	passes = f.readlines()
line = []
char = []
hiseat = 0
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
	if(currseat > hiseat):
		hiseat = currseat
	rowstr = ""
	colstr = ""
print(hiseat)