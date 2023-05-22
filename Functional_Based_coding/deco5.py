def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator(100)
def my_function():
    print("Hello, world!")
my_function()
