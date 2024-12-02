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

similarscore = 0

for i in list1:
	similarcount = 0
	for j in list2:
		if i == j:
			similarcount += 1
	similarscore += i * similarcount

			
print(similarscore)