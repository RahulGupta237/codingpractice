
class Student:
    def __init__(self,name,marks) -> None:
        self.name=name
        self.marks=marks
    def display(self):
        print(f"Hi {self.name}")
        print(f"Your marks are: {self.marks}")
    def grade(self):
        if self.marks>=60:
            print("You got first grade")
        elif self.marks>=50:
            print("You got second grade")
        elif self.marks>=35:
            print("You got second grade")

        else:
            print("failed")
n=int(input("enter number of student"))
for i in range(n):
    name=input("enter name")
    marks=int(input("enter a marks"))
    s=Student(name,marks)
    s.display()
    s.grade()
    print()