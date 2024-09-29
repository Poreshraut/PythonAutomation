print("ek jhalak of Encapsulation")

class Emergency:

    name = None
    password = None


    def __init__(self):
        self.password = "it_is_secret_password"

    def change_my_password(self):
        print(f"My password is: {self.password}")



person1 = Emergency()
print(person1.password)
person1.password = "Some one has changed the password.. You can not access it now!"
person1.change_my_password()