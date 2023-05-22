from functools import partial
print("*********explore functools  partial*************")
def add(x, y):
    return x + y

add_5 = partial(add, 5) # creates a new function with the first argument set to 5

print(add_5(3)) # prints 8


print("*********explore functools reduce*************")

from functools import reduce

def multiply(x, y):
    return x * y

lst = [1, 2, 3, 4]
result = reduce(multiply, lst)

print(result) # prints 24


from functools import cached_property
print("*********explore functools cached_property *************")


class MyClass:
    def __init__(self, x):
        self.x = x
    
    @cached_property
    def square(self):
        print("Calculating square...")
        return self.x ** 2

my_obj = MyClass(5)

print(my_obj.square) # prints "Calculating square..." and 25
print(my_obj.square) # prints only 25 (no calculation)


