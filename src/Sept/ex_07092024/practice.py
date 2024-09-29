# method overriding: same method name in different class
# method overloading: same method name in same class. it is not possible in python

'''
In your code, print(a.ab) doesn't work because the Son class overrides the __init__ method of the Father class.
This means when you create an instance of the Son class, the __init__ function in the Father class is not called,
so the ab attribute from the Father class isn't created.
To fix this, you can call the __init__ method of the Father class inside the Son class using super() like this:
'''

class Father:

    a = "father variable"

    def __init__(self):
        self.ab = "father's init function"

    def home(self):
        print("it is fathers home")

class Son(Father):

    b = "son variable"

    def __init__(self):
        self.bc = "son's init function"

    def home(self):
        print("it is sons home")


a = Son()
print(a.a)
print(a.b)
print(a.bc)
# print(a.ab)
a.home()
print("------------------------------------------------------------------------------------")
class Parent:

    a = "normal Parent Variable"

    def __init__(self):
        self.parent_variable = "Parent init variable"

    def sweet_home(self):
        print("this is parent's sweet home")

class Child(Parent):

    b = "normal Child Variable"

    def __init__(self):
        self.child_variable = "Child init variable"
        super().__init__()

    def sweet_home(self):
        print("this is child's sweet home")
        super().sweet_home()

chi = Child()
print(chi.a)
print(chi.b)
print(chi.parent_variable)
print(chi.child_variable)
chi.sweet_home()
# ===============================================================================================================================
print("==========================================================================================================================")

class Cricket:

    bat = "MRF"

    def virat(self, vari2):
        print("i have most 50 in one day cricket")
        print(vari2)

    def virat(self, vari1 = "Sachin"):
        print("i have most 100 in one day cricket")
cri = Cricket()
print(cri.bat)

cri.virat()
