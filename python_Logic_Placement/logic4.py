"""
write a python program to replace every nth index character  in  string 
by the given value

input = "Welco To my my python" value="#" nth=3


"""

input_str=input("enter a string")
value=input("enter a character what you want to replace at given index")
output=""
n=int(input("enter nth index to replace value in input string"))
for index,item in enumerate(input_str):
    if index%n==0 and index!=0:
        output+=value
    else:
        output+=item
print(output)
