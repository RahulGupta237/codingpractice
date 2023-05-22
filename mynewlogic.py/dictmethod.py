# Example usage
print("*********Dict Methods Keys()********************")
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
print(my_dict.keys())  # Output: dict_keys(['apple', 'banana', 'orange'])


print("*********Dict Methods values()********************")

# Example usage
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
print(my_dict.values())  # Output: dict_values([1, 2, 3])


print("*********Dict Methods items()********************")
# Example usage
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
print(my_dict.items())  # Output: dict_items([('apple', 1), ('banana', 2), ('orange', 3)])

print("*********Dict Methods dict.get(key,default_value)********************")


# Example usage
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
print(my_dict.get('apple'))  # Output: 1
print(my_dict.get('pear'))  # Output: None
print(my_dict.get('pear', 'not found'))  # Output: 'not found'

print("*********Dict Methods dict.pop(key,default_value)********************")



# Example usage
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
print(my_dict.pop('banana'))  # Output: 2
print(my_dict)  # Output: {'apple': 1, 'orange': 3}
print(my_dict.pop('pear', 'not found'))  # Output: 'not found'


print("*********Dict Methods dict.update********************")


# Example usage
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
other_dict = {'pear': 4, 'watermelon': 5}
my_dict.update(other_dict)
print(my_dict)  # Output: {'apple': 1, 'banana': 2, 'orange': 3, 'pear': 4, 'watermelon': 5}

my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
other_dict = {'apple': 4, 'watermelon': 5}
my_dict.update(other_dict)
print(my_dict)  


print("*********Dict Methods dict.fromkeys(iterable, value=None)********************")



# Example usage
fruits = ['apple', 'banana', 'orange']
default_value = 0
fruit_dict = dict.fromkeys(fruits, default_value)
print(fruit_dict)  # Output: {'apple': 0, 'banana': 0, 'orange': 0}

print("*********List to Dictionary conversion ********************")



my_list = ['apple', 'banana', 'orange']
my_dict = dict(zip(my_list, range(len(my_list))))

print(my_dict)
# Output: {'apple': 0, 'banana': 1, 'orange': 2}


print("*********enumerate function with list ********************")


my_list = ['apple', 'banana', 'orange']
my_dict = {str(idx): value for idx, value in enumerate(my_list)}

print(my_dict)
# Output: {'0': 'apple', '1': 'banana', '2': 'orange'}

print("*********enumerate function with dictionary ********************")


my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
for idx, (key, value) in enumerate(my_dict.items()):
    print(idx, key, value)


print("*********=== vs is  ********************")


a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)   # Output: True
print(a == c)   # Output: True

print(a is b)   # Output: True
print(a is c)   # Output: False


print("*********=== vs is  ********************")

my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]

print("*********extend insert  ********************")



my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]



my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # Output: [1, 4, 2, 3]


my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]


my_list = [1, 2, 3]
popped_item = my_list.pop(1)
print(my_list)      # Output: [1, 3]
print(popped_item)  # Output: 2

my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  # Output: 1

my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)  # Output: 2


my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]


my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]



my_string = 'hello, world'
new_string = my_string.replace('hello', 'hi')
print(new_string)  # Output: 'hi, world'


my_string = 'apple,banana,orange'
my_list = my_string.split(',')
print(my_list)  # Output: ['apple', 'banana', 'orange']



my_list = ['apple', 'banana', 'orange']
delimiter = ','
my_string = delimiter.join(my_list)
print(my_string)  # Output: 'apple,banana,orange'


var=10,20,30,40
var2=var,50,60
var3=(100),var2
print(var3)



