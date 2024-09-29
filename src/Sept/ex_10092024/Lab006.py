"""We are learning Custom Exception"""

# If I have 100/- balance and withdrawing 1000/-, it should give me exception

class LowBalanceException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)

balance = 100
withdraw = int(input("enter withdrawal amount: "))
if withdraw > balance:
    raise LowBalanceException("Your balance is low!")
else:
    print(f"Amount has been withdraw: {withdraw} and remaining balance is {balance - withdraw}")
