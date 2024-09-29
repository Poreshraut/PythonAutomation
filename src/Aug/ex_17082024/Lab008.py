### Task #3
# - Explain the difference between the = operator and the == operator in Python.
'''
= operator is called as assignment operator
= operator assign literal to the identifier
= operator assign value from right to left
== operator is called as comparison operator
== operator does the comparison between values
'''
import math

# - What does the ** operator do in Python, and how is it used?
'''
** operator it works as same as pow() function
ex. 2 raised to the power 3 = 8 (2**3=8)
'''
# - What does the ^ operator do in Python, and in what context is it commonly used?
'''
In Python, the ^ operator is the bitwise XOR (exclusive OR) operator. It operates on the binary representations of integers. 
Here's how it works:
Bitwise XOR (^): It compares each bit of its operands. If the bits of the operands are different, the resulting bit is set to 1. 
If the bits are the same, the resulting bit is set to 0.
0 ^ 0 = 0
1 ^ 1 = 0
0 ^ 1 = 1
1 ^ 0 = 1
'''
# ex. for ^ operator
a = 5 # 0101
b = 3 # 0011
print(a ^ b) # 0110

### Task #4
# - Write a Python program to calculate the area of a circle given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)
# step1: figure out the input and output
# step2: write rough logic
# step3: write logic
'''
input: value of pi? ==> 3.14 or math.pi, radius is in float or int?, for power what to use ==> pow(x,y) or **
output: is in float or int?
rough logic: area = math.pi*10**2 or area = 3.14*pow(10,2)
'''
r = float(input("Enter the radius of the circle: "))
area1 = math.pi*pow(r,2)
area2 = 3.14*r**2
print(f"the area of the circle is: {area1:.2f}")
print(area2)
# print(3.141592653589793*(float(input("Enter the radius\n"))**2))

### Task #5
# - Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second
# number.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# First way:
if num1 == num2:
    print("First number is equal to the second number")
elif num1 > num2:
    print("First number is greater than then second number")
else:
    print("First number is less than the second number")

# Second way:
if num1 == num2:
    print("First number is equal to the second number")
if num1 > num2:
    print("First number is greater than then second number")
if num1 < num2:
    print("First number is less than the second number")

### Task #6
# - Develop a Python script that calculates the square and cube of a given number.

given_number = int(input("Enter the number: "))
print(f"the square of {given_number} is: {given_number**2}")
print(f"the cube of {given_number} is: {given_number**3}")