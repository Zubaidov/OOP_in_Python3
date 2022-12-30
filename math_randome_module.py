import math
import random
from collections import Counter

# print(math.pi)
# print(random.randint(0,100))

lst1 = [1,2,3,4,5,6,7,8,9,10]
lst2 = ['Shohruz', 'Shuhrat', 'Ibrahim', 'Shodruz', 'Jamshed', 'Durandesh']

print(random.choice(lst1))
print(random.choice(lst2))

lst2_upr = []
for i in range(20):
    lst2_upr.append(random.choice(lst2))

print(lst2_upr)
print(Counter(lst2_upr))

mylist = list(range(0,20))
print(random.choices(population=mylist, k=10))
print(random.sample(population=mylist, k=10))