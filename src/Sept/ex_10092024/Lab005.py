class ExceptionInClass:

    def f1(self):
        try:
            a = int(input("enter the integer: "))
        except Exception as e:
            print(e)
            print("Always use integers..")
        else:
            print(a)
        finally:
            print("I will always execute the closing statement..")

ex = ExceptionInClass()
ex.f1()