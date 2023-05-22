"""
  Super()--->  Super method is a built in method which is useful to
   call the super class constructor,variable and methods from the child class

"""

class Person:
    """
  Super()--->  Super method is a built in method which is useful to
   call the super class constructor,variable and methods from the child class

"""
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def display(self):
        print(f"Name: {self.name}\n Age {self.age}")
class Student(Person):
    def __init__(self, name, age,rollno,marks) -> None:
        super().__init__(name, age)
        self.rollno=rollno
        self.marks=marks
    def display(self):
        super().display()
        print(f"roll No {self.rollno}\n Marks {self.marks}")
print(Person.__doc__)
S1=Student("Rahul Gupta",28,56,71)
S1.display()
