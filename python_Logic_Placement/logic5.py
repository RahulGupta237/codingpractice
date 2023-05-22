"""
Write a python program to extract the start and end index
of all the element of words
of another list from a given string

input ="welcome to python coding "
check_list=["to":[8,9],"coding":[18,19]]


"""
input_str=input("enter string")
check_list=[x for x in input().split()]
res={}
for ele in check_list:
    if ele in input_str:
        index=input_str.index(ele)
        print(type(index))
        index2=input_str.index(ele[-1],index+1)
        print(((index,index2)))
        res[ele]=[index,index+len(ele)-1]
print(res)
    
