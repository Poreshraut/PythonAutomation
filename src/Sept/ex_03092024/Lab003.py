from math import acosh

print("Let's make calculator with something new using object oriented programming system")

class Calcula:

    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b


    def add(self):
        print(f"addition: {self.a + self.b}")

    def sub(self):
        print(f"subtraction: {self.b - self.a}")

    def mul(self):
        print(f"multiplication: {self.a * self.b}")

    def div(self):
        print(f"division: {self.b / self.a}")


calculator = Calcula(1,2)
print()
calculator.add()
calculator.sub()
calculator.mul()
calculator.div()
