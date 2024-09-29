from importlib.metadata import requires
from sys import prefix

print("we are leaning about abstraction")

# hiding the details and showing what is required



from abc import ABC, abstractmethod

class God(ABC):

    @abstractmethod
    def payFees(self, fees):
        print("i have paid all the fees of your course")

    def enrolled(self, name):
        print(f"{name} has been successfully enrolled in the PoreshInstitute")

    def __init__(self):
        print("i wanted to create humans and following are the necessary behavior they suppose to have")

    @abstractmethod
    def eyes(self, eyes):
        print(f"i have {eyes} beautiful eyes")
    @abstractmethod
    def nose(self, nose):
        print(f"i have {nose} beautiful nose with two holes")
    @abstractmethod
    def hands(self, hand):
        print(f"i have {hand} hands")

    def voice(self):
        print("i can talk")

    def it_is_not_there(self, variable1):
        print(f"it is not there in the {variable1}")

class Human1(God):

    def legs(self, leg):
        print(f"i have {leg} legs")

    def payFees(self, fees):
        pass

    def eyes(self, eyes):
        pass

    def hands(self, hand):
        print(f"i have {hand} hands")

    def nose(self, nose):
        pass



hum = Human1()

hum.legs(2)
hum.hands(2)

hum.it_is_not_there("human1")
print("====================================================Dhasu example===========================================")

class PoreshInstitute(God):

    def payFees(self, fees):
        print("i have paid all the fees of your course")

    def nose(self, nose):
        pass

    def hands(self, hand):
        pass

    def eyes(self, eyes):
        pass

    def surrounding(self):
        print("PoreshInstitute has good surroundings")


poresh = PoreshInstitute()

poresh.payFees(100)


poresh.enrolled("Virat")

