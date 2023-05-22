"""
Public-->

Bydefault Every attribute is public we can access from anywhere
either with in class or from outside of the class
eg--> name="Zaid"

Protected-->

Protected attribute can be accessed within the class anywhere
but from outside of the class only can child class.
wecan specify an attribute as protected by prefix with _ symbol

eg-->   _name="Rahul Gupta"

but it is just convention and in reality doesnot exit protected attributes

Private-->

Private attribute can be access only within class 
i.e from outside of the class can not be access.
We can declare a variable as private explicity by prefixing with __ symbol
eg-->  __name="Brijesh"

"""

class Test:
    x=10 # Public
    _y=20 # Protected
    __z=30 # Private
    def m1(self):
        print("Inside Test Class\n",Test.x)
        print(Test._y)
        print(Test.__z,"\nabove inside Test class")

t=Test()
t.m1()
print(t.x) #valid
print(t._y) # valid
#print(t.__z) # THis is not access private variable direct from out side of the class
print("Here we can access private variable",t._Test__z)
