f = open("day6.in", "r")

part = 1
line = f.readline()
count = 1

for i in line:
    tmpStr = line[count : (count + 4 if part == 1 else count + 14)]
    sortedStr = ''.join(sorted(set(tmpStr)))
    if (len(sortedStr) != 4 and part == 1) or (len(sortedStr) != 14 and part == 2):
        count += 1
    else:
        print(count + 4 if part == 1 else count + 14)
        break