from pathlib import Path
filename = Path(__file__).parent.__str__() + "/Day04IN.txt"
with open(filename) as f:
    puz = [x.strip() for x in f]

m = 'M'
a = 'A'
s = 'S'
count = 0

for i in range(len(puz)):
    for j in range(len(puz[i])):
        if i == 0 or i == len(puz)-1 or j == 0 or j == len(puz[i])-1:
            continue
        if puz[i][j] == a:
            ul = puz[i-1][j-1]
            ur = puz[i-1][j+1]
            ll = puz[i+1][j-1]
            lr = puz[i+1][j+1]
            if (
               (ul == m and ur == m and lr == s and ll == s)
            or (ul == s and ur == m and lr == m and ll == s)
            or (ul == s and ur == s and lr == m and ll == m)
            or (ul == m and ur == s and lr == s and ll == m)
            ):
                count += 1
         
print(count)
