print("############# Polymorphism #############")
print(
"""

Related to polyphormism having 4 types are important


1) Duck Typing philospy python 
2) Overloading
3) Overriding


""")
print('############## 1) Duck Typing philospy python  #############')
class Duck:
    """

Related to polyphormism having 4 types are important

1) Duck Typing philospy python 
 Dog has no attribute talk  But we can solve this problem by using hasattr() function
 hasattr(obj,'attributename')
 attributename can be method name or variable name
    
    """
    def talk(self):
        print("Quack Quack Quack")
class Dog:
    def bark(self):
        print("Bow Bow Bow")
    
def f1(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()
print(Duck.__doc__)
d=Duck()
f1(d)
dg=Dog()
f1(dg)




