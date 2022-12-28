import numpy as np

headPos = [0, 0]
tailPos = [0,0]
allPos = [[0] * 2 for i in range(9)]
tailMoves = [[0, 0]]
tailMoves2 = [[0, 0]]

class Position:
    def tailMove():
        global headPos
        global tailMoves
        global tailPos
        if Position.isAdjacent(headPos, tailPos) == False:
            tmpX = Position.getNum(headPos[0] - tailPos[0])
            tmpY = Position.getNum(headPos[1] - tailPos[1])
            tailPos[0] += tmpX
            tailPos[1] += tmpY
            tailMoves.append(tailPos.copy())

    def allMove():
        global headPos
        global allPos
        global tailMoves2
        for i in range(9):
            if i == 0:
                if Position.isAdjacent(headPos, allPos[i]) == False:
                    tmpX = Position.getNum(headPos[0] - allPos[i][0])
                    tmpY = Position.getNum(headPos[1] - allPos[i][1])
                    allPos[i][0] += tmpX
                    allPos[i][1] += tmpY
            else:
                if Position.isAdjacent(allPos[i-1], allPos[i]) == False:
                    tmpX = Position.getNum(allPos[i-1][0] - allPos[i][0])
                    tmpY = Position.getNum(allPos[i-1][1] - allPos[i][1])
                    allPos[i][0] += tmpX
                    allPos[i][1] += tmpY
            if i == 8:
                tailMoves2.append(allPos[i].copy())

    def isAdjacent(headPos, tailPos):
        return abs(headPos[0] - tailPos[0]) <= 1 and abs(headPos[1] - tailPos[1]) <= 1

    def getNum(n):
        if n == 0:
            return 0
        elif n > 0:
            return 1
        elif n < 0:
            return -1

for line in open("day9.in").read().splitlines():
    x, y = line.split()
    if x == "U":
        for i in range(1, int(y) + 1):
            headPos[0] -= 1
            Position.tailMove()
            Position.allMove()
    elif x == "D":
        for i in range(1, int(y) + 1):
            headPos[0] += 1
            Position.tailMove()
            Position.allMove()
    elif x == "L":
        for i in range(1, int(y) + 1):
            headPos[1] -= 1
            Position.tailMove()
            Position.allMove()
    elif x == "R":
        for i in range(1, int(y) + 1):
            headPos[1] += 1
            Position.tailMove()
            Position.allMove()

t1 = list(set(map(tuple, tailMoves)))
t2 = list(set(map(tuple, tailMoves2)))

print(len(t1))
print(len(t2))
