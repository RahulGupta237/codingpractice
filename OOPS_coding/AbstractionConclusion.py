print("""     

########## Conclusion ################

if a class contain atleast one abstract method and if we are extending ABC 
then instaniation is not possible

*** Abstract class with abstract method instantiation is not possible
** Abstract class  can contain both abstract method and concrete method i.e non abstract method



###############

#  Parent class abstract method should be implemented in the child classes 
#otherwise we can not instantiat child class.
# if we not creating child class object then we would not get any error  

###############


""")


from abc import *
class Vehicle(ABC):

    @abstractmethod
    def noofwheel(self):
        pass
class Bus(Vehicle):
    # if we not creating child class object then we would not get any error  
   
    print("testing occur continue")
    pass
    def noofwheel(self):
        pass
        # pass here working if uncommented meand 
b=Bus() #we can not create object or instance of child class because abstract method should be there
