def read_integers(filename):
	with open(filename) as f:
		return [x for x in f]

input = read_integers("Day04IN.txt")[0]
print(input)

import hashlib
num = 0

while True:
    string = f'{input}{num}'
    hash = hashlib.md5(string.encode()).hexdigest()
    if str(hash).startswith("00000"):
        break

    num += 1

print(num)
