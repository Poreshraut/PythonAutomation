from typing import get_origin

print("Let do object oriented programming....")

class Dog:
    name = None
    bread = None
    color = None

    def sleep(self):
        print("sleeping..")

    def bark(self):
        print("bark...")

    def eat(self, food):
        print(f"He it's {food}")

    def dog_name(self):
        print(f"Dog name is: {self.name}")

dog1 = Dog()

dog1.name = "chow"
dog1.bread = "american"
dog1.color = "brown"
print(dog1.name)
print(dog1.bread)
print(dog1.color)
dog1.sleep()
dog1.bark()
dog1.eat("banana")
dog1.dog_name()
print()
print("keep some distance between two objects")
dog2 = Dog()
dog2.name = "Dhinchak"
dog2.color = "White"
dog2.bread = "Rassian"
print(dog2.name)
print(dog2.color)
print(dog2.bread)
dog2.sleep()
dog2.bark()
dog2.eat("vegitables")
dog2.dog_name()
