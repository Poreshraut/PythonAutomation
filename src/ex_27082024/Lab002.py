global_variable = "Global Variable"

def my_function1():
    print(f"this is the global variable: {global_variable}")
    global local_variable
    local_variable = "local variable of my function1"
    print(f"this is the local variable of my function1: {local_variable}")

my_function1()

print(f"calling global variable outside: {global_variable}")

print(f"calling local variable of my function1 outside: {local_variable}")



