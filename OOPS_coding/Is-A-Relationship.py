class Person:
    """ Is-A-Relationship By Inheritence"""
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def eatdrink(self):
        print("Eat biryani and drink")
class Employee(Person):
    def __init__(self, name, age,eno,esal) -> None:
        super().__init__(name, age)
        self.eno=eno
        self.esal=esal
    def work(self):
        print("Python Coding is very easy just like drinking chill bear")
        super().eatdrink()
    def empinfo(self):
        print("Employee Name:",self.name)
        print("Employee Number:",self.eno)
        print("Employee Sallary:",self.esal)
e=Employee('Rahul Gupta',76,567,38000)
print("rahul testing outside",e.name)
print(e.eatdrink())
e.eatdrink()
e.work()
e.empinfo()
