from itertools import chain

f = open("day7.in", "r")

actualDirName = ""
parentDirName = ""
totalCountDirSize = 0
smallestDirToDelete = []
rootSize = 0

class Dir:
    def __init__(self, key):
        self.name = key
        self.childDir = []
        self.size = 0
        self.parent = None

    def printTree(self):
        global totalCountDirSize
        global smallestDirToDelete
        global rootSize
        space = '-' * self.getLevel()
        print(space + self.name)
        totalSize = self.totalSize()
        if self.name == "/":
            rootSize = totalSize
        if totalSize >= rootSize - 40000000:
            smallestDirToDelete.append(totalSize)
        if totalSize <= 100000:
            totalCountDirSize += totalSize
        print(space + str(totalSize))

        if self.childDir:
            for child in self.childDir:
                child.printTree()

    def totalSize(self):
        totalCount = self.size
        if self.childDir:
            for child in self.childDir:
                tmpTotalSize = child.totalSize()
                if tmpTotalSize != None:
                    totalCount += tmpTotalSize
        return totalCount

    def addChild(self, child):
        child.parent = self
        self.childDir.append(child)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def searchDir(self, key):
        if self.childDir:
            for child in self.childDir:
                if child.name == key:
                    return child
        
def newDir(key):
    tmp = Dir(key)
    return tmp

root = newDir("/")
tmpDir = root

for line in f.readlines():
    line = line.split()
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                if tmpDir != None:
                    tmpDir = tmpDir.parent
            elif line[2] == "/":
                tmpDir = root
                actualDirName = root.name
            else:
                parentDirName = actualDirName
                actualDirName = line[2]
                if tmpDir != None:
                    tmpDir = Dir.searchDir(tmpDir, actualDirName)
    elif line[0].isnumeric():
        if tmpDir != None:
            tmpDir.size += int(line[0])
    elif line[0] == "dir":
        if tmpDir != None:
            tmpDir.addChild(newDir(line[1]))

print(Dir.printTree(root))

print(totalCountDirSize)
print(min(smallestDirToDelete))