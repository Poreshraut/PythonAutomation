'''
Home Work Task | 13th Aug 2024
Task #1
# Home Can you create a Program I will give you number(userinput and print table)
f"{}" String format concept
User input - num int -> 10, 100, -1, 2, 3.14 -> input
9x1 = 9
9x2 = 18... till 10
Task #2
Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}
You need to share this via the GITHUB repo.
'''
# First Task
number = int(input("Enter a number for table: "))
print(f"{number}*1 = {number*1}")
print(f"{number}*2 = {number*2}")
print(f"{number}*3 = {number*3}")
print(f"{number}*4 = {number*4}")
print(f"{number}*5 = {number*5}")
print(f"{number}*6 = {number*6}")
print(f"{number}*7 = {number*7}")
print(f"{number}*8 = {number*8}")
print(f"{number}*9 = {number*9}")
print(f"{number}*10 = {number*10}")

# Second Task
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"This is the maximum number from you provided: {max(num1, num2)}")
print(f"This is the power of first number: {pow(num1, num2)}")
print(f"Addition of the numbers you provided is: {num1+num2}")
print(f"Subtraction of the numbers you provided is: {num1-num2}")
print(f"Division of the numbers you provided is: {num1/num2}")
print(f"Multiplication of the numbers you provided is: {num1*num2}")

