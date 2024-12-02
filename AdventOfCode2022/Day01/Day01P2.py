def readFile(filename):
	with open(filename) as f:
		return [x for x in f]

calList = readFile("Day01IN.txt")

print(calList)
max1 = 0
max2 = 0
max3 = 0
cnt = 0

for line in calList:
	try:
		cal = int(line)
		# print("cal =", cal)
		cnt += cal
		# print("cnt =", cnt)
	except:
		print(cnt)
		if cnt > max1:
			max3 = max2
			max2 = max1
			max1 = cnt
		elif cnt > max2:
			max3 = max2
			max2 = cnt
		elif cnt > max3:
			max3 = cnt
		cnt = 0

print("total of 3 max =", max1+max2+max3)

