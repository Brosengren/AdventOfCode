from pathlib import Path
filename = Path(__file__).parent.__str__() + "/Day06IN.txt"
with open(filename) as f:
    raw_input = [list(x.strip()) for x in f]

def get_location() -> list[int]:
    for row in raw_input:
        if row.__contains__('^'):
            return [raw_input.index(row), row.index('^')]
        
location = get_location()
x = 'X'
raw_input[location[0]][location[1]] = x
direction = 0 #0up 1right 2down 3left

def turn():
    global direction
    direction = (direction + 1) % 4

def move(new_location):
    global location
    global raw_input
    location = new_location
    raw_input[location[0]][location[1]] = x


in_room = True
while in_room:
    moved = False
    while not moved:
        try:
            if direction == 0:
                new_loc = [location[0]-1,location[1]]
                if raw_input[new_loc[0]][new_loc[1]] == '#':
                    turn()
                else:
                    move(new_loc)

            elif direction == 1:
                new_loc = [location[0],location[1]+1]
                if raw_input[new_loc[0]][new_loc[1]] == '#':
                    turn()
                else:
                    move(new_loc)

            if direction == 2:
                new_loc = [location[0]+1,location[1]]
                if raw_input[new_loc[0]][new_loc[1]] == '#':
                    turn()
                else:
                    move(new_loc)

            if direction == 3:
                new_loc = [location[0],location[1]-1]
                if raw_input[new_loc[0]][new_loc[1]] == '#':
                    turn()
                else:
                    move(new_loc)
        except IndexError as e:
            in_room = False
            break

count = 0
for row in raw_input:
    count += row.count(x)
print(count)