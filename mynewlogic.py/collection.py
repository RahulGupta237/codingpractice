from collections import Counter,defaultdict

fruits = ['apple', 'banana', 'cherry', 'apple', 'banana', 'apple']
fruit_counts = Counter(fruits)
print(dict(fruit_counts))

print("************Default Dict********************")
word_counts = defaultdict(int)
words = ['apple', 'banana', 'cherry', 'apple', 'banana', 'apple']
for word in words:
    word_counts[word] += 1
print(dict(word_counts))


print("**************Deque****************** ")
from collections import deque

d = deque([1, 2, 3])
d.append(4)
d.appendleft(0)
print(d)



print("**************NamedTuple****************** ")
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'gender'])
p = Person(name='Alice', age=30, gender='female')
print(p)
print(list(p.name))








