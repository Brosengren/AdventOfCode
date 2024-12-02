def read_file(filename):
	with open(filename) as f:
		return f.readlines()


input = read_file("Day03IN.txt")
report = [x.strip('\n') for x in input]
numbits =len(report[0])
ogrlist = list(report)
csrlist = list(report)
#print(ogrlist)
for col in range(numbits):
    if len(ogrlist) == 1:
        continue
    count = 0
    for row in ogrlist:
        if row[col] == '1':
            count += 1
        else:
            count -= 1
#    print(count)
    length = len(ogrlist)
    row = 0
    while (row < length):
        if count >= 0:
            if ogrlist[row][col] == '0':
                ogrlist.remove(ogrlist[row])
                row -= 1
                length -= 1
        else:
            if ogrlist[row][col] == '1':
                ogrlist.remove(ogrlist[row])
                row -= 1
                length -= 1
        row += 1
#    print(ogrlist)

for col in range(numbits):
    if len(csrlist) == 1:
        continue
    count = 0
    for row in csrlist:
        if row[col] == '1':
            count += 1
        else:
            count -= 1
#    print(count)
    length = len(csrlist)
    row = 0
    while (row < length):
        if count >= 0:
            if csrlist[row][col] == '1':
                csrlist.remove(csrlist[row])
                row -= 1
                length -= 1
        else:
            if csrlist[row][col] == '0':
                csrlist.remove(csrlist[row])
                row -= 1
                length -= 1
        row += 1
#    print(csrlist)


ogr = int(ogrlist[0],2)
csr = int(csrlist[0],2)

print(ogr)
print(csr)
print(ogr * csr)
