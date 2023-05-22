class Student:
    """
    Composition-->In this program Student Object there is no chance of 
    existing his name Hence Student object and his name are strongly
     associated which is nothing but Composition
    
    Aggregation--> But Without existing Student object there is may be chance of existing collegeName
    Hence Student object and collegeName are weakly associated which is nothing but Aggregation

    Conclusion ----->
            The Relationship between object and its instance variable is always Composition where as the relationship between object and static variable is aggregation
    """
    collegeName="Sana Engineer College"

    def __init__(self,name) -> None:
        self.name=name
print(Student.__doc__)
print(Student.collegeName)
s=Student("Rahul Gupta and Shabnam")
print(s.name)