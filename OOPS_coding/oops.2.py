
class Test:

    """
    Static variable
    Static variable is not varied from object to object such type of variable we have to declare within class directly such type of variable are called Static variable For total class only one copy of static variable will be created shared by all object of that class we can access static variable either by classname or by object reference variable but recomended to class name

        Various place to declare static variable
        inside constructor by class name
        inside instance method by using class name
        inside class method by using either class name or cls variable
        inside static method by using class name
    
    """
    a=10
    def __init__(self) -> None:
        Test.b=20
    def m1(self):
        Test.c=30
    @classmethod
    def m2(cls):
        cls.d1=40
        Test.d2=400
    @staticmethod
    def m3():
        Test.e=50
print(Test.__doc__)
print(f" Dictionary of class without create object reference varaiable \n\n {Test.__dict__}\n \n")
t=Test()
print(f" Dictionary of class with create object t=Test() reference varaiable \n\n {Test.__dict__}\n \n")
t.m1()
print(f" Dictionary of class with create object t=Test() and call m1 method  reference varaiable \n\n {Test.__dict__}\n \n")
t.m2()
print(f" Dictionary of class with create object t=Test() and call m2 method  reference varaiable \n\n {Test.__dict__}\n \n")
t2=Test()
t2.m3()
print()
print("###################")
print(Test.__dict__)
