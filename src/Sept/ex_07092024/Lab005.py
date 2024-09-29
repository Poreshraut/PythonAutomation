from src.Sept.ex_07092024.Lab004 import Human1

print("here we will learn about the static method")

class Human:


    def __init__(self, name):
        self.name = name

    def your_name(self):
        print(f"my name is {self.name}")

    @staticmethod
    def company_name(company):
        print(f"company name is {company}")

# hum = Human("Poresh")
#
# hum.company_name('valantic')
# hum.your_name()

Human.company_name("valantic (former doitlean)")