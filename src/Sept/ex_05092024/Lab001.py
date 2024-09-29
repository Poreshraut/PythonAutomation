print("this is for Encapsulation")

class Myclass:

    public_variable = "Public Variable"
    _protected_variable = "Protected Variable"
    __private_variable = "Private Variable"

    def fetch_private(self):
        print(self.__private_variable)


my_class = Myclass()

print(my_class.public_variable)
print(my_class._protected_variable)
my_class.fetch_private()
