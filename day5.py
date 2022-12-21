f = open("day5.in", "r")

part = 1
saveLines = True
linesTmp = []
stackArr = []
stackIndex = 1
spaceCount = 0
resultStr = ""

for line in f.readlines():
    if line[0] == "\n":
        continue
    elif line[1].isnumeric():
        saveLines = False
        stackCount = len(line.split())
        for i in range(stackCount + 1):
            stackArr.append([])
        for floor in reversed(linesTmp):
            for char in floor:
                if char == " ":
                    spaceCount += 1
                elif char.isalpha():
                    stackIndex = int(stackIndex + (spaceCount // 4))
                    stackArr[stackIndex].append(char)
                    spaceCount = 0
                    stackIndex += 1
                elif char == '\n':
                    stackIndex = 1
                    spaceCount = 0
    elif saveLines:
        linesTmp.append(line)
    elif line.split()[0] == "move":
        if part == 1:
            for i in range(int(line.split()[1])):
                stackArr[int(line.split()[5])].append(stackArr[int(line.split()[3])].pop())
        else:
            for i in reversed(range(int(line.split()[1]))):
                stackArr[int(line.split()[5])].append(stackArr[int(line.split()[3])].pop(int(len(stackArr[int(line.split()[3])]) -i -1)))

for i in range(1, len(stackArr)):
    resultStr += stackArr[i].pop()

print(resultStr)