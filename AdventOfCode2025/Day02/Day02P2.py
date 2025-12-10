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
        good = False
        for plen in range(1, (len(num_str)//2)+1):
            pattern = num_str[0:plen]
            repetitions = len(num_str)//plen
            if(pattern * repetitions != num_str):
                continue
            check_loc = plen
            while(check_loc <= len(num_str)):
                if num_str[check_loc:check_loc+plen] != pattern:
                    break
                check_loc += plen
                if check_loc == len(num_str):
                    good = True
        if good:
            count += num

print(count)
