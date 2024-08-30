print("Welcome to Goa Singham!")


def multi_arguments(*args):
    print(args[1])


multi_arguments("Sachin", "Poresh", "Shilpa")

def multi2_arguments(*argus):
    for i in argus:
        print(i, end=" " "\n")

multi2_arguments("Poresh", "Virat", "Dhoni", "Suryakumar")

print("Poresh", "Sachin", "Dhoni", "Rohit")

print("My name is anthony gonsalvish")

print("================================================================")
flag = 100

if flag > 1011:
    print("Flag is Greater")
else:
    print("Flag is Smaller")