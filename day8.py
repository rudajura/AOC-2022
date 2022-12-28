inputArr = []
inputSeen = []
totalCount = 0
scenicScore = 0

for line in open("day8.in").read().splitlines():
    inputArr.append(line)

def visibility():
    global inputArr
    global inputSeen
    global totalCount
    #top
    for j in range(1, len(inputArr[0]) - 1):    #columns
        for i in range(1, len(inputArr) - 1):   #rows
            for k in range(0, i + 1):
                if k == i and inputSeen[i][j] == False:
                    inputSeen[i][j] = True
                    totalCount += 1
                elif inputArr[i][j] <= inputArr[k][j]:
                    break
    #bottom
    for j in range(1, len(inputArr[0]) - 1):              #columns
        for i in reversed(range(1, len(inputArr) - 1)):   #rows
            for k in reversed(range(i, len(inputArr))):
                if k == i and inputSeen[i][j] == False:
                    inputSeen[i][j] = True
                    totalCount += 1
                elif inputArr[i][j] <= inputArr[k][j]:
                    break
    #left
    for i in range(1, len(inputArr) - 1):           #rows
        for j in range(1, len(inputArr[0]) - 1):    #columns
            for k in range(0, j + 1):
                if k == j and inputSeen[i][j] == False:
                    inputSeen[i][j] = True
                    totalCount += 1
                elif inputArr[i][j] <= inputArr[i][k]:
                    break
    #right
    for i in range(1, len(inputArr) - 1):                   #rows
        for j in reversed(range(1, len(inputArr[0]) - 1)):  #columns
            for k in reversed(range(j, len(inputArr[0]))):
                if k == j and inputSeen[i][j] == False:
                    inputSeen[i][j] = True
                    totalCount += 1
                elif inputArr[i][j] <= inputArr[i][k]:
                    break

def scenic():
    global inputArr
    global inputSeen
    global scenicScore

    for j in range(1, len(inputArr[0]) - 1):    #columns
        for i in range(1, len(inputArr) - 1):   #rows
            if inputSeen[i][j]:
                tmpScenic = 1
                #top
                for k in reversed(range(-1, i)):
                    if k == 0:
                        tmpScenic *= i - k
                        break
                    elif inputArr[k][j] >= inputArr[i][j]:
                        tmpScenic *= i - k
                        break
                #bottom
                for k in range(i + 1, len(inputArr)):
                    if k == len(inputArr) - 1:
                        tmpScenic *= k - i
                        break
                    elif inputArr[k][j] >= inputArr[i][j]:
                        tmpScenic *= k - i
                        break
                #left
                for k in reversed(range(-1, j)):
                    if k == 0:
                        tmpScenic *= j - k
                        break
                    if inputArr[i][k] >= inputArr[i][j]:
                        tmpScenic *= j - k
                        break
                #right
                for k in range(j + 1, len(inputArr[0])):
                    if k == len(inputArr[0]) - 1:
                        tmpScenic *= k - j
                        break
                    if inputArr[i][k] >= inputArr[i][j]:
                        tmpScenic *= k - j
                        break
                if tmpScenic > scenicScore:
                    scenicScore = tmpScenic

inputSeen = [[False] * len(inputArr[0]) for i in range(len(inputArr))]
totalCount += len(inputArr) * 2 + (len(inputArr[0]) - 2) * 2
visibility()
scenic()
print(totalCount)
print(scenicScore)
