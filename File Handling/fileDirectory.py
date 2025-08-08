import os

fileName = "fileDir.txt"
try:
    os.makedirs(fileName)
except OSError as e:
    print(f"Directory '{fileName}' already exists. \n{e}")
try:
    os.mkdir('newDir')
except OSError as e:
    print(f"Directory 'newDir' already exists. \n{e}")

print(os.getcwd())

print(os.listdir(os.getcwd()))

os.chdir(os.getcwd() + "/newDir")
os.chdir('/Users/arpitpardesi/Programming/Python/Restart/Python Practice/File Handling')
print(os.getcwd())

os.rmdir('newDir')