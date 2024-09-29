print("let's work on encapsulation concepts")

class Bank:

    def __init__(self, account, balance):
        self.__account_number = account
        self.balance = balance

    def public_function(self):
        print("i am public method")
        print(self.__account_number)
        self.__private_function2()

    def __private_function1(self):
        print("i am private method 1")

    def __private_function2(self):
        print(self.__account_number)
        self.__private_function1()

    def deposit(self, money):
        self.balance = self.balance + money

    def check_bank_balance(self):
        print(self.balance)

    def show_me_account_number(self, authenticator):
        if authenticator == True:
            print(self.__account_number)
        else:
            print("not allowed!")


axis = Bank(12345, 50000000000000)

axis.show_me_account_number(True)
axis.check_bank_balance()
axis.deposit(100)
axis.check_bank_balance()
print("--------------------------------")
axis.public_function()

'''
1. we can call private methods or functions within the class
2. we can not call private methods or functions out the class
3. within the class inside public method we can call private variable as well as private function --> we have to use self. keyword
4. within the class inside the private method we can call public functions as well as private variable --> we have to use self. keyword
'''