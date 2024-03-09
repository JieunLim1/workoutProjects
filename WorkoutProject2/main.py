def __valid(num):
    if type(num) is int:
        return True
    else:
        False

def cryptographic(lst):
        # encryption
        if lst[1] == "-e":
            f = open(lst[2])
            lines = f.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].strip()
            content = lines[0]
            total = len(content)
            f.close()

            #cut into 11-length strings
            cutlines = []
            key = int(lst[-1])
            start = 0
            for j in range(len(content)):
                if j != 0 and j % key == 0:
                    cutlines.append(content[start:j])
                    start = j
                if j == len(content)-1:
                    cutlines.append(content[start:])

            #separating a row into a char
            for i in range(len(cutlines)):
                cutlines[i] = list(cutlines[i])

            #transform into matrix

            clength = len(cutlines)
            matrix = [[0]*clength for i in range(11)]
            for i in range(len(cutlines[0])):
                for j in range(len(cutlines)):
                    try:
                        matrix[i][j] = cutlines[j][i]
                    except:
                        pass

            #check if there's 0  in the last row
                for index in range(len(matrix[-1])):
                    if matrix[-1][index] == 0:
                        matrix[-1][index] = ' '

            encrypted = ''
            for i in range(len(matrix)):
                    joined = ''.join(matrix[i])
                    encrypted += joined
                
            #write it into a file
            f = open(lst[3],'w')
            f.write(encrypted)
            f.close()



            #decryption
        elif lst[1] == '-d':
            f = open(lst[2])
            lines = f.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].strip()
            content = lines[0]
            f.close()
            total = len(content)
            key = int(lst[-1])
            remain = total % key
            clength = 0
            if remain == 0:
                clength = total // key
            else:
                clength = total // key
                clength += 1
            # key
            spacenum = total % clength

            #cut into column
            cutlines = []
            start = 0
            for j in range(len(content)):
                if j != 0 and j % clength == 0:
                    cutlines.append(content[start:j])
                    start = j
                if j == len(content)-1:
                    cutlines.append(content[start:])

            #separate each string into a single char
            for i in range(len(cutlines)):
                cutlines[i] = list(cutlines[i])
            #transform
            matrix = [[0]*len(cutlines) for i in range(clength)]
            for i in range(len(cutlines[0])):
                for j in range(len(cutlines)):
                    try:
                        matrix[i][j] = cutlines[j][i]
                    except:
                        pass

            # check zero
            for i in range(len(matrix[0])):
                if matrix[-1][i] == 0:
                    matrix[-1][i] = ""

            #joining
            original = ''
            for i in range(len(matrix)):
                joined = ''.join(matrix[i])
                original += joined


            #writing it on a file
            f = open(lst[3],'w')
            f.write(original)
            f.close()