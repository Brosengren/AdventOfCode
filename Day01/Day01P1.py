def read_integers(filename):
	with open(filename) as f:
		return [x for x in f]

inputs = read_integers("Day01IN.txt")
list1 = []
list2 = []
for line in inputs:
	nums = line.split()
	list1.append(int(nums[0]))
	list2.append(int(nums[1]))
list1.sort()
list2.sort()
totdiff = 0
for i in range(len(list1)):
	totdiff += abs(list1[i] - list2[i])
print(totdiff)