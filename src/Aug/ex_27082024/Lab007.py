# Lambda expression
import math
from os import times_result


def triple_me(number):
    print(number ** 3)

triple_me(10)


tripe = lambda num: num ** 3

print(f"we are doing this using lambda: {tripe(10)}")
print()

def sum_three_number(a, b, c):
    return a + b + c

three_addition = sum_three_number(1,2,3)
print(three_addition)

three_add = lambda a, b, c: a + b + c
print(f"we are doing this using lambda: {three_add(1,2,3)}")

print("======================================================================================")
print("======================================================================================")

# Create a function to tell even and odd number

def even_or_odd(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")


even_odd = lambda numb: "Even" if numb % 2 == 0 else "Odd"

print(even_odd(21))

print()
print()

# function to find the power of a number

def give_me_power(number1):

    return math.pow(number1, 2)

print(give_me_power(3))

# give me power of a number by lambda function


power_of_number = lambda: math.pow(int(input("enter number: ")), 2)

print(power_of_number())



































