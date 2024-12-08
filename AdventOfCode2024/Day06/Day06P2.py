from pathlib import Path
filename = Path(__file__).parent.__str__() + "/Day06IN.txt"
with open(filename) as f:
    raw_input = [list(x.strip()) for x in f]

def get_location() -> list[int]:
    for row in raw_input:
        if row.__contains__('^'):
            return [raw_input.index(row), row.index('^')]

starting_location = get_location()   
location = starting_location
x = 'X'
# raw_input[location[0]][location[1]] = x
direction = 0 #0up 1right 2down 3left
turn_list = [[-1,-1]]
count = 0

def turn():
    global direction
    global turn_list
    global count
    direction = (direction + 1) % 4
    if location in turn_list[:-1]:
        count += 1
        return True
    if location != turn_list[-1]:
        turn_list.append(location)
    return False

def move(new_location):
    global location
    global room
    global moved
    location = new_location
    room[location[0]][location[1]] = x
    moved = True

for row in range(len(raw_input)):
    for col in range(len(raw_input[row])):
        if raw_input[row][col] in '#^':
            continue
        
        direction = 0
        location = starting_location
        room = [x[:] for x in raw_input]
        room[row][col] = "#"
        turn_list = [[-1,-1]]

        looping = False
        in_room = True
        while in_room and not looping:
            moved = False
            while not moved:
                if direction == 0:
                    if location[0]-1 < 0:
                        in_room = False
                        break
                    new_loc = [location[0]-1,location[1]]
                    if room[new_loc[0]][new_loc[1]] == '#':
                        if turn():
                            looping = True
                            break
                    else:
                        move(new_loc)

                elif direction == 1:
                    if location[1]+1 == len(room[row]):
                        in_room = False
                        break
                    new_loc = [location[0],location[1]+1]
                    if room[new_loc[0]][new_loc[1]] == '#':
                        if turn():
                            looping = True
                            break
                    else:
                        move(new_loc)

                if direction == 2:
                    if location[0]+1 == len(room):
                        in_room = False
                        break
                    new_loc = [location[0]+1,location[1]]
                    if room[new_loc[0]][new_loc[1]] == '#':
                        if turn():
                            looping = True
                            break
                    else:
                        move(new_loc)

                if direction == 3:
                    if location[1]-1 < 0:
                        in_room = False
                        break
                    new_loc = [location[0],location[1]-1]
                    if room[new_loc[0]][new_loc[1]] == '#':
                        if turn():
                            looping = True
                            break
                    else:
                        move(new_loc)

print(count)
