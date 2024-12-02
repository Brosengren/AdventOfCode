def readFile(filename):
	with open(filename) as f:
		return [x for x in f]

calList = readFile("Day01INtest.txt")

print(calList)
max = 0
cnt = 0

for line in calList:
	try:
		cal = int(line)
		print("cal =",cal)
		cnt += cal
		print("cnt =", cnt)
	except:
		if cnt > max:
			max = cnt
			print("Changed max =", max)
		cnt = 0

print("total max =", max)
