num = 0
inraw = []
with open("Day6IN.txt") as f:
	inraw = f.read().split("\n\n")
answers = []
for line in inraw:
	answers.append(line.split("\n"))
for group in answers:
	common = '8675309'
	for person in group:
		if(common == '8675309'):
			common = person
		else:
			i = 0
			while(i < len(common)):
				try:
					if(common[i] not in person):
						common = common.replace(common[i], '')
						i -= 1 
				except:
					pass
				i += 1
	print(common)
	for each in common:
		num += 1
print(num)