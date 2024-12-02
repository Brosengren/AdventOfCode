# input = []
# with open("Day04INtest.txt") as f:
#     for line in f:
#         input.append(line.strip())

# #print(input)
# picks = input[0]

# boards = []
# board = []
# for i in range(2, len(input), 6):
#     for x in range(5):
#         board.append([int(y) for y in input[i+x].split(' ') if y != ''])
#     else:
#         if board != []:
#             boards.append(board)
#             board = []
# print(picks)
# print(boards)


# #set picks to -1
# for pick in picks:
#     for board in boards:
#         for line in board:
#             for i in range(len(line)):
#                 line[i] = -1
#     #check for bingo
#     for board in boards:
#         #check lines
#         for line in board:
#             if

import random

def create_rand():
    shapes = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven']
    randshapes = []

    for i in range(7):
        randshapes.append(shapes.pop(random.randint(0, len(shapes)-1)))
    return randshapes


sequence = []

while(len(sequence) < 25):
    for each in create_rand():
        sequence.append(each)

print(sequence)

while(len(sequence) > 25):
    sequence.pop()

print(sequence)
