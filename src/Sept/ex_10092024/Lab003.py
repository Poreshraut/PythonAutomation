import os

print("here also we will learn try, except, else, and finally block")

try:
    print(os.getcwd())
    file = open("C:/Users/91703/PycharmProjects/PyATB4xLearning/src/Sept/ex_10092024/example.txt", "r")
    file1 = file.read()
    print(file1)
except FileNotFoundError as f:
    print(f"{f} please provide correct path of the file or create file")
else:
    print(file1)
finally:
    try:
        file.close()
    except Exception as e:
        print(f"{e}, please correct code")
