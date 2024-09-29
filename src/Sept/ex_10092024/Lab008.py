'''File Handling'''
'''File Reading'''
from importlib.resources import contents

# Please refer old notes

try:
    with open("file1.txt", "r") as f:
        content = f.readlines()  # it will print one single line  # read() ==> prints all the content
except FileNotFoundError as FiN:
    print(FiN)
else:
    print(content)
finally:
    try:
        f.close()
        print("file closed")
    except NameError as Na:
        print(Na)