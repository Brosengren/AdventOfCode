def read_input(filename):
    with open(filename) as f:
        return [x.strip() for x in f]

inputs = read_input("Day04IN.txt")

shelf = []
for line in inputs:
    line = "." + line + "."
    shelf.append(line)
new_line = "."*len(shelf[0])
shelf.append(new_line)
shelf.insert(0, new_line)

count = 0
for x in range(1, len(shelf)-1):
    for y in range(0, len(shelf[x])):
        if shelf[x][y] == "@":
            # print(f"{x},{y}")
            a_count = -1
            for j in range((x-1), (x+2)):
                for k in range((y-1), (y+2)):
                    if shelf[j][k] == "@":
                        # print(f"adding: {j},{k}")
                        a_count += 1
            if a_count < 4:
                count += 1
                # print(f"Count: {count}")

print(count)