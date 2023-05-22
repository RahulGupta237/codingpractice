print("############ Case 4th ################")
"""
From Child Class Method of Child class 
how to call parrent class instance methods and constructor
With the help of below method
super(B,cls).__init__(cls)
super(B,cls).m1(cls)

"""
class A:
    """
Case 4th

From Child Class Method of Child class 
how to call parrent class instance methods and constructor
With the help of below method
super(B,cls).__init__(cls)
super(B,cls).m1(cls)

"""
    def __init__(self) -> None:
        
        print("Parrent class Constructor")
    def m1(self):
        print("Parrent Instance Method")
class B(A):
    @classmethod
    def m2(cls):
        super(B,cls).__init__(cls)
        super(B,cls).m1(cls)
print(A.__doc__)
B.m2()


print("############### Case 5th ###############")
"""
In Child class static method we are not allowed to use super()
give Run Time Error super no arguments
generally but in special way we can use

Special way below


"""

class P:
    """
Case 5th 

In Child class static method we are not allowed to use super()
give Run Time Error super no arguments
generally but in special way we can use

Special way below

super(childclassname,childclassname).methodname()
super(c,c).m3()


"""
    a=10
    def __init__(self) -> None:
        self.b=30
        print("Parrent constructor")
    def m1(self):
        print("parrent instance method")
    @classmethod
    def m2(cls):
        print("parrent class method")
    @staticmethod
    def m3():
        print("parrent static method")
class C(P):
    @staticmethod
    def m1():
        # super().__init__() Invalid
        # super().m1() invalid
        # super().m2() invalid
        # super().m3() invalid
        pass
        # super().m1()
        # super(C,C).m2()
        super(C,C).m3()

print(P.__doc__)
c=C()
c.m1()