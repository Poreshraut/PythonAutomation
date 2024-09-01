# We can do chaining of the decorators
from wsgiref.util import request_uri

from src.ex_27082024.Lab002 import my_function1


def my_decorator1(func):
    def wrapper():
        print(f"launching my decorator 1...")
        func()
    return wrapper()

def my_decorator2(func):
    def wrapper():
        print(f"launching my decorator 2...")
        func()
    return wrapper()

@my_decorator1
@my_decorator2
def my_function():
    print("testing functionality")

my_function()

