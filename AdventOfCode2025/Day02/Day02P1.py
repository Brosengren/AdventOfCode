def read_input(filename):
    with open(filename) as f:
        return [x for x in f]

inputs = read_input("Day02IN.txt")
unchecked_ranges = [x for x in inputs[0].split(",")]

count = 0

for id_ranges in unchecked_ranges:
    start = int(id_ranges.split("-")[0])
    end = int(id_ranges.split("-")[1])
    for num in range(start, end+1):
        num_str = str(num)
        if(len(num_str) % 2 == 0):
            first_half = num_str[0:int(len(num_str)/2)]
            second_half = num_str[int(len(num_str)/2):len(num_str)]
            if(first_half == second_half):
                count += num
print(count)
