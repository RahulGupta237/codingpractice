
print("########### Case 1 #############################")
# Case 1 
"""
From child class we are not allowed to access parent class instance variable 
by using super(), Compulsory we should use self only 
But  we can access class static variable by using Super()


"""


class P:

    """
Case 1st-->
From child class we are not allowed to access parent class instance variable 
by using super(), Compulsory we should use self only 
But  we can access class static variable by using Super()


"""
    a=10
    def __init__(self) -> None:
        self.b=30
class C(P):
    a=888
    def m1(self) -> None:
        """

           print(super().b) # invalid
            AttributeError: 'super' object has no attribute 'b'

        
        """
        print(super().a) # valid
        print(self.b)# valid
        #print(super().b) # invalid  


print(P.__doc__)       
c=C()
c.m1()

print("########### Case 2 #############################")
# Case 2
"""

From Child Class constructor and Instance method 
we can access parrent class,Instance method,static method and class method
by using super() method
"""

class P:
    """
Case 2nd

From Child Class constructor and Instance method 
we can access parrent class,Instance method,static method and class method
by using super() method
"""
    a=10
    def __init__(self) -> None:
        self.b=30
        print("Parent constructor")
    def m1(self):
        print("parrent instance method")
    @classmethod
    def m2(cls):
        print("parrent class method")
    @staticmethod
    def m3():
        print("parrent static method")
class C(P):
    a=888
    def __init__(self) -> None:
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

print(P.__doc__)
        
c=C()
c.m1()

# Case 3
"""

From Child Class, class method we can not access parent class instance methods and constructor by using super()
directly but indirectly possible. But we can access parrent class static and class method

"""


print("########### Case 3 #############################")

class P:
    """
Case 3rd

From Child Class, class method we can not access parent class instance methods and constructor by using super()
directly but indirectly possible. But we can access parrent class static and class method

Type Error

"""
 
    a=10
    def __init__(self) -> None:
        self.b=30
        print("Parent constructor")
    def m1(self):
        print("parrent instance method")
    @classmethod
    def m2(cls):
        print("parrent class method")
    @staticmethod
    def m3():
        print("parrent static method")
class C(P):
    a=888
    @classmethod
    def m1(cls):
        # super().__init__() --> Invalid
        # super().m1() --> Invalid
        super().m2()
        super().m3()

print(P.__doc__)
        
C.m1()

