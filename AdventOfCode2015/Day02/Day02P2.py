def read_integers(filename):
	with open(filename) as f:
		return [x for x in f]

inputs = read_integers("Day02IN.txt")
total = 0
for input in inputs:
    print(input)
    input=input.replace('\n',"")
    dim=input.split('x')
    dim = [int(x) for x in dim]
    print(dim)
    vol=dim[0]*dim[1]*dim[2]
    dim.pop(dim.index(max(dim)))
    print(dim)
    per=2*(dim[0]+dim[1])
    l=vol+per
    total+=l

print(total)