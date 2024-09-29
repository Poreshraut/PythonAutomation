print("here we will learn about os module")
'''
==> If it prints nt, it means you're on a Windows system. "NT" refers to Windows NT, which is a core part of the Windows operating system family.
==> If it prints posix, it means you're on a Unix-like system, such as Linux or macOS.'''
import os
print(os.name) # When you run print(os.name), it tells you which kind of operating system your Python script is running on

if os.name == "nt":
    print("Working on Windows")
else:
    print("linux or mac")

print(os.getcwd())
# os.chdir("C:/Users/91703/PycharmProjects/PyATB4xLearning/src/Sept/ex_10092024/example2.txt")
print(os.listdir())
for file in os.listdir():
    print(file)
# os.chdir("C:/Users/91703/PycharmProjects/PyATB4xLearning/src/Sept/ex_10092024/example3.txt")
# os.remove("example3.txt")
print("================================================================28th Sept==================================================")

print(os.name)

if os.name == "nt":
    print("working on Windows")
else:
    print("working on Linux or macOS")

print(os.getcwd())
print(os.listdir()) # it will display all the files and folder this directory contains

for file in os.listdir():
    print(file)
    if file == "Lab001.py":
        break
print(os.path)

full_path1 = os.path.join("C:/Users/91703/PycharmProjects/PyATB4xLearning/src/Sept/ex_10092024", "file.txt")
print(full_path1)

print(os.path.isfile("C:/Users/91703/PycharmProjects/PyATB4xLearning/src/Sept/ex_10092024/example2.txt"))
print(os.path.exists("C:/Users/91703/PycharmProjects/PyATB4xLearning/src/Sept/ex_10092024/example4.txt"))
print(os.path.isdir("C:/Users/91703/PycharmProjects/PyATB4xLearning/src/Sept/ex_10092024/example2.txt"))



