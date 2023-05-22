"""

same constructor have different arguments then those constructor are said to be overloaded methods
But in python Constructor overloaing is not possible
if we are trying to declare multiple constructor with same name and
different number of arguments the python will always consider only last constructor

This challenges how can we handle


"""

print("###### Constructor with default arguments ######")

class Test:
    def __init__(self,a=None,b=None,c=None) -> None:
        print("constructor have 1|2|3|0 arguments")
c=Test(2,3,4)
c=Test()
c=Test(34)
        


print("########## Constructor with variable number of arguments ")


class Test:
    def __init__(self,*a) -> None:
        print("constructor have 1|2|3|0 arguments")
c=Test(2,3,4)
c=Test()
c=Test(34)