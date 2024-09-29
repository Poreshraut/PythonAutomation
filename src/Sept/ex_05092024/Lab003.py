print("access the private variable through the methods within the class")

class Bank:

    def __init__(self, account_number, bank_balance):
        self.__account_number = account_number
        self.bank_balance = bank_balance

    def deposit(self, money):
        self.bank_balance = self.bank_balance + money

    def check_bank_balance(self):
        print(self.bank_balance)

    def my_account_number(self, authenticate):
        if authenticate == True:
            print(self.__account_number)
        else:
            print("Not Allowed!")


axis = Bank(123443212345, 500000000000000)

axis.deposit(100)
axis.deposit(100)
axis.deposit(100)
axis.deposit(100)
axis.check_bank_balance()

axis.my_account_number(True)
axis.my_account_number(False)

'''
1. private variable can be access by the methods within the class
2. private variable can be access by the private methods as well
3. we have encapsulated private variable within the methods so, it can not be access outside the class but within the class using function

'''
