def read_file(filename):
	with open(filename) as f:
		return f.readlines()


input = read_file("Day02IN.txt")
movement = [x.strip('\n').split(' ') for x in input]

h = 0
d = 0
a = 0

for travel in movement:
	if   (travel[0].lower() == "forward"):
		h += int(travel[1])
		d += int(travel[1]) * a
	elif (travel[0].lower() == "down"):
		a += int(travel[1])
	elif (travel[0].lower() == "up"):
		a -= int(travel[1])
print(h*d)