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

    side1=dim[0]*dim[1]
    side2=dim[1]*dim[2]
    side3=dim[2]*dim[0]

    print(side1)
    print(side2)
    print(side3)

    sa=(side1+side2+side3)*2
    print (sa)
    smallest=min((side1,side2,side3))
    print(smallest)
    paper=sa+smallest
    print(paper)
    total+=paper
print(total)