f = open("day2.in", "r")

totalScore = 0
part = 1

for line in f.readlines():
    if part == 1:
        if line[0] == "A":
            if line[2] == "X":
                totalScore += 4
            elif line[2] == "Y":
                totalScore += 8
            elif line[2] == "Z":
                totalScore += 3
        elif line[0] == "B":
            if line[2] == "X":
                totalScore += 1
            elif line[2] == "Y":
                totalScore += 5
            elif line[2] == "Z":
                totalScore += 9
        elif line[0] == "C":
            if line[2] == "X":
                totalScore += 7
            elif line[2] == "Y":
                totalScore += 2
            elif line[2] == "Z":
                totalScore += 6
    elif part == 2:
        if line[0] == "A":
            if line[2] == "X":
                totalScore += 3
            elif line[2] == "Y":
                totalScore += 4
            elif line[2] == "Z":
                totalScore += 8
        elif line[0] == "B":
            if line[2] == "X":
                totalScore += 1
            elif line[2] == "Y":
                totalScore += 5
            elif line[2] == "Z":
                totalScore += 9
        elif line[0] == "C":
            if line[2] == "X":
                totalScore += 2
            elif line[2] == "Y":
                totalScore += 6
            elif line[2] == "Z":
                totalScore += 7

print(totalScore)