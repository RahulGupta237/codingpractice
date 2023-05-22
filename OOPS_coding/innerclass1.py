class Person:
    """
      Without exiting one type of object there is no chance of exiting another type of object
      example without exiting car object there is no change of existing engine object
    
    """
    def __init__(self) -> None:
        self.name='rahul Gupta'
        self.db=self.Dob()
    def display(self):
        print(f"Name is {self.name}")
    class Dob:
        def __init__(self) -> None:
            self.dd=10
            self.mm=5
            self.yy=1996
        def display(self):
            print(f"DOB {self.dd}-{self.mm}-{self.yy}")
print(Person.__doc__)
p=Person()
p.display()
x=p.db
x.display()
