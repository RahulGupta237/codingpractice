print("*********Lambda Function**Filter*************")

# Filter even numbers from a list using lambda function
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
# Output: [2, 4, 6, 8, 10]

print("*********Lambda Function**Mapping*************")


# Square each number in a list using lambda function
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)
# Output: [1, 4, 9, 16, 25]

print("*********Lambda Function**Reduce*************")


# Find the product of all numbers in a list using lambda function and reduce function
from functools import reduce

nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print(product)
# Output: 120


print("*********Dictionary Lambda Function**Filter*************")


# Create a dictionary of student names and their marks
marks = {'Alice': 80, 'Bob': 60, 'Charlie': 75, 'Dave': 90, 'Eve': 55}

# Filter students with marks greater than or equal to 70 using lambda function
passed_students = dict(filter(lambda x: x[1] >= 70, marks.items()))
print(passed_students)
# Output: {'Alice': 80, 'Charlie': 75, 'Dave': 90}

print("*********Dictionary Lambda Function**Maping*************")

# Create a dictionary of student names and their marks
marks = {'Alice': 80, 'Bob': 60, 'Charlie': 75, 'Dave': 90, 'Eve': 55}

# Map marks to grades using lambda function
grades = dict(map(lambda x: (x[0], 'A' if x[1] >= 80 else 'B' if x[1] >= 70 else 'C' if x[1] >= 60 else 'F'), marks.items()))
print(grades)
# Output: {'Alice': 'A', 'Bob': 'C', 'Charlie': 'B', 'Dave': 'A', 'Eve': 'F'}
print("*********Dictionary Lambda Function**Maping*************")

# Reduce marks to their average using lambda function

from functools import reduce
average_mark = reduce(lambda x, y: x + y, marks.values()) / len(marks)
print(average_mark)
# Output: 72.0


