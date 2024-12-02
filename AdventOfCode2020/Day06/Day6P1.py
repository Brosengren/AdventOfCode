import re

num = 0
seen = []
with open("Day6IN.txt") as f:
	for line in f.read().split('\n'):
		print(line)
		for char in line:
			match = 0
			for check in seen:
				if(char == check):
					match = 1
			if(match == 0):
				num += 1
				seen.append(char)
				print(seen)
		if(line == ''):
			seen = []
print(num)