print("This time we are learning Object Oriented Programming.......!")

class Person:

    name = None
    eyes = None
    hairs = None
    color = None
    id = None
    gender = None

    def name_of_the_person(self):
        print(f"My name is: {self.name}")

    def my_eyes_color(self, eyes):
        print(f"my eyes are: {self.eyes} {eyes}")

    def my_hairs(self, hairs):
        print(f"my hairs are: {hairs}")


person1 = Person()

print(person1.name)
print(person1.id)
print(person1.color)

person1.name_of_the_person()
person1.my_eyes_color("black")
person1.my_hairs("brown")

person1.name = "Sachin"
person1.name_of_the_person()

person1.eyes = "green"
person1.my_eyes_color(123)