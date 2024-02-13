import sys


print(sys.argv)
if sys.argv[1] == "-e":
    f = open(sys.argv[2])
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    content = lines[0]

#cut into 11-length strings
cutlines = []
start = 0
for j in range(len(content)):
    if j != 0 and j % 11 == 0:
        cutlines.append(content[start:j])
        start = j
    if j == len(content)-1:
        cutlines.append(content[start:])
print(cutlines)

#separating a row into a char
for i in range(len(cutlines)):
    cutlines[i] = list(cutlines[i])
print(cutlines)

#transform into matrix
matrix = [[0]*6 for i in range(11)]
for i in range(len(cutlines[0])):
    for j in range(len(cutlines)):
        print(j)
        try:
            matrix[i][j] = cutlines[j][i]
        except:
            pass
    print(matrix[i])
    


