class Employee:
    """ Passing member of one class to another class """
    def __init__(self,eno,ename,esal) -> None:
        pass
        self.eno=eno
        self.ename=ename
        self.esal=esal
        print("i am first here")
    def display(self):
        print("I am third here")
        print("Employee number",self.eno)
        print("Employee name",self.ename)
        print("Employee sallary",self.esal)
class EmployeInfo:
    def modifysal(emp):
        print("I am second here")
        emp.esal+=10000
        print("modified sallary",emp.esal)
        emp.display()
        print("hi i am working after calling last display")

e =Employee(100,'Rahul',10000)
EmployeInfo.modifysal(e)

