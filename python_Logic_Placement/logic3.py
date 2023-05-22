"""
write a program to get string from given string
where all occurance of first character changed to # except
first charcatrer

input=pythonpy
outputpython#y

"""

str=input("enter a string")
newres1=str.replace(str[0],"#",len(str))
print(newres1)
res=newres1.replace("#",str[0],1)
print(res)