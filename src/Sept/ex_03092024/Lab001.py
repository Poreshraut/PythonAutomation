from copyreg import constructor

print("Let's get started with OOP's again")

class Person:
    name = None
    age = None
    occupation = None
    salary = None

    def __init__(self):
        self.name = input("enter name: ")
        self.age = int(input("enter age: "))
        self.occupation = input("enter occupation: ")
        self.salary = int(input("enter salary: "))

    def my_name_is(self):
        print(f"my name is: {self.name}")
        print(f"I know my name is unique. But I like it....")

    def my_age(self):
        print(f"I am {self.age} years old. What about you?")
        print(f"I know we should not ask age to any girl, but it is part of the process")

    def my_occupation(self):
        print(f"I am working in renowned IT company and I am {self.occupation}")
        print(f"What do you do for living?")

    def my_salary(self):
        print(f"I earn {self.salary} LPA")
        print(f"Remember that IT person doesn't disclose there salary. They all are liars.")


person1 = Person()

person1.my_name_is()
print()
print(person1.name)
print(person1.salary)
print(person1.occupation)
print(person1.age)
print()
person1.my_age()
person1.my_occupation()
person1.my_salary()









