 # Escape sequence characters

 # \n --> new line
 # \b --> backspace
 # \t --> tab

print('Hello World')
print('Hello\nWorld')
print('Hello\tWorld')
print('Hello\bWorld')

# dir = "c:\poru\n.txt"
# dir = 'c:\poru\n.txt'
dir = r'c:\poru\n.txt'  # here we have used the 'r' raw, to avoid the conversion of escape sequence character
print(dir)

# this 'r' concept used in --> API automation, web automation and file path
# to get the directory names then we use the 'r'


# can we use single quote and double quote both in python --> Yes

name = "Sachin Tendulkar"
name2 = 'Sachin Tendulkar'
print(name)
print(name2)

# name3 = 'Virat 'Kohli' --> with single quote we can not use single quote within signle quotes
# print(name3)


name4 = "Virat 'Kohli" # with double quotes we can use single quote within
print(name4)

# to use single quote within single quote, we have to use escape sequence concept
# how so
name5 = 'virat \'kohli'  # that's how we can use single quote within single quotes
print(name5)
