print("let's learn about login functionality")

class Application:

    username = None
    password = None


    def __init__(self, username, password):
        self.username = username
        self.password = password


    def confirm_login(self):
        if self.username == "poreshraut@gmail.com" and self.password == "porreshraaut":
            print("Login allowed!")

        else:
            print("Login is not allowed!")

username = input("enter username: ")
password = input("enter password: ")
login = Application(username, password)
login.confirm_login()