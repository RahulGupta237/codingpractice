
class Student:
    """

    set and get the value to the instance variable


    """
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.name=marks
    def getMarks(self):
        return self.getMarks

n=int(input("enter number of student"))
for i in range(n):
    name=input("enter name")
    marks=int(input("enter a marks"))
    s=Student()
    s.setName(name)
    s.getName()
    s.setMarks(marks)
    s.getMarks()