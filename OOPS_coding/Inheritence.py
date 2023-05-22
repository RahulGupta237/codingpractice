#----Single level Inheritence

class P:
    """
    Single Inheritence
    
    """
    def m1(self):
        print("parrents Class")
class C(P):
    def m2(self):
        print("Child Class")
c=C()

c.m2()
c.m1()

#------Multi Level Inheritence

class Multi_P:
    """
    Multilevel Inheritence
    
    """
    def m1(self):
        print("parrents Class")
class Multi_C(Multi_P):
    def m2(self):
        print("Child Class")
class Multi_CC(Multi_C):
    def m3(self):
        print("sub child class")
print(Multi_P.__doc__)
x=Multi_CC()
x.m3()
x.m2()
x.m1()


#-------Hierarchical Inheritence--------


class Multi_P:
    """
    Hierarchical Inheritence
    
    """
    def m1(self):
        print("parrents Class")
class Multi_C(Multi_P):
    def m2(self):
        print("Child 1 Class")
class Multi_CC(Multi_P):
    def m3(self):
        print("Child 2 class")
print(Multi_P.__doc__)
x=Multi_CC()
x.m1()
x.m3()
y=Multi_C()
y.m1()
y.m2()


#----------Multiple Inheritence----------------



class Multi_P:
    """
    Multiple Inheritence
    
    """
    def m1(self):
        print("parrents Class")
class Multi_C:
    def m2(self):
        print("Child 1 Class")
class Multi_CC(Multi_C,Multi_P):
    def m3(self):
        print("Child 2 class")
print(Multi_P.__doc__)
x=Multi_CC()
x.m1()
x.m3()
x.m2()






