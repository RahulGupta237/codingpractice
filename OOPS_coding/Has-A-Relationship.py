class Engine:
    """ Has-A-Relationship means By composition method
       By using class name or by creating object we can access member of one class inside another class is nothing but composition

       main advantage of Has-A-Relationship is code Reusability
    
    
    """

    a=10
    def __init__(self) -> None:
        pass
        self.b=20
    def m1(self):
        print("Engine Specific functionality")
class Car:
    def __init__(self) -> None:
        self.engine=Engine()
    def m2(self):
        print("Car using Engine Class Functionality")
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()
print(Engine.__doc__)
c=Car()
c.m2()