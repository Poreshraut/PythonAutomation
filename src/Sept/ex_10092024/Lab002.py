print("here we will learn try, except and finally blocks")

try:
    a = int(input("enter first value: "))
    b = int(input("enter second value: "))
    c = a / b
    print(f"result: {c}")
except ValueError as v:
    print(f"{v} please don't enter string or float, it should be always integer")
except ZeroDivisionError as z:
    print(f"{z} please don't use 0 for second value")
else:
    print(f"Result: {c}")
finally:
    print("this code will always execute, eventhough there is error, exception or not")

