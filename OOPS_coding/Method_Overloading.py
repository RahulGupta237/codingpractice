print("Method Overloading")



class Test:

    """

same method have different arguments then those method are said to be overloaded methods
But in python Method overloaing is not possible
if we are trying to declare multiple methods with same name and
different number of arguments the python will always consider only last method

This challenges how can we handle


"""
    def m1(self):
        print("no arguments")
    def m1(self,a):
        print("one arguments")
    def m1(self,a,b):
        """
        consider only last method i.e this method
        
        """
        print("Two arguments")
print(Test.__doc__)
t =Test()
# t.m1()
# t.m1(30)
t.m1(5,87)


print("########1 ##################How can we handle overloaded method Requirements in Python #####")


class Tests:
    """
    first case style-->
    How can we handle overloaded method Requirements in Python
    """
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(f"The sum of three number {a+b+c}")
        elif a!=None and b!=None:
            print(f"the sum of two number {a+b}")
        else:
            print("please provide two or three number")
print(Tests.__doc__)
r=Tests()
r.sum(3,8)
r.sum(3,8,9)


print("###################2########################")


class Tests2:
    """
    first case style-->
    How can we handle overloaded method Requirements in Python
    """
    def sum(self,*a):
        total=0
        for x in a:
            total+=x
        print(f"The total number are {total}")
print(Tests2.__doc__)
r=Tests2()
r.sum(3,8,88)
r.sum(3,8,9,78)