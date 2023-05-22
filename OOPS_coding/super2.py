"""
How to call Method of Particular super class
super(ClassName,self).MethodName()
"""
class A:
    """
    How to call Method of Particular super class
super(ClassName,self).MethodName()
    
    """
    def m1(self):
        print("A class Method")
class B(A):
    def m1(self):
        print("B class Method")
class C(B):
    def m1(self):
        print("C class Method")
class D(C):
    def m1(self):
        print("D class Method")
class E(D):
    def m1(self):
        super(D,self).m1()
        A.m1(self)

print(A.__doc__)
obj=E()
obj.m1()


