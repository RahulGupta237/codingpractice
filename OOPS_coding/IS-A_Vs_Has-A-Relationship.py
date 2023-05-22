class Car:
    def __init__(self,name,model,color) -> None:
        self.name=name
        self.model=model
        self.color=color
    def getinfo(self):
        print(f"Car Name: {self.name}, Model:{self.model} and color {self.color}")
    
class Person:
    """ Is-A-Relationship By Inheritence"""
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def eatdrink(self):
        print("Eat biryani and drink")
class Employee(Person):
    """
        If we want to extend existing functionality with some more extra functionality then we should go for IS-A Relationship.

        if we dont want to extend and just we have to use existing functionality then we should go for Has-A-Relationship

        Here This program  Employee class extend person class functionality But Employee class just use Car functionality but not extending



        Employee use car functionality ---> Has-A-Relationship
        Employee extend person class functionality-->Is-A-Relationship

        """
    
    def __init__(self,name,age,esal,eno,car) -> None:
        super().__init__(name,age)
        self.esal=esal
        self.eno=eno
        self.car=car
    def work(self):
        print("Python Coding is very easy just like drinking chill bear")
        
    def empinfo(self):
        print(f"Employee name: {self.name}\n Employee Number: {self.eno}\n Employee Car information")
        self.car.getinfo()
print(Employee.__doc__)
c=Car('BMW',"5.88V","Black Green")
e=Employee("Rahul Gupta",67,2498,20000,c)
e.eatdrink()
e.work()
e.empinfo()

"""
Eat biryani and drink
Python Coding is very easy just like drinking chill bear
Employee name: Rahul Gupta
Employee Number:2498
Employee Car information
Car Name: BMW, Model:5.88V and color Black Green



"""
        