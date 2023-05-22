d = {'a': 1, 'b': 2, 'c': 3}

swapped_d = {value: key for key, value in d.items()}

print(swapped_d) # prints {1: 'a', 2: 'b', 3: 'c'}
print("************nested list comprehensive *************")

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

products = [x * y for x in lst1 for y in lst2]

print(products) # prints [4, 5, 6, 8, 10, 12, 12, 15, 18]
products = [x * y for x in lst2 for y in lst1]
print(products)

print("************ comprehensive with multiple condition *************")


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

selected = [x for x in lst if x % 3 == 0 and x > 5]

print(selected) # prints [6, 9]

print("************ complex comprehensive *************")



students = [
    {'name': 'Alice', 'age': 18, 'grades': {'math': 80, 'physics': 70, 'chemistry': 90}},
    {'name': 'Bob', 'age': 20, 'grades': {'math': 90, 'physics': 80, 'chemistry': 70}},
    {'name': 'Charlie', 'age': 19, 'grades': {'math': 70, 'physics': 75, 'chemistry': 80}},
    {'name': 'Dave', 'age': 21, 'grades': {'math': 60, 'physics': 70, 'chemistry': 80}},
    {'name': 'Eve', 'age': 22, 'grades': {'math': 70, 'physics': 70, 'chemistry': 70}},
]

# target = Oldest student with at least 70 in all subjects: Charlie
# Define a list comprehension to filter the students with at least 70 in all subjects
filtered_students = [student for student in students if all(grade >= 70 for grade in student['grades'].values())]

# Define a dict comprehension to get the age of each filtered student
ages = {student['name']: student['age'] for student in filtered_students}

# Find the name of the oldest filtered student
oldest_student_name = max(ages, key=ages.get)

# Print the result
print(f"Oldest student with at least 70 in all subjects: {oldest_student_name}")





print("************ Nested list comprehensive *************")


# Create a list of lists containing even numbers from 0 to 9
even_lists = [[num for num in range(i, i+3) if num % 2 == 0] for i in range(0, 7, 3)]
print(even_lists)
# Output: [[0, 2, 4], [3, 5], [6, 8]]
# here logics is list contain 3 items
even_lists = [[num for num in range(i, i+3) if num % 2 == 0] for i in range(0, 7, 3)]
print(even_lists)



print("************ Nested Dict comprehensive *************")


# Create a dictionary of dictionaries containing the squares of even numbers from 0 to 9
even_squares_dict = {num: {i: i**2 for i in range(num)} for num in range(0, 10, 2)}
print(even_squares_dict)
# Output: {0: {}, 2: {0: 0, 1: 1}, 4: {0: 0, 1: 1, 2: 4, 3: 9}, 6: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}, 8: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}}

