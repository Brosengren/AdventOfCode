def read_integers(filename):
	with open(filename) as f:
		return [x for x in f]

input = read_integers("Day01IN.txt")[0]

print(input)
count = 0
position = 0
for x in input:
    position += 1
    if x == '(':
        count += 1
    if x  == ')':
        count -= 1
    if count < 0:
        break
    

print(count)
print(position)