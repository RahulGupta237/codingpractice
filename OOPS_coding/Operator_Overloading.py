print('############# Over loading   ##################')

"""
Python support operator overloading
we can use same operator for multiple purpose


"""

print("\nExample 1\n")
class Book:
    """

    TypeError: unsupported operand type(s) for +: 'Book' and 'Book'

    we can overload + operator to work with Book object i.e Python support operator overloading
    For every operator have magic method are available
    
    """
    def __init__(self,pages) -> None:
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
print(Book.__doc__)
b1=Book(300)
b2=Book(200)
print(b1+b2)



print("\nExample 2\n")

class Employee:
    def __init__(self,name,sallary) -> None:
        self.name=name
        self.sallary=sallary
    def __mul__(self,other):
        return self.sallary*other.days
class TimeSheet:
    def __init__(self,name,days) -> None:
        self.name=name
        self.days=days
e=Employee("Rahul Gupta",27000)
t=TimeSheet('Rahul',11)
print(f"Hellow{e.name} sallary having {e*t}")
    



