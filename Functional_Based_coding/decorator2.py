def dec1(num):
     def wrapper():
        print("before dec1 modification")
        a1=num()
        new1=a1*2
        print("After dec1 modification")
        return new1
     return wrapper

def dec(num):
    def wrapper():
        print("before modification")
        a=num()
        new=a+456
        print("After modification")
        return new
    return wrapper


@dec
@dec1
def num():
    return 100
print(num())


"""

def num():
    return 100
result=dec(dec1(num))
print(result())


"""
