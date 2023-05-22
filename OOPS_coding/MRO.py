class A:
    """
    MRO--> Method Resolution Order its fallow DLR Depth First left to Right Child will more periority than Parent
    """
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
print(A.__doc__)
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())