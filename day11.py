import math as math

f = open("day11.in", "r")
for totalMonkeysCount, line in enumerate(f):
    pass

f = open("day11.in", "r")

totalMonkeysCount = round(totalMonkeysCount / 7)
monkeyCount = -1
saveParam = 3   #0 for items, 1 for operation, 2 for test, 3 for rest
opCount = 0
operation = ""
itemLen = 0
tmpItemWorry = 0
part = 1

monkeyItems = [[] for i in range(totalMonkeysCount)]

#every monkey will have 4 parameters stored
#operation = [monkeyCount][0]
#test divisible = [monkeyCount][1]
#test true = [monkeyCount][2]
#test false = [monkeyCount][3]
monkeyOp = [[] for i in range(totalMonkeysCount)]   

monkeyInspectCount = [0 for i in range(totalMonkeysCount)]

#store input from file
for line in f:
    for word in line.split():
        # print(word)
        if word == "Monkey":
            monkeyCount += 1
        elif word == "items:":
            saveParam = 0
        elif word == "=":
            saveParam = 1
        elif word == "by":
            saveParam = 2
        elif word == "Operation:":
            saveParam = 3
        elif word == "monkey":
            saveParam = 2

        elif saveParam == 0:
            monkeyItems[monkeyCount].append(int(word.replace(',', '')))

        elif saveParam == 1 or saveParam == 2:
            if saveParam == 1 and opCount == 3:
                monkeyOp[monkeyCount].append(operation)
                operation = ""
                saveParam = 3
                opCount = 0
            elif saveParam == 1 and opCount < 3:
                operation += str(word)
                opCount += 1
            elif saveParam == 2:
                saveParam = 3
                monkeyOp[monkeyCount].append(word)
        else:
            saveParam = 3
            continue

monkeyCount = -1

totalCount = 1
for i in range(totalMonkeysCount):
    totalCount *= int(monkeyOp[i][1])

for round in range(20 if part == 1 else 10000):
    for monkey in monkeyItems:
        monkeyCount += 1
        for item in monkey:
            for i in range(len(monkeyItems[monkeyCount])):
                tmpItemWorry = eval((monkeyOp[monkeyCount][0]).replace("old", str(monkeyItems[monkeyCount][0])))
                del monkeyItems[monkeyCount][0]
                if part == 1:
                    tmpItemWorry = math.floor(tmpItemWorry / 3)
                else:
                    tmpItemWorry = math.floor(tmpItemWorry % totalCount)
                if tmpItemWorry % int(monkeyOp[monkeyCount][1]) == 0:
                    monkeyItems[int(monkeyOp[monkeyCount][2])].append(tmpItemWorry)
                else:
                    monkeyItems[int(monkeyOp[monkeyCount][3])].append(tmpItemWorry)
                monkeyInspectCount[monkeyCount] += 1

    monkeyCount = -1

monkeyBusinessLevel = sorted(monkeyInspectCount)[-1] * sorted(monkeyInspectCount)[-2]
print(monkeyBusinessLevel)
