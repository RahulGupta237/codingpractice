"""
write a python program to get first 2 character and last two character
if string less than 2 then get empty string

input= python
output=pyon

"""

str=input("enter string")
len_str=len(str)
res=""
if len_str <2:
    print(res)
else:
    
    res+=str[:2]+str[len_str-2::]
    print(res)
    