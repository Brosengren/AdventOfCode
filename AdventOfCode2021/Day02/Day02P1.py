def read_file(filename):
	with open(filename) as f:
		return f.readlines()


input = read_file("Day02IN.txt")
movement = [x.strip('\n').split(' ') for x in input]
#print(movement)
h = 0
d = 0

for travel in movement:
	if   (travel[0].lower() == "forward"):
		h += int(travel[1])
	elif (travel[0].lower() == "down"):
		d += int(travel[1])
	elif (travel[0].lower() == "up"):
		d -= int(travel[1])
print(h*d)