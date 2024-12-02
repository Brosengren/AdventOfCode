def read_integers(filename):
	with open(filename) as f:
		return [x for x in f]

input = read_integers("Day03IN.txt")[0]
print(input)

xLocation=0
yLocation=0
grid = {
"0,0": 1
}

for x in input:
    match(x):
        case '^':
            yLocation+= 1
        case 'v':
            yLocation-= 1
        case '<':
            xLocation-= 1
        case '>':
            xLocation+= 1

    location = f"{xLocation},{yLocation}"
    print(location)
    if location in grid.keys():
        grid[location]+= 1
    else:
        grid.update({location: 1})
print(grid)
print(len(grid))
    

