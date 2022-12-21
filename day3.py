import itertools as it

f = open("day3.in", "r")

part = 1
totalPriority = 0
lineCount = 0
linesArr = []

for line in f.readlines():
    str1 = line[ : int(len(line) / 2)]
    str2 = line[int(len(line) / 2) : ]  
    if part == 1:
        for i, j in it.product(str1, str2):
            if i == j:
                if i.islower():
                    totalPriority += ord(i) - 96
                    print(ord(i) - 96)
                    break
                else:
                    totalPriority += ord(i) - 38
                    print(ord(i) - 38)
                    break
    if part == 2:
        linesArr.append(line)
        lineCount += 1
        if lineCount == 3:
            for i, j, k in it.product(linesArr[0], linesArr[1], linesArr[2]):
                if i == j == k:
                    if i.islower():
                        totalPriority += ord(i) - 96
                        print(ord(i) - 96)
                        break
                    else:
                        totalPriority += ord(i) - 38
                        print(ord(i) - 38)
                        break
            linesArr = []
            lineCount = 0

print(totalPriority)
