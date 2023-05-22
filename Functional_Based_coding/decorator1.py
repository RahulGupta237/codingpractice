def dec(num):
    def wrapper():
        print("before modification")
        a=num()
        new=a+456
        print("After modification")
        return new
    return wrapper
@dec
def num():
    return 100
print(num())

"""

def num():
    return 100

result_new=dec(num)
print(result_new())

"""

