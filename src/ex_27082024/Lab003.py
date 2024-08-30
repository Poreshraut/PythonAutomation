import time


def my_decorator(func):

    print("launching decorator.....")

    def wrapper():
        print("first")
        print("second")
        func()
        print("last")
    return wrapper()

@my_decorator
def my_function():
    print("testing is going on......")
print("*************************************************************")

# time calculator:

def my_decorator2(func):

    print("my decorator2 has been launched.....")
    def wrapper():

        start_time = time.time()
        func()
        end_time = time.time()
        # print("time taken by block to execute:", end_time - start_time)
        print(f"time taken by {func()} to execute: {end_time - start_time}")
    return wrapper()


@my_decorator2
def my_function2():
    print("testing has been started....")
    time.sleep(4)

@my_decorator2
def my_function3():
    print("third function executing....")
    time.sleep(9)








