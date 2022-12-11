f = open("day1.txt", "r")

sum = 0
sumList = []

for line in f.readlines():
    if line.strip():
        sum += int(line)
    else:
        sumList.append(int(sum))
        sum = 0

print(sorted(sumList)[-1])  #part 1
print(sorted(sumList)[-1] + sorted(sumList)[-2] + sorted(sumList)[-3])  #part2