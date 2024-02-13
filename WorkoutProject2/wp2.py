import sys

# # encryption
# if sys.argv[1] == "-e":
#     f = open(sys.argv[2])
#     lines = f.readlines()
#     for i in range(len(lines)):
#         lines[i] = lines[i].strip()
#     content = lines[0]
#     f.close()

#     #cut into 11-length strings
#     cutlines = []
#     start = 0
#     for j in range(len(content)):
#         if j != 0 and j % 11 == 0:
#             cutlines.append(content[start:j])
#             start = j
#         if j == len(content)-1:
#             cutlines.append(content[start:])
#     print(cutlines)

#     #separating a row into a char
#     for i in range(len(cutlines)):
#         cutlines[i] = list(cutlines[i])
#     print(cutlines)

#     #transform into matrix
#     matrix = [[0]*6 for i in range(11)]
#     for i in range(len(cutlines[0])):
#         for j in range(len(cutlines)):
#             print(j)
#             try:
#                 matrix[i][j] = cutlines[j][i]
#             except:
#                 pass
#         print(matrix[i])

#     #check if there's 0  in the last row
#         for index in range(len(matrix[-1])):
#             if matrix[-1][index] == 0:
#                 matrix[-1][index] = ' '

#     encrypted = ''
#     for i in range(len(matrix)):
#             joined = ''.join(matrix[i])
#             encrypted += joined
#     print(encrypted)
        
# #write it into a file

#decryption
# if sys.argv[1] == '-d':
#     f = open(sys.argv[2])
#     lines = f.readlines()
#     for i in range(len(lines)):
#         lines[i] = lines[i].strip()
#     content = lines[0]
#     f.close()
content = 'T.P.aehUrwrsiCoie.sIgt.c..rhLoiIa.iusCmSbr.Smorst3ifaeh2ntr!e.gwi '
total = len(content)
# key = int(sys.argv[-1])
key = 11
clength = total // key # key
spacenum = total % clength

#cut into column
cutlines = []
start = 0
for j in range(len(content)):
    if j != 0 and j % clength == 0:
        cutlines.append(content[start:j+1])
        start = j
    if j == len(content)-1:
        cutlines.append(content[start:])
print(cutlines)

#separate each string into a single char
for i in range(len(cutlines)):
    cutlines[i] = list(cutlines[i])
print(cutlines)

#transform
matrix = [[0]*len(cutlines) for i in range(clength)]
for i in range(len(cutlines[0])):
    for j in range(len(cutlines)):
        print(j)
        try:
            matrix[i][j] = cutlines[j][i]
        except:
            pass

original = ''
for i in range(len(matrix)):
        joined = ''.join(matrix[i])
        original += joined
print(original)