print("now we will learn about constructor...")

# it is for automatically called while creating an object of an class

class Dog:

    name = None
    age = None

    def __init__(self, name, age):
        print("I will automatically get called while creating object of an class")
        self.name = name
        self.age = age

    def sleeping_dog(self):
        print(f"who is sleeping: {self.name}")
        print(f"{self.name} age is: {self.age}")
        return "Sachin"

dog1 = Dog("chow", 29)
dog1.sleeping_dog()

dog2 = Dog("mow", 34)
dog2.sleeping_dog()
print("---------------------------------------------")
sleeping_dog = dog1.sleeping_dog()
print(sleeping_dog)