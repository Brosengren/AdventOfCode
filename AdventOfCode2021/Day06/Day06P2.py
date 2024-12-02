def read_file(filename):
	with open(filename) as f:
		return f.readlines()


input = read_file("Day06IN.txt")
fishes = input[0].split(',')

today = [0 for each in range(9)]
yesterday = list(today)
for each in fishes:
	today[int(each)] += 1
# print(today)
# print(yesterday)
days = 256
for each in range(1, days+1):
	yesterday = list(today)
	today = [0 for each in range(9)]
	for x in range(len(yesterday)):
		if(x==0):
			today[6] += yesterday[x]
			today[8] += yesterday[x]
		else:
			today[x-1] += yesterday[x]
	print(f"{each} {today}")
print(sum(today))