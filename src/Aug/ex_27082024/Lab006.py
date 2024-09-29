def decorator1(func):
    def wrapper():
        print("decorator 111111111111111111")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("decorator 222222222222222222")
        func()
    return wrapper

@decorator1
@decorator2
def my_function():
    print("testing...")

my_function()

"""



decorator 111111111
decorator 2222222222222
testing....
"""