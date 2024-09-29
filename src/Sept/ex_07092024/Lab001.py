print("let's talk about the method overriding...")
# Method Overriding:
# child class or subclass can have same method name as the parent class or super class

class shape:

    def area(self):
        print("I am the area of the shape")


class rectangle(shape):

    def __init__(self, a, b):
        self.length = a
        self.width = b

    def area(self):
        print(f"area of the rectangle is: {self.length * self.width}")


class circle(shape):

    def __init__(self, b):
        self.radius = b

    def area(self):
        print(f"area of the circle is: {3.14 * self.radius * self.radius}")


rec = rectangle(5, 3)

print(rec.length)
print(rec.width)
rec.area()


cir = circle(6)
print(cir.radius)
cir.area()