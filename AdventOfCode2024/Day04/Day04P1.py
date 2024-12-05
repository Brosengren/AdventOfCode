from pathlib import Path
filename = Path(__file__).parent.__str__() + "/Day04IN.txt"
with open(filename) as f:
    raw_input = [x for x in f]

x = 'X'
m = 'M'
a = 'A'
s = 'S'
count = 0

for i in range(len(raw_input)):
    for j in range(len(raw_input[i])):
        if raw_input[i][j] == x:
            try:
                if raw_input[i-1][j-1] == m and raw_input[i-2][j-2] == a and raw_input[i-3][j-3] == s:
                    count += 1
            except:pass
            try:
                if raw_input[i-1][j] == m and raw_input[i-2][j] == a and raw_input[i-3][j] == s:
                    count += 1
            except:pass
            try:
                if raw_input[i-1][j+1] == m and raw_input[i-2][j+2] == a and raw_input[i-3][j+3] == s:
                    count += 1
            except:pass
            try:
                if raw_input[i][j-1] == m and raw_input[i][j-2] == a and raw_input[i][j-3] == s:
                    count += 1
            except:pass
            try:
                if raw_input[i][j+1] == m and raw_input[i][j+2] == a and raw_input[i][j+3] == s:
                    count += 1
            except:pass
            try:
                if raw_input[i+1][j-1] == m and raw_input[i+2][j-2] == a and raw_input[i+3][j-3] == s:
                    count += 1
            except:pass
            try:
                if raw_input[i+1][j] == m and raw_input[i+2][j] == a and raw_input[i+3][j] == s:
                    count += 1
            except:pass
            try:
                if raw_input[i+1][j+1] == m and raw_input[i+2][j+2] == a and raw_input[i+3][j+3] == s:
                    count += 1
            except:pass
print(count)