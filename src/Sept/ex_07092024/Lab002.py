print("learn polymorphism or method overriding")
# method overriding: same method name in parent and child class
# child always override the parent function
# super() method is nothing but the calling parent class method
'''In Python, the super() function gives you access to the methods and attributes of the parent class. However, it follows the method 
resolution order (MRO), which means it looks for methods and attributes in the next class in the inheritance chain, not necessarily 
the top-most class.'''
'''You can access Grandfather's home() method, but only if you call super().home() in the Father class because super() will always 
reference the next class in the inheritance hierarchy.'''
'''Attributes can be accessed from any class in the hierarchy because they are not "overridden" like methods.
Methods follow MRO and must be explicitly called using super() in the parent class to ensure the chain continues.'''


class Grandfather:

    a = 10
    f = 50

    def home(self):
        print("i have a house")

class Father(Grandfather):

    b = 20
    f = 90

    def home(self):
        print("i have a flat")
        super().home()

class Son(Father):

    c = 30

    def home(self):
        print("i have a 1bhk")
        print(f"Grandfather attribute: {super().a}") # parent of parents attribute using super() method
        print(f"Father attribute: {super().b}") # parents attribute using super() method
        super().home() # Parents method only not parent of parent
        print(f"self. means my own variable: {self.c}")
        print(f"super(). means my fathers or parents variable: {super().a} or {super().b}")
        print(f"Trying to fetch Grandfathers f: {super().f}")

grand = Grandfather()
print(grand.a)
grand.home()
print("\n")
fath = Father()
print(fath.b)
print(fath.a)
fath.home()
print("\n")
sonn = Son()
print(sonn.a)
print(sonn.b)
print(sonn.c)
sonn.home()
print("------------------------------------")

sonn.home()