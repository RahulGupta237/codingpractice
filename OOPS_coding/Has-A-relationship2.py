class Car:
    """
    Has A Relationship We can access members of one class inside another class
    In this program Employee class Has-A Car reference  and hence Employee class can access all members of Car class
    
    """
    def __init__(self,name,model,color) -> None:
        self.name=name
        self.model=model
        self.color=color
    def getinfo(self):
        print(f"Car Name: {self.name}, Model:{self.model} and color {self.color}")
    

class Employee:
    def __init__(self,ename,eno,car) -> None:
        self.ename=ename
        self.eno=eno
        self.car=car
    def empinfo(self):
        print(f"Employee name: {self.ename}\n Employee Number: {self.eno}\n Employee Car information")
        self.car.getinfo()
print(Car.__doc__)
c=Car('BMW',"5.88V","Black Green")
e=Employee("Rahul Gupta","2498",c)
e.empinfo()
        