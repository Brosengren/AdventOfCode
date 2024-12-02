
def read_integers(filename):
	with open(filename) as f:
		return [x for x in f]

input = read_integers("Day03IN.txt")[0]
print(input)

xLocation=0
yLocation=0
rxLocation=0
ryLocation=0
turn= True
grid = {
"0,0": 2
}

for x in input:
    match(x):
        case '^':
            if turn:
                yLocation+= 1
            else:
                ryLocation+= 1
        case 'v':
            if turn:
                yLocation-= 1
            else:
                ryLocation-= 1
        case '<':
            if turn:
                xLocation-= 1
            else:
                rxLocation-= 1
        case '>':
            if turn:
                xLocation+= 1
            else:
                rxLocation+= 1

    location = f"{xLocation},{yLocation}"
    rlocation = f"{rxLocation},{ryLocation}"
    print(location + ":::" + rlocation)
    if turn:
        if location in grid.keys():
            grid[location]+= 1
        else:
            grid.update({location: 1})
    else:
        if rlocation in grid.keys():
            grid[rlocation]+= 1
        else:
            grid.update({rlocation: 1})
    turn = not turn

print(grid)
print(len(grid))
    

