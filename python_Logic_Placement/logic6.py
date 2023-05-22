"""

write program to return length of the longest word
 from the list of world

 input = mango apple papaya orange plums banana
 output papaya



"""

input_name=input("enter a name")
words_list=input_name.split()
final_list=[]

for i in words_list:
    final_list.append((len(i),i))

final_list.sort()
print(final_list[-1][1])