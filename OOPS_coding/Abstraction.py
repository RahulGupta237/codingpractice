from abc import *
print("###########  Abstract Method Without ABC class i.e Abstract class ###########")
print()
class Test:
    """
    Point should be noted that here only abstract method not abstract class thats why we can create instance of class below code you can understand with i.o output


    ("i am practice here. Abstract method has only declaration but not implementation")
    Some time we dont know about implementation still we can declare a method such type of methods are called abstract method


    
    """
    print("rahul gupta")
    @abstractmethod
    def m1(self):
        pass
        print("no need declare but here working bcz class is not abstract but method have abstract")

print(Test.__doc__)
x=Test()
x.m1()
print()
print()
print("############## End Abstract Method ##############")

#######################################################################################


print()
print("################## Concrete Class  ##################")
print()

class concreteclass:
    """
    In this code we can create object for test class bcz it is concrete class its doesnot have any abstract method

    
    """
    pass
obj=concreteclass()
print(concreteclass.__doc__)

print()
print("#################### End ######################")

##############################################


print("############# Abstract class without abstract method  ###################")
print()

class Test1(ABC):
    """
    In below code we can create object even it is derived from ABC class
    b'z it doesnot contain any abstract method
    
    """
    print("Gupta")
print(Test1.__doc__)
x=Test1()


print()
print("#########  End Abstract class ########")


print("############# Abstract class with abstract method ###################")
print()

class Test2(ABC):
    """
    In below code we can not create object even it is derived from ABC class
    b'z it contain abstract method
    
    """
    @abstractmethod
    def m1():
        pass
    print("i g")
print(Test2.__doc__)
# x=Test2()


print()
print("#########  End Abstract class ########")



print("""     

########## Conclusion ################

if a class contain atleast one abstract method and if we are extending ABC 
then instaniation is not possible

*** Abstract class with abstract method instantiation is not possible



##############################


""")







