"""

write a python program to extract the index of mid occurence of character


"""

input_str=input("enter a string")
x=input("enter character")
indices=[]
for ind,char in enumerate(input_str):
    if char==x:
        indices.append(ind)
res=indices[(len(indices)//2)]
print(res)