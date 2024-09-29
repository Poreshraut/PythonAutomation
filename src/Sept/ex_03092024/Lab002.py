print(f"Let's create Calculator using Object Oriented Programming System")


class Calcu:

    def __init__(self):
        print("I will execute while defining the object")

    def addition(self, a, b):
        return a + b

    def subtration(self, a, b):
        return b - a

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return b // a

calculator1 = Calcu()
print()

print(f"Addition: {calculator1.addition(1,2)}")
print(f"Subtraction: {calculator1.subtration(1,2)}")
print(f"multiplication: {calculator1.multiplication(1,2)}")
print(f"division: {calculator1.division(1,2)}")
