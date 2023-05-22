def dec(num):
    def wrapper(*args, **kwargs):
        print("before modification")
        a = num(*args, **kwargs)  # pass any arguments to the original num function
        new = a + 456
        print("After modification")
        return new
    return wrapper

@dec
def num(x):
    return x

print(num(187))  # Output: before modification
                 #         After modification
                 #         643
