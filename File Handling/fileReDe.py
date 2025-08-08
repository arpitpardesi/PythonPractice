import os

fileLines = ['This is the first line\n', 'This is the second line\n', 'This is the third line\n', 'This is the fourth line\n']

with open("fileReDe.txt", "w") as file1:
    file1.writelines(fileLines)
    file1.close()

fileName = "fileReDe.txt"
newFileName = "fileReDeNew.txt"

os.rename(fileName, newFileName)
os.remove(newFileName)

