f = open("day4.in", "r")

part = 1
elfs = []
sections = []
overlapsCount = 0

for line in f.readlines():
    elfs = line.split(",")
    for section in elfs:
        sections.append(section.split("-"))
    if ((int(sections[0][0]) >= int(sections[1][0]) and int(sections[0][1]) <= int(sections[1][1])) 
        or (int(sections[0][0]) <= int(sections[1][0]) and int(sections[0][1]) >= int(sections[1][1]))):
        overlapsCount += 1
    elif part == 2:
        if ((int(sections[0][0]) >= int(sections[1][0]) and int(sections[0][1]) <= int(sections[1][1])) 
            or (int(sections[0][0]) <= int(sections[1][0]) and int(sections[0][1]) >= int(sections[1][1]))
            or (int(sections[0][1]) >= int(sections[1][0]) and int(sections[0][1]) <= int(sections[1][1])) 
            or (int(sections[0][0]) >= int(sections[1][0]) and int(sections[0][0]) <= int(sections[1][1]))):
            overlapsCount += 1
    sections = []
print(overlapsCount)