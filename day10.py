f = open("day10.in", "r")

i = 1
carrySum = 1
totalSum = 0
position = 0

spritePos = "###....................................."
resultPos = ""

for line in f:
    for word in line.split():
        if i == 20:
            totalSum += carrySum * 20
        elif (i-1) % 40 == 0:
            resultPos += "\n"
            position = 0
        elif i == 60:
            totalSum += carrySum * 60
        elif i == 100:
            totalSum += carrySum * 100
        elif i == 140:
            totalSum += carrySum * 140
        elif i == 180:
            totalSum += carrySum * 180
        elif i == 220:
            totalSum += carrySum * 220
    
        if word == "noop":
            resultPos += spritePos[position]
            i += 1
            position += 1
        elif word == "addx": 
            resultPos += spritePos[position]
            i += 1
            position += 1
        else:
            resultPos += spritePos[position]
            i += 1
            carrySum += int(word)
            spritePos = ("."*((carrySum-1)%40)) + ("#"*3) + ("."*(38-carrySum%40))
            position += 1

print(totalSum)
print(resultPos)
