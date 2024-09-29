def my_decorator1(func):
    def wrapper():
        print("launching my decorator 1...")
        func()
    return wrapper  # Return the wrapper function itself, not its result

def my_decorator2(func):
    def wrapper():
        print("launching my decorator 2...")
        func()
    return wrapper  # Return the wrapper function itself, not its result

@my_decorator1
@my_decorator2
def my_function():
    print("testing functionality")

my_function()


emi_interest = 163.62
gst = 29.45
emi_principal = 789.95
print(emi_interest+emi_principal+gst)