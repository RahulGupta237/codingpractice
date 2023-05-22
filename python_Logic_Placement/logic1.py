# string="fcaebook.com"
# To count the number of character
# expected output {"f":1,"w":3....}

def number_character(string1):
    i=0
    new={}
    for letter in string1:
        if letter in new:
         new[letter]+=1
        else:
            new[letter]=1
    print(new)
str=input("enter string")
number_character(str)

# 2 nd method
from collections import Counter
newstr=input("enter string")
number_character1=Counter(newstr)
print(number_character1)


