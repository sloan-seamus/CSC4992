#!/usr/bin/env python3
import datetime

def main():
    A = File("FileA")
    print("File A:\n")
    print("Name: ", A.getName())
    print("Owner: ", A.getOwner())
    print("Date: ", A.getDate())
    print("\nContent:")
    print(A.getContent())
    print("\nAdding line 'This is funny'...")
    print("\nContent:")
    A.addLine("This is funny")
    print(A.getContent())
    print("_________________________________\n")

    B = File("FileB", "This is content1")
    print("File B:\n")
    print("Name: ", B.getName())
    print("Owner: ", B.getOwner())
    print("Date: ", B.getDate())
    print("\nContent:")
    print(B.getContent())
    print("\nAdding line 'This is funny'...")
    print("\nContent:")
    B.addLine("This is funny")
    print(B.getContent())
    print("\nDeleting second line...")
    print("\nContent:")
    B.deleteLine(2)
    print(B.getContent())
    print("\nSearching for 'Content1'...")
    print("Found 'Content1': ", B.hasWord("Content1"))
    print("\nReplacing 'content1'...")
    B.replace("content1", "REPLACER!")
    print(B.getContent())
    print("_________________________________\n")

    C = File("FileC", "This is content2", "Seamus")
    print("File C:\n")
    print("Name: ", C.getName())
    print("Owner: ", C.getOwner())
    print("Date: ", C.getDate())
    print("\nContent:")
    print(C.getContent())
    print("\nAdding line 'This is funny'...")
    print("\nContent:")
    C.addLine("This is funny")
    print(C.getContent())
    print("\nDeleting first line...")
    print("\nContent:")
    C.deleteLine(1)
    print(C.getContent())
    print("\nSetting content to '5'...")
    print("\nContent:")
    C.setContent("5")
    print(C.getContent())
    print("_________________________________\n")


class File:
    fileName = ""
    fileOwner = "Unspecified"
    dateModified = ""
    fileNumber = 0

    def __init__(self, name, content=None, owner="Unspecified"):
        self.fileName = name + ".txt"
        self.modifyDate()
        self.fileOwner = owner
        temp = open(self.fileName, "w+")
        if content is not None:
            temp.write(content)
        temp.close()

    def getName(self):
        return self.fileName

    def setOwner(self, ownerName):
        self.fileOwner = ownerName
        self.modifyDate()

    def getOwner(self):
        return self.fileOwner

    def setDate(self, date):
        self.dateModified = date
        self.modifyDate()

    def getDate(self):
        return self.dateModified

    def modifyDate(self):
        self.dateModified = datetime.datetime.today()

    def countLines(self):
        temp = open(self.fileName, "r")
        length = len(temp.readlines())
        temp.close()
        return length

    def addLine(self, line):
        temp = open(self.fileName, "a+")
        if self.countLines() > 0:
            temp.write("\n%s" % line)
        else:
            temp.write(line)
        self.modifyDate()

    def deleteLine(self, lineNumber):
        temp = open(self.fileName, "r+")
        lines = temp.readlines()
        lines[lineNumber-1] = ''
        temp.truncate(0)
        for i in range(len(lines)):
            temp.write(lines[i])
        temp.close()

    def getContent(self):
        temp = open(self.fileName, "r")
        return temp.read()

    def setContent(self, content):
        temp = open(self.fileName, "w")
        temp.truncate()
        temp.write(content)
        temp.close()

    def hasWord(self, word):
        count = 0
        temp = open(self.fileName, "r")
        lines = temp.readlines()
        for line in lines:
            for lineWord in line.split():
                print(lineWord)
                if lineWord.upper() == word.upper():
                    count = count + 1
        if count > 0:
            return True
        else:
            return False


    def addFrom(self):
        print("Hello!")

    def countWord(self):
        print("Hello!")

    def replace(self, replacedWord, newWord):
        temp = open(self.fileName, "r+")
        lines = temp.readlines();
        for line in lines:
            for lineWord in line.split():
                if lineWord == replacedWord:
                    lineWord = newWord
        temp.truncate(0)
        for line in lines:
            temp.write(line)


if __name__ == '__main__':
    main()
