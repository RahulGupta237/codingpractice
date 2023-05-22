print("rahul");print("i am here")
import keyword
print(dir(keyword))
print(keyword.kwlist)
print(keyword.softkwlist)
tgr="rahul"
"""hj@=98
67list=[9,78]  illegal varaible  """
x=bin(8)
print(f"binary{x}")
x=bin(5)
print(f"binary{x}")
print(f"here{type(0)}--{0b101}")
print(int("100",2))
str1="rahul"
print(str1)
print(list(str1))
xr=((2,"rahul"),(3,"mypassion"))
print(f"my tuple of order (kry,value) {xr}")
print(f"convert tuple to dictionary {dict(xr)}")
x=dict(xr)
print(list(x.items()))

for k,v in x.items():
    print(x[k])
list3=[(2, 'rahul'), (3, 'mypassion')]

print(dict(set(list3)))
print(ord("a"))
print("string formatting")
x="%s having %s year experience in IT "%("Rahuul","2")
print(x)
import math
print(math.ceil(-100.01))
print(math.ceil(-100))
print(math.ceil(-1))
print(math.ceil(100.01))


str2="rahul"
rs="rahul"
print(str2 is rs)
print(list(str2) is list(rs))
