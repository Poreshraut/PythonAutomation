print("let's learn method overloading...")
# method overloading means: same name but work is different
# method overloading is only possible when we give the default values (function with default value)
# python doesn't support method overloading

class Mathfunction:

    def additionfunction(self, a, b):
        print(a + b)

    def additionfunction(self, a, b, c):
        print(a + b + c)

math1 = Mathfunction()
# math1.additionfunction(3,4) ==> Python interpreter got confused which one to call as there are two same method name in class

# object is parent of every class
class Function1(object):
    pass
# every class is a object class - single inheritance

# function with default value

class Function3:

    def add(self, a, b):
        print(a + b)

    def add(self, a, b, c = 0):
        print(a + b + c)

fun3 = Function3()
fun3.add(3,4,5)
fun3.add(4,5)

