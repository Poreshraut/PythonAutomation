from calendar import error

print("here we will learn about the exception handling")
# An unwanted and unexpected event which disrupts the normal flow of the program
# Error and Exception: both are mechanism in python which indicates the problem in the program
# All the exceptions are nothing but a class (ex. Arithemetic exception, OSError, FileNotFound Error)
# Exception is a class which contains all the type of exception / classes

print("--- start of the program ---")
a = int(input("enter first value: "))
b = int(input("enter second value: "))
c = a / b
print(f"Result of expression: {c}")
print("--- end of the program ---")

print("==== now we will use this code in try and except block ===")
print("--- start of the code ---")
try:
    ab = int(input("enter first value: "))
    bc = int(input("enter second value: "))
    cd = ab / bc
    print(f"Result of the expression: {cd}")
except Exception as e:
    print(e)
    print("please provide correct values")
print("--- end of the code ---")

# try:
#     code to be executed, if error
# except Exception as e:
#     execute me if try has error or exception