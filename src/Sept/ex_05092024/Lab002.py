print("let's get started with encapsulations")

class Bank:

    def __init__(self, account_number, bank_balance):
        self.account_number = account_number
        self.bank_balance = bank_balance

    def my_function(self, name):
        self.name = name
        print(f"my name is {name}")



axis = Bank(123456789098, 5000000000000)

print(axis.account_number)
print(axis.bank_balance)
# print(axis.name) AttributeError: 'Bank' object has no attribute 'name'
# because axis.name doesn't exist until we call axis.my_function("Alex")
# When we calls function name variable appears and it disappears as the function ends

axis.my_function("Venugopal aierr")
print(axis.name)

'''Points to Remember: 
1. there are different types of variables we can see 
ex. instance variables, local variables etc
so, instance variables are belongs to the object.
when we create object then it has it's own variable now
but local variables are only accessible in the function
we have to call the function first to active the variable and as the functions end variable disappears
'''